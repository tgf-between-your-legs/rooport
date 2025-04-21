+++
# --- Basic Metadata ---
id = "WF-RURU-SIMPLEREFACTOR-001"               # << WORKFLOW-SCOPE-NNN >>
title = "Workflow: Roo Commander Path Refactor (Simplified .ruru/ Consolidation)"            # << Human-readable title of the Workflow/SOP >>
status = "draft"      # << draft, active, deprecated, under-review >>
created_date = "2025-04-21"     # << YYYY-MM-DD >>
updated_date = "2025-04-21"     # << YYYY-MM-DD >>
version = "1.0"       # << Workflow document version >>
tags = ["workflow", "sop", "refactoring", "paths", "ruru", "consolidation", "fixed-path"] # << Keywords >>

# --- Ownership & Context ---
owner = "prime" # Or relevant Lead Agent
related_docs = [
    ".planning/ruru-simpler-refactoring/CTX-RURU-SIMPLEREFACTOR-OVERVIEW.md",
    ".planning/ruru-simpler-refactoring/CTX-RURU-SIMPLEREFACTOR-IMPL-GUIDE.md",
    ".planning/ruru-simpler-refactoring/CTX-RURU-SIMPLEREFACTOR-RISKS.md"
]     # << Paths/URLs to essential specs, guides, PAL doc >>
related_templates = [] # << Paths to data templates used/produced >>

# --- Workflow Specific Fields ---
objective = "To consolidate standard Roo Commander operational directories under a single, fixed `.ruru/` directory." # << REQUIRED: Goal of this workflow >>
scope = "Applies to the Roo Commander workspace structure. Involves moving directories, updating path references in code and documentation, and modifying build scripts."     # << REQUIRED: Applicability and boundaries >>
roles = ["prime", "prime-dev", "prime-txt", "roo-commander"]     # << REQUIRED: List agent roles involved >>
trigger = "Manual initiation by Prime Coordinator based on user request."   # << How is this workflow typically initiated? >>
success_criteria = [
    "All specified directories moved under `.ruru/`.",
    "All path references updated correctly.",
    "Build scripts function correctly.",
    "Core workflows execute without path errors.",
    "Documentation updated."
] # << Measurable conditions for successful completion >>
failure_criteria = [
    "Incomplete directory moves.",
    "Incorrect path references remain.",
    "Build scripts fail.",
    "Core workflows fail due to path errors."
] # << Conditions indicating workflow failure >>

# --- Integration ---
acqa_applicable = true # Does the ACQA process apply to steps in this workflow? (Yes, for file edits)
pal_validated = false # Has this workflow been validated using PAL?
validation_notes = "" # Link to PAL validation records/notes

# --- AI Interaction Hints (Optional) ---
# context_type = "workflow_definition"
+++

# Workflow: Roo Commander Path Refactor (Simplified .ruru/ Consolidation)

## 1. Objective 🎯
*   To consolidate standard Roo Commander operational directories under a single, fixed `.ruru/` directory at the workspace root. This aims to clean up the workspace root, organize Roo Commander artifacts logically, and provide a basic level of adaptability for forks.

## 2. Scope ↔️
*   Applies to the Roo Commander workspace structure.
*   Involves moving standard hidden directories (e.g., `.tasks`, `.docs`, `.modes`, `.templates`) into a new `.ruru/` directory, while `.roo` remains at the root.
*   Requires updating path references in source code (`.js`), documentation (`.md`), and configuration files.
*   Requires modifying build scripts (`build_*.js`, `create_build.js`).
*   Does **not** involve making the `.ruru/` directory itself configurable.

## 3. Roles & Responsibilities 👤
*   **`prime` (Prime Coordinator):** Initiates the workflow, performs directory operations (backup, create, move), delegates tasks, coordinates testing, and oversees the process.
*   **`prime-dev`:** Updates JavaScript files (build scripts) and `.gitignore` based on Coordinator instructions.
*   **`prime-txt`:** Updates Markdown files (documentation, rules) based on Coordinator instructions.
*   **`roo-commander` (Potentially):** May be involved in testing core workflows after the refactoring.

