# Directus: Authentication

Configuring and managing user authentication methods in Directus.

## Core Concept: Verifying User Identity

Authentication is the process of verifying that a user is who they claim to be. Directus provides several methods for authenticating users accessing the Data Studio UI and the API. Authenticated users are associated with a Role, which determines their permissions.

**Authentication Methods:**

1.  **Local Authentication:** The default method. Users register and log in with an email and password stored securely (hashed) in the `directus_users` collection.
2.  **Single Sign-On (SSO):** Allows users to authenticate using external identity providers. Directus supports various protocols:
    *   **OAuth 2.0:** Standard protocol used by Google, Facebook, GitHub, etc.
    *   **OpenID Connect (OIDC):** Built on top of OAuth 2.0, providing more identity information (e.g., Auth0, Okta, Keycloak).
    *   **LDAP:** Connect to existing LDAP directories (e.g., Active Directory).
    *   **SAML:** Another enterprise standard for SSO.
3.  **Static Tokens:** Fixed access tokens associated with a specific user. Useful for server-to-server communication or simple API integrations where a full login flow isn't practical. Should be treated as secrets.

## Configuration (Primarily via Environment Variables)

Authentication methods and their settings are primarily configured using environment variables in your Directus `.env` file.

**1. Local Authentication:**

*   Enabled by default.
*   Password policy (minimum length, complexity) can be configured.
*   Two-Factor Authentication (2FA) can be enabled (`AUTH_MFA_REQUIRED=true`).

**2. SSO Providers (OAuth 2.0 / OpenID Connect Example - Google):**

*   Requires registering your Directus instance as an application with the provider (e.g., Google Cloud Console) to get a Client ID and Client Secret.
*   Set environment variables:
    ```dotenv
    # .env
    AUTH_PROVIDERS="google" # Comma-separated list of enabled providers

    AUTH_GOOGLE_DRIVER="openid" # or "oauth2"
    AUTH_GOOGLE_CLIENT_ID="YOUR_GOOGLE_CLIENT_ID"
    AUTH_GOOGLE_CLIENT_SECRET="YOUR_GOOGLE_CLIENT_SECRET"
    AUTH_GOOGLE_SCOPE="openid email profile" # Requested permissions
    # For OpenID, issuer URL is often needed:
    AUTH_GOOGLE_ISSUER_URL="https://accounts.google.com"
    # Optional: Restrict login to specific domains
    # AUTH_GOOGLE_ALLOWED_DOMAINS="yourcompany.com"
    # Optional: Map provider roles to Directus roles
    # AUTH_GOOGLE_ROLES_MAP='{"google_group_id": "directus_role_uuid"}'

    PUBLIC_URL="https://your-directus-instance.com" # Important: Must match redirect URI in provider config
    ```
*   Similar variables exist for other providers (`AUTH_GITHUB_*`, `AUTH_AZURE_*`, `AUTH_OKTA_*`, etc.). Consult Directus documentation for specific provider keys.

**3. Static Tokens:**

*   Can be generated for specific users via the Directus UI (User settings) or API.
*   Set `ACCESS_TOKEN_TTL` environment variable to control default expiry (e.g., `ACCESS_TOKEN_TTL="15m"` for 15 minutes, `-1` for no expiry).

## API Authentication

Clients consuming the REST or GraphQL APIs need to authenticate their requests:

*   **Session Cookies:** If logging in via the `/auth/login` endpoint, Directus sets an HTTP-only cookie (`directus_session_token`) which the browser automatically sends with subsequent requests. Suitable for traditional web apps or frontends served from the same domain. Requires CSRF protection configuration in Directus if used cross-origin.
*   **Bearer Tokens (JWT/Static):**
    *   After login (`POST /auth/login`), the response includes an `access_token` (JWT, short-lived) and optionally a `refresh_token`.
    *   Static tokens can be used directly.
    *   Send the token in the `Authorization` header: `Authorization: Bearer <your_access_token_or_static_token>`
    *   Use the `refresh_token` with the `/auth/refresh` endpoint to get a new `access_token` when the old one expires.
    *   This is the standard method for SPAs, mobile apps, and server-to-server communication.

## Key Considerations

*   **Security:** Store client secrets and static tokens securely. Use HTTPS for all communication. Configure `PUBLIC_URL` correctly.
*   **Role Mapping:** When using SSO, carefully map external groups or attributes to Directus roles to ensure correct permissions.
*   **User Provisioning:** Decide how users are created when logging in via SSO for the first time (automatic creation based on provider info, or require manual invitation). Configure the default role for new SSO users (`AUTH_DEFAULT_ROLE_ID`).
*   **Token Expiry:** Configure appropriate TTLs for access tokens (`ACCESS_TOKEN_TTL`) and refresh tokens (`REFRESH_TOKEN_TTL`).
*   **CSRF Protection:** Ensure CSRF protection is enabled and configured correctly if using cookie-based authentication, especially across different origins.

Directus offers flexible authentication options. Choose the methods appropriate for your users and client applications. Configure providers securely using environment variables and manage API access using tokens or cookies.

*(Refer to the official Directus documentation on Authentication and SSO.)*