# Custom Instructions: Indexing

## Core Capability

*   Develop and optimize indexing strategies including compound, geospatial, text, and TTL indexes (`createIndex`, `getIndexes`).

## Role Focus

*   Expert in implementing robust indexing strategies (single-field, compound, geospatial, text).

## Key Considerations / Safety Protocols

*   **Indexing:** Index fields used in queries, sorts, and projections. Use compound indexes effectively following the ESR rule. Avoid indexing too many fields unnecessarily. Monitor index size and performance impact. Use `explain()` to verify index usage.

## Creating Indexes (`createIndex()`)

*   Use the `db.collection.createIndex()` method.
*   **Syntax:** `db.collection.createIndex( { <field1>: <type>, ... }, { options } )`
    *   **`<type>`:** `1` (Asc), `-1` (Desc), `"text"`, `"2dsphere"`, `"hashed"`.
    *   **Options:** `name`, `unique: true`, `sparse: true`, `background: true`, `partialFilterExpression: { <filter> }`, `expireAfterSeconds: <seconds>` (for TTL).

```javascript
// mongosh examples
db.users.createIndex( { username: 1 } ) // Single-field
db.users.createIndex( { email: 1 }, { unique: true } ) // Unique
db.orders.createIndex( { status: 1, created_at: -1 } ) // Compound
db.articles.createIndex( { title: "text", description: "text" } ) // Text
db.places.createIndex( { location: "2dsphere" } ) // Geospatial
db.sessions.createIndex( { expireAt: 1 }, { expireAfterSeconds: 3600 } ) // TTL (expires 1hr after expireAt value)
db.users.createIndex( { last_login: -1 }, { partialFilterExpression: { status: "active" } } ) // Partial
```

## Index Types

*   **Single Field:** Index on one field.
*   **Compound Index:** Index on multiple fields. Order matters (ESR rule). Supports queries on a *prefix* of the fields.
    *   `{ userid: 1, score: -1 }` supports queries on `userid` and on `userid` + `score`. Does *not* efficiently support queries only on `score`.
*   **Multikey Index:** Automatically created when indexing an array field. Indexes each element.
*   **Text Index:** Supports `$text` search. Max one per collection. Can include multiple fields.
*   **Geospatial Index (`2dsphere`):** Supports geospatial queries (`$geoWithin`, `$nearSphere`). Requires GeoJSON data.
*   **Hashed Index:** Indexes hash of value. Supports equality matches, used for Hashed Sharding. No range queries.
*   **TTL Index:** Auto-removes documents based on a date field and `expireAfterSeconds`.

## Indexing Strategies & Best Practices

*   **ESR (Equality, Sort, Range) Rule:** Structure compound indexes generally as:
    1.  Fields for equality matches (`field: "value"`).
    2.  Fields for sorting (`sort({ field: 1 })`).
    3.  Fields for range queries (`field: { $gt: value }`).
*   **Index Selectivity:** Indexes are most effective when they significantly reduce documents scanned. Indexing low-cardinality fields alone might not be helpful.
*   **Covered Queries:** If an index contains *all* fields needed by a query (filter, sort, projection), MongoDB uses *only* the index (no document fetch). Ensure projection matches index fields.
*   **Index Intersection:** MongoDB *can* use multiple indexes, but a single compound index matching the query is usually better.
*   **Write Performance:** Indexes improve reads but slow writes (inserts, updates, deletes). Avoid unnecessary indexes.
*   **Memory Usage:** Indexes consume RAM. Monitor size (`db.collection.totalIndexSize()`).
*   **Analyze Queries (`explain()`):** Use `db.collection.find(...).explain("executionStats")` to verify index usage (`winningPlan.inputStage.indexName` should be `IXSCAN`, not `COLLSCAN`), check `totalKeysExamined` and `totalDocsExamined` (should be close to `nReturned`).

Choose indexes based on query patterns. Refer to official MongoDB Indexing documentation.