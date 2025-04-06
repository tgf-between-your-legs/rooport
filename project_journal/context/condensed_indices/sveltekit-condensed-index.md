## SvelteKit - Condensed Context Index

### Overall Purpose
SvelteKit is a framework built on Svelte for creating robust, performant web applications of all sizes. It provides file-based routing, server-side rendering (SSR), data loading mechanisms, form handling, and deployment adapters, focusing on developer experience and optimized output.

### Core Concepts & Capabilities
*   **Project Structure:** Standardized layout (`src/routes`, `src/lib`, `static`, `svelte.config.js`, `vite.config.js`). Initialized via `npm create svelte@latest`.
*   **Routing:** File-based routing within `src/routes`. Folders define URL segments. Special files (`+page.svelte`, `+layout.svelte`, `+server.js`, etc.) define route behavior. Dynamic routes use `[param]` syntax (e.g., `src/routes/blog/[slug]`).
*   **Components:** Pages (`+page.svelte`) and Layouts (`+layout.svelte`) are Svelte components. Layouts wrap pages and persist across navigation. Use `$props()` rune to access props like `data` and `form`.
*   **Data Loading:** `load` functions exported from `+page.js` (client/server) or `+page.server.js` / `+layout.server.js` (server-only) fetch data for components. Data is passed via the `data` prop. Use provided `fetch`, access `params`, `locals`, and `parent` data.
*   **Form Handling:** Standard HTML `<form>` elements are enhanced. Server-side logic defined in `actions` object within `+page.server.js`. Actions handle `POST` requests, process `request.formData()`, interact with databases/APIs, and return responses (success, `fail` for validation, `redirect`). Progressive enhancement via `use:enhance`.
*   **Hooks:** Server-side hooks (`src/hooks.server.js`) modify framework behavior: `handle` (intercept requests, manage `event.locals`), `handleFetch` (modify server-side `fetch`), `handleError` (centralized error logging/reporting).
*   **Adapters:** Configure deployment target in `svelte.config.js` (e.g., `adapter-auto`, `adapter-node`, `adapter-static`, `adapter-vercel`, `adapter-cloudflare`). Adapters build the app for specific platforms.
*   **Service Workers:** Enable offline capabilities and caching via `src/service-worker.js`. Uses `$service-worker` module for build assets.
*   **Error Handling:** Use `error` helper from `@sveltejs/kit` in `load`/`actions` for expected errors (e.g., 404). Use `handleError` hook for unexpected errors. Display errors in UI using `form` prop or custom error pages (`src/error.html`).

### Key APIs / Components / Configuration / Patterns
*   **`+page.svelte`:** Defines the UI for a specific route. Receives `data` and `form` props.
*   **`+layout.svelte`:** Defines UI structure shared by child routes. Receives `data` prop and renders children via `{@render children()}`. Can use `setContext` for state sharing.
*   **`+page.js` / `+layout.js`:** Exports `load` function (runs on server & client) for fetching data.
*   **`+page.server.js` / `+layout.server.js`:** Exports `load` function (server-only) and `actions` object (server-only) for form handling. Can access private resources/credentials.
*   **`+server.js`:** Defines API endpoints (request handlers like `GET`, `POST`). Uses `json` helper for responses.
*   **`src/hooks.server.js`:** Exports `handle`, `handleError`, `handleFetch` hooks.
*   **`svelte.config.js`:** Main configuration file. Defines `kit.adapter`, Vite plugins, preprocessors, etc.
*   **`load({ params, fetch, parent, locals, cookies })`:** Function signature for data loading. `params` for route parameters, `fetch` for API calls, `parent` for parent layout data, `locals` for request-specific data (set in `handle`), `cookies` for cookie access (server-only).
*   **`actions = { default: async ({ request, cookies, locals }), namedAction: ... }`:** Structure for form actions in `+page.server.js`. Access `request.formData()`.
*   **`fail(status, data)`:** Function from `@sveltejs/kit` to return validation errors from actions. `data` is passed back to the page via the `form` prop.
*   **`redirect(status, location)`:** Function from `@sveltejs/kit` to perform server-side redirects in `load` or `actions`.
*   **`error(status, message)`:** Function from `@sveltejs/kit` to throw expected errors (e.g., 404, 401) in `load` or `actions`.
*   **`use:enhance`:** Svelte action (from `$app/forms`) applied to `<form>` for progressive enhancement (AJAX submission).
*   **`<svelte:head>`:** Element for setting page metadata like `<title>`.
*   **`$app/forms`:** Module providing `enhance` action.
*   **`$app/server`:** Module providing `read` function for accessing static assets within adapters.
*   **`$service-worker`:** Module providing `build`, `files`, `version` for service worker implementation.
*   **`event.locals`:** Object available in server hooks, `load`, `actions` to pass request-scoped data (e.g., user session). Set in `handle` hook.

### Common Patterns & Best Practices / Pitfalls
*   **Data Loading:** Return data from `load`, don't set global state. Use server `load` for sensitive data/operations.
*   **Form Validation:** Use `fail` to return specific errors and preserve user input. Display errors clearly in the UI using the `form` prop.
*   **Error Handling:** Distinguish expected (`error` helper) vs. unexpected (`handleError` hook) errors. Provide user-friendly error pages.
*   **State Management:** Use `load` for route data. Use stores or context API (`setContext`/`getContext`) for shared UI state within layouts/components.
*   **Progressive Enhancement:** Use `use:enhance` on forms for better UX, but ensure server-side actions work without JavaScript.
*   **SEO/Accessibility:** Set unique `<title>` in `<svelte:head>` for each page.

This index summarizes the core concepts, APIs, and patterns for SvelteKit. Consult the full source documentation (`project_journal/context/source_docs/sveltekit-llms-context-20250406.md`) for exhaustive details.