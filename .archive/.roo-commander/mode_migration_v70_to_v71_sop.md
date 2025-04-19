# Standard Operating Procedure (SOP): Migrating Modes from v7.0 to v7.1 Source Structure

**Version:** 2.0
**Date:** 2025-04-16
**Status:** Active

**Objective:** To provide a reliable, step-by-step process for migrating existing v7.0 Roo Commander modes to the **v7.1 source structure**, using a **template-first approach** to improve schema adherence. This source structure requires a separate build process to generate runtime files.

**Reference Documents:**
*   `.templates/modes/mode_specification.md` (Defines v7.1 schema)
*   `.templates/modes/example_mode_template/mode.md` (Base template for copying)
*   `.roo/rules/00-standard-toml-md-format.md` (Defines TOML+MD format rules)
*   `.processes/acqa-process.md` (Defines QA principles)
*   `.processes/afr-process.md` (Defines Adaptive Failure Resolution)
*   `.processes/pal-process.md` (Defines Process Assurance Lifecycle)

**Inputs:**
*   **Source Material:**
    *   Path to existing v7.0 primary mode definition file (verified by Coordinator).
    *   Path to existing v7.0 `custom-instructions` directory (verified by Coordinator, if exists).
    *   List of relevant external URLs (optional, provided by Coordinator).
*   **Mode Identification:** (Provided/Confirmed by Coordinator)
    *   `id`, `name`, `classification`, `domain`, `sub_domain` (optional).

**Process:**

**Phase 1: Preparation & Template Copy**

1.  **Identify Source & Target (Coordinator Task):**
    *   Obtain source material info from user/request.
    *   Confirm target `id`, `name`, `classification`, `domain`, `sub_domain`.
    *   Determine target directory path: `v7.1/modes/[classification]/[domain]/` (add `[sub_domain]/` if applicable) `/[id]/`.
    *   Determine target definition filename: `{id}.mode.md` (e.g., `context-resolver.mode.md`).

2.  **Verify Inputs & Create Target Directory (Coordinator Task):**
    *   **Verify Source Paths:** Use `list_files` on the specific v7.0 mode directory to verify the exact filename of the primary definition file and the existence/path of any `custom-instructions` directory. Handle cases where source files might be missing or named unexpectedly, potentially querying the user via `ask_followup_question`.
    *   **Verify Template:** Confirm the base template file (`.templates/modes/example_mode_template/mode.md`) exists using `read_file` (check for success/failure, not content). Report error if missing.
    *   **Create Target Directory:** Although `write_to_file` often creates directories, explicitly ensure the target directory (`v7.1/modes/[...]/[id]/`) exists. Use `execute_command` with `mkdir -p [target_directory_path]` if needed.

3.  **Copy Base Template (Coordinator delegates to `mode-maintainer`):**
    *   **Action:** Copy the content of the base template file (`.templates/modes/example_mode_template/mode.md`) to the new target file path (`v7.1/modes/[...]/[id]/{id}.mode.md`).
    *   **Tool:** `read_file` (on template) then `write_to_file` (to target path, ensuring correct `line_count`).
    *   **Wait for confirmation.**

**Phase 2: Populate Template (`{id}.mode.md`)**

4.  **Read Source Material (Coordinator delegates to `mode-maintainer`):**
    *   Provide **verified exact paths** for v7.0 definition file and `custom-instructions` dir (if exists).
    *   Instruct `mode-maintainer` to read these source files using `read_file` / `list_files`.
    *   **Wait for confirmation.**

5.  **Gather External Context (Coordinator delegates to `mode-maintainer`, if applicable):**
    *   Provide external URLs.
    *   Instruct `mode-maintainer` to fetch/analyze/synthesize content.
    *   **Wait for confirmation.**

