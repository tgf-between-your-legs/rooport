# Frappe: Common `bench` CLI Commands

Reference for essential commands used with the Frappe Bench command-line interface.

## Core Concept

`bench` is the command-line utility for managing Frappe development environments and sites. It handles tasks like creating sites, installing apps, running migrations, managing processes, and more. Commands are typically run from the bench directory (e.g., `frappe-bench`).

## Site Management

*   **`bench new-site <site-name>`**: Creates a new Frappe site with its own database and configuration. Prompts for database details and admin password.
*   **`bench use <site-name>`**: Sets the default site for subsequent bench commands in the current terminal session.
*   **`bench set-default-site <site-name>`**: Sets the default site globally for the bench (updates `sites/common_site_config.json`).
*   **`bench drop-site <site-name>`**: Deletes a site, including its database (use with extreme caution).
*   **`bench list-sites`**: Lists all sites in the current bench.
*   **`bench --site <site-name> [command]`**: Run a specific bench command targeting a particular site without changing the default.

## App Management

*   **`bench get-app <app-git-url> [--branch <branch-name>]`**: Downloads a Frappe app from a Git repository into the `apps/` directory.
*   **`bench new-app <app-name>`**: Creates the boilerplate structure for a new custom Frappe app.
*   **`bench install-app <app-name> [--site <site-name>]`**: Installs an app on a specific site (or the default site). This runs the app's installation hooks and database migrations.
*   **`bench uninstall-app <app-name> [--site <site-name>]`**: Uninstalls an app from a site.
*   **`bench remove-app <app-name>`**: Removes an app completely from the bench's `apps/` directory.

## Database Migrations

*   **`bench migrate [--site <site-name>]`**: Applies pending database schema migrations for all installed apps on the specified site (or default site). This synchronizes the database schema with the DocType definitions.
*   **`bench backup [--site <site-name>]`**: Creates a backup of the site's database and optionally files. Backups are stored in `sites/<site-name>/private/backups`.
*   **`bench --site <site-name> restore <path-to-sql-backup-file>`**: Restores a database backup.
*   **`bench --site <site-name> mariadb`** or **`bench --site <site-name> psql`**: Opens a database shell connected to the site's database.

## Process Management & Development Server

*   **`bench start`**: Starts the development server (Frappe processes, web server, workers, scheduler). Uses `Procfile` for configuration. Suitable for local development only. Press `Ctrl+C` to stop.
*   **`bench restart`**: Restarts the Frappe processes (web server, workers). Useful after configuration changes.
*   **`bench build`**: Builds frontend assets (JS, CSS) for all apps. Required after modifying client-side code or installing/updating apps with frontend components.
*   **`bench watch`**: Automatically watches for changes in app code and rebuilds assets as needed during development.
*   **`bench set-config <key> <value> [--site <site-name>]`**: Sets a configuration value in `sites/<site-name>/site_config.json` (e.g., `bench set-config developer_mode 1`).
*   **`bench console [--site <site-name>]`**: Starts a Python interpreter with the Frappe environment loaded for the specified site. Useful for debugging and running Frappe API commands interactively.

## Updates & Versioning

*   **`bench update [--pull] [--patch] [--build] [--bench-repo <url>] [--requirements] [--restart-supervisor]`**: Updates Frappe framework (bench) and all apps.
    *   `--pull`: Pulls latest changes from Git repositories.
    *   `--patch`: Runs patch scripts defined in apps.
    *   `--build`: Runs `bench build`.
    *   `--requirements`: Updates Python dependencies.
    *   `--restart-supervisor`: Restarts supervisor processes (if used for production).
*   **`bench switch-to-branch <branch-name> [<app-name>]`**: Switches the branch for Frappe framework and/or specified apps. Often used with `bench update` afterwards.
*   **`bench switch-to-develop` / `bench switch-to-master`**: Common shortcuts for switching branches.

## Testing

*   **`bench run-tests [--app <app-name>] [--doctype <doctype-name>] [--test <module.path.to.test>]`**: Runs automated tests (usually Python `unittest` based) for the specified app, DocType, or test module.

## Other

*   **`bench --help`**: Shows general help and available commands.
*   **`bench [command] --help`**: Shows help for a specific command.

Mastering the `bench` CLI is crucial for efficient Frappe development and site management.

*(Refer to the official Frappe Bench documentation and cheat sheet.)*