# Common Angular CLI Commands

A quick reference for frequently used Angular CLI commands. Use these with `execute_command`.

## Generating Code (`ng generate` or `ng g`)

*   **Component:** `ng generate component path/to/component-name [options]`
    *   *Options:* `--standalone` (recommended), `--skip-tests`, `--module=[module-name]` (if not standalone), `--prefix=[prefix]`
    *   *Example:* `ng generate component features/user-profile --standalone`
*   **Service:** `ng generate service path/to/service-name [options]`
    *   *Options:* `--skip-tests`
    *   *Example:* `ng generate service core/auth/auth`
*   **Module (Less common with standalone):** `ng generate module module-name [options]`
    *   *Options:* `--routing` (creates routing module), `--module=[parent-module]` (adds to parent imports)
    *   *Example:* `ng generate module features/admin --routing --module=app`
*   **Directive:** `ng generate directive path/to/directive-name [options]`
    *   *Options:* `--standalone` (recommended), `--skip-tests`
    *   *Example:* `ng generate directive shared/directives/highlight --standalone`
*   **Pipe:** `ng generate pipe path/to/pipe-name [options]`
    *   *Options:* `--standalone` (recommended), `--skip-tests`
    *   *Example:* `ng generate pipe shared/pipes/custom-date --standalone`
*   **Guard:** `ng generate guard path/to/guard-name [options]`
    *   *Options:* `--implements=CanActivate` (or other interfaces)
    *   *Example:* `ng generate guard core/auth/auth --implements=CanActivate`
*   **Interceptor:** `ng generate interceptor path/to/interceptor-name [options]`
    *   *Options:* `--functional` (recommended)
    *   *Example:* `ng generate interceptor core/http/auth --functional`
*   **Enum:** `ng generate enum path/to/enum-name`
*   **Interface:** `ng generate interface path/to/interface-name`
*   **Class:** `ng generate class path/to/class-name`

## Running the Application (`ng serve` or `ng s`)

*   **Serve:** `ng serve [options]`
    *   *Options:* `-o` or `--open` (opens browser), `--port [port-number]`
    *   *Example:* `ng serve -o`

## Building the Application (`ng build` or `ng b`)

*   **Build:** `ng build [options]`
    *   *Options:* `--configuration=production` (or other build target), `--output-path [path]`
    *   *Example:* `ng build --configuration=production`

## Running Tests (`ng test`)

*   **Unit Tests:** `ng test [options]` (Runs Karma/Jasmine tests)
    *   *Options:* `--no-watch` (run once), `--code-coverage`
    *   *Example:* `ng test --no-watch --code-coverage`
*   **End-to-End Tests:** `ng e2e [options]` (Runs Protractor/Cypress/etc. depending on setup)
    *   *Example:* `ng e2e`

## Other Useful Commands

*   **Help:** `ng help`, `ng generate --help`, `ng build --help`
*   **Update:** `ng update @angular/core @angular/cli` (Check official update guide first: update.angular.io)
*   **Add:** `ng add @angular/material` (Adds libraries with schematics)

*(Always refer to the official Angular CLI documentation (`ng help [command]`) for the most up-to-date commands and options.)*