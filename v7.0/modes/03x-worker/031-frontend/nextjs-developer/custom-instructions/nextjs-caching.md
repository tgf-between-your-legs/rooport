# Next.js: Caching Fundamentals (App Router)

Understanding the different caching layers in the Next.js App Router.

## Core Concept: Multi-Layer Caching

Next.js employs multiple caching layers to optimize performance and reduce the cost of data fetching and rendering. Understanding these layers helps in controlling how fresh your data is and how quickly pages load.

**Primary Caching Layers:**

1.  **Request Memoization (React `cache` / Server Components):**
    *   **Scope:** Single server request during rendering.
    *   **Mechanism:** React's `cache` function (used automatically by `fetch` in Server Components) memoizes identical `fetch` requests *within the same request lifecycle*. If you call `fetch('.../data')` multiple times in different components during a single server render, only one actual network request is made.
    *   **Control:** Automatic for `fetch`. Can manually wrap functions with `React.cache()` for similar behavior with other data sources (e.g., database clients), though direct `fetch` caching is often preferred.
2.  **Data Cache (Persistent across requests):**
    *   **Scope:** Across multiple incoming requests (persistent).
    *   **Mechanism:** Next.js automatically caches the results of `fetch` requests (unless opted out). This cache is persisted on the server (or CDN if configured). Subsequent requests for the same data URL (within the revalidation period) will receive the cached response instead of hitting the origin server.
    *   **Control:**
        *   Default: Caches indefinitely (`cache: 'force-cache'`).
        *   Opt-out: `fetch(url, { cache: 'no-store' })`.
        *   Time-based Revalidation (ISR): `fetch(url, { next: { revalidate: seconds } })`.
        *   On-Demand Revalidation: `revalidatePath(path)` or `revalidateTag(tag)` (used in Server Actions or Route Handlers to invalidate specific caches). Requires tagging fetches: `fetch(url, { next: { tags: ['collection'] } })`.
3.  **Full Route Cache (Server-Side):**
    *   **Scope:** Caches the fully rendered HTML and React Server Component Payload (RSC Payload) for a route.
    *   **Mechanism:** Statically generated routes (SSG) are cached indefinitely at build time. Dynamically rendered routes (SSR) are generally *not* cached by this layer by default, but ISR routes are cached and revalidated.
    *   **Control:** Primarily controlled by whether a route is static or dynamic. Using dynamic functions (`cookies()`, `headers()`) or uncached fetches opts the route into dynamic rendering, bypassing the Full Route Cache for subsequent requests (though individual `fetch` calls might still be cached by the Data Cache). `revalidatePath`/`revalidateTag` invalidates this cache for affected routes.
4.  **Router Cache (Client-Side):**
    *   **Scope:** In-memory cache within the user's browser session.
    *   **Mechanism:** Stores the RSC Payload for previously visited route segments. When navigating back/forward or clicking a `<Link>`, Next.js first checks this client-side cache. If available and not stale, it avoids making a new request to the server, enabling instant navigation.
    *   **Control:** Largely automatic. `router.refresh()` clears the Router Cache and triggers a new server request. `revalidatePath`/`revalidateTag` on the server invalidates relevant parts of the client-side Router Cache on the *next* navigation to that path. Cache duration is session-based or time-limited (e.g., 5 minutes for dynamic segments).

## How Layers Interact

1.  User navigates to `/products/1`.
2.  **Router Cache (Client):** Checked first. If valid payload exists, render instantly. If not...
3.  Request goes to **Next.js Server**.
4.  **Full Route Cache (Server):** Checked. If valid HTML/RSC Payload exists (e.g., from previous ISR), serve it. If not...
5.  **Render Route (Server):**
    *   Server Components execute.
    *   `fetch('/api/products/1')` is called.
    *   **Request Memoization (Server):** If this exact fetch happened earlier *in this same render*, return memoized result. If not...
    *   **Data Cache (Server):** Checked. If valid cached data for `/api/products/1` exists (within `revalidate` time), return it. If not...
    *   **Actual Fetch:** Request goes to `api.example.com`. Response received.
    *   **Data Cache (Server):** Response stored in Data Cache (with revalidation rules).
    *   **Request Memoization (Server):** Response stored for this render pass.
    *   Data returned to Server Component.
    *   Component finishes rendering.
6.  **Full Route Cache (Server):** Rendered HTML/RSC Payload stored if applicable (ISR/SSG).
7.  **Response Sent to Client.**
8.  **Router Cache (Client):** Received RSC Payload stored in client memory.
9.  Page hydrates/renders.

## Cache Invalidation

*   **Time-based (ISR):** Set `revalidate` in `fetch` or page config. Cache becomes stale after the specified time.
*   **On-Demand:** Use `revalidatePath(path)` or `revalidateTag(tag)` in Server Actions or Route Handlers to manually invalidate specific data or page caches immediately. Requires tagging `fetch` requests for `revalidateTag`.

```typescript
// app/actions.ts
'use server';
import { revalidateTag, revalidatePath } from 'next/cache';
// import { updateProduct } from '@/lib/db';

export async function updateProductAction(productId: string, data: any) {
  try {
    // await updateProduct(productId, data);
    revalidateTag(`product-${productId}`); // Invalidate fetches tagged with this
    revalidatePath('/products'); // Invalidate the product listing page
    revalidatePath(`/products/${productId}`); // Invalidate the specific product page
    return { success: true };
  } catch (e) {
    return { success: false, message: 'Update failed' };
  }
}

// Fetching data with a tag
// await fetch(`https://.../products/${id}`, { next: { tags: [`product-${id}`] } });
```

Understanding these caching layers and how to control them (especially `cache: 'no-store'`, `revalidate`, `revalidatePath`, `revalidateTag`) is crucial for balancing performance and data freshness in Next.js applications.

*(Refer to the official Next.js documentation on Caching.)*