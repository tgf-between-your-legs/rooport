+++
id = "CTX-RURU-SIMPLEREFACTOR-IMPL-GUIDE"
title = "Roo Commander Path Refactor (Simplified): Implementation Guide & Impact"
context_type = "implementation_guide"
scope = "Detailed list of required changes for consolidation under .ruru/"
target_audience = ["ai_dev_team", "roo-commander"]
granularity = "detailed"
status = "proposal"
last_updated = "2025-04-21"
tags = ["refactoring", "paths", "ruru", "implementation", "checklist", "fixed-path"]
+++

# Roo Commander Path Refactor (Simplified): Implementation Guide & Impact

This document details the steps required to refactor the Roo Commander system to consolidate its operational directories under a fixed `.ruru/` parent directory.

**Assumptions:**
*   The chosen fixed parent directory is `.ruru/`.
*   Placeholders and substitution scripts are **not** being used for this simpler approach.

**Implementation Steps:**

1.  **🛑 Backup Repository:** Before starting, ensure all changes are committed and create a full backup or a dedicated branch (`git branch pre-ruru-refactor`).

2.  **Create Parent Directory:** Create the `.ruru/` directory at the workspace root.

3.  **Move Existing Directories:** Move the following directories from the workspace root *into* the newly created `.ruru/` directory:
    *   `.tasks/` -> `.ruru/.tasks/`
    *   `.docs/` -> `.ruru/.docs/`
    *   `.decisions/` -> `.ruru/.decisions/`
    *   `.context/` -> `.ruru/.context/`
    *   `.logs/` -> `.ruru/.logs/`
    *   `.planning/` -> `.ruru/.planning/`
    *   `.reports/` -> `.ruru/.reports/`
    *   `.templates/` -> `.ruru/.templates/`
    *   `.workflows/` -> `.ruru/.workflows/`
    *   `.processes/` -> `.ruru/.processes/`
    *   `.archive/` -> `.ruru/.archive/`
    *   `.snippets/` -> `.ruru/.snippets/`
    *   `.modes/` -> `.ruru/.modes/`
    *   `.roo/` -> `.ruru/.roo/`

4.  **Global Search & Replace:** Perform careful, case-sensitive, whole-word (where appropriate) search-and-replace operations across **all relevant files** (primarily `.md` and `.js` files within the *new* `.ruru/` subdirectories, plus `README.md`, `.gitignore`, build scripts at the root).
    *   Replace `".ruru/tasks/"` with `".ruru/.tasks/"`
    *   Replace `".ruru/docs/"` with `".ruru/.docs/"`
    *   Replace `".ruru/decisions/"` with `".ruru/.decisions/"`
    *   Replace `".ruru/context/"` with `".ruru/.context/"`
    *   Replace `".ruru/logs/"` with `".ruru/.logs/"`
    *   Replace `".ruru/planning/"` with `".ruru/.planning/"`
    *   Replace `".ruru/reports/"` with `".ruru/.reports/"`
    *   Replace `".ruru/templates/"` with `".ruru/.templates/"`
    *   Replace `".ruru/workflows/"` with `".ruru/.workflows/"`
    *   Replace `".ruru/processes/"` with `".ruru/.processes/"`
    *   Replace `".ruru/archive/"` with `".ruru/.archive/"`
    *   Replace `".ruru/snippets/"` with `".ruru/.snippets/"`
    *   Replace `".ruru/modes/"` with `".ruru/.modes/"`
    *   Replace `".ruru/"` with `".ruru/.roo/"`
    *   Replace `".builds/"` with `".ruru/.builds/"` (If `.builds` is also moved)
    *   Replace `".roomodes"` with `".ruru/.roomodes"` (If `.roomodes` is moved inside `.ruru/`)
    *   **Crucially:** Verify that replacements only affect actual paths and not code examples or explanatory text discussing the *old* paths. Use IDE search/replace tools with preview and confirmation.

5.  **Modify Build Scripts (`build_*.js`, `create_build.js`):**
    *   Update hardcoded path constants at the top of each script to reflect the new structure. Examples:
        *   `build_roomodes.js`: `const MODES_DIR = '.ruru/.modes';`, `const OUTPUT_FILE = '.roomodes';` (Keep `.roomodes` at root unless moved), `const SUMMARY_OUTPUT_FILE = '.ruru/.modes/roo-commander/kb/kb-available-modes-summary.md';`
        *   `create_build.js`: Update `outputDir` if needed. Update `includedFilesAndDirs` and `emptyDirsToCreate` to copy things *from* the `.ruru/` subdirectories *into* the staging build folder, maintaining the desired structure *within the final zip*. The zip file itself should probably still contain the folders directly at its root (e.g., `.modes/`, `.roo/`) for user convenience upon extraction, meaning the script needs to copy from `.ruru/.modes` to `staging/.modes`, etc.
    *   **`.rurumodes` Generation:** Ensure `build_roomodes.js` generates the correct *relative* paths for `kb_path` and `custom_instructions_path` within the `.rurumodes` file, assuming Roo Code resolves them relative to the workspace root. Examples *assuming `.modes` and `.roo` are inside `.ruru`*:
        *   `kb_path` should likely be `".ruru/.modes/<slug>/kb"`
        *   `custom_instructions_path` should likely be `".ruru/.roo/rules-<slug>/"`

6.  **Update `.gitignore`:** Ensure patterns correctly ignore files within the new `.ruru/` subdirectories if necessary (e.g., `.ruru/.context/`, `.ruru/.logs/`).

7.  **Update Core Documentation:**
    *   `README.md`: Update installation instructions (extracting into root will now create `.ruru/`).
    *   `.ruru/.docs/standards/project_structure_inventory.md`: Rewrite to reflect the new structure under `.ruru/`.
    *   `.ruru/.roo/rules/02-workspace-default-folders.md`: Update to list paths relative to `.ruru/` or explain the new structure.

8.  **Thorough Testing:**
    *   Run build scripts (`build_roomodes.js`, `create_build.js`). Verify outputs (`.roomodes`, summary file, build zip).
    *   **CRITICAL:** Test core Roo Commander workflows (onboarding, simple delegation, MDTM delegation, ADR creation, logging) extensively. Verify that modes can find their rules, KBs, and target directories correctly. Check paths used in tool commands.