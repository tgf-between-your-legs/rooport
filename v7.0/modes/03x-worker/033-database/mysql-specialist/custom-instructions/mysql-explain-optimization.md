# MySQL: Query Optimization with `EXPLAIN`

Analyzing MySQL query execution plans to identify performance bottlenecks.

## Core Concept

The `EXPLAIN` statement provides information about how MySQL executes SQL statements (primarily `SELECT`, but also `INSERT`, `UPDATE`, `DELETE`, `REPLACE`, `TABLE`). It shows the join order, which indexes are considered and used, estimations of rows examined, and potential issues like filesorts or temporary tables. Analyzing this output is crucial for optimizing slow queries.

## Using `EXPLAIN`

*   **Syntax:** Prepend `EXPLAIN` (or `DESCRIBE`/`DESC`) to your SQL statement.
    ```sql
    EXPLAIN SELECT customer_id, COUNT(*)
    FROM orders
    WHERE order_date >= '2024-01-01'
    GROUP BY customer_id;

    EXPLAIN UPDATE products SET price = price * 0.9 WHERE category_id = 10;
    ```
*   **Output Format:** `EXPLAIN` returns rows, each describing a table involved in the query execution plan. Key columns include:
    *   **`id`**: Select identifier (sequential number for each `SELECT` in the query).
    *   **`select_type`**: Type of `SELECT` (e.g., `SIMPLE`, `PRIMARY`, `SUBQUERY`, `DERIVED`, `UNION`).
    *   **`table`**: The table being accessed in this row of the plan.
    *   **`partitions`**: Partitions matched (if using partitioning).
    *   **`type`**: **Crucial.** The join type or access method. Aim for better types (closer to the top):
        *   `system`: Table has only one row (system table). Best.
        *   `const`: Table has at most one matching row (read once). Uses PRIMARY KEY or UNIQUE index with constant values. Very fast.
        *   `eq_ref`: One row read for each combination of rows from previous tables. Used for joins on PRIMARY KEY or UNIQUE NOT NULL columns. Fast.
        *   `ref`: Rows with matching index values read for each combination from previous tables. Used for joins on non-unique indexes or unique index prefixes. Good.
        *   `fulltext`: Join performed using a FULLTEXT index.
        *   `ref_or_null`: Like `ref`, but also searches for NULL values.
        *   `index_merge`: Indicates index merge optimization is used (multiple indexes combined). Performance varies.
        *   `unique_subquery`: `eq_ref` for certain `IN` subqueries.
        *   `index_subquery`: Like `unique_subquery` but for non-unique indexes in `IN` subqueries.
        *   `range`: Rows retrieved within a given range using an index. Better than `index` or `ALL`.
        *   `index`: Full scan of an index tree. Faster than `ALL` if the index covers the query, otherwise requires table lookups.
        *   `ALL`: **Full Table Scan.** Scans the entire table. **Avoid this on large tables.** Usually indicates a missing or unusable index for the query conditions.
    *   **`possible_keys`**: Indexes MySQL *could* potentially use for this table.
    *   **`key`**: The index MySQL *actually decided* to use. `NULL` indicates no index was used.
    *   **`key_len`**: Length of the index key part used. Shorter is generally better. Helps determine how much of a compound index is utilized.
    *   **`ref`**: Column(s) or constant compared to the index specified in `key`.
    *   **`rows`**: MySQL's *estimate* of the number of rows it needs to examine to execute this part of the query. Aim to minimize this.
    *   **`filtered`**: Estimated percentage of rows examined that will be filtered by the table condition (`WHERE` clause). A low value might indicate wasted effort.
    *   **`Extra`**: **Crucial.** Contains additional information about the execution plan. Important values:
        *   `Using index`: Query was satisfied entirely using index data (Covering Index). Excellent performance.
        *   `Using where`: MySQL applied `WHERE` clause filtering *after* retrieving rows (either from index or table scan). Common, but check if index could do more filtering.
        *   `Using index condition`: Index Pushdown. Storage engine filters using the index, reducing rows sent back to the server (Good).
        *   `Using filesort`: MySQL must perform an external sort because `ORDER BY` could not be satisfied by an index. **Bad for performance** on large datasets. Add an appropriate index covering the sort columns.
        *   `Using temporary`: MySQL needs to create an internal temporary table (often in memory, sometimes disk) to resolve the query, typically for `GROUP BY`, `DISTINCT`, or `UNION`. **Can be bad for performance.** Try adding indexes on `GROUP BY`/`ORDER BY` columns.
        *   `Impossible WHERE`: `WHERE` clause is always false.

## Optimization Workflow

1.  **Identify Slow Queries:** Use the slow query log, monitoring tools (like Percona Monitoring and Management - PMM), or application performance monitoring (APM).
2.  **Run `EXPLAIN`:** Execute `EXPLAIN` (or `EXPLAIN ANALYZE` in newer MySQL/MariaDB for actual execution stats) on the slow query.
3.  **Analyze Output:**
    *   Look for `ALL` (Full Table Scan) in the `type` column for large tables.
    *   Check if the `key` column is `NULL` or if an suboptimal index is chosen.
    *   Examine the `rows` estimate – is it excessively high?
    *   Pay close attention to the `Extra` column for `Using filesort` or `Using temporary`.
    *   Check `filtered` - low values might suggest index improvements.
4.  **Formulate Hypothesis:** Based on the analysis, guess the cause (e.g., missing index, poorly ordered compound index, non-SARGable query condition, inefficient join).
5.  **Apply Optimization:**
    *   **Add/Modify Indexes:** Create appropriate single-column or compound indexes based on `WHERE`, `JOIN`, `ORDER BY`, and `GROUP BY` clauses. Consider covering indexes.
    *   **Rewrite Query:** Modify the SQL query structure (e.g., change join order, rewrite subqueries as joins, simplify conditions, use appropriate functions). Ensure conditions are SARGable (Search Argument Able - can use an index). Avoid functions on indexed columns in the `WHERE` clause.
    *   **Schema Changes:** (More involved) Consider denormalization or other schema adjustments if query patterns fundamentally clash with the current structure.
6.  **Re-run `EXPLAIN`:** Verify that the optimizer uses the new index or follows the improved plan. Check if `rows`, `Extra` (`filesort`/`temporary`), and execution time (using `EXPLAIN ANALYZE` or profiling) have improved.
7.  **Test:** Test the query with realistic data volumes to confirm performance gains.

Optimization is often an iterative process of analyzing, changing, and measuring.

*(Refer to the official MySQL documentation on Optimizing Queries with EXPLAIN.)*