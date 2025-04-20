# Citation Formats

Use these formats for citing sources within research summaries and task logs. Consistency is key.

## 1. Web Pages / Online Articles

*   **Format:** `[Page Title](URL) - [Site Name/Author], [Date Accessed/Published]`
*   **Example:** `[React Hooks Documentation](https://react.dev/reference/react/useState) - react.dev, 2025-04-14`
*   **Example:** `[State Management in Microfrontends](https://martinfowler.com/articles/micro-frontends.html#StateManagement) - Martin Fowler, 2025-04-14`

## 2. Local Project Files

*   **Format:** `[File Path Relative to Project Root]`
*   **Example:** `.planning/project_vision.md`
*   **Example:** `src/utils/auth.js`
*   **Example:** `.decisions/ADR-003-database-choice.md`

## 3. Task Logs

*   **Format:** `[Task Log File Path]`
*   **Example:** `.tasks/TASK-FE-123.md`

## 4. Code Snippets (within summary)

*   If including a direct code snippet, mention the source file immediately before or after the code block.
*   **Example:**
    ```markdown
    As seen in `src/components/Button.jsx`:
    ```jsx
    function Button({ onClick, children }) {
      return <button onClick={onClick}>{children}</button>;
    }
    ```
    ```

## 5. References Section

*   At the end of the research summary report, include a `## References` section.
*   List all cited sources using a consistent format (e.g., bullet points with the full citation).
*   **Example:**
    ```markdown
    ## References
    *   [React Hooks Documentation](https://react.dev/reference/react/useState) - react.dev, 2025-04-14
    *   `.planning/project_vision.md`
    *   `.tasks/TASK-FE-123.md`
    ```

*(Adapt these formats slightly if needed, but maintain consistency within a report.)*