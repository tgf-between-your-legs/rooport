# Sub-Task: Refine Mode - 040-asst-firecrawl-specialist.mode.md

**Master Task:** project_journal/tasks/TASK-PM-20250413-090710-v7-mode-refinement.md
**Status:** Complete ✅
**Coordinator:** roo-commander
**Assigned To:** technical-writer
**Mode File:** 04x-assistant/firecrawl-specialist/040-asst-firecrawl-specialist.mode.md

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
- [x] Read the entire mode file (`read_file 04x-assistant/firecrawl-specialist/040-asst-firecrawl-specialist.mode.md`).
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
- [x] Identify potential `.roo/context/firecrawl-specialist/` needs.
- [x] Apply changes to the mode file (using `apply_diff` or `write_to_file`).
- [x] Mark task as complete.

## Notes
*   Reference `v7.0/future-planning/current-status-and-mode-refinement-plan.md` for detailed scope.
*   Reference `v7.0/templates/mode_template.md` for section structure.
*   Reference `v7.0/templates/mode_hierarchy.md` for reporting/delegation structure.
*   Reference `v7.0/future-planning/mode-manifest-org-chart.md` (draft) for context.

## Identified `.roo/context/` Needs
The following potential context files could be created for the Firecrawl Specialist mode:

1. `.roo/context/firecrawl-specialist/api-reference.md` - Detailed API reference documentation including all endpoints, parameters, and response formats.
2. `.roo/context/firecrawl-specialist/example-payloads.json` - Example JSON payloads for different types of requests (scrape, crawl) with various configuration options.
3. `.roo/context/firecrawl-specialist/error-handling-guide.md` - Comprehensive guide for handling common API errors and troubleshooting steps.

## Completion Summary
The Firecrawl Specialist mode file has been reviewed and updated to ensure alignment with v7 standards. The file already had a well-structured format with all required sections present. The emoji (🔥) was verified as appropriate for the mode. The Tool Groups section was standardized to match the template format. Potential `.roo/context/` needs were identified to enhance the mode's capabilities with specialized knowledge bases.