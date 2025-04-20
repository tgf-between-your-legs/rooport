# Directus: Permissions & Role-Based Access Control (RBAC)

Configuring user roles and permissions to control access to data and features in Directus.

## Core Concept: Role-Based Access Control (RBAC)

Directus employs a powerful RBAC system to manage what users can see and do within the platform and via the API. The core idea is:

1.  **Users:** Individuals who log in to Directus (either the Data Studio or via API).
2.  **Roles:** Groups of users with a defined set of permissions (e.g., `Administrator`, `Editor`, `Contributor`, `Public`). Directus comes with default `Administrator` and `Public` roles.
3.  **Permissions:** Rules assigned to roles that grant or deny access (Create, Read, Update, Delete - CRUD) to specific **Collections** and **Fields**. Permissions can be fine-grained.

**Flow:** A user logs in -> Directus identifies their assigned Role -> When the user tries to access data or perform an action (via UI or API), Directus checks the permissions associated with their Role for the target collection/field -> Access is granted or denied.

## Key Components

*   **Roles:**
    *   Create custom roles in `Settings` -> `Roles & Permissions`.
    *   Assign users to roles. A user typically has one primary role.
    *   **Administrator Role:** Has unrestricted access by default (can be configured).
    *   **Public Role:** Defines access for unauthenticated users/API requests (the `$public` role internally). By default, it has no access. Crucial for public-facing APIs.
*   **Permissions Configuration:**
    *   Select a Role, then configure permissions for each **Collection**.
    *   **CRUD Operations:** Enable/disable Create, Read, Update, Delete actions.
    *   **Access Levels:**
        *   `All Access`: Full CRUD allowed.
        *   `No Access`: No CRUD allowed.
        *   `Use Custom`: Define granular permissions.
    *   **Custom Permissions (Granular Control):**
        *   **Item Permissions:** Define rules based on the item's field values (e.g., an `author` can only update *their own* articles). Uses a filter-like syntax (e.g., `{"author": {"_eq": "$CURRENT_USER"}}`). `$CURRENT_USER`, `$CURRENT_ROLE` are special variables.
        *   **Field Permissions:** Control read/write access for specific fields within a collection for that role.
        *   **Field Validation:** Define validation rules that must pass for Create/Update operations *for that specific role* (in addition to global field validation).
        *   **Field Presets:** Automatically set field values during item creation based on role (e.g., set `author` field to `$CURRENT_USER`).
*   **System Collections:** Permissions can also be set for system collections like `directus_users`, `directus_files`, `directus_roles`, etc., controlling who can manage users, files, and settings.

## Configuring Permissions (via Data Studio)

1.  Navigate to `Settings` -> `Roles & Permissions`.
2.  Select an existing role (e.g., `Public`) or click `Create Role`.
3.  For the selected role, permissions for all collections are listed.
4.  Click on a collection name (e.g., `articles`).
5.  Configure the main CRUD permissions using the icons (Create=Plus, Read=Eye, Update=Pencil, Delete=Trash). Click the shield icon to access custom/granular permissions.
6.  **Read Access:**
    *   Set Item Permissions filter (e.g., only allow reading items where `status` is `published`).
    *   Set Field Permissions (deselect fields the role shouldn't read).
7.  **Create/Update Access:**
    *   Set Item Permissions filter (usually less common for create/update, more for read/delete).
    *   Set Field Permissions (deselect fields the role shouldn't write to).
    *   Set Field Validation rules specific to this role.
    *   Set Field Presets (e.g., automatically set `user_created` to `$CURRENT_USER`).
8.  Save changes for the collection.
9.  Repeat for other collections and roles.

## Common Scenarios & Examples

*   **Public Read Access for Articles:**
    *   Select the `Public` role.
    *   Find the `articles` collection.
    *   Enable `Read` (Eye icon).
    *   Click the Shield icon next to Read.
    *   Under Item Permissions, set a filter like `{"status": {"_eq": "published"}}`.
    *   Under Field Permissions, deselect any sensitive fields not meant for public view.
    *   Save. Now unauthenticated API requests (`GET /items/articles`) will only return published articles with allowed fields.
*   **Editors Can Only Edit Their Own Drafts:**
    *   Select the `Editor` role.
    *   Find the `articles` collection.
    *   Enable `Update` (Pencil icon).
    *   Click the Shield icon next to Update.
    *   Under Item Permissions, set a filter like `{"author": {"_eq": "$CURRENT_USER"}, "status": {"_eq": "draft"}}`.
    *   Save. Now editors can only update articles where they are the author *and* the status is draft.
*   **Preventing Role Escalation:** Carefully configure permissions for `directus_users` and `directus_roles` to prevent non-admin users from changing their own or others' roles.

## API Access

*   Permissions apply automatically to both REST and GraphQL API requests.
*   Unauthenticated requests use the `Public` role's permissions.
*   Authenticated requests use the logged-in user's role permissions. Authentication tokens (Session, Static, JWT) are used to identify the user and their role.

Directus's RBAC system is highly flexible. Plan your roles and access needs carefully, starting with the principle of least privilege (deny access by default, then grant specific permissions). Test permissions thoroughly using different user roles via the UI and API.

*(Refer to the official Directus documentation on Users, Roles & Permissions.)*