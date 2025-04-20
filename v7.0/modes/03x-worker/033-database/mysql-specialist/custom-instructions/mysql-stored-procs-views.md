# MySQL: Stored Procedures, Functions, & Views

Using stored routines and views for encapsulation and simplified access.

## Views

*   **Concept:** A virtual table based on the result set of a stored SQL query. Views do not store data themselves (unless materialized, which is less common in MySQL) but provide a named, reusable way to look at data from one or more underlying tables.
*   **Purpose:**
    *   Simplify complex queries.
    *   Restrict data access (show only certain columns or rows).
    *   Provide a stable interface even if underlying table structures change (to some extent).
    *   Present data in a specific format.
*   **Creating Views:**
    ```sql
    CREATE OR REPLACE VIEW view_name AS
    SELECT
        column1,
        column2,
        -- other columns or expressions
    FROM
        table_name
    WHERE
        condition;
    ```
*   **Using Views:** Query them like regular tables.
    ```sql
    SELECT * FROM view_name WHERE column1 = 'some_value';
    ```
*   **Updating via Views:** Simple views (often based on a single table without aggregation/distinct) can sometimes be updatable (`INSERT`, `UPDATE`, `DELETE`), but complex views are generally read-only. It's often safer and clearer to update the base tables directly.
*   **Dropping Views:**
    ```sql
    DROP VIEW IF EXISTS view_name;
    ```

**Example:**

```sql
-- Create a view showing active users with their basic profile info
CREATE OR REPLACE VIEW active_user_profiles AS
SELECT
    u.id AS user_id,
    u.username,
    u.email,
    p.full_name,
    p.bio
FROM
    users u
LEFT JOIN
    user_profiles p ON u.id = p.user_id
WHERE
    u.is_active = 1;

-- Query the view
SELECT user_id, username, full_name FROM active_user_profiles WHERE username LIKE 'a%';
```

## Stored Procedures

*   **Concept:** A set of pre-compiled SQL statements stored in the database that can be executed by name. They can accept input parameters (`IN`), return output parameters (`OUT`), and modify data (`INOUT`).
*   **Purpose:**
    *   Encapsulate complex business logic within the database.
    *   Reduce network traffic by executing multiple statements on the server.
    *   Provide a controlled interface for data modification.
    *   Improve performance (though the benefit over well-written application queries is debated).
*   **Creating Procedures:** Requires changing the delimiter temporarily as procedures contain semicolons.
    ```sql
    DELIMITER //

    CREATE PROCEDURE procedure_name (
        IN param1 INT,
        OUT output_param VARCHAR(255),
        INOUT inout_param DECIMAL(10, 2)
    )
    BEGIN
        -- Declare local variables
        DECLARE var1 INT DEFAULT 0;

        -- SQL statements, control flow (IF, CASE, LOOP, WHILE)
        SELECT COUNT(*) INTO var1 FROM some_table WHERE id > param1;

        IF var1 > 0 THEN
            SET output_param = 'Found records';
        ELSE
            SET output_param = 'No records found';
        END IF;

        SET inout_param = inout_param * 1.1;

        -- More complex logic...
        -- INSERT, UPDATE, DELETE statements allowed
    END //

    DELIMITER ; -- Reset delimiter
    ```
*   **Calling Procedures:**
    ```sql
    -- Set session variables for OUT/INOUT parameters
    SET @out_val = '';
    SET @inout_val = 100.00;

    CALL procedure_name(10, @out_val, @inout_val);

    -- Retrieve output values
    SELECT @out_val, @inout_val;
    ```
*   **Dropping Procedures:**
    ```sql
    DROP PROCEDURE IF EXISTS procedure_name;
    ```

## Stored Functions

*   **Concept:** Similar to stored procedures, but designed to return a single value. Can be used directly within SQL statements (like built-in functions).
*   **Purpose:** Encapsulate reusable calculations or data lookups.
*   **Restrictions:** Generally cannot modify data (unless declared `MODIFIES SQL DATA`, which is less common and requires specific privileges). Cannot return result sets directly (use procedures for that).
*   **Creating Functions:**
    ```sql
    DELIMITER //

    CREATE FUNCTION function_name (param1 INT, param2 VARCHAR(50))
    RETURNS VARCHAR(100) -- Specify return type
    DETERMINISTIC -- Or NOT DETERMINISTIC, READS SQL DATA, MODIFIES SQL DATA
    BEGIN
        DECLARE result_var VARCHAR(100);

        -- Logic to calculate result_var based on params
        SELECT CONCAT('Result: ', param2, ' - ', param1 * 10) INTO result_var;

        RETURN result_var;
    END //

    DELIMITER ;
    ```
*   **Using Functions:**
    ```sql
    SELECT id, function_name(id, name) AS calculated_value FROM my_table;

    UPDATE my_table SET description = function_name(id, 'Default') WHERE category = 5;
    ```
*   **Dropping Functions:**
    ```sql
    DROP FUNCTION IF EXISTS function_name;
    ```

## Considerations

*   **Maintainability:** Complex logic stored in procedures/functions can be harder to debug, version control, and test compared to application-level code.
*   **Portability:** Stored routines are specific to the database system (MySQL syntax differs from PostgreSQL, SQL Server, etc.).
*   **Performance:** While sometimes beneficial, complex stored routines can also become performance bottlenecks if not written carefully. Application-level logic often scales better horizontally.
*   **Use Cases:** Views are excellent for simplifying reads and providing stable interfaces. Procedures/Functions are best suited for encapsulating specific, reusable database-centric logic or complex multi-step operations that benefit from being executed entirely on the database server. Avoid putting core application business logic entirely into stored routines if possible.

Use these database objects judiciously to enhance organization, security, and sometimes performance.

*(Refer to the official MySQL documentation on Views, Stored Procedures, and Stored Functions.)*