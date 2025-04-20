# API Data Formats: JSON Conventions

Best practices for structuring JSON data in API requests and responses.

## Core Concept: Standardized Data Exchange

JSON (JavaScript Object Notation) is the most common data format for REST APIs due to its simplicity, human-readability, and widespread support across languages. Establishing consistent conventions for your JSON payloads improves interoperability and developer experience.

## Key Conventions

1.  **Use `application/json` Content-Type:** Always set the `Content-Type: application/json` header for requests sending JSON data and responses containing JSON data. Clients should also send `Accept: application/json` to indicate they prefer JSON responses.

2.  **Property Naming Convention:** Choose a consistent case convention for object keys (property names) and stick to it.
    *   **`camelCase` (e.g., `userName`, `createdAt`):** Very common in JavaScript-heavy ecosystems (Node.js, frontend frameworks). Often the default.
    *   **`snake_case` (e.g., `user_name`, `created_at`):** Common in Python, Ruby, and PHP ecosystems.
    *   **Consistency is key.** Avoid mixing cases within the same API. Document the chosen convention.

3.  **Date/Time Formatting:** Use a standard, unambiguous format.
    *   **ISO 8601 String (Recommended):** `YYYY-MM-DDTHH:mm:ss.sssZ` (e.g., `"2023-10-27T10:30:00Z"` for UTC) or including timezone offset (`"2023-10-27T20:30:00+10:00"`). This is machine-readable and widely supported.
    *   **Unix Timestamp (Seconds or Milliseconds):** A number representing seconds or milliseconds since the Unix epoch (Jan 1, 1970 UTC). Less human-readable but compact. Be consistent about using seconds or milliseconds.

4.  **Representing Relationships:**
    *   **Nested Objects:** Embed related resources directly if the relationship is one-to-one or one-to-few, and the data is frequently needed together. Can lead to larger payloads.
        ```json
        {
          "id": 123,
          "title": "Post Title",
          "author": { // Embedded author object
            "id": 456,
            "name": "Alice"
          }
        }
        ```
    *   **Resource IDs:** Include only the ID of the related resource. The client needs to make a separate request to fetch the full related resource if needed. Keeps payloads smaller.
        ```json
        {
          "id": 123,
          "title": "Post Title",
          "authorId": 456 // ID of the author
        }
        ```
    *   **Hypermedia Links (HATEOAS):** Include URIs pointing to related resources (see `rest-api-design-principles.md`).
        ```json
        {
          "id": 123,
          "title": "Post Title",
          "_links": {
            "self": { "href": "/posts/123" },
            "author": { "href": "/users/456" }
          }
        }
        ```
    *   Choose the approach based on client needs and performance trade-offs.

5.  **Handling Null/Empty Values:**
    *   Use JSON `null` for values that are explicitly absent or not applicable.
    *   Avoid omitting keys entirely for absent values unless clearly documented, as it can make client-side handling more complex (checking for property existence vs. checking for null). Consistency is important.
    *   Represent empty collections as empty arrays `[]`, not `null`.

6.  **Booleans:** Use JSON `true` and `false`. Avoid strings like `"true"` or numbers like `1`/`0`.

7.  **Error Responses:** Use a consistent JSON structure for error details (see `api-error-handling.md`).

**Example JSON Payload:**

```json
{
  "data": { // Optional envelope
    "id": "user-abc-123",
    "type": "user", // Optional resource type
    "attributes": {
      "userName": "johndoe",
      "email": "john.doe@example.com",
      "isActive": true,
      "lastLogin": "2023-10-26T15:05:10Z",
      "profile": { // Nested object
        "bio": "Developer",
        "website": null // Explicit null
      },
      "roles": ["editor", "viewer"] // Array
    },
    "relationships": { // Optional section for related resource IDs/links
      "organization": {
        "data": { "type": "organization", "id": "org-xyz" }
        // "_links": { "related": "/organizations/org-xyz" } // HATEOAS style
      }
    },
    "_links": { // Optional HATEOAS links
      "self": { "href": "/users/user-abc-123" }
    }
  },
  "meta": { // Optional metadata
    "timestamp": "2023-10-27T12:00:00Z"
  }
}
```
*(Note: Structures like JSON:API define more specific conventions for relationships, links, and metadata).*

Using consistent JSON formatting, naming conventions, and standard date formats makes your API predictable and easier for clients to integrate with. Document your chosen conventions clearly.