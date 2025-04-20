# SvelteKit Load Functions (`+page.js`, `+page.server.js`)

Fetching data for SvelteKit pages and layouts before they render.

## Core Concept

`load` functions run before a component (page or layout) renders, allowing you to fetch data and provide it as props. SvelteKit distinguishes between `load` functions that run only on the server and those that can run on both server and client.

## 1. Server Load (`+page.server.js` or `+layout.server.js`)

*   **Purpose:** Runs **only on the server**. Use this for fetching data directly from databases, using private environment variables, or accessing server-only resources.
*   **File Naming:** Must be named `+page.server.js` (or `.ts`) for page data or `+layout.server.js` (or `.ts`) for layout data.
*   **Syntax:** Export an `async` function named `load`. It receives an event object containing `params`, `fetch`, `locals`, `cookies`, `parent`, etc.
*   **Return Value:** Must return an object containing the data to be passed as props to the corresponding `+page.svelte` or `+layout.svelte`. Data must be serializable (plain objects, arrays, primitives).
    ```typescript
    // src/routes/products/[productId]/+page.server.ts
    import { error } from '@sveltejs/kit';
    import type { PageServerLoad } from './$types';
    // import { db } from '$lib/server/db'; // Example DB import

    export const load: PageServerLoad = async ({ params, locals }) => {
      console.log('Server load running...');
      // TODO: Check user permissions using locals.user if needed
      // if (!locals.user) { throw error(401, 'Unauthorized'); }

      const productId = params.productId;
      // TODO: Fetch product from database
      // const product = await db.product.findUnique({ where: { id: productId } });
      const product = productId === '123' ? { id: productId, name: 'Awesome Gadget', price: 99.99 } : null; // Placeholder

      if (!product) {
        // Use the error helper for expected errors like "not found"
        throw error(404, 'Product not found');
      }

      // Return data for the page component
      return {
        product: product // This will be available as `data.product` in +page.svelte
      };
    };
    ```
    ```svelte
    <!-- src/routes/products/[productId]/+page.svelte -->
    <script lang="ts">
      import type { PageData } from './$types';
      export let data: PageData; // Receives data returned from load
    </script>

    {#if data.product}
      <h1>{data.product.name}</h1>
      <p>Price: ${data.product.price}</p>
    {:else}
      <p>Product details not available.</p>
    {/if}
    ```

## 2. Universal Load (`+page.js` or `+layout.js`)

*   **Purpose:** Runs **on the server** during initial SSR and **on the client** during client-side navigation. Use this for fetching data from public APIs or when the code needs to run in both environments.
*   **File Naming:** Must be named `+page.js` (or `.ts`) for page data or `+layout.js` (or `.ts`) for layout data.
*   **Syntax:** Similar to server `load`, but the event object has fewer properties (e.g., no direct `locals` or `cookies` access on the client). It receives `fetch` (a version that handles credentials and relative paths), `params`, `data` (from parent load functions), `parent`.
*   **Dependencies (`depends`):** Use `depends()` with URL strings to tell SvelteKit when this `load` function should re-run based on external dependencies changing (e.g., after a form action invalidates data).
*   **Return Value:** Same as server `load` - an object with serializable data.
    ```typescript
    // src/routes/blog/+page.js
    import type { PageLoad } from './$types';

    export const load: PageLoad = async ({ fetch, depends }) => {
      console.log('Universal load running (server or client)...');

      // Mark this load function as dependent on 'app:posts'
      // If something invalidates 'app:posts', this load function will re-run.
      depends('app:posts');

      // Fetch data from a public API or a SvelteKit endpoint (+server.js)
      const response = await fetch('/api/posts'); // Use provided fetch
      if (!response.ok) {
         // Handle fetch error, potentially using the error helper
         // import { error } from '@sveltejs/kit'; throw error(...)
         return { posts: [], error: 'Failed to load posts' };
      }
      const posts = await response.json();

      return {
        posts: posts // Available as data.posts in +page.svelte
      };
    };
    ```

## Combining Server and Universal Load

*   If both `+page.server.js` and `+page.js` exist for the same route, **both** run.
*   The universal `load` function receives the data returned from the server `load` function via its `data` property in the event object.
*   This allows server-only data fetching combined with client/server logic (e.g., fetching sensitive data on the server, then fetching public data and merging them in the universal load).

## Layout Load Functions (`+layout.js`, `+layout.server.js`)

*   Work similarly to page `load` functions but provide data for layout components (`+layout.svelte`).
*   Data returned from parent layout `load` functions is available to child layout and page `load` functions via the `parent()` function within the event object.
    ```typescript
    // src/routes/dashboard/+layout.server.ts
    import type { LayoutServerLoad } from './$types';

    export const load: LayoutServerLoad = async ({ locals }) => {
      // Fetch user data available to all dashboard routes
      return {
        user: locals.user // Assume user is attached in hooks.server.js
      };
    };

    // src/routes/dashboard/settings/+page.js
    import type { PageLoad } from './$types';

    export const load: PageLoad = async ({ parent }) => {
      const { user } = await parent(); // Get data from parent layout load
      return {
        title: `Settings for ${user?.name ?? 'User'}`
        // Can fetch additional page-specific data here
      };
    };
    ```

## Key Considerations

*   **Serialization:** Data returned from `load` must be serializable (no Dates, Maps, Sets, functions, etc., unless using libraries like `devalue`).
*   **Error Handling:** Use the `error` helper from `@sveltejs/kit` to throw expected errors (like 404 Not Found). These will be caught by the nearest `+error.svelte` boundary. Uncaught errors trigger `handleError`.
*   **`fetch`:** Always use the `fetch` provided to the `load` function argument. It's enhanced to handle credentials, relative paths, and server-side fetching correctly.
*   **`parent()`:** Call `await parent()` in child `load` functions to access data from parent layouts.
*   **`depends()`:** Use in universal `load` functions to ensure data re-fetches when necessary after mutations or external changes.

*(Refer to the official SvelteKit documentation on Loading Data: https://kit.svelte.dev/docs/load)*