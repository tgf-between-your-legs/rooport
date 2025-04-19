# Sub-Task: Refine Mode - 020-lead-be-backend-lead.mode.md

**Master Task:** project_journal/tasks/TASK-PM-20250413-090710-v7-mode-refinement.md
**Status:** Complete ✅
**Coordinator:** roo-commander
**Assigned To:** technical-writer
**Mode File:** 02x-lead/backend/backend-lead/020-lead-be-backend-lead.mode.md

## Goal
Review and update the specified mode file to ensure consistency, completeness, and alignment with v7 standards and the hybrid context strategy, as detailed in `v7.0/future-planning/current-status-and-mode-refinement-plan.md` (Section 2, Step 29).

## Acceptance Criteria
- ✅ All standard sections from `v7.0/templates/mode_template.md` are present.
- ✅ Emoji is assigned/verified (⚙️).
- ✅ Core content (Description, Capabilities, Workflow, Role Definition) is accurate and detailed.
- ✅ Custom Instructions (1-6) are populated and aligned with principles.
- ✅ Metadata (Level, Tags, Categories, Stack, Delegates To, Escalates To, Reports To, API Config) is validated and updated.
- ✅ Potential `.roo/context/` needs are identified.
- ✅ Task status is updated to Complete.

## Checklist
- [x] Read the entire mode file (`read_file 02x-lead/backend/backend-lead/020-lead-be-backend-lead.mode.md`).
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
- [x] Identify potential `.roo/context/backend-lead/` needs.
- [x] Apply changes to the mode file (using `apply_diff` or `write_to_file`).
- [x] Mark task as complete.

## Notes
*   Reference `v7.0/future-planning/current-status-and-mode-refinement-plan.md` for detailed scope.
*   Reference `v7.0/templates/mode_template.md` for section structure.
*   Reference `v7.0/templates/mode_hierarchy.md` for reporting/delegation structure.
*   Reference `v7.0/future-planning/mode-manifest-org-chart.md` (draft) for context.

## Identified Context Needs
Recommended `.roo/context/backend-lead/` contents:
- API design templates and best practices
- Security checklists (OWASP Top 10, etc.)
- Code review guidelines for backend systems
- Common backend patterns and architectures
- Performance optimization guidelines
- Error handling and logging standards
- Integration patterns with databases and external services

## Changes Made
1. Reorganized content to match template structure
2. Separated Role Definition from initial content
3. Properly numbered Custom Instructions sections (1-6)
4. Streamlined workflow steps for clarity
5. Maintained all essential information while improving organization
6. Added comprehensive context needs identification
7. Verified and validated all metadata fields
8. Ensured consistent formatting throughout