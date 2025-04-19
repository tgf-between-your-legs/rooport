# Mode Definition Workflow (.md to bundled .json)

## 1. Overview

This document outlines the necessary two-step process to convert the source `.mode.md` files into the final bundled JSON format required by the Roo Code system. This addresses the gap identified between the Markdown-based source format and the JSON-based consumption format.

## 2. Source Format: `.mode.md`

*   Location: `v7.0/modes/` (or similar versioned directory)
*   Structure:
    *   YAML Frontmatter: Contains metadata like `slug`, `name`, `description`, `tags`, `Level`.
    *   Markdown Body: Contains sections like `## Role Definition`, `## Capabilities`, `## Workflow`, `## Constraints`, `## Metadata` (which includes `Tool Groups`), etc.

## 3. Required Conversion Process

**Step 1: Convert `.mode.md` to Individual `.json` Files**

*   **Input:** Directory containing `.mode.md` files (e.g., `v7.0/modes/`).
*   **Output:** Directory containing individual `.json` files, one per mode (e.g., `roo-modes-dev/`).
*   **Tool:** A **new script** is required (e.g., `dev_tools/convert_md_to_json.js`).
*   **Script Logic:**
    1.  Recursively find all `.mode.md` files in the input directory.
    2.  For each `.mode.md` file:
        *   Parse the YAML frontmatter.
        *   Parse the Markdown body to extract key sections (especially `## Role Definition`, `## Metadata` for `Tool Groups`, and potentially combining other sections like Capabilities/Workflow/Constraints into `customInstructions`).
        *   Construct a JSON object adhering to the structure specified in the `create_mode` instructions (requiring `slug`, `name`, `roleDefinition`, `groups`, and optionally `customInstructions`, `tags`, etc.). Ensure multi-line strings use `\n`.
        *   Write the generated JSON object to a corresponding `.json` file in the output directory (e.g., `v7.0/modes/abc/def.mode.md` -> `roo-modes-dev/def.json`).
*   **Responsibility:** This script needs to be developed.

**Step 2: Bundle Individual `.json` Files**

*   **Input:** Directory containing individual `.json` files (e.g., `roo-modes-dev/`).
*   **Output:** Single bundled JSON file (e.g., `v7.0/roo_commander_modes_v7.0.json`).
*   **Tool:** Existing script `dev_tools/bundle_modes.js`.
*   **Script Logic:** (As documented in `dev_tools/bundle_modes_sop.md`)
    1.  Reads all `.json` files from the input directory.
    2.  Sorts modes (roo-commander first, then alphabetically by slug).
    3.  Wraps the sorted array in `{"customModes": [...]}`.
    4.  Writes the final bundled JSON file to the specified output location.
*   **Execution:** `node dev_tools/bundle_modes.js --source roo-modes-dev --outputDir v7.0 --outputFile roo_commander_modes_v7.0.json` (Example)

## 4. Implementation Plan

1.  **Create Task for Converter Script:** Define an MDTM task to develop the `convert_md_to_json.js` script based on the logic described above. Assign to a developer resource.
2.  **Update SOPs:** Once the converter script exists, update `dev_tools/bundle_modes_sop.md` (or create a new master SOP) to document the full two-step workflow.
3.  **Execute Workflow:** Run the converter script followed by the bundler script to generate the final mode file for deployment/use.

This clarifies the complete workflow from our Markdown source files to the operational JSON bundle.