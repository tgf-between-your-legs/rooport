# Material UI: Introduction to Joy UI

Overview of Joy UI, MUI's library for custom design systems.

## Core Concept

Joy UI is a library of beautifully designed React UI components, part of the MUI ecosystem but distinct from MUI Core (Material Design). It's designed to be a great starting point for building **custom design systems** quickly, offering a different aesthetic and more direct customization via CSS variables.

**Key Differences from MUI Core:**

*   **Design System:** Implements its own flexible, modern design system, not strictly Material Design.
*   **Styling:** Primarily customized using **CSS variables**. Uses `<CssVarsProvider>` instead of `<ThemeProvider>`.
*   **Component Set:** Offers a similar range of components (buttons, inputs, cards, etc.) but with potentially different APIs and styling approaches compared to MUI Core.
*   **Default Look:** Has a distinct, often more "playful" or "modern" default aesthetic compared to Material Design.

## Installation

Joy UI components and styling utilities are in the `@mui/joy` package. It still relies on Emotion.

```bash
# Using npm
npm install @mui/joy @emotion/react @emotion/styled

# Using yarn
yarn add @mui/joy @emotion/react @emotion/styled
```

## Setup (`<CssVarsProvider>`)

Joy UI requires wrapping your application with `<CssVarsProvider>` from `@mui/joy/styles` to enable its CSS variable-based theming and automatic dark/light mode switching.

1.  **Create Theme (Optional):** Use `extendTheme` from `@mui/joy/styles` to customize the default Joy theme (palette, typography, variants, etc.). Define customizations within `colorSchemes.light` and `colorSchemes.dark`.
2.  **Provide Theme:** Wrap your app root with `<CssVarsProvider>` and pass your custom `theme`. Use `<CssBaseline />` from `@mui/joy` to apply base styling.

```typescript
// src/joyTheme.ts (Optional theme customization)
import { extendTheme } from '@mui/joy/styles';

const joyTheme = extendTheme({
  fontFamily: {
    body: '"Inter", sans-serif', // Example: Set custom font
  },
  colorSchemes: {
    light: {
      palette: {
        primary: {
          solidBg: '#007FFF', // Example: Set primary button background for light mode
          // ... other variants 50, 100, ..., 900
        },
      },
    },
    dark: {
      palette: {
        primary: {
          solidBg: '#3399FF', // Example: Set primary button background for dark mode
        },
        background: {
          body: '#1A1A1A', // Example: Dark background
        }
      },
    },
  },
  // Add component overrides if needed
  // components: { ... }
});

export default joyTheme;

// src/main.tsx (Vite example)
import React from 'react';
import ReactDOM from 'react-dom/client';
import { CssVarsProvider, extendTheme } from '@mui/joy/styles';
import CssBaseline from '@mui/joy/CssBaseline';
// import joyTheme from './joyTheme'; // Import custom theme if created
import App from './App'; // Your app using Joy components

// const theme = extendTheme(); // Or use default theme
// const theme = joyTheme; // Or use custom theme

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    {/* defaultMode="system" enables auto dark/light mode based on OS preference */}
    <CssVarsProvider
      // theme={theme} // Provide custom theme if you have one
      defaultMode="system"
    >
      <CssBaseline /> {/* Joy UI's baseline */}
      <App />
    </CssVarsProvider>
  </React.StrictMode>,
);
```

## Using Joy UI Components

Import components from `@mui/joy` and use them similarly to MUI Core components. Styling often relies more heavily on the `variant` (`solid`, `soft`, `outlined`, `plain`) and `color` props, which map directly to theme CSS variables. The `sx` prop is also available for overrides.

```jsx
import React from 'react';
import Button from '@mui/joy/Button'; // Import from @mui/joy
import Input from '@mui/joy/Input';
import Checkbox from '@mui/joy/Checkbox';
import Sheet from '@mui/joy/Sheet'; // Similar to Paper/Box
import Typography from '@mui/joy/Typography';
import Stack from '@mui/joy/Stack';
import DarkModeIcon from '@mui/icons-material/DarkMode';
import { useColorScheme } from '@mui/joy/styles'; // Hook for mode switching

function ModeToggle() {
  const { mode, setMode } = useColorScheme();
  return (
    <Button onClick={() => setMode(mode === 'dark' ? 'light' : 'dark')}>
      <DarkModeIcon /> Toggle Mode
    </Button>
  );
}


function JoyDemo() {
  return (
    <Sheet sx={{ p: 4, borderRadius: 'md', boxShadow: 'md' }}> {/* Sheet as container */}
      <Typography level="h3" component="h1" sx={{ mb: 2 }}>Joy UI Demo</Typography>
      <Stack spacing={2}>
        <Input placeholder="Type in here…" />
        <Checkbox label="I agree" defaultChecked />
        <Button variant="solid" color="primary">Solid Button</Button>
        <Button variant="soft" color="success">Soft Button</Button>
        <Button variant="outlined" color="warning">Outlined Button</Button>
        <Button variant="plain" color="danger">Plain Button</Button>
        <ModeToggle />
      </Stack>
    </Sheet>
  );
}

export default JoyDemo;
```

Joy UI offers a distinct alternative to MUI Core, particularly well-suited for projects needing a unique design system or leveraging CSS variables extensively, especially for features like dark/light mode toggling.

*(Refer to the official Joy UI documentation: https://mui.com/joy-ui/getting-started/)*