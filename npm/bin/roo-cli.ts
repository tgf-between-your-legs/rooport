#!/usr/bin/env node
import { Command } from 'commander';
// Import chalk and inquirer if needed later
// import chalk from 'chalk';
// import inquirer from 'inquirer';
import pkg from '../package.json' with { type: 'json' }; // Path relative to cli/bin/
import { handleInitCommand } from '../src/commands/init.js'; // Import from TS source (NodeNext needs .js)
import { handleInstallMcpCommand } from '../src/commands/install-mcp.js'; // Import the new command handler

const program = new Command();

program
  .version(pkg.version)
  .description(pkg.description);

program
  .command('init')
  .description('Initialize Roo configuration in the current directory')
  .action(handleInitCommand);

program
  .command('install-mcp <server-name>')
  .description('Install and configure an MCP server') // Updated description
  .action(handleInstallMcpCommand); // Use the imported handler

program.parse(process.argv);