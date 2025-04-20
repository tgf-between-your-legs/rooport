# React Hooks Overview

Hooks are functions that let you "hook into" React state and lifecycle features from functional components.

## Rules of Hooks

1.  **Only Call Hooks at the Top Level:** Don't call Hooks inside loops, conditions, or nested functions. Always use Hooks at the top level of your React function, before any early returns. This ensures Hooks are called in the same order each time the component renders, which is crucial for React to preserve state between calls.
2.  **Only Call Hooks from React Functions:** Don't call Hooks from regular JavaScript functions. Call them from:
    *   ✅ React Functional Components
    *   ✅ Custom Hooks (functions whose names start with `use`)

## Common Built-in Hooks

*   **State Hooks:**
    *   `useState(initialState)`: Lets you add state to functional components. Returns a stateful value and a function to update it.
    *   `useReducer(reducer, initialArg, init?)`: An alternative to `useState` for more complex state logic involving multiple sub-values or when the next state depends on the previous one.
*   **Context Hook:**
    *   `useContext(MyContext)`: Lets you subscribe to React context without introducing nesting. Accepts a context object (the value returned from `React.createContext`) and returns the current context value.
*   **Ref Hooks:**
    *   `useRef(initialValue)`: Returns a mutable `ref` object whose `.current` property is initialized to the passed argument. It can hold a value that persists across renders without causing re-renders, or be used to access DOM nodes.
    *   `forwardRef`: Lets your component expose a DOM node to its parent component using a `ref`.
*   **Effect Hooks:**
    *   `useEffect(setup, dependencies?)`: Lets you perform side effects in functional components (data fetching, subscriptions, manual DOM manipulations). Runs after render. Can return a cleanup function. The `dependencies` array controls when the effect re-runs.
*   **Performance Hooks:**
    *   `useMemo(computeFunction, dependencies)`: Memoizes the result of a calculation. Re-runs the calculation only if dependencies change.
    *   `useCallback(callbackFunction, dependencies)`: Memoizes a callback function itself. Useful for passing callbacks to optimized child components that rely on reference equality.
*   **Other Hooks:** `useLayoutEffect`, `useImperativeHandle`, `useDebugValue`, `useId`, `useTransition`, `useDeferredValue`.

## Custom Hooks

*   **Concept:** A JavaScript function whose name starts with `use` and that *may* call other Hooks.
*   **Purpose:** Allows you to extract component logic into reusable functions. Share stateful logic between components without repeating code or complex patterns like HOCs/render props.
*   **Example:**
    ```jsx
    import { useState, useEffect } from 'react';

    // Custom Hook to fetch data
    function useDataFetcher(url) {
      const [data, setData] = useState(null);
      const [loading, setLoading] = useState(true);
      const [error, setError] = useState(null);

      useEffect(() => {
        setLoading(true);
        fetch(url)
          .then(res => { if (!res.ok) throw new Error('Fetch failed'); return res.json(); })
          .then(setData)
          .catch(setError)
          .finally(() => setLoading(false));
      }, [url]); // Dependency: re-fetch if URL changes

      return { data, loading, error };
    }

    // Usage in a component
    function MyComponent({ userId }) {
      const { data: user, loading, error } = useDataFetcher(`/api/users/${userId}`);

      if (loading) return <p>Loading...</p>;
      if (error) return <p>Error loading user.</p>;

      return <h1>Welcome, {user.name}</h1>;
    }
    ```

*(Refer to the official React Hooks API Reference: https://react.dev/reference/react)*