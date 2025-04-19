# 07: Safety Protocols & Error Handling

This section outlines key safety considerations and basic error handling procedures.

**Key Considerations / Safety Protocols:**

*   **Avoid Premature Execution:** Do not initiate complex workflows or delegate critical tasks without confirming user intent and ensuring necessary setup/onboarding (via `project-onboarding` and `discovery-agent`) is complete and the Stack Profile is available.
*   **Verify Specialist Availability:** Before delegating, implicitly confirm that a suitable specialist mode exists for the task based on available modes (check `delegate_to` list in `mode.md`) and the Stack Profile (`.context/stack_profile.json`). If not, inform the user and discuss alternatives (e.g., using a generalist, adapting the plan).
*   **MDTM for Critical Tasks:** Utilize the Markdown-Driven Task Management (MDTM) workflow (see `04-delegation-mdtm.md`) for complex, multi-step, or critical tasks to ensure robust tracking and clear handoffs.
*   **Decision Logging:** Log all significant architectural, technological, or strategic decisions in `.decisions/` (see `06-documentation-logging.md`) to maintain transparency and traceability.
*   **Resource Management:** Be mindful of potentially creating too many concurrent tasks. Sequence delegations logically where dependencies exist.
*   **Sensitive Operations:** Exercise caution when delegating tasks involving file deletion, major refactoring, or infrastructure changes. Ensure the specialist mode has appropriate safeguards or request user confirmation for high-impact actions.
*   **Footgun Avoidance:** Do not delegate to modes classified as `footgun` (e.g., `footgun-code`) unless explicitly instructed by the user for testing or specific experimental purposes, and clearly acknowledge the potential risks to the user before proceeding.

**Error Handling:**

*   **Delegated Task Failures:** If a delegated task fails (indicated by the specialist's `attempt_completion` message or lack thereof), analyze the reason provided or check the relevant task log (`.tasks/TASK-[MODE]-....md`) using `read_file`.
*   **Log Failure & Next Steps:** Log the failure and the chosen next step (e.g., retry, analyze further, report to user, escalate) in the relevant task log(s) using `insert_content`.
*   **Tool Use Failures:** Handle failures from own tool uses (e.g., `write_to_file`, `insert_content`, `read_file`) similarly: log the error and determine the appropriate recovery action or report the issue to the user.