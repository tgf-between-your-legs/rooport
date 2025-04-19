# Sub-Task: Refine Mode - 031-work-fe-remix-developer.mode.md

**Master Task:** project_journal/tasks/TASK-PM-20250413-090710-v7-mode-refinement.md
**Status:** Complete ✅
**Coordinator:** roo-commander
**Assigned To:** technical-writer
**Mode File:** 03x-worker/031-frontend/remix-developer/031-work-fe-remix-developer.mode.md

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
- [x] Read the entire mode file (`read_file 03x-worker/031-frontend/remix-developer/031-work-fe-remix-developer.mode.md`).
- [x] Verify/Assign standard emoji in `name` field (💿 verified).
- [x] Ensure standard sections are present (all sections present).
- [x] Review/Update Description (accurate and detailed).
- [x] Review/Update Capabilities (comprehensive list provided).
- [x] Review/Update Workflow (clear steps outlined).
- [x] Review/Update Role Definition (detailed and accurate).
- [x] Review/Update Custom Instructions (Sections 1-6) (all populated and aligned).
- [x] Validate/Update Metadata: Level (031-worker-frontend).
- [x] Validate/Update Metadata: Tags (comprehensive list).
- [x] Validate/Update Metadata: Categories (Frontend, Fullstack, Worker).
- [x] Validate/Update Metadata: Stack (complete tech stack listed).
- [x] Validate/Update Metadata: Delegates To (None - identifies need for delegation by Lead).
- [x] Validate/Update Metadata: Escalates To (comprehensive list with comments).
- [x] Validate/Update Metadata: Reports To (frontend-lead).
- [x] Standardize Metadata: API Configuration (gemini-2.5-pro).
- [x] Identify potential `.roo/context/remix-developer/` needs.
- [x] Apply changes to the mode file (using `apply_diff` or `write_to_file`).
- [x] Mark task as complete. 📣

## Identified Context Needs
The following context resources should be considered for `.roo/context/remix-developer/`:

1. **Documentation:**
   - `remix-core-concepts.md` - Core Remix concepts and patterns
   - `remix-routing-guide.md` - Comprehensive routing documentation
   - `remix-data-flow.md` - Data loading and mutation patterns
   - `remix-error-handling.md` - Error boundary and error handling patterns

2. **Code Examples:**
   - `route-module-examples/` - Directory of common route module patterns
   - `form-handling-examples/` - Progressive enhancement form examples
   - `error-boundary-examples/` - Error handling implementation examples
   - `loader-action-examples/` - Data loading and mutation examples

3. **Configuration:**
   - `adapter-configs/` - Common Remix adapter configurations
   - `vite-integration/` - Vite integration examples and configuration

4. **Best Practices:**
   - `security-guidelines.md` - Security best practices for Remix apps
   - `performance-patterns.md` - Performance optimization patterns
   - `testing-strategies.md` - Testing approaches for Remix apps

## Notes
*   Reference `v7.0/future-planning/current-status-and-mode-refinement-plan.md` for detailed scope.
*   Reference `v7.0/templates/mode_template.md` for section structure.
*   Reference `v7.0/templates/mode_hierarchy.md` for reporting/delegation structure.
*   Reference `v7.0/future-planning/mode-manifest-org-chart.md` (draft) for context.

## Summary of Changes
1. Standardized metadata formatting
2. Removed redundant Tool Groups section
3. Updated API Configuration format
4. Identified context needs for `.roo/context/remix-developer/`
5. Verified all sections against v7 template
6. Confirmed emoji and role definition accuracy