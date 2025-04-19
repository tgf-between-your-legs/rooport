# Next.js Performance & Caching (App Router)

Optimizing Next.js App Router applications for speed and efficiency.

## 1. Server Components & Zero JS by Default

*   **Core Idea:** Server Components render on the server, sending only non-interactive HTML to the client initially. This drastically reduces the client-side JavaScript bundle size compared to traditional SPAs.
*   **Best Practice:** Build with Server Components first. Only opt into Client Components (`'use client'`) when interactivity (state, effects, event listeners) or browser APIs are required. Keep Client Components small and push them down the tree.

## 2. Data Fetch Caching (`fetch`)

*   **Automatic Caching:** Next.js extends `fetch` to automatically cache requests (`force-cache`). Identical GET requests with the same URL and options are deduplicated during a render pass. Statically rendered routes cache fetch results at build time. Dynamically rendered routes cache results per-request unless configured otherwise.
*   **Disabling Cache:** Use `cache: 'no-store'` for data that must be fresh on every request (dynamic rendering).
    ```javascript
    fetch('https://api.example.com/live-data', { cache: 'no-store' });
    // Alternatively, use segment-level dynamic rendering via export const dynamic = 'force-dynamic';
    ```
*   **Time-based Revalidation (ISR):** Use `next: { revalidate: seconds }` to cache data for a specific duration.
    ```javascript
    fetch('https://api.example.com/products', { next: { revalidate: 3600 } }); // Cache for 1 hour
    // Alternatively, use segment-level ISR via export const revalidate = 3600;
    ```
*   **Tag-based Revalidation:** Assign tags to fetch requests and revalidate them on-demand using `revalidateTag` (typically in Server Actions or Route Handlers).
    ```javascript
    // Fetching data with tags
    fetch('https://api.example.com/items', { next: { tags: ['collection', 'items'] } });

    // In a Server Action after mutation
    import { revalidateTag } from 'next/cache';
    // ... perform update ...
    revalidateTag('collection'); // Example: Revalidate fetches tagged with 'collection'
    ```

## 3. Full Route Cache

*   **Concept:** Next.js caches the rendered result (React Server Component Payload + HTML) of routes during static builds or ISR.
*   **Behavior:** Statically rendered routes are cached indefinitely (until next build). Dynamically rendered routes are not cached by default. ISR routes are cached for the specified `revalidate` duration.
*   **Opting Out (Dynamic Rendering):** Using dynamic functions (`cookies()`, `headers()`, `searchParams`) or uncached fetches (`cache: 'no-store'`, `revalidate: 0`) opts the entire route segment into dynamic rendering, bypassing the Full Route Cache.
*   **Segment Config:** Control caching and rendering behavior per segment using exported variables in `layout.tsx` or `page.tsx`:
    ```javascript
    export const dynamic = 'force-dynamic'; // Force dynamic rendering (SSR)
    // export const dynamic = 'force-static'; // Force static rendering (SSG)
    // export const dynamic = 'error'; // Error if dynamic functions/fetches used
    export const revalidate = 60; // Force ISR for this segment (revalidate every 60s)
    ```

## 4. Streaming UI (`React.Suspense`)

*   **Concept:** Improves perceived performance by sending the static parts of the page first, then streaming in dynamic content as data becomes available on the server.
*   **Implementation:** Wrap components that fetch data or render slowly in `<Suspense fallback={...}>`. Use `loading.tsx` for automatic Suspense boundaries tied to route segments.
*   **Benefit:** Faster TTFB and FCP, better user experience on slower connections or with slow data sources.

## 5. Image Optimization (`next/image`)

*   **Component:** Always use the built-in `<Image>` component from `next/image` instead of the standard `<img>` tag.
*   **Benefits:** Automatic resizing/optimization, modern formats, prevents layout shift (requires `width`/`height`), lazy loading by default.
*   **Usage:**
    ```jsx
    import Image from 'next/image';
    import profilePic from '../public/me.png'; // Import local image

    <Image
      src={profilePic} // Local image import or remote URL string
      alt="Picture of the author"
      width={500} // Required for non-fill images
      height={500} // Required for non-fill images
      // priority // Add for LCP images (e.g., hero image) to preload
      // quality={75} // Optional quality setting
      // fill // Optional: Makes image fill parent container (requires position relative/absolute on parent)
      // sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw" // Optional: For responsive sizing with fill
    />
    ```

## 6. Bundle Analysis

*   Use `@next/bundle-analyzer` to visualize the JavaScript bundles generated for your application and identify large dependencies or potential optimization opportunities.

*(Refer to the official Next.js documentation on Data Fetching, Caching, Rendering, and Optimization.)*