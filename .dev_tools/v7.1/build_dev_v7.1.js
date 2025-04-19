const fs = require('fs');
const path = require('path');
const TOML = require('@iarna/toml');

const modesSourceDir = path.join(__dirname, '..', '..', 'v7.1', 'modes');
const rulesTargetRootDir = path.join(__dirname, '..', '..', '.roo');
const roomodesFilePath = path.join(__dirname, '..', '..', '.roomodes');

// --- Helper Functions ---

// Function to recursively find all .mode.md files
function findModeFiles(dir, fileList = []) {
    const files = fs.readdirSync(dir);
    files.forEach(file => {
        const filePath = path.join(dir, file);
        const stat = fs.statSync(filePath);
        if (stat.isDirectory()) {
            findModeFiles(filePath, fileList);
        } else if (file.endsWith('.mode.md')) {
            fileList.push(filePath);
        }
    });
    return fileList;
}

// Function to extract TOML frontmatter
function extractToml(content) {
    const match = content.match(/^\+\+\+([\s\S]*?)\+\+\+/);
    return match ? match[1] : null;
}

// Function to copy directory recursively (Node.js 16.7.0+)
function copyDirRecursive(src, dest) {
    fs.mkdirSync(dest, { recursive: true });
    const entries = fs.readdirSync(src, { withFileTypes: true });

    for (let entry of entries) {
        const srcPath = path.join(src, entry.name);
        const destPath = path.join(dest, entry.name);

        if (entry.isDirectory()) {
            copyDirRecursive(srcPath, destPath);
        } else {
            fs.copyFileSync(srcPath, destPath);
        }
    }
}

// --- Main Build Logic ---
try {
    console.log(`Starting dev build process for v7.1 modes...`);
    console.log(`Source modes directory: ${modesSourceDir}`);
    console.log(`Target rules root directory: ${rulesTargetRootDir}`);
    console.log(`Target .roomodes file: ${roomodesFilePath}`);

    const modeFiles = findModeFiles(modesSourceDir);
    console.log(`\nFound ${modeFiles.length} potential mode files.`);

    const roomodesArray = [];
    let processedCount = 0;
    let errorCount = 0;

    modeFiles.forEach(filePath => {
        const modeFileName = path.basename(filePath);
        const modeDir = path.dirname(filePath);
        const modeId = modeFileName.replace('.mode.md', '');
        const targetRulesDir = path.join(rulesTargetRootDir, `rules-${modeId}`);

        console.log(`\nProcessing: ${modeFileName} (ID: ${modeId})`);

        try {
            // 1. Read and Parse TOML
            const content = fs.readFileSync(filePath, 'utf8');
            const tomlString = extractToml(content);
            if (!tomlString) {
                console.warn(`  WARN: No TOML frontmatter found. Skipping.`);
                return; // Skip this file
            }
            const data = TOML.parse(tomlString);

            // 2. Validate required fields for .roomodes
            if (!data.id || !data.name || !data.system_prompt) {
                console.warn(`  WARN: Missing required fields (id, name, system_prompt) in TOML. Skipping.`);
                return; // Skip this file
            }
            if (data.id !== modeId) {
                 console.warn(`  WARN: TOML id "${data.id}" does not match filename id "${modeId}". Skipping.`);
                 return; // Skip this file
            }

            // 3. Prepare .roomodes entry
            const roomodeEntry = {
                slug: data.id,
                name: data.name,
                roleDefinition: data.system_prompt.trim(),
                groups: ["read", "edit", "browser", "command", "mcp"], // Permissive for dev
                // fileRestrictions: Omitted for dev
                // customInstructions: Omitted
                // model: Omitted
            };
            roomodesArray.push(roomodeEntry);
            console.log(`  Added entry to .roomodes.`);

            // 4. Handle .roo/rules-[id] directory
            console.log(`  Ensuring target rules directory: ${targetRulesDir}`);
            // Clean up existing directory
            if (fs.existsSync(targetRulesDir)) {
                fs.rmSync(targetRulesDir, { recursive: true, force: true });
                console.log(`    Removed existing target directory.`);
            }
            // Create fresh directory
            fs.mkdirSync(targetRulesDir, { recursive: true });
            console.log(`    Created target directory.`);

            // 5. Copy/Create subdirectories (context, custom-instructions, examples) - DISABLED
            // const subDirsToProcess = ['context', 'custom-instructions', 'examples'];
            // subDirsToProcess.forEach(subDir => {
            //     const sourceSubDirPath = path.join(modeDir, subDir);
            //     const targetSubDirPath = path.join(targetRulesDir, subDir);
            //
            //     if (fs.existsSync(sourceSubDirPath)) {
            //         console.log(`    Copying source directory: ${sourceSubDirPath}`);
            //         copyDirRecursive(sourceSubDirPath, targetSubDirPath);
            //         console.log(`      Copied to: ${targetSubDirPath}`);
            //     } else {
            //         console.log(`    Source directory missing, creating empty target: ${targetSubDirPath}`);
            //         fs.mkdirSync(targetSubDirPath, { recursive: true });
            //     }
            // });

            processedCount++; // Moved increment here as it was inside the loop before

        } catch (err) {
            console.error(`  ERROR processing ${modeFileName}: ${err.message}`);
            errorCount++;
        }
    });

    // 6. Write .roomodes file
    try {
        // Wrap the array in the desired object structure
        const outputObject = { customModes: roomodesArray };
        fs.writeFileSync(roomodesFilePath, JSON.stringify(outputObject, null, 2));
        console.log(`\nSuccessfully wrote ${roomodesArray.length} modes to ${roomodesFilePath} (wrapped in customModes object)`);
    } catch (writeErr) {
        console.error(`\nFATAL ERROR writing ${roomodesFilePath}: ${writeErr.message}`);
        process.exit(1);
    }

    console.log(`\nBuild process finished.`);
    console.log(`Successfully processed: ${processedCount} modes.`);
    console.log(`Skipped/Errors: ${modeFiles.length - processedCount}`);

    if (errorCount > 0) {
        console.warn(`\nWARNING: Encountered ${errorCount} errors during processing. Check logs above.`);
    }

} catch (error) {
    console.error(`\nFATAL ERROR during build process: ${error.message}`);
    process.exit(1);
}