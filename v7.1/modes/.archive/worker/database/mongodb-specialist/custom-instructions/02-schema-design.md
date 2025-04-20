# Custom Instructions: Schema Design

## Core Capability

*   Design efficient MongoDB schemas using embedding and referencing strategies.
*   Implement schema validation with `$jsonSchema`.

## Role Focus

*   Expert in designing efficient MongoDB schemas (document modeling, embedding vs. referencing).

## Key Considerations / Safety Protocols

*   **Schema Design:** Carefully consider embedding vs. referencing based on access patterns and data size. Avoid overly large documents (approaching the 16MB BSON limit).
*   **Schema Validation:** Implement schema validation using `$jsonSchema` within `createCollection` or `collMod` commands to enforce data structure and types, improving data quality and preventing unexpected errors.

## Schema Design Patterns

### Core Concept: Flexibility vs. Performance

MongoDB's flexible schema allows documents in the same collection to have different fields. However, designing your schema effectively is crucial for performance, queryability, and data consistency. The main trade-off is between **embedding** related data within a single document versus **referencing** data across multiple documents/collections.

### 1. Embedding (Denormalization)

*   **Concept:** Store related data together within a single document, often using nested objects or arrays.
*   **Example:** Storing address details directly within a `user` document, or storing `comments` as an array within a `post` document.
    ```json
    // User document with embedded address
    {
      "_id": ObjectId("..."), "name": "Alice", "email": "alice@example.com",
      "address": { "street": "123 Main St", "city": "Anytown", "zip": "12345" }
    }
    // Post document with embedded comments array
    {
      "_id": ObjectId("..."), "title": "My Blog Post", "content": "...",
      "comments": [
        { "user": "Bob", "text": "Great post!", "timestamp": ISODate("...") },
        { "user": "Charlie", "text": "I agree.", "timestamp": ISODate("...") }
      ]
    }
    ```
*   **Pros:** Faster Reads (single query), Atomicity (updates to single doc).
*   **Cons:** Larger Documents (16MB limit), Update Complexity, Data Duplication.
*   **When to Use:** "Contains" relationships (one-to-few), data accessed together, data doesn't change often independently, atomicity needed, read performance paramount.

### 2. Referencing (Normalization)

*   **Concept:** Store related data in separate collections and use references (typically the `_id`) to link them.
*   **Example:** Storing `user_id` in a `post` document linking to the `users` collection.
    ```json
    // users collection
    { "_id": ObjectId("user1"), "name": "Alice" }
    // posts collection
    { "_id": ObjectId("post1"), "title": "...", "user_id": ObjectId("user1") }
    ```
*   **Pros:** Smaller Documents, Easier Updates (no duplication), Flexibility (many-to-many, large one-to-many).
*   **Cons:** Slower Reads (potentially, requires `$lookup` or multiple queries), No Automatic Joins.
*   **When to Use:** "Belongs to" relationships (one-to-many, many-to-many), related data changes frequently or is large, avoiding 16MB limit, data consistency important.

### 3. Two-Way Referencing

*   **Concept:** Store references on both sides (e.g., `user` has `post_ids`, `post` has `user_id`).
*   **Pros:** Query relationship from either side without `$lookup`.
*   **Cons:** Increased complexity to maintain consistency during updates/deletes.

### 4. Denormalization (Subset Embedding)

*   **Concept:** Embed a *subset* of frequently needed data from a related document, while still maintaining a reference for the full document.
*   **Example:** Embedding `user.name` and `user._id` in comments.
    ```json
    {
      "_id": ObjectId("..."), "title": "...",
      "comments": [
        { "user": { "_id": ObjectId("user1"), "name": "Alice" }, "text": "...", "timestamp": ISODate("...") }
      ]
    }
    ```
*   **Pros:** Improves read performance for common cases, avoids `$lookup`.
*   **Cons:** Some data duplication, requires updating embedded subset if source changes.

### Choosing the Right Pattern

Analyze your application's data access patterns:

*   **Read vs. Write Frequency:** Frequent reads together favor embedding. Frequent independent updates favor referencing.
*   **Data Cardinality:** One-to-few favors embedding. One-to-many/many-to-many favor referencing.
*   **Data Size:** Avoid embedding large/unbounded data.
*   **Atomicity Needs:** Embedding is simpler for atomicity. Transactions handle cross-document atomicity but add complexity.
*   **Consistency:** Referencing ensures consistency. Embedding requires managing potential inconsistencies.

Use a mix of patterns as needed. Consult official MongoDB Data Modeling documentation for more details.

### Schema Validation (`$jsonSchema`)

*   **Purpose:** Enforce structure, data types, and constraints on documents within a collection.
*   **Usage:** Defined during collection creation (`db.createCollection`) or modification (`collMod`).
*   **Example:**
    ```javascript
    db.createCollection("users", {
      validator: {
        $jsonSchema: {
          bsonType: "object",
          required: ["name", "email", "status"],
          properties: {
            name: {
              bsonType: "string",
              description: "must be a string and is required"
            },
            email: {
              bsonType: "string",
              pattern: "^.+@.+$", // Basic email pattern
              description: "must be a string matching regex and is required"
            },
            status: {
              enum: ["active", "inactive", "pending"],
              description: "can only be one of the enum values and is required"
            },
            year_joined: {
              bsonType: "int",
              minimum: 2000,
              maximum: 3000,
              description: "must be an integer in [ 2000, 3000 ]"
            },
            address: { // Nested object validation
              bsonType: "object",
              required: ["street", "city"],
              properties: {
                street: { bsonType: "string" },
                city: { bsonType: "string" },
                zip: { bsonType: "string" }
              }
            }
          }
        }
      },
      validationAction: "error", // 'error' (reject invalid docs) or 'warn' (log warning)
      validationLevel: "strict" // 'strict' (apply to all inserts/updates) or 'moderate' (apply to valid docs + new/updated fields)
    })
    ```
*   **Benefits:** Improves data quality, prevents errors, acts as documentation.