# Clerk: Clerk Elements for Custom UI

Building custom authentication flows using Clerk Elements.

## Core Concept: Clerk Elements

While Clerk's pre-built components (`<SignIn>`, `<SignUp>`) are convenient, sometimes you need full control over the UI's look, feel, and flow. **Clerk Elements** provide lower-level building blocks to create completely custom authentication interfaces while still leveraging Clerk's backend logic and security.

**Key Features:**

*   **Granular Control:** Build your sign-in/sign-up forms step-by-step using individual elements.
*   **Headless Logic:** Elements handle the underlying authentication logic (calling Clerk APIs, managing state, handling errors).
*   **Custom Styling:** Apply your own CSS or styling solutions directly to the elements and surrounding structure.
*   **Composable:** Combine elements to create unique authentication experiences.

**Packages:**

*   `@clerk/elements/common` (Core logic, required)
*   `@clerk/elements/sign-in`
*   `@clerk/elements/sign-up`
*   `@clerk/elements/user-profile`
*   `@clerk/elements/organization-profile`
*   `@clerk/elements/create-organization`

**Setup:**

*   Ensure `<ClerkProvider>` is set up.
*   Install the necessary `@clerk/elements/*` packages.
    ```bash
    npm install @clerk/elements/common @clerk/elements/sign-in @clerk/elements/sign-up
    ```

## Building a Custom Sign-In Flow

Instead of using `<SignIn>`, you compose your form using elements from `@clerk/elements/sign-in`.

```jsx
import React from 'react';
import * as SignIn from '@clerk/elements/sign-in'; // Import all sign-in elements

export function CustomSignInForm() {
  return (
    <SignIn.Root> {/* Root container for the sign-in flow */}
      <SignIn.Step name="start"> {/* Initial step */}
        <p>Sign in to your account</p>
        {/* Social Providers */}
        <div style={{ display: 'flex', gap: '0.5rem' }}>
          <SignIn.Action navigate="authenticate" strategy="oauth_google">
            <button>Sign in with Google</button>
          </SignIn.Action>
          <SignIn.Action navigate="authenticate" strategy="oauth_github">
            <button>Sign in with GitHub</button>
          </SignIn.Action>
        </div>

        <hr style={{ margin: '1rem 0' }} />

        {/* Email/Password */}
        <SignIn.Action navigate="choose-strategy" strategy="password">
          <button>Sign in with password</button>
        </SignIn.Action>

        {/* Email Link / Code */}
        <SignIn.Action navigate="choose-strategy" strategy="email_link">
          <button>Sign in with email link</button>
        </SignIn.Action>
        <SignIn.Action navigate="choose-strategy" strategy="email_code">
          <button>Sign in with email code</button>
        </SignIn.Action>
      </SignIn.Step>

      {/* Password Strategy Step */}
      <SignIn.Step name="choose-strategy" asChild>
        {/* `asChild` avoids rendering an extra div */}
        <form>
          <SignIn.Action strategy="password" submit>
            <div>
              <label htmlFor="email">Email</label>
              <SignIn.Input name="identifier" type="email" required placeholder="Email address" />
            </div>
            <div>
              <label htmlFor="password">Password</label>
              <SignIn.Input name="password" type="password" required placeholder="Password" />
            </div>
            <button type="submit">Sign In</button>
            {/* Error Handling */}
            <SignIn.GlobalError className="error-message" />
            <SignIn.FieldError name="identifier" className="error-message" />
            <SignIn.FieldError name="password" className="error-message" />
          </SignIn.Action>
          {/* Link to forgot password or other strategies */}
          <SignIn.Action navigate="forgot-password">
            <button type="button">Forgot Password?</button>
          </SignIn.Action>
          <SignIn.Action navigate="previous">
            <button type="button">Back</button>
          </SignIn.Action>
        </form>
      </SignIn.Step>

      {/* Email Link Strategy Step */}
      <SignIn.Step name="verifications" asChild>
         <p>Check your email for the sign-in link.</p>
         {/* Add UI for resend if needed */}
         <SignIn.Action navigate="previous">
            <button type="button">Back</button>
          </SignIn.Action>
      </SignIn.Step>

      {/* Add other steps as needed (e.g., 'forgot-password', MFA steps like 'verifications') */}

      {/* Loading State */}
      <Clerk.Loading>
        {/* Optional: Render a loading indicator while actions are pending */}
        <div className="loading-overlay">Loading...</div>
      </Clerk.Loading>

    </SignIn.Root>
  );
}

// Import Clerk from common for Loading
import * as Clerk from '@clerk/elements/common';
```

## Key Elements & Concepts

*   **`<SignIn.Root>` / `<SignUp.Root>`:** The main wrapper for the flow.
*   **`<SignIn.Step name="...">` / `<SignUp.Step name="...">`:** Represents a distinct screen or stage in the authentication flow (e.g., choosing a strategy, entering a password, verifying MFA). Clerk automatically manages transitions between steps based on user actions and API responses.
*   **`<SignIn.Action navigate="..." strategy="...">` / `<SignUp.Action ...>`:** Represents an action the user can take.
    *   `navigate`: Moves the user to a different step (e.g., `choose-strategy`, `forgot-password`, `previous`).
    *   `strategy`: Specifies the authentication method to use (e.g., `password`, `oauth_google`, `email_link`).
    *   `submit`: Indicates the action submits the current step's form data (usually used on a button within a `<form>`).
*   **`<SignIn.Input name="...">` / `<SignUp.Input ...>`:** Renders an input field bound to Clerk's internal state. Requires a `name` corresponding to Clerk's expected fields (`identifier`, `password`, `emailAddress`, `firstName`, `code`, etc. - see Clerk docs).
*   **`<Clerk.Loading>`:** Conditionally renders its children when an action (like submit) is pending.
*   **Error Handling:**
    *   `<SignIn.GlobalError />` / `<SignUp.GlobalError />`: Displays general errors for the current step.
    *   `<SignIn.FieldError name="..." />` / `<SignUp.FieldError ...>`: Displays errors specific to a named input field.

## Considerations

*   **Complexity:** Building custom flows with Elements requires more code and understanding of Clerk's state machine compared to using pre-built components.
*   **Styling:** You are responsible for all styling. Apply classes or use styled-components as needed.
*   **Accessibility:** Ensure your custom structure, labels, and error messages are accessible. Use semantic HTML and ARIA where appropriate.
*   **Completeness:** You need to handle all relevant steps and potential error states for the authentication methods you enable.

Clerk Elements offer maximum flexibility for creating bespoke authentication UIs while leveraging Clerk's robust backend and state management.

*(Refer to the official Clerk Elements documentation.)*