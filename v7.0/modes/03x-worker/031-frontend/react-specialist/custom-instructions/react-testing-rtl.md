# React: Testing with React Testing Library (RTL)

Writing tests for React components focused on user behavior using React Testing Library.

## Core Concept: Testing User Behavior

React Testing Library (RTL) encourages writing tests that resemble how users interact with your application, rather than focusing on internal implementation details. This leads to more resilient tests that don't break easily during refactoring.

**Guiding Principles:**

*   **Query by Accessibility:** Find elements the way users would (by visible text, label, role, etc.). Avoid querying by implementation details like CSS classes or test IDs unless necessary.
*   **Interact like a User:** Simulate user events (clicks, typing) using the `@testing-library/user-event` library.
*   **Observe the Result:** Assert based on what the user would see or experience (e.g., text appearing/disappearing, elements becoming enabled/disabled).
*   **Accessible Queries:** RTL's preferred queries (`getByRole`, `getByLabelText`, `getByText`, etc.) inherently push you towards writing more accessible components.

**Common Setup:** Often used with a test runner like Jest and `jest-dom` for helpful DOM assertions. Create React App, Next.js, and Vite templates often include this setup.

## Key RTL APIs

Import functions from `@testing-library/react`.

*   **`render(ui)`:** Renders a React element (`ui`) into a container attached to `document.body`. Returns an object with query functions and utilities.
*   **Query Functions:** Used to find elements in the rendered output. They throw an error if no element or multiple elements are found (unless using `queryBy*` or `findAllBy*`).
    *   **`getBy*`:** Find a single element. Throws error if none or multiple found.
    *   **`queryBy*`:** Find a single element. Returns `null` if none found, throws if multiple found. Useful for asserting an element is *not* present.
    *   **`findBy*`:** Find a single element. Returns a **Promise** that resolves when the element appears (waits for async changes). Rejects if not found after a timeout.
    *   **`getAllBy*`:** Find *all* matching elements. Throws if none found.
    *   **`queryAllBy*`:** Find *all* matching elements. Returns `[]` if none found.
    *   **`findAllBy*`:** Find *all* matching elements. Returns a **Promise** that resolves when at least one element appears. Rejects if none found after a timeout.
*   **Query Priorities (Recommended Order):**
    1.  `*ByRole`: Most accessible (e.g., `getByRole('button', { name: /submit/i })`).
    2.  `*ByLabelText`: For form fields associated with a `<label>`.
    3.  `*ByPlaceholderText`: For inputs with placeholder text.
    4.  `*ByText`: Finds elements by their text content.
    5.  `*ByDisplayValue`: Finds form elements by their current value.
    6.  `*ByAltText`: For images.
    7.  `*ByTitle`: For elements with a `title` attribute.
    8.  `*ByTestId`: **Last resort.** Use `data-testid` attribute if you cannot query accessibly.
*   **`screen` Object:** A convenient object pre-bound with all query functions applied to `document.body`. Often preferred over destructuring queries from `render`. `import { screen } from '@testing-library/react';`
*   **`waitFor(callback, [options])`:** Waits for assertions within the callback to pass (useful for async updates).
*   **`within(element)`:** Scopes query functions to search only within a specific element.

## `@testing-library/user-event`

*   **Purpose:** Simulates user interactions more realistically than RTL's built-in `fireEvent`. Recommended for triggering events.
*   **Import:** `import userEvent from '@testing-library/user-event';`
*   **API:** Provides methods like `userEvent.click(element)`, `userEvent.type(element, text)`, `userEvent.keyboard(text)`, `userEvent.selectOptions(element, value)`, etc. Returns Promises.

## Example Test (using Jest & RTL)

```typescript
// src/components/Counter.test.tsx
import React from 'react';
// Import render and screen
import { render, screen } from '@testing-library/react';
// Import userEvent
import userEvent from '@testing-library/user-event';
// Import jest-dom matchers (e.g., toBeInTheDocument)
import '@testing-library/jest-dom';

import Counter from './Counter'; // The component to test

describe('Counter Component', () => {
  test('renders initial count and increments on click', async () => {
    // Arrange: Render the component
    render(<Counter />);

    // Use userEvent setup for v14+
    const user = userEvent.setup();

    // Act & Assert: Find elements and check initial state
    // Use screen queries (preferred)
    const countElement = screen.getByText(/Count: 0/i); // Find element containing text "Count: 0" (case-insensitive)
    expect(countElement).toBeInTheDocument();

    const incrementButton = screen.getByRole('button', { name: /increment/i }); // Find button by accessible name
    expect(incrementButton).toBeInTheDocument();

    // Act: Simulate user clicking the button
    await user.click(incrementButton);

    // Assert: Check if the count updated in the DOM
    // Use findBy* or waitFor for potential async updates, though simple state updates are usually synchronous in tests
    expect(screen.getByText(/Count: 1/i)).toBeInTheDocument();
    // Assert initial count is gone (optional)
    expect(screen.queryByText(/Count: 0/i)).not.toBeInTheDocument();

    // Click again
    await user.click(incrementButton);
    expect(screen.getByText(/Count: 2/i)).toBeInTheDocument();
  });

  test('reset button sets count back to 0', async () => {
    render(<Counter initialCount={5} />); // Test with initial prop
    const user = userEvent.setup();

    expect(screen.getByText(/Count: 5/i)).toBeInTheDocument();

    const resetButton = screen.getByRole('button', { name: /reset/i });
    await user.click(resetButton);

    expect(screen.getByText(/Count: 0/i)).toBeInTheDocument();
    expect(screen.queryByText(/Count: 5/i)).not.toBeInTheDocument();
  });
});
```

Writing tests with RTL focuses on ensuring your components work as users expect, leading to more confidence in your UI and less brittle tests. Prioritize accessible queries and simulate user interactions with `user-event`.

*(Refer to the official React Testing Library and user-event documentation.)*