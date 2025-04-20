# 03: Workflow - Project Coordination & Execution

This phase covers the core activities after initial intent is clear and any necessary onboarding is complete.

1.  **Understand Goals:** Ensure user objectives for the session or next steps are clearly defined.
2.  **Plan Strategically:**
    *   Break down high-level goals into logical phases or actionable tasks.
    *   Generate unique Task IDs (e.g., `TASK-CMD-YYYYMMDD-HHMMSS` for own tasks, `TASK-[MODE]-...` for delegated).
    *   Consider delegating plan creation to `manager-project` via `new_task` if a formal plan document (`.planning/project_plan.md`) is needed.
3.  **Check Context:** Before complex delegations or resuming work, **strongly consider** delegating to `agent-agent-context-resolver` via `new_task`: "🔍 Provide current status summary relevant to [goal/task ID] based on `.tasks/`, `.decisions/`, `.planning/` docs, and the Stack Profile (`.context/stack_profile.json`)." Ensure specialists receive up-to-date context.
4.  **Delegate Tasks:** (See `04-delegation-mdtm.md` in this KB for detailed procedures).
5.  **Monitor Progress:**
    *   Review task logs (`.tasks/TASK-... .md`) via `read_file`.
    *   Use `agent-agent-context-resolver` for broader status checks, especially for complex, multi-delegate workflows.
6.  **Coordinate & Decide:** (See `05-collaboration-escalation.md` in this KB for detailed procedures).
7.  **Completion:**
    *   Review the final state of the project or task.
    *   Potentially use `agent-agent-context-resolver` for a final summary.
    *   Use `attempt_completion` to summarize the overall outcome and the coordinated effort to the user.