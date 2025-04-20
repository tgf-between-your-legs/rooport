# Sub-Task: Refine Mode - 033-work-db-elasticsearch-specialist.mode.md

**Master Task:** project_journal/tasks/TASK-PM-20250413-090710-v7-mode-refinement.md
**Status:** Complete ✅
**Coordinator:** roo-commander
**Assigned To:** technical-writer
**Mode File:** 03x-worker/033-database/elasticsearch-specialist/033-work-db-elasticsearch-specialist.mode.md

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
- [x] Read the entire mode file (`read_file 03x-worker/033-database/elasticsearch-specialist/033-work-db-elasticsearch-specialist.mode.md`).
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
- [x] Identify potential `.roo/context/elasticsearch-specialist/` needs.
- [x] Apply changes to the mode file (using `apply_diff` or `write_to_file`).
- [x] Mark task as complete. 📣

## Notes
*   Reference `v7.0/future-planning/current-status-and-mode-refinement-plan.md` for detailed scope.
*   Reference `v7.0/templates/mode_template.md` for section structure.
*   Reference `v7.0/templates/mode_hierarchy.md` for reporting/delegation structure.
*   Reference `v7.0/future-planning/mode-manifest-org-chart.md` (draft) for context.

## Completion Summary

The Elasticsearch Specialist mode file has been successfully reviewed and updated according to v7 standards. The following changes were made:

1. **Verified all standard sections** - All required sections from the template were present and properly formatted.
2. **Confirmed emoji** - The 🔍 emoji was already correctly assigned.
3. **Reviewed core content** - Description, Capabilities, Workflow, and Role Definition were already detailed and accurate.
4. **Reviewed Custom Instructions** - All sections (1-6) were already well-populated and aligned with principles.
5. **Updated Metadata**:
   - Level: Confirmed correct as "033-worker-database"
   - Tags, Categories, Stack: All appropriate and comprehensive
   - Delegates To: Confirmed as "None"
   - Escalates To: Confirmed appropriate escalation paths
   - Reports To: Added `database-lead` to existing reporting structure
   - API Configuration: Standardized to `gemini-2.5-pro` (was "quasar-alpha")
6. **Added `.roo/context/` needs** - Identified potential context files that would benefit this mode:
   - Version differences documentation
   - Query DSL examples
   - Mapping templates
   - Vector search examples
   - Performance tuning guidelines
   - Cluster management commands
   - Analyzers reference

The mode file now fully complies with v7 standards and the hybrid context strategy.