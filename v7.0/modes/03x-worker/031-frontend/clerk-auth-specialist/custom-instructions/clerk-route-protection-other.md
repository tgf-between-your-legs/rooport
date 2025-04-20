# Clerk: Route Protection (Remix, Express, etc.)

Patterns for protecting server-side routes and loaders in various frameworks using Clerk.

## Core Concept

While Next.js has specific helpers (`clerkMiddleware`, `getAuth`), Clerk provides backend SDKs and strategies to protect routes in other Node.js frameworks like Remix, Express, Fastify, etc. The general approach involves:

1.  **Authenticating the Request:** Using Clerk's backend SDK (`@clerk/backend`) or framework-specific helpers to verify the session token (JWT) present in the incoming request (usually via cookies or Authorization header).
2.  **Accessing Auth State:** Retrieving the `auth` object containing `userId`, `sessionId`, `orgId`, etc.
3.  **Enforcing Protection:** Checking for a valid `userId` (or specific roles/permissions) and either:
    *   Redirecting unauthenticated users (for page loads).
    *   Returning a 401/403 error (for API requests).
    *   Filtering data based on the `userId`/`orgId`.

## 1. Remix Protection (`rootAuthLoader`, Route Loaders)

*   **Framework:** Remix (`@remix-run/node`, `@remix-run/react`)
*   **SDK:** `@clerk/remix`
*   **Mechanism:**
    *   Use `rootAuthLoader` in `app/root.tsx` to load auth state and make it available via context. It also handles passing the publishable key.
    *   In individual route loader functions (`app/routes/some-route.tsx`), import `getAuth` from `@clerk/remix/ssr.server`.
    *   Call `await getAuth(args)` (where `args` are the loader arguments) to get the `auth` object (`userId`, etc.).
    *   Check `auth.userId` and throw a `redirect` if the user is not authenticated.

```typescript
// app/routes/dashboard.tsx (Remix Example)
import type { LoaderFunctionArgs } from "@remix-run/node";
import { redirect } from "@remix-run/node"; // Import redirect
import { getAuth } from "@clerk/remix/ssr.server"; // Import getAuth
import { useLoaderData } from "@remix-run/react";

export const loader = async (args: LoaderFunctionArgs) => {
  const { userId, sessionId } = await getAuth(args); // Get auth state

  if (!userId) {
    // Redirect to sign-in if not authenticated
    // You might want to include a redirect URL query parameter
    throw redirect("/sign-in");
  }

  // Fetch data specific to the user
  // const data = await fetchDataForUser(userId);
  const data = { message: `Dashboard data for user ${userId}` };

  return { userId, data }; // Return data including userId
};

export default function Dashboard() {
  const { userId, data } = useLoaderData<typeof loader>();

  return (
    <div>
      <h1>Dashboard</h1>
      <p>Welcome, User {userId}!</p>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}
```

## 2. Express Protection (Middleware)

*   **Framework:** Express
*   **SDK:** `@clerk/backend`
*   **Mechanism:**
    *   Use `ClerkExpressRequireAuth()` or `ClerkExpressWithAuth()` middleware from `@clerk/clerk-express`.
    *   `ClerkExpressRequireAuth()`: Protects routes, automatically returning a 401 error if the user is not authenticated. Access auth state via `req.auth`.
    *   `ClerkExpressWithAuth()`: Attaches auth state to `req.auth` but *does not* automatically block unauthenticated requests (allows optional authentication).

```javascript
// server.js (Express Example)
import express from 'express';
import { ClerkExpressRequireAuth, ClerkExpressWithAuth } from '@clerk/clerk-express';

const app = express();
const PORT = process.env.PORT || 3001;

// --- Protecting Specific Routes ---
// This route requires authentication
app.get(
  '/api/protected',
  ClerkExpressRequireAuth({
    // options like authorizedParties, jwtKey, etc. can be passed
  }),
  (req, res) => {
    // If middleware passes, req.auth is populated
    const { userId, sessionId } = req.auth;
    console.log('Protected route accessed by user:', userId);
    // Fetch data for user userId...
    res.json({ data: `Sensitive data for ${userId}` });
  }
);

// This route makes auth state available but doesn't require sign-in
app.get(
  '/api/public-or-private',
  ClerkExpressWithAuth(),
  (req, res) => {
    const { userId } = req.auth;
    if (userId) {
      res.json({ message: `Hello user ${userId}` });
    } else {
      res.json({ message: 'Hello anonymous user' });
    }
  }
);

// --- Protecting All Routes (Example) ---
// app.use(ClerkExpressRequireAuth()); // Apply middleware globally
// app.get('/dashboard', (req, res) => { /* ... */ }); // Now protected

app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});
```

## 3. Other Node.js Frameworks (Fastify, Koa, Hono, etc.)

*   **SDK:** `@clerk/backend`
*   **Mechanism:** Use the core `authenticateRequest` function from `@clerk/backend` within your framework's middleware or route handler context.
    *   Pass the `request` object, `secretKey`, `publishableKey`, and other options.
    *   It returns the authentication state (`userId`, `sessionId`, etc.) or throws an error if authentication fails.
    *   Handle the success/error cases according to your framework's conventions (e.g., calling `next()`, returning responses).

```javascript
// Generic Node.js Example (Conceptual)
import { authenticateRequest } from '@clerk/backend';

async function myMiddlewareOrHandler(request, response, next) { // Framework-specific signature
  try {
    const requestState = await authenticateRequest({
      request, // The incoming request object (e.g., Node http.IncomingMessage, Fetch API Request)
      secretKey: process.env.CLERK_SECRET_KEY,
      publishableKey: process.env.CLERK_PUBLISHABLE_KEY,
      // Other options...
    });

    if (requestState.status === 'signed-in') {
      // Attach auth state to request context for later use
      request.auth = requestState.toAuth();
      return next ? next() : /* handle success */;
    } else {
      // Handle signed-out state
      return response.status(401).send('Unauthorized'); // Or redirect
    }
  } catch (error) {
    console.error('Clerk Auth Error:', error);
    // Handle errors (e.g., invalid token)
    return response.status(401).send('Authentication Error');
  }
}
```

Always refer to the specific Clerk documentation for your chosen framework (Remix, Express, Fastify, etc.) for the most accurate and up-to-date integration patterns and helper functions. The core principle remains validating the request's authentication state on the server before granting access or returning data.

*(Refer to the official Clerk documentation for Backend SDKs and specific framework guides.)*