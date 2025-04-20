# React Testing with Jest & React Testing Library (RTL)

Writing unit and integration tests for React components.

## Core Philosophy (RTL)

*   **Test Like a User:** React Testing Library encourages writing tests that resemble how users interact with your application. Focus on querying the DOM in ways users would (by accessible roles, labels, text content) and asserting based on the visible output, rather than testing implementation details.
*   **Avoid Implementation Details:** Don't test component internal state, instance methods, or lifecycle methods directly. Focus on the relationship between user input/interaction and the resulting UI output.

## Setup

*   Typically requires installing `jest`, `@testing-library/react`, `@testing-library/jest-dom` (for custom matchers), and potentially `@testing-library/user-event` (for simulating user interactions). Create React App and Next.js often include Jest/RTL setup.
*   Configure Jest (e.g., `jest.config.js` or `package.json`) to work with React, JSX, TypeScript, CSS Modules, etc. (often handled by framework presets).

## Writing Tests (`*.test.js` or `*.test.tsx`)

```typescript
import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import userEvent from '@testing-library/user-event'; // Recommended for simulating user interactions
import '@testing-library/jest-dom'; // Import custom matchers

import Counter from './Counter'; // The component to test

// Test suite using describe()
describe('Counter Component', () => {

  // Individual test case using test() or it()
  test('renders initial count of 0', () => {
    // 1. Render the component
    render(<Counter />);

    // 2. Query the DOM for elements (using RTL queries)
    // getBy*: Finds one element, throws error if none or multiple found.
    // findBy*: Finds one element asynchronously, throws error if none or multiple found after timeout.
    // queryBy*: Finds one element, returns null if none found, throws error if multiple found.
    // getAllBy*, findAllBy*, queryAllBy*: Find multiple elements.

    // Prefer accessible queries:
    const countElement = screen.getByText(/Count: 0/i); // Find by text content (case-insensitive regex)
    const buttonElement = screen.getByRole('button', { name: /increment/i }); // Find by accessible role and name

    // 3. Assertions (using Jest `expect` and jest-dom matchers)
    expect(countElement).toBeInTheDocument();
    expect(buttonElement).toBeInTheDocument();
    expect(buttonElement).toBeEnabled();
  });

  test('increments count when button is clicked', async () => {
    // Setup userEvent (recommended over fireEvent for more realistic interactions)
    const user = userEvent.setup();

    // 1. Render
    render(<Counter />);

    // 2. Find elements
    const buttonElement = screen.getByRole('button', { name: /increment/i });

    // 3. Simulate user interaction
    await user.click(buttonElement);

    // 4. Assert the result
    // Use findBy* for asynchronous updates or if waiting for elements to appear
    const countElement = await screen.findByText(/Count: 1/i);
    expect(countElement).toBeInTheDocument();

    // Simulate another click
    await user.click(buttonElement);
    expect(await screen.findByText(/Count: 2/i)).toBeInTheDocument();
  });

  test('handles initial count prop', () => {
    render(<Counter initialCount={5} />);
    expect(screen.getByText(/Count: 5/i)).toBeInTheDocument();
  });

  // Example testing input change
  test('updates input value on change', async () => {
    const user = userEvent.setup();
    render(<MyInputComponent />); // Assume this has an input

    const input = screen.getByRole('textbox');
    await user.type(input, 'Hello World');

    expect(input).toHaveValue('Hello World');
  });

});
```

## Key RTL Queries (Priority Order)

1.  **`getByRole`**: Most accessible (e.g., `button`, `link`, `textbox`, `heading`). Use `name` option for accessible name (label, text content, `aria-label`).
2.  **`getByLabelText`**: Finds elements associated with a `<label>`.
3.  **`getByPlaceholderText`**: Finds inputs by placeholder.
4.  **`getByText`**: Finds elements by their text content.
5.  **`getByDisplayValue`**: Finds form elements by their current value.
6.  **`getByAltText`**: Finds images by `alt` text.
7.  **`getByTitle`**: Finds elements by `title` attribute.
8.  **`getByTestId`**: Finds elements by `data-testid` attribute (use as a last resort if other queries aren't feasible).

*   Replace `getBy` with `findBy` (async), `queryBy` (no error if not found), `getAllBy`, `findAllBy`, `queryAllBy` as needed.

## Simulating Events

*   **`@testing-library/user-event` (Recommended):** Simulates full user interactions more realistically than `fireEvent`. Use `await user.click(element)`, `await user.type(element, 'text')`, `await user.keyboard('{Enter}')`, etc.
*   **`fireEvent`:** Simulates single DOM events (e.g., `fireEvent.click(element)`, `fireEvent.change(input, { target: { value: 'new' } })`). Less realistic for complex interactions.

## Mocking

*   Use Jest's mocking capabilities (`jest.fn()`, `jest.mock()`) to mock functions, modules, or API calls (`fetch`) to isolate component behavior.

## Debugging

*   `screen.debug()`: Prints the current DOM structure to the console. Useful for inspecting what's rendered.
*   Use standard debugger statements or IDE debugging tools.

*(Refer to React Testing Library docs: https://testing-library.com/docs/react-testing-library/intro/ and Jest docs: https://jestjs.io/docs/getting-started)*