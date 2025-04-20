# Vite: Migrating from Other Build Tools

Tips and considerations when migrating a project from Webpack, Parcel, or Create React App (CRA) to Vite.

## Core Concept: Shifting Build Philosophy

Migrating to Vite often involves adapting to its different development philosophy (Native ESM dev server) and build configuration (Rollup-based).

**Key Differences to Consider:**

*   **Dev Server:** Vite serves source code via native ESM, unlike Webpack/Parcel which bundle everything first. This leads to faster startup but requires code to be largely ESM-compatible.
*   **Build Tool:** Vite uses Rollup for production builds, while CRA/Webpack use Webpack. Configuration syntax and plugin ecosystems differ.
*   **HTML Entry Point:** Vite treats `index.html` as the primary entry point, discovering dependencies from script tags and imports, whereas Webpack often starts from a JS entry point.
*   **Module Resolution:** While similar (Node.js resolution), specific alias configurations or non-standard resolutions might need adjustment.
*   **Asset Handling:** Vite's `public` directory and import-based asset handling differ from Webpack's loaders or Parcel's zero-config approach.
*   **Environment Variables:** Vite uses `import.meta.env` and the `VITE_` prefix for client-side exposure, differing from CRA's `REACT_APP_` or Webpack's `DefinePlugin`.
*   **CommonJS Dependencies:** Vite's pre-bundling handles most CJS dependencies, but complex cases might require adjustments.
*   **Node.js Polyfills:** Vite does *not* automatically polyfill Node.js core modules for the browser like older CRA/Webpack versions did. You'll need to explicitly add polyfills if your code relies on them (e.g., `buffer`, `process`).

## General Migration Steps

1.  **Install Vite & Dependencies:**
    ```bash
    npm install -D vite @vitejs/plugin-react # or other framework plugin
    # or
    yarn add -D vite @vitejs/plugin-react
    ```
2.  **Create `vite.config.js`/`ts`:** Start with a basic configuration, including the necessary framework plugin (e.g., `@vitejs/plugin-react`).
3.  **Move `index.html`:** Move your main HTML file to the project root (or configure `root` and `build.outDir` if keeping it elsewhere). Ensure it includes `<script type="module" src="/src/main.jsx"></script>` (or your main JS/TS entry point).
4.  **Update `package.json` Scripts:** Change `dev`/`start` script to `vite` and `build` script to `vite build`. Add a `preview` script: `vite preview`.
5.  **Environment Variables:**
    *   Rename client-exposed variables (e.g., `REACT_APP_...`) to use the `VITE_` prefix.
    *   Update code to access them via `import.meta.env.VITE_...` instead of `process.env.REACT_APP_...`.
    *   For variables used only server-side or during build, plan to use `loadEnv` in `vite.config.js` or handle them via your server setup.
6.  **Asset Handling:**
    *   Move assets intended to be served as-is (favicon, robots.txt) to the `public` directory and update references to use absolute paths (e.g., `/favicon.ico`).
    *   Update JavaScript/CSS code to `import` assets like images/fonts directly to get their resolved URLs. Replace Webpack loader syntax or hardcoded paths.
7.  **Module Resolution & Aliases:**
    *   Replicate any necessary path aliases from Webpack (`resolve.alias`) or `jsconfig.json`/`tsconfig.json` (`paths`) into `vite.config.js`'s `resolve.alias` section.
    *   Ensure corresponding `paths` are also in `tsconfig.json` if using TypeScript.
8.  **CSS:**
    *   Vite supports CSS Modules (`.module.css`), PostCSS (install `autoprefixer` and configure `postcss.config.js`), and CSS preprocessors (install the preprocessor, e.g., `npm i -D sass`). Imports usually work out-of-the-box.
    *   Remove Webpack-specific CSS loader syntax.
9.  **SVGs:** If using SVGs as React components (common in CRA), install and configure `vite-plugin-svgr`.
10. **Node.js Polyfills:** If your code relies on Node.js built-ins (like `Buffer`, `process`), explicitly install polyfills (e.g., using `vite-plugin-node-polyfills` or manual polyfills via aliases).
11. **CommonJS Issues:** If the dev server fails due to a CommonJS dependency, try adding it to `optimizeDeps.include`. Check if an ESM version of the dependency exists.
12. **Test Thoroughly:** Run the dev server (`vite`), test HMR, run the production build (`vite build`), and preview (`vite preview`). Check for runtime errors, missing assets, or incorrect environment variables.

Migration can range from straightforward to complex depending on the project's setup. Start with the basic config, address environment variables and asset handling, configure aliases, and then iteratively fix issues reported by the dev server or build process, consulting Vite's documentation frequently.

*(Refer to the official Vite documentation on Migration from v2 and specific framework guides.)*