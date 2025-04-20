# Task Log: code-reviewer-conversion - Technical Writing: Code Reviewer Mode Migration

**Goal:** Process the `code-reviewer.md` file from `v7.0/modes/md/` according to the final conventions
**Subject:** Mode file migration and standardization
**Audience:** Development team
**Purpose:** Document the migration process and ensure proper implementation of the final conventions
**References:** 
- Final Convention ADR: `project_journal/decisions/20251104-mode_convention_final_refinement.md`
- Mode file to process: `v7.0/modes/md/code-reviewer.md`
- Updated Template: `v7.0/templates/mode_template.md`
- Hierarchy/Structure Guides: 
  - `v7.0/templates/mode_hierarchy.md`
  - `v7.0/templates/mode_folder_structure.md`
  - `v7.0/templates/mode_classification_guide.md`

## Process Steps

1. ✅ Review the source mode file
2. ✅ Determine the correct target folder and filename
3. ✅ Create the target folder if needed
4. ✅ Copy and rename the mode file to the target location
5. ✅ Update the new file's metadata according to the template and final conventions
6. ✅ Flag any ambiguous or missing critical information
7. ✅ Update this task log with the process and outcome
8. ✅ (Optional) Delete the source file

## Current Status: Complete

## Implementation Details

### Metadata Updates
The following metadata fields were added or updated in the new mode file:
- **Level:** Set to `039-worker-cross-functional` to reflect the mode's classification as a cross-functional worker
- **Categories:** Added `Cross-Functional` and `Quality Assurance` categories
- **Stack:** Added `Language-agnostic` to indicate the mode works with any programming language
- **Reports To:** Added `roo-commander` and `project-manager` to indicate who the mode reports to
- **API Configuration:** Updated to use the new YAML list format instead of JSON

### File Structure
- Created the directory structure: `v7.0/modes/03x-worker/039-cross-functional/code-reviewer/`
- Created the mode file with the new naming convention: `039-work-xf-code-reviewer.mode.md`
- Deleted the original source file: `v7.0/modes/md/code-reviewer.md`

## Findings

### Source File Analysis
The source file `v7.0/modes/md/code-reviewer.md` contains a well-structured mode definition for the Code Reviewer mode. The mode is responsible for reviewing code changes for quality, standards adherence, bugs, security, performance, maintainability, and providing actionable feedback.

### Classification Determination
Based on the mode classification guide:
- **Level**: The Code Reviewer is a Level 3 Worker mode as its primary function is executing specific tasks (code review) focused on a particular skill set.
- **Department**: The Code Reviewer belongs to the Cross-Functional department (039) as it supports the overall development process across multiple domains.
- **Department Shortcode**: xf (for cross-functional)

### Target Location
- **Target Folder**: `v7.0/modes/03x-worker/039-cross-functional/code-reviewer/`
- **Target Filename**: `039-work-xf-code-reviewer.mode.md` (following the convention `[level_prefix]-[department_shortcode]-[mode_slug].mode.md`)