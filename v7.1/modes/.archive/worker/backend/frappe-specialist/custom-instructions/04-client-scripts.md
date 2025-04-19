# Frappe Specialist: Client Scripts (JavaScript)

Client Scripts allow adding custom JavaScript behavior to Frappe forms (DocType views) and list views, enhancing the user interface and interaction beyond standard capabilities.

## 1. Where to Write Client Scripts

*   **DocType Client Script Section (UI):**
    *   **Location:** Customize Form -> Select DocType -> Client Scripts section.
    *   **Use Case:** Good for very simple, quick, DocType-specific logic.
    *   **Pros:** Easy access via UI.
    *   **Cons:** Not easily version controlled (stored in DB), can become messy.
*   **App's `public/js` Folder (Recommended):**
    *   **Location:** Create `.js` files in `[app_name]/public/js/`.
    *   **Linking:** Connect scripts to DocTypes via `hooks.py`:
        ```python
        # [app_name]/hooks.py
        doctype_js = {
            "My Doctype": "public/js/my_doctype.js",
            # Can be a list for multiple scripts
            "Another Doctype": ["public/js/common.js", "public/js/another_doctype.js"]
        }
        doctype_list_js = {
             "My Doctype": "public/js/my_doctype_list.js"
        }
        ```
    *   **Pros:** Version controlled (Git), better organization, reusable code.
    *   **Cons:** Requires `bench build` after changes.

## 2. Form Scripts (`doctype_js`)

*   **API:** Use the `frappe.ui.form.on(doctype, event_handlers)` function.
*   **`frm` Object:** Represents the current form instance. Key properties/methods:
    *   `frm.doc`: The document data object (e.g., `frm.doc.fieldname`).
    *   `frm.set_value(fieldname, value)`: Set field value. Triggers change events.
    *   `frm.get_value(fieldname)`: Get field value.
    *   `frm.refresh_field(fieldname)`: Re-render a field.
    *   `frm.set_df_property(fieldname, property, value)`: Change field properties (e.g., `read_only`, `hidden`, `reqd`, `options`, `label`).
    *   `frm.toggle_display(fieldname, show)`: Show/hide field.
    *   `frm.add_custom_button(label, action, group)` / `frm.remove_custom_button(...)`.
    *   `frm.save()` / `frm.save_or_update()`: Trigger form save.
    *   `frm.is_new()`: Check if it's a new document.
    *   `frm.set_query(fieldname, query_function | {filters: {...}})`: Set dynamic filters for Link fields.
    *   `frm.call(method, args, callback)`: Call a server-side `@frappe.whitelist()` method associated with the DocType controller.
    *   `cur_frm`: Global variable referencing the currently active form (use `frm` passed to handlers where possible).

*   **Common Form Events (within `frappe.ui.form.on` object):**
    *   `setup(frm)`: Runs once when the form layout is first created. Good for setting up queries (`frm.set_query`).
    *   `onload(frm)`: Runs when document data is loaded (after `setup`). Good for setting initial values on new docs (`frm.is_new()`).
    *   `refresh(frm)`: Runs whenever the form is refreshed (load, save, some field changes). Good for adding custom buttons, setting field properties (`set_df_property`), showing/hiding fields (`toggle_display`).
    *   `validate(frm)`: Runs before saving. Use for client-side validation. Set `frappe.validated = false;` to prevent saving.
    *   `before_save(frm)`: Runs just before data is sent to the server.
    *   `after_save(frm)`: Runs after successful save.
    *   `[fieldname](frm)`: Runs when the value of `fieldname` changes. Good for cascading changes, fetching related data (`frappe.call`), dynamic UI updates.
    *   **Child Table Events:**
        *   `[child_table_fieldname]_on_form_rendered(frm)`: Runs when the child table grid is rendered.
        *   `[child_table_fieldname]_add(frm, cdt, cdn)`: Runs after a new row is added. `cdt`=Child DocType, `cdn`=Child doc name.
        *   `[child_table_fieldname]_remove(frm, cdt, cdn)`: Runs before a row is removed.
        *   `[child_fieldname](frm, cdt, cdn)`: Runs when a field *within* a child table row changes. Access the row data using `frappe.get_doc(cdt, cdn)`.

