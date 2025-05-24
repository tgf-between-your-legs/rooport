# Examples: Using the Ultimate Agentic Coding Tool

This section provides practical examples of how to interact with the Ultimate Agentic Coding Tool (via Roo Commander) for various development tasks. Remember that the system operates autonomously, so your interaction is often about setting goals and observing/guiding rather than step-by-step commanding.

## Example 1: Starting a New Feature

**User Goal:** Implement a feature that allows users to upload a profile picture.

**Interaction with Roo Commander:**

```
User: Implement a new feature: User Profile Picture Upload.
      Users should be able to select a JPG or PNG image from their device,
      upload it, and it should display on their profile page.
      The image should be stored securely.
```

**Expected Autonomous Agentic Behavior (Simplified):**

1.  **Task Decomposition & Planning (Internal):**
    *   Roo Commander (using the Ultimate Agentic Orchestrator) understands the request.
    *   It might create an MDTM task for this feature.
    *   The Agentic RAG Engine searches ConPort for existing profile components, image handling utilities, security guidelines for file uploads, or relevant ADRs.
    *   The POE might identify risks (e.g., "No existing image validation library found") or opportunities (e.g., "Can reuse existing S3 storage integration").

2.  **Initial Implementation Steps (Autonomous):**
    *   Roo Commander might delegate to a frontend specialist mode to create UI components (file input, image preview).
    *   It might delegate to a backend specialist mode to create API endpoints for upload and image URL retrieval.
    *   Code for image validation (file type, size) and secure storage (e.g., uploading to a private S3 bucket, generating a signed URL for display) would be generated.

3.  **Proactive Feedback/Suggestions to User:**
    *   Roo Commander might report:
        *   "Started work on User Profile Picture Upload. Initial UI components for selection are drafted. Backend endpoint for upload is being designed."
        *   (POE Suggestion): "Consider adding image resizing on the backend to optimize storage and display performance. Current plan uses original image sizes."
        *   (CLS Insight, if applicable later): "Previous image upload features had issues with large file timeouts. Recommending client-side size validation before upload."

4.  **User Interaction (If Needed or for Refinement):**
    *   User: "Good point about resizing. Please add backend resizing to a maximum of 800x800 pixels."

5.  **Continued Autonomous Implementation & Testing:**
    *   The system incorporates the feedback and continues implementation.
    *   It might autonomously generate unit tests or suggest integration test scenarios.

6.  **Completion:**
    *   Roo Commander: "User Profile Picture Upload feature is complete. UI allows selection, backend handles upload, resizing, and secure storage. Profile page now displays the uploaded picture. Relevant ConPort entries updated."

## Example 2: Investigating a Performance Issue

**User Goal:** Diagnose why the dashboard page is loading slowly.

**Interaction with Roo Commander:**

```
User: The main dashboard page is loading very slowly, sometimes taking over 5 seconds.
      Can you investigate and identify the cause?
```

**Expected Autonomous Agentic Behavior (Simplified):**

1.  **Information Gathering (Agentic RAG):**
    *   Roo Commander uses the RAG engine to query ConPort for:
        *   Dashboard component code.
        *   Related API endpoints and their performance metrics (if logged).
        *   Recent changes to dashboard or related services.
        *   Known performance bottlenecks from past CLS reports.
        *   Relevant system patterns for performance optimization.

2.  **Analysis & Hypothesis Generation (POE & Orchestrator):**
    *   The POE might analyze the retrieved information.
    *   The Orchestrator might form hypotheses: "Is it a frontend rendering issue? A slow API call? Large data transfer?"

3.  **Diagnostic Actions (Autonomous, if safe):**
    *   If monitoring tools are integrated and accessible, it might query them for real-time metrics.
    *   It might analyze code complexity of dashboard components or backend API logic.
    *   *(Caution: Direct execution of performance profiling tools on production might be gated by safety rules, but it could analyze existing profiling data.)*

4.  **Reporting Findings & Suggestions:**
    *   Roo Commander:
        *   "Investigating dashboard performance. Initial analysis shows the `getUserActivity` API endpoint has an average response time of 3.5 seconds. This is a likely contributor."
        *   (RAG Insight): "The `getUserActivity` endpoint queries three large database tables without optimized indexing for the date range filter used by the dashboard."
        *   (POE Suggestion): "Recommend adding a composite index on `(user_id, activity_date)` to the `user_activities` table to improve `getUserActivity` query performance."
        *   (CLS Insight): "Previous performance optimizations on similar reporting queries benefited significantly from database indexing."

5.  **User Confirms/Guides:**
    *   User: "That makes sense. Please generate the SQL for adding that composite index and show me the relevant backend code for the `getUserActivity` endpoint."

6.  **Action & Further Investigation (Autonomous):**
    *   Roo Commander generates the SQL, shows the code.
    *   If the user approves, it might create an MDTM task for a database specialist to apply and test the index.
    *   It continues to monitor or suggest other potential optimizations if the first one isn't sufficient.

## Example 3: Understanding System Architecture

**User Goal:** Understand how authentication is handled in the project.

**Interaction with Roo Commander:**

```
User: Can you explain how user authentication is implemented in this project?
      What are the key components involved?
```

**Expected Autonomous Agentic Behavior (Simplified):**

1.  **Targeted RAG Retrieval:**
    *   Roo Commander uses the Agentic RAG Engine.
    *   The RAG engine queries ConPort specifically for:
        *   ADRs related to "authentication" or "security".
        *   System patterns tagged with "auth".
        *   Custom data in categories like "SecurityGuidelines" or "ServiceIntegrations" (if an external auth provider is used).
        *   Code files related to authentication (e.g., `authController.js`, `passportConfig.py`).

2.  **Information Synthesis:**
    *   The RAG engine synthesizes the information from multiple sources.
    *   It identifies key components (e.g., login API, token generation, session management, password hashing library, relevant database tables).
    *   It pieces together the flow from user login request to session establishment.

3.  **Comprehensive Explanation:**
    *   Roo Commander:
        *   "User authentication is handled via a token-based system. When a user logs in through the `/api/auth/login` endpoint, credentials are validated against the `users` table using bcrypt hashing."
        *   "Upon successful validation, a JWT (JSON Web Token) is generated by the `AuthTokenService` (see `authService.ts`). This token includes user ID and roles, and is signed with a secret key."
        *   "The token is returned to the client and must be included in the Authorization header for subsequent API requests."
        *   "Middleware in `apiMiddleware.ts` validates the token on protected routes."
        *   (POE Suggestion/Insight from ADR): "As per ADR-005, we plan to implement refresh tokens in Q3 to improve session longevity without compromising security. This is not yet implemented."
        *   (Link to ConPort): "For more details, see Decision ID: ADR-003 (Authentication Strategy)."

These examples illustrate how the Ultimate Agentic Coding Tool aims to provide a more intelligent, proactive, and context-aware development experience. The key is to communicate your goals clearly and allow the system to leverage its integrated AI capabilities.