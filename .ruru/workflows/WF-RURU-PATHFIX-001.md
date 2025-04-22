+++
# --- Basic Metadata ---
id = "RURU-PATHFIX-001"               # << WORKFLOW-SCOPE-NNN >>
title = "Workflow: Update Legacy Paths in .roo Directory"            # << Human-readable title of the Workflow/SOP >>
status = "active"      # << draft, active, deprecated, under-review >> - Changed to active
created_date = "2025-04-22"     # << YYYY-MM-DD >>
updated_date = "2025-04-22"     # << YYYY-MM-DD >>
version = "1.0"       # << Workflow document version >>
tags = ["workflow", "refactor", "paths", "prime", "ruru"] # << Keywords >>

# --- Ownership & Context ---
owner = "Prime Coordinator" # Or relevant Lead Agent
related_docs = [
    ".ruru/rules-prime-coordinator/03-meta-dev-workflow-rule.md",
    ".ruru/rules/07-save-point-commit-policy.md",
    ".ruru/rules/08-git-commit-standard.md"
    ]     # << Paths/URLs to essential specs, guides, PAL doc >>
related_templates = [] # << Paths to data templates used/produced >>

# --- Workflow Specific Fields ---
objective = "Systematically find and replace legacy path references (e.g., '.archive') with '.ruru/' prefixed paths within the .roo/ directory, excluding .roo/ itself and .roomodes." # << REQUIRED: Goal of this workflow >>
scope = "All files within the .roo/ directory, excluding .roo/ itself and .roomodes. Special handling (staging) for files matching `.roo/rules/**`."     # << REQUIRED: Applicability and boundaries >>
roles = ["prime-coordinator", "prime-dev", "prime-txt", "dev-git"]     # << REQUIRED: List agent roles involved >>
trigger = "Manual initiation by Prime Coordinator following completion of WF-RURU-SIMPLEREFACTOR-001 or similar refactoring."   # << How is this workflow typically initiated? >>
success_criteria = [
    "No legacy path references (e.g., '.archive', '.context', etc. without '.ruru/' prefix) remain within files in the `.roo/` directory (excluding `.roo/` itself and `.roomodes`).",
    "All necessary changes have been applied (either directly or manually after staging).",
    "Changes are committed to version control."
    ] # << Measurable conditions for successful completion >>
failure_criteria = [
    "Legacy paths remain after execution.",
    "Protected files are modified incorrectly.",
    "Workflow is aborted due to unresolvable errors."
    ] # << Conditions indicating workflow failure >>

# --- Integration ---
acqa_applicable = true # Does the ACQA process apply to steps in this workflow?
pal_validated = false # Has this workflow been validated using PAL?
validation_notes = "" # Link to PAL validation records/notes

# --- AI Interaction Hints (Optional) ---
# context_type = "workflow_definition"
+++

# Workflow: Update Legacy Paths in .roo Directory

## 1. Objective 🎯
*   Systematically find and replace legacy path references (e.g., `'.archive'`, `'.context'`) with their new `.ruru/` prefixed counterparts (e.g., `'.ruru/archive'`, `'.ruru/context'`) within the `.roo/` directory.
*   Ensure protected files (`.roo/rules/**`) are handled safely via staging.
*   Minimize user prompts for non-protected file changes, respecting user preference.
*   Track changes via Git commits.

## 2. Scope ↔️
*   **Includes:** All files recursively within the `.roo/` directory.
*   **Excludes:** The `.roo/` directory itself, the `.roomodes` file.
*   **Protected:** Files matching the pattern `.roo/rules/**` require the Staging Workflow as defined in `PRIME-RULE-METADEV-V2`.

