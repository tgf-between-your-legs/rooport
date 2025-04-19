# Flask: Deployment (WSGI / ASGI)

Understanding deployment options for Flask applications.

## Core Concept: WSGI & ASGI

*   **WSGI (Web Server Gateway Interface):** The standard interface between Python web applications/frameworks (like Flask, Django) and web servers for handling **synchronous** requests. Defined in PEP 3333.
*   **ASGI (Asynchronous Server Gateway Interface):** A successor to WSGI designed to handle **asynchronous** Python web frameworks and features (like WebSockets, long polling). It's backward compatible with WSGI. Defined in ASGI Specification.
*   **Flask & Interfaces:**
    *   Flask is fundamentally a WSGI application.
    *   It can be run using ASGI servers via WSGI-to-ASGI adapters (like the one built into Uvicorn). This allows running sync Flask code alongside async frameworks or using async features like WebSockets via extensions (e.g., Flask-SocketIO with an ASGI server).

## Development Server vs. Production Servers

*   **Flask Development Server (`flask run`):**
    *   **Purpose:** Convenient for local development, debugging, and automatic reloading.
    *   **Limitations:** **NOT suitable for production.** It's single-threaded by default (can handle only one request at a time) and not designed for performance, security, or stability under load.
*   **Production Servers:** You need a dedicated WSGI or ASGI server to run Flask in production. Common choices include:
    *   **Gunicorn:** A mature, widely used WSGI HTTP server for UNIX. Simple to configure and manage multiple worker processes.
    *   **uWSGI:** A feature-rich application server container (supports WSGI, ASGI, and other protocols). Can be more complex to configure than Gunicorn but offers more options.
    *   **Uvicorn:** A lightning-fast ASGI server, built on uvloop and httptools. Often used with FastAPI, but can also run WSGI applications (like Flask) using its built-in adapter. Ideal if you need async capabilities or are mixing Flask with async frameworks.
    *   **Waitress:** A production-quality, pure-Python WSGI server. Works on Windows and UNIX. Simpler than Gunicorn/uWSGI but might not offer the same level of performance tuning.

## Deployment Strategy Overview

1.  **Choose a Server:** Select a WSGI/ASGI server (Gunicorn, Uvicorn, Waitress, etc.).
2.  **Install Server:** Add the chosen server to your `requirements.txt` and install it (`pip install gunicorn`).
3.  **Create App Entry Point:** Ensure you have a way to access your Flask `app` instance (often via the Application Factory pattern in `create_app()`). You might need a small `wsgi.py` or similar file.
    ```python
    # wsgi.py (Example for Gunicorn/uWSGI)
    from app import create_app # Assuming create_app is in app/__init__.py

    app = create_app('production') # Load production config

    # Server will import 'app' from this file
    ```
4.  **Configure Server:**
    *   **Gunicorn:** Typically run via command line:
        ```bash
        # Example: Run Gunicorn with 4 worker processes, binding to port 8000
        # Assumes wsgi.py contains the 'app' instance
        gunicorn --workers 4 --bind 0.0.0.0:8000 wsgi:app
        ```
        Configuration can also be done via a config file (`gunicorn.conf.py`).
    *   **Uvicorn (Running Flask as WSGI):**
        ```bash
        # Example: Run Uvicorn with 4 workers, binding to port 8000
        # Tells Uvicorn to treat wsgi:app as a WSGI application
        uvicorn --workers 4 --host 0.0.0.0 --port 8000 wsgi:app
        ```
    *   **Waitress:**
        ```bash
        # Example: Run Waitress
        waitress-serve --host 0.0.0.0 --port 8000 wsgi:app
        ```
5.  **Reverse Proxy (Recommended):** Run your WSGI/ASGI server behind a dedicated web server like **Nginx** or **Caddy**.
    *   **Benefits:** Handles HTTPS/SSL termination, serves static files efficiently, load balancing, buffering slow clients, security headers.
    *   **Configuration:** Configure the reverse proxy to forward requests to the WSGI/ASGI server (e.g., `proxy_pass http://127.0.0.1:8000;` in Nginx).
6.  **Process Management:** Use tools like `systemd` or `supervisor` to manage the WSGI/ASGI server process (start, stop, restart on failure). Docker/Kubernetes handle this in containerized environments.
7.  **Static Files:** Configure your reverse proxy (Nginx) to serve static files directly from the `static` folder collected by `flask collect` (or your build process) for better performance. Don't serve static files through Flask in production.

## Deployment Platforms

*   **PaaS (Platform-as-a-Service):** Heroku, Google App Engine, Render, PythonAnywhere often simplify deployment by handling server configuration, process management, and scaling. You typically provide a `Procfile` (Heroku) or `app.yaml` (GAE) specifying how to run your app (e.g., using Gunicorn).
*   **Containers (Docker):** Package your Flask app, WSGI/ASGI server, and dependencies into a Docker image. Deploy using Docker Compose, Kubernetes, ECS, etc. Provides consistency across environments.
*   **Serverless:** Deploy Flask apps using frameworks like Zappa, Chalice, or Serverless Framework to AWS Lambda/API Gateway or similar platforms. Requires adapting the application structure.
*   **Virtual Private Server (VPS):** Manually configure the server, database, WSGI/ASGI server, reverse proxy, process manager, and firewall. Most flexible but requires more setup and maintenance.

Choose the deployment strategy and server based on your application's needs, scalability requirements, and operational preferences. Always use a production-ready WSGI/ASGI server and preferably a reverse proxy.

*(Refer to the official Flask Deployment Options documentation.)*