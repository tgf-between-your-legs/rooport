# Custom Instructions: 🔥 SvelteKit Developer

This directory contains specific instructions and guidelines for the `sveltekit-developer` mode, supplementing the base system prompt.

## Instruction Files

1.  **`01-core-principles-workflow.md`**: General operational principles, best practices, and standard task workflow.
2.  **`02-routing.md`**: File-based routing, layouts, dynamic/optional/rest parameters, layout groups, navigation.
3.  **`03-load-functions.md`**: Universal vs. Server `load` functions, signature, return values, combining, layout loads, `parent()`, `depends()`.
4.  **`04-form-actions.md`**: Server-side form handling using the `actions` object, default/named actions, `fail()`, `redirect()`, progressive enhancement (`use:enhance`), `$page.form`.
5.  **`05-server-endpoints.md`**: Creating API routes using `+server.js`, HTTP method handlers, `Request`/`Response` objects, `json()` helper.
6.  **`06-hooks.md`**: Server (`handle`, `handleError`, `handleFetch`) and Client (`handleError`) hooks, `event.locals`.
7.  **`07-state-management.md`**: Using Svelte Stores (`writable`, `readable`, `derived`, `$app/stores`) and the Context API (`setContext`, `getContext`).
8.  **`08-error-handling.md`**: Using the `error()` helper, `+error.svelte` component, `handleError` hook (server/client), and `fail()` for validation.
9.  **`09-service-workers.md`**: Setup, `$service-worker` modules (`build`, `files`, `version`), lifecycle (`install`, `activate`, `fetch`), caching strategies.
10. **`10-adapters-deployment.md`**: Role of adapters, common adapters (`auto`, `node`, `static`, `vercel`), build process.
11. **`11-collaboration-escalation.md`**: Guidelines for collaborating with other specialist modes and escalating issues to the lead.
12. **`12-key-concepts-best-practices.md`**: Summary of core SvelteKit ideas and security/best practice considerations.