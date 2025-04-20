# Condensed Context Index Template: API Documentation

Use this template as a starting structure when condensing API documentation for embedding into mode instructions. Focus on density, keywords, and core concepts.

## [API Name] v[Version] - Condensed Context Index

### Overall Purpose
*   [1-2 sentence summary: What does this API do? What problem does it solve?]

### Core Concepts & Capabilities
*   **Authentication:** [Method(s) used, e.g., API Key in Header `X-API-KEY`, OAuth2 Bearer Token]
*   **Rate Limiting:** [Key limits, e.g., 100 requests/min per key, Link to details if available]
*   **Error Handling:** [Common HTTP status codes used, e.g., 400 Bad Request, 401 Unauthorized, 404 Not Found, 500 Server Error. Link to error code details if available.]
*   **Resource:** `[Resource Name 1, e.g., /users]`
    *   *Purpose:* [Brief description, e.g., Manage user accounts]
    *   *Key Endpoints:* `GET /users`, `POST /users`, `GET /users/{id}`, `PUT /users/{id}`
*   **Resource:** `[Resource Name 2, e.g., /orders]`
    *   *Purpose:* [Brief description, e.g., Create and retrieve orders]
    *   *Key Endpoints:* `POST /orders`, `GET /orders/{id}`
*   ... *(Add more core concepts like pagination, filtering, webhooks if applicable)*

### Key Endpoints / Operations
*(Focus on the ~5-10 most critical or frequently used endpoints)*

*   **`GET /resource`**
    *   *Purpose:* [e.g., List all resources]
    *   *Key Params:* `limit`, `offset`, `filter_by_field`
    *   *Response:* [e.g., Array of resource objects]
*   **`POST /resource`**
    *   *Purpose:* [e.g., Create a new resource]
    *   *Request Body:* [Key fields, e.g., `name` (string, required), `description` (string)]
    *   *Response:* [e.g., Created resource object with ID]
*   **`GET /resource/{id}`**
    *   *Purpose:* [e.g., Retrieve a specific resource by ID]
    *   *Response:* [e.g., Single resource object]
*   **`PUT /resource/{id}`**
    *   *Purpose:* [e.g., Update a specific resource]
    *   *Request Body:* [Key fields, e.g., `description` (string)]
    *   *Response:* [e.g., Updated resource object]
*   **`DELETE /resource/{id}`**
    *   *Purpose:* [e.g., Delete a specific resource]
    *   *Response:* [e.g., 204 No Content]
*   ... *(Add more key endpoints)*

### Common Patterns & Best Practices / Pitfalls
*(Optional, include 2-4 highly relevant points if prominent in docs)*
*   [e.g., Always check for rate limit headers in responses.]
*   [e.g., Use PUT for full updates, PATCH for partial updates (if supported).]
*   [e.g., Pitfall: Forgetting to handle pagination correctly can lead to incomplete data.]

---
*This index summarizes the core concepts and key endpoints for the [API Name] v[Version]. Consult the full source documentation ([path/URL to source]) for exhaustive details.*