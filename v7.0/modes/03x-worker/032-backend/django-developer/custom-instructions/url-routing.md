# Django: URL Routing (`urls.py`)

Mapping URL patterns to view functions or classes in Django.

## Core Concept: URLconf

*   Django uses URL configurations (URLconfs) to map requested URLs to the appropriate view code that should handle them.
*   A URLconf is a Python module containing a list named `urlpatterns`. Each item in this list maps a URL pattern to a view.
*   The main URLconf is specified by the `ROOT_URLCONF` setting in `settings.py`.
*   It's common practice to have a root URLconf that includes URLconfs from individual apps.

## `path()` Function

*   The primary function used in `urlpatterns` to define routes.
*   **Syntax:** `path(route, view, kwargs=None, name=None)`
    *   **`route` (string):** The URL pattern to match. Can include converters to capture parts of the URL. Does **not** match GET/POST parameters or domain name. Patterns do **not** start with a `/` but **do** end with one (usually).
    *   **`view` (callable):** The view function or the `.as_view()` method of a class-based view that should handle requests matching the route.
    *   **`kwargs` (dict, optional):** Arbitrary keyword arguments to pass to the target view.
    *   **`name` (string, optional):** A unique name for this URL pattern. Allows you to refer to it unambiguously from elsewhere in Django, especially templates (`{% url 'name' %}`). **Highly recommended.**

## URL Converters

*   Used within the `route` string to capture parts of the URL and pass them as arguments to the view.
*   **Syntax:** `<converter:parameter_name>`
*   **Built-in Converters:**
    *   `str`: Matches any non-empty string (excluding `/`). Default if no converter specified.
    *   `int`: Matches zero or any positive integer.
    *   `slug`: Matches any slug string (ASCII letters/numbers, hyphens, underscores).
    *   `uuid`: Matches a formatted UUID.
    *   `path`: Matches any non-empty string, including `/`.

## Example: Project `urls.py` (Root URLconf)

```python
# project/urls.py
from django.contrib import admin
from django.urls import path, include # Import include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include URLs from the 'blog' app, prefixing them with 'blog/'
    path('blog/', include('blog.urls', namespace='blog')),
    # Include URLs from the 'users' app
    path('accounts/', include('users.urls', namespace='users')),
    # Example: Include Django's built-in auth views
    path('accounts/', include('django.contrib.auth.urls')),
]
```

## Example: App `urls.py` (`blog/urls.py`)

```python
# blog/urls.py
from django.urls import path
from . import views # Import views from the current app

# Define an app namespace (matches the namespace in the include() call)
app_name = 'blog'

urlpatterns = [
    # Example: /blog/
    path('', views.post_list, name='post_list'), # Function-based view

    # Example: /blog/post/my-first-post/
    path('post/<slug:post_slug>/', views.post_detail, name='post_detail'),

    # Example: /blog/archive/2023/
    path('archive/<int:year>/', views.post_archive_year, name='post_archive_year'),

    # Example: /blog/create/ (Class-based view)
    path('create/', views.PostCreateView.as_view(), name='post_create'),

    # Example: /blog/post/123/update/
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
]
```

## `include()` Function

*   Allows referencing other URLconfs.
*   When Django encounters `include()`, it chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing.
*   **`namespace` Argument:** Provides a namespace for the included URL patterns. This allows you to reverse URLs unambiguously, even if different apps use the same URL name (e.g., `{% url 'blog:post_detail' ... %}` vs. `{% url 'news:post_detail' ... %}`).

## URL Reversing (`{% url %}` and `reverse()`)

*   **Purpose:** Avoid hardcoding URLs in templates and views. Use the `name` provided in `path()`.
*   **In Templates:** `{% url 'url_name' arg1 arg2 ... %}`
    *   If using namespaces: `{% url 'namespace:url_name' arg1 ... %}`
    ```html
    <a href="{% url 'blog:post_detail' post.slug %}">View Post</a>
    ```
*   **In Views (Python):** `reverse('url_name', args=[...], kwargs={...})`
    *   If using namespaces: `reverse('namespace:url_name', ...)`
    ```python
    from django.urls import reverse
    from django.shortcuts import redirect

    def my_view(request):
        # ... logic ...
        # Redirect to the named URL 'blog:post_list'
        return redirect(reverse('blog:post_list'))
    ```

## How Django Processes a Request

1.  Receives request URL (e.g., `/blog/post/my-slug/`).
2.  Loads the root URLconf (`ROOT_URLCONF`).
3.  Iterates through `urlpatterns` in order.
4.  Matches `/blog/` against `path('blog/', include('blog.urls', namespace='blog'))`.
5.  Strips `/blog/` and sends `post/my-slug/` to `blog.urls`.
6.  `blog.urls` iterates through its `urlpatterns`.
7.  Matches `post/<slug:post_slug>/` against `path('post/<slug:post_slug>/', views.post_detail, name='post_detail')`.
8.  Calls `views.post_detail(request, post_slug='my-slug')`.
9.  If no pattern matches, Django raises a 404 error.

*(Refer to the official Django URL dispatcher documentation: https://docs.djangoproject.com/en/stable/topics/http/urls/)*