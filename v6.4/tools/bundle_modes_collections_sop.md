# Standard Operating Procedure: Bundling Mode Collections

## Overview

This document outlines the process for bundling Roo mode collections using the `bundle_modes_collections_with_core.js` script. This process takes individual mode JSON files and bundles them into collections according to the definitions in `mode_collections_wrapped.json`.

## Prerequisites

- Node.js installed
- Source directory containing individual mode JSON files
- Collections definition file (`mode_collections_wrapped.json`)
- Output directory for the bundled collections

## Files

1. **`bundle_modes_collections_with_core.js`**: The main script that processes mode files and creates collection bundles.
2. **`mode_collections_wrapped.json`**: Defines the collections and which modes belong to each collection.

## Process

### 1. Prepare the Source Directory

Ensure all individual mode JSON files are in the source directory. Each mode file should:
- Be a valid JSON file
- Contain a `slug` property that uniquely identifies the mode
- Include all required properties for a mode (name, roleDefinition, etc.)

### 2. Prepare the Collections Definition File

The collections definition file (`mode_collections_wrapped.json`) should:
- Define a `collections` object containing collection definitions
- Each collection should have:
  - A unique key (e.g., `core`, `frontend_react`)
  - A `name` property (display name)
  - A `description` property
  - A `modes` array listing the slugs of modes to include in the collection

Example:
```json
{
  "collections": {
    "core": {
      "name": "Core",
      "description": "Essential modes for coordination and basic project tasks.",
      "modes": [
        "roo-commander",
        "project-onboarding",
        "context-resolver"
      ]
    }
  }
}
```

### 3. Run the Bundling Script

Execute the script with the following parameters:

```bash
node bundle_modes_collections_with_core.js --source <source_dir> --collections <collections_file> --outputBaseDir <output_dir>
```

Parameters:
- `--source`: Directory containing individual mode JSON files (default: `roo-modes-dev`)
- `--collections`: Path to the collections definition file (default: `dev_tools/mode_collections.json`)
- `--outputBaseDir`: Base directory for output (default: `.`)

Example:
```bash
node bundle_modes_collections_with_core.js --source v6.3/modes --collections dev_tools/mode_collections_wrapped.json --outputBaseDir v6.4/modes
```

### 4. Verify the Output

After running the script:
1. Check the output directory for the created collection directories
2. Each collection should have its own subdirectory (e.g., `v6.4/modes/core/`)
3. Each collection directory should contain a JSON file with the bundled modes (e.g., `core_modes.json`)
4. Verify that the core modes are included in each collection
5. Verify that the roo-commander mode is the first mode in each collection

## How the Script Works

1. **Reading Mode Files**: The script reads all JSON files from the source directory and extracts mode definitions.
2. **Reading Collections Definition**: The script parses the collections definition file to determine which modes belong to which collections.
3. **Identifying Core Modes**: The script identifies core modes from the `core` collection.
4. **Processing Collections**: For each collection:
   - The script filters modes based on the slugs defined in the collection
   - Core modes are added to the collection (if not already included)
   - Modes are sorted (with roo-commander first)
   - The final JSON is prepared with the `customModes` property
5. **Writing Output Files**: The script creates the necessary directories and writes the bundled JSON files.

## Troubleshooting

- **Missing Modes**: If a mode slug is listed in a collection but the corresponding mode file is not found, the script will log a warning and continue.
- **Invalid JSON**: If a mode file contains invalid JSON, the script will log an error and skip that file.
- **Output Directory Issues**: If there are problems creating the output directories, the script will log an error and skip that collection.

## Example

To bundle modes from `v6.3/modes` according to the collections defined in `dev_tools/mode_collections_wrapped.json` and output to `v6.4/modes`:

```bash
node dev_tools/bundle_modes_collections_with_core.js --source v6.3/modes --collections dev_tools/mode_collections_wrapped.json --outputBaseDir v6.4/modes
```

This will create collection directories in `v6.4/modes/` (e.g., `v6.4/modes/core/`, `v6.4/modes/frontend_react/`, etc.) with the corresponding bundled JSON files.