# Astro Developer: Safety & Error Handling

## 1. Key Considerations / Safety Protocols

*   **Best Practices:** Adhere to established best practices for Astro (component structure, island architecture, content collections, routing, integrations, Astro DB, Astro Actions, middleware, performance).
*   **Efficiency:** Leverage Astro's zero-JS-by-default approach and selective hydration (`client:*` directives) for optimal performance. Use islands only where necessary.
*   **Server-Side Validation:** Crucial for validating all user input from forms or actions on the server (within Astro Actions or API routes). Do not rely solely on client-side validation. Use libraries like Zod (integrated with Actions) for schema validation.
*   **Performance:** Be aware that top-level `await fetch()` in `.astro` components can block rendering; consider alternatives like `server:defer` or client-side fetching if needed, especially in SSR mode. Use Astro's performance audit tools (`npx astro check --perf`).
*   **Environment Variables:** Use `.env` files and `import.meta.env` for managing environment-specific configurations securely. Prefix client-exposed variables with `PUBLIC_`. Do not commit sensitive keys to version control.
*   **Security Headers:** Consider adding security headers (CSP, HSTS, etc.) via middleware or deployment platform configuration.
*   **Dependencies:** Keep dependencies updated and audit them for known vulnerabilities.

## 2. Error Handling

*   **Build/Render Errors:** Address errors reported during `npm run build` or shown on the dev server error overlay. Check terminal output for details.
*   **API Route/Action Errors:** Implement proper error handling in API routes, middleware, and actions using try/catch blocks or result patterns. Return appropriate HTTP status codes (e.g., 400 for bad input, 401 for unauthorized, 404 for not found, 500 for server errors). Provide informative (but not overly revealing) error messages.
*   **Client-Side Errors:** Handle errors within island components (e.g., failed data fetches, invalid user input) using standard framework error handling techniques (try/catch, error boundaries in React). Provide user-friendly feedback.
*   **Tool Errors:** If tools fail (`execute_command`, `write_to_file`, etc.), report the error clearly via `attempt_completion`.
*   **Astro Action Errors:** Use `ActionError` from `astro:actions` for expected, structured errors (like validation failures or unauthorized access) that can be easily handled on the client. Let unexpected errors bubble up (they will likely result in a 500 status).

```typescript
// Example in Astro Action handler
import { ActionError } from 'astro:actions';

// ... inside handler ...
if (!isValid) {
  throw new ActionError({
    code: 'VALIDATION_FAILED',
    message: 'Input data is invalid.'
  });
}
// ...