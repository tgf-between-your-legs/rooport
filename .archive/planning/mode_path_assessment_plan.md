# Plan: Assess Mode Path Expectations

## 1. Goal

To systematically identify all references to project-level file paths (both existing old paths like `project_journal/` and potentially non-existent but intended paths) within all current mode definitions (`v7.0/modes/**/*.mode.md`). The findings will be documented and mapped to the new proposed hidden folder structure (`.tasks/`, `.docs/`, etc.) to inform the refactoring effort.

## 2. Background

Modes often contain references to specific files or directories for context, task management, templates, or knowledge. These references might be hardcoded in `roleDefinition` or `customInstructions`. As we transition from `project_journal/` and other locations to the new hidden folder structure, we need to find and update these references.

Furthermore, some modes might reference paths that *don't currently exist* but were likely intended during their creation (e.g., referencing `planning/project_plan.md` directly instead of `project_journal/planning/project_plan.md`). We need to capture this intent and map it correctly to the new structure.

## 3. Assessment Steps

**Step 3.1: Identify Mode Files**
*   **Action:** Use `list_files` to get a comprehensive list of all `.mode.md` files within the `v7.0/modes/` directory.
*   **Output:** A list of mode file paths to be scanned.

**Step 3.2: Scan for Path Patterns**
*   **Action:** Use `search_files` targeting the identified mode files (`*.mode.md` within `v7.0/modes/`). Search for regex patterns matching known old paths and potential intended paths.
    *   Pattern 1: `project_journal/`
    *   Pattern 2: `v7\.0/(context|templates|future-planning)/`
    *   Pattern 3: `\b(planning|knowledge|tasks|decisions|context|templates|reviews|ideas|visualizations)/` (Word boundary `\b` helps avoid matching parts of other words, looks for these names potentially used without `project_journal/`)
*   **Output:** Search results showing lines containing potential path references within each mode file.

**Step 3.3: Analyze Search Results & Mode Context**
*   **Action:** Manually review the output from `search_files`. For each match:
    *   Use `read_file` on the specific mode file to understand the context of the path reference (e.g., is it mentioned as a place to read context, write output, find a template?).
    *   Determine the *intended* purpose of the referenced file/directory.
    *   If the path doesn't exist (e.g., `planning/project_plan.md`), confirm the likely intent based on the mode's role and instructions.
*   **Output:** Understanding of *why* each path is referenced.

**Step 3.4: Create Mapping Report**
*   **Action:** Create a markdown report (`.planning/mode_path_assessment_report.md`) summarizing the findings. Use a table format:
    | Mode File Path | Referenced Path (Old/Intended) | Context/Intent | Proposed New Path | Notes |
    |---|---|---|---|---|
    | `v7.0/modes/.../some.mode.md` | `project_journal/tasks/TASK-XYZ.md` | Reading/Updating task status | `.tasks/TASK-XYZ.md` | Standard MDTM task |
    | `v7.0/modes/.../another.mode.md` | `v7.0/context/mdtm_standard.md` | Referencing MDTM standard | `.docs/standards/mdtm_standard.md` | Moved to docs |
    | `v7.0/modes/.../writer.mode.md` | `knowledge/style_guide.md` | Following style guide | `.docs/guides/style_guide.md` | Assumed intent, map to docs |
    | ... | ... | ... | ... | ... |
*   **Output:** `.planning/mode_path_assessment_report.md`

**Step 3.5: Plan Refactoring Tasks**
*   **Action:** Based on the mapping report, create specific, actionable tasks (likely MDTM tasks in `.tasks/`) for updating the mode definitions. These tasks can be assigned to the `mode-maintainer` or `technical-writer`.
*   **Output:** A set of refactoring tasks ready for delegation.

## 4. Tools Required

*   `list_files`
*   `search_files`
*   `read_file`
*   `write_to_file`

## 5. Deliverables

*   `.planning/mode_path_assessment_report.md`: The detailed report mapping old/intended paths to the new structure for each mode.
*   A set of MDTM tasks in `.tasks/` for executing the refactoring.

This plan provides a structured way to identify all necessary changes before starting the actual refactoring work.