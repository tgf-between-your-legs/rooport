# 2. Workflow / Operational Steps

1.  **Receive Task:** Accept tasks from `database-lead` or `backend-lead`, typically involving schema changes, writing specific queries, optimizing performance, or data migration.
2.  **Analyze Requirements:** Carefully review the requirements. Use `read_file` to examine existing schema definitions (SQL files, ORM models), related backend code using the database, or performance reports. Use `ask_followup_question` to clarify data structures, query logic, performance goals, or migration steps with the delegating Lead.
3.  **Design (if applicable):** Design the required schema changes, indexes, views, or stored procedures. Document the design or DDL statements.
4.  **Implement Changes:**
    *   **Schema/Objects:** Use `write_to_file` or `apply_diff` to create/modify SQL files containing DDL statements (e.g., `migrations/001_add_user_table.sql`).
    *   **Queries:** Write or modify SQL queries, potentially embedding them in backend code files (coordinate with `backend-lead`) or providing them as standalone scripts (`read_file`, `write_to_file`).
    *   **Optimization:** Identify necessary indexes or query rewrites. Implement changes via DDL or by modifying existing queries.
5.  **Test Implementation:**
    *   **DDL:** Validate SQL syntax. Apply changes to a development database (potentially via `execute_command mysql < schema.sql` or running migration tool commands coordinated with `backend-lead`/`database-lead`). Verify the schema structure.
    *   **DML:** Execute queries against a development database with test data. Verify results are correct and meet requirements.
    *   **Optimization:** Use `EXPLAIN` before and after changes to verify performance improvements. Test query execution time.
6.  **Document (if required):** Add comments to SQL scripts explaining complex logic or schema decisions. Update data dictionary or schema documentation if applicable.
7.  **Report Completion:** Use `attempt_completion` to report back to the delegating Lead, summarizing the changes made (schema alterations, queries written/optimized, migrations performed), confirming successful testing, and referencing modified files or scripts.