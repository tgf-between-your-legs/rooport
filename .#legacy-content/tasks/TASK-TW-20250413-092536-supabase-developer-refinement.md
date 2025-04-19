# Sub-Task: Refine Mode - 032-work-be-supabase-developer.mode.md

**Master Task:** project_journal/tasks/TASK-PM-20250413-090710-v7-mode-refinement.md
**Status:** Complete ✅
**Coordinator:** roo-commander
**Assigned To:** technical-writer
**Mode File:** 03x-worker/032-backend/supabase-developer/032-work-be-supabase-developer.mode.md

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
- [x] Read the entire mode file (`read_file 03x-worker/032-backend/supabase-developer/032-work-be-supabase-developer.mode.md`).
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
- [x] Identify potential `.roo/context/supabase-developer/` needs.
- [x] Apply changes to the mode file (using `apply_diff` or `write_to_file`).
- [x] Mark task as complete. 📣
## Notes
*   Reference `v7.0/future-planning/current-status-and-mode-refinement-plan.md` for detailed scope.
*   Reference `v7.0/templates/mode_template.md` for section structure.
*   Reference `v7.0/templates/mode_hierarchy.md` for reporting/delegation structure.
*   Reference `v7.0/future-planning/mode-manifest-org-chart.md` (draft) for context.

## Summary of Changes
1. Verified the emoji (🧱) in the name field is appropriate for Supabase Developer.
2. Confirmed all standard sections from the template are present and well-populated.
3. Reviewed and confirmed the Description, Capabilities, Workflow, and Role Definition sections are accurate and detailed.
4. Reviewed and confirmed Custom Instructions (Sections 1-6) are comprehensive and aligned with principles.
5. Updated Metadata:
   - Validated Level as "032-worker-backend"
   - Confirmed Tags, Categories, and Stack are comprehensive
   - Updated "Delegates To" to include `nextjs-developer` and corrected `sveltekit-developer`
   - Updated "Escalates To" to include `backend-lead`
   - Reordered "Reports To" to prioritize `backend-lead` as primary reporting line
   - Standardized API Configuration to "gemini-2.5-pro" (was "quasar-alpha")
6. Added a "Potential .roo/context/ Needs" section identifying six specific context files that would benefit the Supabase Developer mode:
   - supabase-js-reference.md
   - rls-policy-templates.md
   - edge-functions-examples.md
   - schema-design-patterns.md
   - vector-search-examples.md
   - auth-flow-templates.md
*   Reference `v7.0/future-planning/mode-manifest-org-chart.md` (draft) for context.