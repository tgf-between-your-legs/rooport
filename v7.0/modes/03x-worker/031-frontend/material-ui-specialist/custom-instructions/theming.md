# MUI Theming (Core & Joy UI)

Guide to customizing the theme in MUI Core (v5+) and Joy UI.

## Core Concept

MUI theming allows you to define a consistent design language (colors, typography, spacing, component styles) across your application.

*   **MUI Core:** Uses `createTheme` and `<ThemeProvider>`. Based on Material Design principles but highly customizable.
*   **Joy UI:** Uses `extendTheme` and `<CssVarsProvider>`. Has its own design system and relies heavily on CSS variables for theming and mode switching (light/dark).

## MUI Core Theming (`@mui/material`)

1.  **Create Theme:** Use `createTheme` from `@mui/material/styles`. Define overrides for `palette`, `typography`, `spacing`, `breakpoints`, `shape`, `components`, etc.
    ```javascript
    // src/theme.js (or .ts)
    import { createTheme } from '@mui/material/styles';
    import { red } from '@mui/material/colors';

    const theme = createTheme({
      palette: {
        primary: {
          main: '#556cd6', // Example primary color
        },
        secondary: {
          main: '#19857b',
        },
        error: {
          main: red.A400,
        },
        // mode: 'light', // Can set default mode here
      },
      typography: {
        fontFamily: '"Roboto", "Helvetica", "Arial", sans-serif',
        fontSize: 14,
        h1: {
          fontSize: '2.5rem',
        },
      },
      spacing: 8, // Base spacing unit (default is 8px)
      shape: {
        borderRadius: 4,
      },
      components: {
        // Global style overrides for specific components
        MuiButton: {
          defaultProps: {
            disableElevation: true, // Example: Disable elevation globally for Buttons
          },
          styleOverrides: {
            root: { // Style the root element
              textTransform: 'none', // Example: Default to normal case buttons
              padding: '10px 20px',
            },
            containedPrimary: { // Style specific variant/color
              '&:hover': {
                backgroundColor: '#3e52a3',
              },
            },
          },
          variants: [ // Define custom variants
            {
              props: { variant: 'dashed', color: 'secondary' },
              style: {
                border: `2px dashed ${red[500]}`,
              },
            },
          ],
        },
        // Override other components... MuiTextField, MuiCard, etc.
      },
    });

    export default theme;
    ```
2.  **Apply Theme:** Wrap your application root with `<ThemeProvider>` from `@mui/material/styles` and pass the created theme object. Add `<CssBaseline />` to apply baseline styles.
    ```jsx
    // src/App.js (or equivalent root)
    import * as React from 'react';
    import { ThemeProvider } from '@mui/material/styles';
    import CssBaseline from '@mui/material/CssBaseline';
    import theme from './theme';
    // ... other imports

    function App() {
      return (
        <ThemeProvider theme={theme}>
          <CssBaseline /> {/* Applies baseline styles */}
          {/* Rest of your application */}
        </ThemeProvider>
      );
    }
    ```

## Joy UI Theming (`@mui/joy`)

1.  **Create Theme:** Use `extendTheme` from `@mui/joy/styles`. Joy UI uses CSS variables extensively. Customizations often involve defining `colorSchemes` (for light/dark modes) and overriding tokens.
    ```javascript
    // src/theme.js (or .ts)
    import { extendTheme } from '@mui/joy/styles';

    const theme = extendTheme({
      colorSchemes: {
        light: {
          palette: {
            primary: {
              solidBg: '#0B6BCB', // Main solid background for primary
              solidHoverBg: '#0959A9',
              // ... other shades: solidActiveBg, outlinedColor, outlinedBorder, etc.
              50: '#E3F2FD', // Lightest shade
              // ... 100, 200, ..., 900 (Darkest shade)
            },
            // Define neutral, danger, success, warning palettes similarly
            background: {
              body: 'var(--joy-palette-neutral-50)', // Example using another token
              surface: '#fff',
            },
          },
        },
        dark: {
          palette: {
            primary: {
              solidBg: '#65B3F0',
              solidHoverBg: '#7CC0F3',
              // ... other shades
            },
            background: {
              body: 'var(--joy-palette-common-black)',
              surface: 'var(--joy-palette-neutral-900)',
            },
          },
        },
      },
      fontFamily: {
        body: '"Inter", var(--joy-fontFamily-fallback)', // Example font stack
        display: '"Poppins", var(--joy-fontFamily-fallback)',
      },
      typography: {
        h1: {
          fontSize: '3rem',
        },
      },
      radius: { // Border radius tokens
        sm: '4px',
        md: '8px',
        lg: '12px',
      },
      shadow: { // Shadow tokens
        sm: '0 1px 2px 0 rgba(0, 0, 0, 0.05)',
        md: '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)',
      },
      // Component overrides (less common than Core, often done via sx or styled)
      // components: {
      //   JoyButton: {
      //     styleOverrides: {
      //       root: ({ ownerState, theme }) => ({
      //         ...(ownerState.size === 'lg' && {
      //           padding: '12px 24px',
      //         }),
      //       }),
      //     },
      //   },
      // },
    });

    export default theme;
    ```
2.  **Apply Theme:** Wrap your application root with `<CssVarsProvider>` from `@mui/joy/styles`. Add `<CssBaseline />` from `@mui/joy`.
    ```jsx
    // src/App.js (or equivalent root)
    import * as React from 'react';
    import { CssVarsProvider } from '@mui/joy/styles';
    import CssBaseline from '@mui/joy/CssBaseline';
    import theme from './theme';
    // ... other imports

    function App() {
      return (
        <CssVarsProvider theme={theme} defaultMode="system"> {/* Handles light/dark mode */}
          <CssBaseline />
          {/* Rest of your application */}
        </CssVarsProvider>
      );
    }
    ```

*(Refer to the official MUI Theming documentation for Core and Joy UI for comprehensive details.)*