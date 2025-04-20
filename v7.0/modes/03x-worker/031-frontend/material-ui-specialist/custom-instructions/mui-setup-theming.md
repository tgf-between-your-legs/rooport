# Material UI: Theming (MUI Core & Joy UI)

Customizing the look and feel of MUI components using themes.

## Core Concept: Theming

MUI provides a powerful theming system that allows you to centrally define colors, typography, spacing, breakpoints, component defaults, and more, ensuring consistency across your application.

*   **MUI Core:** Uses `createTheme` and `<ThemeProvider>`. Relies on a single theme object.
*   **Joy UI:** Uses `extendTheme` and `<CssVarsProvider>`. Supports CSS variables for dynamic changes (like dark/light mode) without needing multiple theme objects.

## MUI Core Theming (`@mui/material`)

1.  **Create Theme:** Use `createTheme` from `@mui/material/styles` to define your theme object. You can customize various keys:
    *   `palette`: Define primary, secondary, error, warning, info, success colors, background colors, text colors. Each color object has `main`, `light`, `dark`, `contrastText`.
    *   `typography`: Define font family, sizes (`h1`-`h6`, `body1`, `button`, etc.), weights.
    *   `spacing`: Base spacing unit (default 8px). Use `theme.spacing(multiplier)` in styles.
    *   `breakpoints`: Customize screen size breakpoints (`xs`, `sm`, `md`, `lg`, `xl`).
    *   `shape`: Border radius values.
    *   `components`: Override default props and styles for specific MUI components globally.
    *   `zIndex`: Manage z-index values.

    ```typescript
    // src/theme.ts (Example)
    import { createTheme, responsiveFontSizes } from '@mui/material/styles';
    import { red } from '@mui/material/colors';

    // Create a theme instance.
    let theme = createTheme({
      palette: {
        primary: {
          main: '#556cd6', // Custom primary color
        },
        secondary: {
          main: '#19857b',
        },
        error: {
          main: red.A400,
        },
        background: {
          default: '#f4f6f8',
        }
      },
      typography: {
        fontFamily: '"Roboto", "Helvetica", "Arial", sans-serif',
        h1: {
          fontSize: '2.5rem',
          fontWeight: 500,
        },
        // ... other typography variants
      },
      spacing: 8, // Base spacing unit (8px)
      shape: {
        borderRadius: 4,
      },
      components: {
        // Example: Override default props for MuiButton
        MuiButton: {
          defaultProps: {
            disableElevation: true, // Disable shadow by default
            variant: 'contained', // Default variant
          },
          styleOverrides: {
            // Example: Apply styles to the root element of contained buttons
            root: ({ ownerState, theme }) => ({
              ...(ownerState.variant === 'contained' &&
                ownerState.color === 'primary' && {
                  // Custom styles for primary contained buttons
                  // backgroundColor: theme.palette.primary.dark,
                  // '&:hover': {
                  //   backgroundColor: theme.palette.primary.main,
                  // },
              }),
              textTransform: 'none', // No uppercase text
              padding: theme.spacing(1, 3), // Use theme spacing
            }),
          },
        },
        // Override other components... MuiTextField, MuiAppBar, etc.
      },
    });

    // Optional: Make typography responsive
    theme = responsiveFontSizes(theme);

    export default theme;
    ```

2.  **Provide Theme:** Wrap your application's root component (e.g., in `_app.tsx` for Next.js Pages Router, `layout.tsx` for App Router, `main.tsx` for Vite) with `<ThemeProvider>` from `@mui/material/styles` and pass your created `theme` object. Add `<CssBaseline />` to apply baseline styles (like background color, box-sizing).

    ```typescript
    // Example: src/app/layout.tsx (Next.js App Router with ThemeRegistry)
    // See MUI docs for full ThemeRegistry implementation for SSR/caching
    import ThemeRegistry from './ThemeRegistry'; // Your custom registry component

    export default function RootLayout({ children }) {
      return (
        <html lang="en">
          <body>
            <ThemeRegistry options={{ key: 'mui' }}> {/* Wraps ThemeProvider & CssBaseline */}
              {children}
            </ThemeRegistry>
          </body>
        </html>
      );
    }

    // Example: src/main.tsx (Vite)
    // import React from 'react';
    // import ReactDOM from 'react-dom/client';
    // import { ThemeProvider } from '@mui/material/styles';
    // import CssBaseline from '@mui/material/CssBaseline';
    // import theme from './theme';
    // import App from './App';

    // ReactDOM.createRoot(document.getElementById('root')!).render(
    //   <React.StrictMode>
    //     <ThemeProvider theme={theme}>
    //       <CssBaseline /> {/* Apply baseline styles */}
    //       <App />
    //     </ThemeProvider>
    //   </React.StrictMode>,
    // );
    ```

## Joy UI Theming (`@mui/joy`)

Joy UI uses CSS variables for theming, making dynamic changes like dark/light mode easier.

1.  **Create Theme:** Use `extendTheme` from `@mui/joy/styles`. It merges your customizations with the default Joy theme. Configure similar keys (`palette`, `typography`, etc.), but also `colorSchemes`.
2.  **Provide Theme:** Wrap your app with `<CssVarsProvider>` from `@mui/joy/styles` and pass your theme. It handles applying CSS variables and theme switching. Use `<CssBaseline />` from `@mui/joy` as well.

```typescript
// src/joyTheme.ts (Example)
import { extendTheme } from '@mui/joy/styles';

const theme = extendTheme({
  colorSchemes: {
    light: {
      palette: {
        primary: {
          solidBg: '#0b6bcb', // Example override
          // ... other primary variants
        },
      },
    },
    dark: {
      palette: {
        primary: {
          solidBg: '#65a3d3',
          // ...
        },
        background: {
          body: '#121212',
        }
      },
    },
  },
  fontFamily: {
    body: 'system-ui, sans-serif',
  },
  // ... other customizations
});

export default theme;

// Example: src/main.tsx (Vite with Joy UI)
// import React from 'react';
// import ReactDOM from 'react-dom/client';
// import { CssVarsProvider } from '@mui/joy/styles';
// import CssBaseline from '@mui/joy/CssBaseline';
// import joyTheme from './joyTheme';
// import App from './App'; // Your app using Joy components

// ReactDOM.createRoot(document.getElementById('root')!).render(
//   <React.StrictMode>
//     <CssVarsProvider theme={joyTheme} defaultMode="system"> {/* Handles light/dark */}
//       <CssBaseline />
//       <App />
//     </CssVarsProvider>
//   </React.StrictMode>,
// );
```

Theming is central to customizing MUI. Define your design tokens (colors, typography, spacing) in the theme object for application-wide consistency.

*(Refer to the official MUI Theming documentation for Core and Joy UI.)*