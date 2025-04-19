# Custom Instructions: Basic Administration

## Core Capability

*   Conduct basic database administration including backup (`mongodump`), restore (`mongorestore`), and monitoring (`$currentOp`).

## Role Focus

*   Managing database operations.

## Key Considerations / Safety Protocols

*   **Backups:** Understand the backup strategy (`mongodump`, Atlas backups) but rely on `devops-lead`/`infrastructure-specialist` for execution and management unless specifically tasked with basic operations.

## Common Administrative Commands (`mongosh`)

*   **Connecting:**
    *   `mongosh "mongodb://user:pass@host:port/db?options"`
    *   `mongosh --host ... --port ... -u ... -p ... --authenticationDatabase ...`
*   **Basic Shell:**
    *   `help`, `show dbs`, `use <db>`, `show collections`, `db`, `db.stats()`, `db.collection.stats()`, `cls`, `exit`
*   **Index Management:**
    *   `db.collection.createIndex(...)`
    *   `db.collection.getIndexes()`
    *   `db.collection.dropIndex(...)`
    *   `db.collection.dropIndexes()`
    *   `db.collection.reIndex()` (Resource-intensive)
*   **Diagnostics & Monitoring:**
    *   `db.collection.find(...).explain("executionStats")` (See `06-performance-tuning.md`)
    *   `db.currentOp()`: Show in-progress operations.
    *   `db.serverStatus()`: Detailed server state overview.
    *   `db.setProfilingLevel(level, options)`: Enable profiling (0=off, 1=slow, 2=all). Use cautiously. Check `system.profile`.
    *   `rs.status()`: Replica set status.
    *   `rs.conf()`: Replica set configuration.
    *   `sh.status()`: Sharded cluster status.
*   **User & Role Management:** (See `07-security.md`)
    *   `db.createUser(...)`, `db.updateUser(...)`, `db.dropUser(...)`, `db.changeUserPassword(...)`
    *   `db.createRole(...)`, `db.updateRole(...)`, `db.dropRole(...)`
    *   `db.grantRolesToUser(...)`, `db.revokeRolesFromUser(...)`
    *   `db.getUsers()`, `db.getRoles(...)`

## Backup & Restore (OS Shell Commands)

*   **`mongodump`**: Creates a BSON dump.
    *   `mongodump --uri="mongodb://..." --out=/path/to/backup/dir`
    *   Options: `--db <db>`, `--collection <coll>`, `--gzip`
*   **`mongorestore`**: Restores a dump.
    *   `mongorestore --uri="mongodb://..." /path/to/backup/dir`
    *   Options: `--db <db>`, `--collection <coll>`, `--drop` (drop collections before restore), `--gzip`

**Important:** While you should understand these commands, the execution and management of backup/restore procedures in production environments are typically handled by `devops-lead` or `infrastructure-specialist`. Confirm responsibility before executing potentially disruptive commands like `mongorestore --drop`.

Refer to official MongoDB `mongosh` Methods and Database Tools documentation.