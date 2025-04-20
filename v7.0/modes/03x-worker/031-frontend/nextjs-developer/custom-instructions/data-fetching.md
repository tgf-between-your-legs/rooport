# Next.js Data Fetching (App Router)

Strategies for fetching data in the Next.js App Router, focusing on Server Components, Route Handlers, and Caching.

## 1. Fetching in Server Components (Recommended for Page Data)

*   **Concept:** Server Components can directly use `async/await` with `fetch` (or other data sources like databases/ORMs) to get data needed for rendering. This happens entirely on the server.
*   **Caching:** Next.js automatically extends the native `fetch` API to provide powerful caching and revalidation controls.
    *   **Default:** `fetch` requests are automatically cached (`force-cache`). Good for data that doesn't change often.
    *   **Opt-out of Caching:** Fetch fresh data on every request.
        ```javascript
        fetch('https://...', { cache: 'no-store' });
        // Or for segment-level dynamic rendering:
        // export const dynamic = 'force-dynamic';
        ```
    *   **Time-based Revalidation (ISR):** Fetch data and cache it for a specific duration.
        ```javascript
        fetch('https://...', { next: { revalidate: 3600 } }); // Revalidate every hour (3600s)
        // Or for segment-level ISR:
        // export const revalidate = 3600;
        ```
*   **Example:**
    ```tsx
    // app/posts/[slug]/page.tsx (Server Component)
    async function getPost(slug: string) {
      const res = await fetch(`https://api.example.com/posts/${slug}`, {
        next: { revalidate: 60 }, // Revalidate data every 60 seconds
      });
      if (!res.ok) return undefined; // Or throw error for error.tsx
      return res.json();
    }

    export default async function PostPage({ params }: { params: { slug: string } }) {
      const post = await getPost(params.slug);

      if (!post) {
        notFound(); // Trigger not-found.tsx (if it exists)
      }

      return (
        <article>
          <h1>{post.title}</h1>
          <p>{post.body}</p>
        </article>
      );
    }
    ```

## 2. Route Handlers (API Routes)

*   **Concept:** Create API endpoints within your Next.js app using files named `route.ts` (or `.js`) inside the `app/api/` directory (or other directories).
*   **Use Cases:**
    *   Providing data endpoints for Client Components to fetch from.
    *   Handling specific backend logic triggered by requests (e.g., form submissions *without* Server Actions).
    *   Integrating with third-party services or webhooks.
*   **Implementation:** Export async functions named after HTTP methods (GET, POST, PUT, DELETE, etc.). Use `NextRequest` and `NextResponse` from `next/server`.
    ```typescript
    // app/api/items/route.ts
    import { NextRequest, NextResponse } from 'next/server';
    import { auth } from '@clerk/nextjs/server'; // Example: Auth check

    export async function GET(request: NextRequest) {
      const { userId } = auth();
      if (!userId) return new NextResponse("Unauthorized", { status: 401 });

      const searchParams = request.nextUrl.searchParams;
      const query = searchParams.get('query');

      // Fetch items based on query and userId
      // const items = await db.query...
      const items = [{ id: 1, name: `Item related to ${query}` }]; // Placeholder

      return NextResponse.json({ items });
    }

    export async function POST(request: NextRequest) {
       const { userId } = auth();
       if (!userId) return new NextResponse("Unauthorized", { status: 401 });

       const body = await request.json();
       // Validate body data...
       // const newItem = await db.create...
       const newItem = { id: 2, ...body }; // Placeholder

       return NextResponse.json(newItem, { status: 201 });
    }
    ```
*   **Caching:** Route Handlers are dynamically rendered by default (`cache: 'no-store'`). Caching behavior can be configured similarly to Server Components if needed (less common for APIs).

## 3. Fetching in Client Components (`useEffect`)

*   **Concept:** Fetch data client-side after the component mounts using `useEffect` and standard `fetch` or libraries like SWR/React Query.
*   **Use Cases:**
    *   Fetching data based on client-side interactions (user input).
    *   Displaying frequently changing data where SSR/SSG isn't ideal.
    *   When accessing browser-only APIs is required for the fetch.
*   **Considerations:**
    *   Data is not available for initial server render (can cause layout shifts or require loading states).
    *   Can lead to network waterfalls if multiple components fetch independently.
    *   Consider using libraries like SWR or React Query for caching, revalidation, and state management on the client.
    ```tsx
    'use client';
    import { useState, useEffect } from 'react';
    import useSWR from 'swr'; // Example using SWR

    const fetcher = (url: string) => fetch(url).then((res) => res.json());

    export default function UserProfile({ userId }: { userId: string }) {
      // Using SWR
      const { data, error, isLoading } = useSWR(`/api/users/${userId}`, fetcher);

      // Manual fetch with useEffect
      // const [data, setData] = useState(null);
      // const [isLoading, setIsLoading] = useState(true);
      // const [error, setError] = useState(null);
      // useEffect(() => {
      //   setIsLoading(true);
      //   fetch(`/api/users/${userId}`)
      //     .then(res => { if (!res.ok) throw new Error('Failed'); return res.json(); })
      //     .then(setData)
      //     .catch(setError)
      //     .finally(() => setIsLoading(false));
      // }, [userId]);

      if (error) return <div>Failed to load</div>;
      if (isLoading) return <div>Loading...</div>;

      return <div>Hello {data.name}!</div>;
    }
    ```

## 4. On-Demand Revalidation

*   **Purpose:** Manually trigger revalidation (re-fetching and caching) of data for specific paths or cache tags, often after a mutation (e.g., via Server Actions or Route Handlers).
*   **Functions (`next/cache`):**
    *   `revalidatePath('/path/to/revalidate')`: Revalidates data associated with a specific URL path.
    *   `revalidateTag('my-cache-tag')`: Revalidates data associated with a specific cache tag (applied during `fetch`).
*   **Usage:** Call these functions within Server Actions or Route Handlers after data has been updated.
    ```typescript
    // Example in a Server Action
    'use server';
    import { revalidatePath } from 'next/cache';

    export async function updatePost(formData: FormData) {
      const id = formData.get('id');
      // ... update post in database ...
      revalidatePath(`/posts/${id}`); // Revalidate the specific post page
      revalidatePath('/posts'); // Revalidate the posts list page
    }
    ```

*(Choose the data fetching strategy based on where the data is needed, how often it changes, and whether it's required for the initial render.)*