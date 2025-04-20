# Django: Models & ORM

Defining data structures and interacting with the database using Django's Object-Relational Mapper.

## Core Concept: Mapping Python to SQL

Django's ORM provides a Pythonic way to define your database schema and interact with your data, abstracting away most raw SQL.

*   **Models:** Python classes in `models.py` that subclass `django.db.models.Model`. Each model class represents a database table.
*   **Fields:** Attributes defined within a model class represent table columns. Django provides various field types (`CharField`, `IntegerField`, `DateTimeField`, `ForeignKey`, `ManyToManyField`, etc.) that map to corresponding SQL column types.
*   **Migrations:** Django can automatically generate SQL migration files (`manage.py makemigrations`) based on changes detected in your `models.py`. These migrations track schema changes and can be applied to update the database schema (`manage.py migrate`).
*   **QuerySets:** The primary way to retrieve objects from the database. They represent a collection of database rows and allow filtering, slicing, ordering, and other operations using Python methods before hitting the database. QuerySets are lazy – the database query is only executed when the QuerySet is evaluated.

## Defining Models (`models.py`)

```python
# myapp/models.py
from django.db import models
from django.contrib.auth.models import User # Example: Linking to built-in User
from django.utils import timezone
from django.urls import reverse # For get_absolute_url

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bio = models.TextField(blank=True, null=True)
    # Add other author-specific fields

    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "categories" # Correct plural name in Admin
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # Example assuming you have a URL pattern named 'category_detail'
        return reverse('myapp:category_detail', kwargs={'slug': self.slug})


class Article(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique_for_date='publish_date')
    # Use ForeignKey for Many-to-One relationships
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='articles')
    # Use ManyToManyField for Many-to-Many relationships
    categories = models.ManyToManyField(Category, related_name='articles', blank=True)
    content = models.TextField()
    publish_date = models.DateTimeField(default=timezone.now, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True) # Automatically set on creation
    updated_at = models.DateTimeField(auto_now=True)     # Automatically set on save
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', db_index=True)
    is_featured = models.BooleanField(default=False, db_index=True)

    class Meta:
        ordering = ['-publish_date'] # Default ordering for querysets
        # Example: Index for common filtering
        indexes = [
            models.Index(fields=['status', 'publish_date']),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Example assuming you have a URL pattern named 'article_detail'
        return reverse('myapp:article_detail', kwargs={'pk': self.pk})


    # Example custom model method
    def was_published_recently(self):
        now = timezone.now()
        return now - timezone.timedelta(days=1) <= self.publish_date <= now

```

**Common Field Types:**

*   `CharField`: Text field (requires `max_length`).
*   `TextField`: Large text field.
*   `IntegerField`, `FloatField`, `DecimalField`: Numeric types.
*   `BooleanField`: True/False.
*   `DateField`, `DateTimeField`, `TimeField`: Date/time types (`auto_now`, `auto_now_add`).
*   `EmailField`, `URLField`, `SlugField`: Specialized character fields with validation.
*   `FileField`, `ImageField`: For file uploads.
*   `JSONField`: For storing JSON data (database support required).
*   **Relationships:**
    *   `ForeignKey`: Many-to-one (requires `on_delete` option, e.g., `models.CASCADE`, `models.SET_NULL`).
    *   `ManyToManyField`: Many-to-many (often uses `related_name`).
    *   `OneToOneField`: One-to-one (like `ForeignKey` with `unique=True`).

**Field Options:**

*   `max_length`: Required for `CharField`.
*   `blank=True`: Allows empty value in forms.
*   `null=True`: Allows `NULL` value in the database.
*   `default`: Default value for the field.
*   `unique=True`: Enforces database uniqueness constraint.
*   `choices`: Provides dropdown options in forms/admin.
*   `verbose_name`: Human-readable field name.
*   `help_text`: Additional help text in forms/admin.
*   `db_index=True`: Creates a database index on the field.

**`Meta` Options:**

*   `ordering`: Default ordering for QuerySets.
*   `verbose_name`, `verbose_name_plural`: Names used in the admin.
*   `unique_together`: Enforce uniqueness across multiple fields.
*   `indexes`: Define more complex database indexes.

## Querying Data (Views, Shell, etc.)

Django's ORM provides managers (usually `objects`) on model classes to perform database queries.

```python
# --- Retrieving Objects ---

# Get all articles
all_articles = Article.objects.all()

# Get a single article by primary key (pk)
try:
    article = Article.objects.get(pk=1)
except Article.DoesNotExist:
    print("Article not found")

# Filter articles (returns a QuerySet)
published_articles = Article.objects.filter(status='published')
recent_articles = Article.objects.filter(publish_date__gte=timezone.now() - timezone.timedelta(days=7))
articles_by_alice = Article.objects.filter(author__user__username='alice') # Follow relationships

# Complex lookups (Q objects for OR conditions)
from django.db.models import Q
complex_filter = Article.objects.filter(
    Q(title__icontains='django') | Q(content__icontains='django'), # Case-insensitive contains
    status='published'
)

# Exclude objects
drafts = Article.objects.exclude(status='published')

# Order results
ordered_articles = Article.objects.order_by('title', '-publish_date') # Sort by title asc, then date desc

# Limit results (slicing)
first_five = Article.objects.all()[:5]

# --- Creating Objects ---
new_article = Article.objects.create(
    title='Intro to ORM',
    slug='intro-to-orm',
    author=some_author_instance, # Assign ForeignKey instance
    content='...'
)
# Or:
# article = Article(title='...', ...)
# article.save()

# Add ManyToMany relationships (after saving both instances)
category_tech = Category.objects.get(slug='tech')
new_article.categories.add(category_tech)

# --- Updating Objects ---
article = Article.objects.get(pk=1)
article.title = 'Updated Title'
article.save() # Saves only changed fields by default

# Update multiple objects
Article.objects.filter(status='draft').update(status='archived') # More efficient bulk update

# --- Deleting Objects ---
article = Article.objects.get(pk=1)
article.delete()

Article.objects.filter(status='archived').delete() # Bulk delete

# --- QuerySet Laziness ---
# QuerySets are lazy. No DB query is made until evaluated:
qs = Article.objects.filter(status='published') # No DB query yet
print(qs) # DB query executed here (when iterating/printing)
count = qs.count() # DB query executed here (optimized COUNT(*))
exists = qs.exists() # DB query executed here (optimized EXISTS)

# --- Performance: select_related / prefetch_related ---
# Use select_related for ForeignKey/OneToOneField (SQL JOIN)
articles = Article.objects.select_related('author__user').filter(status='published')
for article in articles:
    print(article.title, article.author.user.username) # No extra DB query for author/user

# Use prefetch_related for ManyToManyField/reverse ForeignKey (separate SQL queries, joined in Python)
authors = Author.objects.prefetch_related('articles')
for author in authors:
    print(author.user.username)
    for article in author.articles.all(): # No extra DB query per author for articles
        print(f"- {article.title}")

```

The Django ORM is a powerful tool for database interaction. Define models clearly, understand relationships, and use QuerySet methods effectively, including `select_related` and `prefetch_related` for performance. Remember to create and apply migrations (`makemigrations`, `migrate`) whenever you change your models.