# API Error Handling Best Practices

Designing consistent and informative error responses for REST and GraphQL APIs.

## Core Concept: Communicating Failure Clearly

When an API request fails (due to client error, server error, or other issues), the response should clearly communicate:

1.  **That an error occurred:** Indicated primarily by the HTTP status code (for REST).
2.  **What went wrong:** A machine-readable error code or type and a human-readable message.
3.  **Specific details (if applicable):** For validation errors, indicate which fields failed and why.
4.  **How to potentially resolve it (optional):** Links to documentation or suggestions.

Consistent error handling improves the developer experience for API consumers and aids debugging.

## REST API Error Handling

*   **Use Appropriate HTTP Status Codes:** Select the most specific 4xx (client error) or 5xx (server error) status code (see `rest-api-design-principles.md`).
*   **Consistent JSON Error Body:** Define a standard JSON structure for error responses. Common structures include:
    *   **Simple:**
        ```json
        {
          "error": "Authentication Failed",
          "message": "Invalid credentials provided."
        }
        ```
    *   **More Detailed (RFC 7807 Problem Details inspired):**
        ```json
        {
          "type": "/errors/authentication-failed", // URL to error documentation (optional)
          "title": "Authentication Failed", // Short summary
          "status": 401, // Mirror HTTP status
          "detail": "Invalid username or password provided.", // Human-readable detail
          "instance": "/auth/login" // Specific endpoint instance (optional)
        }
        ```
    *   **Validation Errors:** Include details about specific field errors.
        ```json
        {
          "title": "Validation Failed",
          "status": 422,
          "detail": "One or more fields failed validation.",
          "errors": [
            {
              "field": "email",
              "message": "Email address must be valid."
            },
            {
              "field": "password",
              "message": "Password must be at least 8 characters long."
            }
          ]
        }
        ```
*   **Avoid Revealing Sensitive Information:** Do not include stack traces, database error details, or internal configuration in production error responses. Log these details server-side.
*   **Use `Content-Type: application/json`** (or `application/problem+json` for RFC 7807).

## GraphQL API Error Handling

GraphQL has a built-in mechanism for returning errors alongside partial data.

*   **Top-Level `errors` Array:** The standard GraphQL response includes a top-level `data` field (nullable) and an optional `errors` field (array). Errors encountered during query execution are added to this array.
    ```json
    {
      "errors": [
        {
          "message": "Cannot query field 'nonExistentField' on type 'User'.",
          "locations": [{ "line": 3, "column": 5 }],
          "path": ["user", "nonExistentField"],
          "extensions": { // Optional custom data
            "code": "GRAPHQL_VALIDATION_FAILED",
            "timestamp": "2023-10-27T10:00:00Z"
          }
        }
      ],
      "data": null // Or potentially partial data if some fields resolved
    }
    ```
*   **Error Structure:** Each error object typically includes:
    *   `message`: Human-readable description.
    *   `locations`: Line/column in the query where the error occurred.
    *   `path`: Field path leading to the error.
    *   `extensions`: A map for adding custom, machine-readable error information (like error codes, timestamps). **This is the standard place for custom error details.**
*   **Throwing Errors in Resolvers:** Throw standard `Error` objects or custom error classes within your resolvers. GraphQL server libraries typically catch these and format them into the `errors` array. Attach custom data to the error object to populate the `extensions` field.
*   **Partial Success:** GraphQL allows returning partial data (`data` field is not null) even if some fields failed to resolve (those errors appear in the `errors` array).
*   **Mutation Payloads:** For business logic errors (e.g., validation failures specific to a mutation), it's often better practice to return specific error information *within* the mutation's payload type rather than relying solely on the top-level `errors` array. This makes expected business errors part of the schema contract.
    ```graphql
    type UserError {
      field: String # e.g., "email"
      message: String!
    }

    type CreateUserPayload {
      user: User # Null if creation failed due to validation
      errors: [UserError!] # Empty array on success
    }

    type Mutation {
      createUser(input: CreateUserInput!): CreateUserPayload
    }
    ```

**General Best Practices:**

*   **Consistency:** Use a consistent error structure (REST) or leverage the standard `errors` array and `extensions` (GraphQL).
*   **Machine-Readable Codes:** Include unique error codes (e.g., `AUTH_INVALID_TOKEN`, `VALIDATION_REQUIRED_FIELD`) in the response (`extensions` in GraphQL, a dedicated field in REST JSON) to allow clients to handle specific errors programmatically.
*   **Human-Readable Messages:** Provide clear messages suitable for display to end-users (but avoid sensitive details).
*   **Log Detailed Errors Server-Side:** Log the full error details, including stack traces, on the server for debugging.

Consistent and informative error handling is crucial for API usability and maintainability. Choose a standard format and apply it across your API.

*(Refer to RFC 7807 for REST Problem Details and GraphQL documentation on Error Handling.)*