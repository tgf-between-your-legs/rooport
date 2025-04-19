# Firebase: Cloud Functions Triggers

Understanding the different ways Cloud Functions can be triggered.

## Core Concept

Cloud Functions for Firebase allow you to run backend code automatically in response to events emitted by Firebase services or direct HTTP requests. You don't need to manage servers; Firebase handles the scaling and execution environment.

## Trigger Types

1.  **HTTPS Triggers:**
    *   **`onRequest` (HTTP Functions):**
        *   **Trigger:** Standard HTTP requests (GET, POST, PUT, DELETE, etc.) to a unique URL provided by Firebase upon deployment.
        *   **Use Case:** Building REST APIs, webhooks, serving dynamic HTML.
        *   **Handler Signature (Node.js):** Receives `request` (Express.js-like Request object) and `response` (Express.js-like Response object).
        *   **Handler Signature (Python):** Receives a Flask Request object. Must return a Flask Response object or compatible value.
    *   **`onCall` (Callable Functions):**
        *   **Trigger:** Direct calls from your client app using the Firebase client SDKs (`https://firebase.google.com/docs/functions/callable`).
        *   **Use Case:** RPC-style calls from your frontend where authentication context and data validation are automatically handled.
        *   **Handler Signature (Node.js):** Receives `data` (deserialized data sent from client) and `context` (includes `context.auth` with user info if authenticated). Must return a JSON-serializable object or a Promise resolving to one.
        *   **Handler Signature (Python):** Receives a `CallableRequest` object containing `data` and `auth`. Must return a JSON-serializable object.
        *   **Benefits:** Automatically deserializes request body, validates auth tokens, handles CORS. Simpler client-side invocation compared to standard HTTPS functions.

2.  **Background Triggers (Event-Driven):**
    *   Run in response to events happening in other Firebase or Google Cloud services.
    *   **Authentication Triggers (`functions.auth`):**
        *   `user().onCreate()`: Triggered when a new Firebase Auth user is created.
        *   `user().onDelete()`: Triggered when a Firebase Auth user is deleted.
        *   **Use Case:** Create user profile in Firestore, send welcome email, clean up user data.
        *   **Handler Signature:** Receives `user` (UserRecord object).
    *   **Firestore Triggers (`functions.firestore`):**
        *   `document().onCreate()`: Triggered when a document is created.
        *   `document().onUpdate()`: Triggered when a document is updated.
        *   `document().onDelete()`: Triggered when a document is deleted.
        *   `document().onWrite()`: Triggered on create, update, or delete.
        *   **Path Specification:** Use wildcards (`{userId}`, `{documentId}`) to specify which documents trigger the function (e.g., `functions.firestore.document('users/{userId}')`).
        *   **Use Case:** Denormalize data, aggregate values, send notifications on data changes, enforce complex validation.
        *   **Handler Signature:** Receives `change` (for `onUpdate`/`onWrite`, has `before` and `after` snapshots) or `snap` (for `onCreate`/`onDelete`), and `context` (includes event ID, timestamp, path parameters).
    *   **Cloud Storage Triggers (`functions.storage`):**
        *   `object().onArchive()`: Triggered when an object is archived (versioning enabled).
        *   `object().onDelete()`: Triggered when an object is permanently deleted.
        *   `object().onFinalize()`: Triggered when a new object is successfully created/uploaded (including overwrites). **(Most common)**.
        *   `object().onMetadataUpdate()`: Triggered when an object's metadata changes.
        *   **Bucket Specification:** Can target the default bucket or a specific one (`functions.storage.bucket('my-bucket').object()`).
        *   **Use Case:** Generate image thumbnails, process uploaded files, update Firestore with file metadata.
        *   **Handler Signature:** Receives `object` (Storage Object metadata) and `context`.
    *   **Pub/Sub Triggers (`functions.pubsub`):**
        *   `topic().onPublish()`: Triggered when a message is published to a Google Cloud Pub/Sub topic.
        *   **Use Case:** Decoupled event handling, processing asynchronous tasks.
        *   **Handler Signature:** Receives `message` (Pub/Sub message object) and `context`.
    *   **Scheduled Triggers (`functions.pubsub.schedule().onRun()`):**
        *   **Trigger:** Runs on a defined schedule (using App Engine cron syntax).
        *   **Use Case:** Recurring cleanup tasks, generating reports, sending scheduled notifications.
        *   **Handler Signature:** Receives `context`.

## Choosing Triggers

*   Use **HTTPS `onRequest`** for standard web APIs or webhooks.
*   Use **HTTPS `onCall`** for direct, authenticated calls from your client app.
*   Use **Background Triggers** for reacting to events within Firebase/GCP services automatically.
*   Use **Scheduled Triggers** for recurring tasks.

*(Refer to the official Cloud Functions documentation for trigger types: https://firebase.google.com/docs/functions/triggers)*