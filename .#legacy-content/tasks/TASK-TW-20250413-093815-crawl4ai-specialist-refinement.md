# Sub-Task: Refine Mode - 040-asst-crawl4ai-specialist.mode.md

**Master Task:** project_journal/tasks/TASK-PM-20250413-090710-v7-mode-refinement.md
**Status:** Complete ✅
**Coordinator:** roo-commander
**Assigned To:** technical-writer
**Mode File:** 04x-assistant/crawl4ai-specialist/040-asst-crawl4ai-specialist.mode.md

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
- [x] Read the entire mode file (`read_file 04x-assistant/crawl4ai-specialist/040-asst-crawl4ai-specialist.mode.md`).
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
- [x] Identify potential `.roo/context/crawl4ai-specialist/` needs.
- [x] Apply changes to the mode file (using `apply_diff` or `write_to_file`).
- [x] Mark task as complete. 📣

## Notes
*   Reference `v7.0/future-planning/current-status-and-mode-refinement-plan.md` for detailed scope.
*   Reference `v7.0/templates/mode_template.md` for section structure.
*   Reference `v7.0/templates/mode_hierarchy.md` for reporting/delegation structure.
*   Reference `v7.0/future-planning/mode-manifest-org-chart.md` (draft) for context.

## Summary of Changes
- Verified the spider emoji (🕷️) is appropriate for the Crawl4AI Specialist mode.
- Confirmed all standard sections are present and properly formatted.
- Reviewed and validated all core content sections (Description, Capabilities, Workflow, Role Definition).
- Reviewed and validated all Custom Instructions sections (1-6).
- Updated section 6 (Context / Knowledge Base) to reference `.roo/context/crawl4ai-specialist/` files instead of `project_journal/context/` according to the hybrid context strategy.
- Identified potential `.roo/context/crawl4ai-specialist/` needs:
  * crawl4ai-docs.md
  * asyncio-concepts.md
  * crawling-best-practices.md
  * browser-automation.md
  * html-css-selectors.md
- Validated all metadata fields and confirmed they align with v7 standards.
- Standardized Tool Groups section to use the standard v7.0 format.
- Confirmed API Configuration is set to the standard `gemini-2.5-pro`.