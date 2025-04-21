+++
id = "CTX-RURU-REFACTOR-IMPL-GUIDE"
title = "Roo Commander Path Refactor: Implementation Guide & Impacted Areas"
context_type = "implementation_guide"
scope = "Detailed list of required changes across the codebase"
target_audience = ["ai_dev_team", "roo-commander"]
granularity = "detailed"
status = "proposal"
last_updated = "2025-04-21"
tags = ["refactoring", "configuration", "paths", "ruru", "implementation", "checklist"]
+++

# Roo Commander Path Refactor: Implementation Guide & Impacted Areas

This document outlines the necessary changes across the Roo Commander codebase to implement configurable paths using the `ruru.config.toml` file and placeholder substitution.

**1. Create `ruru.config.toml`:**
*   Create the central configuration file at the workspace root with the structure defined in the Architecture document.

**2. Create/Adapt Substitution Script (`substitute-paths.js`):**
*   Develop the Node.js script capable of parsing `ruru.config.toml`, finding target Markdown files, performing placeholder substitution (`{{RURU_...}}`), and writing processed files to a designated output directory.

**3. Modify Build Scripts:**
*   **`build_roomodes.js`:**
    *   Read `ruru.config.toml` to get `modes_root`, `rules_root`, `modes_file`.
    *   Use `modes_root` to locate the `.modes` directory.
    *   Use `modes_file` for the output path.
    *   When generating the `customModes` array for `.rurumodes`, dynamically construct the `kb_path` (e.g., `{MODES_ROOT}/{slug}/kb`) and `custom_instructions_path` (e.g., `{RULES_ROOT}/rules-{slug}/`) based on the config values for *each mode*. Ensure these generated paths are relative to the workspace root as expected by Roo Code.
*   **`build_mode_summary.js`:**
    *   Read `ruru.config.toml` to get `modes_root` and `mode_summary_file`.
    *   Use `modes_root` to find mode directories.
    *   Use `mode_summary_file` as the output path.
*   **`create_build.js`:**
    *   Read `ruru.config.toml` to get `builds_dir` and paths for included/excluded items relative to the workspace root.
    *   Adapt the logic to copy files *from their configured locations* into the temporary staging directory.
    *   Adapt the `emptyDirsToCreate` logic based on the configured paths.

**4. Update Templates (`.templates/`):**
*   Replace hardcoded paths (e.g., `.tasks/`, `.docs/`, `.templates/toml-md/...README.md`) in TOML blocks and Markdown content with placeholders (`{{RURU_TASKS_DIR}}`, `{{RURU_DOCS_DIR}}`, etc.).
*   Pay special attention to `template_schema_doc` paths.

**5. Update Rules Files (`.roo/rules/`, `.roo/rules-<slug>/`):**
*   **Action:** Replace *all* hardcoded path references (e.g., `.tasks/`, `.decisions/`, `.modes/roo-commander/kb/`, `.templates/`) with corresponding placeholders (`{{RURU_TASKS_DIR}}`, `{{RURU_DECISIONS_DIR}}`, `{{RURU_MODES_ROOT}}/roo-commander/kb/`, `{{RURU_TEMPLATES_DIR}}`).
*   **KB Lookup Rules:** Update the `kb_directory` field to use placeholders, e.g., `kb_directory = "{{RURU_MODES_ROOT}}/{{MODE_SLUG}}/kb"`. Ensure the substitution script can handle the `{{MODE_SLUG}}` context or that these rules are processed specifically.

**6. Update Knowledge Base Files (`.modes/**/kb/*.md`):**
*   **Action:** This requires the most extensive changes. Systematically replace *all* hardcoded path references to standard directories, other KB files, rules, templates, etc., with the appropriate `{{RURU_...}}` placeholders.
*   **Example:** `"Log the goal to {{RURU_TASKS_DIR}}/[TaskID].md"`.

**7. Update Mode Definitions (`.modes/**/*.mode.md`):**
*   **TOML:**
    *   Remove `kb_path`, `custom_instructions_path` if they will be dynamically generated into `.rurumodes` or handled differently by Roo Code.
    *   Review `context_files`, `documentation_urls`, `related_docs`, `file_access` patterns. Replace internal workspace paths with placeholders where appropriate. Be cautious with `file_access` patterns – complex globs might be hard to make dynamic via simple placeholders.
*   **System Prompt/Markdown:** Replace hardcoded paths (especially KB references) with placeholders. E.g., `KB located in {{RURU_MODES_ROOT}}/<your-mode-slug>/kb/`.

**8. Update Core Documentation:**
*   **`README.md`:** Update installation instructions to include running the substitution script or using a pre-processed build.
*   **`.docs/standards/project_structure_inventory.md`:** Rewrite to explain the *configurable* structure based on `ruru.config.toml`.
*   **`.roo/rules/02-workspace-default-folders.md`:** Update to refer to `ruru.config.toml` as the source of truth.

**9. Testing:**
*   Test the substitution script thoroughly.
*   Test the build scripts (`build_roomodes.js`, etc.) with different `ruru.config.toml` settings.
*   Test Roo Commander's core workflows (onboarding, delegation) with both root-level and nested (`workspace_base = ".ruru"`) configurations.
*   Test specific modes that heavily rely on path interactions.