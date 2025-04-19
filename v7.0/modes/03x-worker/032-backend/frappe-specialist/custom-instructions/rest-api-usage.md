# Frappe: REST API Usage

Interacting with Frappe DocTypes via the built-in REST API.

## Core Concept

Frappe automatically provides a RESTful API for CRUD (Create, Read, Update, Delete) operations on all DocTypes that have the "API Access" permission enabled for relevant roles.

## Authentication

*   **API Keys & Secrets:** The standard method. Generate API Key and Secret pairs for a User via the User's settings page in the Desk UI.
*   **Request Headers:** Pass credentials in the `Authorization` header:
    *   **Token Method:** `Authorization: token <api_key>:<api_secret>`
    *   **Basic Auth:** Use API Key as username and API Secret as password (less common).
*   **Session Auth:** If making requests from a logged-in browser session, the session cookie handles authentication.

## Common Endpoints & Methods

Base URL is typically `http://<your-site-name>:<port>/api/resource`

*   **List Resources:** `GET /api/resource/<DocType>`
    *   Returns a list of documents for the specified DocType.
    *   Supports pagination, filtering, and field selection via query parameters.
*   **Create Resource:** `POST /api/resource/<DocType>`
    *   Request Body: JSON object representing the document data to create.
    *   Response: JSON object of the newly created document.
*   **Read Resource:** `GET /api/resource/<DocType>/<name>`
    *   `<name>` is the unique ID (usually the `name` field) of the document.
    *   Response: JSON object of the specified document.
*   **Update Resource:** `PUT /api/resource/<DocType>/<name>`
    *   Request Body: JSON object containing the fields to update.
    *   Response: JSON object of the updated document.
*   **Delete Resource:** `DELETE /api/resource/<DocType>/<name>`
    *   Response: Typically a success message (e.g., `{"message": "ok"}`).

## Query Parameters (for GET List)

*   **`fields`**: Comma-separated list of fields to return. Use backticks for JSON format.
    *   Example: `?fields=["name","subject","status"]`
*   **`filters`**: Filter results based on field values. JSON list of lists/tuples `[field, operator, value]`.
    *   Operators: `=`, `!=`, `>`, `<`, `>=`, `<=`, `like`, `not like`, `in`, `not in`.
    *   Example: `?filters=[["status","=","Open"],["priority","=","High"]]`
*   **`limit_page_length`**: Number of documents per page (default usually 20). Use `0` for potentially unlimited (use with caution).
    *   Example: `?limit_page_length=50`
*   **`limit_start`**: Starting offset for pagination (0-indexed).
    *   Example: `?limit_start=50` (for page 2 if limit is 50)
*   **`order_by`**: Field to sort by, optionally add `asc` or `desc`.
    *   Example: `?order_by=creation desc`

## Example Requests (using `curl`)

```bash
BASE_URL="http://localhost:8000" # Your site URL
DOCTYPE="Project Task"
API_KEY="your_api_key"
API_SECRET="your_api_secret"

# List Open, High Priority Tasks (first 10)
curl -G "$BASE_URL/api/resource/$DOCTYPE" \
  --header "Authorization: token $API_KEY:$API_SECRET" \
  --data-urlencode 'fields=["name","subject","status","priority"]' \
  --data-urlencode 'filters=[["status","=","Open"],["priority","=","High"]]' \
  --data-urlencode 'limit_page_length=10' \
  --data-urlencode 'order_by=creation desc'

# Get a specific Task by name (ID)
TASK_NAME="TASK-00001"
curl "$BASE_URL/api/resource/$DOCTYPE/$TASK_NAME" \
  --header "Authorization: token $API_KEY:$API_SECRET"

# Create a new Task
curl -X POST "$BASE_URL/api/resource/$DOCTYPE" \
  --header "Authorization: token $API_KEY:$API_SECRET" \
  --header "Content-Type: application/json" \
  --data '{
    "subject": "New Task via API",
    "status": "Open",
    "priority": "Medium"
  }'

# Update a Task
TASK_NAME_TO_UPDATE="TASK-00002"
curl -X PUT "$BASE_URL/api/resource/$DOCTYPE/$TASK_NAME_TO_UPDATE" \
  --header "Authorization: token $API_KEY:$API_SECRET" \
  --header "Content-Type: application/json" \
  --data '{
    "status": "In Progress"
  }'

# Delete a Task
TASK_NAME_TO_DELETE="TASK-00003"
curl -X DELETE "$BASE_URL/api/resource/$DOCTYPE/$TASK_NAME_TO_DELETE" \
  --header "Authorization: token $API_KEY:$API_SECRET"
```

## Whitelisted Functions (`@frappe.whitelist()`)

*   Custom Python functions decorated with `@frappe.whitelist()` can be called via the API.
*   **Endpoint:** `GET /api/method/<app_name>.<path.to.module>.<function_name>`
*   **Parameters:** Pass function arguments as query parameters.
*   **POST:** Use POST requests for whitelisted functions that modify data. Pass arguments in the JSON request body.

```bash
# Call the whitelisted function get_task_summary from api.py example
curl -G "$BASE_URL/api/method/my_app.api.get_task_summary" \
  --header "Authorization: token $API_KEY:$API_SECRET" \
  --data-urlencode 'project_name=Project Alpha'
```

## Considerations

*   **Permissions:** API requests respect Frappe's Role Permissions system. The user associated with the API Key/Secret must have the necessary permissions for the DocType and action.
*   **Performance:** Be mindful of fetching large amounts of data. Use `fields`, `filters`, and `limit_page_length`.
*   **Error Handling:** API returns standard HTTP status codes (e.g., 403 Forbidden, 404 Not Found, 400 Bad Request, 500 Internal Server Error) with JSON error messages.

The REST API provides a standard way to integrate Frappe with external applications and services.

*(Refer to the official Frappe REST API documentation: https://frappeframework.com/docs/user/en/api/rest)*