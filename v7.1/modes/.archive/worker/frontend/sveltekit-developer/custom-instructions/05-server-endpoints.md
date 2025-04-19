# SvelteKit Dev: Server Endpoints (`+server.js`)

Server endpoints allow you to create dedicated API routes within your SvelteKit application, separate from your pages.

## 1. Core Concept

*   **Purpose:** Create backend logic accessible via specific URLs, often used for:
    *   Data APIs consumed by your frontend (or external clients).
    *   Handling webhooks from third-party services.
    *   Serving dynamic non-HTML content (JSON, XML, etc.).
*   **File Convention:** Create a `+server.js` or `+server.ts` file within the `src/routes` directory structure. The file's path defines the endpoint URL (e.g., `src/routes/api/users/+server.ts` corresponds to `/api/users`).
*   **HTTP Method Handlers:** Export `async` functions named after HTTP methods (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `OPTIONS`, `HEAD`) to handle corresponding requests.
*   **Server-Side Execution:** All code within `+server.js` runs **only on the server**.
*   **Request/Response:**
    *   Handlers receive an event object `{ request, params, locals, cookies, url, route, fetch, ... }`.
    *   Handlers **must return a standard `Response` object**. Use helpers like `json()`, `text()`, or `error()` from `@sveltejs/kit` for convenience.

## 2. Implementation

```typescript
// src/routes/api/items/[itemId]/+server.ts
import type { RequestHandler } from './$types';
import { json, error, text } from '@sveltejs/kit';
// import { db } from '$lib/server/db'; // Example DB client
// import { authorize } from '$lib/server/auth'; // Example auth helper

// --- GET Handler ---
// Handles GET requests to /api/items/[itemId]
export const GET: RequestHandler = async ({ params, locals }) => {
  // Authorization check
  // if (!authorize(locals.user, 'read:item')) {
  //   return error(403, 'Forbidden');
  // }

  const itemId = params.itemId;
  try {
    // const item = await db.getItem(itemId);
    const item = { id: itemId, name: `Fetched Item ${itemId}`, price: Math.random() * 100 }; // Placeholder

    if (!item) {
      return error(404, `Item ${itemId} not found`);
    }
    return json(item); // Use json() helper
  } catch (err) {
    console.error(`API GET /api/items/${itemId} Error:`, err);
    return error(500, 'Failed to retrieve item');
  }
};

// --- PUT Handler ---
// Handles PUT requests to /api/items/[itemId]
export const PUT: RequestHandler = async ({ request, params, locals }) => {
  // if (!authorize(locals.user, 'update:item')) {
  //   return error(403, 'Forbidden');
  // }

  const itemId = params.itemId;
  try {
    const body = await request.json(); // Parse request body

    // Validation (example)
    if (!body.name || typeof body.name !== 'string') {
      return json({ message: 'Invalid name provided' }, { status: 400 });
    }

    // const updatedItem = await db.updateItem(itemId, { name: body.name });
    const updatedItem = { id: itemId, name: body.name }; // Placeholder

    if (!updatedItem) {
      return error(404, `Item ${itemId} not found for update`);
    }
    return json(updatedItem);
  } catch (err) {
    console.error(`API PUT /api/items/${itemId} Error:`, err);
    if (err instanceof SyntaxError) { // Handle invalid JSON
      return json({ message: 'Invalid JSON format' }, { status: 400 });
    }
    return error(500, 'Failed to update item');
  }
};

// --- DELETE Handler ---
// Handles DELETE requests to /api/items/[itemId]
export const DELETE: RequestHandler = async ({ params, locals }) => {
    // if (!authorize(locals.user, 'delete:item')) {
    //   return error(403, 'Forbidden');
    // }

    const itemId = params.itemId;
    try {
        // await db.deleteItem(itemId);
        console.log(`Deleted item ${itemId}`); // Placeholder
        // Return a text response with 204 No Content status
        return new Response(null, { status: 204 });
        // Or return text('Item deleted', { status: 200 });
    } catch (err) {
        console.error(`API DELETE /api/items/${itemId} Error:`, err);
        return error(500, 'Failed to delete item');
    }
};

// --- Fallback for other methods ---
// export const fallback: RequestHandler = async ({ request }) => {
//   return text(`Unsupported method ${request.method}`, { status: 405 });
// };
```

## 3. Fetching from Endpoints

Call these endpoints using `fetch`:

*   **Client-side (`.svelte`):** Use standard `fetch('/api/items')`.
*   **Load Functions/Actions:** Use the `fetch` argument provided (`await fetch('/api/items')`). This ensures correct handling of relative paths and credentials on the server.

## 4. Key Considerations

*   **Return `Response`:** Always return a `Response` object. Use helpers (`json`, `text`, `error`) or construct one manually (`new Response(...)`).
*   **Error Handling:** Use the `error()` helper for standard HTTP error responses. Catch unexpected errors and return appropriate `Response` objects (often status 500).
*   **Security:** Perform authentication and authorization checks within handlers, often using `locals` populated by the `handle` hook. Validate all incoming data.
*   **Dynamic Segments:** Endpoints can use dynamic parameters (`[param]`, `[[param]]`, `[...param]`) just like pages.