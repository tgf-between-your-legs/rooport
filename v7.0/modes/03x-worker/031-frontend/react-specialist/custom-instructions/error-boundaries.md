# React Error Boundaries

Catching JavaScript errors anywhere in a component tree and displaying a fallback UI.

## Core Concept

Error boundaries are React components that catch JavaScript errors during rendering, in lifecycle methods, and in constructors of the whole tree below them. They **do not** catch errors for:

*   Event handlers (use regular `try...catch`)
*   Asynchronous code (`setTimeout`, `requestAnimationFrame`, promises without `await`)
*   Server-side rendering (SSR) errors (handled differently depending on framework)
*   Errors thrown in the error boundary component itself (the error propagates to the nearest boundary above it).

## Implementation (Class Component)

As of React 18, there is **no Hook equivalent** for error boundaries. You must implement them using a **class component** with specific lifecycle methods:

1.  **`static getDerivedStateFromError(error)`:** A static method that renders a fallback UI after an error has been thrown by a descendant component. It should return a state object to update the boundary's state (e.g., `{ hasError: true }`).
2.  **`componentDidCatch(error, errorInfo)`:** Runs after an error has been thrown by a descendant component. It receives the error and information about which component threw the error. Use this for side effects like logging the error to a reporting service.

```jsx
import React, { Component } from 'react';

class ErrorBoundary extends Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  // 1. Update state so the next render will show the fallback UI.
  static getDerivedStateFromError(error) {
    return { hasError: true, error: error };
  }

  // 2. Log the error to an error reporting service
  componentDidCatch(error, errorInfo) {
    console.error("ErrorBoundary caught an error:", error, errorInfo);
    // logErrorToMyService(error, errorInfo); // Example logging
  }

  render() {
    if (this.state.hasError) {
      // You can render any custom fallback UI
      return (
        <div>
          <h2>Something went wrong.</h2>
          <p>We're sorry, an error occurred. Please try refreshing the page.</p>
          {/* Optionally display error details during development */}
          {process.env.NODE_ENV === 'development' && this.state.error && (
            <details style={{ whiteSpace: 'pre-wrap' }}>
              {this.state.error.toString()}
              <br />
              {this.state.error.stack}
            </details>
          )}
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

Wrap parts of your UI that might throw errors with your `ErrorBoundary` component. The granularity is up to you – wrap individual widgets, sections, or the entire application.

```jsx
import React from 'react';
import ErrorBoundary from './ErrorBoundary';
import MyWidget from './MyWidget'; // Assume this might throw an error

function App() {
  return (
    <div>
      <h1>My Application</h1>
      <ErrorBoundary>
        {/* Errors inside MyWidget will be caught by ErrorBoundary */}
        <MyWidget />
      </ErrorBoundary>
      <ErrorBoundary>
        <AnotherSection />
      </ErrorBoundary>
      <p>Other content...</p>
    </div>
  );
}
```

## Key Considerations

*   **Placement:** Place error boundaries strategically. A boundary high up might show a generic error page, while boundaries around specific widgets can allow the rest of the app to function.
*   **Fallback UI:** Design a user-friendly fallback UI. Avoid showing raw error messages in production.
*   **Error Reporting:** Use `componentDidCatch` to log errors to a service (Sentry, LogRocket, etc.) for debugging.
*   **Resetting State:** Error boundaries catch errors from *renders*. If you need to recover, you might need a way to reset the boundary's state (e.g., passing a `key` prop that changes, or providing a reset button in the fallback UI that triggers a state update in a parent). The `reset` function passed to `error.tsx` in Next.js App Router serves a similar purpose.
*   **Next.js App Router:** Uses `error.tsx` file convention, which *must* be a Client Component and effectively acts as an error boundary for its segment. It receives `error` and `reset` props.

*(Refer to the official React documentation on Error Boundaries: https://react.dev/reference/react/Component#catching-rendering-errors-with-an-error-boundary)*