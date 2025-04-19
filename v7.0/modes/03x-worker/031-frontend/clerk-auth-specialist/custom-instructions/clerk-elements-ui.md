# Clerk Elements for Custom UI

Guide to using Clerk Elements (`@clerk/elements/*`) for building custom authentication UIs in React/Next.js.

## Core Concept

Clerk Elements provide unstyled, functional components that handle the underlying logic of authentication flows (sign-in, sign-up, verification, etc.). This allows developers to build completely custom UIs while leveraging Clerk's backend logic and security.

This contrasts with Clerk's pre-built components (`<SignIn>`, `<SignUp>`) which offer less UI customization but faster integration.

## Key Packages

*   `@clerk/elements`: Core package providing the building blocks.
*   Specific packages for different flows:
    *   `@clerk/elements/sign-in`
    *   `@clerk/elements/sign-up`
    *   `@clerk/elements/verify-email-address`
    *   `@clerk/elements/verify-phone-number`
    *   `@clerk/elements/reset-password`
    *   `@clerk/elements/user-profile` (for profile management sections)
    *   `@clerk/elements/organization-profile` (for org management sections)
    *   ... and others.

## Basic Structure (Sign In Example)

```jsx
import * as SignIn from "@clerk/elements/sign-in";
import React from 'react';

export default function CustomSignIn() {
  return (
    <SignIn.Root> {/* Root component for the sign-in flow */}
      <SignIn.Step name="start"> {/* Initial step */}
        <h2>Sign In</h2>
        {/* Social Providers */}
        <SignIn.SupportedStrategy name="google">
          <button>Sign in with Google</button>
        </SignIn.SupportedStrategy>
        {/* Separator */}
        <div>OR</div>
        {/* Email/Username Input */}
        <SignIn.Action submit> {/* Action to move to next step */}
          <label htmlFor="email-address">Email address</label>
          <input id="email-address" name="identifier" type="email" required />
          <button type="submit">Continue</button>
        </SignIn.Action>
        {/* Link to Sign Up */}
        <p>Don't have an account? <a href="/sign-up">Sign Up</a></p>
      </SignIn.Step>

      <SignIn.Step name="verifications"> {/* Step for password, OTP, etc. */}
        {/* Password Input */}
        <SignIn.Strategy name="password">
          <SignIn.Action submit>
            <label htmlFor="password">Password</label>
            <input id="password" name="password" type="password" required />
            <button type="submit">Sign In</button>
          </SignIn.Action>
          {/* Forgot Password Link */}
          <SignIn.Action navigate="forgot-password">
            <button type="button">Forgot Password?</button>
          </SignIn.Action>
        </SignIn.Strategy>

        {/* Email Code Verification */}
        <SignIn.Strategy name="email_code">
          <p>Check your email for a verification code.</p>
          <SignIn.Action submit>
            <label htmlFor="code">Verification Code</label>
            <input id="code" name="code" required />
            <button type="submit">Verify</button>
          </SignIn.Action>
        </SignIn.Strategy>

        {/* Add other verification strategies (Phone Code, TOTP) as needed */}

        {/* Go Back Link */}
        <SignIn.Action navigate="previous">
          <button type="button">Go Back</button>
        </SignIn.Action>
      </SignIn.Step>

      {/* Add other steps like 'forgot-password' if needed */}
      <SignIn.Step name="forgot-password">
         {/* ... Forgot password form elements ... */}
         <SignIn.Action navigate="previous">
           <button type="button">Go Back</button>
         </SignIn.Action>
      </SignIn.Step>

      {/* Loading State */}
      <Clerk.Loading>
         <div>Loading...</div> {/* Use Clerk.Loading from @clerk/elements */}
      </Clerk.Loading>

      {/* Error Handling */}
      <SignIn.Action.Error>
        {(error) => <p style={{ color: 'red' }}>{error.longMessage || 'An error occurred'}</p>}
      </SignIn.Action.Error>

    </SignIn.Root>
  );
}
```

## Key Components & Concepts

*   **Flow Root (`<SignIn.Root>`, `<SignUp.Root>`, etc.):** Wraps the entire flow.
*   **Step (`<SignIn.Step name="...">`):** Represents a distinct stage in the flow (e.g., initial identifier input, password verification, OTP verification). Clerk manages transitions between steps.
*   **Strategy (`<SignIn.Strategy name="...">`):** Represents a specific authentication method within a step (e.g., password, email_code, google). Clerk shows the relevant strategy based on user input or configuration.
*   **Action (`<SignIn.Action submit|navigate="...">`):** Triggers transitions.
    *   `submit`: Submits data for the current step/strategy (usually wraps form elements and a submit button).
    *   `navigate="previous"`: Goes back to the previous step.
    *   `navigate="forgot-password"`: Navigates to the step named "forgot-password".
*   **Field (`<Clerk.Field name="...">`):** (From `@clerk/elements`) A helper to connect labels and inputs, often managing error states.
*   **Loading (`<Clerk.Loading>`):** Conditionally renders its children when Clerk is performing an action.
*   **Error (`<SignIn.Action.Error>`):** Renders error messages associated with the last action.

## Styling

Clerk Elements are **unstyled** by default. You apply your own CSS classes or use styling solutions like Tailwind CSS, CSS Modules, Styled Components, etc., to match your application's design system.

## Considerations

*   **Complexity:** Building custom flows with Elements is more complex than using pre-built components but offers maximum UI flexibility.
*   **State Management:** Clerk Elements manage the internal authentication state. You typically don't need to manage loading/error states manually unless you need highly custom feedback.
*   **Accessibility:** While Elements provide semantic structure, ensure your custom styling and layout maintain accessibility (focus management, contrast, etc.).

*(Refer to the official Clerk Elements documentation for detailed API and examples: https://clerk.com/docs/elements/overview)*