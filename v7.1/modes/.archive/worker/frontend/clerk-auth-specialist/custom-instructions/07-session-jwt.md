# Custom Instructions: Session Management & JWT Templates

Understanding how Clerk manages sessions and using JWT templates for custom claims.

## Core Concept: Sessions & Tokens

Clerk handles user session management automatically across your frontend and backend.

*   **Session Cookie:** After sign-in, Clerk sets a secure, HTTP-only cookie (`__session`) containing an encrypted short-lived session token.
*   **Frontend SDK:** Manages active user/session state in the browser (via hooks like `useAuth`, `useSession`). Refreshes the token automatically.
*   **Backend SDK / Middleware:** Intercepts requests, reads the cookie/token, verifies it using the **secret key**, and populates the auth context (`req.auth`, `auth()`, `getAuth()`).
*   **Session Token (JWT):** The token is a JSON Web Token signed by Clerk. Your backend verifies its signature and claims.

## Accessing Session State

*   **Frontend (Hooks):**
    *   `useAuth()`: Provides `sessionId`, `isSignedIn`, `isLoaded`.
    *   `useSession()`: Provides the detailed `session` object (`id`, `status`, `lastActiveAt`, etc.).
*   **Backend (Helpers/Middleware):**
    *   `auth()` (Next.js App Router): Returns `sessionId`, `userId`, `sessionClaims`, etc.
    *   `getAuth(req)` (Next.js Pages Router): Returns `sessionId`, `userId`, `sessionClaims`, etc.
    *   `req.auth` (Express Middleware): Contains `sessionId`, `userId`, `sessionClaims`, etc.
    *   `authenticateRequest()` (Core Backend SDK): Returns state including `sessionId`, `userId`, `sessionClaims`.

## Session Lifetime & Configuration

*   Configured within your Clerk Dashboard under **Sessions** (duration, inactivity timeouts).
*   Frontend SDK handles automatic token refresh during user activity.

## JWT Templates & Custom Claims

*   **Purpose:** Include custom data (claims) in the JWT session token (e.g., roles, permissions, subscription IDs) to avoid extra backend lookups.
*   **Configuration:** Create a JWT Template in Clerk Dashboard (**JWT Templates** section).
    *   Define custom claims (short keys recommended, e.g., `rls`, `perm`, `sub`).
    *   Map claims to user metadata using template variables (e.g., `{{user.public_metadata.role}}`, `{{user.private_metadata.subscription_id}}`).
*   **Accessing Custom Claims (Backend):**
    *   Custom claims are typically available on the `sessionClaims` property of the `auth` object after verification.

    ```typescript
    // Example: Next.js App Router API Route
    import { auth } from '@clerk/nextjs/server';
    import { NextResponse } from 'next/server';

    export async function GET() {
      // auth() verifies the token and populates sessionClaims
      const { userId, sessionClaims } = auth();

      if (!userId) {
        return new NextResponse("Unauthorized", { status: 401 });
      }

      // Access custom claims (assuming 'role' was defined in the JWT template)
      // The structure might be sessionClaims.metadata.role or just sessionClaims.role
      // depending on how you configured the template. Check console.log(sessionClaims).
      const role = sessionClaims?.metadata?.role ?? sessionClaims?.role;

      console.log('User Role from JWT:', role);

      if (role !== 'admin') {
         return new NextResponse("Forbidden", { status: 403 });
      }

      // Proceed with admin-only logic...
      return NextResponse.json({ message: 'Admin data' });
    }
    ```

**Considerations for JWT Templates:**
*   **Statelessness:** Changes to user metadata are reflected only in *new* tokens after sign-in/refresh. Existing tokens aren't immediately updated.
*   **Token Size:** Keep claims concise to avoid large cookies/headers.
*   **Sensitivity:** Avoid putting highly sensitive or frequently changing data in claims. Use `userId` to fetch such data from your DB when needed. Use claims for stable authorization data.

Clerk simplifies session management. JWT templates allow efficient passing of authorization data to your backend.

*(Refer to the official Clerk documentation on Sessions, JWTs, and JWT Templates.)*