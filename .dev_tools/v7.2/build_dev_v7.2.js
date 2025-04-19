const fs = require('fs');
const path = require('path');
const TOML = require('@iarna/toml');

// --- Configuration ---
const modesSourceDir = path.join(__dirname, '..', '..', 'v7.1', 'modes');
const v72TargetRootDir = path.join(__dirname, '..', '..', 'v7.2');
const rulesTargetRootDir = path.join(__dirname, '..', '..', '.roo', 'rules');
const manifestFilePath = path.join(v72TargetRootDir, 'manifest.toml');
const defaultKbLookupRuleContent = `
# Rule: Consult Knowledge Base

Before proceeding with the task, review the contents of your Knowledge Base (KB) located in your mode's source directory (\`v7.2/<your-mode-slug>/kb/\`).
Assess if any documents within the KB are relevant to the current task.
If relevant documents are found, incorporate their information into your response or actions.
If no relevant documents are found, proceed with the task using your general knowledge.
`.trim();

// --- Helper Functions ---

// Recursively find all .mode.md files
function findModeFiles(dir, fileList = []) {
    try {
        const files = fs.readdirSync(dir);
        files.forEach(file => {
            const filePath = path.join(dir, file);
            try {
                const stat = fs.statSync(filePath);
                if (stat.isDirectory()) {
                    findModeFiles(filePath, fileList);
                } else if (file.endsWith('.mode.md')) {
                    fileList.push(filePath);
                }
            } catch (statErr) {
                console.warn(`  WARN: Could not stat file ${filePath}: ${statErr.message}`);
            }
        });
    } catch (readErr) {
        console.warn(`  WARN: Could not read directory ${dir}: ${readErr.message}`);
    }
    return fileList;
}

// Extract TOML frontmatter
function extractToml(content) {
    const match = content.match(/^\+\+\+([\s\S]*?)\+\+\+/);
    return match ? match[1] : null;
}

// Copy directory recursively
function copyDirRecursive(src, dest) {
    try {
        fs.mkdirSync(dest, { recursive: true });
        const entries = fs.readdirSync(src, { withFileTypes: true });

        for (let entry of entries) {
            const srcPath = path.join(src, entry.name);
            const destPath = path.join(dest, entry.name);

            try {
                if (entry.isDirectory()) {
                    copyDirRecursive(srcPath, destPath);
                } else {
                    fs.copyFileSync(srcPath, destPath);
                }
            } catch (copyErr) {
                 console.warn(`    WARN: Could not copy ${entry.name} from ${src} to ${dest}: ${copyErr.message}`);
            }
        }
    } catch (mkdirErr) {
        console.warn(`    WARN: Could not create or read directory ${dest}: ${mkdirErr.message}`);
    }
}

