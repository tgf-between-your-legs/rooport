# React: Performance Hooks (`useMemo`, `useCallback`, `React.memo`)

Optimizing React component performance by preventing unnecessary re-renders and calculations.

## Core Concept: Preventing Unnecessary Re-renders

React components re-render when their state or props change. Sometimes, components re-render even if their output would be the same, leading to wasted computation. React provides hooks and utilities to **memoize** (cache) values, functions, or component outputs to skip unnecessary work.

**Key Tools:**

1.  **`React.memo(Component)`:**
    *   A higher-order component (HOC) that wraps a functional component.
    *   It memoizes the wrapped component. React will skip re-rendering the component if its **props** have not changed (shallow comparison by default).
    *   Useful for components that render often with the same props.
2.  **`useMemo(computeFn, dependencies)`:**
    *   A hook that memoizes the **result** of an expensive calculation (`computeFn`).
    *   `computeFn` is only re-executed if one of the `dependencies` has changed.
    *   Returns the cached result from the previous render if dependencies are the same.
    *   Use this to avoid re-computing complex values on every render.
3.  **`useCallback(callbackFn, dependencies)`:**
    *   A hook that memoizes a **callback function** itself.
    *   Returns the same function instance between renders as long as its `dependencies` haven't changed.
    *   Crucial when passing callbacks as props to memoized child components (`React.memo`) to prevent them from re-rendering unnecessarily just because the parent created a new function instance on each render.

## Implementation

**1. `React.memo`:**

Wrap functional components that might receive the same props frequently.

```jsx
import React from 'react';

// Assume this component is expensive to render or receives complex props
function UserDetails({ user }) {
  console.log(`Rendering UserDetails for ${user.name}`);
  return (
    <div>
      <p>Name: {user.name}</p>
      <p>Age: {user.age}</p>
    </div>
  );
}

// Wrap the component with React.memo
const MemoizedUserDetails = React.memo(UserDetails);

// Parent component
function UserList({ users }) {
  const [selectedUserId, setSelectedUserId] = useState(null);

  return (
    <div>
      {/* Other UI */}
      {users.map(user => (
        // MemoizedUserDetails will only re-render if the specific 'user' prop object changes
        <MemoizedUserDetails key={user.id} user={user} />
      ))}
    </div>
  );
}
```
*Note: `React.memo` only does a shallow comparison of props. If props are objects or arrays that change identity on every parent render (even if contents are the same), `React.memo` won't prevent re-renders unless you provide a custom comparison function.*

**2. `useMemo`:**

Memoize the result of expensive calculations.

```jsx
import React, { useState, useMemo } from 'react';

function calculateExpensiveValue(a, b) {
  console.log('Calculating expensive value...');
  // Simulate heavy computation
  // ... complex logic ...
  return a + b * Math.random(); // Example result
}

function Calculator({ numA, numB }) {
  // Re-calculate only when numA or numB changes
  const expensiveResult = useMemo(() => {
    return calculateExpensiveValue(numA, numB);
  }, [numA, numB]); // Dependency array

  return (
    <div>
      <p>Number A: {numA}</p>
      <p>Number B: {numB}</p>
      <p>Expensive Result: {expensiveResult}</p>
    </div>
  );
}
```

**3. `useCallback`:**

Memoize callback functions, especially when passing them to memoized children.

```jsx
import React, { useState, useCallback } from 'react';

// Assume ListItem is wrapped in React.memo
const MemoizedListItem = React.memo(function ListItem({ item, onRemove }) {
  console.log(`Rendering item ${item.id}`);
  return (
    <li>
      {item.name} <button onClick={() => onRemove(item.id)}>Remove</button>
    </li>
  );
});

function TodoList() {
  const [items, setItems] = useState([{ id: 1, name: 'Task 1' }, { id: 2, name: 'Task 2' }]);
  const [filter, setFilter] = useState(''); // Example other state

  // Without useCallback, a new handleRemove function instance is created on every TodoList render,
  // causing MemoizedListItem to re-render even if its 'item' prop hasn't changed.
  const handleRemove = useCallback((idToRemove) => {
    setItems(prevItems => prevItems.filter(item => item.id !== idToRemove));
  }, []); // Empty dependency array: function identity is stable across renders

  return (
    <div>
      <input type="text" value={filter} onChange={e => setFilter(e.target.value)} placeholder="Filter..." />
      <ul>
        {items.map(item => (
          <MemoizedListItem
            key={item.id}
            item={item}
            onRemove={handleRemove} // Pass the memoized callback
          />
        ))}
      </ul>
    </div>
  );
}
```

## Considerations

*   **Don't Memoize Everything:** Memoization has a small cost (memory, comparison). Only apply it where necessary – typically for computationally expensive operations or to prevent prop changes causing large sub-tree re-renders. Profile your application first to identify bottlenecks.
*   **Dependency Arrays:** Correct dependency arrays are crucial for `useMemo` and `useCallback`. Omitting a dependency means the value/function might become stale. Including unnecessary dependencies negates the optimization.
*   **Referential Equality:** `React.memo` (by default), `useMemo`, and `useCallback` rely on referential equality for non-primitive dependencies (objects, arrays, functions). If you create new objects/arrays/functions on every render, memoization won't work unless you also memoize their creation or use custom comparison.

Use these hooks strategically to optimize the performance of your React applications by skipping unnecessary work.

*(Refer to the official React documentation on `React.memo`, `useMemo`, and `useCallback`.)*