## 3. Roles & Responsibilities 👤
*   **`prime-coordinator`**: Orchestrates the workflow, performs discovery, categorizes files, delegates tasks, manages staging for protected files, handles verification, and initiates commits.
*   **`prime-dev` / `prime-txt`**: Execute file modifications (direct or staged) based on Coordinator instructions. Expected to use internal confidence checks to minimize unnecessary user confirmation for *direct* edits, as requested. Must still seek confirmation for staged edits as per their rules.
*   **`dev-git`**: Executes Git commands (`add`, `commit`) as delegated by the Coordinator.

## 4. Preconditions🚦
*   The `.ruru/` directory structure is established.
*   Previous refactoring (like `WF-RURU-SIMPLEREFACTOR-001`) is complete.
*   Workspace is under Git version control.
*   Coordinator has access to necessary tools (`search_files`, `execute_command`, `new_task`, `ask_followup_question`).

## 5. Reference Documents & Tools 📚🛠️
*   **Rules:**
    *   `.roo/rules-prime-coordinator/03-meta-dev-workflow-rule.md` (Defines Staging vs. Direct Edit)
    *   `.roo/rules-prime-coordinator/07-logging-confirmation-rule.md` (Logging & Worker Confirmation)
    *   `.roo/rules/07-save-point-commit-policy.md` (Commit Triggering)
    *   `.roo/rules/08-git-commit-standard.md` (Commit Formatting)
*   **Tools:**
    *   `search_files`: For discovering legacy paths.
    *   `execute_command`: For staging (`cp`, `diff`, `rm`).
    *   `new_task`: For delegating edits and commits.
    *   `ask_followup_question`: For presenting staged diffs and commit proposals.
    *   `read_file`, `write_to_file`, `apply_diff`, `insert_content`, `search_and_replace`: Used by delegate editors.

## 6. Workflow Steps 🪜

*   **Step 1: Discover Legacy Paths (Coordinator Task)**
    *   **Description:** Search for occurrences of the legacy path patterns within the `.roo/` directory.
    *   **Inputs:** List of legacy path patterns (e.g., `'\.archive'`, `'\.context'`, etc. - ensure regex handles quotes/context).
    *   **Procedure:** Use `search_files` with the target path `.roo/` and a regex pattern matching the legacy paths. Exclude `.roomodes` if possible via file pattern or post-filtering.
    *   **Outputs:** A list of files containing potential legacy paths, along with line numbers and context.
    *   **Error Handling:** Log errors if `search_files` fails.

*   **Step 2: Analyze & Categorize Findings (Coordinator Task)**
    *   **Description:** Process the search results, categorizing files into 'Protected' (`.roo/rules/**`) and 'Non-Protected'.
    *   **Inputs:** Output from Step 1.
    *   **Procedure:** Iterate through the search results. For each file path:
        *   Check if it matches the `.roo/rules/**` pattern.
        *   Maintain separate lists for protected and non-protected files needing updates.
    *   **Outputs:** Two lists: `protected_files_to_update`, `non_protected_files_to_update`.

*   **Step 3: Correct Non-Protected Files (Coordinator delegates to `prime-dev`/`prime-txt`)**
    *   **Description:** Delegate the correction of legacy paths in non-protected files using the Direct Edit workflow.
    *   **Procedure:** For each file in `non_protected_files_to_update`:
        1.  **Determine Worker:** `prime-txt` for `.md`, `prime-dev` for others.
        2.  **Prepare Message:** Instruct the worker to replace all occurrences of the legacy paths with their `.ruru/` prefixed versions within the specified `TARGET_PATH`. Include the instruction: "Minimize user confirmation prompts where confidence is high, as per user request for this workflow." Add `USER_CONFIRMATION_REQUIRED=FALSE` *unless* specific file seems high-risk. Remind worker of their internal checks.
        3.  **Delegate:** Use `new_task` to delegate.
        4.  **Await & Log:** Wait for completion, log outcome (Rule `07`). Handle errors reported by the worker.
    *   **Note:** This step iterates through all non-protected files.

