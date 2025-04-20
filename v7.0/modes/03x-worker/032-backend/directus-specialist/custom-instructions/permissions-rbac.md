# Directus: Permissions (Role-Based Access Control - RBAC)

Configuring user roles and permissions to control access to data and features in Directus.

## Core Concept: RBAC

Directus uses Role-Based Access Control (RBAC). Permissions are not assigned directly to users; instead:

1.  **Users** are assigned to **Roles**.
2.  **Permissions** are configured for **Roles**.

This makes managing access for many users much simpler. Directus comes with default roles (`Administrator`, `Public`), and you can create custom roles.

## Key Components

*   **Users:** Individuals who can log in to Directus (managed under Settings -> Users). Each user belongs to one Role.
*   **Roles:** Groups of users sharing the same set of permissions (managed under Settings -> Roles & Permissions).
*   **Permissions:** Rules defining what actions a Role can perform on specific Collections or Directus system resources.

## Configuring Permissions (via Admin UI)

Permissions are primarily managed through the Directus Admin App interface under **Settings -> Roles & Permissions**.

1.  **Select a Role:** Choose the role you want to configure (e.g., "Editor", "Author", or a custom role).
2.  **Collection Permissions:** For each collection (your data models):
    *   **CRUD Operations:** Define permissions for Create, Read, Update, Delete actions.
        *   **All Access:** Full CRUD allowed.
        *   **No Access:** No operations allowed.
        *   **Use Custom:** Define granular permissions.
    *   **Custom Permissions:**
        *   **Item Permissions:** Define rules based on the *item's data* (e.g., "User can only edit articles where `author` field equals their own user ID"). Uses a filter-like JSON structure.
        *   **Field Permissions:** Control read/write access for specific fields within the collection for this role. You can select which fields are visible (`Read Field Whitelist`) or editable (`Write Field Whitelist`).
        *   **Field Validation:** (Optional) Define validation rules that must pass for this role when creating/updating items (overrides collection-level validation if more restrictive).
3.  **System Permissions:** Configure access to Directus system collections and settings (e.g., access to Files, Users, Roles, Settings modules). Use with caution, especially for non-admin roles.
4.  **Admin Access:** Granting "Admin Access" to a role bypasses all configured permissions, giving full system access. Reserve this for administrators only.
5.  **App Access:** Granting "App Access" allows users in this role to log in to the Directus Admin App.

## Permission Details

*   **CRUD:**
    *   **Create:** Allows creating new items.
    *   **Read:** Allows fetching items (lists or single items).
    *   **Update:** Allows modifying existing items.
    *   **Delete:** Allows deleting items.
*   **Item Permissions (Filters):** Define conditions using the same filter syntax as the API (e.g., `{"status": {"_eq": "published"}, "author": {"_eq": "$CURRENT_USER"}}`). Dynamic variables like `$CURRENT_USER`, `$CURRENT_ROLE` can be used.
*   **Field Permissions (Whitelists):** Select the specific fields the role is allowed to see or modify. If left empty, defaults usually grant access based on the main CRUD permissions.

## Common Roles & Scenarios

*   **Public:** (Built-in) Represents unauthenticated users. Typically has read-only access to specific public collections (e.g., published blog posts, public products). Configure via Settings -> Roles & Permissions -> Public.
*   **Author/Editor:** Custom role. Might have create/read/update permissions for their *own* posts (`{"author": {"_eq": "$CURRENT_USER"}}`) and potentially read access to others'. Might have limited field write access (e.g., cannot change `published_date`).
*   **Manager:** Custom role. Might have full CRUD access to certain collections (e.g., manage all articles, approve submissions) but limited access to system settings.
*   **Administrator:** (Built-in) Full access via the "Admin Access" toggle.

## Best Practices

*   **Principle of Least Privilege:** Grant only the minimum permissions necessary for a role to perform its function.
*   **Start Restrictive:** Begin with "No Access" and explicitly grant permissions as needed.
*   **Test Thoroughly:** Log in as a user with the configured role and verify that permissions are enforced correctly via both the Admin App and API requests.
*   **Use Custom Roles:** Create specific roles for different user groups rather than over-granting permissions to default roles.
*   **Secure Admin Access:** Strictly limit who has the Administrator role.
*   **Review Regularly:** Periodically review role permissions to ensure they are still appropriate.

*(Refer to the official Directus documentation on Users, Roles, and Permissions: https://docs.directus.io/configuration/users-roles-permissions.html)*