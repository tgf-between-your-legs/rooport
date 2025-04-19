# Next.js: App Router Routing

Defining routes, dynamic segments, and navigation in the Next.js App Router.

## Core Concept: File-System Based Routing

The App Router uses conventions based on folders and special file names within the `app/` directory to define routes.

*   **Folders Define Segments:** Each folder represents a segment in the URL path.
*   **`page.tsx` / `.js` Defines Routes:** A `page.tsx` file within a folder makes that path segment accessible as a route and defines its UI.
*   **Nested Routes:** Nesting folders creates nested routes (e.g., `app/dashboard/settings/page.tsx` maps to `/dashboard/settings`).
*   **Layouts (`layout.tsx`):** Apply shared UI across segments within a folder and its children.

## Route Types

**1. Static Routes:**

*   Created by folders containing a `page.tsx` file.
*   Example: `app/about/page.tsx` creates the `/about` route.

**2. Dynamic Segments:**

*   **Purpose:** Create routes where part of the URL is variable (e.g., blog post slugs, product IDs).
*   **Syntax:** Use square brackets `[]` around a parameter name in the folder name (e.g., `[slug]`, `[id]`).
*   **Accessing Params:** The value of the dynamic segment is passed as the `params` prop to `layout.tsx`, `page.tsx`, and `generateMetadata` functions within that segment.

```typescript
// app/blog/[slug]/page.tsx
// Matches /blog/post-1, /blog/my-article, etc.

// params object will contain the matched slug: { slug: 'post-1' }
export default async function BlogPostPage({ params }: { params: { slug: string } }) {
  const { slug } = params;
  // const post = await fetchPostBySlug(slug); // Fetch data based on slug

  return (
    <div>
      <h1>Blog Post: {slug}</h1>
      {/* Display post content */}
    </div>
  );
}

// Optional: Generate static paths at build time (SSG)
export async function generateStaticParams() {
  // const posts = await fetchAllPostSlugs(); // Fetch all possible slugs
  const posts = [{ slug: 'post-1' }, { slug: 'post-2' }]; // Example

  return posts.map((post) => ({
    slug: post.slug,
  }));
}
```

**3. Catch-all Segments:**

*   **Purpose:** Match multiple path segments at the end of a URL.
*   **Syntax:** Use square brackets with three dots `[...]` (e.g., `[...slug]`).
*   **Accessing Params:** `params.slug` will be an *array* of the matched segments.
*   Example: `app/shop/[...filters]/page.tsx` matches `/shop/a`, `/shop/a/b`, `/shop/a/b/c`. `params.filters` would be `['a']`, `['a', 'b']`, `['a', 'b', 'c']` respectively.

**4. Optional Catch-all Segments:**

*   **Purpose:** Similar to catch-all, but also matches the route *without* the segment.
*   **Syntax:** Use double square brackets `[[...slug]]`.
*   Example: `app/docs/[[...slug]]/page.tsx` matches `/docs`, `/docs/a`, `/docs/a/b`. `params.slug` would be `undefined`, `['a']`, `['a', 'b']` respectively.

## Navigation (`<Link>` Component)

*   **Purpose:** Enables client-side navigation between routes within your Next.js application without a full page reload. Pre-fetches page data in the background for faster transitions.
*   **Import:** `import Link from 'next/link';`
*   **Usage:** Wrap an `<a>` tag or any other element. Pass the destination path to the `href` prop.

```jsx
import Link from 'next/link';

function Navigation() {
  return (
    <nav>
      <Link href="/">Home</Link> |
      <Link href="/about">About</Link> |
      <Link href="/dashboard">Dashboard</Link> |
      <Link href="/blog/post-1">Blog Post 1</Link> |
      {/* Prefetching disabled example */}
      <Link href="/slow-page" prefetch={false}>Slow Page</Link>
    </nav>
  );
}
```

*   **Prefetching:** Enabled by default when `<Link>` enters the viewport. Can be disabled with `prefetch={false}`.
*   **Dynamic Segments:** Construct the `href` string dynamically: `<Link href={`/blog/${post.slug}`}>`.

## Route Groups (`(folder)`)

*   **Purpose:** Organize routes logically or opt segments into different layouts *without* affecting the URL path.
*   **Syntax:** Wrap a folder name in parentheses `()`.
*   Example: `app/(marketing)/about/page.tsx` still maps to `/about`, but can share a layout defined in `app/(marketing)/layout.tsx`.

## Parallel Routes (`@folder`)

*   **Purpose:** Render multiple, independent pages (sub-routes) within the same layout simultaneously. Useful for dashboards, modals, or complex conditional UI.
*   **Syntax:** Create folders prefixed with `@` (slots). Define `page.tsx` within these slot folders.
*   **Layout:** The parent `layout.tsx` receives each slot as a prop (e.g., `props.analytics`, `props.team`). Render these props where desired in the layout.
*   **Navigation:** Navigating to a parallel route updates only that slot's content.

```typescript
// app/dashboard/layout.tsx
export default function DashboardLayout({
  children, // The main page content
  analytics, // Content from @analytics slot
  team,      // Content from @team slot
}: {
  children: React.ReactNode;
  analytics: React.ReactNode;
  team: React.ReactNode;
}) {
  return (
    <section>
      {children}
      <aside>{analytics}</aside>
      <footer>{team}</footer>
    </section>
  );
}

// app/dashboard/@analytics/page.tsx -> Renders into props.analytics
// app/dashboard/@team/page.tsx      -> Renders into props.team
```

The App Router provides a flexible and powerful file-system based approach to defining static, dynamic, and advanced routing patterns in Next.js.

*(Refer to the official Next.js documentation on Routing.)*