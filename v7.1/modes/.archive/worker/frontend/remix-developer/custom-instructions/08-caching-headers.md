# Caching (`headers` Export)

## Core Concept: HTTP Caching Headers

Remix allows controlling browser and CDN caching for specific routes by exporting a `headers` function from the route module. This function sets standard HTTP caching headers like `Cache-Control`.

**How it Works:**

*   **`headers` Function:** Export a function named `headers`.
*   **Execution:** Runs on the server after `loader` and `action` (if applicable) run successfully.
*   **Signature:** `export function headers({ loaderHeaders, parentHeaders, actionHeaders }) { ... }`
    *   Receives `Headers` objects from loader, parent routes, and action.
*   **Return Value:** **Must return a `Headers` object** (or plain object). These merge with/override headers from loader/action/parents.
*   **Primary Use:** Setting `Cache-Control`.

## Common `Cache-Control` Directives

*   `public`: Allows CDN caching.
*   `private`: Allows browser caching only.
*   `max-age=<seconds>`: Max freshness time (browser).
*   `s-maxage=<seconds>`: Max freshness time for shared caches (CDNs). Overrides `max-age` for CDNs.
*   `no-cache`: Requires revalidation before serving cached response.
*   `no-store`: Disallows caching entirely.
*   `must-revalidate`: Must revalidate stale responses.
*   `stale-while-revalidate=<seconds>`: Serve stale while revalidating in background.
*   `stale-if-error=<seconds>`: Serve stale if origin errors during revalidation.

## Implementation Examples

**1. Caching Public Content (e.g., Blog Post):**

```typescript
// app/routes/posts.$postId.tsx
import type { HeadersFunction } from "@remix-run/node";

export const headers: HeadersFunction = ({ loaderHeaders }) => {
  return {
    "Cache-Control": "public, max-age=60, s-maxage=3600, stale-while-revalidate=300",
    // Browser: 60s, CDN: 1hr, Stale-while-revalidate: 5min
  };
};
```

**2. Caching Private User Data (e.g., Dashboard):**

```typescript
// app/routes/dashboard.tsx
import type { HeadersFunction } from "@remix-run/node";

export const headers: HeadersFunction = () => {
  return { "Cache-Control": "private, max-age=300" }; // Browser cache 5 mins
  // Or: return { "Cache-Control": "private, no-cache" }; // Must revalidate
};
```

**3. Never Cache Sensitive Data:**

```typescript
// app/routes/admin.sensitive-data.tsx
import type { HeadersFunction } from "@remix-run/node";

export const headers: HeadersFunction = () => {
  return { "Cache-Control": "no-store" };
};
```

**4. Merging Headers:**

```typescript
// app/routes/some-route.tsx
import type { HeadersFunction } from "@remix-run/node";

export const headers: HeadersFunction = ({ loaderHeaders, parentHeaders }) => {
  const newHeaders = new Headers(loaderHeaders); // Start with loader headers
  newHeaders.set("X-Custom-Route-Header", "value");
  if (!newHeaders.has("Cache-Control")) {
      newHeaders.set("Cache-Control", "public, max-age=60"); // Default
  }
  return newHeaders;
};
```

The `headers` export provides fine-grained control over HTTP caching per route.

*(Combined from `caching-headers.md` and `remix-caching-headers.md`)*