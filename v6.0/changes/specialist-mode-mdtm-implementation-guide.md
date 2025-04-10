# Implementation Guide: MDTM Workflow for Specialist Modes

**Date:** 2025-04-08
**Related Documents:**
*   `project_journal/knowledge/project-management/roo-commander-task-delegation/roo-commander-task-delegation.md`
*   `v6.0/changes/roo-commander-mdtm-delegation-integration.md`

## 1. Introduction & Goal

This document provides guidance for updating specialist modes to handle the Markdown-Driven Task Management (MDTM) workflow delegated by Roo Commander. The goal is to enable specialists to process complex, multi-step tasks reliably and resiliently using dedicated Markdown task files (`project_journal/tasks/TASK-[MODE]-....md`).

Implementing this requires significant changes to how specialists receive, process, and report on tasks.

## 2. Core Requirements for MDTM-Aware Specialists

Any specialist mode designated to handle MDTM tasks MUST implement the following capabilities within its `customInstructions` or underlying logic:

1.  **MDTM Task Detection:** Identify when a `new_task` message from Roo Commander contains a pointer to a task file (e.g., "Process task file: `path/to/task.md`") instead of direct instructions.
2.  **Task File Reading & Parsing:**
    *   Use `read_file` to fetch the content of the specified task file.
    *   Robustly parse the file content, extracting:
        *   Header information (Goal, Status, Assigned To, Acceptance Criteria, etc.).
        *   The Markdown checklist under the `## Checklist` section.
3.  **Sequential Checklist Processing:** Iterate through the checklist items (`- [ ] ...`), executing them in order. Resume processing from the first item not marked `✅`.
4.  **Atomic Status Updates:**
    *   **Before Action:** Update the current step's status to `⚙️` (In Progress) in the task file using `apply_diff` or `search_and_replace`. **Crucially, confirm this update succeeds before proceeding.**
    *   **After Success:** Update the step's status to `✅` (Done). **Confirm success.**
    *   **After Failure/Block:** Update the step's status to `❌` (Failed) or `🧱` (Blocked). **Confirm success.**
5.  **Action Execution:** Perform the work described in the checklist item using appropriate tools (`execute_command`, `write_to_file`, `apply_diff`, etc.).
6.  **Reporting Point (`📣`) Handling:** If a step description ends with `📣`, pause execution after marking the step `✅` and report back to Roo Commander (e.g., using `ask_followup_question` or `attempt_completion`), awaiting confirmation or further instructions.
7.  **Robust Error Handling:** Implement comprehensive error handling for:
    *   File I/O errors (`read_file`, `apply_diff`, `search_and_replace` on the task file).
    *   Task file parsing errors.
    *   Failures during the execution of the step's action.
    *   Report errors clearly to Roo Commander, referencing the task file and updating the step status appropriately (`❌`/`🧱`).
8.  **Final Reporting:**
    *   Once all checklist items are `✅`, update the main task **Status** in the file header to `✅ Complete`.
    *   Report overall success to Roo Commander using `attempt_completion`, referencing the completed task file.

## 3. Implementation Considerations & Nuances

### 3.1. Detecting MDTM Tasks
-   The simplest way is to check if the incoming message matches a specific pattern, like `^Process task file: \`(.*)\``.
-   The mode should switch its internal state to "MDTM processing mode" upon detection.

### 3.2. Parsing Task Files
-   **Robustness is Key:** Parsing needs to handle potential variations in whitespace or minor formatting deviations, although the Commander should strive for consistency. Regular expressions are likely needed.
-   **Checklist Parsing:** Extract the status marker (`[⏳]`, `[⚙️]`, `[✅]`, etc.) and the step description separately for each checklist item.
-   **Error on Parse Failure:** If the file doesn't match the expected structure (missing header, checklist, etc.), the specialist must report a parsing error immediately.

