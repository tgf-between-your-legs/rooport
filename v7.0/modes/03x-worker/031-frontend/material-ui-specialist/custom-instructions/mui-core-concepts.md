# Material UI: Core Concepts (MUI Core v5+)

Introduction to MUI Core components and setup.

## Core Concept

MUI Core (primarily the `@mui/material` package) provides a comprehensive suite of React components that implement Google's Material Design system. It offers pre-built, customizable components for layout, inputs, navigation, data display, feedback, and more.

**Key Features:**

*   **Material Design:** Components follow Material Design principles for look, feel, and interaction.
*   **React Components:** Built specifically for React applications.
*   **Customization:** Highly customizable through theming, the `sx` prop, and the `styled()` API.
*   **Accessibility:** Components are designed with accessibility (a11y) best practices in mind.
*   **Comprehensive:** Covers a wide range of common UI needs.

## Installation

MUI Core typically requires several packages:

1.  **Core Components:** `@mui/material`
2.  **Styling Engine:** `@emotion/react`, `@emotion/styled` (MUI v5 uses Emotion by default).
3.  **Icons (Optional but common):** `@mui/icons-material`

```bash
# Using npm
npm install @mui/material @emotion/react @emotion/styled
npm install @mui/icons-material

# Using yarn
yarn add @mui/material @emotion/react @emotion/styled
yarn add @mui/icons-material
```

## Basic Usage

1.  **Import Components:** Use named imports from `@mui/material` or `@mui/icons-material`.
2.  **Use in JSX:** Render components like standard React components, passing props for configuration and styling.

```jsx
import React from 'react';
import Button from '@mui/material/Button'; // Named import for Button
import Stack from '@mui/material/Stack';
import DeleteIcon from '@mui/icons-material/Delete'; // Example icon import
import SendIcon from '@mui/icons-material/Send';

function BasicMuiDemo() {
  return (
    <div>
      <h1>MUI Core Components</h1>
      <Stack spacing={2} direction="row"> {/* Stack for layout */}
        <Button variant="text">Text</Button>
        <Button variant="contained">Contained</Button>
        <Button variant="outlined">Outlined</Button>
        <Button variant="contained" color="secondary">Secondary</Button>
        <Button variant="outlined" startIcon={<DeleteIcon />}>
          Delete
        </Button>
        <Button variant="contained" endIcon={<SendIcon />}>
          Send
        </Button>
      </Stack>
    </div>
  );
}

export default BasicMuiDemo;
```

## Key Concepts Covered in Other Files

*   **Theming:** Customizing the overall look and feel (`mui-setup-theming.md`). Requires `<ThemeProvider>`.
*   **Styling:** Applying custom styles using the `sx` prop or `styled()` API (`mui-styling-solutions.md`).
*   **Layout:** Arranging components using `Box`, `Container`, `Grid`, `Stack` (`mui-layout-components.md`).
*   **Components:** Detailed usage of specific input, navigation, data display, and feedback components (see respective `.md` files).
*   **Joy UI & MUI Base:** Alternative component suites within the MUI ecosystem (see `mui-joy-ui-intro.md`, `mui-base-intro.md`).

MUI Core provides a robust foundation for building React applications following Material Design guidelines. Effective use involves understanding its component APIs, theming system, and styling approaches.

*(Refer to the official MUI Core documentation: https://mui.com/material-ui/)*