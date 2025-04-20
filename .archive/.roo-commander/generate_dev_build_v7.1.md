+++
# --- Basic Metadata ---
title = "SOP: Generating Roo Commander v7.1 Dev Build"
status = "Active"
version = "1.0"
# created_date = "" # Optional: Add current date if needed
# updated_date = "" # Optional: Add current date if needed

# --- Document Type Specific Fields (Process/SOP) ---
objective = "To document the process for generating the runtime .roomodes file and .roo/rules-* directories from the v7.1 source mode definitions for development purposes."
inputs = ["Path to v7.1 source modes directory (`v7.1/modes/`)"]
outputs = ["Runtime `.roomodes` file", "Runtime `.roo/rules-[mode-id]/` directories"]
script_path = ".dev_tools/v7.1/build_dev_v7.1.js"
tags = ["build", "development", "v7.1", "modes", "rules", "sop"]
+++

# SOP: Generating Roo Commander v7.1 Dev Build

## Objective 🎯

This document outlines the standard operating procedure for generating the development build artifacts for Roo Commander v7.1. These artifacts include the runtime `.roomodes` file and the associated `.roo/rules-*` directories, which are derived from the source mode definitions located in `v7.1/modes/`. This process is intended for development and testing purposes.

## Prerequisites ✅

*   **Node.js:** Ensure Node.js (version compatible with the script's requirements) is installed on your system.
*   **Dependencies:** Navigate to the script's directory and install the necessary Node.js packages:
    ```bash
    cd .dev_tools/v7.1/
    npm install
    cd ../../.. # Return to workspace root
    ```

## Execution Steps 🚀

1.  **Navigate to Workspace Root:** Ensure your terminal's current working directory is the root of the `roo-commander` workspace (`/home/jeremy/vscode/roo-commander`).
2.  **Run the Build Script:** Execute the development build script using Node.js:
    ```bash
    node .dev_tools/v7.1/build_dev_v7.1.js
    ```

## Script Actions Explained 📜

The `build_dev_v7.1.js` script performs the following actions:

1.  **Scan Source Modes:** It recursively scans the `v7.1/modes/` directory for files ending with `.mode.md`.
2.  **Parse & Validate:** For each found mode file:
    *   It parses the TOML frontmatter using the `@iarna/toml` library.
    *   It validates the presence of required fields: `id`, `name`, and `system_prompt`. Modes missing these fields are skipped.
3.  **Generate `.roomodes`:** It constructs a JSON object containing a `customModes` key, whose value is an array of mode definitions for all valid modes. For this *development* build:
    *   The `model` and `customInstructions` fields are omitted from each mode definition within the array.
    *   The `groups` field is set to a permissive default (e.g., `["read", "edit", "browser", "command", "mcp"]`) allowing wider access during development.
    *   This JSON object is written to the `.roomodes` file in the workspace root.
4.  **Generate `.roo/rules-*` Directories:** For each valid mode:
    *   It cleans any existing corresponding directory at `.roo/rules-[mode-id]/`.
    *   It creates the target directory `.roo/rules-[mode-id]/`.
    *   **(Modified)** This version of the script **does not** copy or create the `context/`, `custom-instructions/`, or `examples/` subdirectories within the `.roo/rules-[mode-id]/` directory. These rule-specific files are managed separately.


## Output Artifacts 📦

*   **`.roomodes` file:** Located in the workspace root (`/home/jeremy/vscode/roo-commander/.roomodes`). This file contains a JSON object with a `customModes` key holding the array of mode definitions for the runtime.
*   **`.roo/rules-*/` directories:** Located within the `.roo/` directory in the workspace root (e.g., `/home/jeremy/vscode/roo-commander/.roo/rules-technical-writer/`). Each directory is created but **remains empty** in this build process; rule-specific files are not copied.

## Important Notes ⚠️

*   This process generates a **development build**. The resulting `.roomodes` file and rules directories may differ from a production build (e.g., permissive group settings, potentially omitted fields like `model`).
*   Ensure dependencies in `.dev_tools/v7.1/` are up-to-date before running the script.