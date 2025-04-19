# Custom Instructions for 🐍 Django Developer Mode

This directory contains specific instructions and guidelines for the `django-developer` mode, broken down by topic.

## Instruction Files

1.  [`01-core-principles-workflow.md`](./01-core-principles-workflow.md): General operational guidelines, MVT pattern, Project vs. Apps structure, standard workflow, and common `manage.py` commands.
2.  [`02-models-orm.md`](./02-models-orm.md): Defining models, fields, relationships, `Meta` options, migrations, and using the ORM for querying (QuerySets, `filter`, `get`, `create`, `update`, `delete`, `select_related`, `prefetch_related`).
3.  [`03-views-urls.md`](./03-views-urls.md): Implementing request handling logic using Function-Based Views (FBVs) and Class-Based Views (CBVs, including generic views), and mapping URL patterns using `urls.py`, `path()`, `include()`, converters, and URL reversing.
4.  [`04-templates-dtl.md`](./04-templates-dtl.md): Using the Django Template Language (DTL) syntax (`{{ var }}`, `{% tag %}`, `{{ var|filter }}`), template inheritance (`{% extends %}`, `{% block %}`), context, and common tags/filters.
5.  [`05-forms.md`](./05-forms.md): Handling user input and validation using `forms.Form` and `forms.ModelForm`, defining fields, widgets, validation methods (`clean_`, `clean`), and rendering forms in templates.
6.  [`06-admin-interface.md`](./06-admin-interface.md): Enabling, accessing, registering models, and customizing the built-in Django admin interface using `ModelAdmin` options (`list_display`, `list_filter`, `search_fields`, `fieldsets`, `inlines`, actions).
7.  [`07-testing.md`](./07-testing.md): Writing unit and integration tests using `django.test.TestCase`, the test client (`self.client`) for simulating requests, setting up test data (`setUpTestData`), and common assertions.
8.  [`08-security.md`](./08-security.md): Overview of Django's built-in protections (XSS, CSRF, SQL Injection, Clickjacking) and essential best practices (HTTPS, `SECRET_KEY`, `DEBUG=False`, input validation, file uploads, security headers).
9.  [`09-performance-caching.md`](./09-performance-caching.md): Techniques for optimizing database queries (`select_related`, `prefetch_related`, `only`, `defer`, `values`, `count`, `exists`, indexing) and using Django's caching framework (backends, per-site, per-view, template fragment, low-level API).
10. [`10-deployment.md`](./10-deployment.md): Overview of deploying Django applications, including the roles of web servers (Nginx), application servers (Gunicorn/Uvicorn), WSGI/ASGI, static file handling (`collectstatic`), and key production settings.
11. [`11-authentication.md`](./11-authentication.md): Using `django.contrib.auth` for user management, login/logout, permissions, groups, password handling, built-in views/forms, and custom user models.
12. [`12-collaboration-escalation.md`](./12-collaboration-escalation.md): Guidelines for collaborating with other specialist modes and when to escalate tasks outside core Django expertise.
13. [`13-drf-basics.md`](./13-drf-basics.md): Introduction to Django REST Framework (DRF) for building APIs, including Serializers (`ModelSerializer`), Views/ViewSets (`ModelViewSet`), Routers, and basic authentication/permissions.