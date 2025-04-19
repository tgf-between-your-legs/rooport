const fs = require('fs');
const path = require('path');
const TOML = require('@iarna/toml');

const modesRootDir = path.join(__dirname, '..', 'v7.1', 'modes');
const outputFilePath = path.join(__dirname, '..', '.docs', 'mode_index_v7.1.md');

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

// --- Main Script Logic ---
try {
    console.log(`Scanning for modes in: ${modesRootDir}`);
    const modeFiles = findModeFiles(modesRootDir);
    console.log(`Found ${modeFiles.length} potential mode files.`);

    const modesData = [];
    let parseErrors = 0;

    modeFiles.forEach(filePath => {
        try {
            const content = fs.readFileSync(filePath, 'utf8');
            const tomlString = extractToml(content);
            if (!tomlString) {
                console.warn(`WARN: No TOML frontmatter found in ${filePath}`);
                return;
            }

            const data = TOML.parse(tomlString);

            // Basic validation
            if (!data.id || !data.name || !data.classification || !data.domain || !data.summary) {
                 console.warn(`WARN: Missing required fields (id, name, classification, domain, summary) in ${filePath}. Skipping.`);
                 return;
            }

            // Exclude footgun modes
            if (data.id.includes('footgun')) {
                console.log(`INFO: Skipping footgun mode: ${data.id}`);
                return; // Skip this mode
            }

            modesData.push({
                id: data.id,
                name: data.name,
                classification: data.classification,
                domain: data.domain,
                sub_domain: data.sub_domain || null, // Handle optional sub_domain
                summary: data.summary.trim(),
                path: path.relative(path.join(__dirname, '..'), filePath).replace(/\\/g, '/') // Relative path for link
            });
        } catch (parseError) {
            console.error(`ERROR: Failed to parse TOML in ${filePath}: ${parseError.message}`);
            parseErrors++;
        }
    });

    if (parseErrors > 0) {
        console.error(`\nEncountered ${parseErrors} parsing errors. Index might be incomplete.`);
    }

    // Sort modes for consistent output
    modesData.sort((a, b) => {
        if (a.classification !== b.classification) return a.classification.localeCompare(b.classification);
        if (a.domain !== b.domain) return a.domain.localeCompare(b.domain);
        if (a.sub_domain !== b.sub_domain) {
            if (!a.sub_domain) return -1; // Modes without sub-domain first
            if (!b.sub_domain) return 1;
            return a.sub_domain.localeCompare(b.sub_domain);
        }
        return a.name.localeCompare(b.name);
    });

    // Group modes by classification -> domain -> sub_domain
    const groupedModes = modesData.reduce((acc, mode) => {
        const { classification, domain, sub_domain } = mode;
        if (!acc[classification]) acc[classification] = {};
        if (!acc[classification][domain]) acc[classification][domain] = {};
        const key = sub_domain || '__no_sub_domain__'; // Use a key for modes without sub-domain
        if (!acc[classification][domain][key]) acc[classification][domain][key] = [];
        acc[classification][domain][key].push(mode);
        return acc;
    }, {});

    // Generate Markdown content
    let markdownContent = `# Roo Commander Mode Index (v7.1)\n\n`;
    markdownContent += `*Generated on: ${new Date().toISOString()}*\n\n`;
    markdownContent += `**Total Modes Found:** ${modesData.length}\n\n`;

    Object.keys(groupedModes).sort().forEach(classification => {
        markdownContent += `## ${classification.charAt(0).toUpperCase() + classification.slice(1)}\n\n`; // Capitalize classification
        Object.keys(groupedModes[classification]).sort().forEach(domain => {
            markdownContent += `### Domain: ${domain}\n\n`;
            Object.keys(groupedModes[classification][domain]).sort().forEach(subDomainKey => {
                if (subDomainKey !== '__no_sub_domain__') {
                    markdownContent += `#### Sub-Domain: ${subDomainKey}\n\n`;
                }
                groupedModes[classification][domain][subDomainKey].forEach(mode => {
                    // Remove the path link from the output
                    markdownContent += `*   **${mode.name} (\`${mode.id}\`)**\n`;
                    markdownContent += `    *   *Summary:* ${mode.summary}\n`;
                });
                markdownContent += `\n`; // Add space after each sub-domain group (or domain group if no sub-domain)
            });
        });
    });

    // Write to output file
    fs.writeFileSync(outputFilePath, markdownContent);
    console.log(`\nSuccessfully generated mode index at: ${outputFilePath}`);
    console.log(`Total modes indexed: ${modesData.length}`);

} catch (error) {
    console.error(`\nFATAL ERROR generating mode index: ${error.message}`);
    process.exit(1);
}