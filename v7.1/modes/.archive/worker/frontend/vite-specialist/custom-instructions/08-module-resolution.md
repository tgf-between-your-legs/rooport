# 8. Module Resolution & Aliases

Configuring how Vite finds and resolves module imports.

## Core Concept: Resolving Imports

When you use `import` statements, Vite (like Node.js or other bundlers) needs to figure out where the corresponding file is located. This process involves several steps and configuration options.

**Key Aspects:**

*   **Native ESM:** In development, Vite leverages the browser's native ESM resolution for your source code.
*   **Pre-Bundling:** Dependencies in `node_modules` are pre-bundled into ESM using esbuild, simplifying resolution for common packages. (See `05-dependency-prebundling.md`)
*   **`resolve` Config:** The `resolve` section in `vite.config.js`/`ts` provides options to customize resolution behavior.
*   **Aliases:** Define shortcuts for frequently used import paths.
*   **Extensions:** Specify which file extensions to try when resolving imports without an extension.
*   **`mainFields`:** Control which fields in a package's `package.json` (like `module`, `browser`, `main`) are checked to find the entry point.

## Configuration (`vite.config.js`/`ts`)

Use the `resolve` object within your Vite configuration.

```typescript
// vite.config.ts
import { defineConfig } from 'vite';
import path from 'path'; // Node.js path module

export default defineConfig({
  resolve: {
    // --- Aliases ---
    alias: {
      // Example: '@' pointing to the 'src' directory
      '@': path.resolve(__dirname, './src'),
      // Example: Alias for a specific file
      'config': path.resolve(__dirname, './src/config.ts'),
      // Example: Alias for a package sub-path (useful if deep imports are needed)
      // 'lodash-es': 'lodash-es', // Default behavior
      // Example: Conditional alias (less common)
      // find: /^~(.+)/,
      // replacement: path.resolve(__dirname, 'node_modules/$1'),
    },

    // --- Extensions ---
    // Default: ['.mjs', '.js', '.mts', '.ts', '.jsx', '.tsx', '.json']
    // You might add others if needed, e.g., '.vue', '.svelte' (often handled by plugins)
    // extensions: ['.mjs', '.js', '.ts', '.jsx', '.tsx', '.json', '.vue'],

    // --- Main Fields ---
    // Default: ['browser', 'module', 'jsnext:main', 'jsnext'] for browser environments
    // Controls which fields in package.json are checked for entry points.
    // Rarely needs changing unless dealing with specific package issues.
    // mainFields: ['module', 'main'],

    // --- Conditions ---
    // Default: ['import', 'module', 'browser', 'default', 'require']
    // Used for Conditional Exports in package.json. Rarely needs changing.
    // conditions: ['import', 'require'],

    // --- Deduplication ---
    // If you have multiple versions of the same dependency (e.g., from linked packages),
    // this forces Vite to always resolve listed dependencies to the same copy (the one
    // from the main project's node_modules).
    // dedupe: ['react', 'react-dom'],
  },
  // ... other config
});
```

## Using Aliases

Once defined in `vite.config.js`, you can use aliases in your import statements:

```typescript
// Instead of: import Button from '../../components/ui/Button';
import Button from '@/components/ui/Button'; // Using '@' alias for src

// Instead of: import { API_URL } from '../../config';
import { API_URL } from 'config'; // Using 'config' alias for specific file
```

**TypeScript Integration:** If using TypeScript and path aliases, you also need to configure them in your `tsconfig.json` under `compilerOptions.paths` so that TypeScript understands them during type checking.

```json
// tsconfig.json
{
  "compilerOptions": {
    "baseUrl": ".", // Required for paths
    "paths": {
      "@/*": ["src/*"], // Must match the alias in vite.config.js
      "config": ["src/config.ts"]
    }
    // ... other options
  }
}
```
*Note: The `vite-tsconfig-paths` plugin can often automate reading aliases from `tsconfig.json` into Vite.*

Vite's module resolution generally works well out-of-the-box for standard projects. The most common customization is setting up path aliases using `resolve.alias` (and mirroring them in `tsconfig.json` if using TypeScript) for cleaner import paths.

*(Refer to the official Vite documentation on `resolve` options.)*