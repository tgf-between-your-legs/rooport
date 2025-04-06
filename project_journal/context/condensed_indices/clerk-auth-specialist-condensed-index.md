## Clerk (Version Unknown) - Condensed Context Index

### Overall Purpose
Clerk is an authentication and user management service for web and mobile applications. It provides SDKs and components (like `ClerkProvider`, `useSignIn`, `useAuth`, `clerkMiddleware`, Clerk Elements) to simplify implementing sign-in, sign-up, session management, and route protection in frameworks like Next.js, React Native, and tRPC.

### Core Concepts & Capabilities
*   **Frontend Integration:** Provides components and hooks (`ClerkProvider`, `useSignIn`, `useAuth`, Clerk Elements) for integrating auth flows into client-side applications (Next.js, React Native), including custom UI implementations (e.g., with shadcn/ui).
*   **Backend/Server-Side Logic:** Offers middleware (`clerkMiddleware`), server-side helpers (`getAuth`, `auth`, `clerkClient`), and Backend SDK functions for protecting routes, accessing user data in SSR/Server Components/Server Actions, and verifying sessions.
*   **Authentication Flows:** Supports various authentication strategies (email/password, social login, email code/link), including sign-in (`signIn.create`), sign-up (`SignUpResource`), session management (`setActive`, `getToken`), email verification (`prepareEmailAddressVerification`), and error handling (`isClerkAPIResponseError`).
*   **UI Customization & Elements:** Enables building custom authentication UIs using Clerk Elements (`<SignIn.Root>`, `<Clerk.Field>`, `<SignIn.Action>`) and styling via CSS or UI libraries.

### Key APIs / Components / Configuration / Patterns
*   `@clerk/nextjs`: Primary package for Next.js integration.
*   `<ClerkProvider>`: Root component wrapping the application to provide auth context.
*   `clerkMiddleware()`: Next.js middleware for handling auth state and route protection. Configure via `middleware.ts` with `matcher`.
*   `useSignIn()`: Hook for managing the sign-in flow state and actions (client-side).
*   `signIn.create({ identifier, password })`: Method (from `useSignIn`) to initiate a sign-in attempt.
*   `setActive({ session })`: Hook function (from `useSignIn`, `useSignUp`) to set the active session after success.
*   `useAuth()`: Hook to access authentication state (`userId`, `isSignedIn`) and session token (`getToken`) (client-side).
*   `getToken()`: Method (from `useAuth`) to retrieve the current session JWT for authenticated requests.
*   `auth()`: Helper function (server-side, Next.js App Router) for accessing auth state (`userId`) in Server Components and Server Actions. Opts route into dynamic rendering.
*   `getAuth(req)`: Helper function (server-side, Next.js Pages Router) for accessing auth state (`userId`) in `getServerSideProps`.
*   `clerkClient`: Backend SDK client for server-side operations (e.g., `users.getUser`, `sessions.verifySession` [deprecated], `authenticateRequest`). Initialize with keys.
*   `isClerkAPIResponseError(err)`: Type guard to check for Clerk-specific API errors during `try/catch`.
*   `ClerkAPIError`: Type for Clerk API errors, containing details like `longMessage`.
*   `SignUpResource`: Represents the sign-up attempt state and methods (client-side).
*   `prepareEmailAddressVerification()`: Method on `SignUpResource` to start email verification flow.
*   `@clerk/elements/common`, `@clerk/elements/sign-in`: Packages for building custom UI flows.
*   `<SignIn.Root>`, `<SignIn.Step>`, `<SignIn.Action>`, `<Clerk.Field>`, `<Clerk.Input>`, `<Clerk.Label>`, `<Clerk.FieldError>`: Key Clerk Elements components for sign-in forms.
*   `tRPC Middleware`: Pattern using `ctx.auth.userId` to protect tRPC procedures.
*   `matcher` (in `middleware.ts` config): Defines routes included/excluded from Clerk middleware processing.

### Common Patterns & Best Practices / Pitfalls
*   **Error Handling:** Use `try/catch` with `isClerkAPIResponseError` for sign-in/sign-up actions. Display `error.longMessage` to users.
*   **Loading States:** Check `isLoaded` from hooks before actions. Use `<Clerk.Loading>` for granular UI feedback in Clerk Elements.
*   **Route Protection:** Combine `clerkMiddleware` with server-side checks (`auth()`, `getAuth()`) or tRPC middleware for comprehensive protection.
*   **Server vs. Client:** Use server helpers (`auth`, `getAuth`, `clerkClient`) server-side and hooks (`useAuth`, `useSignIn`) client-side.
*   **Dynamic Rendering:** Be aware that using `auth()` in Server Components makes the route dynamic.
*   **Custom UI:** Use Clerk Elements for flexible and accessible custom authentication forms. Style with CSS data attributes (e.g., `[data-invalid]`).

This index summarizes the core concepts, APIs, and patterns for Clerk (Version Unknown) based on the provided examples. Consult the full source documentation (project_journal/context/source_docs/clerk-auth-specialist-llms-context-20250406.md) for exhaustive details.