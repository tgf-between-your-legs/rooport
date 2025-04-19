# Neon API Reference (Conceptual Overview)

Using the Neon API to programmatically manage Neon projects, branches, endpoints, and more.

## Core Concept

The Neon API provides RESTful endpoints for managing your Neon resources outside the Neon Console UI or CLI. This is useful for automation, CI/CD integration, or building custom management tools.

*   **Authentication:** Requires an API key generated from your Neon account settings. The key is typically passed in the `Authorization` header as a Bearer token (`Authorization: Bearer <your_neon_api_key>`).
*   **Base URL:** `https://console.neon.tech/api/v2/`
*   **Format:** Standard REST API using JSON for request and response bodies.

## Common API Operations (Conceptual Examples)

*(Note: This is a conceptual overview. Refer to the official Neon API documentation for exact endpoints, parameters, request/response schemas, and authentication details.)*

### Projects

*   **List Projects:** `GET /projects`
    *   Returns a list of your Neon projects.
*   **Get Project Details:** `GET /projects/{project_id}`
    *   Returns details for a specific project.

### Branches

*   **List Branches:** `GET /projects/{project_id}/branches`
    *   Returns a list of branches within a project.
*   **Create Branch:** `POST /projects/{project_id}/branches`
    *   **Request Body (Example):**
        ```json
        {
          "branch": {
            "parent_id": "br-parent-branch-id", // Optional: Specify parent branch ID
            // "parent_lsn": "...", // Optional: Specify LSN for point-in-time branching
            "name": "dev/feature-xyz" // Optional: Name for the new branch
          }
          // Potentially specify compute endpoint settings for the new branch
        }
        ```
    *   Creates a new branch, typically inheriting from the project's primary branch or a specified parent.
*   **Get Branch Details:** `GET /projects/{project_id}/branches/{branch_id}`
    *   Returns details for a specific branch.
*   **Update Branch:** `PATCH /projects/{project_id}/branches/{branch_id}`
    *   Used to modify branch settings (e.g., compute size, autoscaling limits).
*   **Delete Branch:** `DELETE /projects/{project_id}/branches/{branch_id}`
    *   Deletes a specific branch (cannot delete the primary branch).

### Endpoints (Compute Nodes)

*   **List Endpoints:** `GET /projects/{project_id}/endpoints` or `GET /projects/{project_id}/branches/{branch_id}/endpoints`
    *   Returns compute endpoints associated with a project or specific branch. A branch typically has one compute endpoint.
*   **Create Endpoint:** `POST /projects/{project_id}/endpoints`
    *   **Request Body (Example):**
        ```json
        {
          "endpoint": {
            "branch_id": "br-target-branch-id",
            "type": "read_write" // Or "read_only"
            // Specify compute size, autoscaling settings, etc.
          }
        }
        ```
    *   Creates a new compute endpoint (usually done automatically when creating a branch, but API allows explicit creation/management).
*   **Get Endpoint Details:** `GET /projects/{project_id}/endpoints/{endpoint_id}`
    *   Returns details for a specific endpoint, including the connection string.
*   **Update Endpoint:** `PATCH /projects/{project_id}/endpoints/{endpoint_id}`
    *   Modify compute size, autoscaling limits, etc.
*   **Start/Suspend Endpoint:** `POST /projects/{project_id}/endpoints/{endpoint_id}/start`, `POST /projects/{project_id}/endpoints/{endpoint_id}/suspend`
    *   Manually control the compute endpoint's active state (relevant for non-autoscaling endpoints or managing costs).
*   **Delete Endpoint:** `DELETE /projects/{project_id}/endpoints/{endpoint_id}`

### Other Operations

*   **Databases:** `GET /projects/{project_id}/branches/{branch_id}/databases`, `POST ...`
*   **Roles:** `GET /projects/{project_id}/branches/{branch_id}/roles`, `POST ...`
*   **Operations:** `GET /projects/{project_id}/operations`, `GET /projects/{project_id}/operations/{operation_id}` (Check status of long-running API actions like branch creation).

## Use Cases for API

*   **CI/CD:** Create temporary branches for testing pull requests, run migrations, run tests, and delete the branch afterwards.
*   **Infrastructure as Code (IaC):** Manage Neon projects and branches using tools like Terraform (via a Neon provider) or Pulumi, which interact with the API.
*   **Custom Dashboards/Tooling:** Build internal tools for managing Neon resources.
*   **Automated Scaling/Management:** Programmatically adjust compute endpoint sizes based on external metrics (use with caution).

Always use the official Neon API documentation as the definitive source for endpoints, parameters, and behavior.

*(Refer to: https://api-docs.neon.tech/reference/getting-started-with-neon-api)*