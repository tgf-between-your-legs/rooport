# React: Functional Components, JSX, Props & Conditional Rendering

Core concepts for building UI components in modern React.

## Functional Components

*   **Definition:** The standard way to create React components. They are JavaScript functions that accept `props` as an argument and return React elements (usually via JSX).
*   **Syntax:**
    ```jsx
    // Basic functional component
    function Welcome(props) {
      return <h1>Hello, {props.name}</h1>;
    }

    // Using arrow function syntax (common)
    const Greeting = ({ name, message }) => { // Destructuring props
      return (
        <div>
          <h1>{message}, {name}!</h1>
        </div>
      );
    };

    // Can also use React.FC for TypeScript type checking (optional)
    import React from 'react';
    interface GreetingProps {
      name: string;
      message: string;
    }
    const TypedGreeting: React.FC<GreetingProps> = ({ name, message }) => {
      return <h1>{message}, {name}!</h1>;
    };
    ```
*   **Characteristics:** Simpler, easier to read and test, and allow the use of Hooks.

## JSX (JavaScript XML)

*   **Definition:** A syntax extension for JavaScript that looks like HTML/XML. It allows you to write UI structures declaratively within your component code. It's transpiled (by tools like Babel) into standard `React.createElement()` calls.
*   **Key Rules:**
    *   **Single Root Element:** JSX expressions must have exactly one outermost element. Wrap adjacent elements in a parent `<div>`, `<>`, or `React.Fragment`.
        ```jsx
        // Correct: Single root element
        return (
          <div>
            <h1>Title</h1>
            <p>Paragraph</p>
          </div>
        );

        // Correct: Using Fragment shorthand
        return (
          <>
            <h1>Title</h1>
            <p>Paragraph</p>
          </>
        );

        // Incorrect: Multiple root elements
        // return (
        //   <h1>Title</h1>
        //   <p>Paragraph</p>
        // );
        ```
    *   **Embedding Expressions:** Use curly braces `{}` to embed JavaScript expressions (variables, function calls, calculations) within JSX.
        ```jsx
        const name = "Alice";
        const element = <h1>Hello, {name.toUpperCase()}! ({2 + 2})</h1>;
        ```
    *   **Attributes:** Use camelCase for most HTML attributes (e.g., `className` for `class`, `htmlFor` for `for`). Standard HTML attributes work for custom elements (`data-*`, `aria-*`). Attribute values can be strings (`"value"`) or expressions (`{variable}`). Boolean attributes can be written shorthand (`<Button disabled />` is true).
        ```jsx
        <img src={user.avatarUrl} className="profile-pic" alt="User Avatar" />
        <input type="text" value={inputValue} onChange={handleChange} required />
        ```
    *   **Self-Closing Tags:** Tags without children must be self-closed (`<img />`, `<br />`).

## Props (Properties)

*   **Definition:** How components receive data from their parents. Props are passed as attributes in JSX.
*   **Read-Only:** Props are **read-only** within the component that receives them. A component must never modify its own props. This is a core principle of React ("pure functions").
*   **Passing Props:**
    ```jsx
    function UserProfile(props) { // props is an object
      return (
        <div>
          <Avatar user={props.user} /> {/* Pass user object down */}
          <h2>{props.user.name}</h2>
        </div>
      );
    }

    function Avatar(props) {
      return <img src={props.user.avatarUrl} alt={props.user.name} />;
    }

    const userData = { name: 'Bob', avatarUrl: '...' };
    // Usage:
    <UserProfile user={userData} />
    ```
*   **Destructuring Props:** Common practice for cleaner access.
    ```jsx
    function Avatar({ user }) { // Destructure user from props
      return <img src={user.avatarUrl} alt={user.name} />;
    }
    ```
*   **`props.children`:** A special prop containing the content nested inside a component's opening and closing tags.
    ```jsx
    function Card({ children }) {
      return <div className="card">{children}</div>;
    }
    // Usage:
    <Card>
      <h1>Card Title</h1> {/* This becomes props.children */}
      <p>Card content.</p>
    </Card>
    ```

## Conditional Rendering

*   **Concept:** Displaying different UI based on state or props. React doesn't have built-in syntax; use standard JavaScript operators.
*   **`if`/`else`:** Can be used outside JSX or within helper functions.
*   **Ternary Operator (`condition ? exprIfTrue : exprIfFalse`):** Useful for simple inline conditions.
    ```jsx
    <div>
      {isLoggedIn ? <LogoutButton /> : <LoginButton />}
    </div>
    ```
*   **Logical AND (`condition && expression`):** Renders the expression only if the condition is true. If the condition is false, renders nothing. Be careful if the condition might evaluate to `0`, as React will render `0`.
    ```jsx
    <div>
      {unreadMessages.length > 0 &&
        <h2>You have {unreadMessages.length} unread messages.</h2>
      }
    </div>
    ```
*   **Returning `null`:** A component can return `null` to render nothing.

*(Refer to the official React documentation for more details on Components, JSX, Props, and Conditional Rendering: https://react.dev/learn)*