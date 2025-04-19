# Astro: Performance Optimization

Leveraging Astro's features for building fast websites.

## Core Concept: Performance by Default

Astro is designed for performance:

1.  **Zero Client-Side JavaScript by Default:** `.astro` components render to HTML on the server. No JS runtime shipped unless using framework components with `client:*` directives.
2.  **Partial Hydration (Islands):** Only interactive components (islands) load their JS on the client, based on `client:*` directives (`load`, `idle`, `visible`, `media`).
3.  **Server-First Rendering:** Content rendered server-side (SSG or SSR) for faster FCP and better SEO.
4.  **UI Framework Agnostic:** Use frameworks only for interactive parts, minimizing client footprint.
5.  **Asset Optimization:** Automatic CSS/JS bundling/minification, image optimization via `<Image>`.

## Optimization Techniques

1.  **Minimize Islands & Use `client:visible`:**
    *   Keep components static (`.astro`) where possible.
    *   Prefer `client:visible` for islands to delay JS loading until needed. Use `client:idle` or `client:load` sparingly.
2.  **Optimize Framework Components:**
    *   Apply standard framework optimizations (memoization, etc.).
    *   Be mindful of framework runtime/library bundle sizes.
3.  **Code Splitting:** Astro automatically splits JS based on pages and islands.
4.  **Optimize CSS:**
    *   Leverage Astro's default style scoping.
    *   Consider utility-first CSS (e.g., Tailwind) for potentially smaller bundles.
5.  **Optimize Images:**
    *   Use `<Image />` or `<Picture />` from `astro:assets` for automatic optimization (resizing, WebP/AVIF, lazy loading). Place source images in `src/assets/`.
    *   Manually compress static images in `public/`.
6.  **Lazy Load Content:** Use `client:visible` for components below the fold.
7.  **Reduce Server Load (SSR/Hybrid):**
    *   Cache expensive data fetches.
    *   Optimize database queries.
    *   Use `output: 'hybrid'` to pre-render static routes.
    *   Avoid blocking `await` calls in component scripts if possible.
8.  **Analyze Build Output:** Inspect `dist/` for bundle sizes.
9.  **Use Astro Dev Toolbar & Audit:** Identify performance/accessibility issues during development. Run `npx astro check --perf`.
10. **Third-Party Scripts:** Use `@astrojs/partytown` integration to run heavy scripts off the main thread.

*(Refer to the official Astro Performance documentation.)*