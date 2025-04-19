# Sub-Task: Refine Mode - 040-asst-research-context-builder.mode.md

**Master Task:** project_journal/tasks/TASK-PM-20250413-090710-v7-mode-refinement.md
**Status:** Complete ✅
**Coordinator:** roo-commander
**Assigned To:** technical-writer
**Mode File:** 04x-assistant/research-context-builder/040-asst-research-context-builder.mode.md

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
- [x] Read the entire mode file (`read_file 04x-assistant/research-context-builder/040-asst-research-context-builder.mode.md`).
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
- [x] Identify potential `.roo/context/research-context-builder/` needs.
- [x] Apply changes to the mode file (using `apply_diff` or `write_to_file`).
- [x] Mark task as complete. ✅

## Notes
*   Reference `v7.0/future-planning/current-status-and-mode-refinement-plan.md` for detailed scope.
*   Reference `v7.0/templates/mode_template.md` for section structure.
*   Reference `v7.0/templates/mode_hierarchy.md` for reporting/delegation structure.
*   Reference `v7.0/future-planning/mode-manifest-org-chart.md` (draft) for context.

## Potential `.roo/context/` Needs
The Research Context Builder mode could benefit from the following context files:

1. `.roo/context/research-context-builder/research_methodologies.md` - A comprehensive guide to research methodologies, evaluation criteria, and best practices.
2. `.roo/context/research-context-builder/citation_styles.md` - Reference guide for various citation styles and formats.
3. `.roo/context/research-context-builder/credibility_assessment.md` - Framework for evaluating source credibility and reliability.
4. `.roo/context/research-context-builder/report_templates.md` - Templates for different types of research reports and summaries.

## Completion Summary
Updated the Research Context Builder mode file to align with v7 standards. Key changes included:
- Updated Level field to use the full identifier format (04x-assistant)
- Standardized formatting for Categories, Stack, Delegates To, Escalates To, and Reports To sections
- Fixed emoji display issue in the workflow section
- Ensured all sections match the template structure
- Identified potential `.roo/context/` needs for the mode