# Plan: Convert v6.3 Mode Definitions to v7.0 Markdown Format

**Goal:** Convert all v6.3 mode definitions (JSON) into the new v7.0 Markdown format.

**Status:** Planning Complete

**Coordinator:** `roo-commander`

**Source Files:**
*   Mode Definitions: `v6.3/modes/*.json`
*   Descriptions/Capabilities/Workflows: `v6.3/description-capabilities-workflow/*.json`

**Template:** `v7.0/templates/mode_template.md`

**Target Directory:** `v7.0/modes/md/`

**Process Overview:**

1.  **Identify Modes:** Compile a list of all unique mode slugs present in both `v6.3/modes/` and `v6.3/description-capabilities-workflow/`. Handle any discrepancies (modes present in one but not the other).
2.  **Create Task List:** Generate a detailed task list (`project_journal/tasks/mode_conversion_tasks.md`) with one task per mode conversion.
3.  **Delegate Conversion Tasks:** For each mode:
    *   Delegate a task (potentially using MDTM workflow if deemed complex, or simple `new_task` if straightforward) to a suitable specialist (e.g., `technical-writer` or `mode-maintainer` if available).
    *   The task will involve:
        *   Reading the corresponding `.json` file from `v6.3/modes/`.
        *   Reading the corresponding `.json` file from `v6.3/description-capabilities-workflow/`.
        *   Reading the template file `v7.0/templates/mode_template.md`.
        *   Populating the template with data extracted from the two JSON files.
        *   Handling the extraction and structuring of `customInstructions` into the specified sections (this might require careful parsing or a dedicated sub-task).
        *   Writing the resulting Markdown content to `v7.0/modes/md/[mode_slug].md`.
4.  **Review and Verify:** Once all tasks are complete, review the generated Markdown files for accuracy and completeness against the template and source JSONs.
5.  **Address Missing Information (Future Phase):** As noted in the initial request, filling in any missing information (e.g., sections requiring manual input or further definition) will be handled in a subsequent phase.

**Next Steps:**
*   Create the detailed task list in `project_journal/tasks/mode_conversion_tasks.md`.