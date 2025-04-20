# Directus: Extensions SDK Overview

Extending Directus functionality with custom code using the Node.js/TypeScript SDK.

## Core Concept

Directus allows you to extend its core functionality by creating custom extensions. These extensions are typically written in TypeScript (or JavaScript) using the Directus Extension SDK and run within the Directus Node.js environment.

## Extension Types

Directus supports several types of extensions:

1.  **Hooks:**
    *   **Purpose:** Run custom logic before or after specific events occur within Directus (e.g., before creating an item, after user login, on a schedule).
    *   **Types:**
        *   **Action Hooks:** Triggered by specific actions (e.g., `items.create`, `items.update`, `auth.login`). Run once per trigger.
        *   **Filter Hooks:** Modify data during an action (e.g., change payload before saving `items.create.before`, modify response after reading `items.read.after`). Run potentially multiple times.
        *   **Init Hooks:** Run during Directus initialization (e.g., `routes.register`).
        *   **Schedule Hooks:** Run on a cron schedule.
    *   **Location:** `directus/extensions/hooks/{hook-name}/index.js`
2.  **Endpoints:**
    *   **Purpose:** Create custom API endpoints within your Directus instance for specialized logic not covered by the standard CRUD API.
    *   **Mechanism:** Define routes (e.g., `/custom/my-endpoint`) and handlers (functions) that receive request and response objects (often using an Express-like syntax).
    *   **Location:** `directus/extensions/endpoints/{endpoint-name}/index.js`
3.  **App Extensions (Frontend):** These extend the Directus Admin App UI.
    *   **Interfaces:** Custom input components for fields in the data model (e.g., a map selector, a custom markdown editor).
    *   **Displays:** Custom ways to render field data in the item listing/detail pages.
    *   **Layouts:** Custom views for browsing collection items (e.g., calendar layout, map layout).
    *   **Modules:** Custom full-page sections within the Admin App for dashboards, reports, or specific workflows.
    *   **Location:** `directus/extensions/{type}/{extension-name}/` (e.g., `interfaces/my-custom-input/`) - Typically built using Vue.js.

## Development Setup

1.  **Project Structure:** Create an `extensions` directory in your Directus project root. Inside, create subdirectories for each extension type (e.g., `hooks`, `endpoints`, `interfaces`).
    ```
    your-directus-project/
    ├── docker-compose.yml
    ├── .env
    ├── database/
    ├── uploads/
    └── extensions/
        ├── hooks/
        │   └── my-validation-hook/
        │       ├── index.js
        │       └── package.json
        ├── endpoints/
        │   └── custom-report/
        │       ├── index.js
        │       └── package.json
        └── interfaces/
            └── custom-map-input/
                ├── index.js # Entry point for app extension build
                ├── package.json
                └── src/ # Vue component source
                    └── interface.vue
    ```
2.  **Extension SDK:** Use the utilities and types provided by the Directus SDK (`@directus/extensions-sdk` is often implicitly available or managed via tooling).
3.  **Build Process (App Extensions):** App extensions (Interfaces, Displays, Layouts, Modules) typically require a build step (using `directus-extension build`) to bundle the Vue.js code. API extensions (Hooks, Endpoints) written in JS/TS usually don't require a separate build step unless using complex TS features not directly supported by Node.js runtime.
4.  **`package.json`:** Each extension should have its own `package.json` specifying its type and entry point using the `directus:extension` block.
    ```json
    // extensions/hooks/my-validation-hook/package.json
    {
      "name": "directus-extension-my-validation-hook",
      "version": "1.0.0",
      "type": "module", // Use ES Modules
      "directus:extension": {
        "type": "hook",
        "entrypoint": "index.js", // Your hook's main file
        "host": "^10.8.0" // Compatible Directus version
      },
      "dependencies": {
        // Add any specific dependencies here
      }
    }
    ```
    ```json
    // extensions/interfaces/custom-map-input/package.json
    {
      "name": "directus-extension-custom-map-input",
      "version": "1.0.0",
      "type": "module",
      "directus:extension": {
        "type": "interface",
        "path": "dist/index.js", // Output from build step
        "source": "src/index.ts", // Source entry point for build
        "host": "^10.8.0"
      },
      "scripts": {
        "build": "directus-extension build"
      },
      "devDependencies": {
        "@directus/extensions-sdk": "^11.0.0",
        "vue": "^3.3.0",
        // ... other build dependencies
      }
    }
    ```
5.  **Loading:** Directus automatically discovers and loads extensions placed in the `extensions` directory on startup.

## Key SDK Concepts (API Extensions)

*   **Registering Logic:** Use functions provided by the SDK (often exported by your `index.js`) to register hooks or endpoints.
*   **Hook Functions:** Receive context-specific arguments (e.g., `payload`, `meta`, `schema`, `services`). Filter hooks allow modifying the `payload`. Action hooks perform side effects.
*   **Endpoint Handlers:** Receive `req` and `res` objects (similar to Express) and access Directus services via context.
*   **Services:** Access core Directus functionalities (e.g., `ItemsService`, `UsersService`, `MailService`) via the context passed to hooks or handlers to interact with data, send emails, etc.
*   **Database Access:** Use the `database` instance (Knex.js query builder) available in the context for direct SQL queries if needed (use `ItemsService` where possible).

Developing extensions allows tailoring Directus precisely to specific project needs.

*(Refer to the official Directus Extensions documentation: https://docs.directus.io/extensions/introduction.html)*