6.  **Populate TOML Frontmatter (Coordinator delegates to `mode-maintainer`):**
    *   **Action:** Modify the TOML frontmatter (`+++...+++`) of the newly created target file (`v7.1/modes/[...]/[id]/{id}.mode.md`) by replacing placeholders/defaults with information extracted/mapped from source materials (v7.0 files, external context).
    *   **Tool:** `read_file` (on target file) then `apply_diff` (preferred) or `write_to_file`.
    *   **Mapping & Defaulting Strategy:**
        *   `id`: Use value provided by Coordinator (map from v7.0 `slug` if migrating).
        *   `name`: Use value provided by Coordinator (map from v7.0 `name`).
        *   `version`: Set default `"1.0.0"`.
        *   `classification`: Use value provided by Coordinator (map from v7.0 `level`).
        *   `domain`: Use value provided by Coordinator. If inference is required (e.g., based on directory or function), state the basis clearly in documentation or commit message, e.g., "Inferred 'utility' based on function". Avoid inference if uncertain.
        *   `summary`: Map from v7.0 YAML `description` OR extract first paragraph from v7.0 Markdown `## Description`. If neither exists, attempt to generate a concise summary based on `system_prompt` (e.g., "Extract key responsibilities from system_prompt"). If generation fails or is low quality, use placeholder `summary = "<<< GENERATE_SUMMARY >>>"`.
        *   `system_prompt`: Extract content from v7.0 Markdown body (usually under `## Role Definition` or similar heading).
        *   `custom_instructions_source_dir`: Set default `"custom-instructions"`.
        *   `metadata.*`, `file_access.*`, `allowed_tool_groups`, `config.*`, etc.: Populate from corresponding v7.0 YAML fields if they exist and match the v7.1 schema. Ensure paths (`context_files`, `documentation_urls`) are workspace-relative. Omit optional fields if no source info exists.
    *   **Handling Missing REQUIRED Data:** If a required field (per Mode Spec) cannot be filled via mapping, extraction, or default:
        *   Prioritize using a sensible default if defined (e.g., `version = "1.0.0"`).
        *   If no default, insert a clear placeholder: `field_name = "<<< MISSING_DATA >>>"`.
        *   Note the missing field and placeholder used in the completion report. (This informs ACQA confidence).
        *   Avoid leaving required fields blank.
    *   **Adherence:** Emphasize strict adherence to TOML syntax, `+++` delimiters, and the schema in `.templates/modes/mode_specification.md` and rules in `.roo/rules/`.
    *   **Wait for confirmation.**

7.  **Populate Markdown Body (Coordinator delegates to `mode-maintainer`):**
    *   **Action:** Replace placeholder sections (`## Description`, `## Capabilities`, etc.) in the target file's Markdown body with content extracted/synthesized from the v7.0 source file's Markdown body.
    *   **Tool:** `read_file` (on target file) then `apply_diff` (preferred) or `write_to_file`.
    *   **Wait for confirmation.**

**Phase 3: Create Subdirectories**

8.  **Process Custom Instructions (Coordinator delegates to `mode-maintainer`):**
    *   Analyze **all** source instruction material (v7.0 `{id}.mode.md` body, v7.0 `custom-instructions` files, external context).
    *   **Break down instructions:** Group related instructions into logical themes. Create separate, numbered files in the target `custom-instructions` directory for each theme. Use the recommended pattern as a guide (`01-principles.md`, `02-workflow.md`, `03-collaboration.md`, `04-safety.md`, `05-error-handling.md`), adapting and adding mode-specific files (e.g., `06-tool-usage.md`, `07-api-details.md`) as needed. Ensure content within each file is focused.
    *   Use `write_to_file` for each instruction file and the `README.md`.
    *   **Wait for confirmation** after each file write.

9.  **Process Context Files (Coordinator delegates to `mode-maintainer`):**
    *   Create placeholder `README.md` in the target `context` directory.
    *   If `context_files` were defined or external context synthesized, use `write_to_file` to create those files.
    *   **Wait for confirmation.**

10. **Process Examples (Coordinator delegates to `mode-maintainer`):**
    *   Create placeholder `README.md` in the target `examples` directory.
    *   If examples can be derived, use `write_to_file` to create them.
    *   **Wait for confirmation.**

**Phase 4: Quality Assurance (ACQA - Conceptual)**

11. **Initiate QA Review (Coordinator Task):** Trigger review of the completed mode source structure.
12. **Delegate Review Task (Coordinator Task):** Assign to QA agent (`code-reviewer`, `second-opinion`) providing full context (mode path, Mode Spec path, TOML+MD rule path).
13. **Receive QA Feedback (Coordinator Task):** Obtain structured feedback.
14. **Critically Analyze Feedback & Detect Patterns (Coordinator Task):**
    *   Evaluate feedback validity against specs. Focus on actionable deviations (format errors, schema violations, incorrect paths, contradictions). Distinguish from minor stylistic suggestions unless standards exist.
    *   Check for recurring error patterns across modes (as per AFR process - `.processes/afr-process.md`). Escalate for meta-review if patterns detected.
    *   Acknowledge complexity: Prioritize fixing direct spec violations. Deeper logical or semantic review might require `second-opinion` or human judgment.
15. **Initiate Revisions (Coordinator Task, if Necessary):** Delegate specific fixes to `mode-maintainer` based on validated feedback. Repeat QA cycle if needed.

**Phase 5: Completion**

16. **Final Check (Coordinator Task):** Ensure all artifacts are correct and compliant.
17. **Report Completion (Coordinator Task):** Use `attempt_completion`, summarize process, mention QA results, remind about build step.

**Error Handling:** Stop on failure, report error. Coordinator analyzes QA feedback critically before initiating revisions. Coordinator escalates recurring patterns for meta-review.
