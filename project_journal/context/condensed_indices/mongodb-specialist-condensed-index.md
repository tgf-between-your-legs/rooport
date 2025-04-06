## MongoDB vUnknown - Condensed Context Index

### Overall Purpose
MongoDB (Version Unknown) is a NoSQL document database designed for flexibility, scalability, and performance. It stores data in JSON-like BSON documents, supports dynamic schemas, and offers rich querying, aggregation, indexing, and security features for various application needs.

### Core Concepts & Capabilities:
*   **Document Model:** Stores data in flexible, JSON-like BSON documents (`_id`, nested fields, arrays). Supports polymorphic data within a collection.
*   **CRUD Operations:** Core functions for creating (`insertOne`, `insertMany`), reading (`find`, query operators like `$in`, `$gt`, `$lt`, `$geoWithin`), updating (`updateMany`, `$set`, `$inc`), and deleting documents.
*   **Aggregation Pipeline:** Powerful framework for multi-stage data processing and analysis (`aggregate`, `$match`, `$group`, `$project`, `$sort`, `$lookup`, `$bucket`).
*   **Indexing:** Optimizes query performance on specific fields or compound fields (`createIndex`, `getIndexes`, index prefixes).
*   **Schema Validation:** Enforces data structure rules during inserts/updates using `$jsonSchema` within `createCollection` or `collMod`.
*   **User Management & Security:** Role-based access control (RBAC) for managing user permissions (`createUser`, roles like `readWrite`, `dbAdmin`, `clusterAdmin`).
*   **Transactions:** Provides ACID guarantees for multi-document operations across one or more collections (`startSession`, `withTransaction`). Requires replica set/sharded cluster.
*   **Replication:** Ensures high availability and data redundancy through replica sets (`rs.initiate`).
*   **Change Streams:** Real-time monitoring of data changes in collections, databases, or deployments (`watch`).
*   **Client-Side Field Level Encryption (CSFLE):** Automatic encryption/decryption of specific document fields on the client-side for enhanced security. Requires driver/schema configuration.
*   **Backup & Monitoring:** Tools for database backup (`mongodump`) and monitoring active operations (`$currentOp`).

### Key APIs / Components / Configuration / Patterns:
*   `db.collection.find(<query>, <projection>)`: Core method for querying documents. `<query>` uses operators (e.g., `$in`, `$gt`, `$lt`, `$geoWithin`). `<projection>` selects fields.
*   `db.collection.insertOne(<document>)`: Inserts a single document.
*   `db.collection.insertMany([<doc1>, <doc2>, ...])`: Inserts multiple documents.
*   `db.collection.updateMany(<filter>, <update>, <options>)`: Updates multiple documents matching the filter. Uses update operators (`$set`, `$inc`, `$currentDate`).
*   `db.collection.aggregate([<stage1>, <stage2>, ...])`: Executes an aggregation pipeline.
    *   `$match`: Filters documents (similar to `find` query).
    *   `$group`: Groups documents by a key and computes aggregate values (`$sum`, `$avg`, `$month`).
    *   `$project`: Reshapes documents, includes/excludes fields, computes new fields.
    *   `$sort`: Sorts documents.
    *   `$lookup`: Performs a left outer join with another collection.
    *   `$bucket`: Groups documents into buckets based on boundaries.
*   `db.collection.createIndex({ <field>: <1|-1>, ... })`: Creates an index on specified fields (1=ascending, -1=descending).
*   `db.collection.getIndexes()`: Lists existing indexes on a collection.
*   `db.createCollection("<name>", { validator: { $jsonSchema: { ... } } })`: Creates a collection with schema validation rules.
*   `db.createUser({ user: "<name>", pwd: passwordPrompt(), roles: [...] })`: Creates a database user with specified roles.
*   `db.auth()` / `use <db>`: Authenticates / Switches the current database context in the shell.
*   `session.withTransaction(async () => { ... })`: Executes operations within an ACID transaction (requires replica set/sharded cluster).
*   `collection.watch(<pipeline>)`: Opens a change stream to monitor collection modifications (Python example shown).
*   `mongodump`: Command-line utility for creating database backups.
*   `$currentOp`: Aggregation stage or command to view active database operations.
*   **Client-Side Field Level Encryption (CSFLE):** Requires specific driver configuration and a Key Management System (KMS). Encrypts fields automatically based on schema configuration. (Conceptual, specific code varies by driver).
*   **Nested Field Querying:** Use dot notation to query fields within embedded documents (e.g., `"size.h": { $lt: 15 }`).

### Common Patterns & Best Practices / Pitfalls:
*   **Indexing:** Create indexes (`createIndex`) on frequently queried/sorted fields for performance. Use `getIndexes()` to verify. Compound indexes can serve queries on prefixes.
*   **Projections:** Limit fields returned by queries using projection (`find({}, { field: 1 })`) to reduce network traffic and processing load.
*   **Schema Validation:** Use `$jsonSchema` during collection creation (`createCollection`) or modification (`collMod`) to enforce data structure and prevent invalid data insertion.
*   **Transactions:** Use `session.withTransaction()` for atomic multi-document operations, but be aware they require replica sets/sharded clusters and have overhead.
*   **Aggregation:** Leverage the aggregation pipeline (`aggregate`) for complex data transformations and analysis server-side. Add comments for clarity.
*   **Security:** Use Role-Based Access Control (`createUser`, roles) for granular permissions. Consider CSFLE for sensitive field-level encryption.
*   **Change Streams:** Use `resume_token` to handle interruptions and resume monitoring changes reliably.
*   **Backup:** Regularly use tools like `mongodump` for backups.

---
This index summarizes the core concepts, APIs, and patterns for MongoDB (Version Unknown). Consult the full source documentation (project_journal/context/source_docs/mongodb-specialist-llms-context-20250406.md) for exhaustive details.