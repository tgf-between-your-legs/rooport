# React Performance Hooks: `React.memo`, `useMemo`, `useCallback`

Optimizing React components by preventing unnecessary re-renders and calculations.

## The Problem: Unnecessary Re-renders

By default, React components re-render whenever their parent re-renders, even if their props haven't changed. This can lead to performance issues in complex applications. Additionally, expensive calculations within a component might run on every render, even if their inputs haven't changed.

## 1. `React.memo(Component, [arePropsEqual?])`

*   **Purpose:** A Higher-Order Component (HOC) that memoizes your functional component. React will skip rendering the component if its props have not changed (shallow comparison by default).
*   **Usage:** Wrap your component export with `React.memo`.
    ```jsx
    import React from 'react';

    function MyComponent({ name, details }) {
      console.log(`Rendering MyComponent with name: ${name}`);
      return <div>{name} - {details.info}</div>;
    }

    // Memoized version: Will only re-render if 'name' or 'details' props change reference
    const MemoizedComponent = React.memo(MyComponent);

    export default MemoizedComponent;

    // --- In Parent ---
    function Parent() {
      const [count, setCount] = useState(0);
      const [user, setUser] = useState({ name: 'Alice', details: { info: 'Info A' } });

      // This object is recreated on every Parent render
      const detailsObject = { info: 'Info A' };

      return (
        <div>
          <button onClick={() => setCount(c => c + 1)}>Increment Parent ({count})</button>

          {/* This WILL re-render MyComponent on every Parent render because detailsObject is a new object each time */}
          {/* <MyComponent name={user.name} details={detailsObject} /> */}

          {/* This WILL re-render MemoizedComponent on every Parent render because detailsObject is new */}
          {/* <MemoizedComponent name={user.name} details={detailsObject} /> */}

          {/* This will NOT re-render MemoizedComponent when only 'count' changes,
              because user.name and user.details references haven't changed */}
          <MemoizedComponent name={user.name} details={user.details} />
        </div>
      );
    }
    ```
*   **Comparison:** By default, `React.memo` does a shallow comparison of props. It checks if `prevProps.someProp === nextProps.someProp`. For objects and arrays, this means it checks reference equality, not deep equality.
*   **Custom Comparison:** You can provide an optional second argument `arePropsEqual(prevProps, nextProps)` function for custom comparison logic (rarely needed). Return `true` if props are equal (skip render), `false` otherwise.
*   **When to Use:** Wrap components that often render with the same props, especially if they are computationally expensive to render or are deep down the component tree. Don't memoize everything; measure performance first.

## 2. `useMemo(computeFunction, dependencies)`

*   **Purpose:** Memoizes the **result** of an expensive calculation. The `computeFunction` only re-runs if one of the `dependencies` has changed.
*   **Syntax:**
    ```jsx
    import React, { useState, useMemo } from 'react';

    function ExpensiveCalculationComponent({ list, filter }) {
      // This calculation runs on every render without useMemo
      // const filteredList = list.filter(item => item.includes(filter));

      // Memoized version: Calculation only runs if 'list' or 'filter' changes
      const filteredList = useMemo(() => {
        console.log('Running expensive filter...');
        return list.filter(item => item.includes(filter));
      }, [list, filter]); // Dependencies

      return (
        <ul>
          {filteredList.map(item => <li key={item}>{item}</li>)}
        </ul>
      );
    }
    ```
*   **Returns:** The memoized value from `computeFunction`.
*   **Dependencies:** Similar to `useEffect`, provide all reactive values used inside `computeFunction`.
*   **When to Use:** For computationally expensive calculations within a component that shouldn't run on every render if their inputs are the same. Also used to memoize object/array references passed down as props to memoized child components.

## 3. `useCallback(callbackFunction, dependencies)`

*   **Purpose:** Memoizes a **callback function** itself. Returns the same function reference between renders as long as its `dependencies` haven't changed.
*   **Syntax:**
    ```jsx
    import React, { useState, useCallback } from 'react';
    import MemoizedButton from './MemoizedButton'; // Assume this is wrapped in React.memo

    function ParentComponent() {
      const [count, setCount] = useState(0);

      // Without useCallback, a new handleClick function is created on every render,
      // causing MemoizedButton to re-render even if wrapped in React.memo.
      // const handleClick = () => {
      //   console.log('Button clicked!');
      // };

      // Memoized version: Returns the same function reference unless dependencies change
      const handleClick = useCallback(() => {
        console.log('Button clicked!');
        // If the callback needs props/state, include them in dependencies:
        // console.log(`Current count: ${count}`);
      }, []); // Empty array means function is created once

      return (
        <div>
          <p>Count: {count}</p>
          <button onClick={() => setCount(c => c + 1)}>Increment Count</button>
          <MemoizedButton onClick={handleClick}>Click Me</MemoizedButton>
        </div>
      );
    }
    ```
*   **Returns:** The memoized callback function.
*   **Dependencies:** Include all reactive values from the component scope that are used inside the callback function.
*   **When to Use:** Primarily when passing callbacks down to optimized child components (wrapped in `React.memo`) that rely on reference equality (`===`) to prevent unnecessary re-renders. Also useful as a dependency for other hooks like `useEffect`.

## Summary

*   `React.memo`: Prevents component re-renders if props are shallowly equal. For components.
*   `useMemo`: Caches the result of a calculation. For values.
*   `useCallback`: Caches a function definition. For functions passed as props/dependencies.

**Important:** Don't overuse these hooks. Premature optimization can make code harder to read. Profile your application first to identify actual performance bottlenecks before applying memoization.

*(Refer to the official React documentation for `React.memo`, `useMemo`, and `useCallback`: https://react.dev/reference/react)*