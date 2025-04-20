# SvelteKit Dev: Load Functions (`load`)

The `load` function is SvelteKit's primary mechanism for fetching data required by a page (`+page.svelte`) or layout (`+layout.svelte`) **before** it renders. This ensures data is available when the component mounts.

## 1. Core Concept

*   **Runs Before Component:** Executes before the associated `.svelte` component renders.
*   **Server & Client Execution:** Can run on the server (SSR) and/or the client (client-side navigation), depending on the filename.
*   **Data Availability:** Data returned from `load` is accessible in the component via the `data` prop (and `$page.data` store).
*   **Parallel Execution:** `load` functions for all active layouts and the page run in parallel during navigation.
*   **Error Handling:** Use the `error()` helper (from `@sveltejs/kit`) for expected errors, caught by `+error.svelte`.

## 2. Universal vs. Server Load

**a) Universal `load` (`+page.js` / `+layout.js`)**

*   **Runs:** On **both** server (SSR) and client (navigation).
*   **Use Cases:** Fetching from public APIs, processing URL `params`, logic needed in both environments.
*   **Limitations:** Cannot directly access server-only resources (DBs, private env vars). Cannot use server-only modules.
*   **`fetch`:** Receives an enhanced `fetch` that handles credentials/relative paths.
*   **`depends()`:** Use `depends('identifier')` to mark dependencies. If the identifier is invalidated (e.g., by a form action), this `load` function re-runs.

**b) Server `load` (`+page.server.js` / `+layout.server.js`)**

*   **Runs:** **ONLY** on the server. Never in the browser.
*   **Use Cases:** Accessing databases, using private API keys/env vars, sensitive operations.
*   **Security:** Keeps sensitive logic and credentials off the client bundle.
*   **`fetch`:** Can use the provided `fetch` or native Node `fetch`.
*   **Arguments:** Receives additional server-only arguments like `cookies`, `locals`, `setHeaders`.

**Choosing:**

*   Use **Server `load`** if you need server-only access (DB, secrets).
*   Use **Universal `load`** if data is public or logic must run on both client/server.
*   You can have **both** for the same route. They run sequentially (server then universal). Data from server `load` is available as the `data` property in the universal `load` function's argument.

## 3. Implementation

*   **Export:** `export async function load({ /* arguments */ }) { ... }`
*   **Arguments:**
    *   `fetch`: SvelteKit's enhanced `fetch`.
    *   `params`: Dynamic route parameters (e.g., `params.id`).
    *   `parent`: Async function (`const data = await parent()`) to get data from parent layout `load` functions.
    *   `depends`: Function (`depends('app:posts')`) to declare invalidation dependencies (Universal load).
    *   `url`: `URL` object of the current page.
    *   `route`: Object containing the route `id`.
    *   `data`: Data returned from the corresponding server `load` (only in Universal load when both exist).
    *   `cookies` (Server load only): Helper to get/set cookies.
    *   `locals` (Server load only): Request-specific context from `hooks.server.js`.
    *   `setHeaders` (Server load only): Function to set response HTTP headers (e.g., `Cache-Control`).
*   **Return Value:** **Must return an object.** Properties must be serializable (plain objects, arrays, primitives, or use `devalue` for Dates, Maps, etc.). Data is passed to the component's `data` prop.
*   **Streaming:** Return promises within the object (e.g., `streamed: { reviews: fetch(...) }`) to stream data. Resolve in the component using `{#await data.streamed.reviews}`.

```typescript
// Example: src/routes/items/[id]/+page.server.ts
import type { PageServerLoad } from './$types';
import { error, json } from '@sveltejs/kit';
// import { getItemById } from '$lib/server/db';

export const load: PageServerLoad = async ({ params, locals, depends, setHeaders }) => {
  // Check auth using locals from hooks
  // if (!locals.user) error(401, 'Unauthorized');

  depends(`app:item:${params.id}`); // Invalidation dependency

  // const item = await getItemById(params.id);
  const item = { id: params.id, name: `Item ${params.id}` }; // Placeholder

  if (!item) {
    error(404, `Item ${params.id} not found`);
  }

  setHeaders({ 'Cache-Control': 'private, max-age=60' });

  return {
    item, // Passed as data.item
    // Example of streamed data
    // streamed: {
    //   details: fetch(`/api/items/${params.id}/details`).then(r => r.json())
    // }
  };
};
```

## 4. Accessing Data in Components

```svelte
<!-- src/routes/items/[id]/+page.svelte -->
<script lang="ts">
  import type { PageData } from './$types';
  export let data: PageData; // Receives data from load

  $: ({ item, streamed } = data); // Destructure reactively
</script>

<h1>{item.name}</h1>

{#if streamed?.details}
  {#await streamed.details}
    <p>Loading details...</p>
  {:then details}
    <p>{details.description}</p>
  {:catch err}
    <p>Error loading details: {err.message}</p>
  {/await}
{/if}
```

## 5. Key Considerations

*   **Serialization:** Ensure returned data is serializable or use `devalue`.
*   **Error Handling:** Use `error()` helper for expected errors (404, 401, etc.).
*   **`fetch`:** Always use the provided `fetch` argument for consistency and features.
*   **`parent()`:** Essential for accessing data from parent layouts.
*   **`depends()`:** Crucial for re-running universal `load` functions after data mutations.