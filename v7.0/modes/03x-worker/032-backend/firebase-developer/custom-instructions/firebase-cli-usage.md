# Firebase: CLI Usage

Common commands for the Firebase Command Line Interface (CLI).

## Core Concept

The Firebase CLI (`firebase`) is an essential tool for managing Firebase projects, deploying code and assets, running local emulators, and interacting with various Firebase services from your terminal.

## Installation & Login

1.  **Installation:** Install globally using npm:
    ```bash
    npm install -g firebase-tools
    ```
2.  **Login:** Log in to your Google account:
    ```bash
    firebase login
    ```
    (Follow the browser prompts). Use `firebase login --reauth` if needed. Use `firebase logout` to sign out.

## Project Management

*   **`firebase projects:list`**: List all Firebase projects associated with your logged-in account.
*   **`firebase use <project_id_or_alias>`**: Set the active Firebase project for the current directory. Project aliases can be set in the `.firebaserc` file.
    *   `firebase use --add`: Interactively select a project and assign an alias (e.g., `default`, `staging`, `production`).
*   **`.firebaserc` File:** Stores project aliases for the current directory structure.
    ```json
    {
      "projects": {
        "default": "my-dev-project-id",
        "production": "my-prod-project-id"
      }
    }
    ```

## Initialization

*   **`firebase init`**: Initialize Firebase features in your project directory. Creates `firebase.json` and potentially other configuration files (`.rules`, `.indexes.json`).
    *   Prompts you to select features (Firestore, Functions, Hosting, Storage, Emulators, etc.).
    *   Asks configuration questions (e.g., public directory for Hosting, language for Functions, Firestore rules file).

## Emulators (Local Development & Testing)

*   **`firebase emulators:start`**: Start the local Firebase Emulator Suite based on the configuration in `firebase.json`.
    *   **Flags:**
        *   `--only functions,firestore,auth`: Start only specific emulators.
        *   `--import=./my-export-data`: Import data saved from a previous emulator session.
        *   `--export-on-exit=./my-export-data`: Export emulator data on shutdown (Ctrl+C).
*   **Emulator UI:** Access the Emulator Suite UI (usually at `http://localhost:4000`) to view data, logs, and trigger functions.
*   **Configuration (`firebase.json`):** Define emulator ports and settings.
    ```json
    {
      "emulators": {
        "auth": { "port": 9099 },
        "functions": { "port": 5001 },
        "firestore": { "port": 8080 },
        "storage": { "port": 9199 },
        "pubsub": { "port": 8085 },
        "hosting": { "port": 5000 },
        "ui": { "enabled": true, "port": 4000 }
      }
    }
    ```

## Deployment

*   **`firebase deploy`**: Deploys code and configuration based on `firebase.json`.
    *   **Flags:**
        *   `--only hosting`: Deploy only Hosting assets and configuration.
        *   `--only functions`: Deploy only Cloud Functions.
        *   `--only firestore:rules`: Deploy only Firestore security rules.
        *   `--only storage:rules`: Deploy only Storage security rules.
        *   `--only hosting:<target_name>`: Deploy a specific hosting target (for multi-site setups).
        *   `-P <project_id_or_alias>` or `--project <project_id_or_alias>`: Specify the target project, overriding the active one set by `firebase use`.
        *   `--message "Deployment message"`: Add a message to the deployment record.
*   **Hosting Channels:** Deploy to preview channels: `firebase hosting:channel:deploy <channel_id>`.

## Cloud Functions Specific

*   **`firebase functions:log`**: View logs for deployed Cloud Functions.
*   **`firebase functions:config:set my_service.key="value" my_service.secret="shh"`**: Set environment configuration for functions (use for non-sensitive config or retrieve secrets securely within the function).
*   **`firebase functions:config:get`**: View current function configuration.
*   **`firebase functions:delete <functionName>`**: Delete specific deployed functions.

## Database Specific (Firestore)

*   **`firebase firestore:indexes`**: View and manage Firestore composite indexes based on `firestore.indexes.json`.
*   **`firebase firestore:delete [path]`**: Delete Firestore documents or collections (use with extreme caution, especially in production). Add `--recursive` for collections.

## Hosting Specific

*   **`firebase hosting:disable`**: Disable Firebase Hosting for the project.
*   **`firebase hosting:channel:create <channel_id>`**: Create a preview channel.
*   **`firebase hosting:channel:list`**: List active channels.

This CLI is fundamental for managing the Firebase development lifecycle.

*(Refer to the official Firebase CLI Reference: https://firebase.google.com/docs/cli)*