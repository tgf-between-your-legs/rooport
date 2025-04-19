# Directus: Extensions Overview

Understanding the different types of extensions available to customize and extend Directus functionality.

## Core Concept: Tailoring Directus

Directus is designed to be extensible, allowing developers to add custom functionality, integrate with other systems, and tailor the Data Studio UI to specific needs. Extensions are essentially custom code packages (typically written in Node.js/TypeScript or Vue.js for UI components) that hook into or add onto the core Directus platform.

## Types of Extensions

Directus supports several types of extensions, categorized by where they operate:

**1. API Extensions (Backend - Node.js/TypeScript):**

*   **Hooks:** Allow you to execute custom code in response to specific events within the Directus API lifecycle (e.g., before/after item creation, update, delete, authentication). Hooks can modify data, trigger side effects (like sending notifications), or perform complex validation.
    *   **Event Hooks:** Triggered by specific actions (`items.create`, `items.update`, `files.upload`, `auth.login`, etc.). Can run `before` or `after` the action, or as an `async` background task.
    *   **Filter Hooks:** Allow modification of data during an action (e.g., changing item data before saving `items.create.filter`, modifying API query parameters `items.query.filter`).
*   **Endpoints:** Allow you to add custom REST API endpoints to your Directus instance. Useful for implementing custom business logic, integrating with third-party services, or creating specialized data views not easily achievable through standard item queries.

**2. App Extensions (Frontend - Vue.js):**

These extensions customize the Directus Data Studio (the admin web interface).

*   **Interfaces:** Custom Vue components used for editing specific field types in the item detail page. Provide tailored input experiences beyond the standard built-in interfaces (e.g., a custom map selector, a specialized JSON editor, a connection to a specific third-party service).
*   **Displays:** Custom Vue components used to render field values in the collection list view (the table/card view). Useful for displaying previews or formatted representations of complex data (e.g., showing an image preview for a file field, displaying a formatted address from multiple fields).
*   **Layouts:** Custom Vue components that define alternative ways to browse collection items, replacing the default table, card, or calendar views (e.g., a custom media library layout, a kanban board layout).
*   **Modules:** Custom Vue components that add entirely new sections or pages to the main navigation of the Data Studio. Useful for dashboards, custom reports, integrations, or administrative tools specific to your project.

**3. Hybrid Extensions:**

*   Some extensions might involve both backend (API) and frontend (App) components working together.

## Development & Deployment

*   **SDK:** Directus provides tools and utilities (`@directus/extensions-sdk`) to help create, build, and package extensions.
*   **Language:** API/Endpoint extensions are typically written in **TypeScript** (or JavaScript) using Node.js. App extensions (Interfaces, Displays, Layouts, Modules) are written using **Vue.js 3** (usually with TypeScript and `<script setup>`).
*   **Structure:** Extensions follow a specific directory structure and require configuration files (`package.json`, `directus-extension.config.js`).
*   **Building:** Use the `directus-extension build` command provided by the SDK. This bundles the extension code into the required format.
*   **Deployment:**
    *   Place the built extension bundle (usually a `dist/index.js` file and potentially other assets) into the `extensions/{type}/{name}` directory of your Directus project (e.g., `extensions/hooks/my-hook/index.js`, `extensions/interfaces/custom-input/index.js`).
    *   Directus automatically discovers and loads extensions from this directory on startup.
    *   For Docker deployments, you typically mount a volume containing your extensions into the container or build a custom Docker image including the extensions.

Extensions are a powerful way to adapt Directus to specific project requirements. Choose the appropriate extension type based on whether you need to modify backend behavior (Hooks, Endpoints) or customize the admin UI (Interfaces, Displays, Layouts, Modules).

*(Refer to the official Directus documentation on Extensions.)*