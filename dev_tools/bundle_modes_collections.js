const fs = require('fs');
const path = require('path');

// --- Argument Parsing ---
function getArgValue(argName, defaultValue) {
    const argIndex = process.argv.indexOf(argName);
    if (argIndex !== -1 && process.argv.length > argIndex + 1) {
        return process.argv[argIndex + 1];
    }
    return defaultValue;
}

const sourceDir = getArgValue('--source', 'roo-modes-dev');
const collectionsFile = getArgValue('--collections', 'dev_tools/mode_collections.json');
const outputBaseDir = getArgValue('--outputBaseDir', '.'); // Base directory for versioned output (e.g., 'v6.0')
const outputFileName = getArgValue('--outputFile', 'modes.json'); // Name of the output file within each collection dir

const sourcePath = path.resolve(sourceDir);
const collectionsPath = path.resolve(collectionsFile);
const outputBasePath = path.resolve(outputBaseDir);

console.log(`Reading mode files from: ${sourcePath}`);
console.log(`Reading collections definition from: ${collectionsPath}`);
console.log(`Outputting collection bundles to base directory: ${outputBasePath}`);

// --- Read and Parse All Modes ---
let allModes = [];
let allModeSlugs = new Set();
try {
    const files = fs.readdirSync(sourcePath);
    files.forEach(file => {
        if (path.extname(file).toLowerCase() === '.json') {
            const filePath = path.join(sourcePath, file);
            try {
                const fileContent = fs.readFileSync(filePath, 'utf8');
                const mode = JSON.parse(fileContent);
                if (mode && mode.slug) { // Basic validation
                    allModes.push(mode);
                    allModeSlugs.add(mode.slug);
                } else {
                    console.warn(`Skipping file ${file}: Missing or invalid 'slug' property.`);
                }
            } catch (parseError) {
                console.error(`Error reading or parsing file ${file}:`, parseError.message);
            }
        }
    });
} catch (readDirError) {
    console.error(`Error reading source directory ${sourcePath}:`, readDirError.message);
    process.exit(1);
}
console.log(`Found ${allModes.length} total modes.`);

// --- Read Collections Definition ---
let collectionsDefinition;
try {
    const collectionsContent = fs.readFileSync(collectionsPath, 'utf8');
    collectionsDefinition = JSON.parse(collectionsContent);
    if (!collectionsDefinition || !collectionsDefinition.collections) {
        throw new Error("Invalid collections file format. Missing 'collections' property.");
    }
} catch (collectionsError) {
    console.error(`Error reading or parsing collections file ${collectionsPath}:`, collectionsError.message);
    process.exit(1);
}

// --- Helper Function to Resolve Collection Slugs ---
function resolveCollectionSlugs(collectionName, collectionsDef, allSlugs) {
    const definition = collectionsDef.collections[collectionName];
    if (!definition) {
        console.warn(`Collection '${collectionName}' not found in definitions.`);
        return new Set();
    }

    let resolvedSlugs = new Set();

    if (Array.isArray(definition)) {
        // Simple list of slugs
        definition.forEach(slug => resolvedSlugs.add(slug));
    } else if (typeof definition === 'object') {
        // Complex definition with include/add
        if (definition.include) {
            definition.include.forEach(includeName => {
                if (includeName === 'all') {
                    allSlugs.forEach(slug => resolvedSlugs.add(slug));
                } else {
                    const includedSlugs = resolveCollectionSlugs(includeName, collectionsDef, allSlugs);
                    includedSlugs.forEach(slug => resolvedSlugs.add(slug));
                }
            });
        }
        if (definition.add) {
            definition.add.forEach(slug => resolvedSlugs.add(slug));
        }
    }

    return resolvedSlugs;
}

// --- Process Each Collection ---
const collections = collectionsDefinition.collections;
for (const collectionName in collections) {
    if (collections.hasOwnProperty(collectionName)) {
        console.log(`\nProcessing collection: ${collectionName}`);

        // 1. Resolve slugs for this collection
        const collectionSlugs = resolveCollectionSlugs(collectionName, collectionsDefinition, allModeSlugs);
        if (collectionSlugs.size === 0) {
            console.warn(`Collection '${collectionName}' resolved to zero modes. Skipping.`);
            continue;
        }
        console.log(`  - Resolved ${collectionSlugs.size} slugs for collection '${collectionName}'.`);


        // 2. Filter modes based on resolved slugs
        let collectionModes = allModes.filter(mode => collectionSlugs.has(mode.slug));

        // 3. Sort Modes
        collectionModes.sort((a, b) => {
            if (a.slug === 'roo-commander') return -1;
            if (b.slug === 'roo-commander') return 1;
            if (a.slug < b.slug) return -1;
            if (a.slug > b.slug) return 1;
            return 0;
        });
        console.log(`  - Filtered and sorted ${collectionModes.length} modes for collection '${collectionName}'.`);


        // 4. Prepare Final JSON
        const finalJson = {
            customModes: collectionModes
        };

        // 5. Determine Output Path
        const collectionOutputDir = path.join(outputBasePath, collectionName);
        const dynamicOutputFileName = `${collectionName}_modes.json`; // Generate filename like core_modes.json
        const outputPath = path.join(collectionOutputDir, dynamicOutputFileName);

        // 6. Ensure Output Directory Exists
        try {
            fs.mkdirSync(collectionOutputDir, { recursive: true });
        } catch (mkdirError) {
            if (mkdirError.code !== 'EEXIST') {
                console.error(`Error creating output directory ${collectionOutputDir}:`, mkdirError.message);
                continue; // Skip to next collection on error
            }
        }

        // 7. Write Bundled File
        try {
            fs.writeFileSync(outputPath, JSON.stringify(finalJson, null, 2), 'utf8');
            console.log(`  - Successfully wrote bundled modes to: ${outputPath}`);
        } catch (writeError) {
            console.error(`  - Error writing bundled file to ${outputPath}:`, writeError.message);
        }
    }
}

console.log("\nFinished processing all collections.");