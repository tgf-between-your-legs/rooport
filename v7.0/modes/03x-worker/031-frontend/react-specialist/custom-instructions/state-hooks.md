# React State Hooks: `useState` & `useReducer`

Managing component state in functional components.

## `useState(initialState)`

*   **Purpose:** The most basic hook for adding state to a component. Use it for simple state values (strings, numbers, booleans, simple objects/arrays).
*   **Syntax:**
    ```jsx
    import React, { useState } from 'react';

    function Counter() {
      // Declare a state variable 'count' initialized to 0
      // 'setCount' is the function to update the state
      const [count, setCount] = useState(0);

      const increment = () => {
        // Update state using the setter function
        setCount(count + 1);
      };

      // Updater function: Recommended when new state depends on previous state
      const incrementSafely = () => {
        setCount(prevCount => prevCount + 1);
      };

      return (
        <div>
          <p>Count: {count}</p>
          <button onClick={incrementSafely}>Increment</button>
        </div>
      );
    }
    ```
*   **Returns:** An array with two elements:
    1.  The current state value.
    2.  A setter function to update the state. Calling this function triggers a re-render.
*   **Immutability:** **Crucial!** Never mutate state directly. Always use the setter function. For objects and arrays, create *new* objects/arrays with the changes.
    ```jsx
    // Incorrect: Mutating state directly
    // user.name = 'New Name'; setUser(user);
    // list.push('New Item'); setList(list);

    // Correct: Creating new objects/arrays
    setUser(prevUser => ({ ...prevUser, name: 'New Name' }));
    setList(prevList => [...prevList, 'New Item']);
    ```
*   **Updater Function:** When the new state depends on the previous state (like a counter), pass a function to the setter (`setCount(prevCount => prevCount + 1)`). React guarantees `prevCount` will be the correct, up-to-date state value, avoiding potential issues with stale closures in asynchronous updates.

## `useReducer(reducer, initialArg, init?)`

*   **Purpose:** An alternative to `useState` for managing more complex state logic, especially when:
    *   The state involves multiple sub-values (like an object with several fields).
    *   The next state depends on the previous state in non-trivial ways.
    *   Updating state logic is complex and benefits from being centralized.
*   **Syntax:**
    ```jsx
    import React, { useReducer } from 'react';

    // 1. Define the initial state
    const initialState = { count: 0, step: 1 };

    // 2. Define the reducer function: (state, action) => newState
    // It takes the current state and an action object, and returns the *new* state.
    function reducer(state, action) {
      switch (action.type) {
        case 'increment':
          return { ...state, count: state.count + state.step };
        case 'decrement':
          return { ...state, count: state.count - state.step };
        case 'reset':
          return { ...state, count: 0 };
        case 'setStep':
          return { ...state, step: action.payload };
        default:
          throw new Error('Unknown action type');
      }
    }

    function CounterWithReducer() {
      // 3. Initialize the hook
      // 'state' holds the current state object
      // 'dispatch' is the function to send actions to the reducer
      const [state, dispatch] = useReducer(reducer, initialState);

      return (
        <div>
          <p>Count: {state.count} (Step: {state.step})</p>
          {/* 4. Dispatch actions on events */}
          <button onClick={() => dispatch({ type: 'increment' })}>Increment</button>
          <button onClick={() => dispatch({ type: 'decrement' })}>Decrement</button>
          <button onClick={() => dispatch({ type: 'reset' })}>Reset Count</button>
          <input
            type="number"
            value={state.step}
            onChange={(e) => dispatch({ type: 'setStep', payload: Number(e.target.value) })}
          />
        </div>
      );
    }
    ```
*   **Returns:** An array with two elements:
    1.  The current state value.
    2.  A `dispatch` function. You call `dispatch({ type: 'ACTION_TYPE', payload?: ... })` to trigger state updates.
*   **Reducer Function:** A pure function that takes the current `state` and an `action` object, and returns the **new state**. It should not have side effects. Actions typically have a `type` string and an optional `payload` with data.
*   **Benefits:** Centralizes update logic, makes complex state transitions easier to manage and test, can optimize performance in some cases by passing `dispatch` down instead of individual callbacks.

## Choosing Between `useState` and `useReducer`

*   Use `useState` for simple, independent state variables.
*   Consider `useReducer` when state logic becomes complex, involves multiple related pieces of state, or when the next state depends significantly on the previous one.

*(Refer to the official React documentation for `useState` and `useReducer`: https://react.dev/reference/react)*