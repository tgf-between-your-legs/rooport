# Frappe: Client Scripts

Adding custom client-side JavaScript behavior to Frappe forms and views.

## Core Concept

While Frappe provides a rich UI out-of-the-box, you often need to add custom frontend logic to forms or list views. Client Scripts allow you to write JavaScript code that interacts with the Frappe UI framework.

## Where to Write Client Scripts

1.  **DocType Client Script Section (UI):**
    *   **Location:** Customize -> DocType -> Select DocType -> Client Scripts section.
    *   **Pros:** Easy to access and edit directly within the Frappe UI. Good for simple, DocType-specific logic.
    *   **Cons:** Not version controlled easily with Git. Can become cluttered for complex logic. Code is stored in the database.
2.  **App's `public/js` Folder (Recommended for Apps):**
    *   **Location:** Create JS files within your custom app's `public/js` directory (e.g., `my_app/public/js/my_doctype.js`).
    *   **Linking:** Link the script to the DocType using `hooks.py`:
        ```python
        # my_app/hooks.py
        doctype_js = {
            "My Doctype Name": "public/js/my_doctype.js"
            # Can be a single string or a list of strings
            # "Another Doctype": ["public/js/common.js", "public/js/another_doctype.js"]
        }
        # For List Views:
        doctype_list_js = {
             "My Doctype Name": "public/js/my_doctype_list.js"
        }
        ```
    *   **Pros:** Version controlled with Git. Better organization for larger scripts. Can be shared across DocTypes if structured correctly.
    *   **Cons:** Requires `bench build` after changes.

## Client Script API (`frappe.ui.form` / `frappe.listview`)

Frappe provides JavaScript APIs to interact with forms and list views.

### Form Scripts (`doctype_js`)

*   **Entry Point:** Use the `frappe.ui.form.on()` function to attach handlers to specific DocTypes and events.
    ```javascript
    // my_app/public/js/my_doctype.js

    frappe.ui.form.on('My Doctype Name', {
        // --- Form Events ---
        setup: function(frm) {
            // Runs once when the form is initially set up
            console.log('Setup:', frm.doc.name);
            // Example: Set query filters for Link fields
            frm.set_query('project', function() {
                return {
                    filters: {
                        status: 'Open'
                    }
                };
            });
        },

        onload: function(frm) {
            // Runs when the document data is loaded into the form (after setup)
            console.log('Loaded:', frm.doc.name, frm.doc);
            if (frm.is_new()) {
                frm.set_value('status', 'Open'); // Set default value on new forms
            }
        },

        refresh: function(frm) {
            // Runs whenever the form is refreshed (load, save, field change triggers)
            console.log('Refreshed:', frm.doc.name);
            // Example: Add custom buttons based on status
            if (frm.doc.status === 'Open') {
                frm.add_custom_button(__('Start Progress'), function() {
                    frm.set_value('status', 'In Progress');
                    frm.save_or_update();
                }, __('Actions')); // Optional button group
            }
             // Example: Show/hide fields based on conditions
            frm.toggle_display('resolution_details', frm.doc.status === 'Resolved');
        },

        validate: function(frm) {
            // Runs before saving. Use for client-side validation.
            if (frm.doc.estimated_hours < 0) {
                frappe.msgprint(__('Estimated hours cannot be negative.'));
                frappe.validated = false; // Prevent saving
            }
        },

        before_save: function(frm) {
            // Runs just before the document is sent to the server for saving
            console.log('Before Save');
        },

        after_save: function(frm) {
            // Runs after the document is successfully saved
            console.log('After Save');
            frappe.show_alert({ message: 'Document Saved!', indicator: 'green' });
        },

        // --- Field Events ---
        // Triggered when a specific field's value changes
        status: function(frm) {
            console.log('Status changed to:', frm.doc.status);
            frappe.show_alert(`Status updated to ${frm.doc.status}`);
            // Example: Make another field read-only based on status
            frm.set_df_property('project', 'read_only', frm.doc.status !== 'Open');
        },

        project: function(frm) {
            // Example: Fetch data from linked document using frappe.call
            if (frm.doc.project) {
                frappe.call({
                    method: 'frappe.client.get_value',
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
            }
        },

        // --- Child Table Field Events ---
        // Triggered when a field within a child table row changes
        // Replace 'child_table_fieldname' with the actual fieldname of your Table field
        // Replace 'child_fieldname' with the fieldname inside the child table
        // child_table_fieldname + "_on_form_rendered": function(frm) { ... },
        // child_table_fieldname + "_add": function(frm, cdt, cdn) { ... }, // After row added
        // child_table_fieldname + "_remove": function(frm, cdt, cdn) { ... }, // Before row removed
        // child_fieldname: function(frm, cdt, cdn) {
        //    // cdt: Child DocType name (string)
        //    // cdn: Child document name (string, unique ID for the row)
        //    let row = frappe.get_doc(cdt, cdn);
        //    console.log('Child field changed:', row.child_fieldname);
        //    // Example: Calculate total in parent form
        //    // calculate_total(frm);
        // }

    }); // End frappe.ui.form.on
    ```

