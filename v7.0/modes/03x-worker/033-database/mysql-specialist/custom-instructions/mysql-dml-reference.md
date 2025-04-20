# MySQL: DML Reference (SELECT, INSERT, UPDATE, DELETE)

Quick reference for common Data Manipulation Language (DML) statements in MySQL.

## `SELECT` Statement

Retrieves data from one or more tables.

```sql
SELECT
    [DISTINCT] -- Return only unique rows
    select_list -- Columns or expressions to retrieve (* for all columns)
FROM
    table_reference -- Table(s) to query from
[WHERE
    search_condition] -- Filter rows based on conditions
[GROUP BY
    group_by_expression] -- Group rows with the same values in specified columns
[HAVING
    search_condition] -- Filter groups based on conditions (after GROUP BY)
[ORDER BY
    order_by_expression [ASC | DESC]] -- Sort the result set
[LIMIT
    {[offset,] row_count | row_count OFFSET offset}] -- Limit the number of rows returned
;
```

**Key Clauses:**

*   **`SELECT list`**:
    *   `*`: All columns.
    *   `column1, column2`: Specific columns.
    *   `table_alias.column`: Specify table when joining.
    *   `COUNT(*), SUM(col), AVG(col), MAX(col), MIN(col)`: Aggregate functions (used with `GROUP BY`).
    *   `CASE WHEN condition THEN result ELSE default END`: Conditional expressions.
    *   `CONCAT(str1, str2), SUBSTRING(...), DATE_FORMAT(...)`: Various built-in functions.
*   **`FROM table_reference`**:
    *   `table_name`
    *   `table_name AS alias` or `table_name alias`
    *   `table1 JOIN table2 ON join_condition` (See Joins section).
*   **`WHERE search_condition`**:
    *   Operators: `=`, `!=` or `<>`, `>`, `<`, `>=`, `<=`, `LIKE`, `NOT LIKE`, `IN (...)`, `NOT IN (...)`, `BETWEEN ... AND ...`, `IS NULL`, `IS NOT NULL`.
    *   Logical Operators: `AND`, `OR`, `NOT`.
    *   Parentheses `()` for grouping conditions.
*   **`GROUP BY column(s)`**: Groups rows based on common values in specified columns, used with aggregate functions.
*   **`HAVING condition`**: Filters results *after* grouping (unlike `WHERE` which filters before grouping). Often uses aggregate functions.
*   **`ORDER BY column(s) [ASC|DESC]`**: Sorts results. `ASC` (ascending) is default.
*   **`LIMIT count` / `LIMIT offset, count`**: Restricts the number of rows returned.

**Joins:**

*   **`INNER JOIN`**: Returns rows only when there is a match in both tables based on the `ON` condition.
    ```sql
    SELECT u.name, o.order_date
    FROM users u
    INNER JOIN orders o ON u.id = o.user_id;
    ```
*   **`LEFT JOIN` (or `LEFT OUTER JOIN`)**: Returns all rows from the *left* table (users) and matching rows from the *right* table (orders). If no match, NULLs are returned for right table columns.
    ```sql
    SELECT u.name, o.order_date
    FROM users u
    LEFT JOIN orders o ON u.id = o.user_id;
    ```
*   **`RIGHT JOIN` (or `RIGHT OUTER JOIN`)**: Returns all rows from the *right* table and matching rows from the *left* table.
*   **`FULL OUTER JOIN`**: (Not directly supported in MySQL, emulate with `LEFT JOIN UNION RIGHT JOIN`). Returns all rows when there is a match in either table.
*   **`CROSS JOIN`**: Cartesian product (all possible combinations of rows). Use with caution.

**Subqueries:** Queries nested inside another query (in `SELECT`, `FROM`, `WHERE`, `HAVING`).

## `INSERT` Statement

Adds new rows to a table.

```sql
-- Insert a single row, specifying columns
INSERT INTO table_name (column1, column2, column3)
VALUES (value1, value2, value3);

-- Insert a single row, assuming values match column order (less safe)
INSERT INTO table_name
VALUES (value1, value2, value3, ...);

-- Insert multiple rows
INSERT INTO table_name (column1, column2, column3)
VALUES
    (value1a, value2a, value3a),
    (value1b, value2b, value3b),
    (value1c, value2c, value3c);

-- Insert data from another table
INSERT INTO table_name (column1, column2)
SELECT column_a, column_b
FROM another_table
WHERE condition;

-- Insert or Update (ON DUPLICATE KEY UPDATE)
INSERT INTO table_name (id, column1, column2)
VALUES (1, 'value1', 'value2')
ON DUPLICATE KEY UPDATE
    column1 = VALUES(column1), -- Use VALUES() to refer to the inserted value
    column2 = 'new_value';
```

## `UPDATE` Statement

Modifies existing rows in a table.

```sql
UPDATE table_name
SET
    column1 = value1,
    column2 = value2,
    ...
[WHERE
    search_condition] -- IMPORTANT: Filters which rows to update. Without WHERE, ALL rows are updated!
[ORDER BY ...] -- Less common, used with LIMIT
[LIMIT row_count]; -- Limit the number of rows updated
```

**Example:**

```sql
UPDATE products
SET price = price * 1.1, updated_at = NOW()
WHERE category_id = 5 AND stock > 0;
```

## `DELETE` Statement

Removes existing rows from a table.

```sql
DELETE FROM table_name
[WHERE
    search_condition] -- IMPORTANT: Filters which rows to delete. Without WHERE, ALL rows are deleted!
[ORDER BY ...] -- Less common, used with LIMIT
[LIMIT row_count]; -- Limit the number of rows deleted
```

**Example:**

```sql
DELETE FROM logs
WHERE created_at < DATE_SUB(NOW(), INTERVAL 90 DAY);
```

**`TRUNCATE TABLE table_name;`**: Faster way to delete *all* rows from a table (resets auto-increment counters, cannot be easily rolled back). Use with extreme caution.

Always use `WHERE` clauses carefully with `UPDATE` and `DELETE` statements, especially in production environments. Test DML statements thoroughly.

*(Refer to the official MySQL DML documentation: SELECT, INSERT, UPDATE, DELETE)*