import fs from 'fs-extra';
import path from 'path';
import chalk from 'chalk'; // Assuming chalk is available or add it as devDependency
import { fileURLToPath } from 'url';

// Helper to get directory name in ES Module context
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);


// --- Configuration ---
// Paths relative to the project root (one level up from npm/)
const includedFilesAndDirs = [
  '.roo',
  '.ruru/docs/guides',
  '.ruru/docs/standards',
  '.ruru/modes',
  '.ruru/processes',
  '.ruru/templates',
  '.ruru/workflows',
  // '.ruru/scripts', // Exclude scripts from the template itself
  '.roomodes'
];

// Paths relative to the target templates directory (npm/templates/)
const emptyDirsToCreate = [
  '.ruru/archive',
  '.ruru/context',
  '.ruru/decisions',
  '.ruru/logs',
  '.ruru/planning',
  '.ruru/reports', // Note: This was duplicated in your list, keeping one
  '.ruru/snippets',
  '.ruru/tasks',
  '.ruru/mcp-servers',
  '.ruru/repomix',
  '.ruru/sessions',
  '.ruru/temp',
  '.ruru/docs/vertex/answers-direct',
  '.ruru/docs/vertex/answers-web',
  '.ruru/docs/vertex/explanations',
  '.ruru/docs/vertex/reviews',
  '.ruru/docs/notes',
  '.ruru/docs/repomix',
];

// --- Script Logic ---
const projectRoot = path.resolve(__dirname, '..', '..'); // Up two levels from npm/scripts/
const templatesDest = path.resolve(__dirname, '..', 'templates'); // npm/templates/

async function preparePublish() {
  console.log(chalk.blue('Preparing templates for publishing...'));

  try {
    // Ensure the base templates directory exists and is empty
    await fs.emptyDir(templatesDest);
    console.log(chalk.gray(`Ensured empty directory: ${path.relative(projectRoot, templatesDest)}`));

    // Copy included files and directories
    for (const item of includedFilesAndDirs) {
      const sourcePath = path.join(projectRoot, item);
      const destPath = path.join(templatesDest, item);
      if (await fs.pathExists(sourcePath)) {
        await fs.copy(sourcePath, destPath, {
          // Add a filter to exclude node_modules, dist, .git etc. from copied dirs
          filter: (src) => !src.includes('node_modules') && !src.includes('.git') && !src.includes('dist')
        });
        console.log(chalk.green(`Copied: ${item} -> ${path.relative(projectRoot, destPath)}`));
      } else {
        console.log(chalk.yellow(`Warning: Source not found, skipping copy: ${item}`));
      }
    }

    // Create empty directories (ensureDir creates if not exists)
    for (const dir of emptyDirsToCreate) {
      const dirPath = path.join(templatesDest, dir);
      await fs.ensureDir(dirPath);
      // Add a .gitkeep file to ensure directory presence if needed, especially for Git
      await fs.writeFile(path.join(dirPath, '.gitkeep'), '');
      console.log(chalk.green(`Ensured empty directory: ${path.relative(projectRoot, dirPath)}`));
    }

    console.log(chalk.blue.bold('Template preparation complete.'));

  } catch (error) {
    console.error(chalk.red('Error preparing templates:'), error);
    process.exit(1);
  }
}

preparePublish();