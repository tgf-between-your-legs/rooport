# Django: Templates (DTL - Django Template Language)

Creating dynamic HTML using Django's built-in template system.

## Core Concept

Django templates are text files (usually HTML) that contain static content mixed with special syntax for inserting dynamic data and basic logic. The template engine processes these files, replacing variables and executing tags, to generate the final HTML response sent to the user.

## Syntax

DTL uses two main constructs:

1.  **Variables (`{{ variable }}`):**
    *   Output the value of a variable passed from the view's context.
    *   Uses dot notation (`.`) for accessing attributes of objects or dictionary keys (e.g., `{{ user.name }}`, `{{ post.author.bio }}`, `{{ my_dict.key }}`).
    *   Order of lookup: dictionary key -> attribute -> list index.
    *   If a variable doesn't exist, it defaults to an empty string (`''`) unless configured otherwise.
2.  **Tags (`{% tag %}`):**
    *   Perform logic, control flow, load external resources, or output specific content.
    *   Some tags require a closing tag (e.g., `{% if %}`...`{% endif %}`, `{% for %}`...`{% endfor %}`).

## Common Tags

*   **`{% if condition %}` / `{% elif condition %}` / `{% else %}` / `{% endif %}`:** Conditional rendering. Supports `and`, `or`, `not`, equality (`==`, `!=`), comparison (`<`, `>`, `<=`, `>=`), `in`.
    ```html
    {% if user.is_authenticated %}
      <p>Welcome, {{ user.username }}!</p>
    {% elif user.is_guest %}
      <p>Welcome, Guest!</p>
    {% else %}
      <p><a href="/login/">Login</a></p>
    {% endif %}
    ```
*   **`{% for item in item_list %}` / `{% empty %}` / `{% endfor %}`:** Loop over items in a list or queryset.
    *   `forloop.counter`: Current loop iteration (1-indexed).
    *   `forloop.counter0`: Current loop iteration (0-indexed).
    *   `forloop.first`: True if first iteration.
    *   `forloop.last`: True if last iteration.
    *   `{% empty %}`: Rendered if the list is empty.
    ```html
    <ul>
    {% for post in posts %}
      <li>{{ forloop.counter }}. {{ post.title }}</li>
    {% empty %}
      <li>No posts available.</li>
    {% endfor %}
    </ul>
    ```
*   **`{% url 'url_name' arg1 arg2 ... %}`:** Generates a URL based on the name defined in `urls.py`. Avoids hardcoding URLs.
    ```html
    <a href="{% url 'post_detail' post.slug post.id %}">Read More</a>
    ```
*   **`{% static 'path/to/file.css' %}`:** Generates the URL for a static file (requires `{% load static %}` at the top). Uses the `STATIC_URL` setting.
    ```html
    {% load static %}
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
    <img src="{% static 'images/logo.png' %}" alt="Logo">
    ```
*   **`{% csrf_token %}`:** **Essential** security tag for forms submitted via POST to prevent Cross-Site Request Forgery. Place it inside any `<form method="post">`.
*   **`{% load <tag_library> %}`:** Loads custom template tags or filters defined in a template tag library.
*   **`{% include 'path/to/other_template.html' %}`:** Includes the content of another template file.
*   **`{% extends 'path/to/base_template.html' %}`:** Template inheritance. Indicates this template extends a base template. Must be the first tag.
*   **`{% block <block_name> %}` / `{% endblock %}`:** Defines blocks that can be overridden by child templates using `{% extends %}`. Content within the block in the base template serves as default content.

## Common Filters (`{{ variable|filter }}`)

Modify the output of variables.

*   `date:"D d M Y"`: Formats a date/datetime object (e.g., `{{ post.publish_date|date:"Y-m-d" }}`).
*   `length`: Returns the length of a list or string.
*   `lower`, `upper`: Converts string to lowercase/uppercase.
*   `truncatewords:N`: Truncates string after N words.
*   `safe`: Marks a string as safe for HTML output (disables auto-escaping). **Use with extreme caution** only on trusted content to prevent XSS.
*   `escape`: Explicitly escapes HTML characters.
*   `default:"fallback"`: Provides a default value if the variable is falsey (empty string, None, False, 0).
*   `filesizeformat`: Formats a number of bytes into a human-readable file size.
*   `pluralize`: Adds 's' if value is not 1 (e.g., `{{ count }} item{{ count|pluralize }}`).

## Template Inheritance

*   **Purpose:** Define a base structure (e.g., `base.html`) with common elements (header, footer, navigation) and define `{% block %}` tags for areas that child templates can override.
*   **`base.html` Example:**
    ```html
    <!DOCTYPE html>
    <html>
    <head><title>{% block title %}My Site{% endblock %}</title></head>
    <body>
      <header>{% include '_header.html' %}</header>
      <main>
        {% block content %}
        <!-- Default content goes here -->
        {% endblock %}
      </main>
      <footer>{% include '_footer.html' %}</footer>
    </body>
    </html>
    ```
*   **Child Template Example:**
    ```html
    {% extends 'base.html' %}

    {% block title %}About Us{% endblock %}

    {% block content %}
      <h1>About Our Company</h1>
      <p>Details about the company...</p>
    {% endblock %}
    ```

## Context

*   Views pass data to templates via a context dictionary as the third argument to `render()`:
    ```python
    # myapp/views.py
    from django.shortcuts import render
    from .models import Post

    def post_list(request):
        posts = Post.objects.filter(status='published')
        context = {'posts': posts, 'page_title': 'Blog'}
        return render(request, 'myapp/post_list.html', context)
    ```

*(Refer to the official Django Template Language documentation: https://docs.djangoproject.com/en/stable/ref/templates/language/)*