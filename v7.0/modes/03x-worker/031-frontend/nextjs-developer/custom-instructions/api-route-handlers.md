# Next.js API Route Handlers (App Router)

Creating backend API endpoints within your Next.js application using Route Handlers.

## Core Concept

Route Handlers allow you to create API endpoints by exporting functions named after HTTP methods (GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS) within a `route.ts` (or `.js`) file inside the `app/` directory. They execute **only on the server**.

## File Convention

*   Place `route.ts` (or `.js`) files within the `app/` directory, often grouped under an `api/` subdirectory. The folder structure defines the URL path.
    *   `app/api/hello/route.ts` -> Handles requests to `/api/hello`
    *   `app/api/items/[id]/route.ts` -> Handles requests to `/api/items/:id`

## Implementation

*   **Export HTTP Method Functions:** Export `async` functions named `GET`, `POST`, `PUT`, etc.
*   **Request Object:** These functions receive a `NextRequest` object (extended from the standard `Request`) as the first argument. Access URL parameters, search params, headers, cookies, and request body.
*   **Context (Dynamic Routes):** For dynamic routes (e.g., `[id]`), the function receives a second argument containing the `params` object: `async function GET(request: NextRequest, { params }: { params: { id: string } })`.
*   **Response Object:** Return a `NextResponse` object (extended from the standard `Response`) or a standard `Response` object to send data back to the client. `NextResponse.json()` is a common helper.

**Example: GET Request**
```typescript
// app/api/users/route.ts
import { NextRequest, NextResponse } from 'next/server';
// import { db } from '@/lib/db'; // Example database import

export async function GET(request: NextRequest) {
  try {
    // Optional: Get search params
    const searchParams = request.nextUrl.searchParams;
    const limit = searchParams.get('limit');

    // TODO: Fetch users from database, potentially using limit
    // const users = await db.user.findMany({ take: limit ? parseInt(limit) : undefined });
    const users = [{ id: 1, name: 'Alice' }, { id: 2, name: 'Bob' }]; // Placeholder

    return NextResponse.json({ users });
  } catch (error) {
    console.error("[API_USERS_GET]", error);
    return new NextResponse("Internal Server Error", { status: 500 });
  }
}
```

**Example: POST Request**
```typescript
// app/api/users/route.ts (continued)
import { z } from 'zod'; // Example validation

const userSchema = z.object({
  name: z.string().min(1, "Name is required"),
  email: z.string().email("Invalid email"),
});

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const validation = userSchema.safeParse(body);

    if (!validation.success) {
      return new NextResponse(JSON.stringify(validation.error.flatten()), { status: 400 });
    }

    // TODO: Check authorization if needed (e.g., using auth() from Clerk)
    // const { userId } = auth();
    // if (!userId) return new NextResponse("Unauthorized", { status: 401 });

    // TODO: Create user in database
    // const newUser = await db.user.create({ data: validation.data });
    const newUser = { id: 3, ...validation.data }; // Placeholder

    return NextResponse.json(newUser, { status: 201 }); // 201 Created
  } catch (error) {
    console.error("[API_USERS_POST]", error);
    return new NextResponse("Internal Server Error", { status: 500 });
  }
}
```

**Example: Dynamic Route (GET by ID)**
```typescript
// app/api/users/[userId]/route.ts
import { NextRequest, NextResponse } from 'next/server';

export async function GET(
  request: NextRequest,
  { params }: { params: { userId: string } }
) {
  try {
    const userId = params.userId;
    // TODO: Fetch user by ID from database
    // const user = await db.user.findUnique({ where: { id: userId } });
    const user = { id: userId, name: `User ${userId}` }; // Placeholder

    if (!user) {
      return new NextResponse("User not found", { status: 404 });
    }

    return NextResponse.json(user);
  } catch (error) {
    console.error("[API_USER_ID_GET]", error);
    return new NextResponse("Internal Server Error", { status: 500 });
  }
}
// Implement PUT, DELETE similarly using params.userId
```

## Caching & Revalidation

*   Route Handlers are **dynamically rendered by default**.
*   You can configure caching behavior using Route Segment Config options or by manually setting cache headers on the `NextResponse`.
    *   `export const dynamic = 'force-dynamic'` (Default)
    *   `export const dynamic = 'force-static'` (Attempt to statically render at build time - fails if dynamic functions are used)
    *   `export const revalidate = 60;` (ISR - revalidate every 60 seconds)
*   Data fetched *within* a Route Handler using `fetch` follows the caching rules described in `data-fetching.md`.

## Use Cases vs. Server Actions

*   **Route Handlers:**
    *   Ideal for creating traditional REST or GraphQL API endpoints.
    *   Needed when fetching data from Client Components.
    *   Good for webhook handlers.
    *   Provide fine-grained control over request/response objects and headers.
*   **Server Actions:**
    *   Often simpler for handling form submissions and data mutations directly from components (Server or Client).
    *   Provide automatic type safety between client and server function calls.
    *   Reduce the need for manually creating many small API endpoints just for mutations.

*(Refer to the official Next.js Route Handlers documentation: https://nextjs.org/docs/app/building-your-application/routing/route-handlers)*