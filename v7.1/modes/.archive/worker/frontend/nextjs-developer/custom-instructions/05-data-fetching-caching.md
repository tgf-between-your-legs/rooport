# App Router: Data Fetching & Caching

Strategies for fetching data and managing caching in the Next.js App Router.

## Core Concept: Server-Centric Data Fetching

The App Router encourages fetching data primarily on the server using React Server Components (RSCs) for better performance and reduced client-side JS.

**Primary Methods:**

1.  **Direct Fetching in Server Components (Recommended):**
    *   **How:** Use `async/await` with `fetch` (or DB clients/ORMs) directly inside RSCs (`page.tsx`, `layout.tsx`, etc.).
    *   **Benefits:** Simple, colocated logic, data available before render, reduces client waterfalls.
    *   **Caching:** Next.js extends `fetch` for automatic caching and revalidation.

2.  **Route Handlers (`route.ts`):**
    *   **How:** Create API endpoints in `app/api/.../route.ts`. Export `async` functions like `GET`, `POST`.
    *   **Use Cases:** Data endpoints for Client Components, webhooks, backend logic.

3.  **Server Actions (Mutations):**
    *   **How:** Functions marked `'use server'` for server-side mutations (POST, PUT, DELETE). Can also fetch data post-mutation.
    *   **Use Cases:** Form submissions, data updates triggered from client/server components.

**Client-Side Fetching:** Possible in Client Components (`'use client'`) via `useEffect` + `fetch` or libraries (SWR, React Query), but less preferred for initial load.

## Fetching in Server Components (Details)

*   Make components `async` and `await fetch(...)`.
*   **Caching (`fetch` options):**
    *   **Default:** `cache: 'force-cache'` (caches indefinitely or until revalidated/rebuilt).
    *   **No Cache (SSR):** `cache: 'no-store'` (fetches fresh on every request).
    *   **ISR:** `next: { revalidate: seconds }` (caches for `seconds`, revalidates in background).
*   **Dynamic Functions:** Using `cookies()`, `headers()`, or `searchParams` opts the route into dynamic rendering (SSR) and disables static `fetch` caching within that segment.
*   **Streaming:** Wrap data-fetching RSCs in `<Suspense fallback={...}>` to stream UI.

```typescript
// app/posts/[slug]/page.tsx (Server Component)
import { Suspense } from 'react';
import PostContent from '@/components/PostContent'; // Assumed RSC
import PostComments from '@/components/PostComments'; // Assumed RSC fetching comments
import LoadingSpinner from '@/components/LoadingSpinner';
import { notFound } from 'next/navigation';

// Fetch post (ISR: revalidate every hour)
async function getPost(slug: string) {
  const res = await fetch(`https://.../posts/${slug}`, { next: { revalidate: 3600 } });
  if (!res.ok) return null;
  return res.json();
}

// Fetch comments (SSR: no cache)
async function getComments(slug: string) {
  const res = await fetch(`https://.../posts/${slug}/comments`, { cache: 'no-store' });
  if (!res.ok) return [];
  return res.json();
}

export default async function PostPage({ params }: { params: { slug: string } }) {
  const postData = getPost(params.slug); // Initiate fetches
  const commentsData = getComments(params.slug);

  const post = await postData; // Wait for mandatory post data
  if (!post) { notFound(); }

  return (
    <article>
      <PostContent post={post} /> {/* Render immediately */}
      <hr />
      <h2>Comments</h2>
      {/* Stream comments */}
      <Suspense fallback={<LoadingSpinner />}>
        {/* @ts-expect-error Async Server Component */}
        <PostComments commentsPromise={commentsData} />
      </Suspense>
    </article>
  );
}
```

## Caching Fundamentals

Next.js uses multiple caching layers:

1.  **Request Memoization (React `cache`):**
    *   **Scope:** Single server request render pass.
    *   **Mechanism:** Deduplicates identical `fetch` calls *within the same render*. Automatic for `fetch` in RSCs.

2.  **Data Cache (Persistent):**
    *   **Scope:** Across multiple requests. Persisted on server/CDN.
    *   **Mechanism:** Caches `fetch` results based on URL and options.
    *   **Control:** `cache: 'force-cache'` (default), `cache: 'no-store'`, `next: { revalidate: seconds }`.

3.  **Full Route Cache (Server-Side):**
    *   **Scope:** Caches rendered HTML + RSC Payload for a route.
    *   **Mechanism:** Caches SSG/ISR routes. Dynamic routes (SSR) generally bypass this.
    *   **Control:** Route type (static/dynamic/ISR). Invalidated by `revalidatePath`/`revalidateTag`.

4.  **Router Cache (Client-Side):**
    *   **Scope:** Browser memory during session.
    *   **Mechanism:** Stores RSC Payload of visited routes for instant back/forward navigation.
    *   **Control:** Automatic. Cleared by `router.refresh()`. Invalidated by server revalidation on next navigation.

## Cache Invalidation

*   **Time-based (ISR):** `revalidate` option in `fetch` or segment config.
*   **On-Demand:**
    *   `revalidatePath(path)`: Invalidates Data Cache and Full Route Cache for a specific path.
    *   `revalidateTag(tag)`: Invalidates Data Cache entries tagged during `fetch` (`next: { tags: [...] }`) and Full Route Cache for routes using that data.
    *   **Usage:** Call within Server Actions or Route Handlers after mutations.

```typescript
// app/actions.ts
'use server';
import { revalidateTag, revalidatePath } from 'next/cache';

export async function updateItemAction(itemId: string, data: any) {
  // ... update item in DB ...
  revalidateTag(`item-${itemId}`); // Invalidate fetches tagged 'item-...'
  revalidatePath('/items');       // Invalidate listing page
  revalidatePath(`/items/${itemId}`); // Invalidate detail page
}

// Fetching with a tag:
// fetch(`.../items/${id}`, { next: { tags: [`item-${id}`] } });
```

*(Refer to the official Next.js documentation on Data Fetching and Caching.)*