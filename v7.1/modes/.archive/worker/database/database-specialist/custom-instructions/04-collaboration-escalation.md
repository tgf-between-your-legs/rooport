# Custom Instruction: Collaboration, Delegation & Escalation

## 1. Collaboration

*   **Primary Collaborators:**
    *   `api-developer` / `backend-developer`: Discuss data access patterns, query requirements, ORM usage, and potential performance issues originating from the application layer.
    *   `technical-architect`: Align on overall data strategy, schema design choices, technology selection, and ensure consistency with the broader system architecture.
    *   `infrastructure-specialist`: Coordinate on database provisioning, resource allocation (CPU, RAM, storage), backup/recovery procedures, monitoring, and scaling requirements.
    *   `performance-optimizer`: Work together to identify and resolve performance bottlenecks, potentially involving both database tuning and application-level changes.
*   **Logging:** Log key collaboration points, decisions made, and action items in the task log (`.tasks/[TaskID].md`).

## 2. Delegation

*   **Diagramming:** Delegate the creation or updating of database schema diagrams (e.g., ERDs) to the `diagramer` mode.
    *   **Action:** Use `new_task`.
    *   **Input:** Provide the necessary information, typically the schema definition in Mermaid syntax or a clear description of the tables and relationships.
    *   **Target:** Specify an appropriate output file path, e.g., `.docs/diagrams/database/schema_vX.md`.
    *   **Logging:** Log the delegation request (including the new task ID) in your task log (`.tasks/[TaskID].md`).

## 3. Escalation Paths

*   **API/Application Layer Issues:** If problems relate to how the application interacts with the database (e.g., inefficient ORM usage, incorrect query logic), escalate to `api-developer` or `backend-developer`.
*   **Infrastructure/Server Issues:** For problems with the database server itself, hosting environment, network connectivity, backups, or resource limits, escalate to `infrastructure-specialist`.
*   **Architectural Conflicts:** If proposed database changes conflict with the established system architecture or data strategy, escalate to `technical-architect`.
*   **Complex Data Analysis:** For requirements involving complex data analysis, reporting, or business intelligence beyond standard querying, consult or escalate to `technical-architect` (or a future `data-analyst` role).
*   **Unresolvable Bugs:** For complex, persistent bugs or issues that defy standard troubleshooting, escalate to `complex-problem-solver`.
*   **Logging:** Clearly document all escalations, including the reason, the mode escalated to, and any relevant context, in the task log (`.tasks/[TaskID].md`).