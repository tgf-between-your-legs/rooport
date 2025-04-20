# App Router: Middleware

Intercepting requests and modifying responses using Next.js Middleware.

## Core Concept: Middleware

Middleware allows running code **before** a request completes. Based on the incoming `NextRequest`, you can modify the response by rewriting, redirecting, adding headers, or responding directly. It runs on the server (Edge Runtime by default) before caching and routing.

**Key Use Cases:**

*   **Authentication/Authorization:** Check user sessions, redirect unauthenticated users. Often integrated with auth providers (e.g., Clerk).
*   **Redirects/Rewrites:** Handle legacy URLs, A/B testing, routing based on geolocation/preferences.
*   **Header Modification:** Add security headers (CSP, CORS), custom request/response headers.
*   **Bot Detection:** Identify and block bots.
*   **Geolocation / i18n:** Redirect based on location or language.

## Implementation

1.  **Create `middleware.ts` (or `.js`):** Place in the project root (or `src/`).
2.  **Export `middleware` Function:** Default export receiving `NextRequest`.
3.  **Logic:** Inspect `request` (URL, headers, cookies, geolocation).
4.  **Return `NextResponse`:**
    *   `NextResponse.next()`: Continue processing (can add headers before returning).
    *   `NextResponse.redirect(url)`: Redirect user.
    *   `NextResponse.rewrite(url)`: Serve different content without changing URL.
    *   Return standard `Response` directly (e.g., `new Response('Unauthorized', { status: 401 })`) to end request.

```typescript
// middleware.ts (in project root or src/)
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';
// import { clerkMiddleware } from '@clerk/nextjs/server'; // Example: Auth provider

// Example: Basic Auth Check (Manual)
export function middleware(request: NextRequest) {
  const sessionToken = request.cookies.get('session-token')?.value;
  const pathname = request.nextUrl.pathname;

  // Protect dashboard route
  if (pathname.startsWith('/dashboard')) {
    if (!sessionToken /* || !isValidSession(sessionToken) */) {
      const loginUrl = new URL('/login', request.url);
      loginUrl.searchParams.set('redirect_url', pathname);
      return NextResponse.redirect(loginUrl);
    }
  }

  // Add a custom header to all allowed requests
  const response = NextResponse.next();
  response.headers.set('x-middleware-processed', 'true');
  return response;
}

// --- Matcher Configuration ---
// Define paths for middleware execution (more efficient than checking path inside)
export const config = {
  matcher: [
    /*
     * Match all request paths except for the ones starting with:
     * - api (API routes)
     * - _next/static (static files)
     * - _next/image (image optimization files)
     * - favicon.ico (favicon file)
     * - Anything with a file extension (e.g., .png)
     */
    '/((?!api|_next/static|_next/image|favicon.ico|.*\\.).*)',
    // Optional: Include specific protected routes if needed
    // '/dashboard/:path*',
  ],
};
```

## `matcher` Config

*   Exported `config` object alongside `middleware` function.
*   `matcher` array defines path patterns (wildcards/regex-like) for middleware execution.
*   Crucial for excluding static assets and API routes (unless needed) for performance.

## Runtime

*   **Edge Runtime (Default):** Lightweight V8 environment, fast execution, no native Node.js APIs (`fs`, etc.). Preferred for performance.
*   **Node.js Runtime:** Can opt-in if needed (`export const runtime = 'nodejs';` in middleware file), but less common.

*(Refer to the official Next.js documentation on Middleware.)*