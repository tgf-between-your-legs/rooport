# App Router: Routing & Navigation

Defining routes, dynamic segments, and navigation in the Next.js App Router.

## Route Types

**1. Static Routes:**
*   Created by folders containing a `page.tsx` file (e.g., `app/about/page.tsx` -> `/about`).

**2. Dynamic Segments:**
*   **Purpose:** Create routes with variable parts (e.g., blog post slugs, product IDs).
*   **Syntax:** Use square brackets `[]` in the folder name (e.g., `[slug]`, `[id]`).
*   **Accessing Params:** The value is passed as the `params` prop to `layout.tsx`, `page.tsx`, etc. (e.g., `params.slug`).
*   **Example:** `app/blog/[slug]/page.tsx` matches `/blog/post-1`. `params` would be `{ slug: 'post-1' }`.
*   **`generateStaticParams`:** Optional function exported from dynamic segment pages/layouts to statically generate routes at build time (SSG). It should return an array of objects containing the possible `params` values.
    ```typescript
    // app/blog/[slug]/page.tsx
    export async function generateStaticParams() {
      // const posts = await fetchAllPostSlugs();
      const posts = [{ slug: 'post-1' }, { slug: 'post-2' }];
      return posts.map((post) => ({ slug: post.slug }));
    }
    ```

**3. Catch-all Segments:**
*   **Purpose:** Match multiple path segments.
*   **Syntax:** Use square brackets with three dots `[...]` (e.g., `[...slug]`).
*   **Accessing Params:** `params.slug` is an *array* of matched segments.
*   **Example:** `app/shop/[...filters]/page.tsx` matches `/shop/a/b`. `params.filters` would be `['a', 'b']`.

**4. Optional Catch-all Segments:**
*   **Purpose:** Like catch-all, but also matches the route *without* the segment.
*   **Syntax:** Use double square brackets `[[...slug]]`.
*   **Example:** `app/docs/[[...slug]]/page.tsx` matches `/docs` and `/docs/a/b`. `params.slug` would be `undefined` or `['a', 'b']`.

## Navigation

**1. `<Link>` Component:**
*   **Purpose:** Enables client-side navigation between routes without a full page reload. Pre-fetches page data.
*   **Import:** `import Link from 'next/link';`
*   **Usage:** Wrap an `<a>` tag or other element. Pass the destination path to `href`.
    ```jsx
    <Link href="/dashboard">Dashboard</Link>
    <Link href={`/blog/${post.slug}`}>Read Post</Link>
    ```
*   **Prefetching:** Enabled by default (on viewport entry). Disable with `prefetch={false}`.

**2. `useRouter()` Hook:**
*   **Purpose:** Programmatic navigation within Client Components.
*   **Import:** `import { useRouter } from 'next/navigation';`
*   **Usage:**
    ```jsx
    'use client';
    import { useRouter } from 'next/navigation';

    function MyButton() {
      const router = useRouter();
      return <button onClick={() => router.push('/dashboard')}>Go to Dashboard</button>;
    }
    ```
*   Methods: `router.push(path)`, `router.replace(path)`, `router.back()`, `router.forward()`, `router.refresh()`.
*   `router.refresh()`: Useful for refreshing the current route's data from the server without losing client-side state.

**3. `redirect()` Function:**
*   **Purpose:** Server-side redirection within Server Components, Route Handlers, or Server Actions.
*   **Import:** `import { redirect } from 'next/navigation';`
*   **Usage:** Call `redirect('/new-path')`. This throws a specific error caught by Next.js to initiate the redirect. Must be called *outside* a `try...catch` block intended to catch the redirect itself.

## Route Groups (`(folder)`)

*   **Purpose:** Organize routes or opt segments into layouts *without* affecting the URL path.
*   **Syntax:** Wrap a folder name in parentheses `()`.
*   **Example:** `app/(marketing)/about/page.tsx` maps to `/about`. Can share `app/(marketing)/layout.tsx`.

## Parallel Routes (`@folder`)

*   **Purpose:** Render multiple independent pages (slots) within the same layout simultaneously (e.g., dashboards, modals).
*   **Syntax:** Create folders prefixed with `@` (slots). Define `page.tsx` within slot folders.
*   **Layout:** Parent `layout.tsx` receives each slot as a prop (e.g., `props.analytics`, `props.team`). Render these props where desired.
*   **Default Content:** Define a `default.tsx` file in a slot folder to render when the slot isn't actively matched by navigation (e.g., on initial load).

*(Refer to the official Next.js documentation on Routing, Linking, and Navigation.)*