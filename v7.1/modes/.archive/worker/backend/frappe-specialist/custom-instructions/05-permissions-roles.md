# Frappe Specialist: Permissions &amp; Roles

Configuring access control in Frappe using Roles, Role Permissions Manager, Permission Levels, and User Permissions is crucial for security and data integrity.

## 1. Core Concept: Role-Based Access Control (RBAC)

*   **Roles:** Define sets of permissions (e.g., "Sales Manager", "Accountant", "Employee"). Users are assigned one or more roles. Standard roles exist, and custom roles can be created.
*   **Permissions:** Granted to Roles, defining actions (Read, Write, Create, Delete, Submit, Cancel, Amend, Report, Import, Export, Print, Email, Share, Set User Permissions) allowed on specific DocTypes.
*   **Permission Levels (0-9):** Allow field-level access control *within* a DocType. Fields with `permlevel > 0` require the role to have explicit permission granted at that level (or higher) in Role Permission Manager. Level 0 is the default.
*   **User Permissions:** Restrict access to specific *documents* (records) based on links (e.g., User A can only see Projects linked to Department X).

## 2. Managing Permissions (UI)

*   **Role Permission Manager:**
    *   **Location:** Setup -> Permissions -> Role Permission Manager.
    *   **Function:** Main tool to set DocType-level permissions (Read, Write, Create, Delete, Submit, etc.) for specific Roles at specific Permission Levels (0-9).
    *   **Key Options:**
        *   Select DocType, Select Role.
        *   Check allowed actions.
        *   Set Permission Level (0 for base access, 1-9 for restricted field access).
        *   **Apply User Permissions:** If checked, User Permissions rules will be applied for this Role/DocType combination.
        *   **If Owner:** Check if permissions apply only if the user is the owner (`owner` field) of the document.
*   **DocType Configuration (Field Permissions):**
    *   **Location:** Customize -> DocType -> Select DocType -> Edit Fields section.
    *   **Function:** Set the "Perm Level" (0-9) for individual fields. Fields at level 1+ are hidden/read-only unless the user's role has permission granted at that level in Role Permission Manager.
*   **User Permissions (Record-Level Access):**
    *   **Location:** Setup -> Permissions -> User Permissions.
    *   **Function:** Restrict access to specific documents based on link field values matching user properties or specific allowed documents.
    *   **Example:** Allow User 'john@example.com' access to 'Sales Invoice' only where 'Territory' (Link field in Sales Invoice) is 'North'. Requires "Apply User Permissions" to be checked for John's role on the Sales Invoice DocType.

## 3. Key Permission Types (Actions)

*   **Read:** View documents (list/form).
*   **Write:** Modify existing documents.
*   **Create:** Create new documents.
*   **Delete:** Delete documents (moves to trash).
*   **Submit:** Submit submittable documents (DocStatus 1).
*   **Cancel:** Cancel submitted documents (DocStatus 2).
*   **Amend:** Create an amendment of a submitted document.
*   **Report:** Access reports related to the DocType.
*   **Import/Export:** Allow data import/export.
*   **Print/Email/Share:** Allow using these features.
*   **Set User Permissions:** Allow managing User Permissions for others (grant cautiously).

## 4. Server-Side Permission Checks

*   **Automatic:** Standard ORM methods like `frappe.get_doc`, `frappe.get_list` generally respect read permissions. Save/Submit operations respect write/submit permissions.
*   **Manual Check:** Use `frappe.has_permission(doctype, ptype='read', doc=None | docname)` in server scripts (especially `@frappe.whitelist()` methods) to explicitly check permissions before performing actions or returning data.
*   **Permission Query Conditions:** Define hooks (`permission_query_conditions`) to add mandatory filters to `frappe.get_list` queries based on the user, effectively implementing record-level security dynamically in Python.
    ```python
    # hooks.py
    permission_query_conditions = {
        "Project Task": "my_app.permissions.project_task_query_conditions",
    }

    # my_app/permissions.py
    import frappe
    def project_task_query_conditions(user):
        if not user: user = frappe.session.user
        if "System Manager" in frappe.get_roles(user):
            return None # No conditions for System Manager
        else:
            # Only show tasks assigned to the user
            return f"""(`tabProject Task`.`assigned_to` = {frappe.db.escape(user)})"""
    ```

## 5. Best Practices

*   **Least Privilege:** Grant only necessary permissions.
*   **Use Standard Roles:** Leverage built-in roles (System Manager, Sales User, HR User, etc.) first.
*   **Custom Roles:** Create specific custom roles for distinct job functions.
*   **Perm Levels:** Use levels 1-9 for sensitive fields (e.g., financial data, PII).
*   **User Permissions:** Apply for record-level access based on relationships (Company, Territory, Branch, Project, etc.).
*   **Test Thoroughly:** Log in as users with different roles to verify access controls. Check forms, lists, reports, and API access.
*   **Avoid Over-Reliance on "If Owner":** While useful, it can be limiting. User Permissions offer more flexible record-level control.
*   **Documentation:** Document custom roles and complex permission logic.
*   **Security Audits:** Periodically review permissions, especially for sensitive DocTypes. Consult `security-specialist` via lead if unsure.

Properly configured permissions are essential for maintaining data confidentiality, integrity, and enforcing business rules within Frappe.