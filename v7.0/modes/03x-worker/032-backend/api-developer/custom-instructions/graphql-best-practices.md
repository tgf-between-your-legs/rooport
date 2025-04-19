# GraphQL API Best Practices

Guidelines for designing and implementing effective GraphQL APIs.

## Schema Design (SDL)

*   **Strong Typing:** Leverage the type system. Define clear scalar types (`String`, `Int`, `Float`, `Boolean`, `ID`), enums, objects, interfaces, and unions. Avoid excessive use of generic `JSON` or `Object` scalars.
*   **Nullability:** Be intentional about nullability (`Type` vs `Type!`). Make fields non-nullable (`!`) only when you can guarantee a value will always be returned. For lists, consider `[Type!]!` (non-null list of non-null items), `[Type]!` (non-null list of nullable items), or `[Type!]` (nullable list of non-null items) based on requirements.
*   **Descriptive Naming:** Use clear, consistent, and predictable names for types, fields, arguments, and enums. Follow common conventions (e.g., PascalCase for types, camelCase for fields/arguments).
*   **Use Interfaces/Unions:** Model polymorphic relationships using interfaces (shared fields) or unions (distinct possible types).
*   **Input Objects:** Use `input` types for complex arguments in mutations to keep argument lists clean and allow for easier evolution.
*   **Enums:** Use `enum` for fields with a fixed set of allowed string values.
*   **Documentation:** Add descriptions to types, fields, and arguments using GraphQL schema comments (`""" Description """` or `# Description`).

## Queries

*   **Design for Client Needs:** Structure queries to allow clients to fetch exactly the data they need in a single request, avoiding over-fetching or under-fetching.
*   **Pagination:** Implement standardized pagination for lists (e.g., cursor-based pagination using the Relay Cursor Connections Specification is common and robust). Avoid offset/limit pagination for large datasets or real-time updates.
*   **Filtering & Sorting:** Provide arguments on list fields for filtering and sorting capabilities.

## Mutations

*   **Verb-Based Naming:** Name mutations based on the action being performed (e.g., `createUser`, `updatePost`, `deleteComment`).
*   **Single Action per Mutation:** Each mutation should generally perform one logical write operation.
*   **Input Objects:** Use a single, non-nullable `input` object argument for mutations to group related arguments and allow for easier extension.
*   **Return Payload:** Design mutation return types (payloads) carefully.
    *   Include the data that was modified, allowing clients to update their cache easily without needing to re-fetch.
    *   Include a client mutation ID (if following Relay spec) to help clients match requests with responses.
    *   Include specific error fields or use union types to represent potential errors gracefully (see Error Handling).
    ```graphql
    type UpdatePostPayload {
      clientMutationId: String
      post: Post # The updated post
      errors: [UserError!] # List of user-facing errors, if any
    }

    type Mutation {
      updatePost(input: UpdatePostInput!): UpdatePostPayload
    }
    ```

## Error Handling

*   **Distinguish Error Types:** Differentiate between system errors (server unavailable, internal errors) and user/validation errors (invalid input, permission denied).
*   **User Errors in Payload:** For predictable errors (validation, permissions), return them as part of the mutation payload (e.g., a list of `UserError` objects with `field` and `message`). Don't use GraphQL's top-level `errors` array for these.
*   **Top-Level `errors`:** Reserve the top-level `errors` array in the GraphQL response for system-level or unexpected errors (exceptions during resolution).
*   **Nullable Fields:** If a field's resolver might fail independently, consider making that field nullable in the schema so the rest of the query can still succeed.

## Performance

*   **N+1 Problem:** Be aware of the N+1 query problem in resolvers for list fields. Use DataLoader or similar batching techniques to efficiently fetch related data.
*   **Query Complexity/Depth Limiting:** Implement limits on query complexity or depth to prevent malicious or overly expensive queries.
*   **Caching:** Leverage HTTP caching for queries where appropriate. Consider application-level caching for frequently accessed data.

## Security

*   **Authentication:** Implement robust authentication (e.g., JWT, sessions) typically at the HTTP layer or via context.
*   **Authorization:** Perform authorization checks within resolvers or a dedicated authorization layer to ensure users can only access/modify data they are permitted to. Check permissions before accessing data or performing mutations.
*   **Input Validation:** Validate all input arguments in mutations and queries rigorously.
*   **Rate Limiting:** Protect against abuse by implementing rate limiting.

*(Refer to official GraphQL documentation (graphql.org) and resources like Apollo GraphQL Best Practices.)*