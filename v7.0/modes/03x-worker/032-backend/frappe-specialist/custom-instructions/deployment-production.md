# Frappe: Deployment to Production

Considerations for deploying and managing Frappe/ERPNext applications in a production environment.

## Core Components in Production

A typical Frappe production setup involves several components working together:

1.  **Frappe Application Code:** Your custom apps and the Frappe/ERPNext framework code.
2.  **Database:** MariaDB (default) or PostgreSQL. Stores all DocType data, configurations, etc.
3.  **Redis:** Used for caching and as a message broker for background jobs (RQ).
4.  **Web Server (WSGI/ASGI):** Handles HTTP requests and runs the Python application code.
    *   **Gunicorn (WSGI):** Common choice for synchronous workers.
    *   **Uvicorn (ASGI):** Can be used, especially if leveraging async features (less common in standard Frappe).
5.  **Background Workers (`bench worker`):** Processes jobs enqueued via `frappe.enqueue` (e.g., sending emails, long calculations). Listens to Redis queues.
6.  **Scheduler (`bench schedule`):** Enqueues scheduled jobs (defined in `hooks.py`) at the specified times. The jobs are then picked up by `bench worker`.
7.  **Realtime (Optional - `bench socketio`):** Node.js-based server using Socket.IO for real-time updates (e.g., notifications, live forms).
8.  **Reverse Proxy (Nginx - Recommended):** Sits in front of the Frappe web server(s). Handles SSL/TLS termination (HTTPS), serves static assets, load balancing, rate limiting, security headers.
9.  **Process Manager (Supervisor / Systemd):** Keeps the web server, workers, scheduler, and realtime processes running reliably, restarting them if they crash.

## Deployment Strategies

*   **Manual Setup (VPS/Bare Metal):** Install all dependencies (Python, Node.js, MariaDB, Redis, Nginx, Supervisor) and configure them manually. Use `bench setup production <user>` to help configure Nginx and Supervisor. Most flexible but requires significant sysadmin knowledge.
*   **Docker (Recommended):** Use official Frappe/ERPNext Docker images or custom images.
    *   **`docker-compose`:** Define all services (Frappe, Nginx, MariaDB, Redis) in a `docker-compose.yml` file for easy local development and simpler single-server deployments. Frappe provides official examples.
    *   **Kubernetes (K8s):** For scalable, high-availability deployments. Requires managing K8s manifests or using Helm charts. More complex setup.
*   **Managed Services / PaaS:** Some providers might offer specialized Frappe/ERPNext hosting, simplifying parts of the setup.

## Key Deployment Steps & Considerations

1.  **Server Setup:** Provision server(s) with adequate resources (CPU, RAM, Disk). Install OS and dependencies.
2.  **Database Setup:** Install and configure MariaDB or PostgreSQL. Create a dedicated database and user for Frappe. Ensure regular backups are configured.
3.  **Redis Setup:** Install and configure Redis for caching and queues.
4.  **Bench Installation:** Install the `bench` CLI tool.
5.  **Get Apps:** Download Frappe, ERPNext (if used), and your custom apps using `bench get-app`.
6.  **Create Site:** `bench new-site <site-name>` (provide production database details).
7.  **Install Apps:** `bench --site <site-name> install-app <app-name>` for all required apps.
8.  **Configuration (`site_config.json`):**
    *   Set `developer_mode: 0` for production.
    *   Configure database (`db_name`, `db_password`), Redis (`redis_cache`, `redis_queue`), file storage (if using S3 etc.), email domain, etc. **Do not store sensitive passwords directly in `site_config.json` if possible; use environment variables or secure methods.** Bench commands often manage this file.
9.  **Build Assets:** `bench build`.
10. **Run Migrations:** `bench --site <site-name> migrate`.
11. **Setup Production Processes:**
    *   Configure Supervisor or Systemd to manage `gunicorn` (or uvicorn/waitress), `bench worker` (potentially multiple workers for different queues: default, short, long), and `bench schedule`.
    *   Use `bench setup supervisor` to generate initial Supervisor config files (review and adjust).
    *   Enable and start the services.
12. **Configure Reverse Proxy (Nginx):**
    *   Set up Nginx to proxy requests to the Gunicorn/web server port.
    *   Configure SSL/TLS (HTTPS) using Let's Encrypt or other certificates.
    *   Configure Nginx to serve static files directly from `sites/assets` and `apps/.../public` for better performance.
    *   Add security headers (CSP, HSTS, X-Frame-Options, etc.).
    *   Use `bench setup nginx` to generate initial Nginx config (review and adjust).
13. **DNS:** Point your domain name to the server/load balancer IP address.
14. **Testing:** Thoroughly test the deployed application.

## Updates in Production

1.  **Backup:** **ALWAYS** back up the database and site files before updating (`bench backup`).
2.  **Enable Maintenance Mode (Optional):** `bench --site <site-name> set-maintenance-mode on`.
3.  **Pull Changes:** `bench update --pull` (or update specific apps).
4.  **Update Dependencies:** `bench update --requirements`.
5.  **Run Patches:** `bench update --patch`.
6.  **Run Migrations:** `bench --site <site-name> migrate`.
7.  **Build Assets:** `bench build`.
8.  **Restart Processes:** `bench restart` (or restart Supervisor/Systemd services).
9.  **Disable Maintenance Mode:** `bench --site <site-name> set-maintenance-mode off`.
10. **Test:** Verify the update was successful.

Deployment requires careful planning and coordination between development and operations (DevOps). Consult `infrastructure-specialist` and `devops-lead`.

*(Refer to the official Frappe deployment guides and bench documentation.)*