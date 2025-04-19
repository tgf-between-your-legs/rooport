# Example: Delegating a Feature Implementation via MDTM

This example shows how Roo Commander might delegate a multi-step feature implementation using the MDTM workflow.

**User Prompt:**

```prompt
Let's add user profile editing to the web app. This involves updating the frontend React component, adding a new API endpoint (Python/FastAPI), and updating the database schema (PostgreSQL).
```

**Roo Commander Actions:**

1.  **Plan:** Identify sub-tasks: Frontend update, API endpoint creation, DB migration. Note dependencies (API needs DB, Frontend needs API).
2.  **Create Commander Task Log:** `write_to_file` to `.tasks/TASK-CMD-20250415-205500.md` (logging own actions).
3.  **Delegate DB Migration (MDTM):**
    *   Select `database-specialist` (assuming PostgreSQL expertise from Stack Profile).
    *   `write_to_file` to `.tasks/TASK-DB-20250415-205510-add-profile-fields.md` with Goal, Criteria, Context (Stack Profile, schema details), Checklist (`- [⏳] Generate migration script`, `- [⏳] Apply migration`).
    *   `new_task` to `database-specialist`: "Process task file: `.tasks/TASK-DB-...-add-profile-fields.md`. Coordinator: TASK-CMD-..."
    *   `insert_content` into `.tasks/TASK-CMD-...`: "Delegated DB migration to `database-specialist` (TASK-DB-...). Reason: PostgreSQL expertise."
4.  **Await DB Completion:** Monitor `TASK-DB-...` file or wait for `database-specialist` completion message.
5.  **Delegate API Endpoint (MDTM):**
    *   Select `fastapi-developer` (assuming FastAPI from Stack Profile).
    *   `write_to_file` to `.tasks/TASK-API-20250415-205600-profile-endpoint.md` with Goal, Criteria, Context (Stack Profile, DB task ID, API specs), Checklist (`- [⏳] Create endpoint logic`, `- [⏳] Add tests`, `📣 Report after tests pass`).
    *   `new_task` to `fastapi-developer`: "Process task file: `.tasks/TASK-API-...-profile-endpoint.md`. Depends on TASK-DB-... Coordinator: TASK-CMD-..."
    *   `insert_content` into `.tasks/TASK-CMD-...`: "Delegated API endpoint to `fastapi-developer` (TASK-API-...). Reason: FastAPI expertise."
6.  **Await API Completion:** Monitor `TASK-API-...` file or wait for `fastapi-developer` completion message.
7.  **Delegate Frontend Update (MDTM):**
    *   Select `react-specialist` (assuming React from Stack Profile).
    *   `write_to_file` to `.tasks/TASK-FE-20250415-205700-profile-form.md` with Goal, Criteria, Context (Stack Profile, API task ID, UI mockups), Checklist (`- [⏳] Build form component`, `- [⏳] Integrate with API endpoint`, `- [⏳] Add component tests`).
    *   `new_task` to `react-specialist`: "Process task file: `.tasks/TASK-FE-...-profile-form.md`. Depends on TASK-API-... Coordinator: TASK-CMD-..."
    *   `insert_content` into `.tasks/TASK-CMD-...`: "Delegated Frontend update to `react-specialist` (TASK-FE-...). Reason: React expertise."
8.  **Await Frontend Completion:** Monitor `TASK-FE-...` file or wait for `react-specialist` completion message.
9.  **Summarize:** `attempt_completion` to user: "User profile editing feature implemented. Database updated, API endpoint created, and frontend component built."