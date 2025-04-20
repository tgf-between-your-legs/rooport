# Sub-Task: Refine Mode - 033-work-db-mysql-specialist.mode.md

**Master Task:** project_journal/tasks/TASK-PM-20250413-090710-v7-mode-refinement.md
**Status:** Complete ✅
**Coordinator:** roo-commander
**Assigned To:** technical-writer
**Mode File:** 03x-worker/033-database/mysql-specialist/033-work-db-mysql-specialist.mode.md

## Goal
Review and update the specified mode file to ensure consistency, completeness, and alignment with v7 standards and the hybrid context strategy, as detailed in `v7.0/future-planning/current-status-and-mode-refinement-plan.md` (Section 2, Step 29).

## Acceptance Criteria
- All standard sections from `v7.0/templates/mode_template.md` are present.
- Emoji is assigned/verified.
- Core content (Description, Capabilities, Workflow, Role Definition) is accurate and detailed.
- Custom Instructions (1-6) are populated and aligned with principles.
- Metadata (Level, Tags, Categories, Stack, Delegates To, Escalates To, Reports To, API Config) is validated and updated.
- Potential `.roo/context/` needs are identified.
- Task status is updated to Complete ✅ upon successful review and update.

## Checklist
- [x] Read the entire mode file (`read_file 03x-worker/033-database/mysql-specialist/033-work-db-mysql-specialist.mode.md`).
- [x] Verify/Assign standard emoji in `name` field.
- [x] Ensure standard sections are present (add placeholders if needed).
- [x] Review/Update Description.
- [x] Review/Update Capabilities.
- [x] Review/Update Workflow.
- [x] Review/Update Role Definition.
- [x] Review/Update Custom Instructions (Sections 1-6).
- [x] Validate/Update Metadata: Level.
- [x] Validate/Update Metadata: Tags.
- [x] Validate/Update Metadata: Categories.
- [x] Validate/Update Metadata: Stack.
- [x] Validate/Update Metadata: Delegates To (based on full v7 mode set).
- [x] Validate/Update Metadata: Escalates To (based on full v7 mode set).
- [x] Validate/Update Metadata: Reports To (based on full v7 mode set).
- [x] Standardize Metadata: API Configuration (default: `gemini-2.5-pro`).
- [x] Identify potential `.roo/context/mysql-specialist/` needs.
- [x] Apply changes to the mode file (using `apply_diff` or `write_to_file`).
- [x] Mark task as complete. 📣

## Notes
*   Reference `v7.0/future-planning/current-status-and-mode-refinement-plan.md` for detailed scope.
*   Reference `v7.0/templates/mode_template.md` for section structure.
*   Reference `v7.0/templates/mode_hierarchy.md` for reporting/delegation structure.
*   Reference `v7.0/future-planning/mode-manifest-org-chart.md` (draft) for context.

## Summary of Changes
* Restructured the mode file to follow the standard template format from `v7.0/templates/mode_template.md`
* Verified the MySQL Specialist emoji (🐬) is appropriate and retained
* Reorganized core content (Description, Capabilities, Workflow, Role Definition) for clarity and completeness
* Structured Custom Instructions into the 6 standard sections
* Added Categories metadata field with appropriate values
* Added Delegates To metadata field with `technical-writer` for documentation tasks
* Standardized API Configuration to use `gemini-2.5-pro`
* Identified potential `.roo/context/mysql-specialist/` needs for MySQL documentation, project schema reference, common query patterns, migration strategy, SQL best practices, normalization principles, and optimization techniques
* Updated references from `project_journal/context/` to `.roo/context/mysql-specialist/` for the hybrid context strategy