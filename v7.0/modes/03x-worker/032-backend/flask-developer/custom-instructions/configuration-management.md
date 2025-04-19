# Flask: Configuration Management

Handling application configuration in Flask projects.

## Core Concept

Flask applications need configuration for various settings, such as secret keys, database URIs, debugging flags, and extension-specific options. Flask provides a flexible system for loading configuration from different sources.

## `app.config` Object

*   The central place where Flask stores configuration values is the `app.config` object, which behaves like a dictionary.
*   Keys are typically uppercase (e.g., `SECRET_KEY`, `SQLALCHEMY_DATABASE_URI`).
*   Flask itself, as well as extensions, use values from `app.config`.

## Loading Configuration

There are several ways to load configuration, often used in combination, especially with the Application Factory pattern. Later sources override earlier ones.

1.  **Default Values (Directly on `app.config`):**
    *   Set default values directly before loading from other sources.
    ```python
    app = Flask(__name__)
    app.config['DEBUG'] = False # Set a default
    ```
2.  **From a Python File (`app.config.from_pyfile()`):**
    *   Load configuration from a `.py` file (e.g., `config.py`). Variables must be uppercase.
    ```python
    # config.py
    DEBUG = True
    SECRET_KEY = 'my-dev-secret'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'
    ```
    ```python
    # In your app setup
    app.config.from_pyfile('config.py', silent=False) # silent=True ignores file-not-found errors
    ```
3.  **From an Object (`app.config.from_object()`):**
    *   Load configuration from attributes of a Python object (often a class). Attributes must be uppercase. This is common for organizing different environments (Development, Testing, Production).
    ```python
    # config.py
    import os
    basedir = os.path.abspath(os.path.dirname(__file__))

    class Config:
        SECRET_KEY = os.environ.get('SECRET_KEY') or 'default-fallback-key'
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        DEBUG = False
        TESTING = False
        # Default database
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
            'sqlite:///' + os.path.join(basedir, 'app.db')

    class DevelopmentConfig(Config):
        DEBUG = True
        SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
            'sqlite:///' + os.path.join(basedir, 'dev.db')

    class TestingConfig(Config):
        TESTING = True
        SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
            'sqlite:///:memory:' # Use in-memory DB for tests
        WTF_CSRF_ENABLED = False # Often disable CSRF in tests

    class ProductionConfig(Config):
        # Production settings loaded primarily from environment variables
        # SECRET_KEY MUST be set via environment variable
        # SQLALCHEMY_DATABASE_URI MUST be set via environment variable
        pass

    config = {
        'development': DevelopmentConfig,
        'testing': TestingConfig,
        'production': ProductionConfig,
        'default': DevelopmentConfig
    }
    ```
    ```python
    # In create_app() factory
    from config import config

    def create_app(config_name='default'):
        app = Flask(__name__)
        app.config.from_object(config[config_name])
        # ... initialize extensions ...
        return app
    ```
4.  **From Environment Variables (`app.config.from_envvar()`):**
    *   Load configuration from a file specified by an environment variable. Less common than loading directly from environment variables.
    ```bash
    export YOURAPP_SETTINGS='/path/to/settings.cfg'
    ```
    ```python
    app.config.from_envvar('YOURAPP_SETTINGS')
    ```
5.  **From JSON (`app.config.from_json()`):**
    *   Load configuration from a JSON file.
    ```python
    app.config.from_json('config.json')
    ```
6.  **From Mapping (`app.config.from_mapping()` or `update()`):**
    *   Load configuration directly from a dictionary. Useful for defaults or test overrides.
    ```python
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    # Or using update
    app.config.update(
        TESTING=True,
        SECRET_KEY='test'
    )
    ```

## Important Configuration Values

*   **`SECRET_KEY` (Critical):** A long, random, secret string used for signing sessions, CSRF tokens, etc. **Must be kept secret and should be loaded from an environment variable in production.**
*   **`DEBUG` (Boolean):** Enables debug mode (detailed error pages, automatic reloading). **Never `True` in production.**
*   **`TESTING` (Boolean):** Enables testing mode (affects error handling, extension behavior).
*   **`SQLALCHEMY_DATABASE_URI` (Flask-SQLAlchemy):** Connection string for the database.
*   **`SQLALCHEMY_TRACK_MODIFICATIONS` (Flask-SQLAlchemy):** Set to `False` to disable modification tracking and save resources unless needed.
*   **Extension-Specific Keys:** Many extensions (Flask-Login, Flask-Mail, etc.) use `app.config` for their settings. Refer to the specific extension's documentation.

## Best Practices

*   **Use Environment Variables for Secrets:** Load sensitive values like `SECRET_KEY`, database passwords, and API keys from environment variables, especially in production. Do not commit secrets to version control. Use `.env` files (with `python-dotenv`) for local development, ensuring `.env` is in `.gitignore`.
*   **Use Configuration Objects/Files:** Organize configuration for different environments (development, testing, production) using classes or separate files.
*   **Application Factory:** Load configuration within your `create_app` factory function.
*   **Default Values:** Provide sensible default values within your `Config` base class.

Proper configuration management is essential for security and managing different deployment environments.

*(Refer to the official Flask Configuration Handling documentation.)*