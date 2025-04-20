# Django: Security Basics

Overview of built-in security features and common best practices in Django.

## Core Concept

Django provides multiple layers of protection against common web vulnerabilities out-of-the-box. However, developers still need to understand and correctly utilize these features and follow secure coding practices.

## Built-in Protections

*   **Cross-Site Scripting (XSS) Protection:**
    *   **Mechanism:** Django templates automatically escape HTML-specific characters by default (`{{ variable }}` outputs escaped HTML). This prevents malicious scripts embedded in user-generated content from being executed in other users' browsers.
    *   **Caution:** Only disable auto-escaping using the `|safe` filter on content you absolutely trust or have explicitly sanitized.
*   **Cross-Site Request Forgery (CSRF) Protection:**
    *   **Mechanism:** Prevents malicious websites from forcing a logged-in user on your site to unknowingly submit data to your site.
    *   **How it Works:** Django adds a hidden field with a secret token (`csrfmiddlewaretoken`) to outgoing POST forms. On submission, the `CsrfViewMiddleware` checks if this token matches the one stored in the user's session/cookie.
    *   **Implementation:**
        *   Ensure `django.middleware.csrf.CsrfViewMiddleware` is in `MIDDLEWARE` settings (default).
        *   Add the `{% csrf_token %}` template tag inside **every** `<form method="post">` in your templates.
        *   For AJAX POST requests, retrieve the token (e.g., from a cookie named `csrftoken`) and include it in the request header (typically `X-CSRFToken`).
*   **SQL Injection Protection:**
    *   **Mechanism:** Django's ORM uses parameterized queries. It separates the query structure from the query parameters, ensuring user input is treated as data, not executable SQL code.
    *   **Best Practice:** **Always** use the ORM (QuerySets, `filter()`, `get()`, `create()`, etc.) for database interactions. Avoid constructing raw SQL queries with string formatting, especially using user input. If raw SQL is absolutely necessary, use `connection.cursor()` and pass parameters safely as arguments, not via string interpolation.
*   **Clickjacking Protection:**
    *   **Mechanism:** The `XFrameOptionsMiddleware` (enabled by default) sets the `X-Frame-Options` HTTP header to `DENY`, preventing your site from being embedded in an `<frame>` or `<iframe>` on other sites, which could trick users into clicking unintended actions.
    *   **Configuration:** Can be configured via `X_FRAME_OPTIONS` setting (default is `'DENY'`).

## Other Security Considerations

*   **`SECRET_KEY`:**
    *   **Purpose:** Used for cryptographic signing (sessions, CSRF tokens, password reset tokens, etc.).
    *   **Security:** **Keep it secret!** Do not commit it to version control. Load it from environment variables or a secure secrets management system in production. Ensure it's long and random.
*   **`DEBUG` Setting:**
    *   **Security:** **NEVER** run with `DEBUG = True` in production. It exposes detailed error pages (including settings and stack traces) which can reveal sensitive information. Set `DEBUG = False` in production `settings.py`.
    *   **`ALLOWED_HOSTS`:** When `DEBUG = False`, Django requires `ALLOWED_HOSTS` to be set in `settings.py` with a list of valid host/domain names for your site to prevent HTTP Host header attacks.
*   **HTTPS:**
    *   Always deploy Django behind HTTPS in production.
    *   Use security middleware settings like `SECURE_SSL_REDIRECT = True`, `SESSION_COOKIE_SECURE = True`, `CSRF_COOKIE_SECURE = True` to enforce HTTPS and secure cookies. Configure your web server (Nginx, Apache) or load balancer to handle SSL termination.
*   **Password Hashing:** Django uses strong password hashing (PBKDF2 by default) automatically via the auth system.
*   **User-Uploaded Content:**
    *   **Validation:** Validate uploaded file types, sizes, and potentially content.
    *   **Storage:** Store user-uploaded files in a designated `MEDIA_ROOT` outside your main project code directory. Serve them carefully (e.g., via Nginx, not directly through Django in production). Consider using cloud storage (S3, GCS).
    *   **Security:** Never trust the filename or content type provided by the user. Be cautious about potential vulnerabilities related to file content (e.g., XML bombs, malicious scripts if files are served incorrectly).
*   **Authentication & Authorization:**
    *   Use Django's built-in auth system or a reputable third-party package.
    *   Implement proper authorization checks (permissions) in views using decorators (`@login_required`, `@permission_required`) or mixins (`LoginRequiredMixin`, `PermissionRequiredMixin`).
*   **Dependencies:** Keep Django and all third-party packages updated to patch security vulnerabilities. Use tools like `pip-audit` or GitHub Dependabot.

*(Refer to the official Django Security documentation: https://docs.djangoproject.com/en/stable/topics/security/)*