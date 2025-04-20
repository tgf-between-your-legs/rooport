# Remix: Caching with the `headers` Export

Controlling HTTP caching behavior for Remix routes using the `headers` function.

## Core Concept: HTTP Caching Headers

Remix allows you to control browser and CDN caching behavior for specific routes by exporting a `headers` function from the route module. This function lets you set standard HTTP caching headers like `Cache-Control`.

**How it Works:**

*   **`headers` Function:** Export a function named `headers` from your route module.
*   **Execution:** Runs on the server after your `loader` and `action` (if applicable) have run successfully.
*   **Signature:** `export function headers({ loaderHeaders, parentHeaders, actionHeaders }) { ... }`
    *   Receives `Headers` objects containing the headers set by the loader, parent routes' `headers` functions, and the action (if one ran).
*   **Return Value:** **Must return a `Headers` object** (or a plain object literal which Remix converts to Headers). These headers will be merged with and potentially override headers set by the loader/action/parents.
*   **Primary Use:** Setting the `Cache-Control` header to define caching duration and behavior for browsers and CDNs.

## Common `Cache-Control` Directives

*   `public`: Allows caching by intermediate proxies and CDNs.
*   `private`: Allows caching only by the end user's browser.
*   `max-age=<seconds>`: Maximum time the response can be considered fresh.
*   `s-maxage=<seconds>`: Maximum time for shared caches (CDNs) (overrides `max-age` for shared caches).
*   `no-cache`: Requires caches to revalidate with the origin server before serving a cached response (checks `ETag`/`Last-Modified`). Does *not* mean "do not store".
*   `no-store`: Disallows caching entirely. The response should not be stored by any cache.
*   `must-revalidate`: Tells caches they must revalidate stale responses and not serve them.
*   `stale-while-revalidate=<seconds>`: Allows serving a stale response while revalidating in the background.
*   `stale-if-error=<seconds>`: Allows serving a stale response if the origin server errors during revalidation.

## Implementation Examples

**1. Caching Public Content (e.g., Blog Post):**

Cache aggressively on CDNs (`s-maxage`) and allow browser caching (`max-age`). Revalidate periodically.

```typescript
// app/routes/posts.$postId.tsx
import type { HeadersFunction } from "@remix-run/node"; // or adapter

// ... loader ...

export const headers: HeadersFunction = ({ loaderHeaders }) => {
  // Inherit loader headers, but set specific Cache-Control
  return {
    "Cache-Control": "public, max-age=60, s-maxage=3600, stale-while-revalidate=300",
    // Cache in browser for 60s
    // Cache in CDN for 1 hour (3600s)
    // Allow serving stale for 5 mins (300s) while revalidating
  };
};

// ... Component, ErrorBoundary ...
```

**2. Caching Private User Data (e.g., Dashboard):**

Prevent caching by shared CDNs, allow browser caching for a short period or require revalidation.

```typescript
// app/routes/dashboard.tsx
import type { HeadersFunction } from "@remix-run/node";

// ... loader (fetches user-specific data) ...

export const headers: HeadersFunction = () => {
  return {
    // Option 1: No shared cache, browser must revalidate
    // "Cache-Control": "private, no-cache",

    // Option 2: No shared cache, browser cache for 5 mins
    "Cache-Control": "private, max-age=300",
  };
};

// ... Component, Outlet, ErrorBoundary ...
```

**3. Never Cache Sensitive Data:**

Use `no-store` for highly sensitive information that should never be cached anywhere.

```typescript
// app/routes/admin.sensitive-data.tsx
import type { HeadersFunction } from "@remix-run/node";

// ... loader ...

export const headers: HeadersFunction = () => {
  return {
    "Cache-Control": "no-store", // Do not cache anywhere
  };
};

// ... Component ...
```

**4. Merging Headers:**

You can inspect headers set by the loader or parent routes and merge them.

```typescript
// app/routes/some-route.tsx
import type { HeadersFunction } from "@remix-run/node";

// ... loader (might set its own Cache-Control or other headers) ...

export const headers: HeadersFunction = ({ loaderHeaders, parentHeaders }) => {
  const newHeaders = new Headers(loaderHeaders); // Start with loader headers
  // Add or override specific headers
  newHeaders.set("X-Custom-Route-Header", "value");
  if (!newHeaders.has("Cache-Control")) {
      newHeaders.set("Cache-Control", "public, max-age=60"); // Default if loader didn't set one
  }
  // You could also inspect parentHeaders if needed
  return newHeaders;
};

// ... Component ...
```

The `headers` export provides fine-grained control over HTTP caching for each route, allowing you to optimize delivery performance based on how frequently the content changes and whether it's public or private.

*(Refer to the official Remix documentation on `headers` export and HTTP Caching.)*