# SvelteKit: Server Endpoints (`+server.js`)

Creating dedicated API endpoints within your SvelteKit application.

## Core Concept: API Routes

While `+page.server.js` handles data loading (`load`) and form submissions (`actions`) for specific pages, SvelteKit also allows you to create dedicated API endpoints using `+server.js` (or `.ts`) files. These are useful for:

*   Providing a data API for your own frontend (e.g., for `fetch` calls from client-side JavaScript or `useFetcher` in Remix).
*   Creating endpoints for third-party services or webhooks.
*   Serving non-HTML content like JSON, XML, or images dynamically.

**Key Features:**

*   **File Convention:** Place a `+server.js` or `+server.ts` file within the `src/routes/` directory structure. The path to the file defines the endpoint URL (e.g., `src/routes/api/items/+server.ts` handles requests to `/api/items`).
*   **HTTP Method Exports:** Export `async` functions named after HTTP methods (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `OPTIONS`, `HEAD`).
*   **Request & Response:** Handler functions receive an event object containing `request` (standard Fetch `Request`), `params`, `locals`, `cookies`, `fetch`, `url`, etc., similar to server `load` functions. They **must return a standard `Response` object**.
*   **Server-Side Execution:** Code within `+server.js` runs **only on the server**.
*   **Helpers:** Use helpers like `json()` and `text()` from `@sveltejs/kit` to easily create `Response` objects with the correct headers.

## Implementation

```typescript
// src/routes/api/items/+server.ts

import type { RequestHandler } from './$types'; // Provides type safety for handlers
import { json, error, text } from '@sveltejs/kit';
// import { db } from '$lib/server/db'; // Example DB client
// import { verifyUser } from '$lib/server/auth'; // Example auth helper

// --- GET Handler ---
// Handles GET requests to /api/items
export const GET: RequestHandler = async ({ url, locals }) => {
  // Check authentication (example using locals from hooks.server.js)
  // if (!locals.user) {
  //   return error(401, 'Unauthorized'); // Use error helper
  // }

  const limit = Number(url.searchParams.get('limit') ?? 10);
  const offset = Number(url.searchParams.get('offset') ?? 0);

  try {
    // const items = await db.getItems({ limit, offset });
    const items = Array.from({ length: limit }, (_, i) => ({
      id: offset + i + 1,
      name: `Item ${offset + i + 1}`
    })); // Placeholder

    // Return JSON response using json() helper
    return json(items);
  } catch (err) {
    console.error('API GET Error:', err);
    // Use error() helper for standard error responses
    return error(500, 'Failed to retrieve items');
  }
};

// --- POST Handler ---
// Handles POST requests to /api/items
export const POST: RequestHandler = async ({ request, locals }) => {
  // if (!locals.user) {
  //   return error(401, 'Unauthorized');
  // }

  try {
    const body = await request.json(); // Parse JSON body

    // Validate input (e.g., using Zod)
    if (!body.name || typeof body.name !== 'string' || body.name.length < 3) {
      return json({ message: 'Invalid item name' }, { status: 400 });
    }

    // const newItem = await db.createItem({ name: body.name, userId: locals.user.id });
    const newItem = { id: Date.now(), name: body.name }; // Placeholder

    // Return newly created item with 201 status
    return json(newItem, { status: 201 });
  } catch (err) {
    console.error('API POST Error:', err);
    if (err instanceof SyntaxError) {
      return json({ message: 'Invalid JSON format' }, { status: 400 });
    }
    return error(500, 'Failed to create item');
  }
};

// --- Other Handlers (Example: Plain Text) ---
export const PUT: RequestHandler = async () => {
  // ... handle PUT logic ...
  return text('Item updated (placeholder)');
};

// --- Dynamic Segments ---
// You can also have dynamic segments like in pages:
// src/routes/api/items/[itemId]/+server.ts
// export const GET: RequestHandler = async ({ params }) => {
//   const itemId = params.itemId;
//   // ... fetch item by ID ...
//   return json({ id: itemId, name: `Item ${itemId}` });
// };
```

## Fetching from Endpoints

You can call these endpoints from:

*   **Client-side JavaScript:** Using standard `fetch` in `.svelte` components (often within `onMount` or event handlers).
*   **Load Functions:** Using the `fetch` argument provided to `load` functions (`+page.js`, `+page.server.js`). Making relative requests (`fetch('/api/items')`) works correctly.
*   **Server Actions:** Using standard `fetch` within `actions` in `+page.server.js`.

```svelte
<!-- src/routes/some-page/+page.svelte -->
<script lang="ts">
  import { onMount } from 'svelte';

  let items: any[] = [];
  let loading = true;

  onMount(async () => {
    try {
      const response = await fetch('/api/items?limit=5'); // Fetch from endpoint
      if (!response.ok) throw new Error('Network response was not ok');
      items = await response.json();
    } catch (error) {
      console.error("Failed to fetch items:", error);
    } finally {
      loading = false;
    }
  });
</script>

<h1>Items</h1>
{#if loading}
  <p>Loading items...</p>
{:else if items.length > 0}
  <ul>
    {#each items as item (item.id)}
      <li>{item.name}</li>
    {/each}
  </ul>
{:else}
  <p>No items found.</p>
{/if}
```

Server endpoints (`+server.js`) provide a clean way to build dedicated APIs within your SvelteKit application, leveraging standard web Request/Response objects and integrating with SvelteKit's server-side capabilities.

*(Refer to the official SvelteKit documentation on Server-only modules / Endpoints.)*