*   **Step 4: Correct Protected Files (Coordinator manages Staging Workflow)**
    *   **Description:** Apply corrections to protected files using the mandatory Staging Workflow.
    *   **Procedure:** For each file in `protected_files_to_update`:
        1.  **Initiate Staging:** Follow `PRIME-RULE-METADEV-V2`, Step 4.IF.1 (Define `STAGING_PATH`, `execute_command cp`).
        2.  **Delegate Staging Edit:** Follow `PRIME-RULE-METADEV-V2`, Step 4.IF.3 (Determine worker, prepare message with `STAGING_PATH`, delegate via `new_task`). Instructions should be similar to Step 3 but target the staging path. `USER_CONFIRMATION_REQUIRED=FALSE` might be appropriate given these are rules files.
        3.  **Await Completion:** Wait for worker completion (Rule `07`).
        4.  **Generate Diff:** Follow `PRIME-RULE-METADEV-V2`, Step 4.IF.5 (`execute_command diff`).
        5.  **Present Diff & Instruct:** Follow `PRIME-RULE-METADEV-V2`, Step 4.IF.6 (Use `ask_followup_question` to show diff and instruct user on **manual application**). Ask about staging file cleanup.
        6.  **Cleanup (If Confirmed):** Follow `PRIME-RULE-METADEV-V2`, Step 4.IF.7 (`execute_command rm`).
    *   **Note:** This step iterates through all protected files, presenting diffs individually as required by the staging rule.

*   **Step 5: Propose Save Point Commit (Coordinator Task)**
    *   **Description:** After processing a logical batch of files (e.g., all non-protected, or after each protected file), propose a Git commit.
    *   **Procedure:** Follow Rule `07-save-point-commit-policy.md`. Generate a conventional commit message (e.g., `chore(roo): update legacy paths in non-protected files` or `chore(rules): stage update for legacy paths in [filename]`). Use `ask_followup_question` to confirm message and Task ID (`Refs: General` likely appropriate unless part of a larger MDTM task).

*   **Step 6: Execute Commit (Coordinator delegates to `dev-git`)**
    *   **Description:** If the user approves the commit in Step 5.
    *   **Procedure:**
        1.  Finalize the commit message string (Rule `08`).
        2.  Delegate `git add .` and `git commit -m "..."` to `dev-git` via `new_task`.
        3.  Log delegation and outcome (Rule `12`).

*   **Step 7: Verification (Coordinator Task)**
    *   **Description:** After all files are processed and changes (direct or manual) are presumably applied, re-run the discovery search to verify no legacy paths remain.
    *   **Procedure:** Repeat Step 1 (`search_files`).
    *   **Outputs:** Verification results.
    *   **Decision Point:** If search results are empty, proceed to Step 8. If results are found, analyze discrepancies (e.g., missed files, manual application errors) and potentially loop back to Step 2 or report issues to the user.

*   **Step 8: Final Commit (Optional) (Coordinator Task)**
    *   **Description:** If significant changes occurred since the last commit in Step 5/6, propose a final commit.
    *   **Procedure:** Repeat Steps 5 and 6.

## 7. Postconditions ✅
*   Search in Step 7 returns no results for legacy paths in the specified scope.
*   All changes are reflected in the workspace (either directly written or manually applied by the user).
*   Relevant changes are captured in Git commits.

## 8. Error Handling & Escalation (Overall) ⚠️
*   Individual step errors (tool failures, worker errors) should be logged by the Coordinator.
*   If `prime-dev`/`prime-txt` report inability to confidently make direct changes, Coordinator may need to use `ask_followup_question` to get user confirmation for those specific files.
*   If verification (Step 7) fails, Coordinator reports findings to the user for guidance.
*   Persistent errors may require aborting the workflow and manual intervention.

## 9. PAL Validation Record 🧪
*   Date Validated:
*   Method:
*   Test Case(s):
*   Findings/Refinements:

## 10. Revision History 📜
*   v1.0 (2025-04-22): Initial draft.