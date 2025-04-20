# Astro: Integrations

Adding features and framework support using Astro Integrations.

## Core Concept

Astro Integrations are addons that unlock new functionality in your Astro project. They can add support for UI frameworks (React, Vue, Svelte), tools (Tailwind CSS, Partytown), or new features (SSR, sitemaps, image optimization).

**Key Features:**

*   **Extensibility:** The primary way to add features beyond Astro's core.
*   **Configuration:** Managed in the `integrations` array within `astro.config.mjs`.
*   **`astro add` Command:** The easiest way to add official integrations. It handles installation, configuration updates, and often necessary peer dependencies.
*   **Community Integrations:** Many third-party integrations are available.

## Adding Integrations

The recommended way is using the `astro add` command:

```bash
# Installs and configures the integration automatically
npx astro add react
npx astro add tailwind
npx astro add sitemap
npx astro add vercel # Example SSR adapter
```

This command typically:

1.  Installs the integration package (e.g., `@astrojs/react`, `@astrojs/tailwind`) and its peer dependencies via your package manager (npm, yarn, pnpm).
2.  Imports and adds the integration to the `integrations` array in your `astro.config.mjs` file.

**Manual Installation (Less Common):**

1.  Install the package: `npm install @astrojs/react react react-dom`
2.  Manually import and add it to `astro.config.mjs`:

```javascript
// astro.config.mjs
import { defineConfig } from 'astro/config';
import react from '@astrojs/react'; // 1. Import
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  integrations: [
    react(), // 2. Add to integrations array
    tailwind({
      // Optional: Apply Tailwind base styles after other styles
      applyBaseStyles: false,
    }),
    // ... other integrations
  ]
});
```

## Common Integration Types

*   **UI Frameworks:** `@astrojs/react`, `@astrojs/vue`, `@astrojs/svelte`, `@astrojs/solid-js`, `@astrojs/preact`, `@astrojs/lit`. Enable using components from these frameworks within Astro islands.
*   **CSS & Styling:** `@astrojs/tailwind`, `@astrojs/partytown` (for off-main-thread third-party scripts), Sass/Less support (often built-in or via simple config).
*   **SSR Adapters:** `@astrojs/node`, `@astrojs/vercel`, `@astrojs/netlify`, `@astrojs/cloudflare`, etc. Enable server-side rendering or edge functions by providing an adapter for specific deployment platforms. Configured via the `output: 'server'` or `output: 'hybrid'` setting and the `adapter` property in `astro.config.mjs`.
    ```javascript
    // Example SSR config for Vercel
    import { defineConfig } from 'astro/config';
    import vercel from '@astrojs/vercel/serverless'; // Import adapter

    export default defineConfig({
      output: 'server', // Or 'hybrid' for mixed SSG/SSR
      adapter: vercel({
        // Optional adapter config
        webAnalytics: { enabled: true },
      }),
      // ... integrations
    });
    ```
*   **Site Features:** `@astrojs/sitemap` (generates `sitemap.xml`), `@astrojs/mdx` (adds MDX support), `@astrojs/rss` (generates RSS feeds).
*   **Image Optimization:** `@astrojs/image` (older, deprecated) or Astro's built-in `<Image />` and `<Picture />` components (recommended for v2.0+).

## Finding Integrations

*   **Official Integrations:** Listed on the Astro documentation website (https://docs.astro.build/en/guides/integrations-guide/). Use `npx astro add <name>`.
*   **Community Integrations:** Search on npm or the Astro Integrations directory (https://astro.build/integrations/). Install manually via npm/yarn/pnpm and configure in `astro.config.mjs`.

Integrations are a powerful way to extend Astro's capabilities and tailor it to your project's specific needs. Always consult the documentation for the specific integration you are using.

*(Refer to the official Astro Integrations documentation.)*