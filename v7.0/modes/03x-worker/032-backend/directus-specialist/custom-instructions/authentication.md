# Directus: Authentication

Configuring how users authenticate with the Directus API and Admin App.

## Core Concept

Directus provides flexible authentication mechanisms to verify user identity before granting access to data or features based on their assigned role and permissions.

## Authentication Methods

Directus supports several methods out-of-the-box:

1.  **Local Authentication:**
    *   **Mechanism:** Users authenticate with an email and password stored securely (hashed) in the `directus_users` collection.
    *   **Setup:** Enabled by default. Manage users via the Admin App (Settings -> Users).
    *   **API Login:** `POST /auth/login` with `{"email": "...", "password": "..."}`. Returns access and refresh tokens (JWT by default).
    *   **API Usage:** Include the access token in the `Authorization: Bearer <token>` header for subsequent requests.
    *   **Password Resets:** Built-in flow via `/auth/password/request` and `/auth/password/reset`. Requires email setup.
    *   **Two-Factor Authentication (2FA):** Can be enabled per user (TOTP via authenticator app).

2.  **Single Sign-On (SSO) / OAuth 2.0 / OpenID Connect:**
    *   **Mechanism:** Delegate authentication to external providers (Google, GitHub, Facebook, Okta, Auth0, custom OpenID Connect, etc.). Users log in via the provider, which then redirects back to Directus with an authorization code or token. Directus verifies the token and maps the external user to a local Directus user (creating one if needed based on configuration).
    *   **Setup:** Configure providers via environment variables (e.g., `AUTH_GOOGLE_CLIENT_ID`, `AUTH_GOOGLE_CLIENT_SECRET`, `AUTH_GOOGLE_REDIRECT`, `AUTH_PROVIDERS`). See Directus docs for specific provider variables.
    *   **Login Flow:** Typically initiated by navigating to `/auth/login/{provider_name}` (e.g., `/auth/login/google`).
    *   **Role Mapping:** Configure the default role assigned to users created via SSO (`AUTH_PROVIDER_DEFAULT_ROLE_ID`).

3.  **LDAP:**
    *   **Mechanism:** Authenticate against an existing LDAP directory.
    *   **Setup:** Configure via environment variables (`AUTH_LDAP_...`).

4.  **Static Tokens:**
    *   **Mechanism:** Fixed, long-lived tokens assigned to specific users. Useful for server-to-server communication or simple scripts.
    *   **Setup:** Generate tokens for users via the Admin App (User Directory -> User -> Static Access Tokens).
    *   **API Usage:** Pass the token in the `Authorization: Bearer <static_token>` header.
    *   **Security:** Use with caution, as these tokens don't expire automatically. Limit the permissions of the associated user role.

## Key Configuration (Environment Variables - `.env`)

Authentication methods and behavior are primarily configured via environment variables.

*   **Secrets:** `SECRET` (a long random string used for signing tokens - **CRITICAL**).
*   **Public URL:** `PUBLIC_URL` (The public-facing URL of your Directus instance, needed for redirects).
*   **Access Token TTL:** `ACCESS_TOKEN_TTL` (Default: `15m`).
*   **Refresh Token TTL:** `REFRESH_TOKEN_TTL` (Default: `7d`). Use `/auth/refresh` endpoint to get new access tokens.
*   **SSO Providers:** Specific variables for each provider (e.g., `AUTH_GOOGLE_CLIENT_ID`, `AUTH_GITHUB_CLIENT_SECRET`). Consult Directus documentation.
*   **Default Role for SSO:** `AUTH_PROVIDER_DEFAULT_ROLE_ID` (UUID of the role).

## Tokens (JWT Default)

*   **Access Token:** Short-lived token (default 15 mins) used to authenticate API requests. Contains user ID, role, and expiration. Passed via `Authorization: Bearer <token>`.
*   **Refresh Token:** Longer-lived token (default 7 days) used to obtain new access tokens via the `/auth/refresh` endpoint without requiring the user to log in again. Can be stored securely (e.g., HttpOnly cookie).

## Security Considerations

*   **Strong `SECRET`:** Use a long, unpredictable random string for the `SECRET` environment variable.
*   **HTTPS:** Always run Directus over HTTPS.
*   **Token Storage:** Securely store refresh tokens on the client (e.g., HttpOnly cookies are generally preferred over localStorage for web clients to mitigate XSS). Access tokens can be stored in memory.
*   **Permissions:** Authentication only verifies *who* the user is. Authorization (Permissions) determines *what* they can do. Configure roles and permissions carefully (see `permissions-rbac.md`).
*   **SSO Configuration:** Ensure redirect URIs are configured correctly and securely in both Directus and the external provider.
*   **Static Tokens:** Use sparingly and assign them to roles with minimal necessary permissions.

Coordinate with `security-specialist` or `security-lead` for complex authentication setups or security reviews.

*(Refer to the official Directus Authentication documentation: https://docs.directus.io/self-hosted/config-options.html#authentication and https://docs.directus.io/guides/auth.html)*