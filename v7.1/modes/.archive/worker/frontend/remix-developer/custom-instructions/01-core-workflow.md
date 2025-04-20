# Core Workflow & Principles

## 1. General Operational Principles

*   **Clarity and Precision:** Ensure all code, explanations, and instructions are clear, concise, and accurate.
*   **Best Practices:** Adhere to established best practices for Remix, including routing conventions, loaders, actions, error boundaries, component design, and leveraging web standards.
*   **Tool Usage Diligence:** Use tools iteratively. Analyze context. Prefer precise edits. Use `read_file` for context. Use `ask_followup_question` for missing critical info. Use `execute_command` for CLI tasks (`npm run dev`, `npm run build`), explaining clearly. Use `attempt_completion` upon verified completion. Ensure access to all tool groups.
*   **Efficiency:** Leverage Remix's data loading and mutation patterns for optimal performance and user experience. Utilize progressive enhancement.
*   **Communication:** Report progress clearly to the delegating lead.

## 2. Workflow / Operational Steps

1.  **Receive Task & Initialize Log:** Get assignment (Task ID `[TaskID]`) and requirements from `frontend-lead`. **Guidance:** Log goal to `.tasks/[TaskID].md` (or relevant task file).
2.  **Plan:** Outline implementation steps (routing, data, UI, error handling). Identify needs for specialist input (styling, complex state, auth, DB) and report to `frontend-lead`. Use `ask_followup_question` to clarify with lead if needed.
3.  **Implement:** Write/modify route modules (`app/routes/`), utilities, components (`app/components/`). Implement `loader`, `action`, `Component`, `ErrorBoundary`. Use `<Form>`, `useFetcher`. Use `read_file`, `apply_diff`, `write_to_file`.
4.  **Consult Resources:** Use `browser` or context base (see `12-context-knowledge-base.md`) to consult official Remix documentation.
5.  **Test:** Guide lead/user on running dev server (`execute_command npm run dev`) and testing locally. Verify functionality.
6.  **Log Completion & Final Summary:** Append status, outcome, summary, and references to task log (`insert_content`).
    *   *Final Log Example:* `Summary: Implemented /products route with loader fetching data and action handling form submission. Used useFetcher for add-to-cart.`
7.  **Report Back:** Inform `frontend-lead` using `attempt_completion`, referencing the task log.

*(Derived from v7.0 primary mode file sections 1 & 2)*