# SvelteKit Dev: Key Concepts & Best Practices

This summarizes core SvelteKit concepts and important best practices.

## 1. Key Concepts Reminder

*   **Framework:** Built on Svelte (compiler-based). Focuses on performance and developer experience.
*   **File-based Routing (`src/routes/`):** Directory structure defines URL paths.
    *   `+page.svelte`: Page component UI.
    *   `+layout.svelte`: Layout component UI (wraps pages/child layouts). Requires `<slot />`.
    *   `+page.js`/`.server.js`: `load` functions for page data.
    *   `+layout.js`/`.server.js`: `load` functions for layout data.
    *   `+page.server.js`: `actions` object for form handling.
    *   `+server.js`: API endpoint handlers (GET, POST, etc.).
    *   `+error.svelte`: Error page UI.
    *   `[param]`, `[[param]]`, `[...param]`: Dynamic, optional, rest route parameters.
    *   `(group)`: Layout groups (apply layout without adding URL segment).
*   **Load Functions (`load` export):** Fetch data before components render.
    *   Universal (`.js`): Runs on server & client. Use `fetch` argument, `depends()`.
    *   Server (`.server.js`): Runs only on server. Access `locals`, `cookies`, `setHeaders`. Use for sensitive data/operations.
    *   Return serializable data object. Access via `data` prop. Use `await parent()` for layout data.
*   **Form Actions (`actions` export in `+page.server.js`):** Handle server-side form submissions (`POST`).
    *   Receive `request`, `locals`, `cookies`, etc. Use `await request.formData()`.
    *   Use `fail()` for validation errors (returns data to `form` prop).
    *   Use `redirect()` for navigation after success.
    *   Return data object for success messages/state.
    *   Use `<form use:enhance>` for progressive enhancement (client-side fetch without full reload).
*   **Progressive Enhancement:** Build features that work without JavaScript (standard form posts, server-rendered data) and enhance them with client-side JS (`use:enhance`, client-side `fetch`, stores).
*   **Hooks (`src/hooks.server.js`, `src/hooks.client.js`):** Intercept requests/responses.
    *   `handle` (Server): Auth, set `event.locals`, modify response. **Must `await resolve(event)`**.
    *   `handleFetch` (Server): Intercept server-side `fetch`.
    *   `handleError` (Server/Client): Log unexpected errors. Return value shapes `$page.error`.
*   **Stores (`$app/stores`, `svelte/store`):** Manage reactive state (`page`, `navigating`, `updated`, custom `writable`/`readable`/`derived`).
*   **Adapters (`svelte.config.js`):** Configure build output for deployment targets (Node, Vercel, Netlify, Static, etc.).

## 2. Best Practices & Security

*   **TypeScript:** Strongly recommended for type safety, especially with `load` and `action` data. Use generated types (`./$types`).
*   **Server-Side Validation:** **ALWAYS** validate data received in `actions` and `+server.js` handlers on the server, even if client-side validation exists. Never trust client input.
*   **Authorization:** Check user permissions in server `load` functions, `actions`, and `+server.js` handlers (often using `locals` set in the `handle` hook) before accessing or modifying data. Use `error(403, ...)` or `redirect()` for unauthorized access.
*   **Sensitive Data:** Use server `load` (`.server.js`) for fetching sensitive data or using private credentials/API keys. Do not expose secrets to the client bundle.
*   **Error Handling:**
    *   Use `error()` helper for expected errors (404, 401, 403).
    *   Use `fail()` for form validation errors.
    *   Implement user-friendly `+error.svelte` pages.
    *   Use `handleError` hooks primarily for *logging* unexpected errors, returning only safe information (generic message, error ID) to the client.
*   **Progressive Enhancement:** Design forms and data loading to work without JavaScript first, then enhance with `use:enhance` and client-side fetching where appropriate.
*   **`fetch` Argument:** Always prefer the `fetch` provided to `load` functions over global `fetch` for correct credential/relative path handling.
*   **`depends()`:** Use `depends()` in universal `load` functions to ensure data re-fetches correctly after mutations invalidate related data.
*   **Environment Variables:** Use `$env/static/private` and `$env/dynamic/private` for server-side secrets, `$env/static/public` and `$env/dynamic/public` for client-safe variables (see SvelteKit docs on Environment Variables).