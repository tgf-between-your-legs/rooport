+++
id = "KB-REPOMIX-USAGE-CORRECTIONS-V2" # Updated version
title = "Repomix Usage Corrections (Config, CLI Flags & Source Arguments)" # Updated title
context_type = "knowledge"
scope = "Correct usage of repomix config file, CLI flags, and source arguments" # Updated scope
target_audience = ["spec-repomix"]
granularity = "specific-corrections"
status = "active"
last_updated = "2025-05-01" # Updated date
tags = ["kb", "repomix", "configuration", "cli", "schema", "flags", "source", "url", "path", "correction"] # Added tags
related_context = ["repomix documentation"] # Assumed external context
template_schema_doc = ".ruru/templates/toml-md/14_kb_article.README.md"
relevance = "Critical: Corrects known errors in tool usage"
+++

# Repomix Usage Corrections

This document outlines critical corrections for using the `repomix` tool based on observed errors. Adherence to these corrections is crucial for successful `repomix` execution.

## 1. Configuration File (`repomix.config.json`) Schema

**Error:** The `output` field was incorrectly specified as a string.
**Correction:** The `output` field **MUST** be an **object** containing `path` and `format` keys.

**Incorrect Example:**
```json
{
  "output": "my-output-file.md"
}
```

**Correct Example:**
```json
{
  "output": {
    "path": "my-output-file.md",
    "format": "markdown" // Or "xml", "plain"
  }
  // ... other config options
}
```
*   Ensure the `output` field is structured as an object.
*   Valid `format` values include `"markdown"`, `"xml"`, `"plain"`.

## 2. Command-Line Interface (CLI) Flags

### 2.1. Output Format Flag (`--style`)

**Error:** The `--format` flag was used to specify the output format (e.g., `--format markdown`).
**Correction:** The correct flag to specify the output format/style is **`--style`**.

**Incorrect Command:**
```bash
repomix . --format markdown -o output.md
```

**Correct Command Structure:**
```bash
repomix [SOURCE] --style [STYLE_VALUE] -o [OUTPUT_PATH]
```

**Valid `--style` Values & Examples:**

*   **`markdown` (Default if not specified):**
    ```bash
    repomix ./src --style markdown -o output.md
    ```
*   **`xml`:**
    ```bash
    repomix ./src --style xml -o output.xml
    ```
*   **`plain` (or `text`):**
    ```bash
    repomix ./src --style plain -o output.txt
    ```

*   **Key Point:** Always use `--style [value]` instead of `--format [value]`.

## 3. Source Argument Usage (Local Path vs. Remote URL)

**Error:** Remote GitHub URLs were incorrectly treated as local filesystem paths when generating configuration files or commands, leading to errors like "Target directory not readable". This happens when the URL is mistakenly concatenated with the local workspace path (e.g., `/home/user/workspace/https:/github.com/...`) instead of being used for cloning or correctly placed in the config's `source` field.
 
**Correction:** The `spec-repomix` mode handles sources differently:
*   **Local Paths:** Are used directly as the `source` value in the generated temporary configuration file.
*   **Remote URLs:** Are used *only* for the initial `git clone` step. The *local path* of the temporary clone is then used as the `source` value in the generated temporary configuration file. The mode **does not** pass the remote URL directly to the `repomix` command or config file's `source` field.
 
### 3.1. Using a Local Directory Path
 
*   Provide the relative or absolute path to the directory you want to process. This path will be used as the `source` value in the generated temporary config file.
*   **Example:**
    ```bash
    # Process the 'src' directory within the current workspace
    repomix ./src --style markdown -o local_output.md

    # Process a specific subdirectory
     # For a subdirectory, the config would contain: { "source": "./src/components", ... }
     repomix --config temp_config_subdir.json
    ```

### 3.2. Handling Remote GitHub URLs (Mode Workflow)
 
*   The mode first clones the URL to a temporary local path (e.g., `.ruru/temp/clone_123`).
*   This *temporary local path* is then used as the `source` value in the generated config file.
*   **Example (Conceptual - Mode handles this internally):**
    1.  `git clone https://github.com/owner/repo.git .ruru/temp/clone_123`
    2.  Generate `temp_config.json` with `{ "source": ".ruru/temp/clone_123", ... }`
    3.  `repomix --config temp_config.json`
    4.  `rm -rf .ruru/temp/clone_123`

*   **Crucial Avoidance:** Ensure that the process invoking `repomix` passes the URL as a distinct argument and does **not** attempt to resolve it as a local path relative to the current working directory. The error "Target directory not readable: /path/to/workspace/https:/github.com/..." indicates the URL was incorrectly appended to the local path.
+*   **Mode Correction:** The mode's standard workflow avoids this error by always using a local path (either the original or the temporary clone path) as the `source` for the `repomix --config` command.