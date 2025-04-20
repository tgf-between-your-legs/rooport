# Frappe Specialist: Deployment &amp; Configuration

Deploying and configuring Frappe for production requires careful setup of multiple components. Coordinate closely with `devops-lead` and `infrastructure-specialist` via your lead.

## 1. Production Components Overview

*   **Application Code:** Frappe, ERPNext (if used), custom apps.
*   **Database:** MariaDB (default) or PostgreSQL.
*   **Redis:** Caching and Background Job queues (RQ).
*   **Web Server (WSGI):** Gunicorn (common) runs the Python app.
*   **Background Workers (`bench worker`):** Execute jobs from Redis queues. Need separate processes for different queues (short, default, long).
*   **Scheduler (`bench schedule`):** Enqueues scheduled jobs.
*   **Realtime (Optional - `bench socketio`):** Node.js/Socket.IO for live updates.
*   **Reverse Proxy (Nginx - Recommended):** Handles HTTPS, serves static files, load balancing.
*   **Process Manager (Supervisor / Systemd):** Keeps services (gunicorn, workers, scheduler) running.

## 2. Deployment Strategies

*   **Manual Setup (VPS/Bare Metal):** Install all dependencies manually. Use `bench setup production [user]` to help configure Nginx/Supervisor. Requires sysadmin skills.
*   **Docker (Recommended):** Use official or custom images.
    *   `docker-compose`: Good for single-server setups. Define services in `docker-compose.yml`.
    *   Kubernetes (K8s): For scalable, high-availability deployments using Helm charts or manifests. More complex.

## 3. Key Deployment Steps (Conceptual)

1.  **Provision Infrastructure:** Server(s), Database (managed or self-hosted), Redis (managed or self-hosted).
2.  **Install Bench & Dependencies:** Python, Node.js, MariaDB/PostgreSQL client, Redis client, `bench` CLI.
3.  **Get Apps:** `bench get-app ...` for Frappe, ERPNext, custom apps.
4.  **Create Site:** `bench new-site [site-name]` (provide production DB credentials).
5.  **Install Apps:** `bench --site [site-name] install-app [app-name]`.
6.  **Configure (`site_config.json`):**
    *   `developer_mode: 0` **(CRITICAL for production)**.
    *   Database (`db_name`, `db_password`), Redis (`redis_cache`, `redis_queue`).
    *   File storage (S3, etc. - optional).
    *   Email domain, SMTP settings.
    *   **Security:** Avoid hardcoding sensitive passwords; use environment variables or secure injection methods where possible (coordinate with DevOps).
7.  **Build Assets:** `bench build`.
8.  **Run Migrations:** `bench --site [site-name] migrate`.
9.  **Setup Production Processes (Supervisor/Systemd):**
    *   Configure services for: Gunicorn, `bench worker` (multiple, for different queues), `bench schedule`.
    *   Use `bench setup supervisor` to generate initial configs (review/adjust).
    *   Enable and start services.
10. **Configure Reverse Proxy (Nginx):**
    *   Proxy requests to Gunicorn.
    *   Configure SSL/TLS (HTTPS - Let's Encrypt).
    *   Serve static assets (`sites/assets`, `apps/.../public`) directly.
    *   Add security headers (CSP, HSTS, etc.).
    *   Use `bench setup nginx` to generate initial configs (review/adjust).
11. **DNS:** Point domain to server/load balancer.
12. **Testing:** Thoroughly test the live deployment.

## 4. Configuration (`site_config.json`)

*   **Location:** `sites/[site-name]/site_config.json`.
*   **Management:** Use `bench set-config [key] [value]` or edit the file carefully.
*   **Common Keys:**
    *   `db_name`, `db_password`
    *   `redis_cache`, `redis_queue`, `redis_socketio` (connection strings)
    *   `developer_mode`: `0` for production, `1` for development.
    *   `maintenance_mode`: `1` to show maintenance page.
    *   `pause_scheduler`: `1` to stop scheduler from enqueueing jobs.
    *   `logging`: Control log levels.
    *   `mail_server`, `mail_port`, `use_tls`, `mail_login`, `mail_password` (for email sending).
    *   `host_name`: Set if running behind a proxy.
    *   `limits`: Configure rate limits, timeouts.

## 5. Production Updates

1.  **BACKUP FIRST:** `bench backup`.
2.  **(Optional) Maintenance Mode:** `bench set-maintenance-mode on`.
3.  **Pull Code:** `bench update --pull`.
4.  **Update Dependencies:** `bench update --requirements`.
5.  **Run Patches:** `bench update --patch`.
6.  **Migrate DB:** `bench --site [site-name] migrate`.
7.  **Build Assets:** `bench build`.
8.  **Restart Services:** `bench restart` or restart Supervisor/Systemd services.
9.  **(If used) Disable Maintenance Mode:** `bench set-maintenance-mode off`.
10. **Test.**

Deployment is a critical phase requiring careful planning and execution. Always prioritize backups and testing.