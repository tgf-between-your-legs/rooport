#!/usr/bin/env node

const fs = require('fs').promises;
const path = require('path');
const { isBinaryFile } = require('isbinaryfile');
const yargs = require('yargs/yargs');
const { hideBin } = require('yargs/helpers');

// --- Configuration ---
const projectRoot = path.resolve(__dirname, '..'); // Assumes script is in 'scripts' subdir
const oldBaseDirName = '.roo';
const oldSubDirName = 'commander';
const newDirName = '.ruru';
const oldBasePath = path.join(projectRoot, oldBaseDirName);
const oldFullPath = path.join(oldBasePath, oldSubDirName);
const newPath = path.join(projectRoot, newDirName);


const excludedDirs = ['.git', 'node_modules'];
const oldString = '.roo/.commander';
const newString = '.ruru';

// --- Argument Parsing ---
const argv = yargs(hideBin(process.argv))
  .option('dry-run', {
    alias: 'd',
    type: 'boolean',
    description: 'Run script without making any changes to the filesystem',
    default: false,
  })
  .help()
  .alias('help', 'h')
  .argv;

const dryRun = argv.dryRun;

// --- Helper Functions ---
async function pathExists(p) {
  try {
    await fs.access(p);
    return true;
  } catch (error) {
    if (error.code === 'ENOENT') {
      return false;
    }
    throw error; // Re-throw other errors
  }
}

async function renameDirectory(dryRun) {
  console.log(`Checking paths in project root: ${projectRoot}`);
  if (dryRun) {
    console.log('\n*** DRY RUN MODE ENABLED - NO CHANGES WILL BE MADE ***\n');
  }
  const oldFullExists = await pathExists(oldFullPath);
  const newExists = await pathExists(newPath);

  if (!oldFullExists) {
    console.warn(`Warning: Source directory "${oldBaseDirName}/${oldSubDirName}" not found at "${oldFullPath}". Skipping rename.`);
    return false; // Indicate rename didn't happen
  }

  if (newExists) {
    console.error(`Error: Target directory "${newDirName}" already exists at "${newPath}". Aborting rename.`);
    throw new Error(`Target directory "${newDirName}" already exists.`);
  }

  try {
    // --- Directory Rename ---
    if (dryRun) {
        console.log(`[Dry Run] Would rename "${oldBaseDirName}/${oldSubDirName}" at "${oldFullPath}" to "${newDirName}" at "${newPath}"`);
    } else {
        console.log(`Renaming "${oldBaseDirName}/${oldSubDirName}" to "${newDirName}"...`);
        await fs.rename(oldFullPath, newPath);
        console.log(`Successfully renamed directory.`);
    }

    // --- Optional Base Directory Cleanup ---
    try {
        const baseDirExists = await pathExists(oldBasePath);
        if (baseDirExists) {
            const baseDirEntries = await fs.readdir(oldBasePath);
            if (baseDirEntries.length === 0) {
                if (dryRun) {
                    console.log(`[Dry Run] Would remove now empty base directory "${oldBaseDirName}" at "${oldBasePath}"`);
                } else {
                    console.log(`Removing now empty base directory "${oldBaseDirName}"...`);
                    await fs.rmdir(oldBasePath);
                }
            } else {
                console.log(`Base directory "${oldBaseDirName}" still contains other items, not removing.`);
            }
        }
    } catch (cleanupError) {
        console.warn(`Warning: Could not check or remove base directory "${oldBaseDirName}". Error: ${cleanupError.message}`);
    }

    return true; // Indicate rename would/did happen
  } catch (error) {
    console.error(`Error during directory rename/cleanup: ${error.message}`);
    throw error;
  }
}

