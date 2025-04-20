# Directus: Configuration via Environment Variables (`.env`)

Configuring a Directus instance using environment variables, typically stored in a `.env` file.

## Core Concept

Directus relies heavily on environment variables for its core configuration, including database connections, security settings, caching, file storage, authentication providers, and more. This makes it easy to manage different configurations for development, staging, and production without modifying code.

## `.env` File

*   **Location:** Place a `.env` file in the root directory of your Directus project.
*   **Format:** Standard `KEY=VALUE` pairs, one per line. Lines starting with `#` are comments.
*   **Loading:** Directus automatically loads variables from the `.env` file on startup using `dotenv`.
*   **Security:** **Never commit your `.env` file containing sensitive production secrets (database passwords, API keys, `SECRET`) to version control (Git).** Add `.env` to your `.gitignore` file. Use environment variable management provided by your hosting platform for production secrets.

## Key Configuration Variables

**(Note: This is not exhaustive. Refer to official Directus docs for the full list.)**

*   **`SECRET` (Required):** A long, random, unique string used for signing security tokens (JWTs, session cookies). **CRITICAL for security.** Generate a strong random string.
*   **`PUBLIC_URL` (Required):** The public-facing base URL of your Directus instance (e.g., `https://directus.example.com`). Used for redirects, links in emails, etc.
*   **Database:**
    *   `DB_CLIENT`: Database type (e.g., `pg` for PostgreSQL, `mysql`, `sqlite3`, `mssql`, `oracledb`).
    *   `DB_HOST`: Database server hostname.
    *   `DB_PORT`: Database server port.
    *   `DB_DATABASE`: Database name.
    *   `DB_USER`: Database username.
    *   `DB_PASSWORD`: Database password.
    *   `DB_CONNECTION_STRING`: Alternatively, provide a full connection string.
*   **Admin User (Initial Setup):**
    *   `ADMIN_EMAIL`: Email for the initial administrator user.
    *   `ADMIN_PASSWORD`: Password for the initial administrator user. (Use a strong password, consider removing after first login).
*   **Email:**
    *   `EMAIL_FROM`: Default "From" address for emails.
    *   `EMAIL_TRANSPORT`: Transport method (`smtp`, `sendmail`, `ses`).
    *   `EMAIL_SMTP_...`: SMTP specific settings (host, port, user, pass, secure).
*   **CORS:**
    *   `CORS_ENABLED`: `true` or `false`.
    *   `CORS_ORIGIN`: Comma-separated list of allowed origins, or `*` (use with caution).
    *   `CORS_METHODS`, `CORS_ALLOWED_HEADERS`, etc.
*   **Rate Limiting:**
    *   `RATE_LIMITER_ENABLED`: `true` or `false`.
    *   `RATE_LIMITER_POINTS`, `RATE_LIMITER_DURATION`.
*   **Caching:**
    *   `CACHE_ENABLED`: `true` or `false`.
    *   `CACHE_STORE`: `memory` (default), `redis`.
    *   `CACHE_REDIS`: Redis connection string if `CACHE_STORE=redis`.
*   **File Storage:**
    *   `STORAGE_LOCATIONS`: Comma-separated list of storage adapter names (e.g., `local`, `s3`).
    *   `STORAGE_LOCAL_ROOT`: Root path for the `local` adapter.
    *   `STORAGE_S3_...`: Configuration for the S3 adapter (key, secret, region, bucket, etc.).
*   **Authentication:**
    *   `ACCESS_TOKEN_TTL`, `REFRESH_TOKEN_TTL`.
    *   `AUTH_PROVIDERS`: Comma-separated list of enabled SSO providers (e.g., `google`, `github`, `openid`).
    *   `AUTH_{PROVIDER_NAME}_...`: Specific settings for each enabled SSO provider (client ID, secret, redirect URL).
    *   `AUTH_PROVIDER_DEFAULT_ROLE_ID`: UUID of the role assigned to new SSO users.
*   **WebSockets:**
    *   `WEBSOCKETS_ENABLED`: `true` or `false`.
    *   `WEBSOCKETS_BROKER_URL`: URL for message broker (e.g., Redis) for multi-instance scaling.
*   **Extensions:**
    *   `EXTENSIONS_PATH`: Path to the extensions directory (default: `./extensions`).
*   **Logging:**
    *   `LOG_LEVEL`: `info`, `warn`, `error`, `debug`, `trace`.
    *   `LOG_TYPE`: `stdout` (default), `file`.
    *   `LOG_FILE`: Path if `LOG_TYPE=file`.

## Applying Configuration

*   Changes to the `.env` file require a **restart** of the Directus instance to take effect.
*   In containerized environments (Docker), environment variables are typically passed directly to the container rather than using a `.env` file inside the container.

Properly configuring Directus via environment variables is essential for security, scalability, and managing different deployment environments.

*(Refer to the official Directus Environment Variables documentation: https://docs.directus.io/self-hosted/config-options.html)*