# Custom Instructions for Frappe Specialist Mode

This directory contains specific instructions and guidelines for the `frappe-specialist` mode, broken down by topic.

## Files

1.  **[01-core-principles-operational.md](01-core-principles-operational.md):** General operating principles, standard workflow, safety protocols, and error handling.
2.  **[02-doctypes-schema.md](02-doctypes-schema.md):** Defining DocTypes, key field types, file structure, schema migrations, and best practices.
3.  **[03-server-scripts-hooks-api.md](03-server-scripts-hooks-api.md):** Writing Python server-side code using DocType controllers, `hooks.py`, and the Frappe server-side API functions.
4.  **[04-client-scripts.md](04-client-scripts.md):** Implementing custom JavaScript logic for Form and List views using the Frappe client-side API (`frappe.ui.form`, `frappe.listview_settings`).
5.  **[05-permissions-roles.md](05-permissions-roles.md):** Configuring access control using Roles, Role Permission Manager, Permission Levels, and User Permissions.
6.  **[06-workflows.md](06-workflows.md):** Defining and managing document lifecycles using the Frappe Workflow engine.
7.  **[07-rest-api-integration.md](07-rest-api-integration.md):** Using the standard REST API for CRUD operations and calling custom `@frappe.whitelist()` methods for integration. Includes notes on Webhooks.
8.  **[08-bench-cli.md](08-bench-cli.md):** Reference for common and essential `bench` command-line interface commands for site, app, process, and database management.
9.  **[09-background-jobs.md](09-background-jobs.md):** Using `frappe.enqueue` and the Frappe Scheduler (`hooks.py`) for running asynchronous background tasks with RQ and Redis.
10. **[10-deployment-configuration.md](10-deployment-configuration.md):** Overview of production components, deployment strategies, key steps, `site_config.json`, and update procedures.
11. **[11-collaboration-escalation.md](11-collaboration-escalation.md):** Guidelines for collaborating with other specialist modes and escalating issues via the lead. (To be created if source content exists)
12. **[12-ui-views-reporting.md](12-ui-views-reporting.md):** Instructions related to standard UI elements (Workspaces, Dashboards) and Frappe's reporting engine. (To be created if source content exists)

*(These instructions supplement the base mode definition and should be consulted when performing relevant tasks.)*