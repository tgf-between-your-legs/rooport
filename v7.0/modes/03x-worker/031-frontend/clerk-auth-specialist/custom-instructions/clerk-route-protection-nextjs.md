# Clerk: Route Protection in Next.js (App & Pages Router)

Securing pages and API routes in Next.js applications using Clerk middleware and helpers.

## Core Concept

Route protection ensures that only authenticated users (and sometimes users with specific roles/permissions) can access certain pages or API endpoints. Clerk provides different mechanisms depending on whether you're using the Next.js App Router or Pages Router.

**Key Principles:**

*   **Protect Both Frontend & Backend:** Secure both the client-side pages (redirecting unauthenticated users) and the server-side API routes/Server Components/Actions (returning errors or filtering data).
*   **Use Middleware (App Router Recommended):** Clerk's middleware (`clerkMiddleware`) is the primary way to protect routes in the App Router, running on the server before the request reaches your page or API.
*   **Use Server-Side Helpers (Pages Router / Server Components):** Functions like `auth()` (App Router Server Components/Actions/Route Handlers) or `getAuth()` (Pages Router `getServerSideProps`/API routes) allow checking authentication state on the server.

## 1. App Router Protection (`middleware.ts`)

*   **Location:** Create a `middleware.ts` (or `.js`) file in your project's root directory (or inside `src/` if using `src/` directory).
*   **Implementation:** Import `clerkMiddleware` from `@clerk/nextjs/server`. Use it to define which routes are public and which require authentication.
*   **Configuration:**
    *   Pass an object to `clerkMiddleware` to configure public routes, ignored routes, and behavior after sign-in/sign-up.
    *   Use `createRouteMatcher` to easily define route patterns.

```typescript
// middleware.ts (in project root or src/)
import { clerkMiddleware, createRouteMatcher } from '@clerk/nextjs/server';

// Define routes that should NOT be protected
const isPublicRoute = createRouteMatcher([
  '/', // Home page
  '/sign-in(.*)', // Sign-in page and its sub-routes
  '/sign-up(.*)', // Sign-up page and its sub-routes
  '/api/webhooks/(.*)', // Example: Public webhook endpoint
]);

// Define routes that should be ignored by Clerk (e.g., static assets)
// Note: This is often not needed as Clerk tries to be smart about static files.
// const isIgnoredRoute = createRouteMatcher([
//   '/ignored-route(.*)',
// ]);

export default clerkMiddleware((auth, req) => {
  // If the route is not public, protect it.
  if (!isPublicRoute(req)) {
    auth().protect(); // If user is not signed in, redirects to sign-in page
  }

  // Example: Protect based on role for specific routes
  // const isAdminRoute = createRouteMatcher(['/admin(.*)']);
  // if (isAdminRoute(req)) {
  //   auth().protect((has) => {
  //     // Requires user to be signed in AND have the 'org:admin' role
  //     return has({ role: 'org:admin' });
  //   });
  // }
});

export const config = {
  // The following matcher runs middleware on all routes
  // except static assets.
  matcher: [ '/((?!.*\\..*|_next).*)', '/', '/(api|trpc)(.*)'],
};
```

*   **`auth().protect()`:** If the user is not authenticated, this function automatically redirects them to the sign-in page (URL configured in Clerk environment variables or dashboard). It can also accept a condition based on roles/permissions (`protect((has) => has({ role: 'admin' }))`).

## 2. App Router Server Component/Action/Route Handler Protection (`auth()`)

*   **Purpose:** Access authentication state directly within Server Components, Server Actions, or API Route Handlers (defined in `app/api/...`).
*   **Usage:** Import `auth` from `@clerk/nextjs/server`. Calling `auth()` returns an object with `userId`, `sessionId`, `orgId`, etc., or throws an error if the user is not authenticated (unless accessed within middleware first).

```typescript
// app/dashboard/page.tsx (Server Component Example)
import { auth } from '@clerk/nextjs/server';
import { redirect } from 'next/navigation';

export default function DashboardPage() {
  const { userId, orgId } = auth(); // Get auth state

  // Redirect if not signed in (alternative/addition to middleware)
  if (!userId) {
    redirect('/sign-in');
  }

  console.log('User ID:', userId);
  console.log('Org ID:', orgId);

  // Fetch data specific to the user/org
  // const data = await fetchDataForUser(userId);

  return (
    <div>
      <h1>Dashboard</h1>
      <p>Welcome, User {userId}!</p>
      {/* Display user-specific data */}
    </div>
  );
}

// app/api/mydata/route.ts (Route Handler Example)
import { auth } from '@clerk/nextjs/server';
import { NextResponse } from 'next/server';

export async function GET() {
  const { userId } = auth();

  if (!userId) {
    return new NextResponse("Unauthorized", { status: 401 });
  }

  // Fetch data for the authenticated user
  // const data = await fetchDataForUser(userId);
  const data = { message: `Data for user ${userId}` };

  return NextResponse.json({ data });
}
```

## 3. Pages Router Protection (`getServerSideProps` / API Routes)

*   **Purpose:** Protect pages rendered server-side or API routes in the Pages Router.
*   **Usage:** Import `getAuth` from `@clerk/nextjs/server`. Call it within `getServerSideProps` or your API route handler. It takes the `req` object as an argument.
*   **Return Value:** Returns an object with `userId`, `sessionId`, etc., or `null` if the user is not authenticated.

```typescript
// src/pages/protected-page.tsx (getServerSideProps Example)
import { getAuth } from '@clerk/nextjs/server';
import type { GetServerSideProps } from 'next';

export default function ProtectedPage({ userId }) {
  return <div>Protected Content for User ID: {userId}</div>;
}

export const getServerSideProps: GetServerSideProps = async (ctx) => {
  const { userId, sessionId } = getAuth(ctx.req);

  if (!userId) {
    // Redirect to sign-in page if not authenticated
    return {
      redirect: {
        destination: '/sign-in?redirect_url=' + encodeURIComponent(ctx.resolvedUrl),
        permanent: false,
      },
    };
  }

  // User is authenticated, pass userId as prop
  return { props: { userId } };
};

// src/pages/api/pages-data.ts (API Route Example)
import type { NextApiRequest, NextApiResponse } from 'next';
import { getAuth } from '@clerk/nextjs/server';

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  const { userId } = getAuth(req);

  if (!userId) {
    return res.status(401).json({ error: 'Unauthorized' });
  }

  // Fetch data specific to the user
  const data = { message: `Sensitive data for user ${userId}` };

  return res.status(200).json(data);
}
```

Choose the appropriate protection method based on your Next.js router version and whether you're protecting pages or APIs. Middleware is generally the most comprehensive approach for the App Router.

*(Refer to the official Clerk documentation for Next.js.)*