# Astro: Performance Optimization

Leveraging Astro's features for building fast websites.

## Core Concept: Performance by Default

Astro is designed with performance as a primary goal. Its architecture inherently promotes faster websites compared to traditional SPAs.

**Key Principles:**

1.  **Zero Client-Side JavaScript by Default:** `.astro` components render to HTML on the server. No JavaScript runtime is shipped to the client unless you explicitly opt-in using framework components and `client:*` directives.
2.  **Partial Hydration (Islands Architecture):** Only interactive components (islands) load their necessary JavaScript on the client, and only when specified by the `client:*` directive (`load`, `idle`, `visible`, `media`). This avoids hydrating the entire application.
3.  **Server-First Rendering:** Content is rendered on the server (SSG or SSR), leading to faster First Contentful Paint (FCP) and better SEO compared to client-side rendered (CSR) applications.
4.  **UI Framework Agnostic:** Use your preferred UI framework (React, Vue, Svelte, etc.) only for the interactive parts, minimizing the client-side footprint.
5.  **Asset Optimization:** Astro automatically optimizes assets in `src/assets/` (CSS bundling/minification, JS bundling/minification, image optimization via `<Image>`).

## Optimization Techniques

While Astro is fast by default, you can further optimize:

1.  **Minimize Islands & Use `client:visible`:**
    *   Be deliberate about which components *truly* need client-side interactivity. Keep as much as possible as static `.astro` components.
    *   For interactive islands, prefer `client:visible` to delay loading JavaScript until the component scrolls into view. Use `client:idle` for lower-priority components above the fold, and `client:load` only for critical, immediately interactive elements.
2.  **Optimize Framework Components:**
    *   Ensure the framework components used in islands are themselves performant. Apply standard framework optimization techniques (e.g., memoization in React, computed properties in Vue).
    *   Be mindful of the bundle size impact of framework runtimes and libraries imported by your islands.
3.  **Code Splitting:** Astro automatically code-splits based on pages and islands. JavaScript for one island doesn't block others.
4.  **Optimize CSS:**
    *   Astro scopes `<style>` tags in `.astro` components by default.
    *   Global CSS is bundled and minified.
    *   Consider using utility-first CSS frameworks like Tailwind CSS (via `@astrojs/tailwind` integration) which often result in smaller CSS bundles by reusing classes.
5.  **Optimize Images:**
    *   Use Astro's built-in `<Image />` component (`import { Image } from 'astro:assets';`) for automatic optimization (resizing, format conversion like WebP/AVIF) and best practices (lazy loading, `width`/`height` attributes). Place source images in `src/assets/`.
    *   Use the `<Picture />` component for more advanced art direction (different images/formats based on viewport).
    *   For static images in `public/` that don't need optimization, ensure they are appropriately sized and compressed manually.
6.  **Lazy Load Content:** Use `client:visible` for components displaying non-critical content below the fold.
7.  **Reduce Server Load (SSR/Hybrid):**
    *   Cache expensive data fetching operations where appropriate.
    *   Optimize database queries (`astro:db` or external).
    *   Use `output: 'hybrid'` mode to pre-render static pages where possible, reserving SSR only for truly dynamic routes.
    *   Be mindful of blocking `await` calls in the component script; use client-side fetching or deferring for non-critical data if it impacts server response time.
8.  **Analyze Build Output:** Inspect the build output (`dist/`) to understand bundle sizes and asset structure.
9.  **Use Astro Dev Toolbar & Audit:** The Astro Dev Toolbar includes an audit feature powered by Lighthouse to identify performance bottlenecks and accessibility issues during development. Run `npx astro check --perf` for static analysis of potential performance issues.
10. **Third-Party Scripts:** Use the `@astrojs/partytown` integration to run heavy third-party scripts (analytics, ads) off the main thread in a web worker, reducing their impact on main thread blocking time.

By leveraging Astro's architecture and applying these techniques, you can build exceptionally fast websites and applications.

*(Refer to the official Astro Performance documentation.)*