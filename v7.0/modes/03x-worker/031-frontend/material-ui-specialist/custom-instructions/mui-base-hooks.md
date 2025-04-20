# MUI Base Unstyled Components & Hooks

Guide to using MUI Base for building custom-designed components with MUI's accessibility and interaction logic.

## Core Concept

MUI Base provides unstyled ("headless") components and low-level hooks that handle complex logic like accessibility (ARIA attributes, focus management) and state management for common UI patterns. You provide the visual styling using any styling solution (CSS, Tailwind, Emotion, etc.).

This is useful when you need complete control over the component's appearance and structure, deviating significantly from Material Design or Joy UI's look and feel, but still want robust underlying functionality.

## Key Packages

*   `@mui/base`: Contains the unstyled components and hooks.

## Using Unstyled Components

These components render minimal (or no) default HTML structure or styles. You compose them and apply your own styles.

```jsx
import * as React from 'react';
import { Button as BaseButton } from '@mui/base/Button'; // Import unstyled component
import { styled } from '@mui/system'; // Or your preferred styling solution

// Example: Creating a custom styled button using MUI Base Button
const CustomButton = styled(BaseButton)(({ theme }) => `
  font-family: IBM Plex Sans, sans-serif;
  font-size: 0.875rem;
  line-height: 1.5;
  background-color: #007bff;
  color: white;
  border-radius: 8px;
  font-weight: 600;
  padding: 8px 16px;
  cursor: pointer;
  transition: all 150ms ease;
  border: none;

  &:hover {
    background-color: #0056b3;
  }

  &.base--active { // Class applied by BaseButton on active state
    background-color: #004085;
  }

  &.base--focusVisible { // Class applied for keyboard focus
    outline: 3px solid #a0cfff;
    outline-offset: 2px;
  }

  &.base--disabled { // Class applied when disabled
    background-color: #e0e0e0;
    color: #a0a0a0;
    cursor: not-allowed;
  }
`);

function MyComponent() {
  return <CustomButton onClick={() => console.log('Clicked!')}>Custom Styled Button</CustomButton>;
}
```
*   **Key Idea:** Import the component from `@mui/base/*`. Apply your styles targeting the component itself and the state classes provided by MUI Base (e.g., `.base--focusVisible`, `.base--disabled`, `.base--active`, `.base--expanded`).

## Using Hooks

Hooks provide the logic (state, event handlers, accessibility props) without rendering any DOM elements. You use these hooks in your own components to build the structure and apply the returned props.

```jsx
import * as React from 'react';
import { useSwitch, UseSwitchParameters } from '@mui/base/useSwitch';
import { styled } from '@mui/system';

// Example: Creating a custom Switch using the useSwitch hook
const SwitchRoot = styled('span')`/* ... styles for the container */`;
const SwitchInput = styled('input')`/* ... styles for the hidden input */`;
const SwitchThumb = styled('span')`/* ... styles for the thumb */`;

function CustomSwitch(props: UseSwitchParameters) {
  const { getInputProps, checked, disabled, focusVisible, readOnly } = useSwitch(props);

  const stateClasses = {
    'base--checked': checked,
    'base--disabled': disabled,
    'base--focusVisible': focusVisible,
    'base--readOnly': readOnly,
  };

  return (
    <SwitchRoot className={/* Combine stateClasses into string */ Object.entries(stateClasses).filter(([, active]) => active).map(([className]) => className).join(' ')}>
      <SwitchThumb className={/* stateClasses */} />
      <SwitchInput {...getInputProps()} /> {/* Apply props from hook */}
    </SwitchRoot>
  );
}

function MyComponent() {
  return <CustomSwitch defaultChecked />;
}

```
*   **Key Idea:** Import the hook (e.g., `useSwitch`, `useButton`, `useSlider`, `useTabsList`, etc.) from `@mui/base/*`. Call the hook with necessary parameters. Spread the returned props (`getInputProps`, `getRootProps`, etc.) onto your custom DOM elements. Use the returned state (`checked`, `disabled`, `focusVisible`) to apply conditional styles or classes.

## Common Unstyled Components & Hooks

*   **Button:** `<Button>`, `useButton`
*   **Input:** `<Input>`, `useInput`
*   **Slider:** `<Slider>`, `useSlider`
*   **Switch:** `<Switch>`, `useSwitch`
*   **Select:** `<Select>`, `useSelect`, `<Option>`, `useOption`
*   **Tabs:** `<Tabs>`, `useTabs`, `<TabsList>`, `useTabsList`, `<Tab>`, `useTab`, `<TabPanel>`, `useTabPanel`
*   **Menu:** `<Menu>`, `useMenu`, `<MenuItem>`, `useMenuItem` (often used with Popper)
*   **Popper:** `<Popper>`, `usePopper` (for positioning floating elements)
*   ... and many others.

## Benefits

*   **Maximum Design Control:** Build components that look exactly how you want.
*   **Accessibility & Interactions:** Leverage MUI's built-in accessibility features (ARIA, focus management) and interaction logic without reinventing the wheel.
*   **Framework Agnostic Styling:** Use any styling solution (Tailwind, plain CSS, CSS-in-JS).

*(Refer to the official MUI Base documentation for details on specific components and hooks: https://mui.com/base-ui/getting-started/)*