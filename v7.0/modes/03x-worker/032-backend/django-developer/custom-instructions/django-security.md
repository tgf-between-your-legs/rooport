# Django: Security Best Practices

Implementing common security measures in Django applications.

## Core Concept: Built-in Protection & Developer Responsibility

Django provides built-in protection against several common web vulnerabilities, but developers still need to use these features correctly and be aware of potential security pitfalls. Security is a continuous process, not a one-time setup.

**Key Built-in Protections:**

*   **Cross-Site Scripting (XSS) Prevention:** Django templates automatically escape HTML-specific characters in variable output (`{{ variable }}`) by default.
*   **Cross-Site Request Forgery (CSRF) Protection:** Requires a `{% csrf_token %}` in POST forms and validates this token on submission via middleware (`CsrfViewMiddleware`).
*   **SQL Injection Protection:** The ORM generally uses parameterized queries, preventing most SQL injection vulnerabilities when used correctly. Avoid constructing raw SQL queries with user input.
*   **Clickjacking Protection:** The `XFrameOptionsMiddleware` helps prevent your site from being embedded in malicious `<iframe>` tags.
*   **Password Hashing:** Securely hashes passwords using configurable algorithms (PBKDF2 is default).

## Essential Security Practices

1.  **Keep Django & Dependencies Updated:** Regularly update Django and all third-party packages to patch known vulnerabilities (`pip install -U Django`, `pip list --outdated`).
2.  **Use HTTPS:** Deploy your application over HTTPS using TLS/SSL certificates to encrypt data in transit. Configure settings like `SECURE_SSL_REDIRECT = True`, `SESSION_COOKIE_SECURE = True`, `CSRF_COOKIE_SECURE = True` in production.
3.  **Protect the `SECRET_KEY`:** Keep the `SECRET_KEY` in `settings.py` confidential. Do *not* commit it to version control. Load it from environment variables or a secrets management system in production.
4.  **Disable `DEBUG` in Production:** **Never** run with `DEBUG = True` in production. It exposes sensitive configuration details and stack traces. Set `DEBUG = False` and configure `ALLOWED_HOSTS` in `settings.py`.
5.  **CSRF Protection:**
    *   Always use the `{% csrf_token %}` template tag within `<form>` elements that use the `POST` method.
    *   Ensure `django.middleware.csrf.CsrfViewMiddleware` is in your `MIDDLEWARE` setting.
    *   AJAX requests using POST/PUT/PATCH/DELETE also need to include the CSRF token (often via a header like `X-CSRFToken`).
6.  **XSS Prevention:**
    *   Rely on Django's default template auto-escaping.
    *   Use the `|safe` filter *only* on content you explicitly trust or have properly sanitized.
    *   Be cautious when generating HTML directly in views. Use formatting functions like `django.utils.html.format_html` instead of manual string formatting if including user data.
    *   Set the `X-Content-Type-Options: nosniff` header (often default or via `SecurityMiddleware`).
    *   Implement a strong `Content-Security-Policy` (CSP) header to restrict where resources (scripts, styles, images) can be loaded from.
7.  **SQL Injection Prevention:**
    *   Primarily use the Django ORM. Avoid raw SQL queries (`Manager.raw()`, `cursor.execute()`) whenever possible.
    *   If raw SQL is necessary, *never* use string formatting/interpolation to insert parameters. Use parameterized queries: `cursor.execute("SELECT * FROM myapp_article WHERE status = %s", [status_variable])`.
8.  **Authentication & Authorization:**
    *   Use Django's built-in auth system or a well-vetted third-party package.
    *   Protect sensitive views with `@login_required` / `LoginRequiredMixin` and `@permission_required` / `PermissionRequiredMixin` or custom permission checks.
    *   Enforce strong password policies.
    *   Consider enabling Two-Factor Authentication (2FA).
9.  **Input Validation:**
    *   Validate *all* user-provided data rigorously using Django Forms or DRF Serializers. Check types, lengths, ranges, formats.
    *   Don't trust data from `request.GET` or `request.POST` directly in sensitive operations (like database queries) without validation.
10. **File Uploads:**
    *   Validate uploaded file types, names, and sizes.
    *   Store uploaded files outside the web server's document root if possible.
    *   Serve user-uploaded files carefully (e.g., set appropriate `Content-Type` headers, consider `Content-Disposition: attachment`). Do not serve files with executable permissions.
    *   Use a dedicated media storage solution (like S3) in production.
11. **Session Security:**
    *   Use secure session cookies (`SESSION_COOKIE_SECURE = True` in production).
    *   Consider setting `SESSION_COOKIE_HTTPONLY = True` to prevent client-side script access.
    *   Set `SESSION_COOKIE_SAMESITE = 'Lax'` or `'Strict'` to mitigate CSRF.
12. **Error Handling:** Configure `ADMINS` and email settings for error reporting in production, but don't expose detailed error information to users (`DEBUG = False`).
13. **Security Headers:** Utilize `django.middleware.security.SecurityMiddleware` and configure settings like `SECURE_HSTS_SECONDS`, `SECURE_CONTENT_TYPE_NOSNIFF`, `SECURE_BROWSER_XSS_FILTER`.

Security is paramount. Leverage Django's built-in features, keep software updated, validate all input, handle authentication/authorization correctly, and configure your production environment securely (HTTPS, `DEBUG=False`, protected `SECRET_KEY`). Consult the Django security documentation and OWASP resources regularly. Coordinate with `security-specialist` for complex security requirements or audits.