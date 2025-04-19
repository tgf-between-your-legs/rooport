# Directus: Configuration (Environment Variables)

Understanding and managing Directus instance settings using environment variables.

## Core Concept: Environment-Based Configuration

Directus is configured primarily through **environment variables**, typically loaded from a `.env` file in the project root or set directly in the deployment environment (e.g., Docker environment variables, PaaS configuration). This approach follows the Twelve-Factor App methodology, keeping configuration separate from code.

Using environment variables allows you to have different settings for development, staging, and production environments without modifying the Directus core code or committed configuration files.

## Key Configuration Areas & Variables

**(Note: This is not exhaustive. Refer to official Directus docs for a complete list.)**

**1. Database Connection:** (REQUIRED)

*   `DB_CLIENT`: The SQL database type (e.g., `pg` for PostgreSQL, `mysql`, `sqlite3`, `mssql`, `oracledb`).
*   `DB_HOST`: Database server hostname or IP address.
*   `DB_PORT`: Database server port.
*   `DB_DATABASE`: Database name.
*   `DB_USER`: Database username.
*   `DB_PASSWORD`: Database password.
*   `DB_CONNECTION_STRING`: Alternatively, provide a full connection string.
*   (SQLite specific) `DB_FILENAME`: Path to the SQLite file (e.g., `./data.db`).

**2. Security & Keys:** (REQUIRED)

*   `KEY`: A unique, randomly generated string for general cryptographic purposes (e.g., hashing non-password secrets). **Must be set.**
*   `SECRET`: A unique, highly random string used for signing authentication tokens (JWTs, session tokens). **Must be set and kept secret.** Generate strong random strings for these.
*   `PUBLIC_URL`: The primary, user-facing URL of your Directus instance (e.g., `https://directus.example.com`). Crucial for redirects, asset URLs, OAuth callbacks, etc.

**3. Admin Account:**

*   `ADMIN_EMAIL`: Email for the initial administrator user.
*   `ADMIN_PASSWORD`: Password for the initial administrator user. (Directus will hash this on first startup).

**4. Authentication:** (See `directus-authentication.md`)

*   `AUTH_PROVIDERS`: Comma-separated list of enabled SSO providers (e.g., `google,github`).
*   `AUTH_<PROVIDER>_DRIVER`, `AUTH_<PROVIDER>_CLIENT_ID`, `AUTH_<PROVIDER>_CLIENT_SECRET`, etc.
*   `ACCESS_TOKEN_TTL`, `REFRESH_TOKEN_TTL`: Lifetimes for JWTs.
*   `AUTH_PASSWORD_RESET_URL`: URL for password reset emails.
*   `AUTH_MFA_REQUIRED`: Enforce 2FA (`true`/`false`).

**5. Email:**

*   `EMAIL_FROM`: Default "From" address for emails sent by Directus.
*   `EMAIL_TRANSPORT`: Method for sending emails (`smtp`, `sendmail`, `ses`, `mailgun`).
*   `EMAIL_SMTP_HOST`, `EMAIL_SMTP_PORT`, `EMAIL_SMTP_USER`, `EMAIL_SMTP_PASSWORD`, `EMAIL_SMTP_SECURE`, etc. (Variables depend on the chosen transport).

**6. Caching:**

*   `CACHE_ENABLED`: Enable/disable internal caching (`true`/`false`).
*   `CACHE_STORE`: Cache storage (`memory` or `redis`).
*   `CACHE_REDIS`: Redis connection string if `CACHE_STORE=redis`.
*   `CACHE_TTL`: Default cache time-to-live (e.g., `5m`).
*   `CACHE_QUERY_TTL`: Specific TTL for query/response caching.

**7. File Storage:** (See `directus-file-storage.md`)

*   `STORAGE_LOCATIONS`: Comma-separated list of enabled storage adapters (e.g., `local,s3`).
*   `STORAGE_<LOCATION>_DRIVER`, `STORAGE_<LOCATION>_KEY`, `STORAGE_<LOCATION>_SECRET`, `STORAGE_<LOCATION>_BUCKET`, etc.

**8. CORS (Cross-Origin Resource Sharing):**

*   `CORS_ENABLED`: Enable/disable CORS headers (`true`/`false`).
*   `CORS_ORIGIN`: Allowed origins (comma-separated list or `*` for all - use with caution).
*   `CORS_METHODS`, `CORS_ALLOWED_HEADERS`, `CORS_EXPOSED_HEADERS`, `CORS_CREDENTIALS`, `CORS_MAX_AGE`.

**9. Rate Limiting:**

*   `RATE_LIMITER_ENABLED`: Enable/disable global rate limiting (`true`/`false`).
*   `RATE_LIMITER_STORE`: Storage for rate limit tracking (`memory` or `redis`).
*   `RATE_LIMITER_POINTS`: Max requests per duration.
*   `RATE_LIMITER_DURATION`: Duration in seconds.

**10. Logging:**

*   `LOG_LEVEL`: Logging verbosity (`trace`, `debug`, `info`, `warn`, `error`, `fatal`).
*   `LOG_TYPE`: Output format (`pretty`, `json`).
*   `LOG_DESTINATION`: Where to log (`console` or file path).

**11. Extensions:**

*   `EXTENSIONS_PATH`: Path to the extensions directory (default: `./extensions`).
*   `EXTENSIONS_AUTO_RELOAD`: Automatically reload extensions on change (dev only) (`true`/`false`).

## Managing `.env` Files

*   **Location:** Place the `.env` file in the root directory of your Directus project.
*   **`.gitignore`:** **Crucially, add `.env` to your `.gitignore` file.** Never commit sensitive credentials (database passwords, API keys, secrets) to version control.
*   **Environment Specificity:** Use different `.env` files or environment variable settings for different environments (development, staging, production). Deployment platforms often provide secure ways to manage production environment variables.
*   **Loading:** Directus automatically loads variables from `.env` using `dotenv`.

Configuration via environment variables is central to deploying and managing Directus instances. Ensure required variables like database connection details and security keys (`KEY`, `SECRET`) are set correctly and kept secure. Refer to the official documentation for the full list of available variables and their specific usage.

*(Refer to the official Directus documentation on Environment Variables.)*