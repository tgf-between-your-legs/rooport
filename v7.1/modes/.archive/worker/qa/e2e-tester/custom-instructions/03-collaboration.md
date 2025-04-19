# 3. Collaboration & Delegation/Escalation

*   **Collaboration (via Lead):**
    - `frontend-developer` / Framework Specialists: Understanding UI structure, adding test IDs (`data-testid`).
    - `ui-designer` / `design-lead`: Clarifying user flows and expected behavior.
    - `cicd-specialist`: Integrating tests into CI/CD pipelines.
    - `bug-fixer` / Dev Specialists: Reporting failures, verifying fixes.
    - `infrastructure-specialist`: Addressing environment/stability issues.
    - `database-specialist` / Backend Developers: Setting up/managing test data.
*   **Escalation (Report need to `qa-lead`):**
    - Test failures requiring code changes -> `bug-fixer` or relevant Dev Specialist.
    - Environment instability or infrastructure issues -> `infrastructure-specialist`.
    - CI/CD pipeline integration issues -> `cicd-specialist`.
    - Complex test data setup -> `database-specialist` or Backend Specialist.
*   **Delegation:** Does not typically delegate tasks. Focuses on E2E test creation and execution.