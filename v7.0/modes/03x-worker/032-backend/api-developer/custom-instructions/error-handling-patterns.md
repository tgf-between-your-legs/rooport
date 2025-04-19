# API Error Handling Patterns

Designing consistent and informative error responses for APIs.

## Goals of Good Error Handling

*   **Informative:** Help the client (and potentially the end-user) understand what went wrong.
*   **Consistent:** Use a standard format for all errors across the API.
*   **Secure:** Avoid leaking sensitive internal details (stack traces, database errors) in production responses.
*   **Actionable:** Provide guidance on how the client might resolve the issue, if possible.

## REST API Error Handling

*   **Use HTTP Status Codes:** Leverage standard HTTP status codes appropriately:
    *   `400 Bad Request`: General client-side error (e.g., invalid syntax, missing parameters). Often used for validation errors.
    *   `401 Unauthorized`: Authentication is required and has failed or has not yet been provided.
    *   `403 Forbidden`: The server understood the request, but refuses to authorize it (user authenticated but lacks permission).
    *   `404 Not Found`: The requested resource could not be found.
    *   `405 Method Not Allowed`: The HTTP method used is not supported for the requested resource.
    *   `409 Conflict`: The request could not be completed due to a conflict with the current state of the resource (e.g., trying to create a resource that already exists).
    *   `422 Unprocessable Entity`: The server understands the content type and syntax, but was unable to process the contained instructions (often used for semantic validation errors).
    *   `429 Too Many Requests`: Rate limiting has been exceeded.
    *   `500 Internal Server Error`: A generic error message for unexpected server-side errors. Avoid returning specific details here in production.
    *   `502 Bad Gateway`: Invalid response from an upstream server.
    *   `503 Service Unavailable`: The server is temporarily unavailable (e.g., maintenance, overload).
    *   `504 Gateway Timeout`: Did not receive a timely response from an upstream server.
*   **Consistent Error Response Body:** Define a standard JSON structure for error responses, especially for 4xx errors.
    *   **RFC 7807 Problem Details:** A standard format for HTTP API errors.
        ```json
        // Example RFC 7807 Response (Status: 400 Bad Request)
        {
          "type": "https://example.com/probs/validation-error", // URL identifying the error type
          "title": "Validation Failed", // Short, human-readable summary
          "status": 400, // The HTTP status code
          "detail": "One or more fields failed validation.", // Human-readable explanation
          "instance": "/users/123/email", // Optional: Specific resource instance related to the error
          // Extension members for more details (e.g., validation errors)
          "invalid-params": [
            {
              "name": "email",
              "reason": "must be a valid email address"
            },
            {
                "name": "age",
                "reason": "must be a positive number"
            }
          ]
        }
        ```
    *   **Simpler Custom Format:** If RFC 7807 is too complex, define a simpler consistent structure.
        ```json
        // Example Simpler Format (Status: 400 Bad Request)
        {
          "error": {
            "code": "VALIDATION_ERROR", // Machine-readable error code
            "message": "Input validation failed.", // Human-readable message
            "details": [ // Optional array for specific field errors
              { "field": "email", "issue": "Invalid format" },
              { "field": "password", "issue": "Too short" }
            ]
          }
        }
        ```
*   **Validation Errors:** For `400` or `422` validation errors, include details about which fields failed and why (as shown in the examples above).

## GraphQL Error Handling

*   **Top-Level `errors` Array:** GraphQL responses have a standard top-level `errors` array. This should primarily be used for **system-level** or **request-level** errors (e.g., query syntax errors, network issues preventing part of the query, internal server errors during resolution). Avoid putting expected application/validation errors here.
    ```json
    {
      "errors": [
        {
          "message": "Cannot query field 'emal' on type 'User'. Did you mean 'email'?",
          "locations": [{ "line": 3, "column": 5 }],
          "extensions": { "code": "GRAPHQL_VALIDATION_FAILED" }
        },
        {
          "message": "Internal server error occurred.",
          "locations": [{ "line": 4, "column": 7 }],
          "path": ["user", "address"], // Path to the field where error occurred
          "extensions": { "code": "INTERNAL_SERVER_ERROR" }
        }
      ],
      "data": {
        "user": {
          "name": "Alice",
          "address": null // Field resolver failed, returns null
        }
      }
    }
    ```
*   **Partial Responses:** If a resolver for a *nullable* field fails, GraphQL returns `null` for that field and adds an error to the top-level `errors` array, but still returns data for other successful fields. If a resolver for a *non-nullable* field fails, the error propagates up, potentially nullifying parent fields.
*   **Application/User Errors (In Payload):** For predictable errors related to business logic or validation (e.g., "Email already taken", "Password too short"), return these as part of the `data` payload, typically within the mutation's response type.
    *   **Dedicated Error Types:** Define specific error types in your schema (often implementing a common `UserError` interface).
    *   **Union Types:** Use union types in mutation payloads to indicate either success data or specific error types.
    ```graphql
    interface UserError {
      message: String!
      field: String # Optional field path
    }

    type EmailTakenError implements UserError {
      message: String!
      field: String!
      email: String!
    }

    type CreateUserSuccess {
      user: User!
    }

    union CreateUserResult = CreateUserSuccess | EmailTakenError # Add other error types

    type Mutation {
      createUser(input: CreateUserInput!): CreateUserResult!
    }
    ```
    ```json
    // Example Response for Validation Error
    {
      "data": {
        "createUser": {
          "__typename": "EmailTakenError", // Tells client which type in the union was returned
          "message": "Email address is already in use.",
          "field": "email",
          "email": "test@example.com"
        }
      }
    }
    ```

## General Best Practices

*   **Log Server Errors:** Always log detailed internal server errors (`5xx` in REST, top-level `errors` in GraphQL) on the server-side for debugging, but don't expose stack traces or sensitive details to the client in production.
*   **Error Codes:** Consider using machine-readable error codes (`VALIDATION_ERROR`, `AUTH_EXPIRED`, etc.) in addition to human-readable messages to allow clients to handle specific errors programmatically.
*   **Documentation:** Clearly document your error response formats and common error codes/types.