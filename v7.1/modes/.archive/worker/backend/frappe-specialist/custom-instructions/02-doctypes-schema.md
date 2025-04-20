# Frappe Specialist: DocTypes &amp; Schema

DocTypes are the fundamental building blocks in Frappe, defining the data models (schema), views (forms, lists), and associated logic for entities within the system (e.g., Customer, Sales Order, Project Task).

## 1. DocType Definition

*   **Location:** Defined primarily via JSON files within a custom app's module structure: `[app_name]/[module_name]/doctype/[doctype_name]/[doctype_name].json`.
*   **UI Editor:** Can also be created and modified via the Desk UI (Setup -> Customize -> DocType), which updates the underlying JSON file. Using the UI is often convenient for initial creation and simple modifications. For complex changes or version control, editing the JSON directly is preferred.
*   **Core Components:**
    *   **Fields:** Define the data fields (columns in the database table). Each field has a `fieldname`, `label`, `fieldtype`, and various options (e.g., `reqd`, `unique`, `read_only`, `options`, `default`, `description`, `depends_on`, `mandatory_depends_on`).
    *   **Permissions:** Define default role-based permissions (Read, Write, Create, Delete, etc.). These are often further refined using the Role Permission Manager.
    *   **Naming:** How documents of this type are named (e.g., by `field:`, `naming_series:`, `prompt`, `format:`, `expression:`).
    *   **Settings:** Various flags controlling behavior (e.g., `is_submittable`, `is_tree`, `track_changes`, `track_seen`).
    *   **Controller:** Associated Python class (`[doctype_name].py`) for server-side logic.

## 2. Key Field Types

*   **Data:** Plain text (max 140 chars).
*   **Small Text:** Plain text (multi-line, no formatting).
*   **Text Editor:** Rich text (HTML).
*   **Int:** Integer numbers.
*   **Float:** Floating-point numbers.
*   **Currency:** Floating-point numbers formatted as currency.
*   **Percent:** Floating-point numbers formatted as percentage.
*   **Select:** Dropdown list (options defined in the `options` property, separated by newlines).
*   **Link:** Link to another DocType (creates a foreign key relationship). `options` property specifies the target DocType. Use `frm.set_query` in client scripts for dynamic filtering.
*   **Dynamic Link:** Link to a DocType specified by another field in the same document.
*   **Table (Child Table):** Link to another DocType that acts as a child table (one-to-many relationship). `options` property specifies the child DocType. Child DocTypes should typically have `istable: 1` set.
*   **Date:** Date value.
*   **Datetime:** Date and Time value.
*   **Time:** Time value.
*   **Check:** Checkbox (stores 1 or 0).
*   **Attach Image / Attach File:** File upload fields.
*   **Read Only:** Display-only field.
*   **HTML:** Render custom HTML.
*   **Section Break / Column Break:** Control form layout.

## 3. DocType Structure &amp; Files

A DocType typically consists of several files within its directory:

*   `[doctype_name].json`: The core definition (fields, permissions, settings). **This is the primary file defining the schema.**
*   `[doctype_name].py`: The server-side Python controller class (inherits `frappe.model.document.Document`). Contains custom methods and can override standard event methods (`validate`, `on_update`, etc., though using `hooks.py` is often preferred for events).
*   `[doctype_name]_list.js`: (Optional) Client-side JavaScript for customizing the List View (`frappe.listview_settings`). Linked via `hooks.py`.
*   `[doctype_name].js`: (Optional) Client-side JavaScript for customizing the Form View (`frappe.ui.form.on`). Linked via `hooks.py`.
*   `test_[doctype_name].py`: (Optional) Python unit tests for the DocType and its controller logic. Run via `bench run-tests`.

## 4. Schema Migrations

*   **Trigger:** Any change to a DocType's `*.json` file (adding/removing fields, changing field types, modifying options like `unique`) requires a schema migration.
*   **Command:** Run `bench migrate` (or `bench --site [site_name] migrate`).
*   **Process:** Frappe compares the JSON definition with the database table schema and applies necessary `ALTER TABLE` statements (add/drop columns, change types, add/drop indexes).
*   **Caution:** Be careful with destructive changes (removing fields, changing field types) as they can lead to data loss if not handled properly. Back up before migrating.
*   **Data Migrations:** If data needs to be transformed *during* a schema change (e.g., splitting a field into two, populating a new mandatory field), use Patch scripts defined in `patches.txt` within your app.

## 5. Best Practices

*   **Naming Conventions:** Use clear, descriptive names for DocTypes and fields (snake_case recommended for fieldnames).
*   **Modularity:** Group related DocTypes into modules within your app.
*   **Standard Fields:** Leverage standard fields (`owner`, `creation`, `modified`, `docstatus`, `_user_tags`, etc.) where appropriate.
*   **Relationships:** Use Link and Table fields correctly to model relationships. Avoid storing redundant data.
*   **Indexing:** Frappe automatically indexes certain fields (`name`, Link fields). Add custom indexes via the DocType definition (`"idx": 1` on a field) if needed for performance on frequently queried fields, but consult `database-lead` for complex indexing strategies.
*   **Validation:** Implement validation logic in `validate` methods (controller or hook) or using field properties (`reqd`, `unique`).
*   **Permissions:** Define appropriate default permissions in the JSON, but refine using Role Permission Manager and Permission Levels.
*   **Version Control:** Keep DocType JSON files under Git version control.
*   **Avoid Direct DB Changes:** Do not modify Frappe database tables directly. Always use `bench migrate` after changing DocType JSON definitions.

Understanding DocTypes is fundamental to developing within the Frappe framework. They define the structure upon which the entire application logic is built.