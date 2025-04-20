# App Router: API Route Handlers

Creating API endpoints within the Next.js App Router using Route Handlers.

## Core Concept: Route Handlers

Route Handlers allow creating custom API endpoints within the `app/` directory, similar to API routes in the Pages Router. Define them by exporting named functions corresponding to HTTP methods (`GET`, `POST`, `PUT`, etc.) from a `route.ts` (or `.js`) file.

**Key Features:**

*   **File Convention:** Place `route.ts` files within `app/` (often `app/api/`) to define endpoints (e.g., `app/api/users/route.ts` -> `/api/users`).
*   **HTTP Methods:** Export `async` functions: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`.
*   **Request & Response:** Handlers receive `NextRequest` (extends `Request`) and should return `NextResponse` (extends `Response`) or a standard `Response`. `NextResponse.json()` is a common helper.
*   **Server-Side Execution:** Run only on the server (or edge).
*   **Use Cases:** Building APIs, webhooks, backend for Client Components, serving dynamic non-page content.
*   **Caching:** `GET` handlers are cached by default (like RSC fetches). Use dynamic functions (`cookies()`, `headers()`, `NextRequest`) or `fetch` with `cache: 'no-store'` to opt into dynamic execution. Other methods (`POST`, `PUT`, etc.) are always dynamic.

## Defining Route Handlers

```typescript
// app/api/items/route.ts
import { NextResponse, NextRequest } from 'next/server';
import { cookies, headers } from 'next/headers'; // Example dynamic functions

// --- GET Handler ---
export async function GET(request: NextRequest) {
  const searchParams = request.nextUrl.searchParams;
  const limit = searchParams.get('limit');
  const userPref = cookies().get('user-preference')?.value; // Dynamic
  const authHeader = headers().get('Authorization'); // Dynamic

  console.log(`GET /api/items - Limit: ${limit}, Pref: ${userPref}`);

  try {
    // const items = await getItemsFromDB({ limit }); // Fetch data
    const items = [{ id: 1, name: 'Default Item' }]; // Placeholder
    return NextResponse.json(items);
  } catch (error) {
    console.error('GET /api/items Error:', error);
    return new NextResponse('Internal Server Error', { status: 500 });
  }
}

// --- POST Handler ---
export async function POST(request: NextRequest) {
  try {
    const body = await request.json(); // Read request body

    // Validate input (e.g., using Zod)
    if (!body.name) {
      return NextResponse.json({ error: 'Item name is required' }, { status: 400 });
    }

    // Perform action (e.g., create item in DB)
    // const newItem = await createItemInDB(body);
    const newItem = { id: Date.now(), ...body }; // Placeholder

    return NextResponse.json(newItem, { status: 201 }); // 201 Created
  } catch (error) {
    console.error('POST /api/items Error:', error);
    if (error instanceof SyntaxError) {
        return new NextResponse('Invalid JSON body', { status: 400 });
    }
    return new NextResponse('Internal Server Error', { status: 500 });
  }
}
```

## Dynamic Route Segments

Route Handlers can use dynamic segments (`[id]`, `[...slug]`). The `params` object is passed as the second argument.

```typescript
// app/api/items/[id]/route.ts
import { NextResponse, NextRequest } from 'next/server';

// GET /api/items/:id
export async function GET(
  request: NextRequest,
  { params }: { params: { id: string } } // Access params
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
    return new NextResponse(null, { status: 204 }); // No Content
  } catch (error) {
    return new NextResponse('Internal Server Error', { status: 500 });
  }
}
```

## Use Cases vs. Server Actions

*   **Route Handlers:** Best for traditional REST/GraphQL endpoints, fetching data *from* Client Components, webhook handlers, fine-grained request/response control.
*   **Server Actions:** Often simpler for form submissions and mutations directly from components, better type safety between client/server calls, reduces need for many small mutation API endpoints.

*(Refer to the official Next.js documentation on Route Handlers.)*