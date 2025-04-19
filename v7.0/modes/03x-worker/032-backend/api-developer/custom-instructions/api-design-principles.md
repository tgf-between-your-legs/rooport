# General API Design Principles

Guiding principles for creating well-designed APIs, applicable to both REST, GraphQL, and other styles.

## 1. Predictability & Consistency

*   **Naming Conventions:** Use consistent naming for resources, fields, arguments, operations (e.g., camelCase for fields, PascalCase for types, consistent pluralization for REST resources).
*   **Data Formats:** Use consistent data formats (e.g., ISO 8601 for dates, standard country/currency codes).
*   **Structure:** Maintain a consistent structure for requests and responses, especially for common elements like errors, pagination, and metadata.
*   **Behavior:** Ensure similar operations behave similarly across the API.

## 2. Simplicity & Clarity

*   **Intuitive Naming:** Choose names that clearly reflect the purpose or content of resources, fields, and operations. Avoid jargon or overly technical terms where simpler alternatives exist.
*   **Minimalism:** Design endpoints/schemas to expose only the necessary data and functionality for the intended use cases. Avoid overly complex or "chatty" APIs.
*   **Clear Documentation:** Provide comprehensive and easy-to-understand documentation (e.g., OpenAPI, GraphQL schema docs with descriptions).

## 3. Resource/Type Orientation (Focus on the "Nouns")

*   **REST:** Focus on well-defined resources (nouns, e.g., `/users`, `/products/{id}`) and use standard HTTP methods (verbs: GET, POST, PUT, DELETE, PATCH) to operate on them.
*   **GraphQL:** Focus on defining a clear type system (schema) representing the application's data graph. Queries fetch data from this graph, and mutations modify it.
*   **Avoid RPC-Style:** Generally avoid designing APIs around actions/verbs (e.g., `/getUser`, `/updateProductPrice`). Focus on the data entities themselves.

## 4. Effective Error Handling

*   **Standard Codes:** Use standard HTTP status codes correctly (REST) or define clear error types/codes (GraphQL) to indicate the outcome of a request.
*   **Informative Messages:** Provide clear, concise, and helpful error messages, especially for validation or user errors. Avoid exposing sensitive internal details.
*   **Consistent Format:** Use a consistent structure for error responses (e.g., RFC 7807 Problem Details for HTTP, dedicated `errors` field in GraphQL mutation payloads).

## 5. Versioning Strategy

*   **Plan for Change:** APIs evolve. Have a clear strategy for introducing breaking changes.
*   **Common Strategies:**
    *   **URL Versioning (REST):** `/v1/users`, `/v2/users` (Simple, explicit).
    *   **Header Versioning (REST):** Use `Accept` or custom headers (e.g., `Api-Version: 2`).
    *   **GraphQL:** Often avoids explicit versioning by evolving the schema additively (deprecating old fields rather than removing them immediately). Breaking changes still require careful rollout.
*   **Communicate Changes:** Clearly document changes and deprecation timelines for API consumers.

## 6. Security Considerations

*   **Authentication:** Secure endpoints appropriately (e.g., OAuth 2.0, JWT, API Keys).
*   **Authorization:** Ensure users can only access or modify data they are permitted to. Implement checks at the appropriate layer.
*   **Input Validation:** Rigorously validate all incoming data (parameters, request bodies, arguments).
*   **Rate Limiting:** Protect against abuse.
*   **HTTPS:** Always use HTTPS.

## 7. Performance & Scalability

*   **Efficient Data Fetching:** Design endpoints/resolvers to retrieve data efficiently (avoid N+1 problems).
*   **Pagination:** Implement pagination for list endpoints/fields.
*   **Caching:** Leverage HTTP caching (REST) or application-level caching where appropriate.
*   **Payload Size:** Avoid unnecessarily large request/response payloads. Allow clients to select fields (GraphQL native, sparse fieldsets in REST).

## 8. Consumer Focus

*   Design the API with the needs and perspective of the client applications (frontend web, mobile apps, third-party integrations) in mind.
*   Make it easy for consumers to understand and use the API correctly.

Adhering to these principles leads to APIs that are easier to use, maintain, evolve, and secure.