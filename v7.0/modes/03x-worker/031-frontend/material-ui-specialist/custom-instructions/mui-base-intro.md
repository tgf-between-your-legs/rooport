# Material UI: Introduction to MUI Base

Using MUI Base for unstyled components and hooks.

## Core Concept

MUI Base is the foundation upon which MUI Core (Material Design) and Joy UI are built. It provides a set of **unstyled** React components and low-level hooks for building custom design systems from scratch or creating highly customized components without inheriting Material Design or Joy UI styles.

**Key Features:**

*   **Unstyled Components:** Components like `<Button>`, `<Input>`, `<Select>`, `<Slider>`, `<Switch>` are provided without any default visual styles. You apply all styling yourself (using CSS, Tailwind, Emotion, styled-components, etc.).
*   **Accessibility Included:** Components handle essential accessibility features (ARIA attributes, keyboard navigation) out-of-the-box.
*   **Functionality Hooks:** Low-level hooks (e.g., `useButton`, `useSwitch`, `useSelect`) provide the state management and accessibility logic, allowing you to build completely custom component structures around them.
*   **Design System Agnostic:** Not tied to Material Design or Joy UI aesthetics. Build *your* design system.
*   **Smaller Bundle Size:** Using only MUI Base results in a smaller bundle size compared to including the full MUI Core or Joy UI libraries if you don't need their pre-styled components.

## Installation

MUI Base components are available in the `@mui/base` package.

```bash
# Using npm
npm install @mui/base

# Using yarn
yarn add @mui/base
```

## Using Unstyled Components

Import components from `@mui/base` and apply your own classes or styling solution.

```jsx
import React from 'react';
import { Button as BaseButton } from '@mui/base/Button'; // Import unstyled Button
import { Input as BaseInput } from '@mui/base/Input';   // Import unstyled Input
import clsx from 'clsx'; // Utility for conditional classes (optional)

// Example custom styles (e.g., using CSS Modules or Tailwind)
// Assume styles.myButton, styles.myInput exist
import styles from './MyComponent.module.css';

function BaseComponentsDemo() {
  return (
    <div>
      <h1>MUI Base Unstyled Components</h1>

      {/* Apply custom classes for styling */}
      <BaseButton className={clsx(styles.myButton, styles.primary)}>
        Custom Styled Button
      </BaseButton>

      <BaseInput
        className={styles.myInput}
        placeholder="Enter text..."
        slotProps={{ // Customize internal slots if needed
          input: {
            className: styles.myInputInner, // Style the actual <input> element
          }
        }}
      />
    </div>
  );
}

export default BaseComponentsDemo;
```

## Using Functionality Hooks

Hooks provide the logic and accessibility props, giving you complete control over the rendered HTML structure.

```jsx
import React from 'react';
import { useSwitch, UseSwitchParameters } from '@mui/base/useSwitch'; // Import hook and types
import { styled } from '@mui/system'; // Example using MUI System for styling

// Custom styling for the switch elements
const SwitchRoot = styled('span')`/* ... styles ... */`;
const SwitchInput = styled('input')`/* ... styles ... */`;
const SwitchThumb = styled('span')`/* ... styles ... */`;
const SwitchTrack = styled('span')`/* ... styles ... */`;

// Custom Switch component built using the hook
function MyCustomSwitch(props: UseSwitchParameters) {
  const { getInputProps, checked, disabled, focusVisible } = useSwitch(props);

  const stateClasses = {
    'checked': checked,
    'disabled': disabled,
    'focusVisible': focusVisible,
  };

  return (
    <SwitchRoot className={clsx(stateClasses)}>
      <SwitchTrack>
        <SwitchThumb className={clsx(stateClasses)} />
      </SwitchTrack>
      <SwitchInput {...getInputProps()} aria-label="Demo switch" /> {/* Spread accessibility props */}
    </SwitchRoot>
  );
}

function BaseHooksDemo() {
  return (
    <div>
      <h1>MUI Base Hooks</h1>
      <MyCustomSwitch defaultChecked />
      <MyCustomSwitch />
      <MyCustomSwitch disabled />
    </div>
  );
}

// Utility like clsx helps manage conditional classes
import clsx from 'clsx';

export default BaseHooksDemo;
```

## When to Use MUI Base

*   When building a completely custom design system not based on Material Design or Joy UI.
*   When you need full control over the HTML structure and styling of components.
*   When you want the accessibility and state logic provided by MUI but without the associated styles.
*   When minimizing bundle size is a critical requirement and you don't need the full styled component libraries.

MUI Base offers a powerful, flexible foundation for building accessible and functional React components with any styling approach.

*(Refer to the official MUI Base documentation: https://mui.com/base-ui/)*