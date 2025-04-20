# Sub-Task: Refine Mode - 050-footgun-debug.mode.md

**Master Task:** project_journal/tasks/TASK-PM-20250413-090710-v7-mode-refinement.md
**Status:** Complete ✅
**Coordinator:** roo-commander
**Assigned To:** technical-writer
**Mode File:** 05x-footgun/debug/050-footgun-debug.mode.md

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
- [x] Read the entire mode file (`read_file 05x-footgun/debug/050-footgun-debug.mode.md`).
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
- [x] Identify potential `.roo/context/debug/` needs.
- [x] Apply changes to the mode file (using `apply_diff` or `write_to_file`).
- [x] Mark task as complete. 📣

## Notes
*   Reference `v7.0/future-planning/current-status-and-mode-refinement-plan.md` for detailed scope.
*   Reference `v7.0/templates/mode_template.md` for section structure.
*   Reference `v7.0/templates/mode_hierarchy.md` for reporting/delegation structure.
*   Reference `v7.0/future-planning/mode-manifest-org-chart.md` (draft) for context.

## Potential `.roo/context/debug/` Needs
The Footgun Debug mode could benefit from the following context files:

1. `.roo/context/debug/common-error-patterns.md` - A knowledge base of common error patterns and diagnostic approaches for different programming languages
2. `.roo/context/debug/diagnostic-commands.md` - Templates for debugging commands across various environments and platforms
3. `.roo/context/debug/log-analysis-patterns.md` - Techniques and patterns for analyzing different types of logs
4. `.roo/context/debug/troubleshooting-trees.md` - Decision trees for systematic troubleshooting of common issues

## Completion Summary
**Status:** ✅ Complete
**Outcome:** Success
**Summary:** Updated the Footgun Debug mode file to align with v7 standards. Restructured the file to match the template format, fixed the capitalization of "level" in the frontmatter, added "diagnostics" to tags, and identified potential `.roo/context/debug/` needs. The mode now follows the standard structure with proper sections and metadata.