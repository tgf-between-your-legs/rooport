# React Ref Hooks: `useRef` & `forwardRef`

Accessing DOM nodes directly and managing mutable values that don't trigger re-renders.

## `useRef(initialValue)`

*   **Purpose:** Returns a mutable `ref` object whose `.current` property is initialized to the passed `initialValue`. The returned object persists for the full lifetime of the component.
*   **Two Main Uses:**
    1.  **Accessing DOM Nodes:** Attach the `ref` object to a DOM element's `ref` attribute to get direct access to that node.
    2.  **Storing Mutable Values:** Keep track of a value that can change over time but whose change **should not** trigger a component re-render (unlike state).
*   **Syntax:**
    ```jsx
    import React, { useRef, useEffect, useState } from 'react';

    function TextInputWithFocusButton() {
      // 1. Initialize ref for DOM node access (initial value is null)
      const inputRef = useRef(null);

      // 2. Initialize ref for storing a mutable value (e.g., timer ID)
      const timerRef = useRef(null);
      const [count, setCount] = useState(0); // Example state

      // Accessing DOM node in an effect
      useEffect(() => {
        // Focus the input element on mount
        inputRef.current?.focus(); // Use optional chaining ?. as ref might be null initially

        // Example using mutable ref for timer
        timerRef.current = setInterval(() => {
          console.log('Timer tick');
          // Note: Accessing state here might use stale values if count isn't in deps
        }, 1000);

        // Cleanup timer on unmount
        return () => {
          if (timerRef.current) {
            clearInterval(timerRef.current);
          }
        };
      }, []); // Empty dependency array: run only on mount/unmount

      const handleFocusClick = () => {
        // Directly manipulate the DOM node via the ref
        inputRef.current?.focus();
      };

      return (
        <div>
          {/* Attach ref to the DOM element */}
          <input ref={inputRef} type="text" />
          <button onClick={handleFocusClick}>Focus the input</button>
        </div>
      );
    }
    ```
*   **Key Points:**
    *   Mutating `ref.current` **does not** cause a re-render.
    *   Changes to `ref.current` are synchronous (unlike state updates).
    *   Use refs for imperative actions (focusing input, triggering animations, measuring DOM nodes) or when you need a persistent mutable value outside of React's state system.
    *   Avoid overusing refs for things that can be handled declaratively with state and props.

## `forwardRef(render)`

*   **Purpose:** Lets a component expose a DOM node within it to its parent component using `ref`. Necessary when a parent needs direct access to a child's DOM node (e.g., for focusing, measuring).
*   **Syntax:** Wrap your component definition in `React.forwardRef`. The component function receives `props` as the first argument and `ref` as the second argument. Forward the `ref` to the desired DOM node inside the component.
    ```jsx
    import React, { useRef, forwardRef } from 'react';

    // Child component that forwards the ref to its input element
    const FancyInput = forwardRef((props, ref) => {
      return (
        <div>
          <label>{props.label}</label>
          {/* Forward the ref received from the parent to the actual input */}
          <input ref={ref} {...props} />
        </div>
      );
    });

    // Parent component that uses the ref
    function ParentForm() {
      const inputRef = useRef(null);

      const handleFocus = () => {
        inputRef.current?.focus();
      };

      return (
        <div>
          {/* Pass the ref to the child component */}
          <FancyInput ref={inputRef} label="My Input:" placeholder="Enter text" />
          <button onClick={handleFocus}>Focus Child Input</button>
        </div>
      );
    }
    ```
*   **When to Use:** When creating reusable components (like custom inputs, buttons, etc.) where the parent component might need direct access to the underlying DOM node.

## `useImperativeHandle(ref, createHandle, dependencies?)`

*   **Purpose:** Customizes the instance value that is exposed when using `ref` with `forwardRef`. Instead of exposing the entire DOM node, you can expose a specific set of imperative functions (e.g., `focus()`, `clear()`).
*   **Usage:** Use inside a component wrapped with `forwardRef`.
    ```jsx
    import React, { useRef, forwardRef, useImperativeHandle } from 'react';

    const FancyInputWithMethods = forwardRef((props, ref) => {
      const internalInputRef = useRef(null);

      // Expose only specific methods to the parent via the ref
      useImperativeHandle(ref, () => ({
        focusInput: () => {
          internalInputRef.current?.focus();
        },
        clearInput: () => {
          if (internalInputRef.current) {
            internalInputRef.current.value = '';
          }
        }
        // Not exposing the full input node directly
      }), []); // Dependencies if methods rely on props/state

      return (
        <div>
          <label>{props.label}</label>
          <input ref={internalInputRef} {...props} />
        </div>
      );
    });

    // Parent usage
    function ParentUsingImperativeHandle() {
      const fancyInputRef = useRef(null);

      const handleFocus = () => {
        fancyInputRef.current?.focusInput(); // Call the exposed method
      };
      const handleClear = () => {
        fancyInputRef.current?.clearInput(); // Call the exposed method
      };

      return (
        <div>
          <FancyInputWithMethods ref={fancyInputRef} label="Input:" />
          <button onClick={handleFocus}>Focus Child</button>
          <button onClick={handleClear}>Clear Child</button>
        </div>
      );
    }
    ```
*   **When to Use:** When you want to limit the imperative API exposed by your component via `ref`, rather than exposing the entire DOM node.

*(Refer to the official React documentation for `useRef`, `forwardRef`, and `useImperativeHandle`: https://react.dev/reference/react)*