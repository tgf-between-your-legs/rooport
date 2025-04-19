# Next.js: Rendering Strategies (App Router)

Understanding different ways Next.js renders pages: SSG, SSR, ISR, Streaming, PPR.

## Core Concept: Server-Centric Rendering

The Next.js App Router primarily renders on the server, offering various strategies to balance static performance with dynamic content needs.

**Key Strategies:**

1.  **Static Site Generation (SSG - Default for Static Routes):**
    *   **How it works:** Renders pages to HTML at **build time**. Fetched data is also fetched at build time.
    *   **When it happens:** Automatically for routes that do *not* use dynamic functions (`cookies()`, `headers()`) or uncached `fetch` requests (`cache: 'no-store'`). Dynamic segments require `generateStaticParams`.
    *   **Pros:** Fastest possible load times (served from CDN), highly cacheable, good for SEO.
    *   **Cons:** Requires a rebuild to update content. Not suitable for personalized or frequently changing data.
2.  **Server-Side Rendering (SSR - Dynamic Rendering):**
    *   **How it works:** Renders pages on the server **at request time**. Data is fetched fresh for each request.
    *   **When it happens:** Automatically for routes that *do* use dynamic functions (`cookies()`, `headers()`, `searchParams` prop) or `fetch` with `cache: 'no-store'` or `revalidate: 0`.
    *   **Pros:** Content is always fresh, suitable for personalized data. Good for SEO as HTML is rendered on the server.
    *   **Cons:** Slower Time to First Byte (TTFB) compared to SSG as rendering happens on request. Higher server load.
3.  **Incremental Static Regeneration (ISR):**
    *   **How it works:** A hybrid approach. Pages are initially generated statically (SSG), but Next.js re-renders them in the background after a specified time interval (`revalidate`) if new requests come in. Stale content is served initially, then updated after revalidation.
    *   **How to enable:** Use the `revalidate` option in `fetch` calls (`fetch(url, { next: { revalidate: seconds } })`) or export `export const revalidate = seconds;` from a page or layout.
    *   **Pros:** Combines the speed of static generation with periodic content updates without requiring a full rebuild. Reduces server load compared to pure SSR.
    *   **Cons:** Content can be slightly stale between revalidation intervals.
4.  **Streaming UI (with React Suspense):**
    *   **How it works:** Allows parts of a server-rendered page (SSR or SSG/ISR) to be sent to the browser progressively *before* all data has loaded on the server.
    *   **How to enable:** Wrap slower Server Components (especially those performing data fetching) in `<Suspense fallback={...}>`.
    *   **Pros:** Improves perceived performance and Time to Interactive (TTI) by showing initial UI (including loading states defined in `loading.tsx` or Suspense fallbacks) quickly while slower data loads in the background.
    *   **Cons:** Requires careful component structuring.
5.  **Partial Prerendering (PPR - Experimental):**
    *   **How it works:** Combines SSG and Streaming. Renders a static "shell" of the page at build time (like SSG), but defers rendering dynamic parts (wrapped in `<Suspense>`) until request time (like SSR/Streaming).
    *   **How to enable:** `experimental: { ppr: true }` in `next.config.js`. Routes default to PPR unless they use dynamic functions or opt-out fetch caching.
    *   **Pros:** Aims for the fast initial load of SSG with the dynamic capabilities of SSR/Streaming for specific parts of the page.
    *   **Cons:** Still experimental, API and behavior might change.

## Choosing a Strategy

*   **Static Content (Blog posts, marketing pages, docs):** Default to **SSG**. Use `generateStaticParams` for dynamic routes.
*   **Personalized Content / Highly Dynamic Data (Dashboards, user profiles):** Use **SSR** (by using dynamic functions or `cache: 'no-store'`). Combine with **Streaming UI** (`Suspense`) for better perceived performance.
*   **Content needing periodic updates (e-commerce product lists):** Use **ISR** (`revalidate` option). Combine with **Streaming UI**.
*   **Mixed Content (Static shell with dynamic sections):** Explore **PPR** (experimental) or structure carefully with **SSR + Streaming UI**.

## Example: Combining Strategies

```typescript
// app/products/[id]/page.tsx

import { Suspense } from 'react';
import ProductDetails from '@/components/ProductDetails';
import ProductRecommendations from '@/components/ProductRecommendations'; // Fetches personalized recommendations
import LoadingSpinner from '@/components/LoadingSpinner';

// Fetch main product data - revalidate every hour (ISR)
async function getProduct(id: string) {
  const res = await fetch(`https://api.example.com/products/${id}`, {
    next: { revalidate: 3600 }
  });
  if (!res.ok) return null; // Handle not found
  return res.json();
}

// This function makes the route dynamic (SSR) because it uses cookies()
// We'll wrap its component in Suspense
async function getRecommendations(productId: string, userId?: string) {
  // const userCookie = cookies().get('user-prefs')?.value; // Example dynamic function use
  const res = await fetch(`https://api.example.com/recommendations?productId=${productId}&userId=${userId || ''}`, {
     cache: 'no-store' // Ensure recommendations are fresh
  });
  if (!res.ok) return [];
  return res.json();
}

// Generate static paths for known products at build time
export async function generateStaticParams() {
  // const products = await fetchAllProductIds();
  return [{ id: '1' }, { id: '2' }];
}

// Revalidate the whole page at most every 60 seconds (ISR)
// This applies to the static shell generated by generateStaticParams
// Individual fetch calls can have shorter revalidate times.
export const revalidate = 60;

export default async function ProductPage({ params }: { params: { id: string } }) {
  const product = await getProduct(params.id);

  if (!product) {
    notFound(); // Use Next.js notFound helper
  }

  // Recommendations will be fetched dynamically on request
  const recommendationsPromise = getRecommendations(params.id /*, userId from auth() */);

  return (
    <div>
      {/* Product details rendered using ISR data */}
      <ProductDetails product={product} />

      <hr />
      <h2>Recommended Products</h2>
      {/* Recommendations stream in, fallback shown initially */}
      <Suspense fallback={<LoadingSpinner />}>
        {/* @ts-expect-error Async Server Component */}
        <ProductRecommendations recommendationsPromise={recommendationsPromise} />
      </Suspense>
    </div>
  );
}

// components/ProductRecommendations.tsx
async function ProductRecommendations({ recommendationsPromise }) {
  const recommendations = await recommendationsPromise;
  // ... render recommendations ...
}
```

Next.js offers a flexible rendering model. Choose the strategy (or combination) that best fits the data requirements and performance goals for each page or component. Leverage Server Components and Suspense for optimal results.

*(Refer to the official Next.js documentation on Rendering.)*