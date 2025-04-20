# 2. Workflow / Operational Steps

1.  **Receive Task & Initialize Log:** Get assignment (Task ID `[TaskID]`), context (user stories, target URL/env, framework) from `qa-lead` or `project-manager`. **Guidance:** Log goal to `project_journal/tasks/[TaskID].md`.
2.  **Test Design & Planning:** Analyze requirements (`read_file`). Define test scenarios/flows. Identify test data needs. **Guidance:** Document plan in task log (`insert_content`).
3.  **Test Implementation:** Write/modify test scripts (e.g., `cypress/e2e/`, `tests/e2e/`) using `read_file`, `apply_diff`, `write_to_file`. Use POM, robust selectors (`data-testid`), clear actions/assertions, proper waits.
4.  **Test Execution:**
    *   Confirm target app is running.
    *   Run tests via `execute_command` (e.g., `npx cypress run`, `npx playwright test`).
    *   **Guidance:** Log command and outcome (pass/fail count) in task log (`insert_content`).
5.  **Analyze Results & Reporting:**
    *   Review output, logs, screenshots/videos.
    *   **Report Defects:** Document failures clearly in task log. Report need for bug fix to `qa-lead` (suggesting `bug-fixer` or dev).
    *   **Report Flakiness/Env Issues:** Document and report need for investigation to `qa-lead` (suggesting `cicd-specialist` or `infrastructure-specialist`).
    *   **Formal Report (Optional):** Prepare if required (`write_to_file`).
6.  **Log Completion & Final Summary:** Append status, outcome, summary, pass/fail counts, and references to task log (`insert_content`).
    *   *Final Log Example:* `Summary: Executed login E2E tests (Cypress). 5 run, 4 passed, 1 failed. Reported failure #123 to qa-lead.`
7.  **Report Back:** Inform `qa-lead` using `attempt_completion`, referencing task log and summarizing results/escalations.