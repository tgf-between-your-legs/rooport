# Firebase: Cloud Functions (Python)

Developing serverless backend logic using Cloud Functions for Firebase with Python.

## Core Concept

Cloud Functions allow you to run backend code in a managed Python environment without provisioning or managing servers. You write functions that respond to specific triggers (HTTP requests, Firebase events, etc.).

## Setup (Python)

1.  **Initialize Firebase Project:** If not already done, run `firebase init functions` in your project directory.
2.  **Choose Language:** Select Python.
3.  **Install Dependencies:** Firebase CLI sets up a virtual environment (`venv`) and installs initial dependencies (`firebase-functions`, `firebase-admin`) listed in `functions/requirements.txt`. Activate the virtual environment (`source venv/bin/activate`) and install additional dependencies using `pip install <package_name>`.
4.  **Project Structure:**
    ```
    your-project/
    ├── firebase.json
    ├── firestore.rules
    ├── storage.rules
    └── functions/
        ├── main.py         # Your main functions file
        ├── requirements.txt # Python dependencies
        └── venv/           # Virtual environment (usually gitignored)
    ```
5.  **`main.py`:** This is where you define and export your functions using decorators.

## Defining Functions (`functions/main.py`)

*   **Import SDKs:**
    ```python
    # Required for all functions
    from firebase_functions import options, https_fn, firestore_fn, storage_fn, auth_fn, pubsub_fn # Import specific trigger modules
    from firebase_admin import initialize_app, firestore, auth, storage # Admin SDK

    # Initialize Admin SDK (only once)
    initialize_app()

    # Set region globally (optional, can also be set per function)
    options.set_global_options(region=options.SupportedRegion.EUROPE_WEST1)

    # Get Firestore client from Admin SDK
    db = firestore.client()
    ```
*   **Define Functions with Decorators:** Use decorators from the imported trigger modules (`@https_fn`, `@firestore_fn`, etc.) to define your functions.

### HTTPS Functions

```python
# HTTP Request Function (Flask-like Request object)
@https_fn.on_request()
def hello_world(req: https_fn.Request) -> https_fn.Response:
    """Handles HTTP GET requests."""
    print("Received request:", req.method, req.path) # Logging
    # Access query params: req.args.get('name')
    # Access JSON body: req.get_json(silent=True)
    # Access form data: req.form.get('field')
    return https_fn.Response("Hello from Firebase (Python)!")

# Callable Function (Recommended for client calls)
@https_fn.on_call()
def add_message(req: https_fn.CallableRequest) -> dict:
    """Handles callable requests from client SDKs."""
    # Check authentication (req.auth is populated automatically)
    if req.auth is None:
        raise https_fn.HttpsError(
            code=https_fn.FunctionsErrorCode.UNAUTHENTICATED,
            message="The function must be called while authenticated."
        )

    text = req.data.get("text") # Data sent from client
    uid = req.auth.uid

    # Basic validation
    if not isinstance(text, str) or len(text) == 0:
        raise https_fn.HttpsError(
            code=https_fn.FunctionsErrorCode.INVALID_ARGUMENT,
            message='The function must be called with one argument "text".'
        )

    try:
        # Write message to Firestore using Admin SDK
        doc_ref = db.collection('messages').add({
            'text': text,
            'authorId': uid,
            'timestamp': firestore.SERVER_TIMESTAMP # Use server timestamp
        })
        return {"result": f"Message with ID: {doc_ref[1].id} added."}
    except Exception as e:
        print(f"Error adding message: {e}")
        raise https_fn.HttpsError(
            code=https_fn.FunctionsErrorCode.UNKNOWN,
            message="Failed to add message."
        )
```

### Background Triggers (Example: Firestore `onCreate`)

```python
# Triggered when a new document is created in 'users' collection
# Use firestore_fn.Event and firestore_fn.Change for type hints
@firestore_fn.on_document_created(document="users/{userId}")
def send_welcome_email(event: firestore_fn.Event[firestore_fn.Change]) -> None:
    """Sends a welcome email when a new user document is created."""
    user_id = event.params['userId'] # Access wildcard value
    new_user_data = event.data.to_dict() if event.data else {} # Data of the new document

    email = new_user_data.get('email')
    display_name = new_user_data.get('displayName', 'New User')

    if not email:
        print(f"No email found for user {user_id}. Cannot send welcome email.")
        return

    print(f"New user created: {user_id}, Email: {email}")

    # Example: Send email using Firebase Extensions (e.g., Trigger Email)
    # Or use a third-party service like SendGrid/Mailgun via their Python SDK
    try:
        # Placeholder for email sending logic (e.g., add to 'mail' collection for Trigger Email extension)
        db.collection('mail').add({
            'to': [email],
            'message': {
              'subject': f'Welcome, {display_name}!',
              'text': 'Thanks for signing up!',
              # 'html': '...',
            },
          })
        print(f'Welcome email queued for {email}')
    except Exception as e:
        print(f'Error queuing welcome email: {e}')

# Example: Auth trigger
@auth_fn.on_user_deleted()
def user_cleanup(event: auth_fn.AuthUserRecord) -> None:
    """Cleans up user data when an auth user is deleted."""
    uid = event.data.uid
    print(f"Cleaning up data for deleted user: {uid}")
    # Example: Delete user's Firestore profile
    db.collection('users').document(uid).delete()
    # Example: Delete user's files in Storage (requires storage client)
```

## Firebase Admin SDK (Python)

*   **Purpose:** Allows backend code to interact with Firebase services with admin privileges.
*   **Initialization:** `initialize_app()` (usually once).
*   **Usage:** Access services via modules like `firestore`, `auth`, `storage`.

## Deployment

*   **Command:** `firebase deploy --only functions` (or `firebase deploy`).
*   **Process:** Packages your code in `functions/` along with `requirements.txt` dependencies and deploys it to the Cloud Functions environment.

## Local Development & Testing (Emulator Suite)

*   **Command:** `firebase emulators:start --only functions,firestore,auth` (include relevant emulators).
*   **Benefits:** Test locally without deployment, faster iteration. Trigger background functions via emulator interactions. Call HTTPS functions via their local URL.

## Best Practices

*   **Idempotency:** Design background functions to be idempotent.
*   **Region:** Specify function regions (`options.set_global_options` or per-function decorator argument).
*   **Runtime Options:** Configure memory/timeout via decorator arguments (`@https_fn.on_request(memory=options.MemoryOption.MB_512, timeout_sec=120)`).
*   **Error Handling:** Use `try...except` blocks. Raise `https_fn.HttpsError` for callable functions. Log errors effectively.
*   **Security:** Validate data, check authentication (`req.auth` in callable, `event.auth` in some triggers), be mindful of Admin SDK privileges.
*   **Dependencies:** Manage dependencies in `requirements.txt`.

*(Refer to the official Cloud Functions for Firebase Python documentation: https://firebase.google.com/docs/functions/write-firebase-functions)*