# Astro: Server Actions (`astro:actions`)

Defining and calling server-side functions securely from client-side code.

## Core Concept: Astro Actions

Astro Actions provide a type-safe way to define functions that run **only on the server** but can be called directly from your client-side JavaScript or Astro components, typically for handling form submissions or mutations. It simplifies the process of creating API endpoints for these specific use cases.

**Key Features:**

*   **Server-Side Execution:** Action code runs securely on the server, never exposed to the client.
*   **Type Safety:** Define input schemas using Zod and get type inference for arguments and return values on both client and server.
*   **Progressive Enhancement:** Works seamlessly with standard HTML forms. If JavaScript is disabled or fails, the form submission still works via standard HTTP POST.
*   **Simplified API:** Reduces the boilerplate of creating separate API routes for form handling.
*   **Context Access:** Actions have access to API context (cookies, locals set by middleware).

## Setup

1.  **Enable Experimental Actions Flag (If needed):** In older Astro versions, you might need to enable the experimental flag in `astro.config.mjs`:
    ```javascript
    // astro.config.mjs
    export default defineConfig({
      // ...
      experimental: {
        actions: true
      }
    });
    ```
    *(Check current Astro docs if this flag is still required)*
2.  **Create `src/actions/index.ts` (or `.js`):** This is the conventional location to define your server actions.

## Defining Actions (`src/actions/index.ts`)

*   Import `defineAction` from `astro:actions`.
*   Import schema helpers (`z`) from `astro:actions` (re-exported from Zod).
*   Define an `actions` object where each key is the action name (used for calling) and the value is the result of `defineAction`.
*   Inside `defineAction`:
    *   `input`: Define the expected input arguments using a Zod schema (`z.object({...})`).
    *   `handler`: An async function that receives `{ args, context }`.
        *   `args`: The validated input arguments, matching the `input` schema.
        *   `context`: API context (includes `cookies`, `locals`, `request`, etc.).
        *   Perform server-side logic (database operations, API calls, etc.).
        *   Return a result object or throw an error. **Important:** Perform all necessary **server-side validation and authorization** within the handler.

```typescript
// src/actions/index.ts
import { defineAction, z } from 'astro:actions';
import { db, User, eq } from 'astro:db'; // Example using Astro DB

export const server = { // Exported object MUST be named 'server'
  // --- Example: User Login Action ---
  login: defineAction({
    // Define expected input arguments with Zod schema
    input: z.object({
      email: z.string().email(),
      password: z.string().min(6),
    }),
    // The handler runs on the server
    handler: async ({ email, password }, { cookies, redirect }) => {
      console.log('Login action running on server for:', email);

      // --- IMPORTANT: Implement actual authentication logic here ---
      // 1. Find user by email
      // const user = await db.select().from(User).where(eq(User.email, email)).first();
      // 2. Verify password (using a secure hashing library like bcrypt/argon2)
      // const passwordIsValid = user && await verifyPassword(password, user.passwordHash);
      const passwordIsValid = (email === 'test@example.com' && password === 'password'); // Placeholder logic
      const user = passwordIsValid ? { id: 1, name: 'Test User', email } : null; // Placeholder user

      if (!passwordIsValid || !user) {
        // Use standard ActionError for expected failures
        // throw new ActionError({ code: 'UNAUTHORIZED', message: 'Invalid email or password' });
        return { success: false, message: 'Invalid email or password' }; // Or return structured error
      }

      // 3. Create session / set cookie
      const sessionId = 'dummy-session-' + user.id; // Replace with real session ID generation
      cookies.set('session', sessionId, {
        path: '/',
        httpOnly: true,
        secure: import.meta.env.PROD, // Use secure cookies in production
        maxAge: 60 * 60 * 24 * 7 // 1 week
      });

      console.log('Login successful, redirecting...');
      // Optional: Redirect after successful login
      // return redirect('/dashboard');

      // Return success result (can include user data, but avoid sensitive info)
      return { success: true, user: { name: user.name } };
    }
  }),

  // --- Example: Add Comment Action ---
  addComment: defineAction({
    input: z.object({
      postId: z.number(),
      commentBody: z.string().min(1).max(500),
    }),
    handler: async ({ postId, commentBody }, { locals }) => {
      // Example: Check if user is logged in (using data from middleware)
      // const user = locals.user;
      // if (!user) {
      //   throw new ActionError({ code: 'UNAUTHORIZED' });
      // }

      console.log(`Adding comment "${commentBody}" to post ${postId}`);
      // Add comment to database...
      // await db.insert(Comment).values({ postId, body: commentBody, authorId: user.id });

      // Can return data or just success status
      return { success: true, message: 'Comment added!' };
    }
  }),
};
```

