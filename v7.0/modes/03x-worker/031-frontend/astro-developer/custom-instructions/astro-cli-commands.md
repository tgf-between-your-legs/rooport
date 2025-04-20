# Common Astro CLI Commands

A quick reference for frequently used Astro CLI commands. Run via `execute_command`.

## Core Development Commands

*   **`npm run dev`** (or `yarn dev`, `pnpm dev`)
    *   Starts the development server, usually on `http://localhost:4321`.
    *   Enables Hot Module Replacement (HMR).
*   **`npm run build`** (or `yarn build`, `pnpm build`)
    *   Builds the site for production (static or SSR based on config).
    *   Output typically goes to the `dist/` directory.
*   **`npm run preview`** (or `yarn preview`, `pnpm preview`)
    *   Starts a local server to preview the production build from `dist/`. Useful for checking SSR output or static files before deployment.

## Adding Integrations (`npx astro add`)

*   **`npx astro add [integration-name]`**
    *   Installs dependencies and configures integrations.
    *   *Examples:*
        *   `npx astro add react`
        *   `npx astro add vue`
        *   `npx astro add svelte`
        *   `npx astro add tailwind`
        *   `npx astro add node` (SSR Adapter)
        *   `npx astro add vercel` (SSR Adapter)
        *   `npx astro add netlify` (SSR Adapter)
        *   `npx astro add cloudflare` (SSR Adapter)
        *   `npx astro add db` (Astro DB)
        *   `npx astro add mdx`

## Astro DB Commands (`npx astro db`)

*Requires Astro DB integration (`npx astro add db`).*

*   **`npx astro db push`**
    *   Applies schema changes defined in `db/config.ts` to the database (local SQLite file during dev, Astro Studio DB in production). Creates tables/columns if they don't exist.
*   **`npx astro db execute <sql-file>`**
    *   Executes SQL commands from a specified file against the database.
*   **`npx astro db seed [--force]`**
    *   Runs seed scripts defined in `db/seed.ts` to populate the database with initial data. `--force` bypasses safety checks.
*   **`npx astro db studio`**
    *   Opens the Astro Studio web interface for managing your remote database (requires login).

## Other Useful Commands

*   **`npx astro check`**
    *   Checks your project for errors and type issues (requires TypeScript setup).
    *   `npx astro check --watch`: Runs in watch mode.
    *   `npx astro check --perf`: Audits component performance for potential bottlenecks.
*   **`npx astro info`**
    *   Displays helpful information about your Astro environment and dependencies.
*   **`npx astro preferences list/get/set/reset`**
    *   Manages Astro user preferences.
*   **`npx astro --help`**
    *   Displays general help and available commands.
*   **`npx astro [command] --help`**
    *   Displays help for a specific command (e.g., `npx astro add --help`).

*(Always refer to the official Astro CLI documentation for the most up-to-date commands and options: https://docs.astro.build/en/reference/cli-reference/)*