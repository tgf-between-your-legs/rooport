# SOP: Bundling Roo Commander Mode Collections

**Purpose:** To combine individual mode definition JSON files from a development directory into multiple, collection-specific JSON files, organized within a versioned output directory. This script uses a central definition file to determine which modes belong to each collection.

**Tool:** `dev_tools/bundle_modes_collections.js` (Node.js script)

**Prerequisites:** Node.js must be installed and available in your system's PATH.

## Input Files

1.  **Source Modes Directory:** Contains the individual `.json` files for each mode.
    *   Default: `./roo-modes-dev/`
    *   Configurable via `--source` argument.
2.  **Collections Definition File:** A JSON file defining the structure of the collections. It specifies which modes (by slug) belong to each named collection and can include other collections.
    *   Default: `./dev_tools/mode_collections.json`
    *   Configurable via `--collections` argument.

## Output Structure

The script generates the following output structure:

```
<outputBaseDir>/
├── <collection_name_1>/
│   └── <collection_name_1>_modes.json
├── <collection_name_2>/
│   └── <collection_name_2>_modes.json
└── ...
```

*   `<outputBaseDir>`: The base directory for the output (e.g., `v6.1`, `v6.2`). Specified using the `--outputBaseDir` argument. Defaults to the current directory (`.`).
*   `<collection_name_X>`: Subdirectories created automatically, named after each collection defined in the Collections Definition File.
*   `<collection_name_X>_modes.json`: The bundled JSON file containing only the modes belonging to that specific collection. The filename is dynamically generated based on the collection name.

## Procedure

1.  **Navigate to Repository Root:** Open your terminal or command prompt and ensure your current working directory is the root of the `roo-commander` repository (the directory containing `dev_tools/`, `roo-modes-dev/`, etc.).

2.  **Run the Script:** Execute the script using `node`. Use command-line arguments to specify the desired output version directory.

    *   **Creating a Versioned Output (Recommended):**
        *   Use `--outputBaseDir` to specify the target version folder (e.g., `v6.1`). This directory will be created if it doesn't exist. The script will then create collection subdirectories *inside* this base directory.
        *   Example for creating v6.1 collections:
        ```bash
        node dev_tools/bundle_modes_collections.js --outputBaseDir v6.1
        ```
        *   This reads modes from `./roo-modes-dev/`, uses definitions from `./dev_tools/mode_collections.json`, and writes output files like `./v6.1/core/core_modes.json`, `./v6.1/baas/baas_modes.json`, etc.

    *   **Specifying Source Directory (Less Common):**
        *   If your development modes are not in `roo-modes-dev/`, use `--source`.
        ```bash
        node dev_tools/bundle_modes_collections.js --source path/to/your/modes --outputBaseDir v6.1
        ```

    *   **Specifying Collections Definition File (Less Common):**
        *   If your collections definition is not at `dev_tools/mode_collections.json`, use `--collections`.
        ```bash
        node dev_tools/bundle_modes_collections.js --collections path/to/your/collections.json --outputBaseDir v6.1
        ```

3.  **Verify Output:**
    *   The script will print console messages indicating the source directory, collections file, base output directory, and the status of processing each collection.
    *   Check the specified output base directory (e.g., `v6.1/`) for the collection subdirectories (e.g., `core/`, `baas/`).
    *   Inside each collection subdirectory, verify the existence of the corresponding bundled JSON file (e.g., `core_modes.json`).
    *   Open a few bundled files and verify they contain the `{"customModes": [ ... ]}` structure with the expected array of mode objects for that collection.

4.  **Use the Bundled Files:** These collection-specific files can be used to provide tailored sets of modes for different user needs or application contexts.

## Error Handling

*   The script will print error messages to the console if:
    *   It cannot read the source directory.
    *   It cannot read or parse the collections definition file.
    *   It encounters errors parsing individual mode JSON files (it will warn and skip invalid files).
    *   It cannot create the output base directory or collection subdirectories.
    *   It cannot write the final bundled files.
*   If errors occur, check the console output for details, verify file paths and permissions, and ensure the individual JSON mode files and the collections definition file are valid.

## Script Arguments

*   `--source <directory>`: Specifies the input directory containing individual `.json` mode files. (Default: `roo-modes-dev`)
*   `--collections <filepath>`: Specifies the path to the JSON file defining the mode collections. (Default: `dev_tools/mode_collections.json`)
*   `--outputBaseDir <directory>`: Specifies the base directory where the collection subdirectories and their bundled files should be saved. (Default: `.`)