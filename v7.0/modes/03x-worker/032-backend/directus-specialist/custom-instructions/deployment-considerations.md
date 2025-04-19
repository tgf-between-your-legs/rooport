# Directus: Deployment Considerations

Key aspects to consider when deploying and managing Directus instances and extensions.

## Deployment Options

Directus can be deployed in various ways:

1.  **Directus Cloud:** Fully managed platform-as-a-service (PaaS). Simplest option, handles infrastructure, scaling, updates, and backups.
2.  **Self-Hosted (Docker - Recommended):** Deploy using the official Directus Docker image. Provides flexibility in choosing infrastructure (AWS, GCP, Azure, DigitalOcean, on-premise) while simplifying setup. Requires managing the container, database, and potentially caching/messaging services.
3.  **Self-Hosted (Node.js):** Install and run Directus directly using Node.js and npm/yarn/pnpm. Requires managing the Node.js environment, dependencies, database, and process (e.g., using PM2). More manual setup.

## Key Considerations (Self-Hosted)

*   **Environment Variables (`.env`):**
    *   **CRITICAL:** Ensure production secrets (`SECRET`, `DB_PASSWORD`, API keys for SSO/Storage) are **not** committed to Git. Use the hosting platform's secret management or secure environment variable injection.
    *   Configure `PUBLIC_URL` correctly for the production domain.
    *   Set database connection details (`DB_CLIENT`, `DB_HOST`, etc.).
    *   Configure file storage adapters (e.g., `STORAGE_S3_...`) if not using local storage.
    *   Configure email transport (`EMAIL_...`).
    *   Set up caching (`CACHE_ENABLED`, `CACHE_STORE`, `CACHE_REDIS`) for performance.
    *   Configure CORS (`CORS_ORIGIN`) appropriately for your frontend applications.
    *   Set `NODE_ENV=production`.
*   **Database:**
    *   Use a robust production database (PostgreSQL, MySQL recommended over SQLite for production).
    *   Ensure regular backups are configured.
*   **File Storage:**
    *   Local storage (default `storage/uploads`) is simple but doesn't scale across multiple instances and requires volume mounting/backups.
    *   Cloud storage (S3, GCS, Azure Blob) is recommended for scalability and durability. Configure the appropriate adapter and credentials via environment variables.
*   **Caching & Messaging (for Scaling):**
    *   If running multiple Directus instances for high availability or load balancing, configure Redis (or another supported broker) for caching (`CACHE_STORE=redis`) and inter-process messaging (`MESSENGER_STORE=redis`, `WEBSOCKETS_BROKER_URL`) to ensure consistency across instances (e.g., for WebSockets, cache invalidation).
*   **Custom Extensions:**
    *   **Build Step:** App extensions (interfaces, layouts, etc.) need to be built (`npm run build` within the extension directory).
    *   **Deployment:** Ensure the compiled extensions (usually in a `dist` folder within each extension directory) are copied into the `extensions` folder of the running Directus instance.
        *   **Docker:** Mount the local `extensions` directory (containing the built extensions) as a volume into the `/directus/extensions` path inside the container.
        *   **Node.js:** Ensure the `extensions` directory is present alongside the Directus core files.
    *   **Dependencies:** If extensions have their own `node_modules`, these need to be installed or included in the deployment artifact.
*   **Updates:**
    *   Plan for updating the Directus core version (e.g., pulling a new Docker image, updating npm packages).
    *   Check Directus release notes for breaking changes, especially regarding extensions or configuration.
    *   Test updates in a staging environment before applying to production.
*   **Process Management (Node.js):** If running directly with Node.js, use a process manager like PM2 to handle restarts, logging, and clustering.
*   **HTTPS:** Always run Directus behind a reverse proxy (like Nginx or Caddy) or load balancer that handles SSL/TLS termination (HTTPS).
*   **Security:**
    *   Keep the Directus instance and underlying OS/packages updated.
    *   Configure firewalls appropriately.
    *   Review Directus roles and permissions regularly.
    *   Monitor logs.

Coordinate closely with `devops-lead` and `infrastructure-specialist` for setting up and managing the deployment environment, CI/CD pipelines, backups, and monitoring.

*(Refer to the official Directus Deployment documentation: https://docs.directus.io/self-hosted/installation/docker.html and https://docs.directus.io/self-hosted/config-options.html)*