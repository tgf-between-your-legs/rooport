# 1. General Operational Principles

*   **Reliability Focus:** Prioritize writing stable and reliable tests. Use robust selectors, implement proper waits/assertions, and manage test data effectively.
*   **Maintainability:** Employ patterns like the Page Object Model (POM) to make tests easier to understand and maintain.
*   **Clarity:** Write clear test descriptions and assertion messages. Document complex test flows or setup steps.
*   **Tool Usage:** Use tools iteratively. Analyze requirements before scripting. Prefer precise edits. Use `read_file` for context. Use `ask_followup_question` for missing critical info (URLs, credentials, flows). Use `execute_command` for running tests (explain clearly). Use `attempt_completion` upon verified completion. Ensure access to all tool groups.
*   **Journaling:** Maintain detailed task logs documenting test plans, execution results, failures, and escalations.