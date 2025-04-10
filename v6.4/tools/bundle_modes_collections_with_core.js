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
    
    // Check if we have a "collections" wrapper or direct collections
    if (collectionsDefinition.collections) {
        // We have a "collections" wrapper
        collectionsDefinition = collectionsDefinition.collections;
    }
    
    if (!collectionsDefinition) {
        throw new Error("Invalid collections file format.");
    }
} catch (collectionsError) {
    console.error(`Error reading or parsing collections file ${collectionsPath}:`, collectionsError.message);
    process.exit(1);
}

// --- Get Core Modes ---
const coreModes = [];
const coreModeSlugs = new Set();

if (collectionsDefinition.core && collectionsDefinition.core.modes && Array.isArray(collectionsDefinition.core.modes)) {
    collectionsDefinition.core.modes.forEach(slug => coreModeSlugs.add(slug));
    
    // Find the actual mode objects for core modes
    allModes.forEach(mode => {
        if (coreModeSlugs.has(mode.slug)) {
            coreModes.push(mode);
        }
    });
    
    console.log(`Found ${coreModes.length} core modes.`);
} else {
    console.warn("No 'core' collection found or it has no 'modes' array. Core modes will not be included.");
}

// --- Process Each Collection ---
for (const collectionName in collectionsDefinition) {
    if (collectionsDefinition.hasOwnProperty(collectionName)) {
        console.log(`\nProcessing collection: ${collectionName}`);

        // 1. Get the modes for this collection
        const collection = collectionsDefinition[collectionName];
        if (!collection || !collection.modes || !Array.isArray(collection.modes)) {
            console.warn(`Collection '${collectionName}' has no valid 'modes' array. Skipping.`);
            continue;
        }
        
        const collectionSlugs = new Set(collection.modes);
        if (collectionSlugs.size === 0) {
            console.warn(`Collection '${collectionName}' has zero modes. Skipping.`);
            continue;
        }
        console.log(`  - Found ${collectionSlugs.size} slugs for collection '${collectionName}'.`);

        // 2. Filter modes based on slugs
        let collectionModes = allModes.filter(mode => collectionSlugs.has(mode.slug));
        
        if (collectionModes.length === 0) {
            console.warn(`Collection '${collectionName}' resolved to zero valid modes. Skipping.`);
            continue;
        }

        // 3. Add core modes to this collection (if not already included)
        if (coreModes.length > 0) {
            // Create a set of existing mode slugs in this collection
            const existingModeSlugs = new Set(collectionModes.map(mode => mode.slug));
            
            // Add core modes that aren't already in the collection
            coreModes.forEach(coreMode => {
                if (!existingModeSlugs.has(coreMode.slug)) {
                    collectionModes.push(coreMode);
                }
            });
            
            console.log(`  - Added core modes to collection '${collectionName}'.`);
        }

        // 4. Sort Modes (ensure roo-commander is first)
        collectionModes.sort((a, b) => {
            if (a.slug === 'roo-commander') return -1;
            if (b.slug === 'roo-commander') return 1;
            if (a.slug < b.slug) return -1;
            if (a.slug > b.slug) return 1;
            return 0;
        });
        console.log(`  - Filtered and sorted ${collectionModes.length} modes for collection '${collectionName}'.`);

        // 5. Prepare Final JSON
        const finalJson = {
            customModes: collectionModes
        };

        // 6. Determine Output Path
        const collectionOutputDir = path.join(outputBasePath, collectionName);
        const dynamicOutputFileName = `${collectionName}_modes.json`; // Generate filename like core_modes.json
        const outputPath = path.join(collectionOutputDir, dynamicOutputFileName);

        // 7. Ensure Output Directory Exists
        try {
            fs.mkdirSync(collectionOutputDir, { recursive: true });
        } catch (mkdirError) {
            if (mkdirError.code !== 'EEXIST') {
                console.error(`Error creating output directory ${collectionOutputDir}:`, mkdirError.message);
                continue; // Skip to next collection on error
            }
        }

        // 8. Write Bundled File
        try {
            fs.writeFileSync(outputPath, JSON.stringify(finalJson, null, 2), 'utf8');
            console.log(`  - Successfully wrote bundled modes to: ${outputPath}`);
        } catch (writeError) {
            console.error(`  - Error writing bundled file to ${outputPath}:`, writeError.message);
        }
    }
}

console.log("\nFinished processing all collections.");