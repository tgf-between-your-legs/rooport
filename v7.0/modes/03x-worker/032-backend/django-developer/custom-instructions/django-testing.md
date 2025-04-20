# Django: Testing Strategies

Writing unit and integration tests for Django applications using the built-in framework.

## Core Concept: Automated Verification

Django provides a built-in testing framework based on Python's standard `unittest` module, but with added features specifically for testing Django applications. Writing automated tests helps ensure your code works correctly, prevents regressions when making changes, and facilitates refactoring.

**Key Components:**

*   **Test Runner:** Django's `manage.py test` command discovers and runs tests within your project's apps.
*   **`TestCase`:** A subclass of `unittest.TestCase` provided by Django (`django.test.TestCase`). Each test method runs within a database transaction, which is rolled back at the end of the test, ensuring test isolation without needing to manually clean up created data. It also includes a built-in test `Client`.
*   **Test Client (`django.test.Client`):** A utility class that acts like a dummy web browser, allowing you to simulate `GET`, `POST`, and other HTTP requests against your Django views without needing to run a live development server. Available as `self.client` within `TestCase`.
*   **Assertions:** Use standard `unittest` assertion methods (`assertEqual`, `assertTrue`, `assertRaises`, etc.) or methods provided by `TestCase` (`assertContains`, `assertRedirects`, `assertFormError`, etc.).
*   **Fixtures:** Pre-defined data loaded into the test database before tests run. Can be defined in JSON or YAML files within a `fixtures` directory in your app. Loaded using the `fixtures` attribute on `TestCase` or `manage.py loaddata`. Useful for setting up common initial states.
*   **Factories:** Libraries like `factory-boy` provide a more flexible way to generate test data programmatically compared to static fixtures.

## Writing Tests (`tests.py`)

Tests are typically placed in an app's `tests.py` file (or organized into a `tests/` package with multiple files like `test_models.py`, `test_views.py`).

```python
# myapp/tests.py
from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Article, Author, Category # Import models to test
from .forms import ArticleForm # Import forms to test

class ArticleModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods in this class
        # Runs once per class
        cls.user = User.objects.create_user(username='testuser', password='password')
        cls.author = Author.objects.create(user=cls.user)
        cls.category = Category.objects.create(name='Testing', slug='testing')

    def setUp(self):
        # Runs before each test method
        # Create objects needed specifically for this test method if setUpTestData isn't sufficient
        pass

    def test_was_published_recently_with_future_article(self):
        """
        was_published_recently() returns False for articles whose publish_date
        is in the future.
        """
        future_date = timezone.now() + timezone.timedelta(days=30)
        future_article = Article(publish_date=future_date, author=self.author, title="Future")
        self.assertIs(future_article.was_published_recently(), False)

    def test_was_published_recently_with_old_article(self):
        """
        was_published_recently() returns False for articles whose publish_date
        is older than 1 day.
        """
        old_date = timezone.now() - timezone.timedelta(days=1, seconds=1)
        old_article = Article(publish_date=old_date, author=self.author, title="Old")
        self.assertIs(old_article.was_published_recently(), False)

    def test_was_published_recently_with_recent_article(self):
        """
        was_published_recently() returns True for articles whose publish_date
        is within the last day.
        """
        recent_date = timezone.now() - timezone.timedelta(hours=23, minutes=59)
        recent_article = Article(publish_date=recent_date, author=self.author, title="Recent")
        self.assertIs(recent_article.was_published_recently(), True)

    def test_string_representation(self):
        article = Article(title="Test Title", author=self.author)
        self.assertEqual(str(article), "Test Title")


class ArticleViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='password')
        cls.author = Author.objects.create(user=cls.user)
        cls.published_article = Article.objects.create(
            title="Published", slug="published", author=cls.author, status='published'
        )
        cls.draft_article = Article.objects.create(
            title="Draft", slug="draft", author=cls.author, status='draft'
        )

    def setUp(self):
        # self.client is automatically available instance of django.test.Client
        pass

    def test_article_list_view_status_code(self):
        response = self.client.get(reverse('myapp:article_list'))
        self.assertEqual(response.status_code, 200)

    def test_article_list_view_template(self):
        response = self.client.get(reverse('myapp:article_list'))
        self.assertTemplateUsed(response, 'myapp/article_list.html')

    def test_article_list_shows_published_article(self):
        response = self.client.get(reverse('myapp:article_list'))
        self.assertContains(response, self.published_article.title)
        # By default, draft articles might not be shown depending on view logic
        self.assertNotContains(response, self.draft_article.title)

    def test_article_detail_view_published(self):
        url = reverse('myapp:article_detail', kwargs={'pk': self.published_article.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.published_article.title)

    def test_article_detail_view_draft(self):
        # Assuming detail view only shows published articles (based on view logic)
        url = reverse('myapp:article_detail', kwargs={'pk': self.draft_article.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404) # Expect Http404

    def test_article_create_view_get(self):
        # Test requires login
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('myapp:article_create'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], ArticleForm)

    def test_article_create_view_post_valid(self):
        self.client.login(username='testuser', password='password')
        category = Category.objects.create(name='New Cat', slug='new-cat')
        data = {
            'title': 'Test Create Article',
            'slug': 'test-create-article',
            'author': self.author.pk, # Use PK for ForeignKey in POST data
            'categories': [category.pk], # Use list of PKs for ManyToMany
            'content': 'Test content.',
            'status': 'draft',
            'publish_date': timezone.now().strftime('%Y-%m-%dT%H:%M'), # Format for DateTimeField
        }
        response = self.client.post(reverse('myapp:article_create'), data)
        # Should redirect on success
        self.assertEqual(response.status_code, 302)
        # Check if article was created
        self.assertTrue(Article.objects.filter(title='Test Create Article').exists())
        new_article = Article.objects.get(title='Test Create Article')
        self.assertEqual(new_article.author, self.author)
        self.assertIn(category, new_article.categories.all())

    def test_article_create_view_post_invalid(self):
        self.client.login(username='testuser', password='password')
        data = {'title': 'Bad'} # Missing required fields
        response = self.client.post(reverse('myapp:article_create'), data)
        self.assertEqual(response.status_code, 200) # Re-renders form on failure
        self.assertFormError(response, 'form', 'content', 'This field is required.')
        self.assertFormError(response, 'form', 'author', 'This field is required.')
        self.assertFalse(Article.objects.filter(title='Bad').exists())

```

## Running Tests

```bash
# Run all tests in the project
python manage.py test

# Run tests for a specific app
python manage.py test myapp

# Run tests for a specific test class
python manage.py test myapp.tests.ArticleViewTests

# Run a specific test method
python manage.py test myapp.tests.ArticleViewTests.test_article_detail_view_published

# Show more verbose output
python manage.py test -v 2
```

Write tests for your models (custom methods, properties) and views (status codes, templates used, context data, form handling, redirects, permissions). Use the test client to simulate user interactions. Aim for good test coverage to catch regressions and ensure reliability.