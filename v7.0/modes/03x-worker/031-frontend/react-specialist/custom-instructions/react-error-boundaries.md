# React: Error Boundaries

Catching JavaScript errors in component trees and displaying fallback UI using Error Boundaries.

## Core Concept: Error Boundaries

Error Boundaries are React components that **catch JavaScript errors** anywhere in their child component tree, log those errors, and display a **fallback UI** instead of the component tree that crashed.

**Key Features:**

*   **Catch Runtime Errors:** They catch errors during rendering, in lifecycle methods, and in constructors of the whole tree below them.
*   **Do Not Catch:**
    *   Errors inside event handlers (use regular `try...catch`).
    *   Asynchronous code (e.g., `setTimeout`, network request callbacks).
    *   Errors thrown in the error boundary component itself.
    *   Server-side rendering errors (though Next.js `error.tsx` handles this).
*   **Fallback UI:** Allow you to show a user-friendly message instead of a broken UI or white screen.
*   **Logging:** Provide a place (`componentDidCatch`) to log error information to reporting services (e.g., Sentry, LogRocket).
*   **Granularity:** Can be placed at different levels in the component tree to provide more specific fallback UIs for different sections.

## Implementation (Class Component)

As of React 18, Error Boundaries can **only** be implemented as **class components** defining one or both of these lifecycle methods:

1.  **`static getDerivedStateFromError(error)`:**
    *   A static method called during the "render" phase after a descendant component throws an error.
    *   Receives the error as an argument.
    *   Should return an object to update the boundary component's state (typically setting an `hasError: true` flag). Used to trigger rendering the fallback UI.
    *   **Do not** cause side effects here.
2.  **`componentDidCatch(error, errorInfo)`:**
    *   Called during the "commit" phase after an error has been caught by `getDerivedStateFromError`.
    *   Receives the `error` object and an `errorInfo` object (containing component stack trace).
    *   Use this method for **side effects** like logging the error to a reporting service.

```typescript
import React, { Component, ErrorInfo, ReactNode } from 'react';

interface Props {
  children?: ReactNode; // Make children optional or required based on usage
  fallback?: ReactNode; // Optional custom fallback UI prop
}

interface State {
  hasError: boolean;
  error?: Error; // Optional: store error for display
}

class ErrorBoundary extends Component<Props, State> {
  public state: State = {
    hasError: false,
  };

  // Update state so the next render will show the fallback UI.
  public static getDerivedStateFromError(error: Error): State {
    console.log("getDerivedStateFromError caught:", error);
    return { hasError: true, error: error };
  }

  // Log the error to an error reporting service
  public componentDidCatch(error: Error, errorInfo: ErrorInfo) {
    console.error("Uncaught error:", error, errorInfo);
    // Example: logErrorToMyService(error, errorInfo.componentStack);
  }

  // Optional: Add a way to reset the error state if needed
  // public resetError = () => {
  //   this.setState({ hasError: false, error: undefined });
  // }

  public render() {
    if (this.state.hasError) {
      // You can render any custom fallback UI
      return this.props.fallback || (
        <div>
          <h2>Oops! Something went wrong.</h2>
          <p>We're sorry for the inconvenience. Please try refreshing the page.</p>
          {/* Optionally display error details in development */}
          {process.env.NODE_ENV === 'development' && this.state.error && (
            <pre style={{ whiteSpace: 'pre-wrap', fontSize: '0.8em' }}>
              {this.state.error.toString()}
              <br />
              {/* componentStack is available in componentDidCatch, not here directly */}
            </pre>
          )}
          {/* Optionally add a reset button if resetError is implemented */}
          {/* <button onClick={this.resetError}>Try again</button> */}
        </div>
      );
    }

    // Normally, just render children
    return this.props.children;
  }
}

export default ErrorBoundary;

```

## Usage

Wrap parts of your application where errors might occur with your `ErrorBoundary` component.

```jsx
import React from 'react';
import ErrorBoundary from './ErrorBoundary';
import MyWidget from './MyWidget'; // Assume this might throw an error
import AnotherComponent from './AnotherComponent';

function App() {
  return (
    <div>
      <h1>My Application</h1>
      <ErrorBoundary fallback={<p>Failed to load widget.</p>}>
        <MyWidget />
      </ErrorBoundary>
      <hr />
      <ErrorBoundary> {/* Uses default fallback */}
        <AnotherComponent />
      </ErrorBoundary>
    </div>
  );
}
```

**Note on Hooks:** While you cannot *create* an error boundary using only hooks, libraries like `react-error-boundary` provide hook-based APIs (`useErrorHandler`) and components (`<ErrorBoundary>`) that simplify usage within functional components, often wrapping a class-based boundary internally.

Error Boundaries are essential for creating resilient React applications that handle runtime rendering errors gracefully without crashing the entire UI.

*(Refer to the official React documentation on Error Boundaries.)*