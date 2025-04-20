# PostgreSQL: Common SQL Reference

Quick reference for common SQL commands and syntax in PostgreSQL (relevant for Neon).

*(Note: This is not exhaustive. PostgreSQL has a very rich SQL feature set. Refer to official PostgreSQL documentation for full details.)*

## Data Definition Language (DDL)

*   **Create Table:**
    ```sql
    CREATE TABLE table_name (
        column_name data_type [column_constraints],
        ...
        [table_constraints]
    );

    -- Example
    CREATE TABLE users (
        id SERIAL PRIMARY KEY, -- Auto-incrementing integer primary key
        -- id UUID PRIMARY KEY DEFAULT gen_random_uuid(), -- Alternative using UUID
        username VARCHAR(50) NOT NULL UNIQUE,
        email VARCHAR(100) NOT NULL UNIQUE,
        hashed_password TEXT NOT NULL,
        is_active BOOLEAN DEFAULT true,
        created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE posts (
        id BIGSERIAL PRIMARY KEY,
        user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE, -- Foreign key
        title VARCHAR(255) NOT NULL,
        body TEXT,
        published_at TIMESTAMPTZ,
        created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
        CONSTRAINT check_title_length CHECK (length(title) > 0) -- Example check constraint
    );
    ```
*   **Alter Table:**
    ```sql
    -- Add column
    ALTER TABLE table_name ADD COLUMN column_name data_type [constraints];
    -- Drop column
    ALTER TABLE table_name DROP COLUMN column_name [CASCADE | RESTRICT];
    -- Rename column
    ALTER TABLE table_name RENAME COLUMN old_name TO new_name;
    -- Change column type
    ALTER TABLE table_name ALTER COLUMN column_name TYPE new_data_type [USING expression];
    -- Add constraint
    ALTER TABLE table_name ADD CONSTRAINT constraint_name constraint_definition;
    -- Drop constraint
    ALTER TABLE table_name DROP CONSTRAINT constraint_name;
    -- Set default value
    ALTER TABLE table_name ALTER COLUMN column_name SET DEFAULT value;
    -- Drop default value
    ALTER TABLE table_name ALTER COLUMN column_name DROP DEFAULT;
    ```
*   **Drop Table:**
    ```sql
    DROP TABLE IF EXISTS table_name [CASCADE | RESTRICT];
    ```
*   **Create Index:**
    ```sql
    CREATE [UNIQUE] INDEX index_name ON table_name [USING method] (column1 [ASC|DESC], ...);
    -- Example: CREATE INDEX idx_posts_user_id ON posts (user_id);
    -- Example: CREATE INDEX idx_posts_published ON posts (published_at DESC NULLS LAST) WHERE is_published = true; (Partial Index)
    ```
*   **Drop Index:**
    ```sql
    DROP INDEX IF EXISTS index_name;
    ```
*   **Create View:** (See `mysql-stored-procs-views.md` for concept - syntax is similar)
    ```sql
    CREATE OR REPLACE VIEW view_name AS SELECT ...;
    ```
*   **Create Function / Procedure:** (See `mysql-stored-procs-views.md` for concept - syntax uses PL/pgSQL)
    ```sql
    CREATE OR REPLACE FUNCTION function_name(arg1 type, ...)
    RETURNS return_type AS $$
    DECLARE
        variable type;
    BEGIN
        -- PL/pgSQL logic
        RETURN value;
    END;
    $$ LANGUAGE plpgsql;
    ```
*   **Create Schema:** `CREATE SCHEMA IF NOT EXISTS schema_name;`
*   **Create Extension:** `CREATE EXTENSION IF NOT EXISTS extension_name;` (e.g., `vector`, `pgcrypto`, `uuid-ossp`)

## Data Manipulation Language (DML)

*   **`SELECT`:** (See `mysql-dml-reference.md` - syntax is largely standard SQL, with PostgreSQL-specific functions/operators)
    *   PostgreSQL supports `DISTINCT ON (column(s))` for selecting unique rows based on specific columns.
    *   Supports Window Functions and CTEs (including `RECURSIVE`).
    *   Rich set of JSON/JSONB operators and functions (`->`, `->>`, `@>`, `jsonb_agg`, etc.).
    *   Array operators and functions.
