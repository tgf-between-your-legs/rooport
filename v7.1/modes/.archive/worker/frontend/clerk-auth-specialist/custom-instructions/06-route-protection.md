# Custom Instructions: Route Protection (Next.js, Remix, Express)

Securing pages and API routes using Clerk middleware and helpers across different frameworks.

## Core Concept

Route protection ensures only authenticated users (and sometimes users with specific roles/permissions) can access certain pages or API endpoints.

**Key Principles:**
*   **Protect Both Frontend & Backend:** Secure client-side pages (redirecting) and server-side APIs/logic (returning errors/filtering data).
*   **Use Middleware:** Clerk's middleware (`clerkMiddleware` for Next.js, `ClerkExpressRequireAuth` for Express) is often the primary mechanism.
*   **Use Server-Side Helpers:** Functions like `auth()` (Next.js App Router), `getAuth()` (Next.js Pages Router, Remix), or `authenticateRequest()` (core SDK) allow checking auth state on the server.

## 1. Next.js App Router Protection (`middleware.ts`)

*   **Location:** `middleware.ts` (or `.js`) in project root or `src/`.
*   **Implementation:** Use `clerkMiddleware` from `@clerk/nextjs/server`. Define public/protected routes using `createRouteMatcher`.
*   **`auth().protect()`:** Redirects unauthenticated users for pages, returns 401/403 for APIs. Can check roles/permissions: `auth().protect(has => has({ role: 'org:admin' }))`.

```typescript
// middleware.ts
import { clerkMiddleware, createRouteMatcher } from '@clerk/nextjs/server';

const isPublicRoute = createRouteMatcher([
  '/', '/sign-in(.*)', '/sign-up(.*)', '/api/webhooks/(.*)',
]);
const isAdminRoute = createRouteMatcher(['/admin(.*)']);

export default clerkMiddleware((auth, req) => {
  if (isAdminRoute(req)) {
    // Requires sign-in AND admin role
    auth().protect(has => has({ role: 'org:admin' }));
  } else if (!isPublicRoute(req)) {
    // Protect all other non-public routes
    auth().protect();
  }
});

export const config = {
  matcher: [ '/((?!.*\\..*|_next).*)', '/', '/(api|trpc)(.*)'],
};
```

## 2. Next.js App Router Server Component/Action/Route Handler Protection (`auth()`)

*   **Usage:** Import `auth` from `@clerk/nextjs/server`. Call `auth()` to get `userId`, `sessionId`, `orgId`, `sessionClaims`, etc. Throws error if unauthenticated (unless middleware ran first).

```typescript
// app/api/mydata/route.ts (Route Handler Example)
import { auth } from '@clerk/nextjs/server';
import { NextResponse } from 'next/server';

export async function GET() {
  const { userId, sessionClaims } = auth(); // Get auth state and custom claims

  if (!userId) {
    return new NextResponse("Unauthorized", { status: 401 });
  }

  const role = sessionClaims?.metadata?.role; // Access custom claim
  if (role !== 'editor') {
     return new NextResponse("Forbidden", { status: 403 });
  }

  // Fetch data for the authenticated user
  const data = { message: `Data for editor ${userId}` };
  return NextResponse.json({ data });
}
```

## 3. Next.js Pages Router Protection (`getServerSideProps` / API Routes)

*   **Usage:** Import `getAuth` from `@clerk/nextjs/server`. Call `getAuth(ctx.req)` in `getServerSideProps` or `getAuth(req)` in API routes. Returns `userId`, `sessionId`, etc., or `null`.

```typescript
// src/pages/protected-page.tsx (getServerSideProps Example)
import { getAuth } from '@clerk/nextjs/server';
import type { GetServerSideProps } from 'next';

export const getServerSideProps: GetServerSideProps = async (ctx) => {
  const { userId } = getAuth(ctx.req);
  if (!userId) {
    return { redirect: { destination: '/sign-in', permanent: false } };
  }
  return { props: { userId } }; // Pass userId if needed
};
// ... component using userId ...

// src/pages/api/pages-data.ts (API Route Example)
import type { NextApiRequest, NextApiResponse } from 'next';
import { getAuth } from '@clerk/nextjs/server';

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  const { userId } = getAuth(req);
  if (!userId) { return res.status(401).json({ error: 'Unauthorized' }); }
  // ... fetch data ...
  return res.status(200).json({ data: `Sensitive data for user ${userId}` });
}
```

## 4. Remix Protection (Loaders)

*   **SDK:** `@clerk/remix`
*   **Mechanism:** Use `getAuth` from `@clerk/remix/ssr.server` in route loader functions. Check `userId` and throw `redirect` if needed.

```typescript
// app/routes/dashboard.tsx (Remix Example)
import type { LoaderFunctionArgs } from "@remix-run/node";
import { redirect } from "@remix-run/node";
import { getAuth } from "@clerk/remix/ssr.server";
import { useLoaderData } from "@remix-run/react";

export const loader = async (args: LoaderFunctionArgs) => {
  const { userId } = await getAuth(args);
  if (!userId) { throw redirect("/sign-in"); }
  // ... fetch data ...
  return { userId, data: { /* ... */ } };
};

export default function Dashboard() {
  const { userId, data } = useLoaderData<typeof loader>();
  // ... render component ...
}
```

## 5. Express Protection (Middleware)

*   **SDK:** `@clerk/clerk-express`
*   **Mechanism:** Use `ClerkExpressRequireAuth()` (blocks unauthenticated) or `ClerkExpressWithAuth()` (makes `req.auth` available but doesn't block).

```javascript
// server.js (Express Example)
import express from 'express';
import { ClerkExpressRequireAuth } from '@clerk/clerk-express';

const app = express();

app.get(
  '/api/protected',
  ClerkExpressRequireAuth({ /* options */ }), // Middleware enforces auth
  (req, res) => {
    // req.auth is populated if authenticated
    const { userId } = req.auth;
    res.json({ data: `Sensitive data for ${userId}` });
  }
);

app.listen(3001);
```

## 6. Other Node.js Frameworks (Core SDK)

*   **SDK:** `@clerk/backend`
*   **Mechanism:** Use `authenticateRequest` within framework middleware/handlers. Pass request object and keys. Check returned status (`signed-in`, `signed-out`) and handle accordingly (call `next()`, return error/redirect).

```javascript
// Generic Node.js Example (Conceptual)
import { authenticateRequest } from '@clerk/backend';

async function myMiddleware(request, response, next) {
  try {
    const requestState = await authenticateRequest({ request, secretKey: process.env.CLERK_SECRET_KEY, /* ... */ });
    if (requestState.status === 'signed-in') {
      request.auth = requestState.toAuth(); // Attach auth state
      return next ? next() : /* handle success */;
    } else {
      return response.status(401).send('Unauthorized'); // Or redirect
    }
  } catch (error) {
    return response.status(401).send('Authentication Error');
  }
}
```

*(Refer to the official Clerk documentation for framework-specific details.)*