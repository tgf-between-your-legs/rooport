# Sub-Task: Refine Mode - 031-work-fe-accessibility-specialist.mode.md

**Master Task:** project_journal/tasks/TASK-PM-20250413-090710-v7-mode-refinement.md
**Status:** Complete ✅
**Coordinator:** roo-commander
**Assigned To:** technical-writer
**Mode File:** 03x-worker/031-frontend/accessibility-specialist/031-work-fe-accessibility-specialist.mode.md

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
- [x] Read the entire mode file (`read_file 03x-worker/031-frontend/accessibility-specialist/031-work-fe-accessibility-specialist.mode.md`).
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
- [x] Identify potential `.roo/context/accessibility-specialist/` needs.
- [x] Apply changes to the mode file (using `apply_diff` or `write_to_file`).
- [x] Mark task as complete. 📣

## Notes
*   Reference `v7.0/future-planning/current-status-and-mode-refinement-plan.md` for detailed scope.
*   Reference `v7.0/templates/mode_template.md` for section structure.
*   Reference `v7.0/templates/mode_hierarchy.md` for reporting/delegation structure.
*   Reference `v7.0/future-planning/mode-manifest-org-chart.md` (draft) for context.

## Identified `.roo/context/` Needs
The following context files would be valuable for the accessibility-specialist mode:

1. **WCAG Reference (`wcag-guidelines.md`)**
   - Detailed WCAG Success Criteria reference
   - Common implementation patterns for each criterion
   - Best practices and gotchas

2. **Testing Templates (`testing/`)**
   - Screen reader testing checklists
   - Keyboard navigation test scripts
   - Color contrast verification procedures
   - Automated testing tool configurations

3. **Documentation Templates (`templates/`)**
   - VPAT document templates
   - Accessibility audit report templates
   - Issue documentation formats

4. **Common Patterns (`patterns/`)**
   - Reusable ARIA patterns
   - Semantic HTML structures
   - CSS accessibility solutions
   - JavaScript interaction patterns

5. **Tool Configurations (`tools/`)**
   - Axe-core configuration presets
   - Lighthouse accessibility settings
   - Screen reader command references

These context files would enhance the mode's effectiveness by providing quick access to standardized references, templates, and patterns while maintaining clean separation from the main project documentation.