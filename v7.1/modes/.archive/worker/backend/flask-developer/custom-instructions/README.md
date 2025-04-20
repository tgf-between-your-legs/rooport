# Custom Instructions for Flask Developer Mode

This directory contains specific instructions and guidelines for the `flask-developer` mode, focusing on various aspects of Flask application development.

## Files

1.  **`01-core-principles-workflow.md`**: Defines the core role, expertise, operational principles, and standard workflow for the Flask Developer mode.
2.  **`02-routing-views.md`**: Covers mapping URLs to view functions using `@app.route`, handling request methods, variable rules, and class-based views (`MethodView`).
3.  **`03-jinja2-templating.md`**: Explains using the Jinja2 template engine, rendering templates with `render_template`, syntax basics, inheritance, and context processors.
4.  **`04-forms-flask-wtf.md`**: Details handling web forms, validation, and CSRF protection using the Flask-WTF extension and WTForms.
5.  **`05-database-migrations.md`**: Describes managing database schema changes using Flask-Migrate and Alembic, including setup, workflow, and CLI commands.
6.  **`06-authentication-flask-login.md`**: Focuses on user session management (login, logout, protection) using the Flask-Login extension.
7.  **`07-testing.md`**: Guides on writing unit and integration tests using Flask's `test_client` and the `pytest` framework, including fixtures and common assertions.
8.  **`08-security.md`**: Outlines key security best practices for Flask, covering secret key management, XSS, CSRF, input validation, SQL injection, session security, and dependencies.
9.  **`09-configuration-deployment.md`**: Covers managing application configuration for different environments and strategies for deploying Flask applications using WSGI/ASGI servers (Gunicorn, Uvicorn, etc.) and reverse proxies.
10. **`10-collaboration-escalation.md`**: (To be created) Defines collaboration points with other modes and escalation paths for complex tasks.
11. **`11-error-handling.md`**: (To be created) Provides guidelines for handling tool failures and Flask-specific errors during development.

*(These instructions supplement the main mode definition and provide detailed guidance on specific Flask development tasks.)*