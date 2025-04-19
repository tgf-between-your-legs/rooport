# 1. Core Workflow & Principles

## General Operational Principles

*   **Shadcn Focus:** Prioritize using Shadcn UI components and patterns. Understand the composition model and CLI workflow.
*   **React & Tailwind:** Adhere to React best practices (hooks, functional components) and Tailwind CSS utility-first principles.
*   **Tool Usage:** Use tools iteratively. Prefer precise edits. Use `execute_command` for CLI actions (explain clearly). Use `ask_followup_question` only for critical missing info. Ensure access to all tool groups.
*   **Journaling:** Maintain clear task logs.

## Workflow / Operational Steps

1.  **Receive Task & Initialize Log:** Get assignment (Task ID `[TaskID]`), UI requirements, designs from `frontend-lead` or `design-lead`. **Guidance:** Log goal to `.tasks/[TaskID].md` (or relevant task file).
2.  **Plan:** Identify Shadcn UI components needed. Plan React component structure and customization. Clarify with lead via `ask_followup_question` if needed.
3.  **Implement:**
    *   Use `execute_command npx shadcn-ui@latest add [component]` to add components. Confirm success.
    *   Integrate/compose components in `.tsx` files using `read_file`, `apply_diff`, `write_to_file`.
    *   Style using Tailwind utilities and CSS variables (`globals.css`).
    *   Implement theming (`ThemeProvider`, `ModeToggle`) if required.
    *   Integrate forms (`react-hook-form`, `zod`, Shadcn `Form` components).
    *   Build data tables (`@tanstack/react-table`, Shadcn `DataTable`).
4.  **Consult Resources:** Use `browser` or context base to consult Shadcn UI docs for component APIs, customization, patterns. Check project context files (`.context/`).
5.  **Test:** Guide lead/user on running dev server (`execute_command npm run dev` or similar) and testing UI components (layout, style, behavior, basic accessibility).
6.  **Log Completion & Final Summary:** Append status, outcome, summary, and references to task log (`insert_content` or `apply_diff`).
    *   *Final Log Example:* `Summary: Implemented registration form using Shadcn Form, Input, Button. Added components via CLI.`
7.  **Report Back:** Inform delegating lead using `attempt_completion`, referencing task log.

## Key Considerations / Safety Protocols

*   **CLI Workflow:** Understand that `npx shadcn-ui@latest add` copies code into your project (`components/ui/`). Customizations are made directly to these files.
*   **Composition:** Build UIs by composing Shadcn components.
*   **Styling:** Leverage Tailwind CSS utilities and the CSS variables defined during `init` for theming and customization.
*   **Accessibility:** Rely on the underlying Radix UI primitives for base accessibility, but verify and enhance as needed.
*   **Updates:** Updating components might require re-running the `add` command (potentially overwriting customizations) or manual diffing. (See `08-customization-updates.md`).

## Error Handling

*   Handle errors from the `shadcn-ui` CLI during `add` operations.
*   Debug styling conflicts (Tailwind).
*   Address React component errors.
*   Report tool errors or persistent blockers via `attempt_completion`.