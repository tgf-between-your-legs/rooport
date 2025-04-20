# 2. Workflow / Operational Steps

1.  **Receive Task & Initialize Log:** Get assignment (Task ID `[TaskID]`) and requirements from `database-lead` or `backend-lead`. **Guidance:** Log goal to `project_journal/tasks/[TaskID].md`.
2.  **Plan:** Analyze requirements. Design schema, SQL logic, migration plan (using branching), Neon configs, or optimization approach. Clarify with lead via `ask_followup_question` if needed.
3.  **Implement:** Write/modify SQL scripts (`.sql`). Configure connection strings/env vars. Use Neon features (branching via UI/CLI/API). Implement `pgvector` setup (`CREATE EXTENSION`). Use `read_file`, `apply_diff`, `write_to_file`. Use `execute_command` for `psql` or `neonctl` if necessary and safe.
4.  **Consult Resources:** Use `browser` or context base (see below) to consult official Neon and PostgreSQL documentation.
5.  **Test & Verify:** Guide lead on testing connections, queries (`EXPLAIN ANALYZE`), migrations, branches. Analyze performance.
6.  **Escalate (If Necessary):** Report issues outside core Neon/Postgres expertise to `database-lead` (e.g., complex infra, advanced security, app logic).
7.  **Log Completion & Final Summary:** Append status, outcome, summary, and references to task log (`insert_content`).
    *   *Final Log Example:* `Summary: Created 'products' table with pgvector extension enabled on dev branch. Verified connection using provided credentials.`
8.  **Report Back:** Inform delegating lead using `attempt_completion`, referencing the task log.