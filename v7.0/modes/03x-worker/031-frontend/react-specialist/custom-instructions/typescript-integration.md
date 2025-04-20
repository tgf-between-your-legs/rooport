# React with TypeScript

Using TypeScript for type safety in React components, props, state, and events.

## Setup

*   Most modern React frameworks (Next.js, Vite with React template, Create React App with TypeScript template) handle TypeScript setup automatically.
*   Key dependencies: `typescript`, `@types/react`, `@types/react-dom`.
*   Configure `tsconfig.json` (often provided by the framework) with appropriate settings, especially `jsx: "react-jsx"` (or similar).

## Typing Components and Props

*   **Functional Components:** Use `React.FC` (Functional Component) or define prop types directly. `React.FC` implicitly includes `children` prop type. Defining types directly is often preferred for explicitness.
    ```typescript
    import React, { ReactNode } from 'react'; // Import ReactNode for children type

    // Option 1: Define prop types directly
    type GreetingProps = {
      name: string;
      message?: string; // Optional prop
      children?: ReactNode; // Explicitly type children if needed
    };

    const Greeting = ({ name, message = "Hello" }: GreetingProps) => { // Destructure and provide default value
      return <h1>{message}, {name}!</h1>;
    };

    // Option 2: Using React.FC (includes children implicitly)
    interface WelcomeProps {
      name: string;
    }
    const Welcome: React.FC<WelcomeProps> = ({ name, children }) => {
      return (
        <div>
          <h1>Welcome, {name}</h1>
          {children}
        </div>
      );
    };
    ```
*   **Exporting Types:** It's common practice to export prop types alongside the component for use in parent components or tests.

## Typing State (`useState`)

*   TypeScript often infers the type from the initial value.
*   Provide an explicit type argument if the initial value is `null`/`undefined` or if the state can hold multiple types (union type).
    ```typescript
    import React, { useState } from 'react';

    type User = { id: number; name: string };

    function UserProfile() {
      // Type inferred as number
      const [count, setCount] = useState(0);

      // Explicit type needed because initial value is null
      const [user, setUser] = useState<User | null>(null);

      // Type inferred as string[]
      const [tags, setTags] = useState(['react', 'typescript']);

      const loadUser = () => {
        // Assume fetchUser returns a User object
        // fetchUser().then(userData => setUser(userData));
        setUser({ id: 1, name: 'Alice' });
      };

      return (
        <div>
          <p>Count: {count}</p>
          <p>User: {user ? user.name : 'Not loaded'}</p>
          <button onClick={loadUser}>Load User</button>
        </div>
      );
    }
    ```

## Typing Reducers (`useReducer`)

*   Define types for the `state` and the `action` object (often using a discriminated union for action types).
    ```typescript
    import React, { useReducer } from 'react';

    // 1. Define State type
    type CounterState = {
      count: number;
      step: number;
    };

    // 2. Define Action types (Discriminated Union)
    type UpdateCountAction = { type: 'increment' | 'decrement' | 'reset' };
    type SetStepAction = { type: 'setStep'; payload: number };
    type CounterAction = UpdateCountAction | SetStepAction;

    const initialState: CounterState = { count: 0, step: 1 };

    // 3. Define Reducer with types
    function reducer(state: CounterState, action: CounterAction): CounterState {
      switch (action.type) {
        case 'increment':
          return { ...state, count: state.count + state.step };
        case 'decrement':
          return { ...state, count: state.count - state.step };
        case 'reset':
          return { ...state, count: 0 };
        case 'setStep':
          return { ...state, step: action.payload }; // Payload is number here
        default:
          // Enforce exhaustiveness check with 'never' type
          const exhaustiveCheck: never = action;
          throw new Error(`Unhandled action type: ${exhaustiveCheck}`);
      }
    }

    function CounterWithTypedReducer() {
      const [state, dispatch] = useReducer(reducer, initialState);

      return (
        <div>
          {/* ... JSX using state and dispatch ... */}
        </div>
      );
    }
    ```

## Typing Event Handlers

*   Use React's synthetic event types (e.g., `React.ChangeEvent`, `React.MouseEvent`, `React.FormEvent`). Import them from `react`.
*   Specify the HTML element type involved for better type checking (e.g., `React.ChangeEvent<HTMLInputElement>`).
    ```typescript
    import React, { useState, ChangeEvent, MouseEvent, FormEvent } from 'react';

    function MyForm() {
      const [value, setValue] = useState('');

      // Type the event for input change
      const handleChange = (event: ChangeEvent<HTMLInputElement>) => {
        setValue(event.target.value);
      };

      // Type the event for button click
      const handleClick = (event: MouseEvent<HTMLButtonElement>) => {
        console.log('Button clicked!', event.currentTarget);
      };

      // Type the event for form submission
      const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        console.log('Form submitted with value:', value);
      };

      return (
        <form onSubmit={handleSubmit}>
          <input type="text" value={value} onChange={handleChange} />
          <button type="submit" onClick={handleClick}>Submit</button>
        </form>
      );
    }
    ```

## Typing Refs (`useRef`)

*   Provide the element type the ref will hold as a generic argument. Initialize with `null`.
    ```typescript
    import React, { useRef, useEffect } from 'react';

    function FocusInput() {
      // Ref holds an HTMLInputElement or null
      const inputRef = useRef<HTMLInputElement>(null);

      useEffect(() => {
        // Access .current, which might be null initially
        inputRef.current?.focus();
      }, []);

      return <input ref={inputRef} type="text" />;
    }
    ```

*(Refer to the React TypeScript Cheatsheet and official documentation for more advanced patterns: https://react-typescript-cheatsheet.netlify.app/)*