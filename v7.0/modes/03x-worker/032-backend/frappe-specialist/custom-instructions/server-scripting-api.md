# Frappe: Server Scripting & API

Writing server-side Python code for DocType controllers, hooks, and using the Frappe API.

## Core Concept

Frappe allows extending backend logic using Python scripts. These scripts can interact with the framework's ORM, trigger actions, validate data, and integrate with external services.

## Locations for Server Scripts

1.  **DocType Controllers (`<doctype_name>.py`):**
    *   **Location:** Inside the DocType's folder (e.g., `my_app/my_module/doctype/my_doctype/my_doctype.py`).
    *   **Purpose:** Define methods that belong to a specific DocType instance. These methods are called on the document object (`self`). Often used for custom logic triggered by standard DocType events (defined in hooks or called directly).
    *   **Class:** Must contain a class named after the DocType (e.g., `class MyDoctype(Document):`) inheriting from `frappe.model.document.Document`.

    ```python
    # my_app/my_module/doctype/project_task/project_task.py
    import frappe
    from frappe.model.document import Document

    class ProjectTask(Document):
        # Method called via hooks or other scripts: doc.update_project_status()
        def update_project_status(self):
            if self.project:
                # Use frappe.get_doc to load another document
                project = frappe.get_doc("Project", self.project)
                # Custom logic to update the related project
                project.calculate_completion() # Assume this method exists on Project DocType
                project.save() # Save the related document
                frappe.msgprint(f"Project {self.project} status updated.")

        # --- Standard DocType Event Methods (Can be defined here OR triggered via hooks.py) ---
        # These methods are automatically called by Frappe if defined in the controller.
        # It's often cleaner to manage these via hooks.py for better overview.

        # def validate(self):
        #     # Runs before saving (on create and update)
        #     if self.start_date and self.end_date and self.start_date > self.end_date:
        #         frappe.throw("End Date cannot be before Start Date")

        # def before_save(self):
        #     # Runs just before the document is saved
        #     self.internal_status = "Processed"

        # def on_update(self):
        #     # Runs after a document is successfully saved (update only)
        #     frappe.log("Project Task updated: " + self.name)

        # def on_submit(self):
        #     # Runs after a submittable document is submitted
        #     if self.status != 'Completed':
        #          frappe.throw("Only completed tasks can be submitted")
        #     # Call another method
        #     self.notify_completion()

        # def on_cancel(self):
        #     # Runs after a submitted document is cancelled
        #     pass

        # def on_trash(self):
        #     # Runs before a document is moved to trash (deleted)
        #     pass
    ```

2.  **Hooks (`hooks.py`):**
    *   **Location:** In your app's main directory (e.g., `my_app/hooks.py`).
    *   **Purpose:** Define functions to be called automatically on specific DocType events or system events across the app. This is often preferred over defining event methods directly in the controller for better organization.
    *   **Structure:** A dictionary mapping event keys to function paths (dotted notation).

    ```python
    # my_app/hooks.py
    app_name = "my_app"
    app_title = "My App"
    # ... other hooks ...

    doctype_list_js = {"Project Task" : "public/js/project_task_list.js"}
    doctype_js = {"Project Task" : "public/js/project_task.js"}

    # Standard DocType Events
    doc_events = {
        "Project Task": {
            "validate": "my_app.utils.validate_project_task",
            "on_update": "my_app.utils.project_task_updated",
            "on_submit": "my_app.controllers.project_task_controller.handle_submission",
            # "on_cancel": "path.to.cancel.handler",
            # "on_trash": "path.to.trash.handler",
        },
        "*": { # Wildcard for all DocTypes
            "on_update": "my_app.utils.log_all_updates"
        }
    }

    # Scheduler Events (run via bench worker & scheduler)
    scheduler_events = {
        "daily": [
            "my_app.tasks.daily_cleanup"
        ],
        "cron": {
            "*/15 * * * *": [ # Every 15 minutes
                "my_app.tasks.check_external_service"
            ]
        }
    }

    # Other hooks: permission_query_conditions, extend_bootinfo, etc.
    ```
    ```python
    # my_app/utils.py (Example functions called by hooks)
    import frappe

    def validate_project_task(doc, method):
        if doc.start_date and doc.end_date and doc.start_date > doc.end_date:
            frappe.throw("End Date cannot be before Start Date (validated via hook)")

    def project_task_updated(doc, method):
        frappe.log(f"Project Task {doc.name} updated (via hook)")

    def log_all_updates(doc, method):
        frappe.log(f"Document {doc.doctype} {doc.name} updated.")
    ```

