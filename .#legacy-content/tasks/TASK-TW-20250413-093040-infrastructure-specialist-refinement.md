# Sub-Task: Refine Mode - 035-work-do-infrastructure-specialist.mode.md

**Master Task:** project_journal/tasks/TASK-PM-20250413-090710-v7-mode-refinement.md
**Status:** Complete ✅
**Coordinator:** roo-commander
**Assigned To:** technical-writer
**Mode File:** 03x-worker/035-devops/infrastructure-specialist/035-work-do-infrastructure-specialist.mode.md

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
- [x] Read the entire mode file (`read_file 03x-worker/035-devops/infrastructure-specialist/035-work-do-infrastructure-specialist.mode.md`).
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
- [x] Identify potential `.roo/context/infrastructure-specialist/` needs.
- [x] Apply changes to the mode file (using `apply_diff` or `write_to_file`).
- [x] Mark task as complete.

## Notes
*   Reference `v7.0/future-planning/current-status-and-mode-refinement-plan.md` for detailed scope.
*   Reference `v7.0/templates/mode_template.md` for section structure.
*   Reference `v7.0/templates/mode_hierarchy.md` for reporting/delegation structure.
*   Reference `v7.0/future-planning/mode-manifest-org-chart.md` (draft) for context.

## Potential `.roo/context/infrastructure-specialist/` Needs

The Infrastructure Specialist mode would benefit from the following context files:

1. **`.roo/context/infrastructure-specialist/aws-best-practices.md`**: Best practices for AWS infrastructure design, security, and cost optimization.
2. **`.roo/context/infrastructure-specialist/azure-best-practices.md`**: Best practices for Azure infrastructure design, security, and cost optimization.
3. **`.roo/context/infrastructure-specialist/gcp-best-practices.md`**: Best practices for GCP infrastructure design, security, and cost optimization.
4. **`.roo/context/infrastructure-specialist/terraform-patterns.md`**: Common Terraform patterns, modules, and best practices.
5. **`.roo/context/infrastructure-specialist/cloudformation-patterns.md`**: Common CloudFormation patterns, templates, and best practices.
6. **`.roo/context/infrastructure-specialist/pulumi-patterns.md`**: Common Pulumi patterns, components, and best practices.
7. **`.roo/context/infrastructure-specialist/networking-reference.md`**: Reference for common networking configurations (VPCs, subnets, security groups, etc.).
8. **`.roo/context/infrastructure-specialist/security-reference.md`**: Reference for infrastructure security best practices and common IAM policies.
9. **`.roo/context/infrastructure-specialist/monitoring-logging-patterns.md`**: Common patterns for setting up monitoring and logging infrastructure.
10. **`.roo/context/infrastructure-specialist/disaster-recovery-templates.md`**: Templates and strategies for disaster recovery and business continuity.

These context files would provide specialized knowledge that the Infrastructure Specialist can reference when designing, implementing, and managing infrastructure, without cluttering the main project record.

## Changes Made

1. Updated the metadata sections:
   - Added "Security" to Categories
   - Added `technical-writer` to Delegates To
   - Added `devops-lead` to Escalates To
   - Added `devops-lead` to Reports To (as primary reporting line)

2. Identified potential `.roo/context/` needs as listed above.

The mode file was already well-structured and compliant with v7 standards, with all required sections present and the emoji (🏗️) already assigned.