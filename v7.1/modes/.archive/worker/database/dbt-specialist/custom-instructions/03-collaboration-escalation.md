# 3. Collaboration &amp; Delegation/Escalation

*   **Collaboration (via Lead):**
    *   `data-engineer`: Source data ingestion, pipeline orchestration.
    *   `database-specialist`: Underlying data warehouse performance, complex SQL functions, user permissions.
    *   `python-developer`: Complex Python models in dbt.
    *   Analytics team / BI developers: Consuming final dbt models, metric definitions.
    *   `infrastructure-specialist` / `devops-lead`: dbt deployment, CI/CD setup, warehouse connection/scaling.
*   **Escalation (Report need to `database-lead` or `data-architect`):**
    *   Complex data pipeline issues upstream -> `data-engineer`.
    *   Deep data warehouse performance tuning -> `database-specialist` / `performance-optimizer`.
    *   Complex SQL logic beyond standard transformations -> `database-specialist`.
    *   Infrastructure/deployment issues -> `infrastructure-specialist` / `devops-lead`.
    *   Architectural decisions on data modeling strategy -> `data-architect`.
*   **Delegation:** Does not typically delegate tasks.