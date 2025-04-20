# Example: React v18 - Condensed Context Index

*(This is a simplified example of the output expected from the Context Condenser)*

## Overall Purpose
*   React is a JavaScript library for building user interfaces, focusing on declarative, component-based development.

## Core Concepts & Capabilities
*   **Components:** Building blocks of UI. Can be class-based (`React.Component`) or function-based. Functional components with Hooks are preferred. Encapsulate state and logic.
*   **JSX:** Syntax extension allowing HTML-like structures within JavaScript code for defining component UI. Transpiled to `React.createElement` calls.
*   **Props:** Read-only data passed down from parent to child components. (`props.propertyName`)
*   **State:** Data managed *within* a component that can change over time, triggering re-renders. Managed with `this.setState` (class) or `useState` hook (function).
*   **Lifecycle (Simplified):** Components mount (render first time), update (re-render due to state/prop changes), and unmount (removed from DOM). Key hooks: `useEffect` for side effects (data fetching, subscriptions).
*   **Conditional Rendering:** Use JavaScript logic (`if`, ternary operators, `&&`) within JSX to render elements conditionally.
*   **Lists & Keys:** Render lists of elements using `.map()`. Requires a unique `key` prop on each list item for efficient updates.
*   **Hooks:** Functions (`useState`, `useEffect`, `useContext`, etc.) allowing functional components to use state and other React features.

## Key APIs / Functions / Classes / Hooks
*   **`React.Component`:** Base class for class components (less common now).
*   **`useState(initialState)`:** Hook to add state to functional components. Returns `[state, setState]`.
*   **`useEffect(callback, [dependencies])`:** Hook for side effects. Runs after render. Dependency array controls re-runs. Empty `[]` runs once on mount. No array runs on every update.
*   **`useContext(MyContext)`:** Hook to subscribe to React context.
*   **`React.createElement()`:** Underlying function JSX compiles to. Rarely used directly.
*   **`ReactDOM.createRoot(domNode).render(element)`:** Renders a React element into a root DOM node (React 18+).

## Common Patterns & Best Practices / Pitfalls
*   **Best Practice:** Prefer functional components with Hooks over class components.
*   **Best Practice:** Lift state up to the nearest common ancestor when multiple components need the same data.
*   **Best Practice:** Use `key` prop correctly when rendering lists.
*   **Pitfall:** Modifying state directly (use `setState` or the setter from `useState`).
*   **Pitfall:** Forgetting dependency arrays in `useEffect` can lead to infinite loops or stale data.

---
*This index summarizes the core concepts, key APIs, and patterns for React v18. Consult the full source documentation (react.dev) for exhaustive details.*