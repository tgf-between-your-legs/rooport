# Frappe Specialist: Server Scripts, Hooks &amp; API

This section covers writing server-side Python code using DocType controllers, hooks, and the Frappe server-side API.

## 1. Locations for Server Scripts

*   **DocType Controllers (`<doctype_name>.py`):**
    *   **Location:** `[app_name]/[module_name]/doctype/[doctype_name]/[doctype_name].py`.
    *   **Purpose:** Define methods specific to a DocType instance (`self`). Contains the DocType's Python class inheriting from `frappe.model.document.Document`. Methods here can be called by hooks or other scripts. Standard event methods (`validate`, `on_update`, etc.) can be defined here, but using `hooks.py` is often cleaner for managing events.
    *   **Example:**
        ```python
        # my_app/my_module/doctype/project_task/project_task.py
        import frappe
        from frappe.model.document import Document

        class ProjectTask(Document):
            def validate(self):
                if self.start_date and self.end_date and self.start_date > self.end_date:
                    frappe.throw("End Date cannot be before Start Date")

            def update_project_status(self):
                # Custom logic related to this task instance
                pass
        ```

*   **Hooks (`hooks.py`):**
    *   **Location:** App's root directory (`[app_name]/hooks.py`).
    *   **Purpose:** Central place to map system/DocType events to specific Python functions (dotted path). Preferred way to handle standard DocType events (`validate`, `on_update`, `on_submit`, `on_cancel`, `on_trash`, etc.) and schedule background jobs.
    *   **Structure:** Dictionary mapping event keys (e.g., `doc_events`, `scheduler_events`) to function paths.
    *   **Example (`doc_events`):**
        ```python
        # my_app/hooks.py
        doc_events = {
            "Project Task": {
                "validate": "my_app.utils.validate_project_task",
                "on_update": "my_app.utils.project_task_updated",
                # "*" can be used as a wildcard for all doctypes
            }
        }
        ```
        ```python
        # my_app/utils.py
        import frappe
        def validate_project_task(doc, method):
             # doc: the document object
             # method: the event string (e.g., "validate")
             pass
        def project_task_updated(doc, method):
             pass
        ```

*   **API Endpoints (`@frappe.whitelist()`):**
    *   **Location:** Any `.py` file within the app (e.g., `api.py`, `utils.py`).
    *   **Purpose:** Expose Python functions to be callable via the REST API (`/api/method/...`) or client-side `frappe.call`.
    *   **Decorator:** `@frappe.whitelist()`. Use `allow_guest=True` only if unauthenticated access is explicitly required and safe.
    *   **Example:**
        ```python
        # my_app/api.py
        import frappe

        @frappe.whitelist()
        def get_task_count(project):
            # Add permission checks if necessary
            return frappe.db.count("Project Task", {"project": project})
        ```

## 2. Frappe Server-Side API (Common Functions)

Use these functions within your Python scripts:

*   **Document Handling:**
    *   `frappe.get_doc(doctype, name)`: Load a single document.
    *   `frappe.get_doc(dict)`: Create a new document instance from a dictionary.
    *   `doc.save()`: Save changes (runs validation/hooks).
    *   `doc.insert()`: Insert new document (runs validation/hooks).
    *   `doc.submit()`: Submit a submittable document (runs `on_submit`).
    *   `doc.cancel()`: Cancel a submitted document (runs `on_cancel`).
    *   `doc.delete()`: Delete document (runs `on_trash`).
    *   `doc.set(fieldname, value)`: Set field value.
    *   `doc.get(fieldname)`: Get field value.
    *   `doc.reload()`: Reload document data from the database.

*   **Database Queries (Prefer ORM over raw SQL):**
    *   `frappe.get_list(doctype, filters={}, fields=['name'], order_by='modified desc', limit_page_length=20, ...) `: Fetch multiple documents as dictionaries. Efficient for lists.
    *   `frappe.get_all(doctype, filters={}, fields=['name'], ...)`: Similar to `get_list`, slightly different syntax/defaults.
    *   `frappe.get_value(doctype, name | filters, fieldname)`: Get a single field value. Can use filters instead of name.
    *   `frappe.db.get_value(...)`: Similar to `get_value`.
    *   `frappe.db.set_value(doctype, name, fieldname | {fieldname: value}, value)`: Update field(s) directly (bypasses hooks/validation - use with caution).
    *   `frappe.db.exists(doctype, name | filters)`: Check if document(s) exist.
    *   `frappe.db.count(doctype, filters={})`: Count documents.
    *   `frappe.db.sql(query, values=(), as_dict=False)`: Execute raw SQL (use sparingly, potential security/compatibility risks).

*   **Session & Permissions:**
    *   `frappe.session.user`: Current user's ID (email).
    *   `frappe.get_user()`: Get the full User document object.
    *   `frappe.has_permission(doctype, ptype='read', doc=None | docname)`: Check permissions for the current user.

*   **Utilities:**
    *   `frappe.throw("Error message", title="Error Title", exc=frappe.ValidationError)`: Raise user-facing exceptions.
    *   `frappe.msgprint("Message", title="Info", indicator="green")`: Show informational messages to the user.
    *   `frappe.log("Log message")` / `frappe.log_error("Title", "Message")`: Write to Frappe logs (`logs/frappe.log` or `logs/error.log`).
    *   `frappe.enqueue("path.to.function", queue='default', timeout=300, **kwargs)`: Enqueue background jobs (see `09-background-jobs.md`).
    *   `frappe.utils.*`: Various utility functions for dates, times, formatting, etc. (e.g., `now_datetime()`, `today()`, `get_fullname()`).
    *   `frappe.cache()`: Access Frappe's caching mechanism (usually Redis).

## 3. Best Practices

*   **Use Hooks for Events:** Prefer defining standard DocType event handlers (`validate`, `on_update`, etc.) in `hooks.py` for better visibility and organization.
*   **Keep Controllers Lean:** Controller methods (`*.py`) should contain logic specific to the DocType instance. General utility functions should go into separate modules (e.g., `utils.py`).
*   **Error Handling:** Use `try...except` blocks for operations that might fail (e.g., external API calls). Use `frappe.throw` for validation errors. Log unexpected errors using `frappe.log_error`.
*   **Permissions:** Be mindful of permissions, especially in whitelisted methods. Use `frappe.has_permission` if necessary. Background jobs often run as Administrator unless specified otherwise.
*   **Performance:** Avoid complex logic or multiple `save()` calls within loops. Use `frappe.get_list` or `frappe.get_all` with specific `fields` instead of loading full documents (`frappe.get_doc`) inside loops (N+1 problem). Use `frappe.db.set_value` cautiously for bulk updates where hooks/validations are not needed.
*   **Readability:** Write clean, well-commented Python code following PEP 8 guidelines.
*   **Testing:** Write unit tests (`test_*.py`) for complex server-side logic.