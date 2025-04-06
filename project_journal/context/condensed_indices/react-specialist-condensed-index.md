## React (Version Unknown) - Condensed Context Index

### Overall Purpose
React is a JavaScript library for building declarative, efficient, and flexible user interfaces (UIs) based on a component architecture. It enables the creation of complex UIs from small, isolated pieces of code called "components".

### Core Concepts & Capabilities
*   **Components:** Building blocks of React UIs. Defined as JavaScript functions returning JSX. Can be nested and reused (`function MyComponent(props) { ... }`).
*   **JSX:** Syntax extension allowing XML/HTML-like code within JavaScript (`const element = <h1>Hello</h1>;`). Requires transpilation. Use `className` instead of `class`.
*   **Props:** Mechanism for passing data down the component tree (parent to child). Read-only within the component (`props.propertyName`). `children` prop for nested content.
*   **State (`useState`)**: Manages data that changes over time within a component. `const [state, setState] = useState(initialValue)`. Updates trigger re-renders. Treat state as immutable.
*   **Hooks:** Functions allowing functional components to "hook into" React features (state, lifecycle, context, etc.). Rules: Call only at top level, only from React functions. Key hooks: `useState`, `useEffect`, `useContext`, `useReducer`, `useRef`, `useMemo`, `useCallback`.
*   **Conditional Rendering:** Displaying different UI based on conditions (e.g., using ternary operator `{condition ? <A /> : <B />}` or `&&`).
*   **List Rendering:** Dynamically rendering lists of components using `.map()`. Requires a unique, stable `key` prop for each list item (`items.map(item => <li key={item.id}>...</li>)`).
*   **Event Handling:** Responding to user interactions (e.g., `onClick`, `onChange`, `onSubmit`). Event handlers are passed as props. Use `e.preventDefault()` to stop default browser behavior.
*   **Context API (`createContext`, `useContext`, `Provider`)**: Shares data across the component tree without prop drilling. Useful for global state like themes or user authentication.
*   **Refs (`useRef`, `forwardRef`)**: Accessing DOM nodes directly or storing mutable values that persist across renders without causing re-renders.
*   **Effects (`useEffect`)**: Performing side effects (data fetching, subscriptions, manual DOM manipulations) after rendering. Can return a cleanup function.
*   **Performance Optimization (`useMemo`, `useCallback`, `lazy`, `Suspense`)**: Techniques to prevent unnecessary re-renders (memoization) and improve loading performance (code-splitting).
*   **State Management Patterns:** Lifting state up, using reducers (`useReducer`) for complex logic, structuring state effectively.
*   **Server Components / Actions:** Newer paradigm allowing components to run on the server, potentially improving performance and data fetching.

### Key APIs / Components / Configuration / Patterns
*   `useState(initialState)`: Hook to add state to functional components. Returns `[value, setValue]`.
*   `useEffect(setupFn, deps?)`: Hook for side effects. `setupFn` runs after render. Optional cleanup returned. `deps` array controls re-execution.
*   `useContext(MyContext)`: Hook to consume value from nearest `MyContext.Provider`.
*   `useReducer(reducerFn, initialState)`: Hook for state management with a reducer pattern. Returns `[state, dispatch]`.
*   `useMemo(computeFn, deps)`: Hook to memoize expensive computations. Recomputes only if `deps` change.
*   `useCallback(callbackFn, deps)`: Hook to memoize callback functions. Useful for performance optimizations when passing callbacks down.
*   `useRef(initialValue)`: Hook to create a mutable ref object (`ref.current`). Does not trigger re-render on change.
*   `createContext(defaultValue)`: Creates a Context object.
*   `<MyContext.Provider value={value}>`: Component making `value` available to consuming descendants.
*   `React.lazy(loadFn)`: Function for defining a code-split (lazy-loaded) component.
*   `<Suspense fallback={...}>`: Component to display a fallback UI while lazy components load.
*   `forwardRef(renderFn)`: Higher-order component to forward a `ref` prop to a child DOM element or component.
*   `createRoot(domNode)`: Entry point for rendering React apps (client-side). From `react-dom/client`.
*   `root.render(<App />)`: Renders the component tree into the DOM node associated with the root.
*   **JSX Elements:** e.g., `<div>`, `<MyComponent />`, `{jsExpression}`.
*   **Component Function:** `function MyComponent(props) { return <jsx />; }`.
*   **Props Passing:** `<ChildComponent data={myData} />`.
*   **Event Handler:** `onClick={() => console.log('Clicked')}`.
*   **List Mapping:** `data.map(item => <Component key={item.id} {...item} />)`.

### Common Patterns & Best Practices / Pitfalls
*   **Immutability:** Never mutate state or props directly. Use setter functions (`setState`) or create new objects/arrays. Use updater functions (`setState(prev => ...)`) when new state depends on old.
*   **Keys:** Provide stable, unique `key` props when rendering lists to help React identify items. Index as key is often an anti-pattern if list can change order/size.
*   **Lifting State Up:** When multiple components need access to the same state, lift it to their closest common ancestor.
*   **Effect Dependencies:** Provide accurate dependency arrays to `useEffect`, `useMemo`, `useCallback` to avoid stale closures or infinite loops. Empty array `[]` means run once on mount (and cleanup on unmount).
*   **Context Performance:** Memoize values passed to Context Providers (`useMemo`, `useCallback`) if consumers re-render often. Consider splitting contexts for unrelated values.
*   **Avoid Redundant State:** Calculate derived data directly during rendering instead of storing it in state if possible.
*   **Cleanup Effects:** Always clean up subscriptions, timers, or other resources in `useEffect` return function to prevent memory leaks.
*   **TypeScript:** Use TypeScript for better type safety with props, state, and context.

This index summarizes the core concepts, APIs, and patterns for React. Consult the full source documentation (project_journal/context/source_docs/react-specialist-llms-context-20250406.md) for exhaustive details.