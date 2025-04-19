# React Context API

Sharing state across the component tree without prop drilling.

## Core Concept

Context provides a way to pass data through the component tree without having to pass props down manually at every level. It's designed to share data that can be considered "global" for a tree of React components, such as the current authenticated user, theme, or preferred language.

## API

1.  **`React.createContext(defaultValue)`**
    *   Creates a Context object. React reads the current context value from the closest matching `Provider` above it in the tree.
    *   The `defaultValue` argument is **only** used when a component does not have a matching `Provider` above it in the tree. This can be helpful for testing components in isolation.
    ```javascript
    import React from 'react';

    // 1. Create context with a default value
    const ThemeContext = React.createContext('light'); // Default theme is 'light'
    ```

2.  **`<MyContext.Provider value={value}>`**
    *   A component that allows consuming components to subscribe to context changes.
    *   Accepts a `value` prop to be passed to consuming components that are descendants of this Provider.
    *   All consumers that are descendants of a Provider will re-render whenever the Provider's `value` prop changes.
    *   Place it high up in the tree to wrap components that need access to the context.
    ```jsx
    import React, { useState } from 'react';
    import ThemeContext from './ThemeContext'; // Assume context is in a separate file

    function App() {
      const [theme, setTheme] = useState('light');

      const toggleTheme = () => {
        setTheme(prevTheme => (prevTheme === 'light' ? 'dark' : 'light'));
      };

      // 2. Provide the context value
      return (
        <ThemeContext.Provider value={{ theme, toggleTheme }}> {/* Pass state and updater */}
          <Toolbar />
        </ThemeContext.Provider>
      );
    }
    ```

3.  **`useContext(MyContext)`**
    *   A hook to read and subscribe to context within a functional component.
    *   Accepts the context object itself (returned from `React.createContext`).
    *   Returns the current context `value` for that context, determined by the `value` prop of the nearest `<MyContext.Provider>` above the calling component in the tree.
    *   The component calling `useContext` will **always re-render** when the context value changes.
    ```jsx
    import React, { useContext } from 'react';
    import ThemeContext from './ThemeContext';

    function ThemedButton() {
      // 3. Consume the context value
      const { theme, toggleTheme } = useContext(ThemeContext);

      return (
        <button
          style={{ background: theme === 'dark' ? '#333' : '#eee', color: theme === 'dark' ? '#eee' : '#333' }}
          onClick={toggleTheme}
        >
          Switch Theme (Current: {theme})
        </button>
      );
    }
    ```

## Best Practices & Considerations

*   **Use Sparingly:** Context is primarily for "global" data needed by many components at different nesting levels. For passing data from parent to immediate child or a few levels down, prop drilling is often simpler and more explicit.
*   **Performance:** All components consuming a context will re-render when the context `value` changes. If the `value` is an object or array created inline (`value={{ theme, toggleTheme }}`), it will cause re-renders on *every* render of the Provider, even if the underlying data hasn't changed, because a new object reference is created each time.
    *   **Optimization:** Memoize the context value using `useMemo` (for objects/arrays) or `useCallback` (for functions) in the Provider component if performance becomes an issue.
    ```jsx
    // In App component from above example:
    const contextValue = useMemo(() => ({ theme, toggleTheme }), [theme]);
    // ...
    return <ThemeContext.Provider value={contextValue}>...</ThemeContext.Provider>;
    ```
*   **Splitting Contexts:** If different parts of your application need different pieces of global state, consider creating multiple, more specific context objects rather than one large global context. This reduces unnecessary re-renders for components that only care about a subset of the data.
*   **Default Value:** The `defaultValue` in `createContext` is mainly for testing or when a consumer is rendered without a matching Provider. It doesn't automatically update if the Provider's value changes.
*   **Combine with `useState`/`useReducer`:** Often, the state provided via Context is managed within the Provider component using `useState` or `useReducer`.

*(Refer to the official React Context documentation: https://react.dev/learn/passing-data-deeply-with-context and API reference: https://react.dev/reference/react/useContext)*