# 4. Key Considerations / Safety Protocols

*   **Idempotency:** Design models (especially incremental) to be idempotent.
*   **Testing:** Implement tests for key assumptions (uniqueness, non-null constraints, relationships, accepted values) and custom business logic.
*   **Materialization Strategy:** Choose appropriate materializations (`view`, `table`, `incremental`, `ephemeral`) based on model size, query frequency, and performance needs.
*   **Project Structure:** Follow dbt best practices for organizing models (e.g., `staging`, `intermediate`, `marts`).
*   **Secrets Management:** Ensure database credentials in `profiles.yml` are handled securely (e.g., environment variables, not checked into git). Coordinate with `security-specialist` / `devops-lead`.
*   **Performance:** Optimize SQL. Use incremental models effectively. Consider warehouse-specific optimizations.