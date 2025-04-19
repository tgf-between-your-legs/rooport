# Vite: Migration Tips (from Webpack/CRA/etc.)

Guidance on migrating existing projects from other build tools (like Webpack, Create React App) to Vite.

## Why Migrate to Vite?

*   **Faster Dev Server:** Significantly quicker cold starts and HMR due to native ESM approach.
*   **Simpler Configuration:** Often less complex configuration compared to Webpack.
*   **Modern Tooling:** Built on modern standards like native ESM and esbuild.

## General Migration Strategy

1.  **Understand Vite Concepts:** Familiarize yourself with Vite's core ideas: native ESM dev server, Rollup for production builds, `index.html` as the entry point, plugin system, `import.meta.env`.
2.  **Setup Vite:**
    *   Install Vite and relevant framework plugins (`@vitejs/plugin-react`, `@vitejs/plugin-vue`, etc.) as dev dependencies.
    *   Create a basic `vite.config.js` or `vite.config.ts`.
    *   Create an `index.html` file at the project root (or configure `root` and `build.outDir` if your `index.html` is elsewhere, e.g., in `public`). This `index.html` should include `<script type="module" src="/src/main.jsx"></script>` (adjust path to your main entry point).
3.  **Update `package.json` Scripts:** Change `dev`/`start` scripts to use `vite` and `build` script to use `vite build`. Add a `preview` script using `vite preview`.
4.  **Handle HTML Entry Point:**
    *   Move your main HTML file (`public/index.html` in CRA) to the project root (or configure Vite's `root`).
    *   Replace Webpack/CRA specific placeholders (like `%PUBLIC_URL%`) with standard paths (e.g., `/favicon.ico` for assets in the `public` directory).
    *   Ensure your main JavaScript entry point is loaded via `<script type="module" src="...">`.
5.  **Environment Variables:**
    *   Rename client-side environment variables to have the `VITE_` prefix (e.g., `REACT_APP_API_KEY` becomes `VITE_API_KEY`).
    *   Update code to access client-side variables via `import.meta.env.VITE_...` instead of `process.env...`.
    *   Server-side variables (used in Node.js context like SSR) can still be accessed via `process.env` (Vite loads `.env` files using `dotenv`).
6.  **Module Resolution & Aliases:**
    *   If using path aliases (e.g., `@/components`), configure them in `vite.config.js` under `resolve.alias`. Install `vite-tsconfig-paths` if using `tsconfig.json` paths.
    *   Vite uses native ESM resolution. Issues might arise with dependencies relying heavily on Node.js built-ins or specific Webpack features.
7.  **Plugin Equivalents:**
    *   Identify Webpack loaders/plugins used in your old config.
    *   Find equivalent Vite or Rollup plugins (check Awesome Vite). Common replacements:
        *   `babel-loader` -> Often not needed if targeting modern browsers; use `@vitejs/plugin-react` (includes Babel) or `@vitejs/plugin-legacy` if necessary.
        *   `css-loader`/`style-loader` -> Built into Vite.
        *   `file-loader`/`url-loader` -> Built into Vite (asset handling).
        *   `html-webpack-plugin` -> Handled by Vite's `index.html` entry point.
        *   `DefinePlugin` -> Use `define` in `vite.config.js` or environment variables.
        *   SVG Loaders -> Use plugins like `vite-plugin-svgr`.
8.  **CSS Handling:**
    *   Vite supports CSS preprocessors (Sass, Less, Stylus) out-of-the-box (just install the preprocessor).
    *   CSS Modules (`.module.css`) work automatically.
    *   PostCSS is supported (configure `postcss.config.js`).
9.  **Global Imports/Polyfills:**
    *   Avoid relying on Webpack's automatic polyfills for Node.js built-ins if possible. Find browser-compatible alternatives or use specific polyfill plugins if absolutely necessary.
    *   Global styles should be imported in your main entry point (`main.ts`/`js`).
10. **Testing:** Run `vite dev` and `vite build` + `vite preview`. Test thoroughly to catch issues related to module resolution, environment variables, asset handling, or plugin differences.

## Framework-Specific Notes

*   **Create React App (CRA):** Follow guides specifically for migrating CRA to Vite. Key points are `index.html` handling, environment variables (`REACT_APP_` -> `VITE_`), and replacing `react-scripts` with Vite commands and `@vitejs/plugin-react`. SVGR handling might need `vite-plugin-svgr`.
*   **Vue CLI:** Similar process. Replace `vue-cli-service` with Vite commands and `@vitejs/plugin-vue`. Adjust `public/index.html` and environment variables.
*   **Next.js:** Migrating from Next.js to Vite is less common as Next.js provides its own integrated tooling (often Turbopack or Webpack). Vite is sometimes used *within* Next.js via plugins, but a full migration replaces Next.js's routing and server capabilities.

## Common Issues

*   **`process is not defined` / `global is not defined`:** Code relying on Node.js globals in client-side code. Find browser alternatives or configure `define` in Vite config (less ideal).
*   **Dependency Issues:** CommonJS dependencies not converting well, or dependencies relying on Node built-ins. Try adding to `optimizeDeps.include` or check for ESM-compatible versions.
*   **Asset Paths:** Incorrect paths to assets in `public` directory or imported assets. Use absolute paths (`/image.png`) for assets in `public`. Imported assets get hashed URLs.
*   **Environment Variables:** Forgetting the `VITE_` prefix for client-side vars or accessing them incorrectly via `process.env`.

Migration can be complex depending on the project's setup. Proceed incrementally and test frequently.

*(Refer to the official Vite Migration Guide: https://vitejs.dev/guide/migration.html)*