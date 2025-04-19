# Mode Review: supabase-developer

**Mode File:** `roo-modes-dev/supabase-developer.json`

## Analysis Summary

This mode specializes in building applications using the Supabase platform, covering its core features like Postgres DB, Auth, RLS, Edge Functions, Realtime, and Storage.

## Findings & Concerns

1.  **`ROO_COMMANDER_SYSTEM.md` References:** None found.
2.  **MDTM Alignment Gaps:**
    *   **Task ID Reception/Log Initialization:** Step 1 ("Receive Task") lacks explicit instructions to receive a Task ID (`[TaskID]`) from the delegator and initialize the corresponding task log file (`project_journal/tasks/[TaskID].md`) using `write_to_file` or `insert_content`.
    *   **Completion Logging:** Step 6 ("Log Completion") is slightly vague ("relevant task log or journal"). It should explicitly instruct the mode to append a final status, outcome, summary, and references to the specific task log file (`project_journal/tasks/[TaskID].md`) using `insert_content`.
3.  **Embedded Context:** The mode definition includes a large embedded "Condensed Context Index" for Supabase.

## Recommendations for Change

1.  **Update Step 1 (Receive Task):** Add instructions to receive `[TaskID]` and initialize `project_journal/tasks/[TaskID].md` with the initial goal.
2.  **Update Step 6 (Log Completion):** Specify using `insert_content` to append the final summary block (Status, Outcome, Summary, References) to `project_journal/tasks/[TaskID].md`.

## Other Notes/Ideas

*   Consider refactoring the embedded context index into a separate file within `project_journal/context/` and having the mode read it if needed, to reduce the size of the mode definition JSON. (Future enhancement)

## Proposed Changes (JSON `customInstructions`)

*   **Modify Step 1:** Add text like: "Receive Task & Initialize Log: Get assignment (with Task ID `[TaskID]`) and requirements... **Guidance:** Log the initial goal to the task log file (`project_journal/tasks/[TaskID].md`) using `insert_content` or `write_to_file`."
*   **Modify Step 6:** Reword to specify appending the final summary block to `project_journal/tasks/[TaskID].md` using `insert_content`. Example: "Log Completion & Final Summary: Append the final status, outcome, concise summary, and references to the task log file (`project_journal/tasks/[TaskID].md`). **Guidance:** Log completion using `insert_content`."