## Calling Actions (Client-Side)

*   Import the `actions` object from `astro:actions`.
*   Call an action like an async function: `actions.actionName(args)`.
*   Astro handles the network request (POST to a special endpoint).
*   The call returns a Promise that resolves with the action's return value or rejects if an error occurs (including validation errors from the Zod schema or `ActionError` thrown in the handler).

```astro
---
// src/pages/login.astro
import { actions } from 'astro:actions'; // Import actions
import BaseLayout from '../layouts/BaseLayout.astro';

// Handle form submission (runs on server if JS disabled, or client if enabled)
if (Astro.request.method === 'POST') {
  let result;
  try {
    const formData = await Astro.request.formData();
    // Validate and call action on server (progressive enhancement)
    result = await actions.login(formData); // Astro automatically maps FormData to input schema

    if (result.success) {
      // Redirect on server if login is successful via POST
      return Astro.redirect('/dashboard');
    }
  } catch (error) {
    console.error("Action Error (Server):", error);
    // Handle server-side action errors (e.g., display generic message)
    result = { error: 'Login failed. Please try again.' };
  }
  // Re-render page with error message if needed (server-side)
}
---
<BaseLayout pageTitle="Login">
  <h1>Login</h1>
  {/* Display server-side errors if any */}
  {Astro.request.method === 'POST' && result?.error && <p style="color: red;">{result.error}</p>}

  {/* Standard HTML Form */}
  <form method="POST" id="login-form">
    <div>
      <label for="email">Email:</label>
      <input type="email" name="email" id="email" required />
    </div>
    <div>
      <label for="password">Password:</label>
      <input type="password" name="password" id="password" required minlength="6" />
    </div>
    <button type="submit">Login</button>
    <p id="client-error" style="color: red;"></p>
  </form>

  <script>
    // Client-side enhancement (optional)
    import { actions } from 'astro:actions';

    const form = document.getElementById('login-form');
    const errorElement = document.getElementById('client-error');

    form.addEventListener('submit', async (e) => {
      e.preventDefault(); // Prevent default form submission
      errorElement.textContent = ''; // Clear previous errors

      const formData = new FormData(form);
      try {
        // Call action directly from client-side JS
        const result = await actions.login(formData); // Astro handles serialization

        if (result.success) {
          console.log('Client Login OK:', result);
          // Redirect on client after successful action
          window.location.href = '/dashboard';
        } else {
          // Handle structured errors returned by the action
          errorElement.textContent = result.message || 'Login failed.';
        }
      } catch (error) {
        console.error("Action Error (Client):", error);
        // Handle validation errors (from Zod) or other exceptions
        if (error.code === 'VALIDATION_ERROR') {
          // error.errors contains Zod validation issues
          errorElement.textContent = error.errors.map(e => e.message).join(' ');
        } else {
          errorElement.textContent = error.message || 'An unexpected error occurred.';
        }
      }
    });
  </script>
</BaseLayout>
```

Astro Actions provide a convenient, type-safe bridge between client-side interactions (like form submissions) and secure server-side logic, simplifying common full-stack patterns.

*(Refer to the official Astro Actions documentation.)*