// Determine new slug and prefix based on v7.1 path
function getNewSlugAndPrefix(sourceFilePath, oldSlug) {
    const relativePath = path.relative(modesSourceDir, sourceFilePath);
    const pathParts = relativePath.split(path.sep);
    // pathParts will be like: ['worker', 'backend', 'fastapi-developer', 'fastapi-developer.mode.md']
    // or ['core', 'code', 'code.mode.md']

    let prefix = 'spec-'; // Default prefix
    let baseName = oldSlug.replace(/-developer$|-specialist$|-manager$|-lead$|-agent$|-writer$|-tester$|-fixer$|-reviewer$/, ''); // Basic cleanup

    // Determine prefix based on path structure (more specific first)
    if (pathParts.includes('core')) prefix = 'core-';
    else if (oldSlug === 'roo-commander') prefix = 'core-'; // Specific override
    else if (oldSlug === 'project-manager') prefix = 'manager-';
    else if (oldSlug === 'product-manager') prefix = 'manager-';
    else if (pathParts.includes('lead')) prefix = 'lead-';
    else if (pathParts.includes('backend')) prefix = 'dev-';
    else if (pathParts.includes('frontend')) prefix = 'dev-'; // Default for frontend, design might override
    else if (pathParts.includes('design')) prefix = 'design-';
    else if (pathParts.includes('data')) prefix = 'data-';
    else if (pathParts.includes('testing') || pathParts.includes('qa') || oldSlug.includes('-tester')) prefix = 'test-';
    else if (pathParts.includes('devops') || pathParts.includes('infra')) prefix = 'infra-';
    else if (pathParts.includes('utility')) prefix = 'util-';
    else if (oldSlug === 'technical-writer') prefix = 'util-';
    else if (oldSlug === 'code-reviewer') prefix = 'util-';
    else if (oldSlug === 'git-manager') prefix = 'util-';
    else if (oldSlug === 'eslint-specialist') prefix = 'util-'; // Or spec-? Let's try util-
    else if (oldSlug === 'vite-specialist') prefix = 'util-'; // Or spec-? Let's try util-
    else if (pathParts.includes('agent')) prefix = 'agent-';
    else if (oldSlug === 'bug-fixer') prefix = 'dev-'; // Or util-? Let's try dev-

    // Refine baseName further if needed
    if (prefix === 'core-' && pathParts.length > 2) baseName = pathParts[pathParts.length - 2]; // e.g., 'code'
    if (prefix === 'manager-' && pathParts.length > 2) baseName = pathParts[pathParts.length - 2]; // e.g., 'projects'
    if (prefix === 'lead-' && pathParts.length > 2) baseName = pathParts[pathParts.length - 2]; // e.g., 'backend'

    // Handle specific known cases for baseName refinement
    if (oldSlug === 'roo-commander') baseName = 'commander';
    if (oldSlug === 'project-manager') baseName = 'projects';
    if (oldSlug === 'product-manager') baseName = 'products';
    if (oldSlug === 'technical-writer') baseName = 'writer';
    if (oldSlug === 'code-reviewer') baseName = 'reviewer';
    if (oldSlug === 'git-manager') baseName = 'git';
    if (oldSlug === 'eslint-specialist') baseName = 'eslint';
    if (oldSlug === 'vite-specialist') baseName = 'vite';
    if (oldSlug === 'bug-fixer') baseName = 'fixer';
    if (oldSlug === 'fastapi-developer') baseName = 'fastapi';
    if (oldSlug === 'django-developer') baseName = 'django';
    if (oldSlug === 'flask-developer') baseName = 'flask';
    if (oldSlug === 'php-laravel-developer') baseName = 'laravel'; // Or php-laravel?
    if (oldSlug === 'angular-developer') baseName = 'angular';
    if (oldSlug === 'react-specialist') baseName = 'react';
    if (oldSlug === 'vuejs-developer') baseName = 'vue';
    if (oldSlug === 'sveltekit-developer') baseName = 'sveltekit';
    if (oldSlug === 'nextjs-developer') baseName = 'nextjs';
    if (oldSlug === 'astro-developer') baseName = 'astro';
    if (oldSlug === 'remix-developer') baseName = 'remix';
    if (oldSlug === 'tailwind-specialist') baseName = 'tailwind';
    if (oldSlug === 'bootstrap-specialist') baseName = 'bootstrap';
    if (oldSlug === 'material-ui-specialist') baseName = 'mui';
    if (oldSlug === 'shadcn-ui-specialist') baseName = 'shadcn';
    if (oldSlug === 'ant-design-specialist') baseName = 'antd';
    if (oldSlug === 'd3js-specialist') baseName = 'd3';
    if (oldSlug === 'threejs-specialist') baseName = 'threejs';
    if (oldSlug === 'animejs-specialist') baseName = 'animejs';
    if (oldSlug === 'jquery-specialist') baseName = 'jquery';
    if (oldSlug === 'typescript-specialist') baseName = 'typescript';
    if (oldSlug === 'mongodb-specialist') baseName = 'mongo';
    if (oldSlug === 'mysql-specialist') baseName = 'mysql';
    if (oldSlug === 'neon-db-specialist') baseName = 'neon';
    if (oldSlug === 'elasticsearch-specialist') baseName = 'elasticsearch';
    if (oldSlug === 'dbt-specialist') baseName = 'dbt';
    if (oldSlug === 'docker-compose-specialist') baseName = 'docker';
    if (oldSlug === 'cloudflare-workers-specialist') baseName = 'cloudflare';
    if (oldSlug === 'supabase-developer') baseName = 'supabase';
    if (oldSlug === 'firebase-developer') baseName = 'firebase';
    if (oldSlug === 'directus-specialist') baseName = 'directus';
    if (oldSlug === 'frappe-specialist') baseName = 'frappe';
    if (oldSlug === 'wordpress-specialist') baseName = 'wordpress';
    if (oldSlug === 'clerk-auth-specialist') baseName = 'clerk';
    if (oldSlug === 'supabase-auth-specialist') baseName = 'supabase-auth';
    if (oldSlug === 'firebase-auth-specialist') baseName = 'firebase-auth';
    if (oldSlug === 'openai-specialist') baseName = 'openai';
    if (oldSlug === 'huggingface-specialist') baseName = 'huggingface';
    if (oldSlug === 'e2e-tester') baseName = 'e2e';
    if (oldSlug === 'integration-tester') baseName = 'integration';


    // Ensure baseName doesn't start or end with hyphen and is lowercase
    baseName = baseName.replace(/^-+|-+$/g, '').toLowerCase();
    // Replace multiple hyphens with single hyphen
    baseName = baseName.replace(/-{2,}/g, '-');

    const newSlug = `${prefix}${baseName}`;
    console.log(`    Mapping: ${oldSlug} (Path: ${pathParts.slice(0,-1).join('/')}) -> ${newSlug}`);
    return { newSlug, prefix: prefix.replace('-', '') };
}


