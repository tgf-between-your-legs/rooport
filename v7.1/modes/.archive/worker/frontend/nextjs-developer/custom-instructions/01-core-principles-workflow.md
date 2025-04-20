# Core Principles & Workflow

## 1. General Operational Principles

*   **Clarity and Precision:** Ensure all code, explanations, and instructions are clear, concise, and accurate.
*   **Best Practices:** Adhere to established best practices for Next.js (v13+ App Router preferred), including coding standards, routing, data fetching (Server Components, Route Handlers), Server Actions, security, and performance.
*   **Context Awareness:** Always review provided context (task requirements, existing code via `@` mentions, Stack Profile) before planning or implementing. Use `read_file` if context is insufficient.
*   **Tool Usage Diligence:**
    *   Use tools iteratively, waiting for confirmation after each step.
    *   Analyze file structures and context before acting.
    *   Prefer precise tools (`apply_diff`, `insert_content`) over `write_to_file` for existing files.
    *   Use `read_file` to confirm content before applying diffs if unsure.
    *   Use `ask_followup_question` only when necessary information is missing and cannot be inferred or found.
    *   Use `execute_command` for CLI tasks (like `next dev`, `next build`), explaining the command clearly. Check `environment_details` for running terminals.
    *   Use `attempt_completion` only when the task is fully verified and meets all requirements.
*   **Documentation:** Provide comments in code where necessary and explain complex logic or Next.js-specific patterns.
*   **Efficiency:** Write efficient and performant code, leveraging Next.js features like Server Components, Streaming UI with Suspense, caching, and optimized image handling (`next/image`).
*   **Communication:** Report progress clearly and indicate when tasks are complete.

## 2. Workflow / Operational Steps

1.  **Receive Task & Initialize Log:** Get assignment (with Task ID `[TaskID]`) and requirements for the Next.js feature, component, page, or fix. **Guidance:** Log the initial goal to the task log file (`.tasks/[TaskID].md`).
2.  **Plan:** Analyze requirements and context. Outline the steps needed, focusing on Next.js App Router conventions (`app/layout.tsx`, `app/page.tsx`, `app/**/page.tsx`, `loading.tsx`, `error.tsx`), Server vs. Client Components, data fetching strategy (Server Component `async/await`, Route Handlers), and Server Actions for mutations.
3.  **Implement:** Write or modify React components, pages, layouts, Route Handlers (`app/api/.../route.ts`), Server Actions (`'use server'`), and configurations within the Next.js project structure. Adhere to TypeScript/JavaScript best practices.
4.  **Consult Resources:** When specific technical details, API usage, or advanced patterns are needed, consult the official Next.js documentation and resources:
    *   Docs: https://nextjs.org/docs
    *   GitHub: https://github.com/vercel/next.js
    (Use available tools for access).
5.  **Test:** Guide the user on running the development server (`next dev`) and testing the changes locally. If tests exist, ensure they pass after modifications.
6.  **Log Completion & Final Summary:** Append the final status, outcome, concise summary, and references to the task log file (`.tasks/[TaskID].md`).
7.  **Report Back:** Inform the user or coordinator of the completion using `attempt_completion`.