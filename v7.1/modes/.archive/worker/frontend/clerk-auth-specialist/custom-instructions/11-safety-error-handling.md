# Custom Instructions: Safety & Error Handling

## 1. Key Considerations / Safety Protocols

*   **Security Focus:** Ensure Clerk Publishable/Secret Keys are handled via environment variables (`CLERK_PUBLISHABLE_KEY`, `CLERK_SECRET_KEY`, etc.) and **never** exposed client-side (for secret keys) or committed to version control. Review configurations for security best practices (e.g., secure cookie settings in middleware, webhook secret verification). See `03-setup-keys.md`.
*   **Route Protection:** Implement protection on both frontend routes (redirecting unauthenticated users) and backend API routes/server actions (returning 401/403 errors or filtering data based on auth state). See `06-route-protection.md`.
*   **Session Management:** Understand Clerk's session management mechanisms and configure them appropriately (e.g., timeouts in Clerk Dashboard). Be aware of JWT statelessness when using custom claims. See `07-session-jwt.md`.
*   **Custom UI (Elements):** Ensure custom UIs built with Clerk Elements maintain accessibility standards (semantic HTML, ARIA attributes, focus management). See `05-custom-ui-elements.md`.
*   **Webhook Security:** Always verify webhook signatures using the `CLERK_WEBHOOK_SECRET`. See `09-webhooks.md`.

## 2. Error Handling

*   **Frontend Flows:** Implement robust error handling for all authentication flows (login, sign-up, etc.) using Clerk's provided mechanisms:
    *   **Pre-built Components:** Errors are often displayed automatically within `<SignIn>`, `<SignUp>`, etc.
    *   **Clerk Elements:** Use `<SignIn.GlobalError />`, `<SignUp.GlobalError />` for step-level errors and `<Clerk.FieldError />` within `<Clerk.Field>` for input-specific errors.
    *   **Hooks:** Check for errors returned by Clerk hook actions or use `isClerkAPIResponseError` from `@clerk/shared` or specific SDKs to identify Clerk API errors and access details like `error.errors[0].longMessage` for user-friendly messages.
*   **Loading States:** Handle loading states appropriately:
    *   **Hooks:** Use the `isLoaded` boolean returned by `useAuth`, `useUser`, `useSession` before relying on auth state or user data.
    *   **Clerk Elements:** Use `<Clerk.Loading>` to conditionally render loading indicators during pending actions.
*   **Backend/Webhooks:** Implement standard try/catch blocks and logging for operations involving `clerkClient` or webhook processing. Return appropriate HTTP status codes (e.g., 401, 403, 500).
*   **Tool Errors:** Report tool errors or persistent blockers encountered during development via `attempt_completion` to the lead.