# React Effect Hook: `useEffect`

Performing side effects in functional components.

## `useEffect(setup, dependencies?)`

*   **Purpose:** Lets you synchronize a component with an external system. This includes data fetching, setting up subscriptions (e.g., timers, event listeners), or manually manipulating the DOM (though refs are often better for direct DOM access). Effects run *after* the component renders.
*   **Syntax:**
    ```jsx
    import React, { useState, useEffect } from 'react';

    function ExampleComponent({ someProp }) {
      const [data, setData] = useState(null);

      // 1. Setup function: Runs after every completed render (by default)
      useEffect(() => {
        console.log('Component rendered or updated');

        // Example: Fetching data
        let ignore = false; // Flag to prevent state update if component unmounts quickly
        async function fetchData() {
          try {
            const response = await fetch(`/api/data?prop=${someProp}`);
            const result = await response.json();
            if (!ignore) {
              setData(result);
            }
          } catch (error) {
            console.error("Fetch error:", error);
            // Handle error appropriately
          }
        }

        fetchData();

        // 2. Cleanup function (optional): Runs before the component unmounts
        //    and also before the effect runs again (except for the first run).
        return () => {
          console.log('Cleaning up effect');
          ignore = true; // Prevent setting state on unmounted component
          // Example: Clean up subscriptions or timers
          // clearInterval(timerId);
          // window.removeEventListener('resize', handleResize);
        };
      }, [someProp]); // 3. Dependency array

      // ... component JSX ...
      return <div>{data ? JSON.stringify(data) : 'Loading...'}</div>;
    }
    ```

## Dependency Array (`dependencies?`)

*   **Purpose:** Controls **when** the `useEffect` setup function (and its cleanup) runs after the initial render. React compares the current values in the array with the values from the previous render.
*   **Behavior:**
    *   **`undefined` (Omitted):** The effect runs **after every render**. Use this rarely, often indicates a potential issue or need for refinement.
    *   **`[]` (Empty Array):** The effect runs **only once** after the initial render (mount), and the cleanup runs only once when the component unmounts. Useful for setting up subscriptions, initial data fetching that doesn't depend on props/state.
    *   **`[prop1, state2]` (Array with Values):** The effect runs after the initial render **and** after any subsequent render where any value in the dependency array has changed.
*   **Importance:** **Crucial** for correctness and performance.
    *   Include **all reactive values** (props, state, functions defined inside the component) that are read inside the effect's setup function.
    *   Omitting dependencies can lead to **stale closures**, where the effect uses outdated values from previous renders.
    *   Including unnecessary dependencies can cause the effect to run too often.
*   **ESLint Plugin:** The `react-hooks/exhaustive-deps` ESLint rule is highly recommended to help identify missing or incorrect dependencies.

## Cleanup Function

*   **Purpose:** To clean up any resources established by the effect before the component unmounts or before the effect runs again. Prevents memory leaks and unexpected behavior.
*   **When it Runs:**
    1.  Before the component unmounts.
    2.  Before the effect runs *again* due to a dependency change (it cleans up the *previous* effect).
*   **Common Uses:** Clearing timers (`clearInterval`), removing event listeners (`window.removeEventListener`), cancelling subscriptions, aborting fetch requests (`AbortController`).

## Key Considerations

*   **Side Effects Only:** Use `useEffect` for code that interacts with the "outside world" (APIs, DOM outside React, timers, subscriptions). Avoid using it for calculations based purely on props and state (use regular component logic or `useMemo` for that).
*   **Avoid Infinite Loops:** Ensure that state setters called within `useEffect` don't cause the effect's dependencies to change in a way that triggers the effect again immediately, leading to an infinite loop.
*   **Data Fetching:** While `useEffect` can be used for data fetching, consider custom hooks (`useDataFetcher` example in Hooks Overview) or libraries like SWR/React Query for more robust client-side data fetching with caching, revalidation, etc. In Next.js App Router, prefer fetching in Server Components where possible.

*(Refer to the official React `useEffect` documentation: https://react.dev/reference/react/useEffect)*