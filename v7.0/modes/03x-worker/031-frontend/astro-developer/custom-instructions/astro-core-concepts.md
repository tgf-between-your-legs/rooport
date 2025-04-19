# Astro: Core Concepts (.astro Components)

Understanding the structure and syntax of Astro components (`.astro` files).

## Core Concept: Astro Components (`.astro`)

Astro components are the fundamental building blocks for Astro pages, layouts, and reusable UI elements. They use a `.astro` file extension and have a unique single-file component format combining JavaScript/TypeScript (in the "component script") and an HTML-like template.

**Key Features:**

*   **HTML-like Template:** The main part of the component, resembling HTML but with support for JSX-like expressions, importing other components, and special Astro directives.
*   **Component Script (Code Fence `---`):** Optional JavaScript/TypeScript code block at the top, enclosed by `---` fences. Code here runs **only on the server** (during build or SSR request) to fetch data, define variables, and prepare data for the template. It's not shipped to the client by default.
*   **Zero JS by Default:** JavaScript in the component script does *not* run on the client unless you explicitly create an interactive "island" using a UI framework component and a `client:*` directive.
*   **Scoped Styles:** `<style>` tags within an `.astro` component are scoped by default, preventing styles from leaking out.

## Structure of an `.astro` File

```astro
---
// Component Script (Runs on Server) - Optional
// Import other components, utilities, data fetching logic
import SomeOtherComponent from '../components/SomeOtherComponent.astro';
import BaseLayout from '../layouts/BaseLayout.astro';
import { SITE_TITLE } from '../config'; // Import constants/variables

// Define props the component accepts (using TypeScript)
interface Props {
  title: string;
  data?: any[]; // Optional data array
}
const { title, data = [] } = Astro.props; // Destructure props with default value

// Fetch data or perform server-side logic
const response = await fetch('...');
const items = await response.json();

// Define variables for use in the template
const formattedTitle = `${SITE_TITLE} | ${title.toUpperCase()}`;
const itemCount = items.length;
const showWarning = itemCount === 0;
---
<!-- HTML-like Template (Server-Rendered HTML + Client Directives) -->
<BaseLayout pageTitle={formattedTitle}>
  <h1>{formattedTitle}</h1>
  <p>Welcome to the page!</p>

  {/* Conditional Rendering */}
  {showWarning && <p class="warning">No items found!</p>}

  {/* Looping / Mapping */}
  <ul>
    {items.map((item) => (
      <li>{item.name}</li>
    ))}
  </ul>

  {/* Using Imported Components */}
  <SomeOtherComponent message="Hello from parent" />

  {/* Slots: Placeholder for child content passed from parent */}
  <slot /> {/* Default slot */}
  <slot name="details" /> {/* Named slot */}

  {/* Client-side Script (Rarely needed in .astro, prefer framework components) */}
  <script>
    // Standard <script> tags are processed by Astro and bundled.
    // They run ONCE when the element loads.
    console.log('This script runs on the client');
    document.body.classList.add('js-loaded');
  </script>

  {/* Scoped Styles */}
  <style>
    h1 {
      color: purple; /* Scoped to this component */
      font-size: 2rem;
    }
    .warning {
      color: red;
      font-weight: bold;
    }
    /* Global styles (use :global() modifier) */
    :global(body) {
      margin: 0;
    }
  </style>

  {/* Define global styles (less common, prefer global CSS file) */}
  <style is:global>{`
    body { background-color: #f0f0f0; }
  `}</style>

  {/* Define variables accessible to CSS (requires `define:vars`) */}
  <style define:vars={{ themeColor: 'blue' }}>
    h1 { color: var(--themeColor); }
  </style>
</BaseLayout>
```

## Key Template Features

*   **JSX-like Expressions `{}`:** Embed JavaScript expressions directly in the template.
    *   `<h1>{pageTitle}</h1>`
    *   `<p class={isActive ? 'active' : ''}>Status</p>`
    *   `<button disabled={!canSubmit}>Submit</button>`
*   **Component Imports:** Import `.astro` components or UI framework components (React, Vue, etc.) in the script fence and use them like HTML tags. Props are passed as attributes.
    *   `<MyComponent propName="value" count={5} />`
*   **Props (`Astro.props`):** Access data passed from parent components via attributes. Define expected props using `interface Props` in TypeScript.
*   **Slots (`<slot />`):** Allow parent components to pass child HTML content into specific locations within your component's template. Use the `name` attribute for multiple, named slots.
*   **HTML Comments `<!-- -->`:** Standard HTML comments are included in the final HTML output.
*   **JS Comments `{/* */}`:** JavaScript-style comments within JSX-like expressions are stripped during the build.
*   **Directives:** Special attributes like `class:list`, `set:html`, `is:inline`, and `client:*` (for islands).

## CSS Scoping

*   `<style>` tags are scoped by default. Astro adds a unique attribute to elements and rewrites CSS rules to target only elements within that component.
*   Use `:global()` modifier for unscoped styles (e.g., `:global(body)`).
*   Use `is:global` attribute on `<style>` tag for a block of global styles.
*   Use `define:vars` attribute on `<style>` tag to pass script variables to CSS custom properties.

Astro components provide a powerful way to build server-rendered HTML with scoped CSS and optional client-side interactivity via islands.

*(Refer to the official Astro Components documentation.)*