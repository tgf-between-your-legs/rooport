# MySQL: User Management & Security Basics

Basic commands for managing users and privileges in MySQL.

## Core Concept: Privileges

MySQL uses a privilege system to control what actions users can perform on which database objects.

*   **Users:** Defined by a username and the host from which they can connect (e.g., `'app_user'@'localhost'`, `'admin_user'@'192.168.1.%`, `'backup_user'@'%'`).
*   **Privileges:** Specific rights granted to users (e.g., `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `CREATE`, `ALTER`, `INDEX`, `FILE`, `PROCESS`, `RELOAD`, `SUPER`).
*   **Scope:** Privileges can be granted globally (`*.*`), per-database (`database_name.*`), per-table (`database_name.table_name`), or even per-column.
*   **`GRANT` Statement:** Used to give privileges to users.
*   **`REVOKE` Statement:** Used to remove privileges from users.
*   **Roles (MySQL 8.0+):** A named collection of privileges that can be granted to users, simplifying privilege management.

## Managing Users & Privileges (SQL Commands)

*(These commands typically require administrative privileges, like the `root` user or a user with the `CREATE USER` and `GRANT OPTION` privileges.)*

1.  **Create User:**
    ```sql
    -- Create user identified by password, allowing connection from localhost
    CREATE USER 'app_user'@'localhost' IDENTIFIED BY 'complex_password';

    -- Create user allowing connection from any host (less secure, use specific IPs/subnets if possible)
    CREATE USER 'remote_user'@'%' IDENTIFIED BY 'another_password';
    ```
2.  **Grant Privileges:**
    ```sql
    -- Grant basic CRUD privileges on all tables in 'app_database' to 'app_user' from localhost
    GRANT SELECT, INSERT, UPDATE, DELETE ON app_database.* TO 'app_user'@'localhost';

    -- Grant all privileges on 'app_database' (includes DDL like CREATE/ALTER TABLE)
    GRANT ALL PRIVILEGES ON app_database.* TO 'dev_user'@'localhost';

    -- Grant usage (connect only) globally
    GRANT USAGE ON *.* TO 'readonly_user'@'%';
    -- Grant SELECT privilege on a specific table
    GRANT SELECT ON app_database.products TO 'readonly_user'@'%';

    -- Grant privilege to execute a specific stored procedure
    GRANT EXECUTE ON PROCEDURE app_database.calculate_totals TO 'report_user'@'localhost';

    -- Grant privilege with GRANT OPTION (allows user to grant their privileges to others - use carefully)
    GRANT SELECT ON app_database.* TO 'team_lead'@'%' WITH GRANT OPTION;
    ```
3.  **Apply Privilege Changes:** After `GRANT` or `REVOKE`, reload privileges.
    ```sql
    FLUSH PRIVILEGES;
    ```
4.  **Show Grants:** View privileges for a user.
    ```sql
    SHOW GRANTS FOR 'app_user'@'localhost';
    ```
5.  **Revoke Privileges:**
    ```sql
    -- Revoke DELETE privilege on a specific table
    REVOKE DELETE ON app_database.orders FROM 'app_user'@'localhost';

    -- Revoke all privileges on a database
    REVOKE ALL PRIVILEGES ON app_database.* FROM 'dev_user'@'localhost';

    -- Revoke the grant option
    REVOKE GRANT OPTION ON app_database.* FROM 'team_lead'@'%';

    -- Remember to FLUSH PRIVILEGES after REVOKE
    FLUSH PRIVILEGES;
    ```
6.  **Rename User:**
    ```sql
    RENAME USER 'old_user'@'localhost' TO 'new_user'@'localhost';
    ```
7.  **Change Password:**
    ```sql
    -- For MySQL 5.7.6+ / 8.0+
    ALTER USER 'app_user'@'localhost' IDENTIFIED BY 'new_complex_password';

    -- Older MySQL versions might use SET PASSWORD
    -- SET PASSWORD FOR 'app_user'@'localhost' = PASSWORD('new_complex_password');
    ```
8.  **Drop User:**
    ```sql
    DROP USER 'remote_user'@'%';
    ```

## Roles (MySQL 8.0+)

1.  **Create Role:**
    ```sql
    CREATE ROLE 'app_read', 'app_write';
    ```
2.  **Grant Privileges to Role:**
    ```sql
    GRANT SELECT ON app_database.* TO 'app_read';
    GRANT INSERT, UPDATE, DELETE ON app_database.* TO 'app_write';
    ```
3.  **Grant Role to User:**
    ```sql
    GRANT 'app_read', 'app_write' TO 'app_user'@'localhost';
    ```
4.  **Set Default Role:** Specify which roles are active by default when a user connects.
    ```sql
    -- Make app_read and app_write active by default for app_user
    SET DEFAULT ROLE 'app_read', 'app_write' FOR 'app_user'@'localhost';
    -- Or set all granted roles as default
    SET DEFAULT ROLE ALL FOR 'app_user'@'localhost';
    ```
5.  **Activate Roles (Manual):** `SET ROLE 'role_name', ...;` or `SET ROLE ALL;` within a session.
6.  **Show Grants (Including Roles):** `SHOW GRANTS FOR 'app_user'@'localhost';` or `SHOW GRANTS FOR 'app_user'@'localhost' USING 'app_read';`
7.  **Drop Role:** `DROP ROLE 'role_name';`

## Security Best Practices

*   **Least Privilege:** Grant only the minimum necessary privileges to each user/role. Application users rarely need `ALL PRIVILEGES` or DDL rights (`CREATE`, `ALTER`, `DROP`).
*   **Specific Hosts:** Use specific hostnames or IP addresses (`localhost`, `192.168.1.100`, `appserver.domain.com`) instead of the wildcard `%` whenever possible to restrict connection sources.
*   **Strong Passwords:** Enforce strong password policies.
*   **No Root Access for Apps:** Never use the MySQL `root` user or other administrative accounts in application connection strings. Create dedicated application users.
*   **Regular Audits:** Periodically review users and their privileges.
*   **Secure Connection:** Use TLS/SSL to encrypt connections between the application and the database server.

Proper user management and privilege control are essential for database security. Roles (in MySQL 8.0+) simplify managing permissions for multiple users.

*(Refer to the official MySQL documentation on Access Control and Account Management.)*