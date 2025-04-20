# Django: URL Dispatcher & Routing

Mapping URL paths to specific views in a Django application.

## Core Concept: Connecting URLs to Views

Django's URL dispatcher is responsible for examining the requested URL path and determining which Python view function or class method should handle the request. This mapping is defined in `urls.py` files.

**Key Components:**

*   **URLconf (URL Configuration):** Python modules (`urls.py`) containing lists of URL patterns.
*   **`urlpatterns`:** A required list or tuple within a `urls.py` file. Each element in this list defines a mapping between a URL pattern and a view.
*   **`path()` function:** The primary function used to define URL patterns. It takes the route string, the view function/class, optional keyword arguments, and an optional `name`.
*   **`include()` function:** Used in the *project's* root `urls.py` to include URL patterns defined within individual *app* `urls.py` files. This promotes modularity.
*   **URL Reversing:** The ability to generate URLs dynamically based on the `name` given to a URL pattern, rather than hardcoding paths. This makes applications more maintainable. Use the `{% url %}` template tag or the `reverse()` function in Python code.
*   **Namespaces:** Used to prevent URL name collisions between different apps (e.g., two apps might both have a 'detail' view). Define an `app_name` variable in the app's `urls.py` and use it when including (`include(('myapp.urls', 'myapp'), namespace='myapp')`) and reversing (`{% url 'myapp:detail' pk=1 %}`).

## Defining URL Patterns

**1. Project `urls.py`:**

*   Located in the project's main configuration directory (alongside `settings.py`).
*   Defines top-level routes, including the admin site and includes for individual apps.

```python
# project/urls.py
from django.contrib import admin
from django.urls import path, include # Import include

urlpatterns = [
    path('admin/', admin.site.urls), # Default admin site URL
    # Include URLs from 'myapp' using a namespace
    path('articles/', include(('myapp.urls', 'myapp'), namespace='myapp')),
    # Include URLs from another app
    path('accounts/', include('django.contrib.auth.urls')), # Built-in auth URLs
    # Add other app includes or project-level paths here
]
```

**2. App `urls.py`:**

*   Located within an individual app's directory (e.g., `myapp/urls.py`).
*   Defines URL patterns specific to that app.
*   Should define an `app_name` variable for namespacing.

```python
# myapp/urls.py
from django.urls import path
from . import views # Import views from the current app

app_name = 'myapp' # Define the namespace

urlpatterns = [
    # Example: /articles/ (List view)
    path('', views.article_list, name='article_list'),
    # Using FBV

    # Example: /articles/create/ (Create view)
    path('create/', views.article_create, name='article_create'),
    # Using FBV

    # Example: /articles/123/ (Detail view using path converter)
    path('<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    # Using generic CBV DetailView. '<int:pk>' captures an integer into the 'pk' keyword argument.

    # Example: /articles/123/update/ (Update view)
    path('<int:pk>/update/', views.ArticleUpdateView.as_view(), name='article_update'),
    # Using generic CBV UpdateView

    # Example: /articles/123/delete/ (Delete view)
    path('<int:pk>/delete/', views.ArticleDeleteView.as_view(), name='article_delete'),
    # Using generic CBV DeleteView

    # Example: /articles/category/tech/ (Category detail view using slug)
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    # Using FBV and '<slug:slug>' converter

    # Example: API endpoint (could also be in a separate api_urls.py)
    path('api/<int:pk>/', views.api_article_data, name='api_article_data'),
]
```

**Path Converters:**

Django provides built-in converters to capture parts of the URL path and pass them as keyword arguments to the view:

*   `str`: Matches any non-empty string (excluding `/`). Default.
*   `int`: Matches zero or any positive integer.
*   `slug`: Matches any slug string (ASCII letters/numbers, hyphens, underscores).
*   `uuid`: Matches a formatted UUID.
*   `path`: Matches any non-empty string, *including* `/`.

## URL Reversing

Avoid hardcoding URLs. Use the `name` defined in `path()`:

**In Templates:**

```html
<!-- Link to article detail view -->
<a href="{% url 'myapp:article_detail' pk=article.pk %}">{{ article.title }}</a>

<!-- Link to article list view (no arguments) -->
<a href="{% url 'myapp:article_list' %}">All Articles</a>
```

**In Views (Python):**

```python
from django.urls import reverse
from django.shortcuts import redirect

def some_view(request):
    # ... logic ...
    # Redirect to the article list
    return redirect(reverse('myapp:article_list'))

def create_and_redirect(request):
    # ... create article_obj ...
    # Redirect to the detail view of the created article
    return redirect(reverse('myapp:article_detail', kwargs={'pk': article_obj.pk}))
    # Or, if the model has a get_absolute_url() method:
    # return redirect(article_obj.get_absolute_url())
```

The URL dispatcher is fundamental to routing requests in Django. Define clear, consistent URL patterns using `path()`, organize them into apps using `include()`, and always use named URLs with `{% url %}` or `reverse()` for maintainability.