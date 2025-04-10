# Proposed Changes: Integrating MDTM Task Delegation into Roo Commander

**Date:** 2025-04-08
**Related Document:** `project_journal/knowledge/project-management/roo-commander-task-delegation/roo-commander-task-delegation.md`

## 1. Goal

To integrate the Markdown-Driven Task Management (MDTM) workflow into the `customInstructions` of the Roo Commander mode (`roo-modes-dev/roo-commander.json`). This aims to improve resilience and state tracking for complex, multi-step, or critical delegated tasks, as outlined in the related MDTM document.

## 2. Proposed Modifications to `customInstructions` (Phase 2)

The following changes are proposed for Phase 2 of the Roo Commander `customInstructions`:

### Modification to Step 7: Delegate Tasks

**Current Logic (Simplified):**
- Delegate using `new_task`.
- Message includes goal, criteria, context.
- Log delegation start.

**Proposed Logic:**

```diff
 7.  **Delegate Tasks:**
+    *   **Assess Task Type:** Determine if the task is simple/read-only or multi-step/stateful/critical, warranting the MDTM approach.
+    *   **Simple Tasks:** Use `new_task` directly. The message MUST state goal, acceptance criteria, and context refs.
+    *   **Complex/Critical Tasks (MDTM Workflow):**
+        *   **Guidance (Create Task File):** Create a dedicated task file using `write_to_file` at `project_journal/tasks/TASK-[MODE]-[YYYYMMDD-HHMMSS].md`. Include Goal, Status (Pending), Coordinator (self TaskID), Assigned To, Acceptance Criteria, Context Files, and a detailed Checklist (`- [⏳] Step...`). Indicate reporting points with `📣`.
+        *   **Guidance (Delegate):** Use `new_task` targeting the specialist. The message should primarily point to the created task file (e.g., "Process task file: `[path_to_task_file]`"). Include the Commander's Task ID for reference.
-        Use `new_task` (with Task ID) to specialists. Task messages MUST state goal, acceptance criteria, context refs.
     *   **Guidance (Log Delegation):** Regardless of method, log the delegation action (including the specialist Task ID/file path if MDTM) in the Commander's own task log (e.g., `project_journal/tasks/TASK-CMD-....md`) using `insert_content`.
```

**Rationale:** This explicitly guides the Commander to differentiate task types and follow the MDTM procedure (create file, delegate via file reference) for complex tasks, while retaining the simpler direct delegation for basic ones.

### Modification to Step 10: Coordinate & Decide

**Current Logic (Simplified):**
- Analyze completion/failure messages.
- Decide next steps.
- Log coordination.

**Proposed Logic:**

```diff
 10. **Coordinate & Decide:** Manage dependencies. Handle blockers (🧱) or failures (❌):
     *   **Analyze:** Review specialist's `attempt_completion` message or relevant task log (`read_file` for MDTM task files). Use `context-resolver` if needed.
     *   **Decide:** Determine next steps (retry, alternative approach, report to user). **Guidance:** Log decision using `write_to_file` to `project_journal/decisions/...`.
+    *   **Handle Interruption (MDTM):** If a delegated MDTM task seems interrupted (no completion received), use `read_file` on the specific `project_journal/tasks/TASK-[MODE]-....md` file to check the checklist status *before* re-delegating. Re-delegate using `new_task` pointing to the *existing* task file.
     *   **Delegate Analysis:** If needed, delegate analysis to `complex-problem-solver`.
     *   **Diagrams:** Request diagram updates (`diagramer`) for major changes.
     *   **Guidance (Log Coordination):** Log coordination actions in own task log using `insert_content`.
```

**Rationale:** This adds the crucial step for handling interruptions in MDTM tasks by checking the task file's state before resuming or re-delegating, enhancing resilience.

## 3. Important Consideration

Implementing these changes in Roo Commander requires corresponding logic to be implemented in the *specialist modes* that will receive MDTM tasks. Specialists must be able to:
- Read and parse the task file checklist.
- Update checklist item statuses (`⚙️`, `✅`, `❌`, `🧱`) reliably using tools like `apply_diff` or `search_and_replace`.
- Execute the steps defined in the checklist.
- Handle reporting points (`📣`).
- Report final success/failure referencing the task file.

## 4. Next Steps

Review these proposed changes. Once approved, the `roo-modes-dev/roo-commander.json` file can be updated accordingly.