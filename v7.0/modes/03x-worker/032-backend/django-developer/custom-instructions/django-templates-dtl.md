# Django: Templates (DTL - Django Template Language)

Using Django's built-in template system for rendering dynamic HTML.

## Core Concept: Presentation Logic

Django Templates provide a designer-friendly syntax for defining the structure of output documents (typically HTML). They separate presentation logic from Python view logic. Templates are rendered with a **context** (a dictionary-like object passed from the view) containing variables to be displayed.

**Key Features:**

*   **Syntax:** Uses specific tags and variable placeholders embedded within standard HTML.
    *   Variables: `{{ variable_name }}`
    *   Tags: `{% tag_name %}`
    *   Filters: `{{ variable|filter_name }}`
    *   Comments: `{# comment #}` (single-line) or `{% comment %} multi-line {% endcomment %}`
*   **Context:** A dictionary passed from the view containing data to be rendered in the template. Variables in `{{ }}` are looked up in this context.
*   **Template Loading:** Django searches for templates in directories specified in the `TEMPLATES` setting in `settings.py` (usually within each app's `templates/` directory and a project-level `templates/` directory).
*   **Template Inheritance:** A powerful way to reuse common HTML structure (like headers, footers, navigation). Define a base template with `{% block %}` tags, and child templates `{% extends %}` the base and override specific blocks.
*   **Built-in Tags & Filters:** Provides numerous tags (e.g., `if`, `for`, `url`, `load`, `static`, `csrf_token`) and filters (e.g., `date`, `length`, `lower`, `safe`, `truncatewords`) for common tasks.
*   **Custom Tags & Filters:** Allows defining custom template tags and filters in Python for reusable presentation logic.
*   **Auto-escaping:** Django automatically escapes HTML characters in variable output (`{{ variable }}`) by default to prevent Cross-Site Scripting (XSS) attacks. Use the `|safe` filter only if you explicitly trust the variable's content and need to render raw HTML.

## Basic Syntax Examples

```html
<!-- myapp/templates/myapp/article_detail.html -->
{% extends "base.html" %} <!-- Inherit from base template -->
{% load static %} <!-- Load static files tag library -->

{% block title %}{{ article.title }} - My Blog{% endblock %} <!-- Override title block -->

{% block content %} <!-- Override content block -->
  <article>
    <h1>{{ article.title }}</h1>

    {# Display author information if available #}
    {% if article.author %}
      <p>By {{ article.author.user.get_full_name|default:"Unknown Author" }} on {{ article.publish_date|date:"F j, Y" }}</p>
    {% else %}
      <p>Published on {{ article.publish_date|date:"F j, Y" }}</p>
    {% endif %}

    {# Display categories using a loop #}
    {% if article.categories.all %}
      <p>Categories:
        {% for category in article.categories.all %}
          <a href="{% url 'myapp:category_detail' category.slug %}">{{ category.name }}</a>{% if not forloop.last %}, {% endif %}
        {% empty %}
          No categories assigned.
        {% endfor %}
      </p>
    {% endif %}

    {# Display article content - use |safe only if content is trusted HTML #}
    {# Usually better to use a filter like |markdown or |bleach for user-generated content #}
    <div class="content">
      {{ article.content|linebreaksbr }} {# Convert line breaks to <br> #}
    </div>

    {# Link to static file #}
    <img src="{% static 'images/default_article.png' %}" alt="Article image">

    {# Link back to list view using URL reversing #}
    <p><a href="{% url 'myapp:article_list' %}">Back to list</a></p>

  </article>
{% endblock %}
```

```html
<!-- templates/base.html (Example Base Template) -->
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{% block title %}My Site{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'css/base.css' %}">
    {% block extra_head %}{% endblock %}
</head>
<body>
    <header>
        <h1>My Awesome Blog</h1>
        <nav>
            <a href="{% url 'myapp:article_list' %}">Home</a>
            <!-- Add other navigation links -->
        </nav>
    </header>

    <main>
        {% block content %}
        <p>Default content goes here.</p>
        {% endblock %}
    </main>

    <footer>
        <p>&copy; {% now "Y" %} My Site</p> {# Example using 'now' tag #}
    </footer>
    {% block extra_body %}{% endblock %}
</body>
</html>
```

## Key Tags & Filters

*   **Tags (`{% %}`):**
    *   `if`/`elif`/`else`/`endif`: Conditional logic.
    *   `for`/`empty`/`endfor`: Looping over iterables (`forloop.counter`, `forloop.first`, `forloop.last`).
    *   `extends`: Template inheritance.
    *   `block`/`endblock`: Defines replaceable sections in templates.
    *   `include`: Includes another template.
    *   `load`: Loads custom template tag libraries or built-ins like `static`.
    *   `static`: Generates URL for static files (requires `{% load static %}`).
    *   `url`: Reverses a URL pattern name to generate a URL (requires `{% load url %}` or just use name directly in newer Django).
    *   `csrf_token`: Essential security tag for POST forms.
    *   `now`: Displays the current date/time.
*   **Filters (`{{ | }}`):**
    *   `date`: Formats dates/datetimes (e.g., `|date:"Y-m-d"`).
    *   `time`: Formats times.
    *   `length`: Returns the length of a list or string.
    *   `lower`/`upper`: Converts case.
    *   `truncatewords`/`truncatechars`: Truncates text.
    *   `safe`: Marks a string as safe for HTML output (disables auto-escaping - use with extreme caution!).
    *   `linebreaks`/`linebreaksbr`: Converts plain text line breaks to HTML `<p>` or `<br>`.
    *   `default`: Provides a default value if the variable is False or empty.

Django templates provide a powerful yet restricted language focused on presentation. Keep complex logic in views and pass necessary data via the context. Leverage template inheritance and built-in tags/filters for efficiency and maintainability. Always be mindful of security, especially regarding `|safe` and `{% csrf_token %}`.