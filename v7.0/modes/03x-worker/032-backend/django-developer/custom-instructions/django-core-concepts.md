# Django: Core Concepts

Fundamental concepts of the Django web framework.

## 1. MVT Pattern (Model-View-Template)

Django follows a variation of the Model-View-Controller (MVC) pattern, often referred to as Model-View-Template (MVT).

*   **Model:** Represents the data structure, typically mapping to database tables. Handles data access and validation logic. (Defined in `models.py`).
*   **View:** Handles the request/response logic. It receives an HTTP request, interacts with models (to fetch or save data), processes data, and selects a template to render, passing necessary context data to it. (Defined in `views.py` as functions or classes).
*   **Template:** Defines the presentation layer (usually HTML). It receives context data from the view and uses Django Template Language (DTL) to display the data dynamically and structure the output. (Stored in `templates/` directories).
*   **URL Dispatcher:** Maps incoming URL paths to specific view functions or classes. (Defined in `urls.py`).

**Request Flow:** Request -> URL Dispatcher -> View -> Model(s) -> Template -> Response

## 2. Project vs. Apps

*   **Project:** Represents the entire web application or website. Contains project-wide configurations (`settings.py`, root `urls.py`). A project is composed of one or more apps.
*   **App:** A self-contained module within a project that handles a specific piece of functionality (e.g., a blog app, a user authentication app, a polls app). Apps are designed to be reusable across different projects. Each app typically has its own `models.py`, `views.py`, `urls.py` (optional), `forms.py`, `admin.py`, `tests.py`, and `templates/app_name/` directory. Apps must be listed in the `INSTALLED_APPS` setting in `settings.py`.

## 3. Models & ORM (Object-Relational Mapper)

*   **Models:** Python classes defined in `models.py` that subclass `django.db.models.Model`. Each class maps to a database table, and each attribute (field) maps to a table column.
*   **Fields:** Define the type of data stored (e.g., `CharField`, `IntegerField`, `DateField`, `ForeignKey`, `ManyToManyField`).
*   **ORM:** Allows you to interact with your database using Python code instead of writing raw SQL. Django's ORM provides a high-level API for creating, retrieving, updating, and deleting records (CRUD).
*   **QuerySets:** Represent a collection of objects from the database. They are lazy (database query is executed only when the QuerySet is evaluated) and allow chaining of filters (`filter()`, `exclude()`) and ordering (`order_by()`).

## 4. Views (Request Handlers)

*   **Purpose:** Receive `HttpRequest` objects and return `HttpResponse` objects.
*   **Function-Based Views (FBVs):** Simple Python functions taking `request` as the first argument.
*   **Class-Based Views (CBVs):** Python classes inheriting from `django.views.View` or generic views (`ListView`, `DetailView`, etc.). Provide structure and reusability through inheritance and mixins. Handle different HTTP methods via class methods (e.g., `get()`, `post()`).

## 5. Templates (DTL - Django Template Language)

*   **Purpose:** Define the structure of the output (usually HTML).
*   **Syntax:**
    *   Variables: `{{ variable_name }}` (Access context data passed from the view). Dot notation for accessing attributes/dictionary keys (`{{ user.name }}`).
    *   Tags: `{% tag_name %}` (Perform logic like loops, conditionals, template inheritance). Common tags: `{% if %}`, `{% for %}`, `{% url 'name' %}`, `{% load static %}`, `{% extends %}`, `{% block %}`.
    *   Filters: `{{ variable|filter_name:"argument" }}` (Modify variable display). Common filters: `date`, `length`, `lower`, `truncatewords`.
*   **Template Inheritance:** Define a base template (`base.html`) with common structure and `{% block %}` tags. Child templates `{% extends "base.html" %}` and override specific blocks.

## 6. URL Dispatcher

*   **Purpose:** Maps URL paths to views.
*   **`urls.py`:** Project root `urls.py` includes URL patterns from individual apps using `include()`. App-specific `urls.py` files define patterns using `path()`.
*   **`path(route, view, name='url_name')`:** Defines a single URL pattern.
    *   `route`: URL string, can include converters like `<int:pk>`.
    *   `view`: The view function or `View.as_view()` for CBVs.
    *   `name`: A unique name used for reversing URLs (e.g., in templates `{% url 'name' %}` or views `reverse('name')`).

## 7. Forms

*   **Purpose:** Handle user input submission and validation.
*   **`forms.Form` / `forms.ModelForm`:** Classes defined in `forms.py`. `ModelForm` automatically generates fields based on a Django model.
*   **Validation:** Define validation rules per field or for the form as a whole. Call `form.is_valid()` in the view to trigger validation. Access cleaned data via `form.cleaned_data`.
*   **Rendering:** Render forms in templates using tags like `{{ form.as_p }}`, `{{ form.as_ul }}`, or manually looping through fields (`{% for field in form %}`). Crucial for security (`{% csrf_token %}`).

These core concepts form the foundation of building applications with Django's MVT architecture.