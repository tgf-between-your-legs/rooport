# MySQL: Aggregation & Window Functions

Summarizing data using aggregate functions and performing calculations across sets of rows using window functions.

## Aggregate Functions with `GROUP BY`

*   **Purpose:** Perform calculations across a set of rows and return a single summary row for each group. Used with the `GROUP BY` clause.
*   **Common Functions:**
    *   `COUNT(expression | *)`: Counts rows or non-NULL values. `COUNT(*)` counts all rows in the group.
    *   `SUM(expression)`: Sum of values in the group.
    *   `AVG(expression)`: Average of values in the group.
    *   `MIN(expression)`: Minimum value in the group.
    *   `MAX(expression)`: Maximum value in the group.
    *   `GROUP_CONCAT(expression [ORDER BY ...] [SEPARATOR '...'])`: Concatenates non-NULL string values from the group.
*   **`GROUP BY` Clause:** Specifies the columns to group by. All columns in the `SELECT` list must either be in the `GROUP BY` clause or be used within an aggregate function.
*   **`HAVING` Clause:** Filters the results *after* grouping and aggregation (unlike `WHERE` which filters *before* grouping).

```sql
-- Count number of orders per customer
SELECT
    customer_id,
    COUNT(*) AS total_orders,
    SUM(order_total) AS total_spent,
    MAX(order_date) AS last_order_date
FROM orders
WHERE order_date >= '2023-01-01' -- Filter rows before grouping
GROUP BY customer_id
HAVING COUNT(*) >= 2 -- Filter groups after grouping (only customers with 2+ orders)
ORDER BY total_spent DESC;

-- List product categories and the products in each category
SELECT
    category_name,
    COUNT(product_id) AS num_products,
    GROUP_CONCAT(product_name ORDER BY product_name SEPARATOR ', ') AS product_list
FROM products p
JOIN categories c ON p.category_id = c.id
GROUP BY category_name;
```

## Window Functions

*   **Purpose:** Perform calculations across a set of table rows that are somehow related to the current row (the "window"). Unlike aggregate functions with `GROUP BY`, window functions do not collapse rows; they return a value for *each* row based on the window.
*   **Syntax:** `function_name() OVER ( [partition_clause] [order_clause] [frame_clause] )`
    *   **`function_name()`:** The window function (e.g., `ROW_NUMBER()`, `RANK()`, `SUM()`, `AVG()`, `LAG()`).
    *   **`OVER (...)`:** Specifies the window.
        *   **`PARTITION BY expression(s)` (Optional):** Divides rows into partitions (groups). The window function is applied independently to each partition. Similar to `GROUP BY` but doesn't collapse rows.
        *   **`ORDER BY expression(s) [ASC|DESC]` (Often Required):** Orders rows within each partition. Crucial for ranking and functions like `LAG`/`LEAD`.
        *   **`frame_clause` (Optional):** Defines the subset of rows within the partition relative to the current row (e.g., `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`). Defaults often suffice.

**Common Window Functions:**

*   **Ranking:**
    *   `ROW_NUMBER()`: Assigns a unique sequential integer to each row within its partition (e.g., 1, 2, 3, 4).
    *   `RANK()`: Assigns rank based on the `ORDER BY` clause. Gaps can occur for ties (e.g., 1, 2, 2, 4).
    *   `DENSE_RANK()`: Assigns rank without gaps for ties (e.g., 1, 2, 2, 3).
    *   `NTILE(N)`: Divides the partition into N groups (buckets) and assigns a bucket number.
*   **Value:**
    *   `LAG(expression, offset, default)`: Accesses data from a *previous* row in the partition based on `ORDER BY`.
    *   `LEAD(expression, offset, default)`: Accesses data from a *following* row in the partition.
    *   `FIRST_VALUE(expression)`: Gets the value from the first row in the window frame.
    *   `LAST_VALUE(expression)`: Gets the value from the last row in the window frame.
*   **Aggregate (as Window Functions):** `SUM()`, `AVG()`, `COUNT()`, `MIN()`, `MAX()` can be used as window functions with an `OVER` clause to perform running totals, moving averages, etc., without collapsing rows.

```sql
-- Assign row number within each department based on salary (highest first)
SELECT
    employee_name,
    department,
    salary,
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) as salary_rank_in_dept
FROM employees;

-- Calculate running total of sales per month
SELECT
    sale_month,
    monthly_sales,
    SUM(monthly_sales) OVER (ORDER BY sale_month ASC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as running_total_sales
FROM monthly_sales_summary;

-- Compare current month's sales to previous month's sales
SELECT
    sale_month,
    monthly_sales,
    LAG(monthly_sales, 1, 0) OVER (ORDER BY sale_month ASC) as previous_month_sales,
    monthly_sales - LAG(monthly_sales, 1, 0) OVER (ORDER BY sale_month ASC) as month_over_month_change
FROM monthly_sales_summary;

-- Calculate average salary for the department alongside each employee's salary
SELECT
    employee_name,
    department,
    salary,
    AVG(salary) OVER (PARTITION BY department) as avg_dept_salary
FROM employees;
```

## Common Table Expressions (CTEs)

*   **Purpose:** Define temporary, named result sets that you can reference within a single SQL statement (`SELECT`, `INSERT`, `UPDATE`, `DELETE`). Improves readability and organization of complex queries.
*   **Syntax:** `WITH cte_name AS ( SELECT ... ) SELECT ... FROM cte_name ...;`
*   **Recursive CTEs:** Allow performing hierarchical or graph traversal queries. `WITH RECURSIVE cte_name AS ( initial_query UNION ALL recursive_query ) SELECT ... FROM cte_name ...;`

```sql
-- Use CTE to find departments with average salary above overall average
WITH DeptAvgSalary AS (
    SELECT department, AVG(salary) as avg_salary
    FROM employees
    GROUP BY department
), OverallAvgSalary AS (
    SELECT AVG(salary) as overall_avg FROM employees
)
SELECT
    d.department,
    d.avg_salary
FROM DeptAvgSalary d
JOIN OverallAvgSalary o ON d.avg_salary > o.overall_avg;

-- Recursive CTE Example (Employee Hierarchy) - Simplified
WITH RECURSIVE EmployeeHierarchy (id, name, manager_id, level) AS (
  -- Anchor member: Select top-level managers (no manager_id)
  SELECT id, name, manager_id, 0 as level
  FROM employees
  WHERE manager_id IS NULL
  UNION ALL
  -- Recursive member: Select employees reporting to the previous level
  SELECT e.id, e.name, e.manager_id, eh.level + 1
  FROM employees e
  INNER JOIN EmployeeHierarchy eh ON e.manager_id = eh.id
)
SELECT * FROM EmployeeHierarchy ORDER BY level, name;
```

Aggregation, Window Functions, and CTEs are powerful tools for data analysis and complex query construction in MySQL.

*(Refer to the official MySQL documentation on Aggregate Functions, Window Functions, and WITH (Common Table Expressions).)*