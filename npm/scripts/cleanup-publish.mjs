import fs from 'fs-extra';
import path from 'path';
import chalk from 'chalk';
import { fileURLToPath } from 'url';

// Helper to get directory name in ES Module context
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// --- Configuration ---
// These should match the top-level items copied by prepare-publish.js
const itemsToRemove = [
  '.roo',
  '.ruru',
  '.roomodes'
];

// --- Script Logic ---
const projectRoot = path.resolve(__dirname, '..', '..'); // Up two levels from npm/scripts/
const templatesDest = path.resolve(__dirname, '..', 'templates'); // npm/templates/

async function cleanupPublish() {
  console.log(chalk.blue('Cleaning up templates after publishing...'));

  try {
    for (const item of itemsToRemove) {
      const destPath = path.join(templatesDest, item);
      if (await fs.pathExists(destPath)) {
        await fs.remove(destPath);
        console.log(chalk.gray(`Removed: ${path.relative(projectRoot, destPath)}`));
      }
    }

    // Optionally, recreate placeholder files if you want them present in source control
    // await fs.ensureDir(path.join(templatesDest, '.roo'));
    // await fs.writeFile(path.join(templatesDest, '.roo', 'placeholder.txt'), 'Templates are copied here during publish');
    // await fs.ensureDir(path.join(templatesDest, '.ruru'));
    // await fs.writeFile(path.join(templatesDest, '.ruru', 'placeholder.txt'), 'Templates are copied here during publish');


    console.log(chalk.blue.bold('Template cleanup complete.'));

  } catch (error) {
    console.error(chalk.red('Error cleaning up templates:'), error);
    // Don't exit with error code, as publish was successful
  }
}

cleanupPublish();