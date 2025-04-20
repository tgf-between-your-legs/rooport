# Clerk: Session Management & JWT Templates

Understanding how Clerk manages sessions and using JWT templates.

## Core Concept: Sessions & Tokens

Clerk handles user session management automatically across your frontend and backend.

*   **Session Cookie:** After successful sign-in, Clerk sets a secure, HTTP-only cookie (`__session`) in the user's browser. This cookie contains an encrypted short-lived session token.
*   **Frontend SDK:** The Clerk frontend SDK (`@clerk/nextjs`, `@clerk/clerk-react`, etc.) uses the publishable key and interacts with Clerk's Frontend API to manage the active user and session state within the browser context (accessible via hooks like `useAuth`, `useSession`, `useUser`). It periodically refreshes the session token in the background.
*   **Backend SDK / Middleware:** On the server-side (API routes, middleware, server components, loaders), Clerk's backend SDKs or middleware intercept incoming requests. They read the `__session` cookie (or an `Authorization: Bearer` token), verify the session token against Clerk's Backend API using your **secret key**, and populate the authentication context (`req.auth`, `auth()`, `getAuth()`).
*   **Session Token (JWT):** The token within the cookie (and obtainable via `getToken()`) is a JSON Web Token (JWT) signed by Clerk. Your backend verifies this token's signature and claims to confirm the user's identity and session validity.

## Accessing Session State

*   **Frontend (Hooks):**
    *   `useAuth()`: Provides `sessionId`, `isSignedIn`, `isLoaded`.
    *   `useSession()`: Provides the detailed `session` object (`id`, `status`, `lastActiveAt`, `expireAt`, `user`, etc.) and `isLoaded`, `isSignedIn`.
*   **Backend (Helpers/Middleware):**
    *   `auth()` (Next.js App Router): Returns `sessionId`, `userId`, etc.
    *   `getAuth(req)` (Next.js Pages Router): Returns `sessionId`, `userId`, etc.
    *   `req.auth` (Express Middleware): Contains `sessionId`, `userId`, etc.
    *   `authenticateRequest()` (Core Backend SDK): Returns state including `sessionId`, `userId`.

## Session Lifetime & Configuration

*   Session duration and inactivity timeouts are configured within your Clerk Dashboard under **Sessions**.
*   Clerk's frontend SDK automatically handles refreshing session tokens in the background as long as the user is active.

## JWT Templates & Custom Claims

*   **Purpose:** You can configure Clerk to include custom data (claims) within the JWT session token generated for your application. This is useful for passing frequently needed, relatively static user information (like roles, permissions, subscription levels) directly to your backend without needing extra database lookups on every request.
*   **Configuration:** Create a JWT Template in your Clerk Dashboard (**JWT Templates** section).
    *   Choose a signing algorithm (RS256 recommended).
    *   Define custom claims using short keys (e.g., `rls` for roles, `perm` for permissions).
    *   Map claims to user metadata (public or private) stored in Clerk using template variables (e.g., `{{user.public_metadata.role}}`).
*   **Accessing Custom Claims:**
    *   **Backend:** Once the session token is verified by Clerk middleware/helpers, custom claims are typically available on the `sessionClaims` property of the `auth` object.
        ```typescript
        // Example: Next.js App Router API Route
        import { auth } from '@clerk/nextjs/server';
        import { NextResponse } from 'next/server';

        export async function GET() {
          const { userId, sessionClaims } = auth();

          if (!userId) {
            return new NextResponse("Unauthorized", { status: 401 });
          }

          // Access custom claims from JWT template
          const role = sessionClaims?.metadata?.role; // Matches {{user.public_metadata.role}}
          const permissions = sessionClaims?.metadata?.permissions; // Matches {{user.public_metadata.permissions}}

          console.log('User Role:', role);

          if (role !== 'admin') {
             return new NextResponse("Forbidden", { status: 403 });
          }

          // Proceed with admin-only logic...
          return NextResponse.json({ message: 'Admin data' });
        }
        ```
    *   **Frontend (`getToken({ template: '...' })`):** You can request a token based on a specific JWT template from the frontend, but this is less common than accessing claims on the backend. The standard `getToken()` returns Clerk's default session token format.

**Considerations for JWT Templates:**

*   **Statelessness:** JWTs are stateless. If you change user metadata (like roles) used in a claim, the change will only be reflected in *new* tokens issued after the user's *next* sign-in or session refresh. It doesn't invalidate existing tokens immediately.
*   **Token Size:** Adding many custom claims increases the size of the JWT, which is sent with every authenticated request (usually in a cookie). Keep claim keys short and data concise.
*   **Sensitivity:** Avoid putting highly sensitive or frequently changing data directly into JWT claims. Use claims for relatively stable authorization-related data. Fetch highly sensitive or dynamic data directly from your backend database when needed, using the `userId` from the verified token.

Clerk simplifies session management significantly. Understanding the token flow and leveraging JWT templates for custom claims allows for efficient and secure authorization checks in your backend.

*(Refer to the official Clerk documentation on Sessions, JWTs, and JWT Templates.)*