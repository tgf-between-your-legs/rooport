# SvelteKit Dev: Routing

SvelteKit uses a filesystem-based router, meaning the structure of your `src/routes` directory defines the application's URL paths.

## 1. Core Concepts

*   **`src/routes/`:** The root directory for all application routes.
*   **Folders:** Each folder creates a URL path segment (e.g., `src/routes/about` -> `/about`).
*   **`+page.svelte`:** Defines the UI component for a specific route. This file makes the route accessible.
*   **`+layout.svelte`:** Defines a layout component wrapping the current route segment and any child routes. Layouts persist during navigation between child routes.
*   **`+server.js` / `+server.ts`:** Defines server-side API endpoints (Route Handlers).
*   **`+error.svelte`:** Renders when an error occurs for that route segment or its children.

## 2. Layouts

*   **Root Layout (`src/routes/+layout.svelte`):** Required. Wraps all pages. Contains `<html>`, `<head>`, `<body>`, common elements (header/footer), and a `<slot />` where page content is rendered.
*   **Nested Layouts:** A `+layout.svelte` within a folder (e.g., `src/routes/dashboard/+layout.svelte`) wraps all routes within that folder. It must also contain a `<slot />`. Data from parent layout `load` functions is available via `await parent()` in child `load` functions.

## 3. Route Parameters (Dynamic Segments)

*   **Basic Parameter (`[param]`):**
    *   Use square brackets `[]` for dynamic segments (e.g., `src/routes/blog/[slug]/+page.svelte` matches `/blog/post-1`).
    *   Value available in `load` functions via `params.slug`.
*   **Optional Parameter (`[[param]]`):**
    *   Use double square brackets `[[]]` for optional segments (e.g., `src/routes/users/[[id]]/+page.svelte` matches `/users` and `/users/123`).
    *   `params.id` will be `undefined` if the segment is absent.
    *   Useful for pages that serve dual purposes (e.g., list view vs. detail view).
*   **Rest Parameter (`[...param]`):**
    *   Use `[...]` to match *one or more* path segments at the *end* of a route (e.g., `src/routes/files/[...path]/+page.svelte` matches `/files/a/b/c`, `params.path` is `"a/b/c"`).
    *   Does **not** match the base path (e.g., `/files` in the example).
    *   Useful for file browsers, nested documentation.

## 4. Layout Groups (`(group)`)

*   **Purpose:** Apply a layout to a group of routes *without* adding a segment to the URL path.
*   **Syntax:** Wrap a folder name in parentheses `()`.
*   **Example:** `src/routes/(app)/dashboard/+page.svelte` still maps to `/dashboard`, but uses the layout from `src/routes/(app)/+layout.svelte`. Useful for separating sections with different layouts (e.g., marketing vs. authenticated app).

## 5. Route Guards (Protection)

Implement guards using:

*   **Server `load` Functions (Recommended):** Check auth/permissions in `+layout.server.js` or `+page.server.js`. Use `redirect()` (from `@sveltejs/kit`) or `error()` (from `@sveltejs/kit`) if checks fail. This prevents unauthorized access before rendering.
    ```typescript
    // src/routes/admin/+layout.server.ts
    import type { LayoutServerLoad } from './$types';
    import { redirect } from '@sveltejs/kit';

    export const load: LayoutServerLoad = async ({ locals }) => {
      if (!locals.user?.isAdmin) { // Assume user set in hooks.server.js
        redirect(303, '/login?redirectTo=/admin');
      }
      return {}; // Allow access
    };
    ```
*   **`handle` Hook (`src/hooks.server.js`):** Perform global checks based on `event.url.pathname`. Can redirect or modify `event.locals`. Suitable for global rules or setting up user context. (See `06-hooks.md`).

## 6. Navigation

*   **Declarative:** Use standard HTML `<a>` tags. SvelteKit intercepts clicks for client-side navigation.
*   **Programmatic:** Use `goto` from `$app/navigation`.
    ```typescript
    import { goto } from '$app/navigation';
    goto('/path', { replaceState: false, invalidateAll: false });
    ```
*   **Prefetching:** Add `data-sveltekit-prefetch` to `<a>` tags to load code/data on hover/tap. Use `data-sveltekit-prefetch-opts='{"viewport": true}'` for viewport prefetching.
*   **Link Options:** Use attributes like `data-sveltekit-reload` (force reload), `data-sveltekit-replacestate`, `data-sveltekit-keepfocus`, `data-sveltekit-noscroll` to modify link behavior.