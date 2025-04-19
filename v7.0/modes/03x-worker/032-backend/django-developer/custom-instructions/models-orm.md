# Django: Models & ORM

Defining database schema and interacting with data using Django's Object-Relational Mapper (ORM).

## Core Concept: Models (`models.py`)

*   **Definition:** A Django model is a Python class that subclasses `django.db.models.Model`. Each model maps to a single database table.
*   **Fields:** Attributes on the model class represent database fields. Django provides various field types (`CharField`, `IntegerField`, `DateField`, `ForeignKey`, `ManyToManyField`, etc.).
*   **`models.py`:** Models are typically defined within an app's `models.py` file.
*   **Primary Key:** Django automatically adds an auto-incrementing primary key field named `id` unless you specify `primary_key=True` on another field.

```python
# myapp/models.py
from django.db import models
from django.contrib.auth.models import User # Example relationship to built-in User

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "categories" # Correct plural name in Admin

    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique_for_date='publish_date')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True) # Set on creation
    updated_date = models.DateTimeField(auto_now=True) # Set on save
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    categories = models.ManyToManyField(Category, related_name='posts', blank=True)

    class Meta:
        ordering = ('-publish_date',) # Default ordering for queries

    def __str__(self):
        return self.title

    # Example custom method
    def was_published_recently(self):
        # ... logic ...
        return True
```

## Common Field Types

*   `CharField(max_length=...)`: Text field.
*   `TextField()`: Large text field.
*   `IntegerField()`, `FloatField()`, `DecimalField(max_digits=..., decimal_places=...)`: Numeric types.
*   `BooleanField(default=False)`: True/False.
*   `DateField(auto_now=False, auto_now_add=False)`, `DateTimeField(...)`: Date/Timestamp.
*   `EmailField()`, `URLField()`, `SlugField()`: Specialized character fields.
*   `FileField(upload_to=...)`, `ImageField(...)`: File uploads.
*   **Relationships:**
    *   `ForeignKey(OtherModel, on_delete=models.CASCADE, related_name=...)`: Many-to-one relationship. `on_delete` specifies behavior when the related object is deleted (e.g., `CASCADE`, `PROTECT`, `SET_NULL`). `related_name` defines the reverse accessor name.
    *   `ManyToManyField(OtherModel, related_name=..., blank=True)`: Many-to-many relationship. Django creates an intermediate table.
    *   `OneToOneField(OtherModel, on_delete=models.CASCADE, primary_key=False)`: One-to-one relationship.

## Field Options

*   `null=True`: Allows `NULL` values in the database (default: `False`).
*   `blank=True`: Allows the field to be blank in forms/admin (default: `False`). Often used with `null=True` for optional text-based fields.
*   `default=...`: Default value for the field.
*   `unique=True`: Ensures the value in this field is unique across the table.
*   `choices=[...]`: Provides a list of choices for the field (used by forms/admin).
*   `primary_key=True`: Designates this field as the primary key.
*   `verbose_name="..."`: Human-readable name for the field.

## Meta Options (`class Meta`)

*   Inner class within a model to define metadata.
*   `ordering = [...]`: Default ordering for querysets (e.g., `['-publish_date']`).
*   `verbose_name`, `verbose_name_plural`: Names used in the Django admin.
*   `unique_together = [...]`: Define multi-column uniqueness constraints.
*   `db_table = '...'`: Specify a custom database table name.

## Migrations (`manage.py makemigrations` & `migrate`)

*   **Purpose:** Manage changes to your database schema based on changes to your `models.py` files.
*   **Workflow:**
    1.  Modify your `models.py`.
    2.  Run `python manage.py makemigrations <app_name>`: Django detects changes and creates a new migration file in the app's `migrations/` directory. This file contains Python code describing the schema changes.
    3.  Run `python manage.py migrate`: Django applies any unapplied migration files to the database, altering the schema.
*   **Important:** Always run `makemigrations` and `migrate` after changing models. Review migration files before applying them, especially complex ones.

## QuerySets (ORM Interaction)

*   **Access:** Access QuerySets via the model's manager, typically `ModelName.objects`.
*   **Retrieving Objects:**
    *   `all()`: Get all objects.
    *   `filter(**kwargs)`: Get objects matching criteria (e.g., `Post.objects.filter(status='published', author__user__username='alice')`). Uses field lookups (`__exact`, `__iexact`, `__contains`, `__icontains`, `__gt`, `__lt`, `__in`, `__isnull`).
    *   `exclude(**kwargs)`: Get objects *not* matching criteria.
    *   `get(**kwargs)`: Get a *single* object matching criteria. Raises `DoesNotExist` or `MultipleObjectsReturned` if not exactly one match.
*   **Creating Objects:**
    *   `create(**kwargs)`: Creates, saves, and returns a new object in one step.
    *   `obj = MyModel(...)`, `obj.save()`: Create instance, then save.
*   **Updating Objects:**
    *   `obj.field = value`, `obj.save()`: Update instance, then save.
    *   `QuerySet.update(**kwargs)`: Update multiple objects matching the queryset directly in the database (more efficient, but doesn't call model `save()` method).
*   **Deleting Objects:**
    *   `obj.delete()`: Delete a single instance.
    *   `QuerySet.delete()`: Delete multiple objects matching the queryset.
*   **QuerySet Laziness:** QuerySets are lazy. The database query is only executed when the QuerySet is evaluated (e.g., by iterating over it, slicing it, calling `len()`, `list()`, or accessing a single object with `get()`).
*   **Optimization:**
    *   `select_related('foreign_key_field')`: Follows foreign-key relationships via JOINs, retrieving related objects in the same query. For one-to-one and many-to-one.
    *   `prefetch_related('many_to_many_field', 'reverse_foreign_key_field')`: Performs separate lookups for related objects and joins them in Python. For many-to-many and reverse foreign-key relationships. Reduces the number of queries significantly (avoids N+1).

*(Refer to the official Django documentation on Models, Fields, QuerySets, and Migrations.)*