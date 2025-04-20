# SvelteKit: Load Functions (`load`)

Fetching data for pages and layouts using SvelteKit's `load` function.

## Core Concept: Data Loading Before Navigation

SvelteKit's `load` function is the primary mechanism for fetching data required by a page (`+page.svelte`) or layout (`+layout.svelte`) **before** it renders. This ensures data is available when the component mounts, preventing loading spinners within the component itself for initial data.

**Key Features:**

*   **Runs Before Component:** Executes before the associated `.svelte` component renders.
*   **Server & Client Execution:** Can run on the server (during SSR) and/or the client (during client-side navigation), depending on the filename used.
*   **Data Availability:** Data returned from `load` is accessible within the corresponding `.svelte` component via the `data` prop (or `$page.data` store).
*   **Parallel Execution:** For nested routes, `load` functions for all active layouts and the page run in parallel during navigation.
*   **Error Handling:** Errors thrown (or returned via the `error()` helper) are caught by the nearest `+error.svelte` boundary.

## Universal vs. Server Load Functions

1.  **Universal `load` (`+page.js` / `+layout.js`):**
    *   **Runs on both server and client.**
    *   **Use Cases:** Fetching data from public APIs, processing URL parameters, accessing data needed by both server render and client interactions.
    *   **Limitations:** Cannot directly access server-only resources (databases, file system, private environment variables). Cannot use server-only modules.
    *   **`fetch`:** Receives a `fetch` function argument that behaves like the native `fetch` but can make credentialed requests on the server and relative requests on the client.

2.  **Server `load` (`+page.server.js` / `+layout.server.js`):**
    *   **Runs ONLY on the server.** Never runs in the browser.
    *   **Use Cases:** Accessing databases directly, using private API keys or environment variables, performing sensitive operations.
    *   **Security:** Keeps sensitive logic and credentials off the client bundle.
    *   **`fetch`:** Can use native `fetch` or the provided `fetch` argument.

**Choosing:** Use server `load` if you need server-only access. Use universal `load` if the data can be fetched publicly or needs to run on both environments. You can have *both* a `+page.js` and `+page.server.js` for the same route; data from both is merged (server data takes precedence in case of key conflicts).

## Implementation

**1. Define `load` Function:**

*   Export an `async function load` from `+page.js`, `+page.server.js`, `+layout.js`, or `+layout.server.js`.
*   **Signature:** `export async function load({ fetch, params, parent, depends, url, route, data: serverData, cookies, locals, setHeaders }) { ... }`
    *   `fetch`: SvelteKit's enhanced `fetch` function.
    *   `params`: Dynamic route parameters.
    *   `parent`: Async function to get data from parent layout `load` functions (`const parentData = await parent();`).
    *   `depends`: Function to declare dependencies on URLs or custom identifiers, allowing fine-grained invalidation (`depends('app:posts')`).
    *   `url`: `URL` object of the current page.
    *   `route`: Object containing the route `id`.
    *   `data` (`serverData` in universal load): Data returned from the corresponding server `load` function (if both exist).
    *   `cookies` (Server load only): Helper object to get/set cookies.
    *   `locals` (Server load only): App-specific context added via `handle` hook.
    *   `setHeaders` (Server load only): Function to set HTTP headers for the response (e.g., `Cache-Control`).
*   **Return Value:** **Must return an object.** The properties of this object become available to the component via the `data` prop.

```typescript
// src/routes/products/[productId]/+page.server.ts (Server Load)
import type { PageServerLoad } from './$types';
import { error } from '@sveltejs/kit';
// import { getProductById, getStockLevel } from '$lib/server/db'; // Server-only DB access

export const load: PageServerLoad = async ({ params, fetch, depends, cookies, locals }) => {
  console.log(`Server Load: Fetching product ${params.productId}`);
  console.log('User ID from locals:', locals.userId); // Access data from hooks.server.js

  // Example: Declare dependency for invalidation
  depends('app:product:' + params.productId);

  // const product = await getProductById(params.productId);
  const product = { id: params.productId, name: `Product ${params.productId}`, price: 99 }; // Placeholder

  if (!product) {
    // Use error helper for expected errors like Not Found
    error(404, { message: `Product with ID ${params.productId} not found` });
  }

  // Fetch related data (can run in parallel)
  // const stock = await getStockLevel(params.productId);
  const stock = { level: 10 + Math.floor(Math.random() * 5) }; // Placeholder

  // Set cache header (example)
  // setHeaders({ 'Cache-Control': 'public, max-age=60' });

  // Return data object
  return {
    product,
    stockLevel: stock.level,
    streamed: {
        // Example: Return a promise for data to be streamed
        // reviews: fetch(`/api/products/${params.productId}/reviews`).then(r => r.json())
    }
  };
};
```

**2. Access Data in Component (`+page.svelte` / `+layout.svelte`):**

*   Data returned from the corresponding `load` function (and parent layout `load` functions) is automatically passed as a prop named `data`.
*   Use `export let data;` in the `<script>` block to receive the prop.
*   Access properties like `data.product`, `data.stockLevel`.
*   Streamed promises can be resolved using `{#await data.streamed.reviews}` block.

```svelte
<!-- src/routes/products/[productId]/+page.svelte -->
<script lang="ts">
  import type { PageData } from './$types'; // Import generated types

  export let data: PageData; // Receive data from load function(s)

  // Reactive statements update when data changes
  $: ({ product, stockLevel, streamed } = data);
</script>

<h1>{product.name}</h1>
<p>Price: ${product.price}</p>
<p>Stock: {stockLevel}</p>

{#if streamed?.reviews}
  <h2>Reviews</h2>
  {#await streamed.reviews}
    <p>Loading reviews...</p>
  {:then reviews}
    <ul>
      {#each reviews as review}
        <li>{review.text}</li>
      {/each}
    </ul>
  {:catch error}
    <p style="color: red">Error loading reviews: {error.message}</p>
  {/await}
{/if}

<!-- Add to cart form, etc. -->
```

The `load` function is central to SvelteKit's data fetching strategy, enabling efficient server-side or universal data loading before components render. Choose between universal and server load based on whether server-only access is required.

*(Refer to the official SvelteKit documentation on Loading Data.)*