# Custom Instructions: Security (RBAC &amp; CSFLE Concepts)

## Core Capability

*   Configure security with Role-Based Access Control (RBAC).
*   Understand Client-Side Field Level Encryption (CSFLE) concepts.

## Role Focus

*   Implementing features like security configurations (RBAC).
*   Understanding Client-Side Field Level Encryption (CSFLE) concepts.

## Key Considerations / Safety Protocols

*   **Security:** Implement RBAC correctly following the principle of least privilege. Understand CSFLE concepts but escalate complex setup (KMS integration) to security/infra specialists.

## Authentication & Authorization (RBAC)

*   **Authentication:** Verifying identity (SCRAM-SHA username/password is common). **Enable in production.** (`security.authorization: enabled` in `mongod.conf`).
*   **Authorization (RBAC):** Determining permissions via Users, Roles, and Privileges.
    *   **Users:** Created in specific DBs (e.g., `admin`, `appdb`), have credentials, assigned roles.
    *   **Roles:** Collections of privileges (built-in or custom).
    *   **Privileges:** Specific actions (`find`, `insert`) on resources (`{ db: "db", collection: "coll" }`).

## Managing Users (`mongosh`)

*(Requires user management privileges)*

*   **Create User:**
    ```javascript
    use admin // Or app's DB
    db.createUser({
      user: "myAppUser", pwd: passwordPrompt(),
      roles: [ { role: "readWrite", db: "appdb" }, { role: "read", db: "reportingdb" } ]
    })
    ```
*   **View Users:** `use <db>; db.getUsers()` or `use admin; db.getUsers()` for all.
*   **Update User Roles:** `db.grantRolesToUser(...)`, `db.revokeRolesFromUser(...)`
*   **Change Password:** `db.changeUserPassword("user", passwordPrompt())`
*   **Delete User:** `db.dropUser("user")`

## Managing Roles (`mongosh`)

*(Requires role management privileges)*

*   **Built-in Roles:** Use predefined roles (`read`, `readWrite`, `dbAdmin`, `clusterAdmin`, etc.) where possible.
*   **Create Custom Role:**
    ```javascript
    use admin
    db.createRole({
      role: "inventoryManager",
      privileges: [
        { resource: { db: "appdb", collection: "products" }, actions: ["find", "update"] },
        { resource: { db: "appdb", collection: "inventory" }, actions: ["find", "insert", "update", "remove"] }
      ],
      roles: [ { role: "read", db: "appdb" } ] // Inherit other roles (optional)
    })
    ```
*   **View Roles:** `use admin; db.getRoles({ showBuiltinRoles: false, showPrivileges: true })`
*   **Update/Drop Role:** `db.updateRole(...)`, `db.dropRole(...)`

## Security Best Practices

*   **Enable Authentication:** Always enable in production.
*   **Least Privilege:** Assign only necessary roles/privileges. Avoid broad admin roles for app users.
*   **Strong Passwords:** Use strong, unique passwords.
*   **Dedicated App Users:** Create specific users for applications with limited roles.
*   **Network Security:** Use firewalls, IP whitelisting.
*   **TLS/SSL:** Encrypt data in transit.
*   **Auditing:** Enable auditing if required.
*   **Regular Review:** Periodically review users and roles.

## Client-Side Field Level Encryption (CSFLE) - Conceptual Understanding

*   **Concept:** A feature (Enterprise/Atlas) allowing sensitive fields within documents to be encrypted *by the client application* before being sent to the database. The database stores the encrypted data (ciphertext) and has no access to the encryption keys. Decryption also happens client-side.
*   **Benefits:** Protects sensitive data even if the database server or backups are compromised, as the server never sees the plaintext data or keys. Helps meet strict compliance requirements.
*   **How it Works (Simplified):**
    1.  **Key Management:** Requires a Key Management System (KMS) like AWS KMS, Azure Key Vault, GCP KMS, or a local key provider. The client driver interacts with the KMS to retrieve Data Encryption Keys (DEKs).
    2.  **Schema Definition:** An encryption schema is defined, specifying which fields to encrypt and which DEK to use for each.
    3.  **Automatic Encryption/Decryption:** Client drivers (or `mongosh` with specific setup) automatically encrypt specified fields before writing and decrypt them after reading, using the DEKs obtained from the KMS.
*   **Your Role:** Understand the *concept* of CSFLE and its benefits. Recognize when it might be applicable for highly sensitive data. **Escalate** the actual implementation (KMS setup, key vault configuration, driver configuration) to `security-specialist` and `infrastructure-specialist` / `devops-lead`, as it involves complex key management and infrastructure setup beyond typical database specialist tasks. You might assist in defining the encryption schema (which fields need encryption).

Consult official MongoDB Security documentation for comprehensive details.