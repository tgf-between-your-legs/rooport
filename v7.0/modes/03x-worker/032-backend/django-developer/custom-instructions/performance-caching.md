# Django: Performance & Caching

Basic strategies for optimizing Django application performance, focusing on ORM and caching.

## ORM Query Optimization

*   **Problem:** Inefficient database queries are a common performance bottleneck. The ORM can sometimes generate suboptimal queries if not used carefully, especially regarding related objects (N+1 problem).
*   **Key Techniques:**
    *   **`select_related(*fields)`:**
        *   **Purpose:** Follows **foreign-key** (one-to-one, many-to-one) relationships using a single, more complex query (SQL JOIN). Retrieves related objects along with the main object.
        *   **When:** Use for accessing related objects you *know* you will need immediately. Avoids separate queries for each related object later.
        *   **Example:**
            ```python
            # Avoids separate DB hit for each post.author
            posts = Post.objects.select_related('author__user').filter(status='published')
            for post in posts:
                print(post.title, post.author.user.username) # Author and User data already fetched
            ```
    *   **`prefetch_related(*lookups)`:**
        *   **Purpose:** Follows **many-to-many** and **reverse foreign-key** relationships. Performs separate lookups for the related objects and joins them in Python.
        *   **When:** Use for accessing related sets of objects where `select_related` isn't suitable (M2M, reverse FK).
        *   **Example:**
            ```python
            # Avoids separate DB hit for post.categories.all() for each post
            posts = Post.objects.filter(status='published').prefetch_related('categories')
            for post in posts:
                print(post.title)
                for category in post.categories.all(): # Categories already fetched in a separate query
                    print(f"- {category.name}")
            ```
    *   **`only(*fields)` / `defer(*fields)`:**
        *   **Purpose:** Control which fields are loaded from the database initially. `only()` loads *only* the specified fields. `defer()` loads *all except* the specified fields.
        *   **When:** Use if you only need a subset of fields, especially to avoid loading large `TextField`s unnecessarily. Deferred fields will be loaded on first access (causing another query).
        *   **Example:** `Post.objects.only('id', 'title').all()`
    *   **`values(*fields)` / `values_list(*fields, flat=False)`:**
        *   **Purpose:** Retrieve results as dictionaries (`values`) or tuples (`values_list`) instead of full model instances. More efficient if you only need raw data.
        *   **Example:** `User.objects.filter(is_active=True).values_list('email', flat=True)`
    *   **`count()` / `exists()`:**
        *   **Purpose:** Use `queryset.count()` instead of `len(queryset)` for counting (more efficient SQL `COUNT(*)`). Use `queryset.exists()` instead of `queryset.count() > 0` or `if queryset:` to check for existence (more efficient `EXISTS` query).
    *   **`update()` / `delete()` on QuerySets:** Perform bulk updates/deletes directly in the database without loading objects into memory. Faster but bypasses model `save()`/`delete()` methods and signals.
    *   **Indexing:** Ensure appropriate database indexes exist for fields used in `filter`, `exclude`, `order_by`. (Coordinate with `database-specialist`).

## Django Caching Framework

*   **Purpose:** Store the results of expensive operations (view outputs, computed data, query results) temporarily to avoid recomputing/re-fetching them on subsequent requests.
*   **Setup (`settings.py`):**
    *   Configure the `CACHES` setting. Multiple cache backends are supported.
    *   **Memory Cache (Development):** `django.core.cache.backends.locmem.LocMemCache` (Simple, per-process, not production-ready).
    *   **Database Cache:** `django.core.cache.backends.db.DatabaseCache` (Uses a database table, requires running `python manage.py createcachetable`).
    *   **Filesystem Cache:** `django.core.cache.backends.filebased.FileBasedCache`.
    *   **Memcached:** `django.core.cache.backends.memcached.PyMemcacheCache` or `PyLibMCCache` (Requires `memcached` server and Python library). Fast, distributed.
    *   **Redis:** Use third-party packages like `django-redis`. Fast, distributed, persistent options. **(Common choice for production)**.
    ```python
    # settings.py (Example using Redis via django-redis)
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://127.0.0.1:6379/1", # Your Redis server URL
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
            }
        }
    }
    ```
*   **Levels of Caching:**
    *   **Per-Site Cache:** Caches entire rendered pages. Enabled via `UpdateCacheMiddleware` and `FetchFromCacheMiddleware` in `MIDDLEWARE`. Simplest but least granular.
    *   **Per-View Cache:** Cache the output of individual views using the `@cache_page(timeout_seconds)` decorator or `cache_page` URLconf wrapper.
    *   **Template Fragment Caching:** Cache specific sections within a template using the `{% load cache %}` tag and `{% cache timeout_seconds fragment_name [vary_on_arg ...] %}` ... `{% endcache %}`. Allows caching parts of a page that change less frequently.
    *   **Low-Level Cache API:** Directly interact with the cache backend using `django.core.cache.cache`. Use `cache.get(key)`, `cache.set(key, value, timeout)`, `cache.delete(key)`, `cache.get_or_set(key, default_callable, timeout)`. Provides maximum control for caching arbitrary data (e.g., results of expensive computations, query results).

*   **Cache Invalidation:** Crucial but complex. How do you ensure the cache is updated when the underlying data changes?
    *   **Time-based:** Set reasonable timeouts. Simple but might serve stale data.
    *   **Manual:** Use `cache.delete(key)` or `cache.delete_many([...])` when data is updated (e.g., in a model's `save()` method or using signals). Can be hard to get right.
    *   **Key Versioning:** Change the cache key when data changes (e.g., include a timestamp or version number in the key).

Consult with `performance-optimizer` and `database-specialist` for advanced tuning.

*(Refer to the official Django documentation on Database query optimization and Caching.)*