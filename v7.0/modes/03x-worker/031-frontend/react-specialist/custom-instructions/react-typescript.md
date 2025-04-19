# React: Using with TypeScript

Leveraging TypeScript for type safety in React applications.

## Core Concept: Type Safety in React

TypeScript adds static typing to JavaScript, catching potential errors during development rather than at runtime. When used with React, it helps define the expected shapes of props, state, event handlers, and refs, improving code reliability, maintainability, and developer experience (autocompletion, refactoring).

**Key Benefits:**

*   **Error Prevention:** Catches type mismatches, undefined properties, incorrect argument types, etc., before running the code.
*   **Improved Readability:** Explicit types make component APIs (props) clearer.
*   **Enhanced Refactoring:** Type checking helps ensure changes don't break other parts of the application.
*   **Better Autocompletion:** IDEs provide more accurate suggestions based on defined types.

## Setting Up

*   **Create React App:** Use the TypeScript template: `npx create-react-app my-app --template typescript`.
*   **Next.js:** TypeScript is supported out-of-the-box. Use `.ts` or `.tsx` file extensions. Install types for React and Node: `npm install --save-dev @types/react @types/node`.
*   **Vite:** Use the `react-ts` template: `npm create vite@latest my-app -- --template react-ts`.
*   **Manual Setup:** Install `typescript`, `@types/react`, `@types/react-dom` and configure `tsconfig.json` (set `jsx` option, e.g., `"jsx": "react-jsx"`).

## Typing Common React Patterns

**1. Functional Components & Props:**

*   Define an interface or type alias for the component's props.
*   Use `React.FC<PropsType>` (Functional Component) or directly type the props argument. Typing the argument directly is often preferred for simplicity and better inference with default props.

```typescript
import React from 'react';

// Define prop types
interface GreetingProps {
  name: string;
  messageCount?: number; // Optional prop
  children?: React.ReactNode; // Type for children prop
}

// Option 1: Using React.FC (less common now)
// const Greeting: React.FC<GreetingProps> = ({ name, messageCount = 0, children }) => {
//   return (
//     <div>
//       <h1>Hello, {name}!</h1>
//       {messageCount > 0 && <p>You have {messageCount} messages.</p>}
//       {children}
//     </div>
//   );
// };

// Option 2: Typing props argument directly (preferred)
const Greeting = ({ name, messageCount = 0, children }: GreetingProps) => {
  return (
    <div>
      <h1>Hello, {name}!</h1>
      {messageCount > 0 && <p>You have {messageCount} messages.</p>}
      {children}
    </div>
  );
};

export default Greeting;
```

**2. `useState` Hook:**

*   TypeScript often infers the state type from the initial value.
*   Provide an explicit type argument if the initial value is `null`/`undefined` or if the type cannot be fully inferred.

```typescript
import React, { useState } from 'react';

interface User {
  id: number;
  name: string;
}

function UserProfile() {
  // Type inferred as number
  const [count, setCount] = useState(0);

  // Explicit type needed if initial value is null or could be User
  const [user, setUser] = useState<User | null>(null);

  // Type inferred as string[]
  const [tags, setTags] = useState(['react', 'typescript']);

  const loadUser = () => {
    setUser({ id: 1, name: 'Alice' });
  };

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(c => c + 1)}>Increment</button>

      {user ? <p>User: {user.name}</p> : <p>No user loaded.</p>}
      <button onClick={loadUser}>Load User</button>
    </div>
  );
}
```

**3. `useReducer` Hook:**

*   Define types for the `state` and `action` objects used by the reducer.

```typescript
import React, { useReducer } from 'react';

// Defined in react-hooks-reducer.md example
interface CounterState { count: number; step: number; }
type CounterAction =
  | { type: 'INCREMENT' } | { type: 'DECREMENT' }
  | { type: 'SET_STEP'; payload: number } | { type: 'RESET' };

const initialState: CounterState = { count: 0, step: 1 };

function counterReducer(state: CounterState, action: CounterAction): CounterState {
  // ... reducer logic ...
  return state; // Placeholder
}

function TypedReducerCounter() {
  const [state, dispatch] = useReducer(counterReducer, initialState);
  // ... component logic using state and dispatch ...
  return <div>Count: {state.count}</div>;
}
```

**4. `useRef` Hook:**

*   Provide a type argument for the expected ref value (e.g., `HTMLInputElement` for an input element).
*   Initialize DOM refs with `null`.

```typescript
import React, { useRef, useEffect } from 'react';

function TypedFocusInput() {
  // Type the ref for an HTMLInputElement, initialize with null
  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    // Accessing .current is now type-safe
    inputRef.current?.focus();
  }, []);

  return <input ref={inputRef} type="text" />;
}
```

**5. Event Handling:**

*   TypeScript can often infer event types (`e`) based on the handler (e.g., `onClick` gets `React.MouseEvent`).
*   Provide explicit types if needed (e.g., `React.ChangeEvent<HTMLInputElement>` for input `onChange`).

```typescript
import React, { useState } from 'react';

function TypedForm() {
  const [value, setValue] = useState('');

  // Explicitly type the event for input onChange
  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setValue(event.target.value);
  };

  // Type often inferred correctly for form onSubmit
  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    console.log('Submitted:', value);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" value={value} onChange={handleChange} />
      <button type="submit">Submit</button>
    </form>
  );
}
```

**Utility Types:** React provides utility types like `React.ReactNode` (for anything renderable, including `children`), `React.ReactElement`, `React.ComponentPropsWithoutRef`, etc.

Using TypeScript with React significantly enhances development by adding static type checking, making code more robust and easier to manage, especially in larger projects.

*(Refer to the official React documentation on TypeScript.)*