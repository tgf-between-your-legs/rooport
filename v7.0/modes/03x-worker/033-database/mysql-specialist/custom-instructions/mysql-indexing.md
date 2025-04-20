# MySQL: Indexing Strategies

Creating and managing indexes to optimize query performance in MySQL.

## Core Concept

Indexes are special lookup tables that the database engine can use to speed up data retrieval operations. Without an index, MySQL must scan the entire table row by row (`Full Table Scan`) to find matching rows for a `WHERE` clause or to perform a `SORT`. Indexes allow the engine to quickly locate the relevant rows, significantly improving performance for `SELECT` queries, and also speeding up `UPDATE` and `DELETE` operations that use indexed `WHERE` clauses.

## Creating Indexes

*   **During `CREATE TABLE`:**
    ```sql
    CREATE TABLE users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        email VARCHAR(100) NOT NULL,
        status TINYINT DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        UNIQUE KEY idx_username (username), -- Unique index
        INDEX idx_status_created (status, created_at) -- Compound index
    );
    ```
*   **Using `ALTER TABLE`:**
    ```sql
    ALTER TABLE users
        ADD INDEX idx_email (email); -- Add a single-column index

    ALTER TABLE users
        ADD UNIQUE INDEX idx_user_preference (user_id, preference_key); -- Add a unique compound index
    ```
*   **Using `CREATE INDEX`:**
    ```sql
    CREATE INDEX idx_lastname ON users (last_name);

    CREATE UNIQUE INDEX idx_order_product ON order_items (order_id, product_id);
    ```

## Index Types in MySQL (Common)

*   **Primary Key:** Implicitly created, unique index on the primary key column(s). Usually clustered in InnoDB (table data is physically ordered by the primary key).
*   **Unique Index:** Enforces uniqueness for the indexed column(s). Duplicate values are rejected.
*   **Index (Non-Unique / Secondary Index):** Standard index allowing duplicate values. Speeds up lookups and sorting. In InnoDB, secondary indexes store the primary key value to locate the actual row data.
*   **Compound Index (Multi-column Index):** Index spanning multiple columns.
    *   **Order Matters:** The order of columns in the index definition is crucial. An index on `(colA, colB)` can efficiently support queries filtering on `colA` alone, or on `colA` AND `colB`. It generally does *not* efficiently support queries filtering only on `colB`.
    *   **Prefixes:** Supports queries using a left-most prefix of the index columns.
*   **Full-Text Index:** Used for `MATCH() ... AGAINST()` full-text search queries on `CHAR`, `VARCHAR`, or `TEXT` columns. Works differently from standard B-Tree indexes. Supported by InnoDB and MyISAM.
    ```sql
    ALTER TABLE articles ADD FULLTEXT INDEX idx_ft_title_content (title, content);
    -- Query: SELECT * FROM articles WHERE MATCH(title, content) AGAINST('database search' IN NATURAL LANGUAGE MODE);
    ```
*   **Spatial Index:** Used for querying geospatial data types (available with spatial extensions).

## Indexing Strategies & Best Practices

*   **Index Selectivity:** Indexes are most effective on columns with high selectivity (many unique values relative to the total number of rows). Indexing columns with very few distinct values (like boolean flags or gender) is often less effective unless part of a compound index.
*   **Index Columns in `WHERE`, `JOIN`, `ORDER BY`, `GROUP BY`:** Index the columns frequently used in these clauses.
*   **Compound Indexes:** Create compound indexes to cover queries filtering or sorting on multiple columns. Follow the "Equality, Sort, Range" principle where applicable (put equality columns first, then sort columns, then range columns).
*   **Covering Indexes:** If an index contains *all* the columns needed by a query (including those in the `SELECT` list and `WHERE` clause), MySQL can satisfy the query using *only* the index (`Using index` in `EXPLAIN`), avoiding access to the table data. This is very efficient.
*   **Index Prefixes (for Strings):** For long `VARCHAR` or `TEXT` columns, you can index only a prefix of the column to save space and potentially improve performance, but this limits the index's usability for sorting or exact matches beyond the prefix length.
    ```sql
    CREATE INDEX idx_url_prefix ON logs (url(100)); -- Index first 100 characters
    ```
*   **Foreign Keys:** InnoDB automatically creates indexes on foreign key columns if they don't already exist, which is important for join performance and enforcing referential integrity.
*   **Avoid Redundant Indexes:** An index on `(colA, colB)` makes a separate index solely on `colA` redundant for most query types. Review existing indexes before adding new ones.
*   **Write Performance Cost:** Indexes speed up reads but slow down writes (`INSERT`, `UPDATE`, `DELETE`) because the index must also be updated. Don't over-index.
*   **Analyze Queries (`EXPLAIN`):** Use `EXPLAIN SELECT ...` to see how MySQL executes a query and which indexes are considered or used.
    *   **`key` column:** Shows the index actually used. `NULL` often indicates a full table scan.
    *   **`possible_keys`:** Shows indexes MySQL *could* potentially use.
    *   **`rows`:** Estimated number of rows MySQL needs to examine. Aim to minimize this.
    *   **`Extra` column:** Provides additional info. Look for:
        *   `Using index`: Query was covered by the index (Good!).
        *   `Using where`: Filtering applied after fetching rows (Index might be used for lookup, but not all conditions).
        *   `Using index condition`: Index pushdown optimization (Good).
        *   `Using filesort`: MySQL had to do an external sort in memory or on disk because no index could satisfy the `ORDER BY` clause (Bad for performance on large sorts).
        *   `Using temporary`: MySQL had to create a temporary table, often for `GROUP BY` or `UNION` (Can be bad for performance).

Choose indexes strategically based on your application's specific query patterns and performance requirements. Regularly review index usage and query plans.

*(Refer to the official MySQL documentation on Optimization and Indexes, and Using EXPLAIN.)*