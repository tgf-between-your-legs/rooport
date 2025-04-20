# API Security Fundamentals

Essential security considerations when designing and implementing APIs.

## Core Concept: Protecting API Endpoints and Data

APIs are common targets for attacks because they expose application logic and data. Implementing robust security measures is crucial to prevent unauthorized access, data breaches, and denial of service. Security is a layered approach, involving authentication, authorization, input validation, transport security, and rate limiting.

**Key Areas:**

1.  **Authentication (AuthN):** Verifying the identity of the client (user or system) making the request. Who are you?
2.  **Authorization (AuthZ):** Determining if the authenticated client has permission to perform the requested action or access the requested resource. What are you allowed to do?
3.  **Input Validation:** Ensuring data received from the client (parameters, body) is valid, well-formed, and within expected constraints to prevent injection attacks (SQLi, XSS), overflows, etc.
4.  **Transport Security:** Encrypting data in transit between the client and server using HTTPS (TLS/SSL).
5.  **Rate Limiting:** Preventing abuse and denial-of-service (DoS) attacks by limiting the number of requests a client can make within a certain time window.
6.  **Output Encoding/Escaping:** Ensuring data returned by the API is properly encoded or escaped, especially if it might be rendered directly in an HTML context by the client, to prevent Cross-Site Scripting (XSS).
7.  **Information Disclosure:** Avoiding leaking sensitive information (stack traces, internal configurations, excessive user data) in error messages or responses.

## Common Security Mechanisms & Best Practices

1.  **Authentication:**
    *   **Token-Based (JWT, OAuth 2.0 Bearer Tokens):** Most common for SPAs and mobile apps. The client obtains a token (often after login) and sends it in the `Authorization: Bearer <token>` header with each request. The server validates the token signature and expiry.
    *   **API Keys:** Simpler tokens often used for server-to-server or third-party integrations. Should be treated as secrets and sent securely (e.g., custom header `X-API-Key`). Less secure for user authentication.
    *   **Session Cookies (Stateful):** Traditional web approach. Server creates a session on login and sends a session ID cookie to the client. Client sends the cookie with subsequent requests. Requires server-side session storage. Can be vulnerable to CSRF if not protected (use SameSite cookies, anti-CSRF tokens).
    *   **mTLS (Mutual TLS):** Strong authentication for server-to-server communication where both client and server present certificates.

2.  **Authorization:**
    *   **Role-Based Access Control (RBAC):** Assign roles (e.g., 'admin', 'editor', 'viewer') to users and check permissions based on the role required for the specific API endpoint or action.
    *   **Attribute-Based Access Control (ABAC):** Base decisions on attributes of the user, resource, and environment. More fine-grained.
    *   **OAuth 2.0 Scopes:** Used with OAuth tokens to grant specific, limited permissions (e.g., `read:profile`, `write:posts`).
    *   **Implement Checks Server-Side:** Authorization logic *must* reside on the server; never trust client-side checks alone. Check permissions after authenticating the user for every relevant request.

3.  **Input Validation:**
    *   **Validate Everything:** Treat all client input (URL parameters, query strings, request headers, request body) as untrusted.
    *   **Use Schemas:** Define expected data structures and types (e.g., using OpenAPI schemas, JSON Schema, GraphQL input types, framework validation libraries like Zod, Pydantic, Joi).
    *   **Check Types, Formats, Lengths, Ranges:** Ensure data conforms to expected constraints.
    *   **Sanitize vs. Validate:** Prefer validation (rejecting invalid input) over sanitization (attempting to clean up invalid input), as sanitization can be complex and error-prone.
    *   **Use Framework/Library Features:** Leverage built-in validation features of your API framework.

4.  **Transport Security:**
    *   **Use HTTPS Everywhere:** Enforce TLS/SSL for all API communication to encrypt data in transit. Configure your server appropriately (certificates).
    *   **HSTS Header:** Use the `Strict-Transport-Security` header to instruct browsers to only communicate via HTTPS.

5.  **Rate Limiting:**
    *   Implement limits based on IP address, user ID, API key, etc.
    *   Return `429 Too Many Requests` status code when limits are exceeded.
    *   Often implemented at the API gateway, load balancer, or using middleware.

6.  **Other Considerations:**
    *   **Security Headers:** Use headers like `Content-Security-Policy`, `X-Content-Type-Options`, `X-Frame-Options` to mitigate certain browser-based attacks (though some are less relevant for pure data APIs).
    *   **Logging & Monitoring:** Log relevant security events (logins, failures, access attempts) and monitor for suspicious activity.
    *   **Dependency Management:** Keep backend dependencies updated to patch known vulnerabilities.
    *   **OWASP API Security Top 10:** Be familiar with common API vulnerabilities (e.g., Broken Object Level Authorization, Broken Authentication, Excessive Data Exposure, Injection) and how to prevent them.

API security is a critical, multi-faceted concern. Collaborate closely with security specialists (`security-specialist`) and infrastructure teams (`infrastructure-specialist`, `devops-lead`) for robust implementation of authentication, authorization, rate limiting, and infrastructure security. Focus on strong input validation within the API code itself.

*(Refer to OWASP API Security Top 10 and documentation for specific authentication/authorization protocols and framework security features.)*