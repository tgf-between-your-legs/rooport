# Neon: Secure Connections & PostgreSQL Roles

Configuring secure connections and managing user permissions for Neon PostgreSQL databases.

## Secure Connections (`sslmode`)

*   **Requirement:** Neon **requires** secure SSL/TLS connections. Attempting to connect without SSL will fail.
*   **Connection String Parameter:** You must include `sslmode=require` (or a stricter mode like `verify-ca` or `verify-full` if you configure certificate verification) in your PostgreSQL connection string or connection parameters.
*   **Neon Provided Strings:** Connection strings provided in the Neon Console typically already include `sslmode=require`.
*   **Example Connection String (URI format):**
    ```
    postgres://[user]:[password]@[endpoint_hostname]/[database]?sslmode=require
    ```
*   **Example using `psql`:**
    ```bash
    psql "postgres://[user]:[password]@[endpoint_hostname]/[database]?sslmode=require"
    ```
*   **Example using Python (`psycopg`):**
    ```python
    import psycopg

    # Option 1: Include in DSN string
    conn_str = "postgresql://user:pass@host/db?sslmode=require"
    with psycopg.connect(conn_str) as conn:
        # ... use connection ...

    # Option 2: Pass as separate parameter
    # with psycopg.connect(host="host", dbname="db", user="user", password="pass", sslmode="require") as conn:
    #    # ... use connection ...
    ```
*   **Stricter Modes (`verify-ca`, `verify-full`):** These modes provide protection against man-in-the-middle attacks by verifying the server's certificate against a trusted Certificate Authority (CA). This requires obtaining the CA certificate (Neon provides this) and configuring your client/driver to use it (`sslrootcert` parameter). `verify-full` also checks that the hostname matches the certificate's Common Name or Subject Alternative Name. While more secure, `require` is often sufficient if the primary concern is just encryption.

## User and Role Management (Standard PostgreSQL)

Neon uses standard PostgreSQL for managing users (roles) and permissions.

*   **Roles vs. Users:** In PostgreSQL, there isn't a strict distinction; `CREATE USER` is an alias for `CREATE ROLE ... LOGIN`. A role is essentially a collection of privileges, and a role that can log in is typically called a user.
*   **Creating Roles/Users:** (Requires administrative privileges)
    ```sql
    -- Create a role that can log in (a user) with a password
    CREATE ROLE app_user WITH LOGIN PASSWORD 'secure_password';

    -- Create a role intended for grouping privileges (cannot log in by default)
    CREATE ROLE read_only_group;
    ```
*   **Granting Privileges:** Give specific permissions on database objects to roles.
    ```sql
    -- Grant connect privilege on the database
    GRANT CONNECT ON DATABASE my_database TO app_user;
    GRANT CONNECT ON DATABASE my_database TO read_only_group;

    -- Grant usage privilege on a schema
    GRANT USAGE ON SCHEMA public TO app_user;
    GRANT USAGE ON SCHEMA public TO read_only_group;

    -- Grant specific DML privileges on a table
    GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE products TO app_user;
    GRANT SELECT ON TABLE products TO read_only_group;

    -- Grant privileges on all tables in a schema (future tables require ALTER DEFAULT PRIVILEGES)
    GRANT SELECT ON ALL TABLES IN SCHEMA public TO read_only_group;
    GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO app_user;

    -- Grant privileges on sequences (needed for SERIAL/BIGSERIAL defaults)
    GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO app_user;
    ```
*   **Granting Roles to Roles/Users:** Assign membership in a role to another role (user).
    ```sql
    -- Make app_user a member of the read_only_group
    GRANT read_only_group TO app_user;
    ```
*   **Default Privileges:** Grant privileges automatically for *future* objects created by a specific user or role within a schema.
    ```sql
    -- Ensure app_user can select from future tables created by the admin/migration role
    ALTER DEFAULT PRIVILEGES FOR ROLE migration_role IN SCHEMA public
       GRANT SELECT ON TABLES TO app_user;

    -- Ensure read_only_group can select from future tables
    ALTER DEFAULT PRIVILEGES IN SCHEMA public
       GRANT SELECT ON TABLES TO read_only_group;
    ```
*   **Revoking Privileges:** Remove permissions.
    ```sql
    REVOKE DELETE ON TABLE products FROM app_user;
    REVOKE read_only_group FROM app_user;
    ```
*   **Altering Roles:** Change role attributes (e.g., password).
    ```sql
    ALTER ROLE app_user WITH PASSWORD 'new_secure_password';
    ```
*   **Dropping Roles:**
    ```sql
    DROP ROLE app_user;
    ```
*   **Viewing Privileges:** Use `psql` meta-commands:
    *   `\du`: List roles (users).
    *   `\dp table_name`: Show privileges (ACLs) for a table.
    *   `\dn+ schema_name`: Show schema privileges.
    *   `\l`: List databases and connection privileges.

## Best Practices for Neon/PostgreSQL Security

*   **Mandatory SSL:** Always use `sslmode=require` or stricter.
*   **Least Privilege:** Create specific roles (users) for your application with the minimum required privileges. Avoid using the default `postgres` superuser for applications. Grant privileges on specific schemas and tables rather than globally or database-wide where possible.
*   **Schema Security:** Grant `USAGE` on schemas explicitly. Don't grant `CREATE` on schemas to application users unless necessary.
*   **Strong Passwords:** Use strong, unique passwords.
*   **Connection Pooling:** Ensure your connection pooler (if used) handles credentials securely.
*   **Network Restrictions:** Use Neon's IP Allow list feature to restrict connections to known application IP addresses.
*   **Regular Review:** Periodically review roles and privileges.

By combining mandatory SSL encryption with standard PostgreSQL role-based access control, you can effectively secure your Neon database.

*(Refer to Neon documentation on Connecting Securely and PostgreSQL documentation on Roles and Privileges.)*