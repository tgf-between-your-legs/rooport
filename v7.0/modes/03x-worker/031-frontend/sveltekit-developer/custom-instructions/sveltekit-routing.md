# SvelteKit: File-Based Routing (`src/routes`)

Understanding SvelteKit's routing system based on the file structure within `src/routes`.

## Core Concept: Filesystem Defines Routes

SvelteKit uses the structure of your `src/routes` directory to define the routes of your application. Special filenames indicate the purpose of each file within a route segment.

**Key Files & Folders:**

*   **`src/routes/`:** The root directory for all application routes.
*   **Folders:** Each folder creates a new URL path segment (e.g., `src/routes/about` -> `/about`, `src/routes/blog/posts` -> `/blog/posts`).
*   **`+page.svelte`:** Defines the UI component for a specific route. This file makes the route accessible.
*   **`+layout.svelte`:** Defines a layout component that wraps the current route segment (`+page.svelte`) and any child routes. Layouts persist during navigation between child routes. The root layout (`src/routes/+layout.svelte`) is required and wraps the entire application. Child routes are rendered within the `<slot />` element of the layout.
*   **`+page.js` / `+page.ts`:** Contains a universal `load` function that runs on both the server (during SSR) and the client (during client-side navigation) to fetch data for the corresponding `+page.svelte`.
*   **`+page.server.js` / `+page.server.ts`:** Contains a server-only `load` function (runs only on the server) and/or an `actions` object (for handling form submissions server-side).
*   **`+layout.js` / `+layout.ts`:** Universal `load` function for the corresponding `+layout.svelte`. Data returned is available to the layout and all child pages.
*   **`+layout.server.js` / `+layout.server.ts`:** Server-only `load` function for the corresponding `+layout.svelte`.
*   **`+server.js` / `+server.ts`:** Defines server-side API endpoints (Route Handlers) for a specific path. Exports functions like `GET`, `POST`, etc.
*   **`+error.svelte`:** A component that renders when an error occurs during loading or rendering for that route segment or its children. Receives error data via the `$page.error` store.

## Route Parameters (Dynamic Segments)

*   Use square brackets `[]` around a folder or file name to create a dynamic segment (e.g., `src/routes/blog/[slug]/+page.svelte` matches `/blog/post-1`, `/blog/my-article`).
*   The value of the parameter is available in `load` functions via the `params` object (e.g., `params.slug`).
*   **Rest Parameters:** Use `[...param]` to match all subsequent segments (e.g., `src/routes/files/[...path]/+page.svelte` matches `/files/a/b/c`, `params.path` would be `'a/b/c'`).
*   **Optional Parameters:** Use double square brackets `[[param]]` to make a segment optional (e.g., `src/routes/users/[[id]]/+page.svelte` matches `/users` and `/users/123`).

## Layouts

*   **Root Layout (`src/routes/+layout.svelte`):** Required. Wraps all pages. Typically contains `<html>`, `<head>`, `<body>`, and common elements like headers/footers. Must include `<slot />` where page content will be rendered.
*   **Nested Layouts:** Create a `+layout.svelte` file within a folder (e.g., `src/routes/dashboard/+layout.svelte`). This layout wraps all routes within that folder (e.g., `/dashboard`, `/dashboard/settings`). It must also contain a `<slot />` for its child page or layout. Data from parent layout `load` functions is available via the `parent()` function within child `load` functions.

```svelte
<!-- src/routes/dashboard/+layout.svelte -->
<script lang="ts">
  import { page } from '$app/stores'; // Access page data store
  // export let data; // Data from this layout's load function
</script>

<nav>
  <a href="/dashboard" class:active={$page.url.pathname === '/dashboard'}>Overview</a>
  <a href="/dashboard/settings" class:active={$page.url.pathname === '/dashboard/settings'}>Settings</a>
</nav>

<main>
  <!-- Child page (+page.svelte or nested +layout.svelte) renders here -->
  <slot />
</main>

<style>
  nav { /* ... styles ... */ }
  .active { font-weight: bold; }
</style>
```

## Layout Groups (`(group)`)

*   **Purpose:** Apply a layout to a group of routes *without* adding a segment to the URL path.
*   **Syntax:** Wrap a folder name in parentheses `()`.
*   Example: `src/routes/(app)/dashboard/+page.svelte` still maps to `/dashboard`, but it will use the layout defined in `src/routes/(app)/+layout.svelte`. Useful for separating marketing pages from authenticated app sections.

## Navigation

*   Use standard HTML `<a>` tags for navigation. SvelteKit automatically intercepts clicks on local links to perform client-side navigation.
*   **Prefetching:** Add `data-sveltekit-prefetch` attribute to an `<a>` tag to prefetch the route's code and data on hover or tap. Add `data-sveltekit-prefetch-opts='{"viewport": true}'` to prefetch when the link enters the viewport.
*   **Programmatic Navigation:** Use `goto` from `$app/navigation`. `import { goto } from '$app/navigation'; goto('/path', { replaceState: true, invalidateAll: true });`
*   **Link Options:** Add attributes like `data-sveltekit-reload` (force full page reload), `data-sveltekit-replacestate` (use `history.replaceState`), `data-sveltekit-keepfocus` (prevent focus reset), `data-sveltekit-noscroll` (prevent scrolling to top).

SvelteKit's file-based routing provides an intuitive way to structure your application, manage layouts, and handle data loading and mutations within specific route contexts.

*(Refer to the official SvelteKit documentation on Routing, Layouts, and Load functions.)*