# Next.js: Route Handlers (App Router API Routes)

Creating API endpoints within the Next.js App Router using Route Handlers.

## Core Concept: Route Handlers

Route Handlers allow you to create custom API endpoints within the `app/` directory, similar to API routes in the Pages Router. They are defined by exporting named functions corresponding to HTTP methods (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`) from a `route.ts` (or `.js`) file.

**Key Features:**

*   **File Convention:** Place `route.ts` or `route.js` files within the `app/` directory structure to define endpoints (e.g., `app/api/users/route.ts` handles requests to `/api/users`).
*   **HTTP Methods:** Export async functions named `GET`, `POST`, `PUT`, `PATCH`, `DELETE`.
*   **Request & Response:** Handlers receive a `NextRequest` object (extending the standard `Request`) and should return a `NextResponse` object (extending the standard `Response`) or a standard `Response`.
*   **Server-Side Execution:** Route Handlers execute only on the server (or at the edge, depending on configuration/deployment).
*   **Use Cases:** Building APIs, handling webhooks, serving dynamic content not suitable for pages, backend for Server Actions (less common now).
*   **Caching:** `GET` handlers are cached by default similar to Server Component fetches. Use dynamic functions (`cookies()`, `headers()`, `NextRequest`) or `fetch` with `cache: 'no-store'` to opt into dynamic execution. `POST`, `PUT`, etc., are always dynamic.

## Defining Route Handlers

Create a `route.ts` file within your desired API path under `app/`.

```typescript
// app/api/items/route.ts
import { NextResponse, NextRequest } from 'next/server';
import { cookies, headers } from 'next/headers'; // Example: Using dynamic functions
// Assume db functions exist
// import { getItemsFromDB, createItemInDB } from '@/lib/db';

// --- GET Handler ---
// Handles GET requests to /api/items
export async function GET(request: NextRequest) {
  // Access search parameters
  const searchParams = request.nextUrl.searchParams;
  const limit = searchParams.get('limit');

  // Access cookies (opts into dynamic rendering)
  const userPref = cookies().get('user-preference')?.value;

  // Access headers (opts into dynamic rendering)
  const authHeader = headers().get('Authorization');

  console.log(`GET /api/items - Limit: ${limit}, Pref: ${userPref}, Auth: ${authHeader}`);

  try {
    // Fetch data (caching behavior depends on fetch options and dynamic functions used)
    // const items = await getItemsFromDB({ limit: limit ? parseInt(limit) : undefined });
    const items = [{ id: 1, name: 'Default Item' }]; // Placeholder

    // Return data using NextResponse.json()
    return NextResponse.json(items);
  } catch (error) {
    console.error('GET /api/items Error:', error);
    // Return error response
    return new NextResponse('Internal Server Error', { status: 500 });
  }
}

// --- POST Handler ---
// Handles POST requests to /api/items
export async function POST(request: NextRequest) {
  try {
    // Read request body (e.g., JSON)
    const body = await request.json();

    // Validate input data (e.g., using Zod)
    // ... validation logic ...
    if (!body.name) {
      return NextResponse.json({ error: 'Item name is required' }, { status: 400 });
    }

    // Perform action (e.g., create item in database)
    console.log('POST /api/items - Creating item:', body);
    // const newItem = await createItemInDB(body);
    const newItem = { id: Date.now(), ...body }; // Placeholder

    // Return success response
    return NextResponse.json(newItem, { status: 201 }); // 201 Created
  } catch (error) {
    console.error('POST /api/items Error:', error);
    if (error instanceof SyntaxError) { // Handle JSON parsing error
        return new NextResponse('Invalid JSON body', { status: 400 });
    }
    return new NextResponse('Internal Server Error', { status: 500 });
  }
}

// --- Other Methods (PUT, PATCH, DELETE) ---
// export async function PUT(request: NextRequest, { params }: { params: { id: string } }) { ... }
// export async function DELETE(request: NextRequest, { params }: { params: { id: string } }) { ... }
```

## Dynamic Route Segments in Route Handlers

Route Handlers can also use dynamic segments similar to pages. The `params` object is passed as the second argument to the handler function.

```typescript
// app/api/items/[id]/route.ts

import { NextResponse, NextRequest } from 'next/server';
// import { getItemById, deleteItemById } from '@/lib/db';

// GET /api/items/:id
export async function GET(
  request: NextRequest,
  { params }: { params: { id: string } } // Access params here
) {
  const id = params.id;
  try {
    // const item = await getItemById(id);
    const item = { id: id, name: `Item ${id}` }; // Placeholder
    if (!item) {
      return NextResponse.json({ error: 'Item not found' }, { status: 404 });
    }
    return NextResponse.json(item);
  } catch (error) {
    return new NextResponse('Internal Server Error', { status: 500 });
  }
}

// DELETE /api/items/:id
export async function DELETE(
  request: NextRequest,
  { params }: { params: { id: string } }
) {
  const id = params.id;
  try {
    // await deleteItemById(id);
    console.log(`Deleted item ${id}`);
    return new NextResponse(null, { status: 204 }); // 204 No Content on successful delete
  } catch (error) {
    return new NextResponse('Internal Server Error', { status: 500 });
  }
}
```

Route Handlers are the standard way to build backend API endpoints within the Next.js App Router, allowing server-side logic execution triggered by HTTP requests. They integrate with Next.js's caching and rendering system.

*(Refer to the official Next.js documentation on Route Handlers.)*