## 4. Preconditions🚦
*   All current changes in the repository are committed.
*   The Prime Coordinator has access to the planning documents:
    *   `.planning/ruru-simpler-refactoring/CTX-RURU-SIMPLEREFACTOR-OVERVIEW.md`
    *   `.planning/ruru-simpler-refactoring/CTX-RURU-SIMPLEREFACTOR-IMPL-GUIDE.md`
    *   `.planning/ruru-simpler-refactoring/CTX-RURU-SIMPLEREFACTOR-RISKS.md`
*   The Prime Coordinator has the necessary permissions to execute file system commands (`git`, `mkdir`, `mv`) and delegate tasks to `prime-dev` and `prime-txt`.

## 5. Reference Documents & Tools 📚🛠️
*   **Documents:**
    *   `.planning/ruru-simpler-refactoring/CTX-RURU-SIMPLEREFACTOR-IMPL-GUIDE.md` (Primary guide)
    *   `.planning/ruru-simpler-refactoring/CTX-RURU-SIMPLEREFACTOR-OVERVIEW.md`
    *   `.planning/ruru-simpler-refactoring/CTX-RURU-SIMPLEREFACTOR-RISKS.md`
    *   `.roo/rules/` (General rules, especially TOML+MD format)
*   **Tools:**
    *   `execute_command` (for `git`, `mkdir`, `mv`)
    *   `new_task` (for delegation)
    *   `search_and_replace` / `apply_diff` / `write_to_file` (for file modifications by delegates)
    *   `read_file`
    *   `list_files` (potentially for verification)

## 6. Workflow Steps 🪜

*   **Step 1: Backup Repository (Coordinator Task)**
    *   **Description:** Create a safety backup before making significant changes.
    *   **Inputs:** Current repository state.
    *   **Procedure:** Use `execute_command` to run `git branch pre-ruru-refactor` or similar backup command.
    *   **Outputs:** Confirmation of backup branch creation.
    *   **Error Handling:** If `git` command fails, report error and halt workflow until resolved.

*   **Step 2: Create Parent Directory (Coordinator Task)**
    *   **Description:** Create the target `.ruru/` directory.
    *   **Inputs:** Workspace root path.
    *   **Procedure:** Use `execute_command` to run `mkdir .ruru`.
    *   **Outputs:** Confirmation of directory creation.
    *   **Error Handling:** If `mkdir` fails (e.g., directory exists, permissions), report error and halt.

*   **Step 3: Move Existing Directories (Coordinator Task)**
    *   **Description:** State that directories like `.tasks`, `.docs`, `.context`, `.logs`, etc., were moved into `.ruru/` and renamed to remove the leading dot (e.g., `.tasks` became `.ruru/tasks`).
    *   **Inputs:** List of directories from `CTX-RURU-SIMPLEREFACTOR-IMPL-GUIDE.md` (including `.context`, `.logs`).
    *   **Procedure:** Confirm that `execute_command` was used to run `mv <dir> .ruru/<dir_without_dot>` for each specified directory *except* `.roo` (e.g., `mv .tasks .ruru/tasks`, `mv .docs .ruru/docs`, `mv .context .ruru/context`, `mv .logs .ruru/logs`).
    *   **Outputs:** Confirmation of directory moves.
    *   **Validation/QA:** Optionally use `list_files` on `.ruru/` to verify moves.
    *   **Error Handling:** If `mv` fails (e.g., source not found, permissions), report error, attempt to revert any partial moves if possible, and halt.

