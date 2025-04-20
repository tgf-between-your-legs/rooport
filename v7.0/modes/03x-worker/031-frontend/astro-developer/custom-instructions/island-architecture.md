# Astro Island Architecture & Client Directives

Understanding Astro's approach to partial hydration for performance.

## Core Concept: Islands Architecture

*   **Problem:** Traditional SPAs (React, Vue, Svelte) often hydrate the entire application on the client, sending large amounts of JavaScript even for mostly static content.
*   **Astro's Solution:** Render UI components to HTML on the server (or at build time) with **zero client-side JavaScript by default**.
*   **Islands:** Interactive UI components (written in React, Vue, Svelte, etc.) are treated as "islands" within the static HTML. JavaScript for these islands is only loaded and hydrated on the client when needed, based on specific conditions.

## Client Directives (`client:*`)

These directives are added as attributes to UI framework components (`.jsx`, `.vue`, `.svelte`) within your `.astro` files to control *when* their JavaScript loads and hydrates.

*   **`client:load`**
    *   **Behavior:** Loads and hydrates the component JavaScript immediately when the page loads.
    *   **Use Case:** For elements immediately visible and interactive above the fold (e.g., a header menu). Use sparingly as it impacts initial load performance.
    ```astro
    ---
    import InteractiveHeader from '../components/InteractiveHeader.jsx';
    ---
    <InteractiveHeader client:load />
    ```

*   **`client:idle`**
    *   **Behavior:** Loads and hydrates the component JavaScript as soon as the main thread is free (uses `requestIdleCallback`).
    *   **Use Case:** For lower-priority components below the fold that don't need to be immediately interactive (e.g., an image carousel further down the page).
    ```astro
    ---
    import ImageCarousel from '../components/ImageCarousel.svelte';
    ---
    <ImageCarousel client:idle />
    ```

*   **`client:visible`**
    *   **Behavior:** Loads and hydrates the component JavaScript only when the element enters the viewport (uses `IntersectionObserver`).
    *   **Use Case:** Ideal for components further down the page or content that is revealed later. Good balance of performance and interactivity.
    ```astro
    ---
    import VideoPlayer from '../components/VideoPlayer.vue';
    ---
    <VideoPlayer client:visible />
    ```

*   **`client:media={string}`**
    *   **Behavior:** Loads and hydrates the component JavaScript only when a specific CSS media query is met.
    *   **Use Case:** For components only needed on certain screen sizes (e.g., a mobile-only sidebar toggle).
    ```astro
    ---
    import MobileMenuToggle from '../components/MobileMenuToggle.jsx';
    ---
    <MobileMenuToggle client:media="(max-width: 768px)" />
    ```

*   **`client:only={string}`**
    *   **Behavior:** Loads the component JavaScript on the client **but does not hydrate it**. Skips SSR. Requires the framework's client-side runtime.
    *   **Use Case:** For components that *must* run only in the browser and cannot be server-rendered (e.g., components heavily relying on browser-specific APIs like WebGL, or components causing issues during SSR). Use as a last resort.
    ```astro
    ---
    // This component might use browser APIs not available on the server
    import HeavyClientComponent from '../components/HeavyClientComponent.jsx';
    ---
    <HeavyClientComponent client:only="react" />
    ```

## Key Benefits

*   **Performance:** Reduces the amount of JavaScript shipped to the client, leading to faster load times and better Core Web Vitals.
*   **Flexibility:** Allows using multiple UI frameworks on the same page.
*   **Developer Experience:** Write components in your preferred framework while Astro handles the optimization.

## Considerations

*   **Props:** Props passed to island components must be serializable (no functions, complex classes, etc.) as they are sent as JSON.
*   **Shared State:** Sharing state between islands requires specific strategies (Nano Stores, custom events, global state libraries compatible with Astro). Islands are isolated by default.
*   **Choose Wisely:** Select the most appropriate `client:*` directive based on when the component *needs* to become interactive. Default to no directive (static HTML) if no client-side interactivity is required.

*(Refer to the official Astro Islands documentation: https://docs.astro.build/en/concepts/islands/)*