// --- Main Build Logic ---
try {
    console.log(`Starting dev build process for v7.2 modes...`);
    console.log(`Source modes directory: ${modesSourceDir}`);
    console.log(`Target v7.2 root directory: ${v72TargetRootDir}`);
    console.log(`Target rules root directory: ${rulesTargetRootDir}`);
    console.log(`Target manifest file: ${manifestFilePath}`);

    // Ensure target directories exist
    fs.mkdirSync(v72TargetRootDir, { recursive: true });
    fs.mkdirSync(rulesTargetRootDir, { recursive: true });

    const modeFiles = findModeFiles(modesSourceDir);
    console.log(`\nFound ${modeFiles.length} potential mode files.`);

    const manifestEntries = {}; // Use object for easier TOML generation
    let processedCount = 0;
    let errorCount = 0;

    modeFiles.forEach(filePath => {
        const modeFileName = path.basename(filePath);
        const sourceModeDir = path.dirname(filePath);
        const oldSlug = modeFileName.replace('.mode.md', '');

        console.log(`\nProcessing: ${modeFileName} (Old Slug: ${oldSlug})`);

        try {
            // 1. Read and Parse TOML
            const content = fs.readFileSync(filePath, 'utf8');
            const tomlString = extractToml(content);
            if (!tomlString) {
                console.warn(`  WARN: No TOML frontmatter found. Skipping.`);
                return;
            }
            let data;
            try {
                data = TOML.parse(tomlString);
            } catch (tomlErr) {
                console.warn(`  WARN: Invalid TOML in ${modeFileName}: ${tomlErr.message}. Skipping.`);
                return;
            }


            // 2. Validate required fields
            if (!data.id || !data.name || !data.system_prompt) {
                console.warn(`  WARN: Missing required fields (id, name, system_prompt) in TOML. Skipping.`);
                return;
            }
            if (data.id !== oldSlug) {
                 console.warn(`  WARN: TOML id "${data.id}" does not match filename slug "${oldSlug}". Skipping.`);
                 return;
            }

            // 3. Determine New Slug & Prefix
            const { newSlug, prefix } = getNewSlugAndPrefix(filePath, oldSlug);
            if (!newSlug || newSlug.endsWith('-')) { // Basic check for valid slug
                console.warn(`  WARN: Could not determine a valid new slug (Result: ${newSlug}). Skipping.`);
                return;
            }

            // 4. Define Target Paths
            const targetV72ModeDir = path.join(v72TargetRootDir, newSlug);
            const targetModeFilePath = path.join(targetV72ModeDir, `${newSlug}.mode.md`);
            const targetKbDir = path.join(targetV72ModeDir, 'kb');
            const targetRulesDir = path.join(rulesTargetRootDir, newSlug); // Base is .roo/rules/
            const targetKbRuleFile = path.join(targetRulesDir, '01-kb-lookup-rule.md');

            // 5. Create v7.2 Directory Structure
            console.log(`  Ensuring target v7.2 directory: ${targetV72ModeDir}`);
            fs.mkdirSync(targetV72ModeDir, { recursive: true });
            fs.mkdirSync(targetKbDir, { recursive: true }); // Ensure kb dir exists

            // 6. Copy and Modify .mode.md
            console.log(`  Copying and modifying mode file to: ${targetModeFilePath}`);
            // Ensure the replacement is specific enough
            const idRegex = new RegExp(`^id\\s*=\\s*"${oldSlug}"`, 'm');
            let newContent = content;
            if (idRegex.test(newContent)) {
                 newContent = newContent.replace(idRegex, `id = "${newSlug}"`);
            } else {
                 console.warn(`    WARN: Could not find 'id = "${oldSlug}"' in TOML for replacement.`);
                 // Attempt to add/replace anyway if structure is predictable
                 // This part might need refinement based on TOML structure variations
            }
            fs.writeFileSync(targetModeFilePath, newContent, 'utf8');

            // 7. Copy custom-instructions to kb/
            const sourceCustomInstructionsDir = path.join(sourceModeDir, 'custom-instructions');
            if (fs.existsSync(sourceCustomInstructionsDir)) {
                console.log(`  Copying custom-instructions to kb: ${sourceCustomInstructionsDir} -> ${targetKbDir}`);
                copyDirRecursive(sourceCustomInstructionsDir, targetKbDir);
            } else {
                console.log(`  No custom-instructions directory found for ${oldSlug}.`);
            }

            // 8. Create .roo/rules/<new-slug> directory and KB rule
            console.log(`  Ensuring target rules directory: ${targetRulesDir}`);
            // Clean up existing directory first
            if (fs.existsSync(targetRulesDir)) {
                fs.rmSync(targetRulesDir, { recursive: true, force: true });
                // console.log(`    Removed existing target rules directory.`);
            }
            fs.mkdirSync(targetRulesDir, { recursive: true });
            console.log(`  Writing KB lookup rule: ${targetKbRuleFile}`);
            // Inject the correct slug into the rule content
            const ruleContentWithSlug = defaultKbLookupRuleContent.replace('<your-mode-slug>', newSlug);
            fs.writeFileSync(targetKbRuleFile, ruleContentWithSlug, 'utf8');

            // 9. Prepare Manifest Entry
            manifestEntries[newSlug] = {
                slug: newSlug,
                name: data.name,
                prefix: prefix,
                role_definition: data.system_prompt.trim(),
                source_path_v7_1: path.relative(path.join(__dirname, '..', '..'), filePath).replace(/\\/g, '/'), // Normalize path separators
                path_v7_2: path.relative(path.join(__dirname, '..', '..'), targetModeFilePath).replace(/\\/g, '/'),
                rules_path: path.relative(path.join(__dirname, '..', '..'), targetRulesDir).replace(/\\/g, '/'),
                tags: [prefix, ...(data.tags || [])].filter((tag, index, self) => tag && self.indexOf(tag) === index) // Add prefix, ensure unique, remove empty
            };
            console.log(`  Prepared manifest entry for ${newSlug}.`);

            processedCount++;

        } catch (err) {
            console.error(`  ERROR processing ${modeFileName}: ${err.message}`);
            console.error(err.stack); // Print stack trace for debugging
            errorCount++;
        }
    });

    // 10. Write manifest.toml file
    try {
        // Structure the manifest with a top-level 'modes' table containing each mode
        const outputObject = { modes: manifestEntries };
        // Use TOML.stringify from @iarna/toml
        const manifestContent = TOML.stringify(outputObject);

        fs.writeFileSync(manifestFilePath, manifestContent, 'utf8');
        console.log(`\nSuccessfully wrote manifest for ${Object.keys(manifestEntries).length} modes to ${manifestFilePath}`);
    } catch (writeErr) {
        console.error(`\nFATAL ERROR writing ${manifestFilePath}: ${writeErr.message}`);
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
    console.error(error.stack);
    process.exit(1);
}