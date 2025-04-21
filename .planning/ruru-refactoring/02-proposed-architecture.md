+++
id = "CTX-RURU-REFACTOR-ARCHITECTURE"
title = "Roo Commander Path Refactor: Proposed Architecture"
context_type = "reference"
scope = "Technical details of the configurable path solution"
target_audience = ["ai_dev_team", "roo-commander", "core-architect"]
granularity = "detailed"
status = "proposal"
last_updated = "2025-04-21"
tags = ["refactoring", "configuration", "paths", "ruru", "architecture", "toml", "scripting", "placeholders"]
+++

# Roo Commander Path Refactor: Proposed Architecture

This document details the technical components of the configurable path solution.

## 1. Central Configuration (`ruru.config.toml`)

A new file, `ruru.config.toml`, will be placed at the workspace root. It acts as the single source of truth for all core system paths.

**Example `ruru.config.toml`:**

```toml
# Configuration for Roo Commander System Paths

# === Core Paths (Used by Roo Code Extension & Build Scripts) ===
# Base directory for mode-specific rules. Change for forks like Kilocode.
rules_root = ".roo"
# File containing the list of modes loaded by the extension.
modes_file = ".rurumodes" # Renamed from .roomodes

# === Workspace Structure ===
# Base directory for artifact folders. Use "." for root, or e.g., ".ruru" for nesting.
workspace_base = "."
# Base directory for mode definitions and their knowledge bases.
modes_root = ".modes"

# === Artifact Directories (Paths constructed relative to workspace_base) ===
# Define paths using {WORKSPACE_BASE}. The substitution script will resolve this.
tasks_dir = "{WORKSPACE_BASE}/.tasks"
decisions_dir = "{WORKSPACE_BASE}/.decisions"
docs_dir = "{WORKSPACE_BASE}/.docs"
context_dir = "{WORKSPACE_BASE}/.context"
logs_dir = "{WORKSPACE_BASE}/.logs"
planning_dir = "{WORKSPACE_BASE}/.planning"
reports_dir = "{WORKSPACE_BASE}/.reports"
templates_dir = "{WORKSPACE_BASE}/.templates"
workflows_dir = "{WORKSPACE_BASE}/.workflows"
processes_dir = "{WORKSPACE_BASE}/.processes"
archive_dir = "{WORKSPACE_BASE}/.archive"
snippets_dir = "{WORKSPACE_BASE}/.snippets"

# === Specific Generated Files/Dirs (Relative to workspace root) ===
# Directory for storing build artifacts (zip files).
builds_dir = ".builds"
# Path to the generated summary file for modes (depends on modes_root).
# Ensure build_roomodes.js uses this path.
mode_summary_file = "{MODES_ROOT}/roo-commander/kb/kb-available-modes-summary.md"

# === Placeholder Definitions ===
# Maps configuration keys above to the placeholder strings used in source Markdown files.
# The substitution script uses this mapping. Keys should be unique and descriptive.
[placeholders]
RURU_RULES_ROOT = "rules_root"
RURU_MODES_ROOT = "modes_root"
RURU_TASKS_DIR = "tasks_dir"
RURU_DECISIONS_DIR = "decisions_dir"
RURU_DOCS_DIR = "docs_dir"
RURU_CONTEXT_DIR = "context_dir"
RURU_LOGS_DIR = "logs_dir"
RURU_PLANNING_DIR = "planning_dir"
RURU_REPORTS_DIR = "reports_dir"
RURU_TEMPLATES_DIR = "templates_dir"
RURU_WORKFLOWS_DIR = "workflows_dir"
RURU_PROCESSES_DIR = "processes_dir"
RURU_ARCHIVE_DIR = "archive_dir"
RURU_SNIPPETS_DIR = "snippets_dir"
RURU_BUILDS_DIR = "builds_dir"
RURU_MODES_FILE = "modes_file" # Path to the modes list file
RURU_MODE_SUMMARY_FILE = "mode_summary_file" # Path to the summary markdown
```

**Key Points:**
*   Users/forks modify `rules_root`, `workspace_base`, `modes_root` primarily.
*   Artifact directory paths use `{WORKSPACE_BASE}` for flexibility.
*   The `[placeholders]` table maps config keys to the strings used in source files.

## 2. Placeholders in Source Files

*   **Format:** Use a distinct format like `{{RURU_PLACEHOLDER_NAME}}` (e.g., `{{RURU_TASKS_DIR}}`).
*   **Location:** Replace hardcoded paths in all relevant Markdown files (`.modes/**/*.mode.md`, `.modes/**/kb/*.md`, `.roo/rules/**/*.md`, `.templates/**/*.md`, `.workflows/*.md`, `.processes/*.md`, `.docs/**/*.md`, `README.md`).

**Example (in a rule file):**
`Log the failure in the Commander task log ({{RURU_TASKS_DIR}}/TASK-CMD-....md).`

## 3. Substitution Script (`substitute-paths.js`)

*   **Purpose:** To read `ruru.config.toml`, process source Markdown files, and generate output files with placeholders replaced by configured paths.
*   **Trigger:** Run manually after changing `ruru.config.toml`, during a build process, or as a setup step for a specific environment.
*   **Inputs:**
    *   `ruru.config.toml` path.
    *   List of source directories containing Markdown files to process.
    *   Target output directory (e.g., a `.ruru-processed/` folder or potentially overwriting source if carefully managed).
*   **Process:**
    1.  Parse `ruru.config.toml`.
    2.  Resolve `{WORKSPACE_BASE}` in artifact paths.
    3.  Recursively find target `.md` files in source directories.
    4.  For each file:
        *   Read content.
        *   Iterate through `[placeholders]` mapping in config.
        *   Replace all occurrences of `{{PLACEHOLDER_NAME}}` with the corresponding resolved path value from the config.
        *   Write processed content to the target output directory, maintaining the original relative structure.
*   **AI Interaction:** The AI modes (Roo Commander, specialists) will be configured (via `.rurumodes` or extension settings) to read their rules and KB files from the *processed* output directory, ensuring they only ever see concrete paths.