3.  **API Endpoints (`@frappe.whitelist()`):**
    *   **Location:** Any `.py` file within your app.
    *   **Purpose:** Expose Python functions to be callable via the Frappe REST API or client-side `frappe.call`.
    *   **Decorator:** Use `@frappe.whitelist()` above the function definition.
    *   **Guest Access:** Use `@frappe.whitelist(allow_guest=True)` to allow unauthenticated access (use with extreme caution).

    ```python
    # my_app/api.py
    import frappe

    @frappe.whitelist()
    def get_task_summary(project_name):
        if not project_name:
            frappe.throw("Project name is required")

        # Check permissions if needed (whitelisted functions don't automatically check DocType perms)
        # if not frappe.has_permission("Project", "read", doc=project_name):
        #     frappe.throw("Not permitted to read project", frappe.PermissionError)

        count = frappe.db.count("Project Task", {"project": project_name})
        completed_count = frappe.db.count("Project Task", {"project": project_name, "status": "Completed"})

        return {
            "project": project_name,
            "total_tasks": count,
            "completed_tasks": completed_count
        }

    @frappe.whitelist(allow_guest=True)
    def get_public_info():
        return {"version": "1.0", "status": "OK"}
    ```

## Frappe API (Server-Side)

Common functions available within server scripts:

*   **Document Access:**
    *   `frappe.get_doc(doctype, name)`: Load a single document instance.
    *   `frappe.get_doc(dict)`: Create a new document instance from a dictionary. Call `.insert()` or `.save()` on it.
    *   `doc.save()`: Save changes to a document. Runs `validate` and `before_save`/`on_update`.
    *   `doc.insert()`: Insert a new document. Runs `validate` and `before_save`/`on_update`.
    *   `doc.submit()`: Submit a submittable document. Runs `on_submit`.
    *   `doc.cancel()`: Cancel a submitted document. Runs `on_cancel`.
    *   `doc.delete()`: Delete a document (moves to trash). Runs `on_trash`.
    *   `doc.set(fieldname, value)`: Set a field value.
    *   `doc.get(fieldname)`: Get a field value.
*   **Database Queries:**
    *   `frappe.get_list(doctype, filters={}, fields=['name'], order_by='modified desc', limit_page_length=20)`: Fetch a list of documents as dictionaries. Efficient for lists.
    *   `frappe.get_value(doctype, name, fieldname)`: Get a single field value from a document.
    *   `frappe.db.get_value(...)`: Similar to `get_value`.
    *   `frappe.db.set_value(doctype, name, fieldname, value)`: Update a single field value directly (bypasses hooks/validation).
    *   `frappe.db.exists(doctype, name)`: Check if a document exists.
    *   `frappe.db.count(doctype, filters={})`: Count documents.
    *   `frappe.db.sql(query, values=(), as_dict=False)`: Execute a raw SQL query (use with caution, prefer ORM).
*   **User & Session:**
    *   `frappe.session.user`: Current user's ID (email).
    *   `frappe.get_user()`: Get the full User document for the current user.
    *   `frappe.has_permission(doctype, ptype='read', doc=None)`: Check permissions for the current user.
*   **Utilities:**
    *   `frappe.throw("Error message", title="Error Title", exc=frappe.ValidationError)`: Raise an exception, displayed to the user.
    *   `frappe.msgprint("Message")`: Show an informational message to the user.
    *   `frappe.log("Log message")` or `frappe.log_error("Title", "Message")`: Write to Frappe logs.
    *   `frappe.enqueue("path.to.function", arg1=..., arg2=...)`: Enqueue a background job.
    *   `frappe.utils.now_datetime()`, `frappe.utils.today()`: Get current date/time.

Always refer to the Frappe Framework API documentation for detailed usage.