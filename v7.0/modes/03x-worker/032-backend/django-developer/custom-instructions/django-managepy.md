# Django: `manage.py` Utility

Using Django's command-line utility for common administrative and development tasks.

## Core Concept: Command-Line Interface

`manage.py` is a command-line utility automatically created in each Django project. It serves as a thin wrapper around `django-admin` and provides essential commands for interacting with your project during development and deployment.

You run it from your project's root directory (the one containing `manage.py`).

**Basic Usage:**

```bash
python manage.py <command> [options] [args...]
```

## Common Commands

1.  **`runserver`:** Starts the lightweight development web server.
    *   `python manage.py runserver` (Runs on default port 8000)
    *   `python manage.py runserver 8080` (Runs on port 8080)
    *   `python manage.py runserver 0.0.0.0:8000` (Makes server accessible on your network)
    *   **Note:** This server is for development *only*, not suitable for production.

2.  **`startapp <app_name>`:** Creates a new Django app directory structure within your project.
    *   `python manage.py startapp myapp`

3.  **`makemigrations [app_name]`:** Detects changes in your models (`models.py`) and creates new migration files in the app's `migrations/` directory.
    *   `python manage.py makemigrations` (Detects changes in all apps)
    *   `python manage.py makemigrations myapp` (Detects changes only in `myapp`)

4.  **`migrate [app_name] [migration_name]`:** Applies pending migrations to the database, updating the schema.
    *   `python manage.py migrate` (Applies all pending migrations for all apps)
    *   `python manage.py migrate myapp` (Applies pending migrations for `myapp`)
    *   `python manage.py migrate myapp zero` (Unapplies all migrations for `myapp`)
    *   `python manage.py migrate myapp 0001_initial` (Applies migrations up to `0001_initial`)

5.  **`showmigrations`:** Lists all migrations in the project and indicates whether they have been applied.

6.  **`sqlmigrate <app_name> <migration_name>`:** Displays the SQL statements that a specific migration will execute. Useful for debugging or understanding schema changes.
    *   `python manage.py sqlmigrate myapp 0002_add_field`

7.  **`test [app_name] [TestCase] [TestMethod]`:** Discovers and runs automated tests (usually in `tests.py` or `tests/` package).
    *   `python manage.py test` (Runs all tests)
    *   `python manage.py test myapp` (Runs tests for `myapp`)
    *   `python manage.py test myapp.tests.ArticleViewTests` (Runs specific test class)
    *   `python manage.py test myapp.tests.ArticleViewTests.test_article_list_view_status_code` (Runs specific test method)

8.  **`shell`:** Opens an interactive Python shell with your Django project environment loaded (settings, models available). Useful for experimenting with the ORM or running ad-hoc queries.
    *   `python manage.py shell`

9.  **`createsuperuser`:** Creates an administrative user with full permissions (`is_staff=True`, `is_superuser=True`).
    *   `python manage.py createsuperuser`

10. **`changepassword [username]`:** Allows changing a user's password.

11. **`collectstatic`:** Gathers all static files (CSS, JS, images) from `INSTALLED_APPS` and copies them into the directory specified by `STATIC_ROOT` in `settings.py`. Essential for production deployment.
    *   `python manage.py collectstatic --noinput` (Runs non-interactively)

12. **`check`:** Runs system checks to identify common problems in the project configuration or code. Run this before deployment.
    *   `python manage.py check`
    *   `python manage.py check --deploy` (Runs additional checks specific to deployment settings)

13. **`dbshell`:** Opens the command-line client for the database specified in your `settings.py`. Requires the client program to be installed.

14. **`flush`:** Removes *all* data from the database and re-runs any post-synchronization handlers. **Use with extreme caution, especially in production!**

15. **`loaddata <fixture_file>`:** Loads data from fixture files (JSON, YAML, XML) into the database.
    *   `python manage.py loaddata myapp/fixtures/initial_data.json`

16. **`dumpdata [app_name[.ModelName]]`:** Outputs data from the database (for specified apps/models or all data) to standard output, typically in JSON format. Useful for creating fixtures or backups.
    *   `python manage.py dumpdata myapp.Article --indent 2 > myapp/fixtures/articles.json`

**Getting Help:**

*   `python manage.py help`: Lists all available commands.
*   `python manage.py help <command>`: Shows detailed help and options for a specific command.

`manage.py` is the primary tool for interacting with your Django project from the command line. Familiarity with commands like `runserver`, `makemigrations`, `migrate`, `test`, `collectstatic`, and `shell` is essential for development and deployment.