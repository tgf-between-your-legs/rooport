# Sub-Task: Refine Mode - 040-asst-context-resolver.mode.md

**Master Task:** project_journal/tasks/TASK-PM-20250413-090710-v7-mode-refinement.md
**Status:** Complete ✅
**Coordinator:** roo-commander
**Assigned To:** technical-writer
**Mode File:** 04x-assistant/context-resolver/040-asst-context-resolver.mode.md

## Goal
Review and update the specified mode file to ensure consistency, completeness, and alignment with v7 standards and the hybrid context strategy, as detailed in `v7.0/future-planning/current-status-and-mode-refinement-plan.md` (Section 2, Step 29).

## Acceptance Criteria
- All standard sections from `v7.0/templates/mode_template.md` are present.
- Emoji is assigned/verified.
- Core content (Description, Capabilities, Workflow, Role Definition) is accurate and detailed.
- Custom Instructions (1-6) are populated and aligned with principles.
- Metadata (Level, Tags, Categories, Stack, Delegates To, Escalates To, Reports To, API Config) is validated and updated.
- Potential `.roo/context/` needs are identified and documented.
- Task status is updated to Complete ✅ upon successful review and update.

## Checklist
- [x] Read the entire mode file (`read_file 04x-assistant/context-resolver/040-asst-context-resolver.mode.md`).
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
- [x] Identify potential `.roo/context/context-resolver/` needs.
- [x] Apply changes to the mode file (using `apply_diff` or `write_to_file`).
- [x] Mark task as complete.

## Notes
*   Reference `v7.0/future-planning/current-status-and-mode-refinement-plan.md` for detailed scope.
*   Reference `v7.0/templates/mode_template.md` for section structure.
*   Reference `v7.0/templates/mode_hierarchy.md` for reporting/delegation structure.
*   Reference `v7.0/future-planning/mode-manifest-org-chart.md` (draft) for context.

## Completion Notes

The Context Resolver mode file has been successfully updated to align with v7 standards and the hybrid context strategy. Key changes include:

1. Enhanced the Description to emphasize the mode's role as the primary information retrieval service
2. Added capability to access both `project_journal/` and `.roo/context/` directories
3. Updated the Workflow to include checking both directories
4. Expanded the Role Definition to emphasize the mode's service to other modes
5. Added instructions to check mode-specific context in `.roo/context/{mode-slug}/` directories
6. Enhanced the Example Summary Structure section with examples for both project tasks and mode capabilities
7. Updated the Escalates To section to include `product-manager`
8. Changed `project-manager` to `product-manager` in the Reports To section

### Potential `.roo/context/context-resolver/` Needs

The Context Resolver mode would benefit from the following context files:

1. `.roo/context/context-resolver/summary-templates.md` - A collection of standardized summary templates for different types of information (tasks, decisions, capabilities, etc.)
2. `.roo/context/context-resolver/common-project-structures.md` - Documentation of common project directory structures and file naming conventions
3. `.roo/context/context-resolver/mode-knowledge-map.md` - A map of which modes typically have what types of knowledge in their context directories