*   **Step 4: Global Search & Replace (Coordinator delegates to `prime-dev` & `prime-txt`)**
    *   **Description:** Update all hardcoded path references in `.js` and `.md` files to reflect the new `.ruru/` structure.
    *   **Tool:** `new_task` (potentially two separate tasks, one for `.js` to `prime-dev`, one for `.md` to `prime-txt`).
    *   **Inputs Provided by Coordinator:**
        *   List of search/replace pairs from `CTX-RURU-SIMPLEREFACTOR-IMPL-GUIDE.md` (e.g., `".ruru/tasks/"` -> `".ruru/tasks/"`, `".ruru/docs/"` -> `".ruru/docs/"`, `".ruru/modes/"` -> `".ruru/modes/"`, `".ruru/context/"` -> `".ruru/context/"`, `".ruru/logs/"` -> `".ruru/logs/"`, etc.). Note: Do *not* replace `".roo/"`.
        *   Scope: All relevant files (primarily within the *new* `.ruru/` subdirectories, plus root files like `README.md`, `.gitignore`, build scripts).
    *   **Instructions for Delegate:**
        *   Perform careful, case-sensitive, whole-word (where appropriate) search-and-replace operations using `search_and_replace` or similar tools.
        *   **Crucially:** Verify that replacements only affect actual paths and not code examples or explanatory text. Use preview/confirmation features if available.
        *   Report completion, including any files modified or potential issues encountered.
    *   **Expected Output from Delegate:** Confirmation of completion, list of modified files.
    *   **Coordinator Action (Post-Delegation):** Wait for confirmation from both delegates. Review any reported issues.
    *   **Validation/QA:** ACQA applies. Coordinator may perform spot checks using `read_file` or `search_files`.
    *   **Error Handling:** If delegates report errors or issues, Coordinator investigates and may request corrections or perform manual fixes.

*   **Step 5: Modify Build Scripts (Coordinator delegates to `prime-dev`)**
    *   **Description:** Update hardcoded paths and logic in build scripts (`build_*.js`, `create_build.js`).
    *   **Tool:** `new_task`
    *   **Inputs Provided by Coordinator:**
        *   Paths to build scripts: `build_roomodes.js`, `build_mode_summary.js`, `create_build.js`.
        *   Specific instructions from `CTX-RURU-SIMPLEREFACTOR-IMPL-GUIDE.md` regarding path constants (e.g., update to `.ruru/modes`, `.ruru/docs`, `.ruru/context`, `.ruru/logs`) and build output structure (copying *from* `.ruru/*` to staging root).
        *   Instructions for generating correct relative paths in `.rurumodes`.
    *   **Instructions for Delegate:**
        *   Use `read_file` to examine scripts.
        *   Use `apply_diff` or `write_to_file` to modify path constants and logic as instructed.
        *   Pay close attention to the `create_build.js` logic for copying files into the staging directory to ensure the final zip structure is correct.
        *   Verify the path generation logic for `.rurumodes`.
        *   Report completion and confirm changes made.
    *   **Expected Output from Delegate:** Confirmation of completion, diffs or confirmation of changes applied.
    *   **Coordinator Action (Post-Delegation):** Wait for confirmation.
    *   **Validation/QA:** ACQA applies. Coordinator reviews changes. Crucial validation happens during testing (Step 8).
    *   **Error Handling:** If delegate reports errors or build fails later, Coordinator investigates and requests corrections.

*   **Step 6: Update `.gitignore` (Coordinator delegates to `prime-dev` or `prime-txt`)**
    *   **Description:** Ensure `.gitignore` correctly ignores files within the new `.ruru/` subdirectories if needed.
    *   **Tool:** `new_task`
    *   **Inputs Provided by Coordinator:** Path to `.gitignore`. Instruction to check/update patterns for paths like `.ruru/context/`, `.ruru/logs/`.
    *   **Instructions for Delegate:**
        *   Use `read_file` to examine `.gitignore`.
        *   Use `apply_diff` or `write_to_file` to add/modify ignore patterns as needed (e.g., change `/.context/` to `/.ruru/context/`, `/.logs/` to `/.ruru/logs/`).
        *   Report completion and changes made.
    *   **Expected Output from Delegate:** Confirmation of completion, diff or confirmation of changes applied.
    *   **Coordinator Action (Post-Delegation):** Wait for confirmation.
    *   **Validation/QA:** ACQA applies. Coordinator reviews changes.
    *   **Error Handling:** If delegate reports errors, Coordinator investigates.

