# Next.js: Middleware

Intercepting requests and modifying responses using Next.js Middleware.

## Core Concept: Middleware

Middleware allows you to run code **before** a request is completed. Based on the incoming request, you can modify the response by rewriting, redirecting, adding headers, or streaming content. It runs on the server (specifically, the Edge Runtime by default) before caching and route matching occur.

**Key Use Cases:**

*   **Authentication & Authorization:** Checking if a user is logged in and redirecting or blocking access. (Often integrated with auth providers like Clerk via their middleware).
*   **Redirects & Rewrites:** Handling legacy URLs, A/B testing, or routing based on user location/preferences.
*   **Header Modification:** Adding security headers, CORS headers, or custom request/response headers.
*   **Bot Detection:** Identifying and potentially blocking bot traffic.
*   **Geolocation / Internationalization (i18n):** Redirecting users based on their location or language preferences.

## Implementation

1.  **Create `middleware.ts` (or `.js`):** Place this file in the root directory of your project (or inside `src/` if using `src/` directory).
2.  **Export Middleware Function:** Export a default function named `middleware`. This function receives the `NextRequest` object.
3.  **Logic:** Inside the function, inspect the `request` object (URL, headers, cookies, geolocation).
4.  **Return Response:** Based on the logic, return a `NextResponse` object to modify the flow:
    *   `NextResponse.next()`: Continue processing the request as normal (passes to cache or route handler/page). You can add headers to this response *before* returning it.
    *   `NextResponse.redirect(url)`: Redirect the user to a different URL.
    *   `NextResponse.rewrite(url)`: Serve content from a different URL *without* changing the visible URL in the browser.
    *   Return a standard `Response` object directly (e.g., `new Response('Unauthorized', { status: 401 })`) to end the request immediately.

```typescript
// middleware.ts (in project root or src/)
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

// Optional: Import auth middleware if using Clerk, Auth.js, etc.
// import { clerkMiddleware, createRouteMatcher } from '@clerk/nextjs/server';

// Example 1: Basic Logging & Header Modification
// export function middleware(request: NextRequest) {
//   console.log(`Middleware: Processing ${request.method} ${request.nextUrl.pathname}`);
//
//   // Clone the request headers and set a new header
//   const requestHeaders = new Headers(request.headers);
//   requestHeaders.set('x-custom-header', 'hello from middleware');
//
//   // Continue to the next middleware or route, passing the modified headers
//   const response = NextResponse.next({
//     request: {
//       // New request headers
//       headers: requestHeaders,
//     },
//   });
//
//   // Add a custom header to the response
//   response.headers.set('x-middleware-ran', 'true');
//
//   return response;
// }

// Example 2: Redirecting based on path
// export function middleware(request: NextRequest) {
//   if (request.nextUrl.pathname === '/legacy-path') {
//     const newUrl = new URL('/new-path', request.url); // Construct absolute URL
//     return NextResponse.redirect(newUrl);
//   }
//   return NextResponse.next(); // Continue if no redirect needed
// }

// Example 3: Using Clerk Middleware (Recommended for Auth)
// See clerk-route-protection-nextjs.md for details
// export default clerkMiddleware((auth, req) => {
//   // ... protection logic ...
// });

// Example 4: Basic Auth Check (Manual - Less common than using provider middleware)
export function middleware(request: NextRequest) {
  const sessionToken = request.cookies.get('session-token')?.value;
  const pathname = request.nextUrl.pathname;

  // Assume /dashboard requires login
  if (pathname.startsWith('/dashboard')) {
    if (!sessionToken /* || !isValidSession(sessionToken) */) {
      // Redirect to login if no valid session
      const loginUrl = new URL('/login', request.url);
      loginUrl.searchParams.set('redirect_url', pathname); // Pass redirect URL
      return NextResponse.redirect(loginUrl);
    }
  }

  // Allow request to proceed
  return NextResponse.next();
}


// --- Matcher Configuration ---
// Define which paths the middleware should run on.
export const config = {
  matcher: [
    /*
     * Match all request paths except for the ones starting with:
     * - api (API routes)
     * - _next/static (static files)
     * - _next/image (image optimization files)
     * - favicon.ico (favicon file)
     * - Anything with a file extension (e.g., .png, .jpg)
     */
    '/((?!api|_next/static|_next/image|favicon.ico|.*\\.).*)',
    // Optional: Include specific API routes if needed
    // '/api/protected/:path*',
  ],
};
```

## `matcher` Config

*   The `config` object exported alongside the `middleware` function defines which paths the middleware applies to.
*   Use `matcher` with an array of path patterns (supports wildcards and regex-like syntax).
*   This is more efficient than running the middleware on *every* request and checking the path inside the function, especially for excluding static assets.

## Runtime

*   Middleware runs on the **Edge Runtime** by default, which is a lightweight V8-based environment with limitations (no native Node.js APIs like `fs`).
*   You can explicitly opt into the Node.js runtime if needed, but Edge is generally preferred for performance.

Middleware provides a powerful way to intercept requests globally or for specific paths, enabling features like authentication, redirects, and header manipulation before your pages or API routes are processed.

*(Refer to the official Next.js documentation on Middleware.)*