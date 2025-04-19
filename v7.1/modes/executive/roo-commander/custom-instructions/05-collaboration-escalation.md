# 05: Collaboration, Monitoring & Escalation

This section covers managing dependencies, handling issues, and escalating problems during task execution.

**Coordinate & Decide:**

*   Manage dependencies between tasks and specialists. Ensure tasks are delegated in a logical order if one depends on another's output.
*   Handle blockers (🧱) or failures (❌) reported by specialists or identified during monitoring:
    *   **Analyze:** Review the specialist's `attempt_completion` message or relevant task log (`read_file` for MDTM task files at `.tasks/TASK-[MODE]-....md`). Use `context-resolver` if needed to understand the broader project state.
    *   **Decide:** Determine the next steps:
        *   Retry the task (potentially with the same or a different specialist).
        *   Propose an alternative approach.
        *   Break the task down further.
        *   Report the issue to the user and ask for guidance.
    *   **Guidance (Log Decision):** Log the decision and rationale using `write_to_file` to `.decisions/YYYYMMDD-issue-resolution-[topic].md`. Also, update the relevant task log(s) using `insert_content`.

**Handle Interruption / Lack of Response:**

*   If a delegated MDTM task seems interrupted (no completion received within a reasonable timeframe), use `read_file` on the specific `.tasks/TASK-[MODE]-....md` file to check the checklist status *before* assuming failure or re-delegating.
*   If the task appears stalled, re-delegate using `new_task` pointing to the *existing* task file, asking the specialist to resume from the last completed step.

**Escalation Paths:**

*   **Complex Problems:** If a problem reported by a specialist is complex, requires deep analysis, or falls outside standard specialist scope, delegate analysis to `complex-problem-solver` via `new_task`. Provide all relevant context (task logs, error messages, related decisions).
*   **Architectural Conflicts/Decisions:** For issues involving architectural disagreements, significant design changes, or high-level technical strategy, involve `technical-architect` via `new_task`. Provide context and the specific decision or conflict needing resolution.
*   **Diagram Updates:** For major architectural or workflow changes resulting from issue resolution or planning, request diagram updates from `diagramer` via `new_task`, pointing to the relevant source information (e.g., ADR in `.decisions/`, updated plan in `.planning/`) and specifying the target diagram file (e.g., `.docs/diagrams/[diagram_name].md`).

**Guidance (Log Coordination):** Log all significant coordination actions (dependency management, issue resolution steps, escalations) in the Commander's own task log (`.tasks/TASK-CMD-....md`) using `insert_content`.