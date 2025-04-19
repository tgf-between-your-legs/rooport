# Custom Instructions: Secure Key Management

## Core Concept: API Keys

Clerk uses two main keys to connect your application to your Clerk instance:

1.  **Publishable Key:**
    *   **Purpose:** Used in your frontend code (e.g., within `<ClerkProvider>`). It's safe to expose this key in client-side browser code.
    *   **Format:** Starts with `pk_test_...` (for development) or `pk_live_...` (for production).
    *   **Environment Variable Name:** Conventionally `NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY` (for Next.js) or `VITE_CLERK_PUBLISHABLE_KEY` (for Vite), or a similar framework-specific public variable name. The `NEXT_PUBLIC_` or `VITE_` prefix makes it available in the browser bundle.
2.  **Secret Key:**
    *   **Purpose:** Used in your backend code (middleware, API routes, server components, server actions) to authenticate requests and interact with the Clerk Backend API. **This key must be kept secret and never exposed to the client-side.**
    *   **Format:** Starts with `sk_test_...` (for development) or `sk_live_...` (for production).
    *   **Environment Variable Name:** Conventionally `CLERK_SECRET_KEY`.

## Setup using Environment Variables (`.env`)

The standard and recommended way to manage these keys is through environment variables.

1.  **Create `.env.local` file:** In the root of your project, create a file named `.env.local` (this file should typically be listed in your `.gitignore` file to prevent committing secrets).
2.  **Add Keys:** Get your keys from your Clerk Dashboard (Development or Production instance) under "API Keys". Add them to the `.env.local` file using the conventional names for your framework:

    ```dotenv
    # .env.local (Example for Next.js)
    # DO NOT COMMIT THIS FILE TO VERSION CONTROL

    # Frontend Key (Safe to expose)
    NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=pk_test_YOUR_PUBLISHABLE_KEY_HERE

    # Backend Key (Keep Secret!)
    CLERK_SECRET_KEY=sk_test_YOUR_SECRET_KEY_HERE

    # Optional: For configuring webhook signing secret
    # CLERK_WEBHOOK_SECRET=whsec_...
    ```

    *   **Note:** Replace `NEXT_PUBLIC_` with `VITE_` or the appropriate prefix for your specific framework if not using Next.js. The secret key variable name (`CLERK_SECRET_KEY`) is generally consistent.

3.  **Access Keys in Code:**
    *   **Frontend (Client-side):** Access the publishable key using the framework's mechanism for exposing public environment variables.
        *   **Next.js:** `process.env.NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY`
        *   **Vite (React/Vue/etc.):** `import.meta.env.VITE_CLERK_PUBLISHABLE_KEY`
        *   Pass this key to `<ClerkProvider publishableKey={...}>`.
    *   **Backend (Server-side):** Access the secret key (and publishable key if needed) using standard Node.js `process.env`. Clerk's backend SDKs and middleware often read `CLERK_SECRET_KEY` automatically if set.
        *   `process.env.CLERK_SECRET_KEY`
        *   `process.env.NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY`

4.  **Deployment:** When deploying your application, ensure these environment variables (`CLERK_PUBLISHABLE_KEY` / `NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY` and `CLERK_SECRET_KEY`) are securely set in your hosting provider's environment variable configuration (e.g., Vercel Environment Variables, Netlify Build Environment Variables). **Do not hardcode keys directly in your source code.**

## Security Best Practices

*   **NEVER** commit your `CLERK_SECRET_KEY` or files containing it (like `.env.local`) to version control (Git). Add `.env*` (or specifically `.env.local`) to your `.gitignore` file.
*   Use distinct Development and Production keys from your Clerk dashboard for different environments.
*   Rotate keys if you suspect they have been compromised.
*   Ensure your deployment environment securely stores and provides these variables to your application.

Properly managing API keys using environment variables is crucial for the security of your Clerk integration.