# Frappe Specialist: REST API &amp; Integration

Frappe provides a built-in REST API for interacting with DocTypes and calling custom server functions, enabling integration with external systems.

## 1. Standard REST API (CRUD on DocTypes)

*   **Endpoints:** Follow the pattern `/api/resource/[DocType Name]/[Document Name]`.
*   **Authentication:**
    *   **API Keys:** Generate API Key &amp; Secret for a User. Pass via `Authorization: token [api_key]:[api_secret]` header.
    *   **Session Auth:** Works automatically if called from a logged-in browser session.
*   **Methods:**
    *   `GET /api/resource/[DocType]`: List documents (supports filtering, pagination, field selection via query params).
    *   `POST /api/resource/[DocType]`: Create a new document (pass data as JSON body).
    *   `GET /api/resource/[DocType]/[Name]`: Read a specific document.
    *   `PUT /api/resource/[DocType]/[Name]`: Update a specific document (pass fields to update in JSON body).
    *   `DELETE /api/resource/[DocType]/[Name]`: Delete a specific document.
*   **Query Parameters (for GET List):**
    *   `fields`: `["name", "subject"]` (JSON array string)
    *   `filters`: `[["status", "=", "Open"], ["priority", "=", "High"]]` (JSON array of arrays)
    *   `limit_page_length`: Number of records (e.g., `50`).
    *   `limit_start`: Offset for pagination (e.g., `0`, `50`, `100`).
    *   `order_by`: `creation desc` or `subject asc`.
*   **Permissions:** All API calls respect the Role Permissions defined for the authenticating user. Ensure the user associated with the API key has the necessary Read/Write/Create/Delete permissions for the DocType.

## 2. Whitelisted Methods (`@frappe.whitelist()`)

*   **Purpose:** Expose custom Python functions as API endpoints.
*   **Decorator:** `@frappe.whitelist()` on functions in any `.py` file within your app. Use `allow_guest=True` only if unauthenticated access is explicitly needed and safe.
*   **Endpoint:** `/api/method/[app_name].[path.to.module].[function_name]`
*   **Method:**
    *   `GET`: For read-only operations. Pass arguments as query parameters.
    *   `POST`: For operations that modify data. Pass arguments in the JSON request body.
*   **Permissions:** Whitelisted methods *do not* automatically enforce DocType permissions. You must implement permission checks within the function using `frappe.has_permission` if necessary.
*   **Example:**
    ```python
    # my_app/api.py
    import frappe

    @frappe.whitelist()
    def update_task_status(task_name, new_status):
        # Explicit permission check might be needed here
        # if not frappe.has_permission("Project Task", "write", doc=task_name):
        #     frappe.throw("Not permitted", frappe.PermissionError)
        try:
            task = frappe.get_doc("Project Task", task_name)
            task.status = new_status
            task.save()
            return {"status": "success", "message": f"Task {task_name} updated to {new_status}"}
        except Exception as e:
            frappe.log_error(frappe.get_traceback(), "Update Task Status API Error")
            frappe.throw(f"Failed to update task: {e}")
    ```
    ```bash
    # Call via POST using curl
    curl -X POST "http://yoursite.com/api/method/my_app.api.update_task_status" \
      -H "Authorization: token key:secret" \
      -H "Content-Type: application/json" \
      -d '{
            "task_name": "TASK-001",
            "new_status": "Completed"
          }'
    ```

## 3. Webhooks

*   **Purpose:** Send data *from* Frappe *to* an external URL when a specific DocType event occurs.
*   **Configuration:** Setup -> Integrations -> Webhook -> New.
    *   Select DocType and Trigger Event (e.g., `on_update`, `on_submit`).
    *   Specify the Request URL of the external service.
    *   Configure Headers (e.g., for authentication) and Request Body (select fields to send).
*   **Use Case:** Notifying external systems about changes in Frappe (e.g., update CRM when a Lead is created).

## 4. Integration Considerations

*   **Authentication:** Use API Keys & Secrets for server-to-server communication.
*   **Error Handling:** Implement robust error handling in whitelisted methods (`try...except`, `frappe.throw`, `frappe.log_error`). External systems calling the API should also handle potential HTTP errors (4xx, 5xx).
*   **Rate Limiting:** Be aware of potential rate limits on the Frappe server or the external API being called. Implement delays or use background jobs if necessary.
*   **Background Jobs (`frappe.enqueue`):** For integrations that might take time (calling slow external APIs), enqueue the integration logic into a background job to avoid blocking the main request thread.
*   **Security:** Validate data received from external systems. Do not expose sensitive data unnecessarily via guest-allowed whitelisted methods. Consult `security-specialist` via lead for secure integration patterns.
*   **Idempotency:** Design API endpoints (especially POST/PUT) to be idempotent where possible, so calling them multiple times with the same input yields the same result.

The REST API and whitelisted methods are key tools for connecting Frappe with other parts of an IT ecosystem.