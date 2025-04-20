# Next.js Rendering Strategies (App Router)

Overview of different ways Next.js can render your pages.

## 1. Static Rendering (Default - SSG)

*   **Concept:** Components are rendered on the server **at build time**. The resulting HTML, CSS, and minimal JS are served to the client.
*   **Behavior:** By default, routes in the App Router are statically rendered if they don't use dynamic functions (like `cookies()`, `headers()`) or dynamic data fetching (`cache: 'no-store'`, `revalidate: 0`).
*   **Pros:** Very fast (served from CDN), highly cacheable, good for SEO, requires no server runtime after build.
*   **Cons:** Content is fixed at build time. Not suitable for personalized or frequently changing data.
*   **Use Case:** Marketing pages, blog posts, documentation, landing pages.
*   **Configuration:** This is the default. Ensure no dynamic functions or uncached fetches are used in the route segment. Use `generateStaticParams` for dynamic route segments you want to render statically.

## 2. Dynamic Rendering (SSR - Server-Side Rendering)

*   **Concept:** Components are rendered on the server **at request time**. The generated HTML is sent to the client.
*   **Behavior:** A route segment opts into dynamic rendering if it uses dynamic functions (`cookies()`, `headers()`, `searchParams` prop) or fetches data with caching disabled (`cache: 'no-store'`, `revalidate: 0`).
*   **Pros:** Content is always fresh, can be personalized based on the request (user, cookies), good for SEO.
*   **Cons:** Slower than static rendering (requires server computation per request), requires a server runtime.
*   **Use Case:** User dashboards, personalized feeds, pages with frequently updated data, pages requiring access to cookies/headers.
*   **Configuration:** Use dynamic functions or uncached data fetching. Can also explicitly opt-in with `export const dynamic = 'force-dynamic';`. Requires an SSR adapter (e.g., `@astrojs/node`) and `output: 'server'` or `'hybrid'` in `next.config.js`.

## 3. Incremental Static Regeneration (ISR)

*   **Concept:** A hybrid approach. Pages are initially rendered statically at build time, but can be regenerated on the server in the background after a certain time interval or on-demand.
*   **Behavior:** Statically rendered pages are served from the cache until the revalidation period expires. The next request receives the cached (stale) page, while Next.js triggers a background regeneration. Subsequent requests get the newly generated page.
*   **Pros:** Benefits of static speed for most users, while allowing content to update periodically without a full rebuild. Scales well.
*   **Cons:** Initial request after revalidation period might see stale data. Requires a server runtime.
*   **Use Case:** Blog posts with comments, e-commerce product pages (prices might change), pages with moderately frequent updates.
*   **Configuration:** Use the `next: { revalidate: seconds }` option in `fetch` calls within Server Components, or export `export const revalidate = seconds;` from the page/layout. Requires an SSR adapter and `output: 'server'` or `'hybrid'`.

## 4. Streaming UI (`React.Suspense`)

*   **Concept:** Allows parts of the UI to be rendered and streamed to the client progressively as data becomes available on the server, improving perceived performance. Works with both SSR and SSG (with deferred data).
*   **Behavior:** Wrap components that fetch data (or slow-rendering components) in `<Suspense fallback={...}>`. The server sends the initial HTML shell (including the fallback UI), then streams the content of the Suspended component once its data is ready.
*   **Pros:** Faster Time To First Byte (TTFB) and First Contentful Paint (FCP). User sees content sooner, even if some parts are still loading.
*   **Cons:** Requires careful component structure. Can involve more complex loading state management.
*   **Use Case:** Sections of a page that depend on slower data fetches (e.g., personalized recommendations, related articles).
*   **Configuration:** Use `<Suspense>` in your React components. Define `loading.tsx` files for automatic Suspense boundaries tied to route segments.

```tsx
// app/dashboard/page.tsx
import { Suspense } from 'react';
import UserWelcome from './UserWelcome'; // Assume this fetches user data (slow)
import Stats from './Stats'; // Assume this fetches stats (fast)
import StatsSkeleton from './StatsSkeleton'; // Loading UI for Stats

export default function DashboardPage() {
  return (
    <div>
      {/* UserWelcome streams in when ready */}
      <Suspense fallback={<div>Loading user...</div>}>
        <UserWelcome />
      </Suspense>

      {/* Stats streams in when ready, shows skeleton meanwhile */}
      <Suspense fallback={<StatsSkeleton />}>
        <Stats />
      </Suspense>
    </div>
  );
}
```

## 5. Partial Prerendering (PPR - Experimental)

*   **Concept:** Combines static and dynamic rendering within a single route. Renders a static shell for the route quickly, while dynamic parts (wrapped in Suspense) are streamed in based on request-time data.
*   **Behavior:** Aims to provide the speed of static with the dynamism of SSR for specific parts of a page.
*   **Pros:** Potentially the best of both worlds - fast initial load via static shell, dynamic content streamed in.
*   **Cons:** Still experimental, API and behavior might change. Requires careful use of Suspense.
*   **Use Case:** E-commerce pages with static layout but dynamic cart/user info, dashboards with static shells but dynamic content sections.
*   **Configuration:** Enable `experimental: { ppr: true }` in `next.config.js`. Structure page with static shell and dynamic parts wrapped in `<Suspense>`.

*(Choose the rendering strategy per-route based on data freshness requirements, personalization needs, and performance goals.)*