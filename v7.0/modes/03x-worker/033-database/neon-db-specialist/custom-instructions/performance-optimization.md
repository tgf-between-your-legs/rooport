# Neon: Performance Optimization (PostgreSQL)

Optimizing query performance for Neon serverless PostgreSQL databases.

## Core Concept: PostgreSQL Optimization

Since Neon is fully compatible with PostgreSQL, standard PostgreSQL query optimization techniques apply. The goal is to minimize resource usage (CPU, I/O, memory) and execution time, primarily by ensuring queries can efficiently locate and process the required data, often through effective indexing. Serverless adds extra considerations around connection management and potential cold starts.

## Key Optimization Areas

1.  **Indexing (Most Important):**
    *   **Identify Slow Queries:** Use `EXPLAIN (ANALYZE, BUFFERS)` on slow queries to understand the execution plan. Look for `Seq Scan` (Sequential Scan) on large tables, which indicates a missing or unusable index.
    *   **Create Appropriate Indexes:**
        *   Index columns used in `WHERE` clauses, `JOIN` conditions (`ON` clause), `ORDER BY`, and `GROUP BY`.
        *   Use **B-tree indexes** (default) for equality (`=`), range (`>`, `<`, `>=`, `<=`, `BETWEEN`), `IN`, `IS NULL`, and sorting.
        *   Use **Compound Indexes** for queries involving multiple columns. Order matters: place columns used in equality checks first, then sort columns, then range columns.
        *   Use **Partial Indexes** (`CREATE INDEX ... WHERE condition`) for queries that frequently target a specific subset of data.
        *   Use **Covering Indexes** (using `INCLUDE` clause or indexing all selected columns) to allow index-only scans (`Index Only Scan` in `EXPLAIN`), avoiding table heap access.
        *   Use **Hash Indexes** only for simple equality checks (`=`).
        *   Use **GiST/GIN Indexes** for specialized data types (Full-Text Search via `tsvector`, Geospatial via PostGIS, Array operations, `pgvector`).
    *   **Verify Index Usage:** Re-run `EXPLAIN (ANALYZE)` after creating an index to confirm it's being used (`Index Scan`, `Bitmap Index Scan`, `Index Only Scan`) and that the estimated/actual rows scanned have decreased.

2.  **Query Writing:**
    *   **Be Specific:** Select only the columns you need (`SELECT col1, col2`) instead of `SELECT *`.
    *   **Filter Early:** Apply `WHERE` clauses to filter data as early as possible.
    *   **Avoid Functions on Indexed Columns in `WHERE`:** Applying functions (e.g., `WHERE LOWER(email) = '...'` or `WHERE DATE(created_at) = '...'`) often prevents the database from using a standard index on that column. Rewrite queries or create functional indexes if necessary (`CREATE INDEX idx_lower_email ON users (LOWER(email));`).
    *   **Efficient Joins:** Ensure join conditions use indexed columns on both tables. Choose appropriate join types (`INNER JOIN`, `LEFT JOIN`). Avoid overly complex multi-way joins if possible; consider breaking down the query or denormalizing data.
    *   **Subqueries vs. Joins/CTEs:** Analyze whether rewriting correlated subqueries as `JOIN`s or using Common Table Expressions (`WITH`) improves performance (`EXPLAIN` is key).
    *   **`UNION` vs. `UNION ALL`:** Use `UNION ALL` if you don't need to remove duplicate rows, as it's faster than `UNION` (which performs a distinct sort).
    *   **Limit Results:** Use `LIMIT` when you only need a subset of results. Combine with `ORDER BY` on an indexed column for efficiency.

3.  **Aggregation (`GROUP BY`):**
    *   Ensure columns in the `GROUP BY` clause are indexed if performance is critical.
    *   Filter data using `WHERE` *before* grouping whenever possible. Use `HAVING` only for filtering based on aggregate results.

4.  **Connection Management (Serverless Specific):**
    *   **Pooling:** Use efficient connection pooling (see `connection-pooling-patterns.md`). Avoid opening a new connection for every request in high-concurrency environments. Use Neon-aware drivers (`@neondatabase/serverless`) or external poolers (PgBouncer).
    *   **Minimize Round Trips:** Combine multiple queries into a single transaction or stored procedure if appropriate to reduce network latency.

5.  **Schema Design:**
    *   Use appropriate data types (e.g., `INT` vs `BIGINT`, `VARCHAR(n)` vs `TEXT`).
    *   Apply normalization principles correctly, but consider denormalization strategically for read-heavy workloads if joins become a bottleneck (trade-off with write complexity/consistency).

6.  **PostgreSQL Configuration (Less relevant for Neon users):**
    *   In traditional PostgreSQL, tuning parameters like `shared_buffers`, `work_mem`, `effective_cache_size` is important. Neon manages most of these server-level configurations. Focus on query/index/schema optimization.

## Using `EXPLAIN ANALYZE`

*   **Syntax:** `EXPLAIN (ANALYZE, BUFFERS) SELECT ...;`
*   **Output:** Shows the planned *and* actual execution details:
    *   **`actual time`:** Time spent executing each node (first number = time to return first row, second number = time to return all rows for that node).
    *   **`rows`:** Actual number of rows returned by the node.
    *   **`loops`:** Number of times the node was executed.
    *   **`Buffers`:** Information about buffer cache hits (`shared hit`) vs. disk reads (`shared read`). High disk reads indicate data wasn't in cache, potentially impacting I/O performance.
*   **Interpretation:** Compare estimated `rows` from `EXPLAIN` with actual `rows` from `EXPLAIN ANALYZE`. Large discrepancies might indicate stale statistics (`ANALYZE table_name;` might help). Focus on nodes with high `actual time` and high `rows` examined compared to rows returned. Identify `Seq Scan`, `Sort` nodes that operate on many rows.

Optimization is key for both performance and cost in serverless environments like Neon. Regularly analyze slow queries using `EXPLAIN ANALYZE`.

*(Refer to official PostgreSQL documentation on `EXPLAIN`, Query Planning, and Performance Tuning, and Neon's performance guides.)*