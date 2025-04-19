# Sub-Task: Refine Mode - 032-work-be-fastapi-developer.mode.md

**Master Task:** project_journal/tasks/TASK-PM-20250413-090710-v7-mode-refinement.md
**Status:** Complete ✅
**Coordinator:** roo-commander
**Assigned To:** technical-writer
**Mode File:** 03x-worker/032-backend/fastapi-developer/032-work-be-fastapi-developer.mode.md

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
- [x] Read the entire mode file (`read_file 03x-worker/032-backend/fastapi-developer/032-work-be-fastapi-developer.mode.md`).
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
- [x] Identify potential `.roo/context/fastapi-developer/` needs.
- [x] Apply changes to the mode file (using `apply_diff` or `write_to_file`).
- [x] Mark task as complete. 📣

## Notes
*   Reference `v7.0/future-planning/current-status-and-mode-refinement-plan.md` for detailed scope.
*   Reference `v7.0/templates/mode_template.md` for section structure.
*   Reference `v7.0/templates/mode_hierarchy.md` for reporting/delegation structure.
*   Reference `v7.0/future-planning/mode-manifest-org-chart.md` (draft) for context.

## Identified `.roo/context/fastapi-developer/` Needs

The following context files would be beneficial for the FastAPI Developer mode:

1. `.roo/context/fastapi-developer/fastapi-best-practices.md` - Comprehensive guide on FastAPI best practices, including project structure, security considerations, and performance optimization.
2. `.roo/context/fastapi-developer/pydantic-validation-patterns.md` - Common patterns and examples for data validation using Pydantic models.
3. `.roo/context/fastapi-developer/async-patterns.md` - Patterns and examples for asynchronous programming in FastAPI.
4. `.roo/context/fastapi-developer/dependency-injection-examples.md` - Examples of dependency injection patterns for various use cases.
5. `.roo/context/fastapi-developer/orm-integration-guide.md` - Guide for integrating FastAPI with various ORMs, especially SQLModel and SQLAlchemy.
6. `.roo/context/fastapi-developer/testing-strategies.md` - Strategies and examples for testing FastAPI applications using pytest and TestClient.
7. `.roo/context/fastapi-developer/security-implementation-guide.md` - Guide for implementing security features in FastAPI applications.

## Changes Made

1. Added comprehensive content to the "Key Considerations / Safety Protocols" section, focusing on security, performance, and API design best practices.
2. Updated the "Delegates To" section to include `integration-tester`, `e2e-tester`, and `technical-writer`.
3. Updated the "Reports To" section to include `backend-lead` and `technical-architect`.
4. Standardized the API Configuration to use `gemini-2.5-pro` instead of `quasar-alpha`.
5. Identified potential `.roo/context/fastapi-developer/` needs as listed above.