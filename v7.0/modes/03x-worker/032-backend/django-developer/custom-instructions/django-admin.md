# Django: Admin Interface

Utilizing and customizing Django's automatic administration interface.

## Core Concept: Automatic CRUD Interface

One of Django's most powerful features is its built-in admin interface. It reads metadata from your models (`models.py`) to provide a production-ready interface where trusted users can manage content (perform CRUD operations) on your site's data.

**Key Features:**

*   **Automatic Generation:** Creates list, add, edit, and delete views for registered models with minimal code.
*   **Authentication & Permissions:** Integrates with Django's authentication system. Access is typically restricted to staff users (`is_staff=True`). Permissions (`add`, `change`, `delete`, `view`) defined on models are respected.
*   **Customization:** Highly customizable through `ModelAdmin` classes.
*   **User Management:** Provides interfaces for managing users and groups by default.

## Enabling and Accessing the Admin

1.  **Ensure `django.contrib.admin` is in `INSTALLED_APPS`** (in `settings.py`). This is included by default in new projects.
2.  **Include Admin URLs:** Ensure the admin URLs are included in your project's root `urls.py`:
    ```python
    # project/urls.py
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls), # Default path
        # ... other urls
    ]
    ```
3.  **Run Migrations:** Apply necessary database migrations for the admin app: `python manage.py migrate`.
4.  **Create a Superuser:** Create an initial admin user: `python manage.py createsuperuser`. Follow the prompts.
5.  **Run Development Server:** `python manage.py runserver`.
6.  **Access:** Navigate to `/admin/` (or the path you configured) in your browser and log in with the superuser credentials.

## Registering Models (`admin.py`)

To make your app's models manageable in the admin interface, you need to register them in the app's `admin.py` file.

```python
# myapp/admin.py
from django.contrib import admin
from .models import Author, Category, Article # Import your models

# Simple registration (uses default admin options)
admin.site.register(Author)
admin.site.register(Category)
# admin.site.register(Article) # Registering with default options

# --- Customizing the Admin ---
# Create a ModelAdmin class to customize how a model is displayed/managed

@admin.register(Article) # Alternative registration using decorator
class ArticleAdmin(admin.ModelAdmin):
    # --- List View Customization (list_display, list_filter, search_fields) ---

    # Fields to display in the list view
    list_display = ('title', 'author', 'status', 'publish_date', 'is_featured', 'was_published_recently')
    # Fields to allow filtering by in the sidebar
    list_filter = ('status', 'publish_date', 'author', 'categories')
    # Fields to enable searching on
    search_fields = ('title', 'content', 'author__user__username')
    # Fields to automatically populate based on others (e.g., slug from title)
    prepopulated_fields = {'slug': ('title',)}
    # Fields to link to the change page
    list_display_links = ('title',)
    # Enable editing directly in the list view for specified fields
    list_editable = ('status', 'is_featured')
    # Date hierarchy navigation
    date_hierarchy = 'publish_date'
    # Default ordering
    ordering = ('-publish_date',)

    # --- Change/Add Form Customization (fields, fieldsets, readonly_fields, inlines) ---

    # Control field order and grouping in the add/change form
    fieldsets = (
        (None, { # Section title (None for default)
            'fields': ('title', 'slug', 'author', 'status', 'is_featured') # Fields in this section
        }),
        ('Content', {
            'fields': ('content', 'categories')
        }),
        ('Date Information', {
            'fields': ('publish_date',),
            'classes': ('collapse',) # Make section collapsible
        }),
    )
    # Alternatively, use 'fields' for simpler ordering without sections:
    # fields = ('title', 'slug', 'author', 'content', 'status', 'publish_date', 'categories')

    # Display certain fields as read-only
    readonly_fields = ('created_at', 'updated_at')

    # Allow editing related models directly on the Article page (e.g., inline editing of comments)
    # inlines = [CommentInline] # Assuming a CommentInline class is defined

    # Customize ManyToMany field display (e.g., horizontal filter)
    filter_horizontal = ('categories',)
    # filter_vertical = ('categories',)

    # --- Custom Actions ---
    actions = ['make_published', 'make_draft']

    @admin.action(description='Mark selected articles as Published')
    def make_published(self, request, queryset):
        queryset.update(status='published')

    @admin.action(description='Mark selected articles as Draft')
    def make_draft(self, request, queryset):
        queryset.update(status='draft')

    # Customize display of boolean fields in list_display
    @admin.display(boolean=True, description='Published Recently?')
    def was_published_recently(self, obj):
        return obj.was_published_recently() # Call model method

# Example of an Inline ModelAdmin (for related models)
# class CommentInline(admin.TabularInline): # or admin.StackedInline
#     model = Comment # Assuming a Comment model with ForeignKey to Article
#     extra = 1 # Number of empty forms to display
```

The Django admin is a powerful tool for site administrators and content managers. Register your models in `admin.py` and use `ModelAdmin` classes to customize the list display, filtering, search, form layout, and actions available for each model.