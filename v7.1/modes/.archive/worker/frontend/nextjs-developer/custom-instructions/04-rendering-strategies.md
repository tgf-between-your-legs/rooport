# App Router: Rendering Strategies

Understanding different ways Next.js renders pages: SSG, SSR, ISR, Streaming, PPR.

## Core Concept: Server-Centric Rendering

The Next.js App Router primarily renders on the server, offering various strategies to balance static performance with dynamic content needs.

**Key Strategies:**

1.  **Static Rendering (Default - SSG):**
    *   **How:** Renders pages to HTML at **build time**. Data fetched at build time.
    *   **When:** Default for routes without dynamic functions (`cookies()`, `headers()`, `searchParams`) or uncached `fetch`. Dynamic segments need `generateStaticParams`.
    *   **Pros:** Fastest load times (CDN), cacheable, SEO-friendly.
    *   **Cons:** Requires rebuild for updates. Not for personalized/dynamic data.
    *   **Use Case:** Marketing pages, blogs, docs.

2.  **Dynamic Rendering (SSR):**
    *   **How:** Renders pages on the server **at request time**. Data fetched fresh.
    *   **When:** Opt-in via dynamic functions or uncached `fetch` (`cache: 'no-store'`, `revalidate: 0`). Can force with `export const dynamic = 'force-dynamic';`.
    *   **Pros:** Always fresh content, personalized data possible, SEO-friendly.
    *   **Cons:** Slower TTFB than SSG, higher server load.
    *   **Use Case:** Dashboards, user profiles, frequently changing data.

3.  **Incremental Static Regeneration (ISR):**
    *   **How:** Hybrid. Initial static build, then re-renders in background after `revalidate` interval on new requests. Serves stale initially, then updates.
    *   **How to enable:** Use `next: { revalidate: seconds }` in `fetch` or `export const revalidate = seconds;` in page/layout.
    *   **Pros:** Static speed for most users, periodic updates without full rebuild.
    *   **Cons:** Content can be briefly stale.
    *   **Use Case:** Blogs with comments, product pages, moderately updated content.

4.  **Streaming UI (`React.Suspense`):**
    *   **How:** Sends static parts of a server-rendered page first, then streams dynamic content as data loads.
    *   **How to enable:** Wrap slower Server Components (esp. data fetching) in `<Suspense fallback={...}>`. Use `loading.tsx` for route segment boundaries.
    *   **Pros:** Improves perceived performance (TTFB, TTI) by showing initial UI/fallbacks quickly.
    *   **Cons:** Requires careful component structure.
    *   **Use Case:** Sections depending on slower data (recommendations, related items).

5.  **Partial Prerendering (PPR - Experimental):**
    *   **How:** Combines SSG + Streaming. Renders static "shell" at build time, defers dynamic parts (`<Suspense>`) until request time.
    *   **How to enable:** `experimental: { ppr: true }` in `next.config.js`. Routes default to PPR unless dynamic functions/uncached fetches used.
    *   **Pros:** Fast initial load (static shell) + dynamic capabilities (streaming).
    *   **Cons:** Experimental.
    *   **Use Case:** Static shells with dynamic sections (e-commerce cart, user info).

## Choosing a Strategy

*   **Static Content:** Default to **SSG**. Use `generateStaticParams` for dynamic routes.
*   **Personalized/Dynamic Data:** Use **SSR**. Combine with **Streaming UI** (`Suspense`).
*   **Periodic Updates:** Use **ISR**. Combine with **Streaming UI**.
*   **Mixed Content:** Explore **PPR** or structure carefully with **SSR + Streaming UI**.

## Example: Combining ISR and Streaming

```typescript
// app/products/[id]/page.tsx
import { Suspense } from 'react';
import ProductDetails from '@/components/ProductDetails';
import ProductRecommendations from '@/components/ProductRecommendations';
import LoadingSpinner from '@/components/LoadingSpinner';
import { notFound } from 'next/navigation';

// Fetch main product data - revalidate every hour (ISR)
async function getProduct(id: string) {
  const res = await fetch(`https://api.example.com/products/${id}`, {
    next: { revalidate: 3600 }
  });
  if (!res.ok) return null;
  return res.json();
}

// Fetch recommendations dynamically (SSR behavior within the ISR page)
async function getRecommendations(productId: string) {
  const res = await fetch(`https://api.example.com/recommendations?productId=${productId}`, {
     cache: 'no-store' // Ensure recommendations are fresh
  });
  if (!res.ok) return [];
  return res.json();
}

// Statically generate paths for known products
export async function generateStaticParams() {
  return [{ id: '1' }, { id: '2' }];
}

// Revalidate the static shell at most every 60 seconds
export const revalidate = 60;

export default async function ProductPage({ params }: { params: { id: string } }) {
  const product = await getProduct(params.id);
  if (!product) { notFound(); }

  // Recommendations fetched dynamically on request
  const recommendationsPromise = getRecommendations(params.id);

  return (
    <div>
      {/* Product details rendered using ISR data */}
      <ProductDetails product={product} />
      <hr />
      <h2>Recommended Products</h2>
      {/* Recommendations stream in */}
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

*(Refer to the official Next.js documentation on Rendering.)*