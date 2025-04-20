# MongoDB: Indexing Strategies

Creating and managing indexes to optimize query performance in MongoDB.

## Core Concept

Indexes support the efficient execution of queries in MongoDB. Without indexes, MongoDB must perform a collection scan (reading every document) to find matching documents. Indexes store a small portion of the collection's data set in an easy-to-traverse form, allowing MongoDB to select documents more efficiently.

## Creating Indexes (`createIndex()`)

*   Use the `db.collection.createIndex()` method in `mongosh` or the equivalent method in your driver.
*   **Syntax:** `db.collection.createIndex( { <field1>: <type>, <field2>: <type2>, ... }, { options } )`
    *   **`<field>`:** The field to index.
    *   **`<type>`:** The index type/direction:
        *   `1`: Ascending order.
        *   `-1`: Descending order.
        *   `"text"`: For text search (requires specific setup).
        *   `"2dsphere"`: For geospatial queries.
        *   `"hashed"`: For hashed indexes (equality matches on sharded keys).
*   **Options:**
    *   `name`: Custom name for the index.
    *   `unique: true`: Enforces uniqueness for the indexed field(s). Duplicate values will cause write errors.
    *   `sparse: true`: Only index documents that contain the indexed field. Useful for optional fields where most documents lack the field.
    *   `background: true`: Builds the index in the background, allowing other operations during creation (slower build). Default in newer MongoDB versions.
    *   `partialFilterExpression: { <filter> }`: Only index documents matching the filter expression.
    *   `expireAfterSeconds: <seconds>`: TTL (Time-To-Live) index. Documents are automatically deleted after the specified seconds past the indexed date field's value. The indexed field *must* be a date type.

```javascript
// mongosh examples

// Single-field index on 'username' (ascending)
db.users.createIndex( { username: 1 } )

// Unique index on 'email'
db.users.createIndex( { email: 1 }, { unique: true } )

// Compound index on 'status' (asc) and 'created_at' (desc)
db.orders.createIndex( { status: 1, created_at: -1 } )

// Text index on 'title' and 'description' fields
db.articles.createIndex( { title: "text", description: "text" } )

// Geospatial index on 'location' field (GeoJSON Point)
db.places.createIndex( { location: "2dsphere" } )

// TTL index: Documents expire 1 hour after 'expireAt' field value
db.sessions.createIndex( { expireAt: 1 }, { expireAfterSeconds: 0 } )
// Note: expireAfterSeconds is relative to the field value. 0 means expire AT the time specified.
// Common pattern: Set expireAt = new Date(Date.now() + 3600 * 1000) for 1 hour expiry

// Partial index: Only index active users
db.users.createIndex( { last_login: -1 }, { partialFilterExpression: { status: "active" } } )
```

## Index Types

*   **Single Field:** Index on a single field. Supports queries filtering/sorting on that field.
*   **Compound Index:** Index on multiple fields. The order of fields matters significantly. Supports queries that filter/sort on a *prefix* of the indexed fields.
    *   Example: Index `{ userid: 1, score: -1 }` supports queries on `userid` alone, and queries on `userid` and `score` together. It does *not* efficiently support queries filtering only on `score`.
*   **Multikey Index:** Automatically created when indexing a field containing an array value. Indexes each element in the array.
*   **Text Index:** Supports text search queries (`$text` operator) on string content. A collection can have *at most one* text index. Can include multiple fields.
*   **Geospatial Index (`2dsphere`):** Supports queries on geospatial data (points, lines, polygons) using operators like `$geoWithin`, `$geoIntersects`, `$nearSphere`. Requires GeoJSON format for data.
*   **Hashed Index:** Indexes the hash of a field's value. Supports equality matches, often used for Hashed Sharding. Does *not* support range queries.
*   **TTL Index:** Special single-field index that automatically removes documents after a certain time period based on a date field.

## Indexing Strategies & Best Practices

*   **ESR (Equality, Sort, Range) Rule:** For compound indexes, structure them generally as:
    1.  Fields used for equality matches (`field: "value"`).
    2.  Fields used for sorting (`sort({ field: 1 })`).
    3.  Fields used for range queries (`field: { $gt: value }`).
*   **Index Selectivity:** Indexes are most effective when they significantly reduce the number of documents MongoDB needs to examine. Indexing low-cardinality fields (like boolean flags) might not be very helpful unless combined with other fields in a compound index.
*   **Covered Queries:** If an index contains *all* the fields required by a query (both for filtering/sorting and projection), MongoDB can satisfy the query using *only* the index, without fetching the documents themselves. This is highly efficient. Ensure your projection (`{ field: 1 }`) matches the fields in the index.
*   **Index Intersection:** MongoDB can sometimes use multiple indexes to satisfy different parts of a query, but designing a single compound index that matches the query pattern is usually more performant.
*   **Write Performance:** Indexes improve read performance but incur a cost on write operations (inserts, updates, deletes), as the index must also be updated. Avoid creating unnecessary indexes.
*   **Memory Usage:** Indexes consume RAM. Monitor index size (`db.collection.totalIndexSize()`).
*   **Analyze Queries (`explain()`):** Use `db.collection.find(...).explain("executionStats")` to understand how MongoDB executes a query, which index (if any) is used (`winningPlan.inputStage.indexName`), how many documents were scanned (`totalDocsExamined`), and how many keys were scanned (`totalKeysExamined`). This is crucial for identifying missing or inefficient indexes. Look for `COLLSCAN` (collection scan) which indicates no suitable index was used.

Choosing the right indexes based on your application's query patterns is critical for MongoDB performance.

*(Refer to the official MongoDB Indexing documentation: https://www.mongodb.com/docs/manual/indexes/)*