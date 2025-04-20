# Firebase: Web SDK v9 (Modular)

Using the modern, tree-shakable Firebase Web SDK (version 9 and later).

## Core Concept: Modularity

The v9 Web SDK introduced a modular, function-based approach (`firebase/app`, `firebase/auth`, `firebase/firestore`, etc.). This contrasts with the v8 SDK's namespaced, class-based approach (`firebase.auth()`, `firebase.firestore()`).

**Benefits of v9 Modular SDK:**
*   **Tree Shaking:** Build tools (like Webpack, Rollup, Vite) can remove unused code from the Firebase SDK, significantly reducing your application's bundle size. You only import the functions you actually need.
*   **Improved Readability (Subjective):** Function-based approach can sometimes feel more aligned with modern JavaScript patterns.

## Initialization

*   Import `initializeApp` from `firebase/app`.
*   Import `getService` functions (e.g., `getAuth`, `getFirestore`) from the specific service modules.
*   Call `initializeApp` once with your config.
*   Call `getService` functions, passing the initialized `app` instance.

```javascript
// src/firebase.js (or similar config file)
import { initializeApp } from 'firebase/app';
// Import ONLY the services you need
import { getAuth } from 'firebase/auth';
import { getFirestore } from 'firebase/firestore';
import { getStorage } from 'firebase/storage';
// import { getAnalytics } from "firebase/analytics"; // Example: Optional service

const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_AUTH_DOMAIN",
  projectId: "YOUR_PROJECT_ID",
  storageBucket: "YOUR_STORAGE_BUCKET",
  messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
  appId: "YOUR_APP_ID"
  // measurementId: "YOUR_MEASUREMENT_ID" // Optional: For Analytics
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Get service instances (only get what you need)
const auth = getAuth(app);
const db = getFirestore(app);
const storage = getStorage(app);
// const analytics = getAnalytics(app); // Optional

// Export the instances for use in your app
export { auth, db, storage /*, analytics */ };
```

## Using Service Functions

*   Import specific functions directly from the service modules (e.g., `import { collection, addDoc } from 'firebase/firestore';`).
*   Call these functions, passing the service instance (e.g., `auth`, `db`, `storage`) as the first argument.

**Example (Firestore):**

```javascript
// Previous (v8):
// firebase.firestore().collection('users').doc(userId).set({ name: 'Alice' });

// Modular (v9+):
import { doc, setDoc } from 'firebase/firestore';
import { db } from './firebase'; // Import initialized db instance

async function updateUser(userId, data) {
  const userRef = doc(db, 'users', userId); // Get DocumentReference
  await setDoc(userRef, data, { merge: true }); // Pass db instance first
}
```

**Example (Authentication):**

```javascript
// Previous (v8):
// firebase.auth().signInWithEmailAndPassword(email, password);

// Modular (v9+):
import { signInWithEmailAndPassword } from 'firebase/auth';
import { auth } from './firebase'; // Import initialized auth instance

async function signIn(email, password) {
  await signInWithEmailAndPassword(auth, email, password); // Pass auth instance first
}
```

**Example (Storage):**

```javascript
// Previous (v8):
// firebase.storage().ref('images/pic.jpg').put(file);

// Modular (v9+):
import { ref, uploadBytes } from 'firebase/storage';
import { storage } from './firebase'; // Import initialized storage instance

async function uploadImage(file) {
  const storageRef = ref(storage, 'images/' + file.name); // Pass storage instance first
  await uploadBytes(storageRef, file);
}
```

## Key Differences from v8

*   **Imports:** Import functions directly from service modules (`firebase/<service>`) instead of accessing methods on the `firebase` namespace.
*   **Function Calls:** Pass the service instance (`auth`, `db`, `storage`) as the first argument to most functions.
*   **Tree Shakable:** Only the code for the functions you import is included in your final bundle.

## Compatibility (`compat` libraries)

Firebase provides compatibility libraries (`firebase/compat/app`, `firebase/compat/auth`, etc.) that allow you to use the older v8 syntax while benefiting partially from the v9 modular structure under the hood. This can be useful for gradual migration.

```javascript
// Using compat libraries (v8 syntax)
import firebase from 'firebase/compat/app';
import 'firebase/compat/auth';
import 'firebase/compat/firestore';

const firebaseConfig = { /* ... */ };
firebase.initializeApp(firebaseConfig);

const auth = firebase.auth();
const db = firebase.firestore();

// Now use v8 syntax
auth.signInWithEmailAndPassword(email, password);
db.collection('users').doc(userId).set({ name: 'Alice' });
```

**Recommendation:** For new projects or major refactors, use the fully modular v9+ syntax to get the maximum bundle size reduction benefits. Use the `compat` libraries primarily as a temporary step during migration.

*(Refer to the official Firebase Web v9 Upgrade Guide: https://firebase.google.com/docs/web/modular-upgrade)*