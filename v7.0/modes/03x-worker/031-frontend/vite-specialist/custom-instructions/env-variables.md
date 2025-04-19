# Vite: Environment Variables

Managing environment variables for development and production builds in Vite.

## Core Concept

Vite uses `.env` files to load environment variables. It leverages `dotenv` under the hood. Variables prefixed with `VITE_` are exposed to client-side code via `import.meta.env`.

## `.env` Files

Vite loads variables from the following files in your project root, in order of precedence (higher files override lower ones):

1.  `.env`: Loaded in **all** cases.
2.  `.env.local`: Loaded in **all** cases, ignored by git. Use for local overrides, sensitive keys.
3.  `.env.[mode]`: Loaded only in the specified **mode** (e.g., `.env.development`, `.env.production`).
4.  `.env.[mode].local`: Loaded only in the specified **mode**, ignored by git. Use for local overrides specific to a mode.

*   **Mode:** Determined by the command used:
    *   `vite dev` or `vite`: `development` mode by default.
    *   `vite build`: `production` mode by default.
    *   You can override the mode using the `--mode` flag (e.g., `vite build --mode staging`).

**Example Files:**

```bash
# .env (Committed to git)
VITE_APP_TITLE="My Awesome Vite App"
VITE_API_BASE_URL="/api"

# .env.production (Committed to git)
VITE_API_BASE_URL="https://api.prod.example.com"

# .env.local (Ignored by git)
# Overrides for local development, potentially sensitive keys
VITE_API_KEY="local-dev-key-123"
DB_PASSWORD="local-db-password" # Not prefixed, only available server-side

# .env.staging (Committed to git)
VITE_APP_TITLE="My App (Staging)"
VITE_API_BASE_URL="https://api.staging.example.com"
```

## Accessing Env Variables

*   **Client-Side Code (`import.meta.env`):**
    *   Only variables prefixed with `VITE_` are exposed to client-side code (processed by Vite).
    *   Access them via the special `import.meta.env` object.
    *   These variables are **statically replaced** during the build process. Never destructure `import.meta.env`.
    ```javascript
    // src/config.ts
    console.log('App Title:', import.meta.env.VITE_APP_TITLE);
    console.log('API Base URL:', import.meta.env.VITE_API_BASE_URL);
    // console.log('DB Password:', import.meta.env.DB_PASSWORD); // Error: Property 'DB_PASSWORD' does not exist. Not exposed to client.

    // Incorrect: Do not destructure
    // const { VITE_APP_TITLE } = import.meta.env;

    // Access dynamically (use with caution, might hinder static analysis)
    console.log('API Key:', import.meta.env['VITE_API_KEY']);
    ```
*   **Server-Side Code (e.g., `vite.config.js`, SSR):**
    *   Vite loads `.env` files using `dotenv`. You can access **all** variables (including those without the `VITE_` prefix) via `process.env`.
    *   You might need to install `dotenv` (`npm i -D dotenv`) and load it manually in files *not* processed by Vite if needed (less common).
    ```javascript
    // vite.config.ts (Example accessing non-prefixed var)
    import { defineConfig, loadEnv } from 'vite';

    export default defineConfig(({ command, mode }) => {
      // Load env file based on mode in current working directory.
      // process.cwd() is default 3rd param
      const env = loadEnv(mode, process.cwd(), ''); // Load all vars, not just VITE_

      console.log('DB Password (in config):', env.DB_PASSWORD); // Access non-prefixed var

      return {
        // define: {
        //   // Manually define global constants (use with caution)
        //   __APP_VERSION__: JSON.stringify(process.env.npm_package_version),
        // },
        // ... other config
      };
    });
    ```

## Security

*   **NEVER** commit sensitive keys (API secrets, passwords) directly into `.env` or `.env.[mode]` files that are tracked by git.
*   Use `.env.local` or `.env.[mode].local` (which should be in your `.gitignore`) for sensitive local development keys.
*   For production/staging environments, use the hosting provider's environment variable management system (e.g., Vercel Environment Variables, Netlify Build Environment Variables, Docker secrets). Do not commit production secrets to your repository.
*   Be extremely careful about which variables you expose to the client using the `VITE_` prefix. **Only expose public keys or non-sensitive configuration.**

## Typing `import.meta.env` (TypeScript)

You can provide type definitions for your `VITE_` prefixed variables:

```typescript
// src/vite-env.d.ts (or other .d.ts file included by tsconfig)

/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_APP_TITLE: string;
  readonly VITE_API_BASE_URL: string;
  // Add other VITE_ variables here
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}
```

*(Refer to the official Vite Env Variables documentation: https://vitejs.dev/guide/env-and-mode.html)*