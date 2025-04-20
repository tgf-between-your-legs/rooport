# SvelteKit Dev: Adapters & Deployment

Adapters configure the output of `npm run build` to suit specific deployment platforms.

## 1. Core Concept

*   **Build Output:** `npm run build` creates a generic production version of your app.
*   **Adapter Role:** An adapter (configured in `svelte.config.js`) runs *after* the build, transforming the output for a target environment (Node.js, serverless, static host, etc.).
*   **Installation:** Adapters are npm packages (e.g., `@sveltejs/adapter-node`).

## 2. Common Adapters

**a) `@sveltejs/adapter-auto`**

*   **Default:** Tries to auto-detect the platform (Vercel, Netlify, Cloudflare Pages) during build and uses the appropriate adapter. Convenient for common platforms.

**b) `@sveltejs/adapter-node`**

*   **Target:** Standalone Node.js servers (VPS, Docker, traditional hosting).
*   **Output:** Creates a Node server entry point (e.g., `build/index.js`).
*   **Run:** `npm run build && node build`
*   **Config:**
    ```javascript
    // svelte.config.js
    import adapter from '@sveltejs/adapter-node';
    const config = { kit: { adapter: adapter({ out: 'build' }) } };
    export default config;
    ```

**c) `@sveltejs/adapter-static`**

*   **Target:** Static hosting (GitHub Pages, Netlify Drop, S3).
*   **Output:** Pre-renders pages into static HTML, CSS, JS.
*   **Limitations:** Cannot use SSR features (server `load`, `actions`, `+server.js`). Requires routes to be pre-renderable (configure `prerender` option in `svelte.config.js` or export `prerender = true` in routes). Needs a fallback page (`index.html` for SPA, `404.html`).
*   **Config:**
    ```javascript
    // svelte.config.js
    import adapter from '@sveltejs/adapter-static';
    const config = {
      kit: {
        adapter: adapter({
          pages: 'build',
          assets: 'build',
          fallback: 'index.html', // or '404.html'
          precompress: false
        }),
        // Ensure pages are prerenderable if using server-only features elsewhere
        // prerender: { entries: ['*'] } // Example: prerender all pages
      }
    };
    export default config;
    ```

**d) `@sveltejs/adapter-vercel`**

*   **Target:** Vercel platform (Serverless/Edge Functions).
*   **Behavior:** Optimizes output for Vercel. Server `load`/`actions`/`+server.js` become Serverless Functions. Hooks often run as Edge Functions. Often handled by `adapter-auto`.
*   **Config:**
    ```javascript
    // svelte.config.js
    import adapter from '@sveltejs/adapter-vercel';
    const config = { kit: { adapter: adapter({ runtime: 'edge' }) } }; // Optional: specify runtime
    export default config;
    ```

**e) Others:** `adapter-netlify`, `adapter-cloudflare`, `adapter-aws`, etc., exist for specific platforms.

## 3. Build & Deployment Process

1.  **Install Adapter:** `npm install -D @sveltejs/adapter-[name]` (if not using `adapter-auto`).
2.  **Configure:** Set `kit.adapter` in `svelte.config.js`.
3.  **Build:** Run `npm run build`. This executes Vite builds and then the adapter.
4.  **Deploy:** Upload the adapter's output directory (e.g., `build`, `.vercel/output`, etc.) to the hosting platform or configure Git integration.

**Choosing:** Use `adapter-auto` for simplicity on common platforms. Use specific adapters for more control, less common platforms, or specific features (like Node server or static export).