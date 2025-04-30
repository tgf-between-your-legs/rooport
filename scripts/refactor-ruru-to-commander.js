#!/usr/bin/env node

const fs = require('fs').promises;
const path = require('path');
const { isBinaryFile } = require('isbinaryfile');
const yargs = require('yargs/yargs');
const { hideBin } = require('yargs/helpers');

// --- Configuration ---
const projectRoot = path.resolve(__dirname, '..'); // Assumes script is in 'scripts' subdir
const oldDirName = '.ruru';
const newBaseDirName = '.roo';
const newSubDirName = 'commander';
const oldPath = path.join(projectRoot, oldDirName);
const newBasePath = path.join(projectRoot, newBaseDirName);
const newFullPath = path.join(newBasePath, newSubDirName);

const excludedDirs = ['.git', 'node_modules'];
const oldString = '.ruru';
const newString = '.roo/.commander';

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
  const oldExists = await pathExists(oldPath);
  const newBaseExists = await pathExists(newBasePath);
  const newFullExists = await pathExists(newFullPath);

  if (!oldExists) {
    console.warn(`Warning: Source directory "${oldDirName}" not found at "${oldPath}". Skipping rename.`);
    return false; // Indicate rename didn't happen
  }

  if (newFullExists) {
    console.error(`Error: Target directory "${newBaseDirName}/${newSubDirName}" already exists at "${newFullPath}". Aborting rename.`);
    throw new Error(`Target directory "${newBaseDirName}/${newSubDirName}" already exists.`);
  }

  try {
    // --- Base Directory Creation ---
    if (!newBaseExists) {
      if (dryRun) {
        console.log(`[Dry Run] Would create base directory "${newBaseDirName}" at "${newBasePath}"`);
      } else {
        console.log(`Creating base directory "${newBaseDirName}" at "${newBasePath}"...`);
        await fs.mkdir(newBasePath);
      }
    } else {
       console.log(`Base directory "${newBaseDirName}" already exists.`);
    }

    // --- Directory Rename ---
    if (dryRun) {
        console.log(`[Dry Run] Would rename "${oldDirName}" at "${oldPath}" to "${newBaseDirName}/${newSubDirName}" at "${newFullPath}"`);
    } else {
        console.log(`Renaming "${oldDirName}" to "${newBaseDirName}/${newSubDirName}"...`);
        await fs.rename(oldPath, newFullPath);
        console.log(`Successfully renamed directory.`);
    }
    return true; // Indicate rename would/did happen
  } catch (error) {
    console.error(`Error during directory rename/creation: ${error.message}`);
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
    // Ensure we don't try to read the old directory if it was just renamed
    if (!dryRun && dirPath === oldPath) {
        console.log(`Skipping processing of old directory path after rename: ${path.relative(projectRoot, dirPath)}`);
        return 0;
    }

    const entries = await fs.readdir(dirPath, { withFileTypes: true });

    for (const entry of entries) {
      const currentPath = path.join(dirPath, entry.name);
      const relativePath = path.relative(projectRoot, currentPath);

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
  console.log('Starting refactor: .ruru -> .roo/.commander');
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

  // Only proceed with content replacement if rename was successful or skipped (dir didn't exist)
  // In dry run, renameAttempted will be true if it *would* have renamed or skipped.
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
        console.log(`Refactor script completed ${dryRun ? '(Dry Run)' : ''}.`);
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