# Frappe Specialist: Bench CLI Commands

The `bench` command-line interface is essential for managing Frappe environments, sites, and apps. Always run `bench` commands from the bench directory (e.g., `~/frappe-bench`). Use `execute_command` tool for these.

## 1. Site Management

*   `bench new-site [site-name]`: Creates a new site (database, config). Prompts for DB/admin details.
*   `bench use [site-name]`: Sets the default site for the current terminal session.
*   `bench set-default-site [site-name]`: Sets the default site globally for the bench.
*   `bench list-sites`: Lists all sites in the bench.
*   `bench drop-site [site-name]`: **Deletes** a site and its database (USE WITH EXTREME CAUTION).
*   `bench --site [site-name] [command]`: Runs a command specifically for one site without changing the default.

## 2. App Management

*   `bench get-app [git-url] [--branch branch-name]`: Downloads an app into the `apps/` directory.
*   `bench new-app [app-name]`: Creates a boilerplate structure for a new custom app.
*   `bench install-app [app-name] [--site site-name]`: Installs an app onto a site (runs migrations, hooks).
*   `bench uninstall-app [app-name] [--site site-name]`: Uninstalls an app from a site.
*   `bench remove-app [app-name]`: Removes app code from the `apps/` directory.

## 3. Database & Migrations

*   `bench migrate [--site site-name]`: Applies pending schema migrations based on DocType JSON changes. **Crucial after modifying DocTypes.**
*   `bench backup [--site site-name]`: Creates a database backup (and optionally files) in `sites/[site-name]/private/backups`.
*   `bench --site [site-name] restore [path-to-sql-backup]`: Restores a database backup.
*   `bench --site [site-name] mariadb` / `psql`: Opens a database shell for the site.

## 4. Process Management & Development

*   `bench start`: Starts development server (web server, workers, scheduler via `Procfile`). **For development only.**
*   `bench restart`: Restarts Frappe web workers (gunicorn/waitress). Needed after some config changes.
*   `bench build`: Compiles frontend assets (JS/CSS). **Required after changing client scripts or installing/updating apps.**
*   `bench watch`: Watches for asset changes and rebuilds automatically during development.
*   `bench set-config [key] [value] [--site site-name]`: Modifies `site_config.json` (e.g., `bench set-config developer_mode 1`).
*   `bench console [--site site-name]`: Starts a Python interpreter with Frappe context loaded. Useful for debugging.

## 5. Updates & Versioning

*   `bench update [--pull] [--patch] [--build] [--requirements]`: Updates bench, Frappe framework, and all apps.
    *   `--pull`: Fetches latest code from Git remotes.
    *   `--patch`: Runs patch scripts defined in apps.
    *   `--build`: Runs `bench build`.
    *   `--requirements`: Updates Python dependencies (`pip install -r requirements.txt`).
*   `bench switch-to-branch [branch-name] [app-name]`: Switches Git branch for bench/Frappe/apps. Follow with `bench update`.
*   `bench switch-to-develop` / `bench switch-to-master`: Common branch switching shortcuts.

## 6. Background Jobs & Scheduler (Production Focus)

*   `bench worker --queue short,default` / `bench worker --queue long`: Starts background worker processes listening to specific Redis queues.
*   `bench schedule`: Starts the scheduler process that enqueues jobs defined in `hooks.py`.
*   `bench setup supervisor`: Helps generate Supervisor config files to manage production processes (workers, scheduler, web server).
*   `bench setup nginx`: Helps generate Nginx config for reverse proxying.

## 7. Testing

*   `bench run-tests [--app app-name] [--doctype doctype-name] [--test module.path]`: Executes automated tests.

## 8. Other Useful Commands

*   `bench --help`: General help.
*   `bench [command] --help`: Help for a specific command.
*   `bench set-maintenance-mode [on|off] [--site site-name]`: Enable/disable maintenance mode for a site.

Always explain the purpose and potential impact of `bench` commands when using `execute_command`. Confirm success before proceeding with dependent steps (e.g., confirm `bench migrate` success before testing schema changes).