## Django (Version Unknown) - Condensed Context Index

### Overall Purpose
Django is a high-level Python web framework for rapid development of secure and maintainable websites, following the model-template-views (MTV) pattern. It provides an ORM, templating, URL routing, forms, authentication, admin interface, and security features.

### Core Concepts & Capabilities
*   **Models (ORM):** Define database schema in Python (`models.Model`). Includes fields (`CharField`, `ForeignKey`, `ManyToManyField`), relationships, and data access via QuerySets (`filter`, `create`, `bulk_create`).
*   **Views:** Handle request/response logic using functions or classes (`View`, `ListView`, `DetailView`). Process data, interact with models, and render templates (`render`, `HttpResponse`). Supports `async` views.
*   **Templates:** Define presentation (HTML) using Django Template Language (DTL). Embed logic (`{% %}`) and variables (`{{ }}`). Key tags: `{% csrf_token %}`.
*   **URLs:** Map URL patterns to views (`urls.path()`). Supports named URLs and parameter capturing.
*   **Forms:** Handle user input and validation (`forms.Form`). Define fields, widgets, validation rules (`is_valid()`, `cleaned_data`). Essential for security.
*   **Authentication & Authorization:** Built-in `User` model, permissions (`has_perm`), groups. Supports custom user models (`AbstractBaseUser`) and authentication backends (`BaseBackend`).
*   **Admin:** Automatic admin interface for model management (core feature).
*   **Security:** Built-in protection against CSRF, XSS (auto-escaping), SQL Injection (ORM). Tools for password hashing, secret key management, secure form handling.
*   **Testing:** Integrated testing framework (`test.TestCase`, test client) for unit and integration tests.

### Key APIs / Components / Configuration / Patterns
*   `models.Model`: Base class for database models.
*   `models.ForeignKey`, `models.ManyToManyField`: Define model relationships.
*   `models.CharField`, `models.DateField`, `models.EmailField`, etc.: Common field types.
*   `Model.objects`: Default manager for QuerySet access (e.g., `MyModel.objects.filter(...)`).
*   `QuerySet`: Represents a collection of database objects (`filter`, `exclude`, `get`, `order_by`, `bulk_create`).
*   `urls.path(route, view, name='url_name')`: Maps a URL route to a view function/class.
*   `shortcuts.render(request, template_name, context)`: Renders a template with context.
*   `http.HttpResponse`, `http.HttpResponseRedirect`: Basic response types.
*   `views.View`: Base class for class-based views (methods: `get`, `post`).
*   `views.generic.ListView`, `views.generic.DetailView`: Generic views for common tasks.
*   `forms.Form`: Base class for forms. Fields like `forms.CharField`, `forms.BooleanField`.
*   `form.is_valid()`: Method to trigger form validation.
*   `form.cleaned_data`: Dictionary of validated data.
*   `contrib.auth.models.User`: Default user model.
*   `User.objects.create_user()`: Helper to create users.
*   `contrib.auth.models.AbstractBaseUser`, `BaseUserManager`: For custom user models.
*   `contrib.auth.backends.BaseBackend`: For custom authentication.
*   `{% csrf_token %}`: Template tag for CSRF protection in POST forms.
*   `@decorators.csrf.csrf_protect`: View decorator for CSRF protection.
*   `@transaction.atomic`: Decorator/context manager for database transactions.
*   `settings.py`: Main project configuration file (`DATABASES`, `SECRET_KEY`, `INSTALLED_APPS`, `MIDDLEWARE`, `AUTHENTICATION_BACKENDS`).
*   `test.TestCase`: Base class for tests needing database access.
*   `test.Client`: Utility for simulating requests in tests (`client.get`, `client.post`).

### Common Patterns & Best Practices / Pitfalls
*   **Security:** Always use `{% csrf_token %}`. Validate all user input (use Forms). Protect `SECRET_KEY`. Beware of XSS risks even with auto-escaping. Keep Django updated. Use `sensitive_variables`.
*   **ORM:** Use `bulk_create` for efficiency. Understand QuerySet laziness. Use `select_related`/`prefetch_related` for query optimization. Be careful when overriding `save()`.
*   **Forms:** Leverage Django Forms for validation and cleaning.
*   **Views:** Use generic class-based views where appropriate. Pass data via context dictionary.
*   **Transactions:** Wrap related database operations in `transaction.atomic`.
*   **Testing:** Write comprehensive tests for models and views.

---
This index summarizes the core concepts, APIs, and patterns for Django (Version Unknown). Consult the full source documentation (project_journal/context/source_docs/django-developer-llms-context-20250406.md) for exhaustive details.