# Standard Operating Procedure (SOP): Migrating Modes (v7.0 -> v7.1) - v3 (Multi-Delegation)

**Version:** 3.0
**Date:** 2025-04-16
**Status:** Active

**Objective:** To provide a reliable, step-by-step process for migrating existing v7.0 Roo Commander modes to the **v7.1 source structure**, using a **template-first, multi-delegation approach** to improve schema adherence and manage context limitations. This source structure requires a separate build process to generate runtime files.

**Reference Documents:**
*   `.templates/modes/mode_specification.md` (Defines v7.1 schema)
*   `.templates/modes/example_mode_template/mode.md` (Base template for copying)
*   `.roo/rules/00-standard-toml-md-format.md` (Defines TOML+MD format rules)
*   `.processes/acqa-process.md` (Defines QA principles)
*   `.processes/afr-process.md` (Defines Adaptive Failure Resolution)
*   `.processes/pal-process.md` (Defines Process Assurance Lifecycle)

**Inputs:**
*   **Source Material Paths (Verified by Coordinator):**
    *   Path to existing v7.0 primary mode definition file.
    *   Path to existing v7.0 `custom-instructions` directory (if exists).
*   **Mode Identification (Provided/Confirmed by Coordinator):**
    *   `id`, `name`, `classification`, `domain`, `sub_domain` (optional).
*   **Target Directory Path (Determined by Coordinator):** `v7.1/modes/[classification]/[domain]/` (add `[sub_domain]/` if applicable) `/[id]/`.
*   **Target Definition Filename (Determined by Coordinator):** `{id}.mode.md`.
*   **Base Template Path:** `.templates/modes/example_mode_template/mode.md`.

**Process:**

**Phase 1: Preparation (Coordinator Tasks)**

1.  **Identify Source & Target:**
    *   Obtain source info from user/request. Confirm target ID, name, classification, domain, sub-domain. Determine target directory path and definition filename.

2.  **Verify Inputs & Create Target Directory:**
    *   **Verify Source Paths:** Use `list_files` on the v7.0 mode directory to verify exact source filenames/paths. Handle cases where source files might be missing or named unexpectedly, potentially querying the user via `ask_followup_question`.
    *   **Verify Template:** Confirm the base template file (`.templates/modes/example_mode_template/mode.md`) exists using `read_file` (check for success/failure, not content). Report error if missing.
    *   **Create Target Directory:** Although `write_to_file` often creates directories, explicitly ensure the target directory (`v7.1/modes/[...]/[id]/`) exists. Use `execute_command` with `mkdir -p [target_directory_path]` if needed.

3.  **Read Base Template Content:**
    *   Use `read_file` to load the content of the base template (`.templates/modes/example_mode_template/mode.md`) into Coordinator context.

**Phase 2: Initial File Creation (Delegated)**

4.  **Delegate Task 1: Copy Template (Coordinator -> `mode-maintainer`)**
    *   **Action:** Create the initial target definition file using the base template content.
    *   **Tool:** `new_task`
    *   **Inputs Provided:** Target filename (`{id}.mode.md`), Base template content (from Coordinator Step 3).
    *   **Instructions:** "Using the provided content, write it to the target file path: `[Target Definition Filename]`." (Specify `write_to_file` usage).
    *   **Expected Output:** Confirmation of file creation.
    *   **Coordinator Action:** Wait for confirmation. Handle errors.

**Phase 3: Source Reading & TOML Population (Delegated)**

5.  **Delegate Task 2: Read Source & Populate TOML (Coordinator -> `mode-maintainer`)**
    *   **Action:** Read source files and populate the TOML frontmatter of the target definition file.
    *   **Tool:** `new_task`
    *   **Inputs Provided:** Verified source paths (v7.0 file, `custom-instructions` dir if exists), Target definition filename, Mapping/Defaulting strategy (summarized below), Path to Mode Specification, Path to TOML+MD Rule.
    *   **Instructions:**
        1.  "Read the primary source definition file: `[Verified v7.0 Path]`."
        2.  "If `[Verified v7.0 custom-instructions Path]` exists, list and read all `.md` files within it."
        3.  "Read the target definition file: `[Target Definition Filename]`."
        4.  "Modify the TOML frontmatter (`+++...+++`) of the target file, replacing placeholders/defaults based on the source content and the following strategy:"
            *   "Map `id`, `name`, `classification` from Coordinator info (source: v7.0 `slug`, `name`, `level`)."
            *   "Set `version` to '1.0.0'."
            *   "Set `domain` based on Coordinator info."
            *   "Map/Extract `summary` (from v7.0 `description` or Markdown)."
            *   "Extract `system_prompt` (from v7.0 Markdown body)."
            *   "Set `custom_instructions_source_dir` to 'custom-instructions'."
            *   "Populate `metadata.*`, `file_access.*`, etc., from source if fields match v7.1 spec (`.templates/modes/mode_specification.md`). Use workspace-relative paths."
            *   "If other REQUIRED fields are missing, use placeholder `<<< MISSING_DATA >>>`."
        5.  "Strictly adhere to TOML syntax within `+++` delimiters (see `.roo/rules/00-standard-toml-md-format.md`)."
        6.  "Save changes using `apply_diff` (preferred for targeted changes) or `write_to_file` (if extensive changes)."
        7.  "Report completion and any fields set to `<<< MISSING_DATA >>>`."
    *   **Expected Output:** Confirmation of TOML update, list of fields set to `<<< MISSING_DATA >>>`, Confidence Score (future ACQA).
    *   **Coordinator Action:** Wait for confirmation. Handle errors. **Review missing data flags:** Decide whether to query user for missing info now or proceed and flag for later review. Update Coordinator state.