*   **Example:**
    ```javascript
    // my_app/public/js/project_task.js
    frappe.ui.form.on('Project Task', {
        refresh: function(frm) {
            // Add button only if status is Open
            if (frm.doc.status === 'Open') {
                frm.add_custom_button(__('Start Task'), function() {
                    frm.set_value('status', 'Working');
                    frm.save_or_update();
                });
            }
            // Make project read-only if not new
            frm.set_df_property('project', 'read_only', !frm.is_new());
        },
        project: function(frm) {
            // Fetch project customer when project changes
            if (frm.doc.project) {
                frappe.call({
                    method: 'frappe.client.get_value', // Generic method to get field value
                    args: {
                        doctype: 'Project',
                        fieldname: 'customer',
                        filters: { name: frm.doc.project }
                    },
                    callback: function(r) {
                        if (r.message) {
                            frm.set_value('customer', r.message.customer);
                        }
                    }
                });
            } else {
                frm.set_value('customer', ''); // Clear customer if project is cleared
            }
        },
        validate: function(frm) {
            if (frm.doc.actual_hours < 0) {
                frappe.msgprint(__('Actual hours cannot be negative.'));
                frappe.validated = false; // Prevent save
            }
        }
    });
    ```

## 3. List View Scripts (`doctype_list_js`)

*   **API:** `frappe.listview_settings['Doctype Name'] = { ... };`
*   **Purpose:** Customize the appearance and behavior of List Views.
*   **Common Options:**
    *   `onload(listview)`: Runs when the list view loads.
    *   `refresh(listview)`: Runs when the list view refreshes.
    *   `primary_action(listview)`: Define a custom primary button action.
    *   `get_indicator(doc)`: Return `[text, color, filter_condition]` for status indicators.
    *   `formatters`: Object mapping fieldnames to functions that customize cell rendering. `function(value, df, doc)`
    *   `add_fields`: Array of additional fields to fetch (required if used in `get_indicator` or `formatters`).

*   **Example:**
    ```javascript
    // my_app/public/js/project_task_list.js
    frappe.listview_settings['Project Task'] = {
        add_fields: ["priority", "status"], // Fetch priority and status for indicator/formatter
        get_indicator: function(doc) {
            // Color indicator based on status
            const colors = {
                "Open": "grey", "Working": "blue", "Pending Review": "orange", "Completed": "green", "Cancelled": "red"
            };
            return [__(doc.status), colors[doc.status] || "darkgrey", `status,=,${doc.status}`];
        },
        formatters: {
            subject(val, df, doc) {
                // Make high priority subjects bold and red
                if (doc.priority === "High") {
                    return `<strong style="color:red;">${val}</strong>`;
                }
                return val;
            }
        }
    };
    ```

## 4. General Client-Side API (`frappe.*`)

*   `frappe.call(options)`: Call server-side `@frappe.whitelist()` methods.
    *   `method`: Dotted path to function (e.g., `my_app.api.my_function`).
    *   `args`: Object containing arguments for the Python function.
    *   `callback`: Function executed on successful response `(r) => { ... }`. `r.message` contains the return value.
    *   `error`: Function executed on error `(err) => { ... }`.
    *   `freeze`: Boolean, show "Processing..." overlay (default `false`).
*   `frappe.msgprint(message | {message: ..., title: ..., indicator: ...})`: Display messages.
*   `frappe.show_alert(message | {message: ..., indicator: ...}, seconds)`: Temporary alerts.
*   `frappe.confirm(message, success_callback, failure_callback)`: Confirmation dialog.
*   `frappe.prompt(fields, callback, title, primary_label)`: Dialog with input fields.
*   `frappe.route_options`: Get options passed via URL hash (e.g., `...#List/Sales%20Order?status=Draft` -> `frappe.route_options.status === 'Draft'`).
*   `frappe.get_route()`: Get current route as an array (e.g., `['List', 'Sales Order']`).
*   `frappe.model.get_value(doctype, name, fieldname, callback)`: Get single value from server.
*   `frappe.client.get_list(doctype, args, callback)`: Get list of documents from server.
*   `frappe.user.has_role(role)`: Check if current user has a specific role.

Remember to run `bench build` after modifying JavaScript files in the `public` directory and clear browser cache if changes don't reflect immediately.