# 4. Key Considerations / Safety Protocols

*   **Data Integrity:** Always prioritize data integrity. Use appropriate constraints (PK, FK, UNIQUE, NOT NULL, CHECK). Use transactions for multi-statement operations.
*   **Performance:** Write efficient queries. Use indexes appropriately. Avoid `SELECT *` where specific columns are needed. Understand the performance implications of joins and subqueries.
*   **Security:** Avoid SQL injection vulnerabilities (ensure application layer uses parameterized queries/prepared statements - coordinate with backend). Implement appropriate user permissions (coordinate with `devops-lead`/`database-lead`).
*   **Migrations:** Write clear, testable migration scripts. Consider rollback strategies. Test migrations thoroughly on non-production environments.
*   **Backups:** Ensure regular backups are being taken (responsibility usually lies with `devops-lead` or `database-lead`, but be aware).
*   **Schema Changes:** Understand the impact of schema changes (especially `ALTER TABLE` on large tables) on performance and locking. Plan potentially disruptive changes carefully.