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
const outputDir = getArgValue('--outputDir', '.');
const outputFile = getArgValue('--outputFile', 'bundled_modes.json');

const sourcePath = path.resolve(sourceDir);
const outputPath = path.resolve(outputDir, outputFile);

console.log(`Reading mode files from: ${sourcePath}`);

// --- Read and Parse Modes ---
let modes = [];
try {
    const files = fs.readdirSync(sourcePath);
    files.forEach(file => {
        if (path.extname(file).toLowerCase() === '.json') {
            const filePath = path.join(sourcePath, file);
            try {
                const fileContent = fs.readFileSync(filePath, 'utf8');
                const mode = JSON.parse(fileContent);
                if (mode && mode.slug) { // Basic validation
                    modes.push(mode);
                } else {
                    console.warn(`Skipping file ${file}: Missing or invalid 'slug' property.`);
                }
            } catch (parseError) {
                console.error(`Error reading or parsing file ${file}:`, parseError.message);
                // Optionally exit on error: process.exit(1);
            }
        }
    });
} catch (readDirError) {
    console.error(`Error reading source directory ${sourcePath}:`, readDirError.message);
    process.exit(1);
}

console.log(`Found ${modes.length} modes.`);

// --- Sort Modes ---
modes.sort((a, b) => {
    // Prioritize 'roo-commander'
    if (a.slug === 'roo-commander') return -1;
    if (b.slug === 'roo-commander') return 1;

    // Sort the rest alphabetically by slug
    if (a.slug < b.slug) return -1;
    if (a.slug > b.slug) return 1;
    return 0;
});

// --- Prepare Final JSON ---
const finalJson = {
    customModes: modes
};

// --- Ensure Output Directory Exists ---
try {
    fs.mkdirSync(path.dirname(outputPath), { recursive: true });
} catch (mkdirError) {
    if (mkdirError.code !== 'EEXIST') { // Ignore if directory already exists
        console.error(`Error creating output directory ${path.dirname(outputPath)}:`, mkdirError.message);
        process.exit(1);
    }
}

// --- Write Bundled File ---
try {
    fs.writeFileSync(outputPath, JSON.stringify(finalJson, null, 2), 'utf8');
    console.log(`Successfully wrote bundled modes to: ${outputPath}`);
} catch (writeError) {
    console.error(`Error writing bundled file to ${outputPath}:`, writeError.message);
    process.exit(1);
}