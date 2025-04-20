# React: State and Effect Hooks (`useState`, `useEffect`)

Managing component state and side effects using fundamental React Hooks.

## Core Concept: Hooks

Hooks are functions that let you "hook into" React state and lifecycle features from **functional components**. They must be called at the top level of your component, not inside loops, conditions, or nested functions.

## 1. `useState(initialState)`

*   **Purpose:** Adds local state to a functional component. Allows the component to "remember" information between renders.
*   **Syntax:** `const [state, setState] = useState(initialValue);`
*   **Returns:** An array with two elements:
    *   `state`: The current state value for this render.
    *   `setState`: A function to update the state value. Calling `setState` triggers a re-render of the component with the new state value.
*   **Updating State:**
    *   `setState(newValue)`: Replaces the state with `newValue`.
    *   `setState(prevState => newValue)`: **Updater function**. Recommended when the new state depends on the previous state. Receives the pending state and returns the new state. React ensures this uses the correct previous state, even with batching.
*   **Immutability:** Treat state as immutable. When updating objects or arrays, create *new* objects/arrays instead of modifying the existing ones directly.

```jsx
import React, { useState } from 'react';

function Counter() {
  // Initialize state variable 'count' to 0
  const [count, setCount] = useState(0);
  const [user, setUser] = useState({ name: 'Anon', age: 0 });

  const increment = () => {
    // Use updater function when new state depends on previous
    setCount(prevCount => prevCount + 1);
    setCount(prevCount => prevCount + 1); // Correctly increments by 2
  };

  const setName = (newName) => {
    // Create a new object when updating object state
    setUser(prevUser => ({ ...prevUser, name: newName }));
  };

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={increment}>Increment</button>
      <button onClick={() => setCount(0)}>Reset</button>

      <p>User: {user.name}</p>
      <button onClick={() => setName('Alice')}>Set Name to Alice</button>
    </div>
  );
}
```

## 2. `useEffect(setupFn, dependencies?)`

*   **Purpose:** Performs **side effects** in functional components. Side effects are operations that interact with the "outside world" beyond rendering the UI, such as:
    *   Data fetching (APIs)
    *   Setting up subscriptions (timers, WebSockets)
    *   Manually changing the DOM (less common, usually use state/props)
*   **Syntax:** `useEffect(setupFunction, dependencyArray?)`
*   **`setupFunction`:** The function containing the side effect code. It runs *after* React commits changes to the DOM.
*   **`dependencyArray` (Optional):** Controls when the effect re-runs.
    *   **Omitted:** Effect runs after *every* render. (Use with caution, can cause infinite loops if the effect itself triggers a re-render).
    *   **`[]` (Empty Array):** Effect runs only *once* after the initial render (component mount). The cleanup function runs on unmount.
    *   **`[prop1, state1]` (Array with values):** Effect runs after the initial render *and* whenever any value in the dependency array changes between renders.
*   **Cleanup Function (Optional):** The `setupFunction` can optionally return a cleanup function. This function runs:
    *   Before the effect runs again (if dependencies change).
    *   When the component unmounts.
    *   Use this to clean up resources like timers, subscriptions, or event listeners to prevent memory leaks.

```jsx
import React, { useState, useEffect } from 'react';

function Timer() {
  const [seconds, setSeconds] = useState(0);

  useEffect(() => {
    // This effect runs only once after initial render (due to [])
    console.log('Setting up interval...');
    const intervalId = setInterval(() => {
      console.log('Tick');
      // Use updater function for state based on previous state inside interval
      setSeconds(prevSeconds => prevSeconds + 1);
    }, 1000);

    // Cleanup function: Runs when component unmounts
    return () => {
      console.log('Cleaning up interval...');
      clearInterval(intervalId);
    };
  }, []); // Empty dependency array: run only on mount/unmount

  return <div>Timer: {seconds} seconds</div>;
}

function UserData({ userId }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // This effect runs on initial render AND when userId prop changes
    setLoading(true);
    console.log(`Fetching data for user ${userId}...`);
    let isCancelled = false; // Flag to prevent state update on unmounted component

    fetch(`/api/users/${userId}`)
      .then(res => res.ok ? res.json() : Promise.reject(new Error('Fetch failed')))
      .then(data => {
        if (!isCancelled) {
          setUser(data);
        }
      })
      .catch(error => {
        console.error(error);
        // Handle error state if needed
      })
      .finally(() => {
        if (!isCancelled) {
          setLoading(false);
        }
      });

    // Cleanup function: Runs if userId changes before fetch completes, or on unmount
    return () => {
      isCancelled = true;
      console.log(`Cleaning up fetch for user ${userId}`);
    };
  }, [userId]); // Dependency array: re-run effect if userId changes

  if (loading) return <p>Loading user data...</p>;
  if (!user) return <p>User not found.</p>;

  return <div>User Name: {user.name}</div>;
}
```

`useState` and `useEffect` are the cornerstone hooks for managing state and side effects in functional React components. Use them correctly, paying close attention to immutability and dependency arrays, to build robust and predictable UIs.

*(Refer to the official React documentation on `useState` and `useEffect`.)*