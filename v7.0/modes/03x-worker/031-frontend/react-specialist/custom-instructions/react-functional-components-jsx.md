# React: Functional Components & JSX

Understanding the basics of React components and JSX syntax.

## Core Concept: Components

React applications are built using reusable pieces of code called **components**. They encapsulate UI structure, logic, and state. Modern React primarily uses **functional components**.

*   **Functional Component:** A JavaScript function that accepts an optional `props` object as input and returns React elements (typically written using JSX) describing what should appear on the screen.

```jsx
// Simple functional component
function Welcome(props) {
  // Props are received as an object argument
  return <h1>Hello, {props.name}</h1>;
}

// Usage: <Welcome name="Alice" />
```

*   **Props (Properties):** Data passed down from a parent component to a child component. They are read-only within the child component. Use object destructuring for cleaner access.
    ```jsx
    function UserProfile({ name, age, children }) { // Destructuring props
      return (
        <div>
          <h2>{name}</h2>
          <p>Age: {age}</p>
          <div>{children}</div> {/* Renders content passed between tags */}
        </div>
      );
    }
    // Usage: <UserProfile name="Bob" age={30}><p>User Bio</p></UserProfile>
    ```
*   **Composition:** Components can render other components, allowing you to build complex UIs from smaller, reusable parts.

## JSX (JavaScript XML)

*   **Syntax Extension:** JSX allows you to write HTML-like syntax directly within your JavaScript code. It makes describing UI structures more intuitive.
*   **Not HTML:** While it looks like HTML, JSX is transpiled (by tools like Babel) into standard `React.createElement()` calls.
*   **Embedding Expressions:** Use curly braces `{}` to embed any valid JavaScript expression within JSX.
    ```jsx
    const userName = "Charlie";
    const element = <h1>Hello, {userName.toUpperCase()}!</h1>; // Embed variable
    const calculation = <p>2 + 2 = {2 + 2}</p>; // Embed calculation
    ```
*   **Attributes:** JSX uses camelCase for most HTML attribute names (`className` instead of `class`, `htmlFor` instead of `for`). Boolean attributes can be passed as `{true}` or just the attribute name (e.g., `disabled`). String literals use quotes (`alt="Description"`), while expressions use curly braces (`width={imageWidth}`).
    ```jsx
    <img src={user.avatarUrl} alt="User avatar" className="profile-pic" />
    <input type="text" value={inputValue} onChange={handleChange} required />
    <button disabled={isLoading}>Submit</button>
    ```
*   **Single Root Element:** A component must return a *single* root JSX element. If you need multiple elements at the top level, wrap them in a container like a `<div>` or use a **Fragment** (`<>...</>` or `<React.Fragment>...</React.Fragment>`).
    ```jsx
    // Correct: Single root div
    function UserInfo() {
      return (
        <div>
          <h2>User</h2>
          <p>Details...</p>
        </div>
      );
    }

    // Correct: Using Fragment shorthand
    function UserDetails() {
      return (
        <>
          <dt>Name:</dt>
          <dd>Alice</dd>
          <dt>Email:</dt>
          <dd>alice@example.com</dd>
        </>
      );
    }
    ```
*   **Comments:** Use JavaScript comments within curly braces: `{/* This is a JSX comment */}`.

Functional components returning JSX are the standard way to build UIs in modern React. Understanding props for data flow and JSX syntax for describing the UI structure is fundamental.

*(Refer to the official React documentation on Components, Props, and JSX.)*