**Phase 4: Markdown Body Population (Delegated)**

6.  **Delegate Task 3: Populate Markdown Body (Coordinator -> `mode-maintainer`)**
    *   **Action:** Populate the Markdown body sections of the target definition file.
    *   **Tool:** `new_task`
    *   **Inputs Provided:** Target definition filename, Verified primary source v7.0 path.
    *   **Instructions:**
        1.  "Read the target definition file: `[Target Definition Filename]`."
        2.  "Read the primary source definition file: `[Verified v7.0 Path]`."
        3.  "Extract content from the source file's Markdown body corresponding to sections like Description, Capabilities, etc."
        4.  "Replace the placeholder sections in the target file's Markdown body with the extracted/synthesized content using `apply_diff`."
        5.  "Report completion."
    *   **Expected Output:** Confirmation of Markdown update, Confidence Score (future ACQA).
    *   **Coordinator Action:** Wait for confirmation. Handle errors. Update Coordinator state.

**Phase 5: Subdirectory Population (Delegated)**

7.  **Delegate Task 4: Process Subdirectories (Coordinator -> `mode-maintainer`)**
    *   **Action:** Analyze source instructions and create `custom-instructions`, `context`, and `examples` files.
    *   **Tool:** `new_task`
    *   **Inputs Provided:** Target base directory path, Verified source paths (v7.0 file, `custom-instructions` dir), Synthesized external context summary (if generated previously by Coordinator - *Note: External context step removed from this SOP version*).
    *   **Instructions:**
        1.  "Analyze all source instruction material (from `[Verified v7.0 Path]` body and files in `[Verified v7.0 custom-instructions Path]`, plus any provided external context summary)."
        2.  "Group instructions into logical themes (e.g., Principles, Workflow, Collaboration, Safety, Error Handling, Tool Usage, specific APIs/techniques)."
        3.  "Create separate, numbered files (e.g., `01-principles.md`) in `[Target Base Path]/custom-instructions/` for each theme using `write_to_file`. Ensure content is focused and uses workspace-relative paths."
        4.  "Create/Update `[Target Base Path]/custom-instructions/README.md` listing the created files and their purpose using `write_to_file`."
        5.  "Create placeholder `README.md` in `[Target Base Path]/context/` using `write_to_file`."
        6.  "If `context_files` were defined in TOML or external context provided, create those files in `[Target Base Path]/context/` using `write_to_file`."
        7.  "Create placeholder `README.md` in `[Target Base Path]/examples/` using `write_to_file`."
        8.  "Report completion and list of files created."
    *   **Expected Output:** Confirmation, list of created files, Confidence Score (future ACQA).
    *   **Coordinator Action:** Wait for confirmation. Handle errors. Update Coordinator state (migration phase complete).

**Phase 6: Quality Assurance (Coordinator)**

8.  **Initiate QA Review:** Trigger review of the completed mode source structure.
9.  **Delegate Review Task:** Assign to QA agent providing full context (mode path, specs, rules).
10. **Receive QA Feedback:** Obtain structured feedback.
11. **Critically Analyze Feedback & Detect Patterns (Coordinator Task):** Evaluate feedback validity against specs. Check for recurring error patterns across modes (as per AFR process - `.processes/afr-process.md`). Escalate for meta-review if patterns detected.
12. **Initiate Revisions (Coordinator Task, if Necessary):** Delegate specific fixes back to `mode-maintainer` (looping back to appropriate Task # above, e.g., Task 2 for TOML, Task 3 for Body, Task 4 for Instructions) based on validated feedback. Repeat QA cycle (Steps 8-12) if needed.

**Phase 7: Completion (Coordinator)**

13. **Final Check:** Ensure all artifacts are correct and compliant.
14. **Report Completion:** Use `attempt_completion`, summarize process, mention QA results, remind about build step.

**Error Handling:** Stop on failure of any step (Coordinator or Delegated), report error. Coordinator analyzes QA feedback critically before initiating revisions. Coordinator escalates recurring patterns via AFR.