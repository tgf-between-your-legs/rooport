# Astro: Islands & UI Frameworks

## 1. Islands Architecture

Astro renders UI components to HTML on the server by default (Zero JS). Interactive elements require client-side JavaScript. Astro handles this via the **Islands Architecture**:

*   **Static HTML Base:** Most of the site remains static HTML.
*   **Interactive "Islands":** Explicitly mark UI framework components (React, Vue, Svelte, etc.) that need browser interactivity as "islands".
*   **Partial Hydration:** Astro hydrates only these islands on the client, loading their necessary JavaScript based on `client:*` directives.

## 2. Client Directives (`client:*`)

Add these directives to UI framework components (imported into `.astro` files) to control hydration.

*   **`client:load`:** Hydrates immediately on page load. Use sparingly for critical above-the-fold UI.
*   **`client:idle`:** Hydrates when the main thread is free (`requestIdleCallback`). Good for lower-priority components.
*   **`client:visible`:** Hydrates when the component enters the viewport (`IntersectionObserver`). **Often the best default for performance.**
*   **`client:media={query}`:** Hydrates only when a CSS media query is met (e.g., `client:media="(max-width: 768px)"`).
*   **`client:only={framework}`:** Renders *only* on the client, skipping SSR. Use for components incompatible with server rendering (e.g., heavy use of `window`). Requires specifying the framework (e.g., `client:only="react"`).

**Important:**
*   Client directives only work on **framework components**, not `.astro` components.
*   Props passed to client-hydrated islands must be **serializable** (JSON-compatible).

## 3. Integrating UI Frameworks (React, Vue, Svelte, etc.)

Use components from other frameworks within Astro islands.

**Setup:**

1.  **Install Integration:** `npx astro add [react|vue|svelte|etc]` (installs dependencies, updates `astro.config.mjs`).
2.  **Configure `tsconfig.json` (If needed):** Ensure JSX support is configured if using TSX/JSX.

**Usage:**

1.  **Create Component:** Write component using framework syntax (e.g., `.jsx`, `.vue`, `.svelte`) in `src/components/`.
2.  **Import Component:** Import into `.astro` script fence.
3.  **Use in Template:** Use like an HTML tag.
4.  **Pass Props:** Pass serializable props as attributes.
5.  **Add `client:*` Directive:** Add directive if client-side interactivity is needed.

```astro
---
// src/pages/frameworks.astro
import ReactCounter from '../components/ReactCounter.jsx';
import VueToggle from '../components/VueToggle.vue';
---
<ReactCounter initialCount={5} client:idle />
<VueToggle client:visible message="Toggle Me" />
```

```jsx
// src/components/ReactCounter.jsx
import React, { useState } from 'react';
function ReactCounter({ initialCount = 0 }) {
  const [count, setCount] = useState(initialCount);
  return (
    <div>
      <p>Count (React): {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}
export default ReactCounter;
```

*(Refer to the official Astro Islands and UI Frameworks documentation.)*