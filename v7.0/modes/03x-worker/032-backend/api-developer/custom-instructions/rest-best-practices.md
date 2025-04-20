# REST API Best Practices

This document outlines key best practices for designing consistent, scalable, and maintainable RESTful APIs.

## 1. Resource Naming

*   **Use Nouns, Not Verbs:** API endpoints should represent resources (nouns), not actions (verbs).
    *   *Good:* `/users`, `/orders/{orderId}`
    *   *Bad:* `/getUsers`, `/createOrder`
*   **Use Plural Nouns:** Represent collections of resources using plural nouns.
    *   *Good:* `/products`, `/customers`
    *   *Bad:* `/product`, `/customer`
*   **Be Consistent:** Use a consistent naming convention (e.g., lowercase, kebab-case) throughout the API.
    *   *Example:* `/product-categories`, `/user-profiles`
*   **Avoid Deep Nesting:** Limit nesting depth to keep URIs readable. Consider using query parameters for filtering related resources.
    *   *Prefer:* `/orders?customerId=123`
    *   *Over:* `/customers/123/orders` (unless strictly hierarchical)

## 2. HTTP Methods (Verbs)

Use standard HTTP methods semantically:

*   **GET:** Retrieve a resource or collection. (Safe, Idempotent)
*   **POST:** Create a new resource within a collection. (Not Safe, Not Idempotent)
*   **PUT:** Replace an existing resource entirely. (Not Safe, Idempotent)
*   **PATCH:** Partially update an existing resource. (Not Safe, Not necessarily Idempotent)
*   **DELETE:** Remove a resource. (Not Safe, Idempotent)
*   **HEAD:** Retrieve resource metadata (like GET, but no response body). (Safe, Idempotent)
*   **OPTIONS:** Retrieve information about the communication options for the target resource. (Safe, Idempotent)

## 3. HTTP Status Codes

Use standard HTTP status codes accurately to indicate the outcome of a request:

*   **2xx (Success):**
    *   `200 OK`: General success for GET, PUT, PATCH, DELETE.
    *   `201 Created`: Resource successfully created (POST). Include `Location` header with URI of the new resource.
    *   `204 No Content`: Success, but no content to return (e.g., successful DELETE).
*   **3xx (Redirection):**
    *   `301 Moved Permanently`: Resource URI has changed permanently.
    *   `304 Not Modified`: Client's cached version is up-to-date (used with conditional GET).
*   **4xx (Client Errors):**
    *   `400 Bad Request`: Invalid request syntax or parameters.
    *   `401 Unauthorized`: Authentication required or failed.
    *   `403 Forbidden`: Authenticated user lacks permission.
    *   `404 Not Found`: Resource does not exist.
    *   `405 Method Not Allowed`: HTTP method not supported for this resource.
    *   `409 Conflict`: Request conflicts with the current state of the resource (e.g., duplicate creation).
    *   `422 Unprocessable Entity`: Semantically incorrect request (e.g., validation errors). Include error details in the body.
*   **5xx (Server Errors):**
    *   `500 Internal Server Error`: Generic server error. Avoid exposing sensitive details.
    *   `503 Service Unavailable`: Server is temporarily unavailable (e.g., maintenance, overload).

## 4. Versioning

Plan for API evolution:

*   **URI Path Versioning:** Include the version in the URI (e.g., `/v1/users`, `/v2/products`). Simple and explicit.
*   **Query Parameter Versioning:** Use a query parameter (e.g., `/users?version=1`). Less common.
*   **Custom Header Versioning:** Use a custom request header (e.g., `Accept-Version: v1`). Keeps URIs clean.
*   **Accept Header Versioning (Media Type):** Use the `Accept` header with a custom media type (e.g., `Accept: application/vnd.myapi.v1+json`). Technically pure REST, but can be complex.

*Recommendation:* URI path versioning (`/v1/`) is often the most pragmatic approach.

## 5. HATEOAS (Hypermedia as the Engine of Application State)

Include links within API responses to guide clients to related resources and actions. This promotes discoverability and reduces coupling.

*   *Example Response:*
    ```json
    {
      "orderId": 123,
      "total": 50.00,
      "status": "pending",
      "_links": {
        "self": { "href": "/orders/123" },
        "customer": { "href": "/customers/456" },
        "payment": { "href": "/orders/123/payment" }
      }
    }
    ```

## 6. Idempotency

Ensure that safe (GET, HEAD, OPTIONS) and idempotent (GET, PUT, DELETE, HEAD, OPTIONS) methods behave as expected. Making the same request multiple times should yield the same result (state on the server) as making it once. POST and PATCH are generally not idempotent.

*   Handle potential duplicate requests gracefully, especially for non-idempotent operations (e.g., using unique request IDs or idempotency keys).

## 7. Security Considerations

*   **HTTPS:** Always use HTTPS to encrypt communication.
*   **Authentication:** Implement robust authentication (e.g., OAuth 2.0, JWT, API Keys). Don't roll your own.
*   **Authorization:** Enforce proper permissions (e.g., role-based access control) to ensure users can only access/modify resources they are allowed to.
*   **Input Validation:** Rigorously validate all input data (path parameters, query parameters, request bodies) to prevent injection attacks and ensure data integrity.
*   **Rate Limiting:** Protect your API from abuse by implementing rate limiting.
*   **Sensitive Data:** Avoid exposing sensitive data in URIs or error messages. Filter response data based on user permissions.
*   **CORS:** Configure Cross-Origin Resource Sharing (CORS) headers appropriately if the API needs to be accessed from web browsers on different domains.

## 8. Filtering, Sorting, Pagination

Provide mechanisms for clients to manage large collections:

*   **Filtering:** `/products?category=electronics&status=available`
*   **Sorting:** `/users?sort=lastName,-createdAt` (use +/- or similar convention)
*   **Pagination:**
    *   *Offset/Limit:* `/orders?offset=20&limit=10`
    *   *Cursor-based:* `/items?cursor=abcde12345&limit=10` (Generally preferred for performance on large datasets)
    *   Include pagination metadata in the response (e.g., total count, links to next/prev pages).

## 9. Request/Response Formats

*   **JSON:** Use JSON as the standard data format for request and response bodies.
*   **Content Negotiation:** Use `Accept` (client requests format) and `Content-Type` (server indicates response format, client indicates request format) headers correctly.
*   **Consistent Data Structures:** Maintain consistent field naming (e.g., camelCase, snake_case) and data structures across the API.
*   **Error Responses:** Provide clear and consistent error messages in the response body for 4xx/5xx errors, including specific error codes or details where helpful.
    ```json
    {
      "error": {
        "code": "VALIDATION_ERROR",
        "message": "Invalid email address provided.",
        "details": [
          { "field": "email", "issue": "Must be a valid email format." }
        ]
      }
    }