# MongoDB: Security & Role-Based Access Control (RBAC)

Configuring user authentication and authorization in MongoDB.

## Core Concept: Authentication & Authorization

*   **Authentication:** Verifying the identity of a client connecting to the database. MongoDB supports several mechanisms (SCRAM-SHA, x.509 certificates, LDAP, Kerberos). SCRAM (Salted Challenge Response Authentication Mechanism) using username/password is the most common.
*   **Authorization (RBAC):** Determining what actions an authenticated user is permitted to perform on which resources. MongoDB uses Role-Based Access Control (RBAC).
    *   **Users:** Created within specific databases (often the `admin` database for administrative users or the application's database for application users). Users have credentials (e.g., password) and are assigned roles.
    *   **Roles:** A collection of privileges. Roles can be built-in or user-defined.
    *   **Privileges:** Define specific actions allowed on specific resources.
        *   **Action:** e.g., `find`, `insert`, `update`, `remove`, `createCollection`, `createIndex`, `listDatabases`.
        *   **Resource:** Specifies the database and/or collection the action applies to (e.g., `{ db: "appdb", collection: "orders" }`, `{ db: "appdb", collection: "" }` for all collections in `appdb`, `{ cluster: true }` for cluster-wide actions).

## Enabling Authentication

*   Authentication is **not** enabled by default on standalone instances often used for local development.
*   It **is** enabled by default on MongoDB Atlas (cloud service) and should **always** be enabled in production deployments.
*   **Enable Auth (Configuration File):** Add the `security.authorization: enabled` setting to your `mongod.conf` file and restart the `mongod` process.
    ```yaml
    # mongod.conf
    security:
      authorization: enabled
    # ... other settings (net, storage, systemLog)
    ```
*   **First User (Admin):** If enabling auth on an existing deployment without users, you must first connect locally (without auth, if possible via localhost exception) and create the first administrative user (typically in the `admin` database with roles like `userAdminAnyDatabase`, `dbAdminAnyDatabase`, `clusterAdmin`).

## Managing Users (`mongosh`)

*(Connect as a user with user management privileges, e.g., `userAdmin` or `userAdminAnyDatabase` role)*

*   **Create User:**
    ```javascript
    // Switch to the database where the user should be created (e.g., 'admin' or 'appdb')
    use admin // Or use appdb

    db.createUser({
      user: "myAppUser",
      pwd: passwordPrompt(), // Prompts securely for password
      roles: [
        { role: "readWrite", db: "appdb" }, // Read/write access to 'appdb'
        { role: "read", db: "reportingdb" } // Read-only access to 'reportingdb'
        // Add other built-in or custom roles
      ]
    })
    ```
*   **View Users:**
    ```javascript
    use <database> // Switch to the DB where user was created
    db.getUsers()
    // Or view all users across all DBs (requires privileges)
    use admin
    db.getUsers()
    ```
*   **Update User:**
    ```javascript
    use <database>
    // Grant additional role
    db.grantRolesToUser("myAppUser", [{ role: "read", db: "anotherdb" }])
    // Revoke role
    db.revokeRolesFromUser("myAppUser", [{ role: "read", db: "reportingdb" }])
    // Update custom data or password (use changeUserPassword for password)
    db.updateUser("myAppUser", { customData: { employeeId: 123 } })
    ```
*   **Change Password:**
    ```javascript
    use <database>
    db.changeUserPassword("myAppUser", passwordPrompt())
    ```
*   **Delete User:**
    ```javascript
    use <database>
    db.dropUser("myAppUser")
    ```

## Managing Roles (`mongosh`)

*(Requires role management privileges, e.g., `roleAdmin`)*

*   **Built-in Roles:** MongoDB provides many predefined roles (e.g., `read`, `readWrite`, `dbAdmin`, `userAdmin`, `clusterAdmin`, `backup`, `restore`). Use these where possible.
*   **Create Custom Role:**
    ```javascript
    use admin // Roles are typically defined in the admin database

    db.createRole({
      role: "inventoryManager",
      privileges: [
        { resource: { db: "appdb", collection: "products" }, actions: ["find", "update"] },
        { resource: { db: "appdb", collection: "inventory" }, actions: ["find", "insert", "update", "remove"] }
      ],
      roles: [
         // Inherit privileges from other roles (optional)
         { role: "read", db: "appdb" }
      ]
    })
    ```
*   **View Roles:**
    ```javascript
    use admin
    db.getRoles({ showBuiltinRoles: false, showPrivileges: true }) // Show custom roles with privileges
    ```
*   **Update Role:** `db.updateRole(...)`
*   **Drop Role:** `db.dropRole(...)`

## Best Practices

*   **Enable Authentication:** Always enable authentication in production.
*   **Least Privilege:** Assign users only the roles and privileges necessary for their tasks. Avoid overly broad roles like `dbAdminAnyDatabase` or `readWriteAnyDatabase` for application users.
*   **Strong Passwords:** Use strong, unique passwords for database users.
*   **Application Users:** Create dedicated users for your applications with specific roles granting access only to the necessary databases and collections. Don't use admin accounts in application connection strings.
*   **Network Security:** Configure firewalls to restrict access to your MongoDB ports (default 27017) only from trusted application servers. Use IP whitelisting (e.g., in MongoDB Atlas).
*   **TLS/SSL:** Encrypt data in transit by enabling TLS/SSL for connections between your application and MongoDB.
*   **Auditing:** Enable MongoDB auditing to track database activity if required for compliance or security monitoring.
*   **Regular Review:** Periodically review user accounts and roles to remove unused ones and ensure privileges are still appropriate.
*   **CSFLE:** For highly sensitive data, investigate Client-Side Field Level Encryption (requires MongoDB Enterprise or Atlas, more complex setup). Escalate to security specialists.

Proper authentication and authorization are fundamental to securing your MongoDB data.

*(Refer to the official MongoDB Security documentation: https://www.mongodb.com/docs/manual/security/)*