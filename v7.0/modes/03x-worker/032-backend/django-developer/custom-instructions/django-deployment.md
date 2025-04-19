# Django: Deployment Strategies Overview

Considerations and common patterns for deploying Django applications to production.

## Core Concept: Moving from Development to Production

Deploying a Django application involves moving it from your local development environment to a production server where users can access it reliably and securely. This requires several steps beyond just running `manage.py runserver`.

**Key Differences in Production:**

*   **Web Server:** The Django development server (`runserver`) is **not** suitable for production (single-threaded, lacks security/performance features). You need a production-grade web server (like Nginx or Apache).
*   **Application Server (WSGI/ASGI):** Django communicates with the web server via a standard interface:
    *   **WSGI (Web Server Gateway Interface):** The traditional standard for synchronous Python web applications. Common WSGI servers include Gunicorn and uWSGI.
    *   **ASGI (Asynchronous Server Gateway Interface):** A newer standard supporting asynchronous features (like WebSockets, used by Django Channels). Common ASGI servers include Uvicorn, Daphne, and Hypercorn.
*   **Static Files:** Static files (CSS, JS, images) should be served directly by the web server (Nginx/Apache) or a CDN, not through Django, for performance.
*   **Database:** Use a robust production database (PostgreSQL, MySQL) instead of SQLite (which is often used in development).
*   **Security:** `DEBUG` must be `False`, `SECRET_KEY` must be kept secret, `ALLOWED_HOSTS` must be configured, HTTPS must be enforced.
*   **Environment Variables:** Configuration (database credentials, secret keys, etc.) should be managed via environment variables, not hardcoded in `settings.py`.

## Common Deployment Architecture

A typical production setup often looks like this:

```
User Request --> DNS --> Load Balancer (Optional) --> Web Server (Nginx/Apache)
                                                            |
                                                            v
                                          Application Server (Gunicorn/Uvicorn) <--> Django App
                                                            |
                                                            v
                                                      Database (PostgreSQL/MySQL)
                                                            |
                                                            v
                                                      Cache (Redis/Memcached) (Optional)
                                                            |
                                                            v
                                                Task Queue (Celery/RQ) (Optional)
```

*   **Web Server (Nginx/Apache):** Handles incoming HTTP requests, serves static files directly, terminates SSL (HTTPS), and acts as a reverse proxy, forwarding dynamic requests to the application server.
*   **Application Server (Gunicorn/Uvicorn):** Runs multiple instances (workers) of your Django application, manages processes/threads, and communicates with the web server via WSGI or ASGI.
*   **Process Manager (Optional but Recommended):** Tools like `systemd` or `supervisor` are used to manage the application server processes (start, stop, restart on failure).

## Deployment Checklist & Steps (Conceptual)

1.  **Production `settings.py`:**
    *   Set `DEBUG = False`.
    *   Configure `ALLOWED_HOSTS` with your domain(s).
    *   Load `SECRET_KEY`, database credentials, email settings, etc., from environment variables (e.g., using `os.environ.get()`).
    *   Configure `STATIC_ROOT` (where `collectstatic` will place files).
    *   Configure `STATIC_URL` (URL prefix for static files).
    *   Configure `MEDIA_ROOT` and `MEDIA_URL` if handling user uploads.
    *   Configure production database settings (`DATABASES`).
    *   Configure production caching (`CACHES`).
    *   Configure logging for production.
    *   Configure HTTPS-related settings (`SECURE_SSL_REDIRECT`, `SESSION_COOKIE_SECURE`, etc.).
2.  **Server Setup:** Provision a server (VPS, cloud instance) or choose a PaaS (Platform-as-a-Service like Heroku, Render, PythonAnywhere).
3.  **Install Dependencies:** Install Python, `pip`, database drivers, and project dependencies (`pip install -r requirements.txt`). Use a virtual environment.
4.  **Database Setup:** Create the production database and user. Apply migrations (`python manage.py migrate`).
5.  **Collect Static Files:** Run `python manage.py collectstatic`.
6.  **Configure Web Server (e.g., Nginx):**
    *   Set up a server block for your domain.
    *   Configure it to serve static files directly from `STATIC_ROOT`.
    *   Configure it to serve user-uploaded media files from `MEDIA_ROOT` (if applicable).
    *   Configure it as a reverse proxy to pass requests to your application server (Gunicorn/Uvicorn) - often via a Unix socket or localhost port.
    *   Configure SSL/TLS (HTTPS) using certificates (e.g., Let's Encrypt).
7.  **Configure Application Server (e.g., Gunicorn for WSGI):**
    *   Install Gunicorn (`pip install gunicorn`).
    *   Typically run via a process manager (`systemd`, `supervisor`).
    *   Command might look like: `gunicorn --workers 3 --bind unix:/path/to/socket.sock project.wsgi:application` (replace `project.wsgi` with your project's WSGI entry point).
    *   For ASGI (e.g., Uvicorn): `uvicorn --workers 3 --uds /path/to/socket.sock project.asgi:application`
8.  **Configure Process Manager (e.g., `systemd`):**
    *   Create a service file to define how to start, stop, and manage the Gunicorn/Uvicorn process. Ensure it runs under a non-root user and activates the correct virtual environment.
9.  **Run System Checks:** `python manage.py check --deploy`.
10. **Start Services:** Enable and start the `systemd`/`supervisor` service for your application server, and ensure the web server (Nginx/Apache) is running.
11. **Monitoring & Logging:** Set up monitoring and log aggregation for the application and servers.

**Platform-as-a-Service (PaaS):** Platforms like Heroku, Render, Google App Engine, AWS Elastic Beanstalk abstract away much of the server setup. You typically provide your code, a `requirements.txt`, and a `Procfile` (or similar) specifying how to run your application (e.g., `web: gunicorn project.wsgi`), and the platform handles server provisioning, deployment, scaling, and often database/cache services.

Deployment requires careful configuration of the server environment, web server, application server, static files, and security settings. Choose between manual server setup or using a PaaS based on project needs and expertise. Coordinate closely with `infrastructure-specialist` / `devops-lead`.

*(Refer to the official Django Deployment checklist and documentation for specific servers like Gunicorn, Uvicorn, Nginx.)*