*   **`frm` Object:** Represents the current form. Key properties/methods:
    *   `frm.doc`: The current document's data (JavaScript object). Access fields like `frm.doc.fieldname`.
    *   `frm.set_value(fieldname, value)`: Set a field's value.
    *   `frm.get_value(fieldname)`: Get a field's value.
    *   `frm.refresh_field(fieldname)`: Re-render a specific field.
    *   `frm.set_df_property(fieldname, property, value)`: Change field properties dynamically (e.g., `read_only`, `hidden`, `reqd`, `options`).
    *   `frm.toggle_display(fieldname, show)`: Show/hide a field.
    *   `frm.add_custom_button(...)`, `frm.remove_custom_button(...)`.
    *   `frm.save()`, `frm.save_or_update()`: Trigger form save.
    *   `frm.is_new()`: Returns true if the form is for a new document.
    *   `frm.set_query(fieldname, query_function)`: Set dynamic filters for Link fields.
*   **`frappe.call()`:** Make server calls to `@frappe.whitelist()` methods.
*   **`frappe.msgprint()`**, `frappe.show_alert()`**: Display messages.
*   **`frappe.validated`**: Set to `false` within `validate` handler to prevent saving.

### List View Scripts (`doctype_list_js`)

*   Customize the appearance and behavior of List Views.
*   **API:** `frappe.listview_settings['My Doctype Name'] = { ... };`
*   **Options:**
    *   `onload(listview)`: Called when the list view loads.
    *   `refresh(listview)`: Called when the list view refreshes.
    *   `primary_action(listview)`: Define a custom primary button action.
    *   `get_indicator(doc)`: Return `[text, color]` for status indicators in the list.
    *   `formatters`: Customize how field values are displayed in columns.
    *   `add_fields`: Additional fields to fetch for use in formatters or indicators.

```javascript
// my_app/public/js/my_doctype_list.js
frappe.listview_settings['Project Task'] = {
    // Add status indicator
    get_indicator: function(doc) {
        if (doc.status === "Open") {
            return [__("Open"), "grey", "status,=,Open"];
        } else if (doc.status === "In Progress") {
            return [__("In Progress"), "blue", "status,=,In Progress"];
        } else if (doc.status === "Completed") {
            return [__("Completed"), "green", "status,=,Completed"];
        }
    },
    // Customize displayed fields (optional, usually done via List View settings UI)
    // fields: ["name", "subject", "project", "status", "priority"],

    // Custom formatter for priority
    // formatters: {
    //     priority(val) {
    //         if (val === "High") return `<span style="color:red; font-weight:bold;">${val}</span>`;
    //         return val;
    //     }
    // }
};
```

Client Scripts provide significant power to enhance the Frappe user experience. Remember to run `bench build` after making changes to files in the `public` directory.

*(Refer to the official Frappe Client Scripting documentation: https://frappeframework.com/docs/user/en/desk/scripting/client-script)*