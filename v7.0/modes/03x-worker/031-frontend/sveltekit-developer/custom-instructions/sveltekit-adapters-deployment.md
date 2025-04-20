# SvelteKit: Adapters & Deployment

Configuring SvelteKit applications for deployment to different platforms using adapters.

## Core Concept: Adapters

SvelteKit applications can be deployed to various hosting platforms (Node.js servers, serverless functions, static hosts, edge functions). **Adapters** are small plugins that take the output of `svelte-kit build` and transform it into the specific format required by a target deployment environment.

**Key Points:**

*   **Build Output:** `npm run build` (which runs `vite build && vite build --ssr` if using Vite) generates a generic production-ready version of your app.
*   **Adapter Role:** The configured adapter runs *after* the build, tailoring the output for a specific platform (e.g., creating a Node server entry point, generating serverless function handlers, creating static HTML files).
*   **Configuration:** Adapters are configured in the `kit.adapter` property within `svelte.config.js`.
*   **Installation:** Each adapter is typically a separate npm package (e.g., `@sveltejs/adapter-node`, `@sveltejs/adapter-vercel`).

## Common Adapters

1.  **`@sveltejs/adapter-auto`:**
    *   **Default:** The default adapter when creating a new SvelteKit project.
    *   **Behavior:** Attempts to automatically detect the deployment environment (Vercel, Netlify, Cloudflare Pages, etc.) during the build process (`npm run build`) and installs/configures the appropriate adapter dynamically.
    *   **Use Case:** Convenient for common platforms, especially during development or for simple deployments. May need to switch to a specific adapter for more control or less common platforms.

2.  **`@sveltejs/adapter-node`:**
    *   **Target:** Standalone Node.js servers.
    *   **Output:** Creates a Node.js server entry point (e.g., `build/index.js`) that can be run using `node build`.
    *   **Use Case:** Deploying to traditional Node hosting, VPS, Docker containers.
    *   **Configuration:**
        ```javascript
        // svelte.config.js
        import adapter from '@sveltejs/adapter-node';
        // ... other imports

        /** @type {import('@sveltejs/kit').Config} */
        const config = {
          // ... kit options
          kit: {
            adapter: adapter({
              // Options: output directory, precompress assets, etc.
              // out: 'build' // Default
            })
          }
        };
        export default config;
        ```
    *   **Running:** `npm run build && node build`

3.  **`@sveltejs/adapter-static`:**
    *   **Target:** Static file hosting (no server needed).
    *   **Output:** Pre-renders all specified pages into HTML, CSS, and JS files.
    *   **Use Case:** Deploying to platforms like GitHub Pages, Netlify Drop, basic S3 hosting.
    *   **Limitations:** Cannot use server-side rendering (SSR), server `load` functions, `actions`, or `+server.js` endpoints. Requires all routes to be pre-renderable. May need `prerender = true` export in routes or global config. Requires fallback page configuration (e.g., `fallback: '404.html'` or `fallback: 'index.html'` for SPAs).
    *   **Configuration:**
        ```javascript
        // svelte.config.js
        import adapter from '@sveltejs/adapter-static';
        // ... other imports

        /** @type {import('@sveltejs/kit').Config} */
        const config = {
          kit: {
            adapter: adapter({
              pages: 'build', // Output directory for HTML files
              assets: 'build', // Output directory for assets
              fallback: 'index.html', // SPA mode fallback
              // fallback: '404.html', // Traditional fallback
              precompress: false // Optional: precompress assets
            }),
            // Required for adapter-static if not all pages are pre-renderable by default
            // prerender: {
            //   entries: ['*', '/specific-page'] // Specify entries to prerender
            // }
          }
        };
        export default config;
        ```

4.  **`@sveltejs/adapter-vercel`:**
    *   **Target:** Vercel platform (Serverless Functions, Edge Functions).
    *   **Behavior:** Automatically configures output for Vercel's infrastructure. Server `load`, `actions`, and `+server.js` become Serverless Functions. Hooks (`handle`) run as Edge Functions.
    *   **Use Case:** Recommended adapter for deploying to Vercel. Often used automatically by `adapter-auto`.
    *   **Configuration:**
        ```javascript
        // svelte.config.js
        import adapter from '@sveltejs/adapter-vercel';
        // ... other imports

        /** @type {import('@sveltejs/kit').Config} */
        const config = {
          kit: {
            adapter: adapter({
              // Options: edge runtime, split functions, etc.
              // runtime: 'edge' // Optional: deploy serverless functions to edge
            })
          }
        };
        export default config;
        ```

5.  **Other Adapters:** `adapter-netlify`, `adapter-cloudflare`, `adapter-cloudflare-workers`, `adapter-aws`, etc., available for specific platforms.

## Build Process

1.  **`npm run build` (or equivalent):**
    *   Runs the SvelteKit build process (using Vite by default).
    *   Generates client-side assets (JS, CSS) and server-side code.
    *   Runs the configured adapter to transform the build output for the target platform.
2.  **Deployment:** Upload the adapter's output directory (e.g., `build`, `.vercel/output`) to the hosting platform, or configure the platform's Git integration to run the build command automatically.

Choose the adapter that matches your deployment target. `adapter-auto` is convenient for common platforms, while specific adapters offer more control for Node servers, static hosts, or specific cloud providers.

*(Refer to the official SvelteKit documentation on Adapters and Deployment.)*