async function replaceInFile(filePath, dryRun) {
  const relativeFilePath = path.relative(projectRoot, filePath);
  try {
    const stats = await fs.stat(filePath);
    if (!stats.isFile()) {
      return 0; // Not a file
    }

    // --- Binary File Check ---
    const fileBuffer = await fs.readFile(filePath); // Read as buffer first
    if (await isBinaryFile(fileBuffer, stats.size)) {
        console.log(`Skipping binary file: ${relativeFilePath}`);
        return 0;
    }

    // --- Read Text Content ---
    const content = fileBuffer.toString('utf8'); // Convert buffer to string

    // --- Perform Replacement ---
    let replacementsMade = 0;
    const searchRegex = new RegExp(oldString.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'g');
    const newContent = content.replace(searchRegex, (match) => {
      replacementsMade++;
      return newString;
    });

    // --- Write Changes (or Log in Dry Run) ---
    if (replacementsMade > 0) {
       if (dryRun) {
        console.log(`[Dry Run] Would replace ${replacementsMade} occurrence(s) in: ${relativeFilePath}`);
      } else {
        await fs.writeFile(filePath, newContent, 'utf8');
        console.log(`Replaced ${replacementsMade} occurrence(s) in: ${relativeFilePath}`);
      }
      return replacementsMade;
    }
    return 0; // No replacements needed
  } catch (error) {
    console.error(`Error processing file "${relativeFilePath}": ${error.message}`);
    return 0; // Indicate error
  }
}

async function processDirectory(dirPath, dryRun) {
  let totalReplacements = 0;
  try {
     // Ensure we don't try to read the old directory if it was just renamed/removed
    if (!dryRun && dirPath === oldFullPath) {
        console.log(`Skipping processing of old directory path after rename: ${path.relative(projectRoot, dirPath)}`);
        return 0;
    }
     if (!dryRun && dirPath === oldBasePath) {
        // Check if it still exists before trying to read
        const exists = await pathExists(dirPath);
        if (!exists) {
             console.log(`Skipping processing of removed base directory path: ${path.relative(projectRoot, dirPath)}`);
             return 0;
        }
    }

    const entries = await fs.readdir(dirPath, { withFileTypes: true });

    for (const entry of entries) {
      const currentPath = path.join(dirPath, entry.name);
      const relativePath = path.relative(projectRoot, currentPath);

      // Skip the directory being renamed FROM if it somehow still exists during traversal
      if (currentPath === oldFullPath) {
          console.log(`Skipping the source directory itself during content scan: ${relativePath}`);
          continue;
      }

      if (excludedDirs.includes(entry.name)) {
        console.log(`Skipping excluded directory: ${relativePath}`);
        continue;
      }

      if (entry.isDirectory()) {
        totalReplacements += await processDirectory(currentPath, dryRun);
      } else if (entry.isFile()) {
        totalReplacements += await replaceInFile(currentPath, dryRun);
      }
    }
  } catch (error) {
     if (error.code === 'ENOENT') {
        // If the directory doesn't exist (e.g., the old one after rename), skip quietly.
        console.log(`Directory not found (likely renamed or excluded), skipping: ${path.relative(projectRoot, dirPath)}`);
     } else {
        console.error(`Error reading directory "${path.relative(projectRoot, dirPath)}": ${error.message}`);
        // Decide if you want to stop or continue, maybe throw?
     }
  }
  return totalReplacements;
}

async function main(dryRun) {
  console.log('Starting reverse refactor: .roo/.commander -> .ruru');
   if (dryRun) {
    console.log('\n*** DRY RUN MODE ENABLED - NO CHANGES WILL BE MADE ***\n');
  }

  let renameAttempted = false;
  try {
    renameAttempted = await renameDirectory(dryRun); // Pass dryRun flag
  } catch (error) {
    console.error('Failed during directory rename check/attempt. Aborting further processing.');
    process.exit(1);
  }

  // Only proceed with content replacement if rename was successful or skipped
  if (renameAttempted) {
      console.log('\nStarting file content replacement scan...');
      try {
        const totalReplacements = await processDirectory(projectRoot, dryRun); // Pass dryRun flag
        console.log(`\nFinished processing files.`);
         if (dryRun) {
            console.log(`[Dry Run] Would have made approximately ${totalReplacements} replacements in files.`);
        } else {
            console.log(`Total replacements made in files: ${totalReplacements}`);
        }
        console.log(`Reverse refactor script completed ${dryRun ? '(Dry Run)' : ''}.`);
      } catch (error) {
        console.error(`An error occurred during file processing: ${error.message}`);
        process.exit(1);
      }
  } else {
       console.log('Directory rename failed or aborted, skipping file content replacement.');
       process.exit(1); // Exit if rename failed critically
  }
}

main(dryRun).catch(error => { // Pass dryRun to main
  console.error(`Unhandled error in main function: ${error.message}`);
    process.exit(1);
});