# Clerk Backend Protection (Next.js Focus)

Examples of protecting backend API routes and server-side logic using Clerk with Next.js.

## 1. Middleware (`middleware.ts` - App & Pages Router)

*   **Purpose:** Protects pages and API routes by checking authentication status before the request reaches the handler. Redirects unauthenticated users for pages, returns 401/403 for API routes.
*   **Setup:** Create `middleware.ts` at the root of your project (or inside `src/` if using `src` directory).
*   **Implementation:** Use `clerkMiddleware` from `@clerk/nextjs/server`. Configure `publicRoutes` and `ignoredRoutes`.
    ```typescript
    // middleware.ts
    import { clerkMiddleware, createRouteMatcher } from '@clerk/nextjs/server';

    // Define routes that should NOT be protected
    const isPublicRoute = createRouteMatcher([
      '/', // Example: Public homepage
      '/sign-in(.*)',
      '/sign-up(.*)',
      '/api/webhooks(.*)', // Example: Public webhook endpoint
    ]);

    // Define routes that should be ignored by Clerk (e.g., static assets)
    // const isIgnoredRoute = createRouteMatcher([
    //   '/favicon.ico',
    //   '/img/(.*)',
    // ]);

    export default clerkMiddleware((auth, req) => {
      // Protect all routes except public routes
      if (!isPublicRoute(req)) {
        auth().protect(); // If not public, require authentication
      }

      // If you need to ignore routes (less common with App Router's default behavior)
      // if (isIgnoredRoute(req)) {
      //   return; // Do nothing for ignored routes
      // }
    });

    export const config = {
      // The following matcher runs middleware on all routes
      // except static assets.
      matcher: [ '/((?!.*\\..*|_next).*)', '/', '/(api|trpc)(.*)'],
    };
    ```
*   **Behavior:**
    *   Unauthenticated access to protected pages -> Redirects to Sign In URL (configurable in Clerk Dashboard or env vars).
    *   Unauthenticated access to protected API routes -> Returns 401 Unauthorized.
    *   Authenticated access -> Proceeds to page/API route.

## 2. Server Components / Server Actions / Route Handlers (App Router - `auth()`)

*   **Purpose:** Access authentication state and user ID directly within server-side code (Server Components, Server Actions, API Route Handlers).
*   **Helper:** Use the `auth()` helper function from `@clerk/nextjs/server`.
    ```typescript
    // Example: Server Component (app/dashboard/page.tsx)
    import { auth } from '@clerk/nextjs/server';

    export default function DashboardPage() {
      const { userId } = auth(); // Get userId, or null if not logged in

      if (!userId) {
        // Technically middleware should handle this, but good practice for defense-in-depth
        // redirect('/sign-in'); // Or handle appropriately
        return <div>Unauthorized</div>;
      }

      // Fetch user-specific data using userId
      // const userData = await fetchUserData(userId);

      return (
        <div>
          <h1>Dashboard</h1>
          <p>Welcome, User {userId}!</p>
          {/* Display user data */}
        </div>
      );
    }

    // Example: API Route Handler (app/api/items/route.ts)
    import { auth } from '@clerk/nextjs/server';
    import { NextResponse } from 'next/server';

    export async function GET() {
      const { userId } = auth();

      if (!userId) {
        return new NextResponse("Unauthorized", { status: 401 });
      }

      // Fetch items specific to the user
      // const items = await fetchUserItems(userId);
      const items = [{ id: 1, name: 'Test Item' }]; // Placeholder

      return NextResponse.json({ items });
    }
    ```
*   **`auth()` returns:** `{ userId, sessionId, getToken, orgId, orgRole, orgSlug, has, ... }` or throws an error if used incorrectly outside server context.

## 3. API Routes / `getServerSideProps` (Pages Router - `getAuth`)

*   **Purpose:** Access authentication state server-side during page rendering (`getServerSideProps`) or within API routes.
*   **Helper:** Use `getAuth` from `@clerk/nextjs/server`.
    ```typescript
    // Example: getServerSideProps (pages/protected-page.tsx)
    import { getAuth } from '@clerk/nextjs/server';
    import type { GetServerSideProps } from 'next';

    export const getServerSideProps: GetServerSideProps = async (ctx) => {
      const { userId, sessionId } = getAuth(ctx.req);

      if (!userId) {
        return {
          redirect: {
            destination: '/sign-in',
            permanent: false,
          },
        };
      }

      // Fetch data using userId if needed
      // const data = await fetchData(userId);

      return { props: { /* data */ } };
    };

    // Example: API Route (pages/api/my-data.ts)
    import { getAuth } from '@clerk/nextjs/server';
    import type { NextApiRequest, NextApiResponse } from 'next';

    export default async function handler(req: NextApiRequest, res: NextApiResponse) {
      const { userId } = getAuth(req);

      if (!userId) {
        return res.status(401).json({ error: 'Unauthorized' });
      }

      // Fetch user-specific data
      // const data = await fetchData(userId);
      const data = { message: `Data for user ${userId}` }; // Placeholder

      return res.status(200).json(data);
    }
    ```

## 4. Backend SDK (`clerkClient`)

*   **Purpose:** Interact with the Clerk Backend API directly from your server-side code (e.g., create users, manage organizations, update metadata). Requires the **Secret Key**.
*   **Usage:** Import `clerkClient` from `@clerk/nextjs/server` (or `@clerk/backend`).
    ```typescript
    import { clerkClient } from '@clerk/nextjs/server';

    async function getUserList() {
      // Ensure this runs only on the server where CLERK_SECRET_KEY is available
      try {
        const users = await clerkClient.users.getUserList();
        return users;
      } catch (error) {
        console.error("Error fetching users:", error);
        return [];
      }
    }
    ```

*(Always prioritize using the framework-specific helpers (`auth()`, `getAuth`, `clerkMiddleware`) where possible, as they handle session verification automatically. Use `clerkClient` for direct backend API interactions.)*