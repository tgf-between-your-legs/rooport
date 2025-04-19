const fs = require('fs').promises;
const path = require('path');
const yaml = require('js-yaml');

const MODES_DIR = path.join(__dirname, '..', 'v7.0', 'modes');
const ROOMODES_PATH = path.join(__dirname, '..', '.roomodes');
const MODE_FILE_PATTERN = /\.mode\.md$/;

const LEVEL_SORT_ORDER = [
    '00x-executive',
    '01x-director',
    '02x-lead',
    '03x-worker',
    '04x-assistant',
    '05x-footgun',
    // Add any other potential levels here in desired sort order
];

/**
 * Recursively finds all files matching a pattern in a directory.
 * @param {string} dirPath - The directory to search.
 * @param {RegExp} pattern - The regex pattern to match filenames against.
 * @returns {Promise<string[]>} - A promise that resolves to an array of matching file paths.
 */
async function findFilesRecursive(dirPath, pattern) {
    let results = [];
    try {
        const entries = await fs.readdir(dirPath, { withFileTypes: true });
        for (const entry of entries) {
            const fullPath = path.join(dirPath, entry.name);
            if (entry.isDirectory()) {
                results = results.concat(await findFilesRecursive(fullPath, pattern));
            } else if (pattern.test(entry.name)) {
                results.push(fullPath);
            }
        }
    } catch (error) {
        console.error(`Error reading directory ${dirPath}:`, error);
        // Decide if you want to throw or just log and continue
    }
    return results;
}

/**
 * Parses the content of a .mode.md file.
 * @param {string} filePath - Path to the mode file.
 * @returns {Promise<object|null>} - A promise resolving to the parsed mode object or null if parsing fails.
 */
