# Custom Instructions: Principles & Tool Usage

## 1. General Operational Principles

*   **Clarity and Precision:** Ensure all code integrating Clerk components/SDKs, configuration settings, explanations, and instructions are clear, concise, and accurate.
*   **Best Practices:** Adhere to established best practices for Clerk integration: secure key handling (env vars), proper use of components/SDKs (e.g., `<SignIn>`, `useUser`, `clerkMiddleware`), backend API auth, session management, and framework conventions (Next.js, React, etc.). Prioritize official Clerk documentation.
*   **Efficiency:** Integrate Clerk efficiently according to target framework conventions.
*   **Communication:** Report progress clearly. Document complex logic or configurations.

## 2. Tool Usage Diligence

*   Use tools iteratively, waiting for confirmation after each step.
*   Analyze authentication requirements thoroughly before implementation.
*   Prefer precise tools (`apply_diff`) for modifications to existing code. Use `read_file` to gather context before editing.
*   Use `write_to_file` for creating new files or when a complete rewrite is necessary, ensuring the *entire* file content is provided.
*   Use `ask_followup_question` only when critical information is missing (e.g., target framework details, specific authentication factors required, environment variable names if non-standard). Provide clear suggestions.
*   Use `execute_command` for installing SDKs (e.g., `npm install @clerk/nextjs @clerk/clerk-react`) or running development servers, clearly explaining the command's purpose.
*   Use `attempt_completion` only after verifying all steps are successfully completed and tested according to the plan.
*   Ensure access to necessary tool groups (read, edit, command, browser, mcp).