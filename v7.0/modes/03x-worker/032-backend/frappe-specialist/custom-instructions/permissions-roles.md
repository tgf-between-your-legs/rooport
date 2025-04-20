# Frappe: Permissions & Roles

Configuring access control in Frappe using Roles and Permissions.

## Core Concept: Role-Based Access Control (RBAC)

Frappe uses a comprehensive Role-Based Access Control system to manage user permissions.

*   **Roles:** Define sets of permissions (e.g., "Sales Manager", "Accountant", "Employee"). Users are assigned one or more roles.
*   **Permissions:** Granted to Roles, defining what actions (Read, Write, Create, Delete, Submit, Cancel, Amend, etc.) they can perform on specific DocTypes.
*   **Permission Levels:** Allow defining different field-level access *within* a single DocType based on roles (e.g., only HR Manager can see salary field, but Employee can see other fields).
*   **User Permissions:** Allow restricting access to specific *documents* (records) based on links to other documents (e.g., User can only see Projects linked to their Department).

## Managing Roles & Permissions (UI)

Permissions are primarily managed via the Frappe Desk UI:

1.  **Role Permission Manager (Core Tool):**
    *   **Location:** Setup -> Permissions -> Role Permission Manager.
    *   **Function:** The main interface for setting CRUD permissions for a specific Role on a specific DocType.
    *   **Steps:**
        1.  Select the DocType.
        2.  Select the Role.
        3.  Check the boxes for allowed actions (Read, Write, Create, Delete, Submit, Cancel, Amend, Report, Import, Export, Print, Email, Share, Set User Permissions).
        4.  **Permission Level (Perm Level):** Set to 0 for basic access. Use higher levels (1-9) to enable field-level restrictions (see below).
        5.  **Apply User Permissions:** Check if User Permissions should apply for this role/doctype combination.
        6.  Click "Add" or "Update".
2.  **DocType Configuration (Field Permissions):**
    *   **Location:** Setup -> Customize -> DocType -> Select DocType -> Edit Fields section.
    *   **Function:** Set the "Perm Level" (0-9) for individual fields. Fields with Perm Level > 0 are only accessible if the user's role has permission defined for that level (or higher) in the Role Permission Manager.
    *   **Example:** Set `salary` field to Perm Level 1. In Role Permission Manager, give "HR Manager" role Read/Write access at Perm Level 1 for the Employee DocType, while giving "Employee" role only Read access at Perm Level 0. The Employee role won't see/edit the salary field.
3.  **User Permissions (Record-Level Access):**
    *   **Location:** Setup -> Permissions -> User Permissions.
    *   **Function:** Restrict access to specific documents based on link fields.
    *   **Steps:**
        1.  Select the User.
        2.  Select the DocType to restrict (e.g., "Project").
        3.  Select the specific Document/Record the user *is allowed* to access (e.g., "Project Alpha").
        4.  Optionally, set applicability (e.g., "Is Default").
    *   **Alternative (Based on Link):** Instead of selecting a specific document, you can restrict based on a linked field value matching a user property.
        1.  Select User, Select DocType (e.g., "Sales Invoice").
        2.  Check "Apply To All DocTypes".
        3.  Click "Add A Permission".
        4.  Select the Link Field DocType (e.g., "Territory").
        5.  Select the specific allowed value (e.g., "North Zone").
        *   **Effect:** The user can only access Sales Invoices where the `territory` field is "North Zone". This requires the "Apply User Permissions" checkbox to be ticked for the relevant role/doctype in Role Permission Manager.

## Key Permission Types

*   **Read:** View documents (list view, form view).
*   **Write:** Modify existing documents.
*   **Create:** Create new documents.
*   **Delete:** Delete documents (moves to trash, can be restored unless permanently deleted).
*   **Submit:** Submit documents that follow a workflow (e.g., Sales Order, Invoice). Submitted documents are often immutable.
*   **Cancel:** Cancel submitted documents.
*   **Amend:** Create an amendment (new version) of a submitted document.
*   **Report:** Access reports related to the DocType.
*   **Import/Export:** Allow data import/export for the DocType.
*   **Print/Email/Share:** Allow using print, email, and share features for the DocType.
*   **Set User Permissions:** Allow users of this role to manage User Permissions for others (use with caution).

## Best Practices

*   **Standard Roles:** Leverage standard roles provided by Frappe/ERPNext where possible.
*   **Custom Roles:** Create custom roles for specific job functions rather than modifying standard roles excessively.
*   **Least Privilege:** Grant only the minimum permissions required for each role.
*   **Perm Levels:** Use Permission Levels (0-9) for fine-grained field access control within a DocType. Start with level 0 and add restrictions at higher levels.
*   **User Permissions:** Use User Permissions for record-level restrictions based on ownership or links (Territory, Department, Company, etc.). Ensure "Apply User Permissions" is checked appropriately.
*   **Test Thoroughly:** Log in as users with different roles to verify permissions are working as expected. Check list views, form views, reports, and API access.
*   **Documentation:** Document custom roles and complex permission setups.

Effective permission management is crucial for data security and workflow integrity in Frappe applications.

*(Refer to the official Frappe Permissions documentation: https://frappeframework.com/docs/user/en/basics/permissions)*