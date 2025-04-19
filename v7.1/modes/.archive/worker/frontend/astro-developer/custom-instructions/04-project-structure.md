# Astro: Project Structure

Understanding the typical directory layout of an Astro project.

## Core Concept

Astro projects follow a conventional structure, although some aspects can be customized in `astro.config.mjs`. Understanding the purpose of key directories is essential for organizing code and content effectively.

## Default Project Structure

```
├── public/             # Static assets (images, fonts, favicons) - copied directly to build output root
│   └── favicon.svg
├── src/
│   ├── assets/         # Assets processed by Astro (images, CSS, JS) - referenced via import
│   │   └── logo.png
│   ├── components/     # Reusable UI components (.astro, .jsx, .vue, .svelte)
│   │   ├── Header.astro
│   │   └── Button.tsx
│   ├── content/        # Content Collections (Markdown, MDX, JSON, YAML)
│   │   ├── config.ts   # Collection schema definitions
│   │   └── blog/       # Example collection
│   │       ├── post-1.md
│   │       └── post-2.mdx
│   ├── layouts/        # Reusable page layout components (.astro)
│   │   └── BaseLayout.astro
│   ├── middleware.js   # (SSR/Edge) Code run before/after page rendering
│   ├── pages/          # Site pages & API routes (.astro, .md, .mdx, .js/.ts for API)
│   │   ├── index.astro
│   │   ├── about.astro
│   │   ├── blog/
│   │   │   ├── [slug].astro # Dynamic route for blog posts
│   │   │   └── index.astro  # Blog index page
│   │   └── api/
│   │       └── contact.ts # API endpoint at /api/contact
│   ├── styles/         # Global CSS/SCSS/Less files
│   │   └── global.css
│   └── env.d.ts        # TypeScript definitions for Astro environment
├── db/                 # (Optional - Astro DB)
│   └── config.ts       # Database table schema definitions
├── src/actions/        # (Optional - Astro Actions)
│   └── index.ts        # Server action definitions
├── astro.config.mjs    # Astro configuration file
├── package.json        # Project dependencies and scripts
├── tsconfig.json       # TypeScript configuration
└── ...                 # Other config files (tailwind.config.js, etc.)
```

## Key Directories Explained

*   **`public/`**:
    *   Contains static assets that **do not need processing** by Astro's build pipeline.
    *   Files are copied directly to the root of your built site.
    *   Reference files using a root-relative path (e.g., `/favicon.svg`, `/images/logo.png`).
    *   Ideal for: `favicon.ico`, `robots.txt`, fonts, images not needing optimization, manifest files.
*   **`src/`**:
    *   Contains all your source code and content that **will be processed** by Astro.
    *   **`src/assets/`**: Assets (images, CSS, JS) that you want Astro to build, optimize, and bundle. Reference these using relative paths via `import`. Astro handles path resolution and optimization (e.g., image processing).
    *   **`src/components/`**: Reusable UI pieces (`.astro`, `.jsx`, `.vue`, `.svelte`, etc.). These don't become pages themselves but are imported into pages or layouts.
    *   **`src/content/`**: For Astro's Content Collections feature. Store Markdown (`.md`), MDX (`.mdx`), JSON, or YAML files here. Define schemas in `src/content/config.ts` to ensure type safety and structure. Query content using `getCollection()` or `getEntry()`.
    *   **`src/layouts/`**: Special `.astro` components defining the UI structure shared across multiple pages (e.g., header, footer, navigation). Pages use layouts via the `layout` frontmatter property or by importing and wrapping content. Use `<slot />` to indicate where page content should be injected.
    *   **`src/middleware.js` / `.ts`**: (SSR/Edge only) Code that runs on the server for every request, allowing you to intercept and modify request/response data (e.g., authentication, redirects).
    *   **`src/pages/`**: The core of Astro's file-based routing.
        *   Every `.astro`, `.md`, or `.mdx` file in this directory becomes a page on your site based on its file path (e.g., `src/pages/about.astro` -> `/about`).
        *   `index.astro` becomes the root path of its directory (e.g., `src/pages/blog/index.astro` -> `/blog`).
        *   Dynamic routes use brackets: `[param].astro` or `[...rest].astro`. Require `getStaticPaths` for SSG or handle params server-side for SSR.
        *   `.js`/`.ts` files become API endpoints (SSR/Edge only).
    *   **`src/styles/`**: A common convention for storing global CSS files (e.g., `global.css`) imported into layouts or pages.
*   **`db/`**: (Optional) Used by Astro DB. Contains `config.ts` to define database table schemas.
*   **`src/actions/`**: (Optional) Used by Astro Actions. Contains `index.ts` (or similar) to define server-side functions callable from client-side code.

## Configuration

*   **`astro.config.mjs`**: The main configuration file. Define integrations, SSR adapters, build options, site URL, etc.
*   **`tsconfig.json`**: TypeScript configuration, often extended from Astro's base configs.

Understanding this structure helps organize your project logically and leverage Astro's features effectively.

*(Refer to the official Astro Project Structure documentation.)*