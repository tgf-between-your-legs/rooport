# Custom Instructions for 🔑 Clerk Auth Specialist Mode

This directory contains specific instructions and guidelines for the `clerk-auth-specialist` mode, focusing on integrating Clerk for authentication and user management.

## Instruction Files:

*   **`01-principles.md`**: Core operational principles, best practices, and tool usage guidelines.
*   **`02-workflow-collaboration.md`**: Standard operational workflow, collaboration points, and escalation procedures.
*   **`03-setup-keys.md`**: Securely configuring Clerk API keys (Publishable and Secret) using environment variables.
*   **`04-frontend-integration.md`**: Setting up `<ClerkProvider>` and using pre-built components (`<SignIn>`, `<UserButton>`, etc.) and hooks (`useUser`, `useAuth`) in React/Next.js.
*   **`05-custom-ui-elements.md`**: Building custom authentication UIs using Clerk Elements (`@clerk/elements/*`).
*   **`06-route-protection.md`**: Protecting frontend and backend routes in Next.js (App & Pages Router), Remix, and Express using middleware and server-side helpers.
*   **`07-session-jwt.md`**: Understanding Clerk session management, token flow, and using JWT Templates for custom claims.
*   **`08-backend-integration.md`**: Using the Clerk Backend SDK (`clerkClient`) for server-side user/resource management and backend protection concepts.
*   **`09-webhooks.md`**: Setting up, receiving, and securely verifying webhook events from Clerk.
*   **`10-advanced-features.md`**: Implementing Clerk Organizations for multi-tenancy and Multi-Factor Authentication (MFA).
*   **`11-safety-error-handling.md`**: Key security considerations and patterns for handling errors in frontend flows, backend operations, and webhooks.

*(Consult these files alongside official Clerk documentation for specific implementation details.)*