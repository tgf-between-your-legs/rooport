# React: Ref Hook (`useRef`, `forwardRef`)

Accessing DOM nodes directly and persisting mutable values without causing re-renders using refs.

## Core Concept: Refs

Refs provide a way to access DOM nodes or React elements created in the render method. They are also useful for keeping mutable values that persist across renders *without* triggering a re-render when they change (unlike state).

**Use Cases:**

*   Managing focus, text selection, or media playback imperatively.
*   Integrating with third-party DOM libraries.
*   Measuring DOM node dimensions or position.
*   Storing mutable values that don't affect the rendered output (e.g., interval IDs, subscription objects).

**Key Parts:**

1.  **`useRef(initialValue)`:**
    *   A hook that returns a mutable **ref object**.
    *   The returned object has a single property: `current`.
    *   `ref.current` is initialized to `initialValue`.
    *   **Important:** Mutating `ref.current` does **not** trigger a component re-render.
    *   If you pass the ref object to a DOM element via the `ref` attribute (`<div ref={myRef}>`), React will set `myRef.current` to the corresponding DOM node after the component mounts and set it back to `null` just before it unmounts.

2.  **`forwardRef(renderFn)`:**
    *   A higher-order component that lets your component receive a `ref` passed to it by a parent and forward it down to a specific DOM node or child component inside it.
    *   The `renderFn` receives `props` and `ref` as arguments.

## Implementation

**1. Accessing DOM Nodes:**

```jsx
import React, { useRef, useEffect } from 'react';

function FocusInput() {
  // Create a ref object
  const inputRef = useRef<HTMLInputElement>(null); // Initialize with null for DOM refs, provide type

  useEffect(() => {
    // Access the DOM node via inputRef.current
    // The node is guaranteed to exist after the component mounts
    inputRef.current?.focus(); // Optional chaining in case ref isn't attached
  }, []); // Empty dependency array: run only once on mount

  return (
    <div>
      <label htmlFor="myInput">Focus Me:</label>
      {/* Attach the ref to the input element */}
      <input ref={inputRef} type="text" id="myInput" />
    </div>
  );
}
```

**2. Storing Mutable Values (Not for Rendering):**

```jsx
import React, { useState, useEffect, useRef } from 'react';

function IntervalTimer() {
  const [seconds, setSeconds] = useState(0);
  // Use ref to store the interval ID
  const intervalRef = useRef<NodeJS.Timeout | null>(null);

  useEffect(() => {
    // Store the interval ID in ref.current
    // Mutating ref.current does NOT cause a re-render
    intervalRef.current = setInterval(() => {
      setSeconds(prev => prev + 1);
    }, 1000);

    // Cleanup function using the stored ref
    return () => {
      if (intervalRef.current) {
        clearInterval(intervalRef.current);
      }
    };
  }, []); // Run only on mount/unmount

  const handleStop = () => {
    if (intervalRef.current) {
      clearInterval(intervalRef.current);
      intervalRef.current = null; // Clear the ref if needed
    }
  };

  return (
    <div>
      <p>Timer: {seconds}</p>
      <button onClick={handleStop}>Stop Timer</button>
    </div>
  );
}
```

**3. Forwarding Refs (`forwardRef`):**

Used when a parent component needs a ref to a DOM node *inside* a child component.

```jsx
import React, { useRef, forwardRef } from 'react';

// Child component that accepts a forwarded ref
const FancyInput = forwardRef<HTMLInputElement, { label: string }>(
  ({ label, ...props }, ref) => { // Receive ref as second argument
    return (
      <div>
        <label>{label}</label>
        {/* Forward the ref to the actual input DOM node */}
        <input ref={ref} {...props} />
      </div>
    );
  }
);
// Add display name for DevTools
FancyInput.displayName = 'FancyInput';


// Parent component using the child and wanting a ref to the inner input
function ParentForm() {
  const fancyInputRef = useRef<HTMLInputElement>(null);

  const handleFocusClick = () => {
    fancyInputRef.current?.focus();
  };

  return (
    <div>
      {/* Pass the ref to the child component */}
      <FancyInput ref={fancyInputRef} label="My Fancy Input:" type="text" />
      <button onClick={handleFocusClick}>Focus Fancy Input</button>
    </div>
  );
}
```

## Considerations

*   **Avoid Overuse for DOM Manipulation:** Prefer declarative state updates (`useState`) to control UI changes whenever possible. Use refs for imperative actions (focus, media playback) that are hard to express declaratively.
*   **Timing:** `ref.current` is only populated with the DOM node *after* the component mounts. Accessing it during the initial render will result in `null`. Use `useEffect` to safely access `ref.current` after mount.
*   **No Re-renders:** Remember that changing `ref.current` does not trigger a re-render. If you need the UI to update when a value changes, use state (`useState`).

Refs are an escape hatch for interacting directly with the DOM or managing mutable values outside the standard React state flow. Use them judiciously when necessary.

*(Refer to the official React documentation on Refs and `forwardRef`.)*