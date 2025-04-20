# Astro: Common CLI Commands

A quick reference for frequently used Astro CLI commands. Run via `execute_command`.

## Core Development Commands

*   **`npm run dev`** (or `yarn dev`, `pnpm dev`)
    *   Starts the development server (usually `http://localhost:4321`) with HMR.
*   **`npm run build`** (or `yarn build`, `pnpm build`)
    *   Builds the site for production (`dist/` directory).
*   **`npm run preview`** (or `yarn preview`, `pnpm preview`)
    *   Previews the production build locally.

## Adding Integrations (`npx astro add`)

*   **`npx astro add [integration-name]`**
    *   Installs and configures integrations (e.g., `react`, `vue`, `svelte`, `tailwind`, `node`, `vercel`, `netlify`, `cloudflare`, `db`, `mdx`).

## Astro DB Commands (`npx astro db`)

*Requires `npx astro add db`.*

*   **`npx astro db push`**
    *   Applies schema changes from `db/config.ts` to the database.
*   **`npx astro db execute <sql-file>`**
    *   Executes SQL commands from a file.
*   **`npx astro db seed [--force]`**
    *   Runs seed scripts from `db/seed.ts`.
*   **`npx astro db studio`**
    *   Opens the Astro Studio web interface (requires login).

## Other Useful Commands

*   **`npx astro check`**
    *   Checks for errors and type issues.
    *   `--watch`: Runs in watch mode.
    *   `--perf`: Audits component performance.
*   **`npx astro info`**
    *   Displays environment information.
*   **`npx astro preferences list/get/set/reset`**
    *   Manages user preferences.
*   **`npx astro --help`**
    *   Displays general help.
*   **`npx astro [command] --help`**
    *   Displays help for a specific command.

*(Always refer to the official Astro CLI documentation: https://docs.astro.build/en/reference/cli-reference/)*