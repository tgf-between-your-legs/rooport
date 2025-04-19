# Directus: Extension Setup & Development Workflow

Setting up a development environment and workflow for creating Directus extensions.

## Core Concept: Local Development and Bundling

Directus extensions (Hooks, Endpoints, Interfaces, etc.) are developed locally as separate packages, typically using TypeScript or JavaScript. The Directus Extensions SDK provides tools to initialize, build, and manage these packages.

**General Workflow:**

1.  **Initialize:** Use `npx create-directus-extension` to scaffold a new extension package with the correct structure and basic configuration.
2.  **Develop:** Write your extension code (TypeScript/JavaScript for backend, Vue.js for frontend app extensions) within the generated package structure.
3.  **Build:** Use `directus-extension build` (often via `npm run build`) to compile TypeScript, bundle the code, and generate the necessary output (usually a `dist/index.js` file).
4.  **Link/Copy:** Make the built extension available to your local Directus development instance.
5.  **Test:** Run your local Directus instance and test the extension's functionality.
6.  **Deploy:** Copy the final built extension bundle to the `extensions/` directory of your production Directus instance.

## Setting Up an Extension Project

1.  **Prerequisites:** Node.js and npm/yarn installed.
2.  **Create Extension Package:** Navigate *outside* your main Directus project directory and run the SDK command:
    ```bash
    npx create-directus-extension
    ```
    *   Follow the prompts to choose the extension type (hook, endpoint, interface, etc.) and language (TypeScript recommended).
    *   This creates a new directory (e.g., `my-directus-hook`) with the necessary files:
        *   `src/index.ts` (or `.js`): Your main extension code entry point.
        *   `package.json`: Defines dependencies and build scripts.
        *   `tsconfig.json`: TypeScript configuration (if using TS).
        *   `directus-extension.config.js`: Configures how the extension is bundled.
3.  **Install Dependencies:** Navigate into the newly created extension directory and install dependencies:
    ```bash
    cd my-directus-hook
    npm install
    # or
    yarn install
    ```

## Development Workflow

1.  **Write Code:** Edit the `src/index.ts` (or other source files) to implement your extension logic (registering hooks, defining endpoint routes, creating Vue components for app extensions).
2.  **Build in Watch Mode:** For continuous development, run the build command in watch mode. This automatically rebuilds the extension when you save changes.
    ```bash
    npm run dev
    # or
    yarn dev
    ```
    This typically runs `directus-extension build --watch`.
3.  **Link to Local Directus Instance:** Make the built output (`dist/index.js`) accessible to your local Directus server. Two common methods:
    *   **Symlinking (Recommended for Dev):** Create a symbolic link from your Directus instance's `extensions` directory to your extension's build output.
        *   Navigate to your Directus project's `extensions/{type}` directory (e.g., `my-directus-project/extensions/hooks`).
        *   Create the target directory if it doesn't exist: `mkdir my-directus-hook`
        *   Create the symlink (adjust paths as needed):
            ```bash
            # On macOS/Linux
            ln -s /path/to/your/my-directus-hook/dist/index.js my-directus-hook/index.js

            # On Windows (Command Prompt as Admin)
            mklink my-directus-hook\index.js C:\path\to\your\my-directus-hook\dist\index.js
            ```
    *   **Copying:** Manually copy the `dist/index.js` file into the corresponding `extensions/{type}/{name}/` directory in your Directus project after each build. Less convenient for active development.
4.  **Run Directus:** Start your local Directus development server (`npm run dev` in the main Directus project). It should automatically detect and load the linked/copied extension. Check the server logs for confirmation or errors related to your extension.
5.  **Test:** Interact with Directus (UI or API) to test your extension's functionality. Use browser dev tools and check Directus logs for debugging.
6.  **Iterate:** Make changes to your extension code, let the watch mode rebuild, and test again. You might need to restart the main Directus server occasionally if changes affect server startup logic.

## Building for Production

When ready to deploy:

1.  Run the production build command in your extension directory:
    ```bash
    npm run build
    # or
    yarn build
    ```
    This typically runs `directus-extension build`.
2.  Copy the generated `dist` folder (or just the `index.js` file, depending on the extension type and its assets) to the appropriate `extensions/{type}/{name}/` directory on your production Directus server.
3.  Ensure the production Directus instance restarts or reloads extensions to pick up the changes (deployment strategy depends on your hosting setup - Docker, PaaS, etc.). Coordinate with `devops-lead`.

Developing extensions involves creating a separate package, using the SDK's build tools (preferably in watch mode), and linking the output to your local Directus instance for testing.

*(Refer to the official Directus documentation on Creating Extensions.)*