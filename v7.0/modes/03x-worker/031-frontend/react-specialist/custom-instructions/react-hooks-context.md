# React: Context API (`createContext`, `useContext`, `Provider`)

Sharing state across the component tree without prop drilling using the Context API.

## Core Concept: Prop Drilling Problem & Context Solution

*   **Prop Drilling:** Passing data down through multiple layers of nested components via props, even if intermediate components don't need the data themselves. This can become cumbersome and make refactoring difficult.
*   **Context API:** Provides a way to pass data through the component tree without having to pass props down manually at every level. It allows components to "subscribe" to changes in a shared context value.

**Use Cases:**

*   Global state like theme (dark/light mode), user authentication status, language preference.
*   Data that needs to be accessible by many components at different nesting levels.

**Key Parts:**

1.  **`React.createContext(defaultValue)`:**
    *   Creates a Context object. Takes an optional `defaultValue` used only when a component tries to consume the context without a matching Provider higher up the tree.
    *   Returns an object with two components: `Provider` and `Consumer` (though `useContext` hook is preferred over `<Consumer>`).
2.  **`<MyContext.Provider value={sharedValue}>`:**
    *   A component that wraps the part of the component tree that needs access to the context data.
    *   Accepts a `value` prop. All descendant components that consume this context will receive this `value`.
    *   Whenever the `value` prop of the Provider changes, all consuming components below it will re-render.
3.  **`useContext(MyContext)`:**
    *   A hook used within a functional component to *consume* the context value.
    *   Accepts the Context object created by `createContext`.
    *   Returns the current context `value` determined by the *nearest* matching `<MyContext.Provider>` above it in the tree.
    *   Causes the component to re-render whenever the Provider's `value` prop changes.

## Implementation Steps

**1. Create the Context:**

```typescript
// src/context/ThemeContext.tsx
import React, { createContext, useState, useMemo } from 'react';

// Define the shape of the context data and methods
interface ThemeContextType {
  theme: 'light' | 'dark';
  toggleTheme: () => void;
}

// Create the context with a default value (used if no Provider is found)
// Often null or a default object, with type assertion if needed
export const ThemeContext = createContext<ThemeContextType | null>(null);

// Create a Provider component to wrap your app or part of it
export function ThemeProvider({ children }: { children: React.ReactNode }) {
  const [theme, setTheme] = useState<'light' | 'dark'>('light');

  const toggleTheme = () => {
    setTheme(prevTheme => (prevTheme === 'light' ? 'dark' : 'light'));
  };

  // Memoize the context value to prevent unnecessary re-renders of consumers
  // if the Provider itself re-renders but the value hasn't changed.
  const value = useMemo(() => ({ theme, toggleTheme }), [theme]);

  return (
    <ThemeContext.Provider value={value}>
      {children}
    </ThemeContext.Provider>
  );
}
```

**2. Provide the Context:**

Wrap the relevant part of your application tree (often the entire app in `_app.tsx` or `layout.tsx`) with the custom Provider component.

```typescript
// src/app/layout.tsx (Next.js App Router Example)
import { ThemeProvider } from '@/context/ThemeContext'; // Import custom provider

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <ThemeProvider> {/* Wrap the part needing the theme context */}
          {/* Header, Main Content, Footer, etc. */}
          {children}
        </ThemeProvider>
      </body>
    </html>
  );
}
```

**3. Consume the Context:**

Use the `useContext` hook in any functional component *within* the Provider tree.

```typescript
// src/components/ThemedButton.tsx
import React, { useContext } from 'react';
import { ThemeContext } from '@/context/ThemeContext'; // Import the context object
import Button from '@mui/material/Button'; // Example UI component

function ThemedButton() {
  const themeContext = useContext(ThemeContext);

  // Handle case where context might be null (if used outside Provider)
  if (!themeContext) {
    throw new Error("ThemedButton must be used within a ThemeProvider");
    // Or return a default state / null
  }

  const { theme, toggleTheme } = themeContext;

  return (
    <Button
      variant="contained"
      onClick={toggleTheme}
      sx={{
        bgcolor: theme === 'light' ? 'primary.main' : 'secondary.main',
        color: 'white',
      }}
    >
      Toggle Theme (Current: {theme})
    </Button>
  );
}

export default ThemedButton;
```

## Considerations

*   **Performance:** Context causes re-renders. If the `value` provided changes, *all* components consuming that context will re-render, even if they don't use the specific part of the value that changed.
    *   **Memoize Value:** Memoize the `value` object passed to the Provider using `useMemo` to prevent re-renders if the value object identity changes but its contents haven't.
    *   **Split Contexts:** For unrelated state values, consider creating multiple, smaller contexts instead of one large context object.
*   **Alternatives:** For complex global state management, consider dedicated state management libraries like Zustand, Jotai, Redux, or Recoil, which often offer more fine-grained control over updates and performance optimizations. Context API is best suited for low-frequency updates or truly global data like themes or authentication status.

Context API provides a built-in way to manage global or shared state in React without prop drilling, but be mindful of performance implications for frequent updates.

*(Refer to the official React documentation on Context.)*