*   **Step 7: Update Core Documentation (Coordinator delegates to `prime-txt`)**
    *   **Description:** Update key documentation files to reflect the new structure.
    *   **Tool:** `new_task`
    *   **Inputs Provided by Coordinator:**
        *   Paths to documents: `README.md`, `.ruru/docs/standards/project_structure_inventory.md`, `.roo/rules/02-workspace-default-folders.md`.
        *   Instructions: Update installation steps in `README.md`, update paths in `project_structure_inventory.md` (e.g., to `.ruru/docs/standards/...`), update explanation in `.roo/rules/02-workspace-default-folders.md` to reflect that other directories moved while `.roo` remains at the root.
    *   **Instructions for Delegate:**
        *   Use `read_file` to examine documents.
        *   Use `apply_diff` or `write_to_file` to make the necessary updates.
        *   Ensure accuracy and clarity regarding the new mandatory `.ruru/` structure.
        *   Report completion and changes made.
    *   **Expected Output from Delegate:** Confirmation of completion, diffs or confirmation of changes applied.
    *   **Coordinator Action (Post-Delegation):** Wait for confirmation.
    *   **Validation/QA:** ACQA applies. Coordinator reviews changes.
    *   **Error Handling:** If delegate reports errors, Coordinator investigates and requests corrections.

*   **Step 8: Thorough Testing (Coordinator Task, potentially involves `roo-commander`)**
    *   **Description:** Verify the refactoring by running builds and testing core workflows.
    *   **Inputs:** Modified codebase, build scripts.
    *   **Procedure:**
        *   Coordinator uses `execute_command` to run build scripts (`node build_roomodes.js`, `node create_build.js`). Verify outputs (`.roomodes`, summary file, build zip structure and content).
        *   Coordinator (or delegates to `roo-commander` via `new_task`) tests core workflows: onboarding, simple delegation, MDTM task creation/execution, ADR creation, logging functionality.
        *   Verify modes load correctly (find rules/KBs).
        *   Verify tools using paths function correctly.
    *   **Outputs:** Test results (pass/fail), list of any errors encountered.
    *   **Error Handling:** If tests fail, log errors, analyze root cause (likely path issues in code, build scripts, or `.rurumodes`), revert to relevant step (e.g., Step 4, 5) for correction, or perform manual fixes. Repeat testing until successful.

## 7. Postconditions ✅
*   All specified operational directories *except `.roo`* reside within the `.ruru/` directory.
*   All known path references in `.js`, `.md`, and configuration files point to the correct locations within `.ruru/` (e.g., `.ruru/tasks/`, `.ruru/docs/`, `.ruru/context/`, `.ruru/logs/`).
*   Build scripts (`build_*.js`, `create_build.js`) execute successfully and produce correct outputs (`.roomodes`, build archive with expected internal structure).
*   Core Roo Commander workflows function without path-related errors.
*   Key documentation (`README.md`, structure inventory, default folders rule) accurately reflects the new `.ruru/` structure (e.g., `.ruru/docs/standards/project_structure_inventory.md`, with `.roo` remaining at the root).
*   Successful completion meets the `success_criteria` defined in the TOML header.

## 8. Error Handling & Escalation (Overall) ⚠️
*   **Primary Risk:** Incomplete or incorrect path updates (Step 4). Requires meticulous execution and verification.
*   **Build Script Errors:** Errors in build script modification (Step 5) require careful debugging and correction.
*   **Testing Failures:** Failures during testing (Step 8) necessitate identifying the root cause (often a missed path update) and returning to the relevant step for correction.
*   **General:** Log all errors encountered. If issues cannot be resolved by revisiting steps or simple fixes, escalate to the user/developer for manual intervention. Consider reverting using the backup branch if major, unresolvable problems occur.
*   Reference the Adaptive Failure Resolution process (`.processes/afr-process.md`) if applicable.

## 9. PAL Validation Record 🧪
*   Date Validated: TBD
*   Method: TBD (Likely Simulation/Execution)
*   Test Case(s): TBD (Covering core workflows listed in Step 8)
*   Findings/Refinements: TBD

## 10. Revision History 📜
*   v1.0 (2025-04-21): Initial draft.