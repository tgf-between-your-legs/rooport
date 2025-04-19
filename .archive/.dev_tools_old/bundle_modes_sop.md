# SOP: Bundling Roo Commander Modes

**Purpose:** To combine individual mode definition JSON files from a development directory into a single, sorted JSON file suitable for use with Roo Code.

**Tool:** `dev_tools/bundle_modes.js` (Node.js script)

**Prerequisites:** Node.js must be installed and available in your system's PATH.

## Procedure

1.  **Navigate to Repository Root:** Open your terminal or command prompt and ensure your current working directory is the root of the `roo-commander` repository (the directory containing the `dev_tools/` and `roo-modes-dev/` folders).

2.  **Run the Script:** Execute the script using `node`. You can use command-line arguments to customize the input and output locations, or rely on the defaults.

    *   **Using Defaults:**
        *   This will read from `./roo-modes-dev/` and write to `./bundled_modes.json`.
        ```bash
        node dev_tools/bundle_modes.js
        ```

    *   **Specifying Output File/Directory (Recommended for Versioning):**
        *   Use `--outputDir` to specify the target folder (it will be created if it doesn't exist).
        *   Use `--outputFile` to specify the desired filename for the bundle.
        *   Example for creating a v5.0 bundle:
        ```bash
        node dev_tools/bundle_modes.js --outputDir v5.0 --outputFile roo_commander_modes_v5.0.json
        ```
        *   This reads from `./roo-modes-dev/` and writes to `./v5.0/roo_commander_modes_v5.0.json`.

    *   **Specifying Source Directory (Less Common):**
        *   If your development modes are in a different directory, use `--source`.
        ```bash
        node dev_tools/bundle_modes.js --source path/to/your/modes --outputDir v5.1 --outputFile roo_commander_modes_v5.1.json
        ```

3.  **Verify Output:**
    *   The script will print console messages indicating the source directory, the number of modes found, and the final output path upon successful completion.
    *   Check the specified output directory for the newly created bundled JSON file (e.g., `v5.0/roo_commander_modes_v5.0.json`).
    *   Open the file and verify it contains the `{"customModes": [ ... ]}` structure with an array of mode objects; the 'roo-commander' mode should be first, followed by the rest sorted alphabetically by `slug`.

4.  **Use the Bundled File:** Copy the entire content of the generated bundled JSON file and paste it into your Roo Code custom modes settings or save it as `.roomodes` in your project.

## Error Handling

*   The script will print error messages to the console if:
    *   It cannot read the source directory.
    *   It encounters errors parsing individual JSON files (it will warn and skip invalid files).
    *   It cannot create the output directory.
    *   It cannot write the final bundled file.
*   If errors occur, check the console output for details, verify file paths and permissions, and ensure the individual JSON mode files are valid.

## Script Arguments

*   `--source <directory>`: Specifies the input directory containing individual `.json` mode files. (Default: `roo-modes-dev`)
*   `--outputDir <directory>`: Specifies the directory where the bundled file should be saved. (Default: `.`)
*   `--outputFile <filename>`: Specifies the name for the output bundled JSON file. (Default: `bundled_modes.json`)