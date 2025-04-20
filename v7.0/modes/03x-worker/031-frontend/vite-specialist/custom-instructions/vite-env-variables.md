# Vite: Environment Variables

Managing environment variables for different modes (development, production) and accessing them in your code.

## Core Concept: Mode-Based `.env` Files

Vite uses `dotenv` to load environment variables from `.env` files in your project root directory. It supports different files based on the current **mode** Vite is running in (usually `development` for `vite dev` and `production` for `vite build`).

**File Loading Order (Higher precedence overrides lower):**

1.  `.env.[mode].local`: Local overrides for a specific mode (e.g., `.env.development.local`). **Git ignored by default.**
2.  `.env.[mode]`: Mode-specific settings (e.g., `.env.development`, `.env.production`). Can be committed to Git.
3.  `.env.local`: Local overrides, applied to all modes. **Git ignored by default.**
4.  `.env`: Default values, applied to all modes. Can be committed to Git.

**Mode:**

*   Determined by the `--mode` command line flag (e.g., `vite build --mode staging`).
*   Defaults to `'development'` for `vite dev` / `vite`.
*   Defaults to `'production'` for `vite build`.

## Accessing Environment Variables

Vite exposes environment variables to your code through different mechanisms:

**1. Client-Side Source Code (`import.meta.env`):**

*   **Prefix Required:** Only variables prefixed with `VITE_` are exposed to your client-side source code (e.g., in `.js`, `.ts`, `.vue`, `.svelte` files). This prevents accidentally leaking sensitive server-side keys to the browser.
*   **Access:** Use the special `import.meta.env` object.
    ```javascript
    // Example: Accessing VITE_API_URL defined in an .env file
    console.log('API URL:', import.meta.env.VITE_API_URL);
    // Built-in variables provided by Vite:
    console.log('Base URL:', import.meta.env.BASE_URL); // The base public path the app is served from.
    console.log('Mode:', import.meta.env.MODE); // The mode the app is running in ('development' or 'production').
    console.log('Dev:', import.meta.env.DEV); // boolean; true when running in development.
    console.log('Prod:', import.meta.env.PROD); // boolean; true when running production build.
    console.log('SSR:', import.meta.env.SSR); // boolean; true when running server-side rendering.
    ```
*   **Static Replacement:** Vite performs static replacement during the build. `import.meta.env.VITE_SOME_KEY` is replaced directly with the value `"your_value"`. You cannot dynamically access keys like `import.meta.env[key]`.

**2. Server-Side Code (e.g., `vite.config.js`, SSR):**

*   Vite **does not** automatically expose *all* variables loaded from `.env` files directly via `process.env` in the config file or during SSR by default, to avoid conflicts.
*   **Use `loadEnv`:** Import the `loadEnv` helper from Vite in `vite.config.js` or server-side code to explicitly load variables for the current mode.
    ```typescript
    // vite.config.ts
    import { defineConfig, loadEnv } from 'vite';

    export default defineConfig(({ mode }) => {
      // Load env variables for the current mode from process.cwd()
      // Use '' as the third argument to load all variables, not just VITE_ prefixed ones.
      const env = loadEnv(mode, process.cwd(), '');

      console.log('Server-side access to DATABASE_URL:', env.DATABASE_URL); // Access non-prefixed var

      return {
        // Example: Define a global constant based on an env var
        // Use with caution, prefer exposing via server endpoints if possible
        define: {
          __APP_VERSION__: JSON.stringify(env.APP_VERSION || 'unknown')
        }
        // other config options...
      };
    });
    ```
*   **SSR:** Variables loaded via `loadEnv` in `vite.config.js` are *not* automatically passed to the SSR context. You typically need to pass necessary configuration from your server entry point or use framework-specific mechanisms (like SvelteKit's `event.locals` populated via hooks). Variables prefixed with `VITE_` *are* available via `import.meta.env` during SSR, just like on the client.

## Security

*   **Never commit `.env*.local` files to Git.** These are for local overrides and may contain sensitive credentials.
*   **Only use the `VITE_` prefix for variables that are safe to expose in your client-side browser bundle.** Do not put API secrets, database passwords, etc., in variables prefixed with `VITE_`.
*   Keep sensitive keys in `.env` files *without* the `VITE_` prefix and access them only in server-side code (e.g., server `load` functions, `actions`, API endpoints) using `loadEnv` or platform-specific environment variable access (`process.env` in Node, context in serverless/edge).

Vite's `.env` file handling provides a flexible way to manage configuration for different environments. Remember the `VITE_` prefix rule for client-side exposure and use `loadEnv` for accessing non-prefixed variables server-side.

*(Refer to the official Vite documentation on Env Variables and Modes.)*