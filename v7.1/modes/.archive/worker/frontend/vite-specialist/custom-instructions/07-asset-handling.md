# 7. Asset Handling

How Vite handles static assets like images, fonts, JSON, and WebAssembly.

## Core Concept: Automatic Handling & Public Directory

Vite aims to simplify asset handling compared to traditional bundlers.

**Key Mechanisms:**

1.  **Referencing Assets in Code (`import`):**
    *   When you `import` a static asset (e.g., `import imgUrl from './image.png'`), Vite includes it in the build graph.
    *   During the build, the asset is processed (hashed filename for caching) and copied to the output directory (`dist/assets` by default).
    *   The `import` returns the **resolved public URL** of the asset after processing. This URL can be used directly in `src` attributes, CSS `url()`, etc.
    *   Works for common image, media, and font types. Also supports JSON (`import data from './data.json'`) and WebAssembly (`import init from './wasm.wasm?init'`).
2.  **The `public` Directory:**
    *   Assets placed in the `public` directory (at the project root) are **served directly at the root path (`/`)** during development and **copied as-is** to the root of the build output directory (`dist`) during build.
    *   **Use Cases:** Files that must retain their exact filename (e.g., `robots.txt`, favicons), assets that are never directly referenced in source code, or very large assets you don't want processed by the build.
    *   **Referencing:** Reference these assets using **absolute paths** starting from the root (e.g., `/favicon.ico`, `/images/logo.png`).
3.  **`base` Option (`vite.config.js`):**
    *   If your application is deployed under a nested public path (e.g., `https://example.com/my-app/`), set the `base` option in `vite.config.js` to `'/my-app/'`.
    *   Vite automatically prepends this base path to resolved asset URLs from imports and adjusts paths in generated HTML/CSS.
    *   References to assets in the `public` directory need to manually account for the base path if necessary (or use relative paths carefully).

## Implementation Examples

**1. Importing Assets:**

```javascript
// src/MyComponent.jsx
import React from 'react';
import logoUrl from './logo.svg'; // Vite returns the resolved URL
import data from '../data/config.json'; // JSON is parsed automatically
// import initWasm from './logic.wasm?init'; // Example WASM import

function MyComponent() {
  // Example WASM usage (requires async handling)
  // const [wasmInstance, setWasmInstance] = React.useState(null);
  // React.useEffect(() => {
  //   initWasm().then(instance => setWasmInstance(instance));
  // }, []);

  return (
    <div>
      {/* Use the imported URL directly */}
      <img src={logoUrl} alt="App Logo" width="50" />
      <p>Config Value: {data.setting}</p>
      {/* wasmInstance && <p>WASM Result: {wasmInstance.exports.add(2, 3)}</p> */}
    </div>
  );
}

export default MyComponent;
```

```css
/* src/styles.css */
.hero {
  /* Vite resolves the URL during build */
  background-image: url('../assets/background.jpg');
}
```

**2. Using the `public` Directory:**

*   Place `favicon.ico` in `public/favicon.ico`. Reference in HTML as `<link rel="icon" href="/favicon.ico">`.
*   Place `logo.png` in `public/images/logo.png`. Reference in HTML as `<img src="/images/logo.png">`.
*   Place `robots.txt` in `public/robots.txt`. It will be available at `/robots.txt`.

**3. Setting the `base` Option:**

```javascript
// vite.config.js
import { defineConfig } from 'vite';

export default defineConfig({
  base: '/my-nested-app/', // Deploying to example.com/my-nested-app/
  // ... other config
});
```
*   Now, `import logoUrl from './logo.svg'` might resolve to `/my-nested-app/assets/logo.f3a4b5.svg`.
*   An image in `public/images/banner.jpg` should be referenced as `<img src="/my-nested-app/images/banner.jpg">` (or configure your server to handle the base path).

## URL Handling (`new URL(url, import.meta.url)`)

For more complex scenarios, especially in libraries or web workers, you can use the standard `new URL(assetPath, import.meta.url)` pattern to resolve asset URLs relative to the current module. Vite detects this pattern and ensures the asset is included in the build and the path is correctly resolved.

```javascript
// src/worker.js
// Resolve the path to 'image.png' relative to the worker script
const imageUrl = new URL('./image.png', import.meta.url).href;
// Use imageUrl...
console.log('Image URL in worker:', imageUrl);
```

Vite simplifies asset handling by resolving imported assets to their final public URLs and providing the `public` directory for assets that need fixed paths or shouldn't be processed. Remember to configure the `base` option if deploying to a sub-path.

*(Refer to the official Vite documentation on Asset Handling.)*