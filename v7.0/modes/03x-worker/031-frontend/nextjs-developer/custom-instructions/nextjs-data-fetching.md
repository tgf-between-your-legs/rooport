# Next.js: Data Fetching (App Router)

Strategies for fetching data in Next.js App Router applications.

## Core Concept: Server-Centric Data Fetching

The App Router encourages fetching data primarily on the server, leveraging React Server Components (RSCs). This improves performance by reducing client-side JavaScript and moving data fetching closer to the data source.

**Primary Methods:**

1.  **Direct Fetching in Server Components:** Use `async/await` with `fetch` (or database clients/ORMs) directly inside Server Components (`page.tsx`, `layout.tsx`, or other components not marked `'use client'`).
2.  **Route Handlers (`route.ts`):** Create dedicated API endpoints within the `app/api/` directory to fetch data, often used by Client Components or external services.
3.  **Server Actions (for Mutations):** While primarily for mutations (POST, PUT, DELETE), Server Actions can also fetch data after a mutation to return updated state. (See `nextjs-server-actions.md`).

**Client-Side Fetching:** Still possible within Client Components (`'use client'`) using `useEffect` with `fetch`, or libraries like SWR/React Query, but generally less preferred for initial data loading compared to server-centric approaches.

## 1. Fetching in Server Components

*   **How:** Make components `async` and use `await fetch(...)` or `await db.query(...)` directly within the component body.
*   **Benefits:** Simple, colocated data fetching logic, data is available before rendering, reduces client-side waterfalls.
*   **Caching:** Next.js automatically extends the native `fetch` API to provide request memoization and data caching.
    *   **Automatic Caching:** By default, `fetch` requests are cached indefinitely (similar to `getStaticProps` in Pages Router).
    *   **Opting out of Caching:**
        *   `fetch(url, { cache: 'no-store' })`: Fetches fresh data on every request (SSR behavior).
        *   `fetch(url, { next: { revalidate: seconds } })`: Incremental Static Regeneration (ISR) - revalidates data at most once per specified interval.
    *   **Dynamic Functions:** Using functions like `cookies()` or `headers()` from `next/headers`, or `searchParams` prop, will automatically opt the route into dynamic rendering (SSR) and disable static caching for `fetch` requests within that route segment.
*   **Streaming & Suspense:** Wrap data-fetching Server Components in `<Suspense fallback={...}>` to stream UI progressively as data loads.

```typescript
// app/products/[id]/page.tsx (Server Component)
import { Suspense } from 'react';
import ProductDetails from '@/components/ProductDetails'; // Assume this is also an RSC
import ProductReviews from '@/components/ProductReviews'; // Assume this fetches reviews
import LoadingSpinner from '@/components/LoadingSpinner';

// Fetch product details (cached by default)
async function getProduct(id: string) {
  const res = await fetch(`https://api.example.com/products/${id}`);
  if (!res.ok) throw new Error('Failed to fetch product');
  return res.json();
}

// Fetch reviews (example: revalidate every hour)
async function getReviews(id: string) {
  const res = await fetch(`https://api.example.com/products/${id}/reviews`, {
    next: { revalidate: 3600 } // ISR: Revalidate every hour
  });
  if (!res.ok) throw new Error('Failed to fetch reviews');
  return res.json();
}

export default async function ProductPage({ params }: { params: { id: string } }) {
  // Initiate fetches (can run in parallel)
  const productData = getProduct(params.id);
  const reviewsData = getReviews(params.id);

  // Wait for mandatory data (product details)
  const product = await productData;

  return (
    <div>
      {/* Render product details immediately */}
      <ProductDetails product={product} />

      <hr />
      <h2>Reviews</h2>
      {/* Use Suspense for non-critical/slower data */}
      <Suspense fallback={<LoadingSpinner />}>
        {/* This component will stream in when reviewsData resolves */}
        {/* @ts-expect-error Async Server Component */}
        <ProductReviews reviewsPromise={reviewsData} />
      </Suspense>
    </div>
  );
}

// components/ProductReviews.tsx (Example Suspense component)
async function ProductReviews({ reviewsPromise }) {
  // Wait for the promise passed as a prop
  const reviews = await reviewsPromise;
  return (
    <ul>
      {reviews.map(review => <li key={review.id}>{review.text}</li>)}
    </ul>
  );
}
```

## 2. Route Handlers (`app/api/.../route.ts`)

*   **Purpose:** Create traditional API endpoints. Useful for Client Components needing to fetch data, handling webhooks, or providing an API for external use.
*   **How:** Define functions (`GET`, `POST`, etc.) within `route.ts` files. Use `fetch` or database clients inside these functions.
*   **Caching:** Route Handlers can also leverage `fetch` caching, or you can implement custom caching. By default, `GET` handlers are statically evaluated if possible. Using dynamic functions (`cookies()`, `headers()`, `NextRequest`) opts into dynamic evaluation.

```typescript
// app/api/items/route.ts
import { NextResponse, NextRequest } from 'next/server';
import { fetchItemsFromDB } from '@/lib/db'; // Your data fetching logic

// GET /api/items
export async function GET(request: NextRequest) {
  // Example: Opt into dynamic rendering based on search param
  const searchParams = request.nextUrl.searchParams;
  const query = searchParams.get('query');

  try {
    const items = await fetchItemsFromDB({ query }); // Fetch based on query
    return NextResponse.json(items);
  } catch (error) {
    console.error(error);
    return new NextResponse('Failed to fetch items', { status: 500 });
  }
}

// POST /api/items
export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    // Validate body...
    // const newItem = await createItemInDB(body);
    return NextResponse.json({ message: 'Item created' /*, item: newItem */ }, { status: 201 });
  } catch (error) {
    return new NextResponse('Failed to create item', { status: 400 });
  }
}
```

**Fetching from Client Components:** Use `useEffect` with native `fetch` or libraries like SWR/React Query to call your Route Handlers.

```jsx
// components/ItemListClient.tsx
'use client';
import React, { useState, useEffect } from 'react';
import useSWR from 'swr'; // Example using SWR

const fetcher = (url: string) => fetch(url).then((res) => res.json());

export default function ItemListClient() {
  const { data: items, error, isLoading } = useSWR('/api/items', fetcher); // Fetch from Route Handler

  if (error) return <div>Failed to load items</div>;
  if (isLoading) return <div>Loading...</div>;

  return (
    <ul>
      {items?.map((item: any) => <li key={item.id}>{item.name}</li>)}
    </ul>
  );
}
```

Choose the data fetching strategy based on where the data is needed (server or client), caching requirements, and whether you're performing reads or mutations. Server Components offer the most direct and often most performant way for initial data loading.

*(Refer to the official Next.js documentation on Data Fetching.)*