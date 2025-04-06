## Astro (Version Unknown) - Condensed Context Index

### Overall Purpose

Astro is a modern web framework designed for building fast, content-focused websites and web applications. It emphasizes performance through server-first rendering and an "Islands Architecture" that minimizes client-side JavaScript by default. Astro allows developers to use their favorite UI components (React, Vue, Svelte, etc.) or build with Astro's own component syntax, integrating seamlessly with Markdown and data sources.

### Core Concepts & Capabilities

*   **Component-Based Architecture (`.astro` files):** Build UIs with reusable `.astro` components using an HTML-like template syntax and a fenced (`---`) component script section for JavaScript/TypeScript logic. Supports `Astro.props` for passing data and `<slot />` (default and named) for content projection.
*   **Islands Architecture & Hydration:** Optimize performance by shipping minimal or zero client-side JavaScript by default. Use `client:*` directives (`client:load`, `client:visible`, `client:only="framework"`) to selectively hydrate interactive UI components ("islands") on the client. Supports various UI frameworks.
*   **Server Islands (`server:defer`):** Render components server-side in parallel with the main page request, improving time-to-first-byte for components requiring server-side processing.
*   **Content Collections API (`astro:content`):** Manage local content (Markdown, JSON, etc.) in a type-safe way. Define schemas using `zod` (`z`) in `src/content/config.ts` via `defineCollection`, and query content using `getCollection` or `getEntry`. Supports Markdown layouts with `MarkdownLayoutProps`.
*   **File-based Routing:** Create pages by adding `.astro` or `.md` files to the `src/pages/` directory. Supports static and dynamic routes (e.g., `src/pages/posts/[slug].astro`) using `getStaticPaths` to generate pages from data.
*   **Integrations:** Extend functionality via `astro.config.mjs` using the `integrations` array. Add support for UI frameworks (`@astrojs/react`, `@astrojs/vue`), SSR adapters, Tailwind, Astro DB (`@astrojs/db`), etc. Install via `npx astro add [integration]`.
*   **Configuration (`astro.config.mjs`):** Central file for project-wide settings, using `defineConfig` helper for type safety. Configure site URL, integrations, build options, etc.
*   **Data Fetching:** Use standard `fetch` API with top-level `await` in `.astro` component scripts to fetch data during the build or on request (SSR).
*   **Astro DB (`astro:db`):** An integrated SQL database solution (built on LibSQL/Turso). Define tables (`defineTable`) and columns (`column`) in `db/config.ts` using `defineDb`. Interact with the DB using the `db` client (`db.insert`, `db.select`).
*   **Astro Actions (`astro:actions`):** Define type-safe server-side functions in `src/actions/index.ts` using `defineAction` (with `zod` for input validation) that can be called securely from client-side code, simplifying form handling and mutations.
*   **Middleware (`src/middleware.js`):** Intercept requests and responses using an `onRequest` function to modify response data, check authentication, or redirect users. Access/modify shared data via `context.locals`.
*   **TypeScript Support:** First-class TypeScript integration for components (`interface Props`), configuration, content collections, and actions.
*   **Client-Side Scripting:** Include standard `<script>` tags for vanilla JavaScript or module imports. Pass data from server using `data-*` attributes or `define:vars={...}` directive.

### Key APIs / Components / Configuration / Patterns

*   **`.astro` files:** Fundamental component structure with `---` script fence and HTML-like template.
*   **`Astro.props`:** Access properties passed into a component.
*   **`Astro.request`:** Access the incoming request object (SSR/middleware).
*   **`Astro.site`:** Access the base URL from `astro.config.mjs`.
*   **`Astro.generator`:** Astro version identifier (for `<meta>` tags).
*   **`<slot />` / `<slot name="..." />`:** Content injection points within layouts/components.
*   **`client:load | visible | only="framework"`:** Directives for client-side component hydration.
*   **`server:defer`:** Directive for parallel server-side rendering (Server Islands).
*   **`getStaticPaths()`:** Exported function in dynamic route files (`src/pages/`) for defining static paths and props.
*   **`astro.config.mjs`:** Main configuration file; uses `defineConfig`. Key property: `integrations`.
*   **`src/content/config.ts`:** Defines content collections using `defineCollection` and `z` (Zod).
*   **`getCollection('name')` / `getEntry('name', 'id')`:** Functions from `astro:content` to query collections.
*   **`db/config.ts`:** Defines database schema using `defineDb`, `defineTable`, `column` from `astro:db`.
*   **`db` (from `astro:db`):** Client object for database interactions (`db.select`, `db.insert`, etc.).
*   **`src/actions/index.ts`:** Defines server actions using `defineAction` from `astro:actions`.
*   **`src/middleware.js`:** Defines middleware using `onRequest(context, next)`.
*   **`import.meta.glob()`:** Vite feature for importing multiple files (e.g., Markdown posts).
*   **Layout Components (`src/layouts/`):** Reusable page structure components.
*   **`npm create astro@latest` / `yarn create astro`:** Project initialization commands.
*   **`npx astro add [integration]`:** Command to add integrations.

### Common Patterns & Best Practices / Pitfalls

*   **Use Layouts:** Employ layout components (`src/layouts/`) for consistent page structure.
*   **Reusable `<head>`:** Create a dedicated component for common head elements (meta, SEO, links).
*   **Leverage TypeScript:** Use TypeScript (`interface Props`, schemas) for enhanced type safety.
*   **Minimize Client JS:** Default to static HTML; use `client:*` directives sparingly only for interactive elements (Islands).
*   **Content Collections API:** Prefer `astro:content` for managing structured content over manual imports.
*   **Astro DB / Actions:** Utilize built-in DB and Actions for streamlined data persistence and server interactions.
*   **Server-Side Validation:** Crucial for validating all user input from forms or actions on the server.
*   **Performance:** Be aware that top-level `await fetch()` can block rendering; consider alternatives like `server:defer` or client-side fetching if needed.

---
This index summarizes the core concepts, APIs, and patterns for Astro. Consult the full source documentation (`project_journal/context/source_docs/astro-developer-llms-context-20250406.md`) for exhaustive details.