*   **`INSERT`:**
    ```sql
    INSERT INTO table_name (column1, column2) VALUES (value1, value2);
    INSERT INTO table_name (column1, column2) VALUES (val1a, val2a), (val1b, val2b);
    INSERT INTO table_name (column1, column2) SELECT col_a, col_b FROM other_table WHERE ...;

    -- Insert or Update (ON CONFLICT) - "Upsert"
    INSERT INTO table_name (id, column1, column2)
    VALUES (1, 'value1', 'value2')
    ON CONFLICT (id) -- Specify constraint or unique index columns
    DO UPDATE SET
        column1 = EXCLUDED.column1, -- Use EXCLUDED to refer to proposed insertion values
        column2 = 'new_value',
        updated_at = CURRENT_TIMESTAMP;

    -- Insert or Do Nothing
    INSERT INTO table_name (id, column1) VALUES (1, 'value1') ON CONFLICT DO NOTHING;

    -- Returning inserted data
    INSERT INTO table_name (column1) VALUES ('value1') RETURNING id, column1;
    ```
*   **`UPDATE`:**
    ```sql
    UPDATE table_name
    SET column1 = value1, column2 = value2, ...
    [FROM other_tables...] -- Optional: Join for updates
    WHERE condition;

    -- Returning updated data
    UPDATE table_name SET status = 'processed' WHERE id = 5 RETURNING id, status;
    ```
*   **`DELETE`:**
    ```sql
    DELETE FROM table_name
    WHERE condition;

    -- Returning deleted data
    DELETE FROM logs WHERE created_at < '2023-01-01' RETURNING *;
    ```
*   **`TRUNCATE TABLE table_name [RESTART IDENTITY] [CASCADE];`**: Faster delete of all rows.

## Data Control Language (DCL)

*   **`GRANT`:**
    ```sql
    GRANT { { SELECT | INSERT | UPDATE | DELETE | ... | ALL [ PRIVILEGES ] } }
    ON { [ TABLE ] table_name | ALL TABLES IN SCHEMA schema_name | ... }
    TO { role_specification | PUBLIC } [, ...] [ WITH GRANT OPTION ];

    -- Example: GRANT SELECT, INSERT ON users TO app_user;
    -- Example: GRANT app_read_role TO app_user; (Granting a role)
    ```
*   **`REVOKE`:**
    ```sql
    REVOKE [ GRANT OPTION FOR ]
        { { SELECT | INSERT | UPDATE | ... | ALL [ PRIVILEGES ] } }
    ON { [ TABLE ] table_name | ... }
    FROM { role_specification | PUBLIC } [, ...]
    [ CASCADE | RESTRICT ];

    -- Example: REVOKE DELETE ON users FROM app_user;
    -- Example: REVOKE app_write_role FROM app_user;
    ```
*   **User/Role Management:**
    ```sql
    CREATE ROLE role_name [ [ WITH ] option [ ... ] ]; -- Options: LOGIN, PASSWORD, CREATEDB, etc.
    ALTER ROLE role_name [ [ WITH ] option [ ... ] ];
    DROP ROLE role_name;

    -- CREATE USER is alias for CREATE ROLE ... LOGIN
    CREATE USER user_name WITH PASSWORD 'secret';
    ```

## Transaction Control Language (TCL)

*   **`BEGIN;`** or **`START TRANSACTION;`**: Start a transaction.
*   **`COMMIT;`**: Save changes made in the transaction.
*   **`ROLLBACK;`**: Discard changes made in the transaction.
*   **`SAVEPOINT savepoint_name;`**: Create a point within a transaction to potentially roll back to.
*   **`ROLLBACK TO SAVEPOINT savepoint_name;`**: Roll back to a savepoint.
*   **`RELEASE SAVEPOINT savepoint_name;`**: Destroy a savepoint.

This provides a basic reference. Always consult the specific PostgreSQL version documentation for detailed syntax and features.

*(Refer to the official PostgreSQL SQL Commands documentation: https://www.postgresql.org/docs/current/sql-commands.html)*