async function parseModeFile(filePath) {
    try {
        const content = await fs.readFile(filePath, 'utf-8');

        // Find YAML frontmatter ONLY at the beginning
        const frontmatterRegex = /^---\s*([\s\S]*?)\s*---/;
        const match = content.match(frontmatterRegex);

        if (!match || !match[1]) {
            console.warn(`Skipping ${filePath}: No valid YAML frontmatter found at the beginning of the file.`);
            return null;
        }

        const frontmatterContent = match[1];
        const markdownContent = content.substring(match[0].length).trim(); // Content after the frontmatter

        let frontmatter;
        try {
            frontmatter = yaml.load(frontmatterContent);
        } catch (yamlError) {
             console.warn(`Skipping ${filePath}: Error parsing YAML frontmatter: ${yamlError.message}`);
             return null;
        }


        // Validate required frontmatter fields
        if (!frontmatter || typeof frontmatter !== 'object' || !frontmatter.slug || !frontmatter.name || !frontmatter.level) {
            console.warn(`Skipping ${filePath}: Missing or invalid 'slug', 'name', or 'level' in frontmatter.`);
            return null;
        }
        const level = frontmatter.level; // Extract level from frontmatter

        // Extract Role Definition
        const roleDefMatch = markdownContent.match(/##\s+Role Definition\s*\n([\s\S]*?)(?=\n##\s+|$)/);
        const roleDefinition = roleDefMatch ? roleDefMatch[1].trim() : '';
        if (!roleDefinition) {
             console.warn(`Skipping ${filePath}: Could not find '## Role Definition' section.`);
             return null; // Or handle as needed - maybe allow empty roleDefinition?
        }

        // Extract Metadata section
        const metadataMatch = markdownContent.match(/##\s+Metadata\s*\n([\s\S]*?)(?=\n##\s+|$)/);
        const metadataContent = metadataMatch ? metadataMatch[1].trim() : ''; // Trim the captured metadata

        // Level is now extracted from frontmatter above

        // Extract Tool Groups from Metadata section
        // Match "Tool Groups:", then capture everything until the next line starting with ** or the end of the string
        const groupsSectionMatch = metadataContent.match(/\*\*Tool Groups:\*\*\s*\n([\s\S]*?)(?=\n\*\*|$)/);
        let groupsListText = '';
        if (groupsSectionMatch && groupsSectionMatch[1]) {
            groupsListText = groupsSectionMatch[1];
        }
        let groups = [];
        if (groupsListText) {
            const groupsLines = groupsListText.split('\n');
            groups = groupsLines
                .map(item => item.trim())
                .filter(item => item.startsWith('- ')) // Ensure it's a list item
                .map(item => item.substring(2).trim()) // Remove '- '
                .filter(Boolean) // Remove empty items
                .map(itemString => {
                    try {
                        // Attempt to parse as JSON (for complex format)
                        // Need to be careful with JSON parsing, ensure valid JSON structure in .mode.md
                        // Example: - ["group1", {"fileRegex": "\\.js$", "description": "JS Files"}]
                        // Example: - group2
                        // Let's try a simple heuristic: if it starts with [ or {, try parsing
                        if (itemString.startsWith('[') || itemString.startsWith('{')) {
                            return JSON.parse(itemString);
                        }
                        // Otherwise, treat as a simple string
                        return itemString;
                    } catch (parseError) {
                        console.warn(`Warning for ${filePath}: Could not parse Tool Group item as JSON: "${itemString}". Treating as simple string. Error: ${parseError.message}`);
                        // Fallback to treating as a simple string if JSON parse fails
                        return itemString;
                    }
                });
        }
        // No warning needed if groups array is empty, it's a valid state.


        return {
            slug: frontmatter.slug,
            name: frontmatter.name,
            roleDefinition: roleDefinition,
            groups: groups, // Parsed groups (can be strings or complex arrays/objects)
            level: level, // Extracted from frontmatter
        };

    } catch (error) {
        console.error(`Error parsing file ${filePath}:`, error);
        return null;
    }
}

/**
 * Finds the sort index for a given level string based on LEVEL_SORT_ORDER prefixes.
 * It checks if the level string starts with any of the defined prefixes.
 * @param {string} level - The level string (e.g., "031-worker-frontend", "05x-footgun").
 * @returns {number} - The sort index or Infinity if no match found.
 */
function getLevelSortIndex(level) {
    if (!level || typeof level !== 'string') return Infinity;

    const trimmedLevel = level.trim();
    // Extract the initial numeric part (e.g., '03') from the level string
    const levelNumMatch = trimmedLevel.match(/^(\d{2})/);
    if (!levelNumMatch) {
        console.warn(`Could not extract numeric prefix (e.g., '03') from level "${trimmedLevel}". Placing at end.`);
        return Infinity;
    }
    const levelNum = levelNumMatch[1]; // e.g., '03'

    // Iterate through the defined sort order prefixes in LEVEL_SORT_ORDER
    for (let i = 0; i < LEVEL_SORT_ORDER.length; i++) {
        const orderPrefix = LEVEL_SORT_ORDER[i]; // e.g., '03x-worker'
        const trimmedOrderPrefix = typeof orderPrefix === 'string' ? orderPrefix.trim() : '';

        // Extract the initial numeric part from the orderPrefix string
        const orderNumMatch = trimmedOrderPrefix.match(/^(\d{2})/);
        if (!orderNumMatch) continue; // Skip invalid entries in LEVEL_SORT_ORDER
        const orderNum = orderNumMatch[1];

        // Compare the extracted numeric prefixes
        if (levelNum === orderNum) {
             return i; // Return the index of the matching category prefix
        }
    }

    // If no prefix matched after checking all entries in LEVEL_SORT_ORDER
    console.warn(`Level "${trimmedLevel}" (numeric prefix "${levelNum}") does not match any numeric prefix category in LEVEL_SORT_ORDER. Placing at end.`);
    return Infinity; // Not found, place at the end
}


/**
 * Custom sort function for mode objects.
 * Sorts by:
 * 1. 'roo-commander' first.
 * 2. Level prefix based on LEVEL_SORT_ORDER.
 * 3. Alphabetically by slug within the same level.
 * @param {object} a - First mode object.
 * @param {object} b - Second mode object.
 * @returns {number} - Sort order indicator.
 */
function sortModes(a, b) {
    // Rule 1: roo-commander always first
    if (a.slug === 'roo-commander') return -1;
    if (b.slug === 'roo-commander') return 1;

    // Rule 2: Sort by level based on predefined order prefix
    const levelAIndex = getLevelSortIndex(a.level);
    const levelBIndex = getLevelSortIndex(b.level);

    if (levelAIndex !== levelBIndex) {
        return levelAIndex - levelBIndex;
    }

    // Rule 3: Within the same effective level, sort alphabetically by slug
    return a.slug.localeCompare(b.slug);
}


/**
 * Main function to populate .roomodes.
 */
async function populateRoomodes() {
    console.log(`Starting mode population from ${MODES_DIR}...`);

    const modeFiles = await findFilesRecursive(MODES_DIR, MODE_FILE_PATTERN);
    console.log(`Found ${modeFiles.length} potential mode files.`);

    const parsedModes = [];
    for (const filePath of modeFiles) {
        const modeData = await parseModeFile(filePath);
        if (modeData) {
            parsedModes.push(modeData);
        }
    }
    console.log(`Successfully parsed ${parsedModes.length} modes.`);

    if (parsedModes.length === 0) {
        console.error("No modes were successfully parsed. Aborting update.");
        return;
    }

    // Sort the modes
    parsedModes.sort(sortModes);
    console.log("Modes sorted.");
    // console.log("Sorted slugs:", parsedModes.map(m => `${m.level} - ${m.slug}`)); // For debugging sort order

    try {
        // Read existing .roomodes
        let roomodesData = {};
        try {
            const existingContent = await fs.readFile(ROOMODES_PATH, 'utf-8');
            roomodesData = JSON.parse(existingContent);
            console.log(`Read existing .roomodes file.`);
        } catch (readError) {
            if (readError.code === 'ENOENT') {
                console.log(`.roomodes file not found, will create a new one.`);
            } else {
                throw readError; // Rethrow other read errors
            }
        }


        // Update the customModes key
        roomodesData.customModes = parsedModes;
        console.log(`Updated 'customModes' key.`);

        // Write the updated data back
        const outputJson = JSON.stringify(roomodesData, null, 2); // Pretty print
        await fs.writeFile(ROOMODES_PATH, outputJson, 'utf-8');
        console.log(`Successfully updated ${ROOMODES_PATH}`);

    } catch (error) {
        console.error(`Error updating ${ROOMODES_PATH}:`, error);
    }
}

// Run the main function
populateRoomodes().catch(error => {
    console.error("An unexpected error occurred:", error);
    process.exit(1);
});