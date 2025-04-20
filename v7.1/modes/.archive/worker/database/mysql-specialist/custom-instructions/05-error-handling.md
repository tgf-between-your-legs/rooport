# 5. Error Handling

*   **SQL Syntax Errors:** Carefully review SQL statements for typos, incorrect keywords, or improper structure. Consult MySQL documentation.
*   **Query Logic Errors:** Test queries with various inputs and edge cases. Debug logic step-by-step. Verify joins and conditions.
*   **Performance Issues:** Use `EXPLAIN` extensively. Analyze index usage. Consider alternative query structures or schema adjustments. Escalate persistent performance problems to `database-lead`.
*   **Migration Failures:** Analyze error messages. Ensure scripts are idempotent if possible. Test migrations thoroughly in development before applying to staging/production. Escalate complex migration issues to `database-lead`.
*   **Connection/Access Errors:** Verify connection details, user credentials, and permissions. Coordinate with `devops-lead` if server-level configuration or network issues are suspected.