### 3.3. Checklist Processing Logic
-   The core loop should find the *first* checklist item whose status marker is *not* `✅`.
-   Handle resumption correctly: If a task was interrupted while `⚙️`, the specialist should ideally re-attempt that step (or report an issue if re-attempting is unsafe).

### 3.4. Atomic File Updates
-   **Criticality:** Updating the status marker *before* and *after* the action is the core of the resilience mechanism. These updates *must* succeed.
-   **Tool Choice:**
    *   `apply_diff` is generally safer and more precise if the exact line content (including the old status marker) is known. Requires reading the relevant line first if necessary.
    *   `search_and_replace` might be simpler but carries a higher risk of unintended replacements if the pattern isn't specific enough (e.g., replacing `- [⏳]` might match unintended lines if not careful). Restricting by line number (`start_line`/`end_line`) is highly recommended if using `search_and_replace`.
-   **Confirmation:** Always check the result of the file update tool call. If it fails, the specialist must stop and report an error immediately, likely marking the step `❌`.

### 3.5. Action Execution within Steps
-   A single checklist item might require multiple tool calls (e.g., `read_file`, analyze, then `apply_diff`).
-   The specialist must treat this sequence as a single logical step. Only update to `✅` if *all* actions within the step succeed. If any part fails, the step status should become `❌`.

### 3.6. Handling Reporting Points (`📣`)
-   After marking a step with `📣` as `✅`, the specialist should use `ask_followup_question` (for intermediate reports needing confirmation) or `attempt_completion` (if it's the final reporting step before task end) to communicate with the Commander.
-   It must clearly state what step was completed and wait for the Commander's response before proceeding to the next checklist item.

### 3.7. Error Handling
-   Provide specific error messages. Instead of just "failed", report "Failed to update task file status to ⚙️ for step 2" or "Command execution failed for step 3: [error details]".
-   Update the task file status (`❌`/`🧱`) *before* reporting the error to the Commander, ensuring the persistent state reflects the failure.

### 3.8. Final Reporting
-   Ensure the main `**Status:**` line in the header is updated to `✅ Complete` before the final `attempt_completion`.
-   The final success message should clearly reference the task file path.

## 4. Mode-Specific Considerations (Examples)

*   **`git-manager`:** Steps might involve `execute_command` for `git add`, `git commit`, `git push`. Error handling for Git commands is crucial. Status updates must occur reliably between commands.
*   **`project-initializer`:** Steps involve `execute_command` (`npm install`, `mkdir`), `write_to_file`. Needs careful sequencing and error checking (e.g., did `npm install` succeed?).
*   **`refactor-specialist`:** Steps might involve `search_files`, `read_file`, complex analysis (internal), then multiple `apply_diff` calls. The entire sequence for one refactoring step must succeed before marking `✅`.

## 5. Potential Pitfalls / What to Be Careful Of

*   **Race Conditions/Concurrency:** This model assumes serial processing by one specialist per task file. Concurrent modification attempts would corrupt the state.
*   **Fragile Parsing:** Overly strict or simple parsing logic can break easily with minor format changes.
*   **Non-Atomic Updates:** Failing to confirm success of status updates before/after actions breaks the resilience model.
*   **Complex Step Logic:** Managing multi-tool actions within a single checklist step requires careful state management within the specialist.
*   **Infinite Loops:** Ensure the logic for finding the next step and handling errors prevents infinite loops.
*   **Over-Reliance on MDTM:** Using MDTM for very simple, non-critical tasks adds unnecessary overhead. Commander needs judgment (as per its updated instructions).

## 6. Benefits Recap

*   **Resilience:** Tasks can be interrupted and resumed reliably.
*   **Transparency:** Task progress is explicitly tracked in a persistent file.
*   **Debugging:** Easier to pinpoint where a multi-step process failed.

## 7. Recommendation

Implementing MDTM requires careful design and testing for each specialist mode. Start with 1-2 high-priority modes (e.g., `git-manager`, `project-initializer`) as pilot implementations to refine the pattern before broader rollout. Ensure robust testing covers interruption scenarios and various error conditions.