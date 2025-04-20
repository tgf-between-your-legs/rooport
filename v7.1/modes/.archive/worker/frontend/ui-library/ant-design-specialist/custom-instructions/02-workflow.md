# 2. Workflow / Operational Steps

1.  **Receive Task & Initialize Log:** Get assignment (e.g., "Implement user settings form using Ant Design", Task ID `[TaskID]`) with requirements, mockups/designs, and context from `frontend-lead`. **Guidance:** Log the goal in `.tasks/[TaskID].md`.
2.  **Requirement Analysis & Component Selection:** Review UI requirements and designs (`read_file`). Identify the specific `antd` components needed (e.g., `Form`, `Input`, `Select`, `Button`, `DatePicker`, `Table`). Consult Ant Design documentation (`browser`) if unsure about component APIs or best choices. Use `ask_followup_question` to clarify requirements with `frontend-lead`.
3.  **Implementation:** Use `read_file`, `apply_diff`, or `write_to_file` to create/modify React component files (`.tsx`).
    *   Import necessary components from `antd`.
    *   Structure the component using JSX and Ant Design components.
    *   Implement component logic using React hooks (`useState`, `useEffect`, etc.) and TypeScript.
    *   Configure component props (e.g., `placeholder`, `options`, `rules` for Form.Item, `columns` for Table).
    *   Handle state updates and event handlers (`onChange`, `onClick`, `onFinish` for Form).
4.  **Form Handling (If applicable):**
    *   Use `Form` and `Form.Item` components.
    *   Define validation `rules` directly on `Form.Item`.
    *   Implement `onFinish` and `onFinishFailed` handlers for the `Form`.
    *   Use `form.setFieldsValue`, `form.getFieldValue`, `form.resetFields` instance methods if needed (get form instance via `Form.useForm()`).
5.  **Styling & Customization:**
    *   Apply custom styles using CSS Modules, Styled Components, or standard CSS/Less, coordinating with project conventions.
    *   Leverage Ant Design's `ConfigProvider` for theme customization (primary color, border radius, etc.) if applicable at the application level (coordinate with `frontend-lead`).
    *   Use `Row` and `Col` for responsive grid layouts.
6.  **State & Feedback:**
    *   Manage local state with `useState`. Use Context API or state management libraries (Redux, Zustand) for shared state as per project architecture.
    *   Use `message` or `notification` components for user feedback.
    *   Use `Modal` or `Popconfirm` for confirmations or dialogs.
7.  **Testing:**
    *   Write basic unit tests for component logic if feasible.
    *   Manually test component behavior, responsiveness across different screen sizes (using browser dev tools), and form validation in a running application (`execute_command npm run dev` or similar). Perform basic keyboard navigation checks.
8.  **Documentation:** Add JSDoc comments to component props and key functions. Explain complex logic or configurations.
9.  **Log Completion & Report Back:** Update the task log (`apply_diff`). Use `attempt_completion` to report to `frontend-lead`, summarizing work and referencing modified files.