# MongoDB: Common Administrative Commands (`mongosh`)

Reference for common commands used in the MongoDB Shell (`mongosh`) for administration and inspection.

## Connecting

*   `mongosh`: Connect to a MongoDB instance running on `localhost:27017`.
*   `mongosh "mongodb://username:password@host:port/database?options"`: Connect using a connection string URI.
*   `mongosh --host <hostname> --port <port> -u <username> -p <password> --authenticationDatabase <authDB>`: Connect using individual options.

## Basic Shell Commands

*   `help`: Display help information.
*   `show dbs` or `show databases`: List all available databases.
*   `use <database_name>`: Switch the current database context.
*   `show collections`: List all collections in the current database.
*   `db`: Reference to the current database object.
*   `db.stats()`: Show statistics for the current database.
*   `db.<collection_name>.stats()`: Show statistics for a specific collection.
*   `cls` or `clear`: Clear the shell screen.
*   `exit` or `quit()`: Exit the shell.

## CRUD Operations (Shell Equivalents)

*   **Insert:**
    *   `db.collection.insertOne({ field: "value", ... })`
    *   `db.collection.insertMany([{ field: "value1" }, { field: "value2" }])`
*   **Find:**
    *   `db.collection.find({ query })`: Find documents matching the query. Returns a cursor.
    *   `db.collection.findOne({ query })`: Find the first document matching the query.
    *   `.pretty()`: Append to `find()` to format the output nicely.
    *   `.limit(N)`: Limit the number of documents returned.
    *   `.skip(N)`: Skip N documents.
    *   `.sort({ field: 1/-1 })`: Sort documents.
    *   `.count()`: Count matching documents (deprecated, use `countDocuments` or `estimatedDocumentCount`).
    *   `db.collection.countDocuments({ query })`: Accurate count based on query.
    *   `db.collection.estimatedDocumentCount()`: Faster count using metadata (no query).
*   **Update:**
    *   `db.collection.updateOne({ filter }, { $set: { field: "new_value" }, ... }, { upsert: true/false })`
    *   `db.collection.updateMany({ filter }, { $set: { field: "new_value" }, ... })`
    *   `db.collection.replaceOne({ filter }, { new_document }, { upsert: true/false })`
*   **Delete:**
    *   `db.collection.deleteOne({ filter })`
    *   `db.collection.deleteMany({ filter })`

## Index Management

*   `db.collection.createIndex({ field: 1/-1, ... }, { options })`: Create an index (see `indexing-strategies.md`).
*   `db.collection.getIndexes()`: List all indexes on a collection.
*   `db.collection.dropIndex("index_name")` or `db.collection.dropIndex({ field: 1 })`: Drop a specific index.
*   `db.collection.dropIndexes()`: Drop all indexes except the default `_id` index.
*   `db.collection.reIndex()`: Rebuilds all indexes on a collection (can be resource-intensive).

## Aggregation

*   `db.collection.aggregate([ { $match: ... }, { $group: ... }, ... ])`: Execute an aggregation pipeline.

## Diagnostics & Monitoring

*   `db.collection.find(...).explain("executionStats")`: Analyze query performance (see `performance-optimization.md`).
*   `db.currentOp()`: Display information on in-progress operations.
*   `db.serverStatus()`: Provides a detailed overview of the database server's state.
*   `db.setProfilingLevel(level, options)`: Enable database profiling (0=off, 1=slow ops, 2=all ops). Check `system.profile` collection for output. Use with caution in production.
    *   `db.setProfilingLevel(1, { slowms: 100 })`
    *   `db.getProfilingLevel()`
    *   `db.getProfilingStatus()`
    *   `show profile`
*   `rs.status()`: (Replica Sets) Show the status of the replica set.
*   `rs.conf()`: (Replica Sets) Show the replica set configuration.
*   `sh.status()`: (Sharded Clusters) Show the status of the sharded cluster.

## User & Role Management (Requires Admin Privileges)

*   `db.createUser({ user: "name", pwd: passwordPrompt(), roles: [ { role: "readWrite", db: "database" }, ... ] })`
*   `db.updateUser("name", { roles: [...], ... })`
*   `db.dropUser("name")`
*   `db.changeUserPassword("name", passwordPrompt())`
*   `db.createRole(...)`, `db.updateRole(...)`, `db.dropRole(...)`
*   `db.grantRolesToUser("name", [ { role: ..., db: ... } ])`
*   `db.revokeRolesFromUser("name", [ { role: ..., db: ... } ])`
*   `db.getUsers()`, `db.getRoles({ showBuiltinRoles: true })`

## Backup & Restore (Typically run from OS shell, not `mongosh`)

*   **`mongodump --uri="mongodb://..." --out=/path/to/backup/dir`**: Create a BSON dump of databases.
    *   `--db <db_name>`: Dump a specific database.
    *   `--collection <coll_name>`: Dump a specific collection.
    *   `--gzip`: Compress the output.
*   **`mongorestore --uri="mongodb://..." /path/to/backup/dir`**: Restore a dump.
    *   `--db <db_name>`: Restore to a specific database.
    *   `--collection <coll_name>`: Restore a specific collection.
    *   `--drop`: Drop collections before restoring.
    *   `--gzip`: If the dump was compressed.

This covers many common administrative and diagnostic commands used within `mongosh`.

*(Refer to the official MongoDB `mongosh` Methods documentation: https://www.mongodb.com/docs/mongodb-shell/reference/methods/)*