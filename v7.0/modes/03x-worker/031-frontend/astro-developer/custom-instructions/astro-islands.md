# Astro: Islands Architecture & Client Directives

Understanding Astro's approach to partial hydration using islands and `client:*` directives.

## Core Concept: Islands Architecture

Astro renders your UI components to HTML on the server by default, shipping **zero client-side JavaScript**. This leads to fast initial page loads (quick First Contentful Paint and Time to Interactive).

However, many UIs require interactive elements that need JavaScript to run in the browser (e.g., image carousels, stateful counters, data fetching components, anything using `useState` or `useEffect` in React/Vue/Svelte).

Astro handles this using the **Islands Architecture**:

*   **Static HTML Base:** Most of your site remains static HTML, rendered on the server.
*   **Interactive "Islands":** You explicitly mark specific UI framework components (React, Vue, Svelte, etc.) that need to run in the browser as "islands".
*   **Partial Hydration:** Astro automatically hydrates (makes interactive) only these islands on the client, loading their necessary JavaScript. The surrounding static HTML remains untouched by client-side JS.

This approach avoids hydrating the entire page, significantly reducing the amount of JavaScript shipped to the browser compared to traditional SPAs.

## Client Directives (`client:*`)

You mark a UI framework component as an island by adding a `client:*` directive to it in your `.astro` template. These directives control *when* the component's JavaScript should be loaded and hydrated.

**Available Directives:**

*   **`client:load`:**
    *   **Behavior:** Loads and hydrates the component JavaScript immediately when the page loads.
    *   **Use Case:** For elements immediately visible and interactive on page load (e.g., a header with a dropdown menu). Use sparingly as it impacts initial load time.
*   **`client:idle`:**
    *   **Behavior:** Loads and hydrates the component JavaScript as soon as the main thread is free (uses `requestIdleCallback`).
    *   **Use Case:** For lower-priority components that don't need to be immediately interactive but should load fairly soon (e.g., a sidebar toggle, an image carousel further down the page).
*   **`client:visible`:**
    *   **Behavior:** Loads and hydrates the component JavaScript only when the element enters the viewport (uses `IntersectionObserver`).
    *   **Use Case:** Ideal for components below the fold or content that only needs to become interactive when visible (e.g., image carousels, interactive widgets in footers or sidebars, video players). **Often the best default choice for performance.**
*   **`client:media={query}`:**
    *   **Behavior:** Loads and hydrates the component JavaScript only when a specific CSS media query is met.
    *   **Use Case:** For components only needed on certain screen sizes (e.g., a mobile-only sidebar toggle).
    *   **Example:** `client:media="(max-width: 768px)"`
*   **`client:only={framework}`:**
    *   **Behavior:** Loads the component JavaScript immediately on page load but **skips server-rendering (SSR)**. The component renders *only* in the client browser. Requires specifying the framework (e.g., `client:only="react"`).
    *   **Use Case:** For components that heavily rely on browser-only APIs in their initial render (e.g., accessing `window` directly) or components that simply cannot be server-rendered. Use with caution as it can impact perceived performance and SEO if misused.

**Important Notes:**

*   Client directives can **only** be used on UI framework components (React, Vue, Svelte, etc.) imported into an `.astro` file. They **cannot** be used on `.astro` components themselves (as `.astro` components render to HTML only on the server).
*   Props passed to island components must be **serializable** (convertible to JSON), as Astro needs to send them from the server to the client. Functions, complex classes, etc., cannot be passed directly as props.

## Example Usage

```astro
---
// src/pages/index.astro
import BaseLayout from '../layouts/BaseLayout.astro';
import StaticAstroComponent from '../components/StaticAstroComponent.astro';
// Import UI framework components
import InteractiveCounter from '../components/InteractiveCounter.jsx'; // React component
import ImageCarousel from '../components/ImageCarousel.svelte'; // Svelte component
import MobileMenuToggle from '../components/MobileMenuToggle.vue'; // Vue component
---
<BaseLayout pageTitle="Astro Islands">
  <h1>Welcome</h1>
  <StaticAstroComponent /> {/* Renders only HTML */}

  {/* React Counter: Hydrates when main thread is idle */}
  <InteractiveCounter client:idle />

  <section style="margin-top: 150vh;"> {/* Section far down the page */}
    <h2>Image Gallery</h2>
    {/* Svelte Carousel: Hydrates only when it scrolls into view */}
    <ImageCarousel client:visible />
  </section>

  {/* Vue Toggle: Hydrates only on smaller screens */}
  <MobileMenuToggle client:media="(max-width: 600px)" />

  {/* React component that MUST run client-side only */}
  {/* <HeavyClientComponent client:only="react" /> */}

</BaseLayout>
```

By strategically applying `client:*` directives, you control the hydration process, ensuring optimal performance by loading JavaScript only when and where it's needed. Start with `client:visible` and use `client:idle` or `client:load` only when necessary for immediate interactivity.

*(Refer to the official Astro Islands and Client Directives documentation.)*