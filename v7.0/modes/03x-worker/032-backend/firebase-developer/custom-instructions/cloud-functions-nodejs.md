# Firebase: Cloud Functions (Node.js / TypeScript)

Developing serverless backend logic using Cloud Functions for Firebase with Node.js and TypeScript.

## Core Concept

Cloud Functions allow you to run backend code in a managed Node.js environment without provisioning or managing servers. You write functions that respond to specific triggers (HTTP requests, Firebase events, etc.).

## Setup (Node.js/TypeScript)

1.  **Initialize Firebase Project:** If not already done, run `firebase init functions` in your project directory.
2.  **Choose Language:** Select TypeScript or JavaScript. TypeScript is highly recommended for type safety and better tooling.
3.  **Install Dependencies:** `cd functions` and run `npm install` (or `yarn`). Install the Firebase SDKs: `npm install firebase-functions firebase-admin` (or `yarn add ...`).
4.  **Project Structure:**
    ```
    your-project/
    ├── firebase.json
    ├── firestore.rules
    ├── storage.rules
    └── functions/
        ├── src/
        │   └── index.ts    # Your main functions file (TypeScript)
        ├── lib/            # Output directory for compiled JS (from TS)
        ├── node_modules/
        ├── package.json
        └── tsconfig.json   # TypeScript configuration
    ```
5.  **`index.ts` (or `index.js`):** This is where you define and export your functions.
6.  **TypeScript Compilation:** If using TypeScript, the `firebase deploy` command (or `npm run build` if configured in `package.json`) will compile your `.ts` files in `src/` to JavaScript files in `lib/`. Firebase deploys the compiled JavaScript.

## Defining Functions (`functions/src/index.ts`)

*   **Import SDKs:**
    ```typescript
    import * as functions from "firebase-functions"; // Core functions module
    import * as admin from "firebase-admin"; // Admin SDK for backend access

    // Initialize Admin SDK (only once)
    admin.initializeApp();

    // Get Firestore instance from Admin SDK
    const db = admin.firestore();
    ```
*   **Export Functions:** Each function you want to deploy must be exported.

### HTTPS Functions

```typescript
// HTTP Request Function (Express-like)
export const helloWorld = functions.https.onRequest((request, response) => {
  functions.logger.info("Hello logs!", {structuredData: true}); // Structured logging
  response.send("Hello from Firebase!");
});

// Callable Function (Recommended for client calls)
export const addMessage = functions.https.onCall(async (data, context) => {
  // Check authentication (context.auth is populated automatically)
  if (!context.auth) {
    throw new functions.https.HttpsError('unauthenticated', 'The function must be called while authenticated.');
  }
  const text = data.text; // Data sent from client SDK
  const uid = context.auth.uid;

  // Basic validation
  if (!(typeof text === 'string') || text.length === 0) {
    throw new functions.https.HttpsError('invalid-argument', 'The function must be called with one arguments "text" containing the message text to add.');
  }

  try {
    // Write message to Firestore using Admin SDK
    const writeResult = await db.collection('messages').add({
        text: text,
        authorId: uid,
        timestamp: admin.firestore.FieldValue.serverTimestamp(), // Use server timestamp
    });
    return { result: `Message with ID: ${writeResult.id} added.` };
  } catch (error) {
    functions.logger.error("Error adding message:", error);
    throw new functions.https.HttpsError('unknown', 'Failed to add message', error);
  }
});
```

### Background Triggers (Example: Firestore `onCreate`)

```typescript
// Triggered when a new document is created in 'users' collection
export const sendWelcomeEmail = functions.firestore
    .document('users/{userId}') // Wildcard for userId
    .onCreate(async (snap, context) => {
        const newUser = snap.data(); // Data of the new document
        const userId = context.params.userId; // Access wildcard value

        const email = newUser.email;
        const displayName = newUser.displayName || 'New User';

        functions.logger.log(`New user created: ${userId}, Email: ${email}`);

        // Example: Send email using Firebase Extensions (e.g., Trigger Email)
        // Or use a third-party service like SendGrid/Mailgun via their Node.js SDK
        try {
            // Placeholder for email sending logic
            await db.collection('mail').add({
                to: email,
                message: {
                  subject: `Welcome, ${displayName}!`,
                  text: `Thanks for signing up!`,
                  // html: '...',
                },
              });
            functions.logger.log('Welcome email queued for', email);
        } catch (error) {
            functions.logger.error('Error sending welcome email:', error);
        }
        return null; // Return value often ignored for background triggers
    });

// Example: Auth trigger
export const userCleanup = functions.auth.user().onDelete(async (user) => {
    const uid = user.uid;
    functions.logger.log(`Cleaning up data for deleted user: ${uid}`);
    // Example: Delete user's Firestore profile
    await db.collection('users').doc(uid).delete();
    // Example: Delete user's files in Storage (requires more complex logic)
});
```

## Firebase Admin SDK

*   **Purpose:** Allows your backend code (Cloud Functions) to interact with Firebase services with **full administrative privileges**, bypassing security rules.
*   **Initialization:** `admin.initializeApp()` (usually done once at the top level).
*   **Usage:** Access services like `admin.firestore()`, `admin.auth()`, `admin.storage()`. The API is similar but distinct from the client-side SDKs.

## Deployment

*   **Command:** `firebase deploy --only functions` (or just `firebase deploy`).
*   **Process:** Deploys the compiled JavaScript code from your `lib` directory (if using TypeScript) or your source directory (if using JavaScript).

## Local Development & Testing (Emulator Suite)

*   **Command:** `firebase emulators:start --only functions,firestore,auth` (include emulators for services your functions interact with).
*   **Benefits:** Test functions locally without deploying, faster iteration, no real costs incurred. Trigger background functions by interacting with the emulated services (e.g., create a document in the Firestore emulator UI). Call HTTPS functions via their local URL.

## Best Practices

*   **Idempotency:** Design background functions (especially event-triggered ones) to be idempotent where possible (running them multiple times with the same input produces the same result). Firebase guarantees "at-least-once" delivery for most background triggers.
*   **Region:** Specify the region for your functions (`functions.region('europe-west1')...`) to deploy them closer to your users or database location.
*   **Runtime Options:** Configure memory allocation and timeout for functions (`functions.runWith({timeoutSeconds: 120, memory: '1GB'})...`).
*   **Error Handling:** Implement robust error handling and logging (`functions.logger`).
*   **Security:** Remember the Admin SDK bypasses security rules. Ensure your function logic includes necessary validation and authorization checks if needed. For callable functions, check `context.auth`.
*   **Dependencies:** Manage `package.json` dependencies carefully. Avoid unnecessary large dependencies.
*   **Cold Starts:** Be aware of cold start latency. Keep functions focused and minimize initialization time. Consider setting minimum instances for latency-sensitive functions (incurs cost).

*(Refer to the official Cloud Functions documentation: https://firebase.google.com/docs/functions)*