# Custom Instructions: Clerk Elements for Custom UI

Building custom authentication flows using Clerk Elements (`@clerk/elements/*`).

## Core Concept: Clerk Elements

While Clerk's pre-built components (`<SignIn>`, `<SignUp>`) are convenient, **Clerk Elements** provide lower-level, unstyled building blocks to create completely custom authentication interfaces while still leveraging Clerk's backend logic and security.

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
*   ... and others for specific flows (verify email/phone, reset password).

**Setup:**
*   Ensure `<ClerkProvider>` is set up.
*   Install the necessary `@clerk/elements/*` packages.
    ```bash
    npm install @clerk/elements/common @clerk/elements/sign-in @clerk/elements/sign-up
    ```

## Building a Custom Sign-In Flow (Example)

Instead of using `<SignIn>`, you compose your form using elements from `@clerk/elements/sign-in`.

```jsx
import React from 'react';
import * as SignIn from '@clerk/elements/sign-in'; // Import all sign-in elements
import * as Clerk from '@clerk/elements/common'; // Import common elements like Loading

export function CustomSignInForm() {
  return (
    <SignIn.Root> {/* Root container for the sign-in flow */}
      <SignIn.Step name="start"> {/* Initial step */}
        <h2>Sign In</h2>
        {/* Social Providers */}
        <div style={{ display: 'flex', gap: '0.5rem', marginBottom: '1rem' }}>
          <SignIn.Action navigate="authenticate" strategy="oauth_google">
            <button>Sign in with Google</button>
          </SignIn.Action>
          {/* Add other social providers similarly */}
        </div>

        <hr />

        {/* Email/Password */}
        <SignIn.Action navigate="choose-strategy" strategy="password">
          <button>Sign in with password</button>
        </SignIn.Action>
        {/* Other strategies */}
        <SignIn.Action navigate="choose-strategy" strategy="email_code">
          <button>Sign in with email code</button>
        </SignIn.Action>
      </SignIn.Step>

      {/* Password Strategy Step */}
      <SignIn.Step name="choose-strategy" asChild>
        <form>
          <SignIn.Action strategy="password" submit>
            <Clerk.Field name="identifier"> {/* Use Clerk.Field for label/input connection */}
              <Clerk.Label>Email</Clerk.Label>
              <Clerk.Input type="email" required placeholder="Email address" />
              <Clerk.FieldError /> {/* Display field-specific error */}
            </Clerk.Field>
            <Clerk.Field name="password">
              <Clerk.Label>Password</Clerk.Label>
              <Clerk.Input type="password" required placeholder="Password" />
              <Clerk.FieldError />
            </Clerk.Field>
            <button type="submit">Sign In</button>
            <SignIn.GlobalError className="error-message" /> {/* Display step errors */}
          </SignIn.Action>
          <SignIn.Action navigate="forgot-password">
            <button type="button">Forgot Password?</button>
          </SignIn.Action>
          <SignIn.Action navigate="previous">
            <button type="button">Back</button>
          </SignIn.Action>
        </form>
      </SignIn.Step>

      {/* Email Code Verification Step */}
      <SignIn.Step name="verifications" asChild>
         <form>
           <p>Check your email for a verification code.</p>
           <SignIn.Action strategy="email_code" submit>
             <Clerk.Field name="code">
               <Clerk.Label>Verification Code</Clerk.Label>
               <Clerk.Input type="text" required inputMode="numeric" />
               <Clerk.FieldError />
             </Clerk.Field>
             <button type="submit">Verify</button>
             <SignIn.GlobalError className="error-message" />
           </SignIn.Action>
           <SignIn.Action navigate="previous">
             <button type="button">Back</button>
           </SignIn.Action>
         </form>
      </SignIn.Step>

      {/* Add other steps as needed (e.g., 'forgot-password', MFA steps) */}

      {/* Loading State */}
      <Clerk.Loading>
        <div className="loading-overlay">Loading...</div>
      </Clerk.Loading>

    </SignIn.Root>
  );
}
```

## Key Elements & Concepts

*   **`<SignIn.Root>` / `<SignUp.Root>`:** The main wrapper for the flow.
*   **`<SignIn.Step name="...">` / `<SignUp.Step name="...">`:** Represents a distinct screen or stage in the authentication flow (e.g., `start`, `choose-strategy`, `verifications`, `forgot-password`). Clerk automatically manages transitions between steps.
*   **`<SignIn.Strategy name="...">` / `<SignUp.Strategy name="...">`:** Represents a specific authentication method within a step (e.g., `password`, `email_code`, `oauth_google`). Clerk shows the relevant strategy based on user input or configuration.
*   **`<SignIn.Action navigate="..." strategy="..." submit>` / `<SignUp.Action ...>`:** Represents an action the user can take.
    *   `navigate`: Moves the user to a different step (e.g., `choose-strategy`, `forgot-password`, `previous`, `authenticate`).
    *   `strategy`: Specifies the authentication method to use (e.g., `password`, `oauth_google`, `email_link`, `verification_code`, `backup_code`).
    *   `submit`: Indicates the action submits the current step's form data (usually used on a button within a `<form>`).
*   **`<Clerk.Field name="...">`:** (From `@clerk/elements/common`) Helper component to wrap label, input, and error message for a specific field. Binds to Clerk's state.
*   **`<Clerk.Label>`:** Renders a label associated with a `Clerk.Field`.
*   **`<Clerk.Input name="...">`:** Renders an input field bound to Clerk's internal state. Requires a `name` corresponding to Clerk's expected fields (`identifier`, `password`, `emailAddress`, `firstName`, `code`, etc.).
*   **`<Clerk.FieldError />`:** Displays errors specific to the containing `Clerk.Field`.
*   **`<SignIn.GlobalError />` / `<SignUp.GlobalError />`:** Displays general errors for the current step, often placed within an `<Action submit>`.
*   **`<Clerk.Loading>`:** Conditionally renders its children when an action (like submit) is pending.

## Considerations

*   **Complexity:** Building custom flows with Elements requires more code and understanding of Clerk's state machine compared to using pre-built components.
*   **Styling:** You are responsible for all styling. Apply classes or use styling solutions as needed.
*   **Accessibility:** Ensure your custom structure, labels, and error messages are accessible. Use semantic HTML (`<form>`, `<label>`, `<button>`) and ARIA where appropriate. `Clerk.Field` helps with label association.
*   **Completeness:** You need to handle all relevant steps (including MFA if enabled) and potential error states for the authentication methods you enable.

Clerk Elements offer maximum flexibility for creating bespoke authentication UIs while leveraging Clerk's robust backend and state management.

*(Refer to the official Clerk Elements documentation.)*