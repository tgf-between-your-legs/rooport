TITLE: Installing Material UI with npm/pnpm/yarn
DESCRIPTION: Commands to install Material UI and its Emotion dependencies using different package managers.

LANGUAGE: bash
CODE:
npm install @mui/material@next @emotion/react @emotion/styled

LANGUAGE: bash
CODE:
pnpm add @mui/material@next @emotion/react @emotion/styled

LANGUAGE: bash
CODE:
yarn add @mui/material@next @emotion/react @emotion/styled

----------------------------------------

TITLE: Installing Joy UI Dependencies with Package Managers
DESCRIPTION: Commands to install Joy UI and its required Emotion dependencies using different package managers (npm, pnpm, yarn).

LANGUAGE: bash
CODE:
npm install @mui/joy @emotion/react @emotion/styled

LANGUAGE: bash
CODE:
pnpm add @mui/joy @emotion/react @emotion/styled

LANGUAGE: bash
CODE:
yarn add @mui/joy @emotion/react @emotion/styled

----------------------------------------

TITLE: Creating Custom Theme with Color Palette
DESCRIPTION: Demonstrates creating a custom theme with primary and secondary color palettes using createTheme function.

LANGUAGE: js
CODE:
import { createTheme } from '@mui/material/styles';
import { green, purple } from '@mui/material/colors';

const theme = createTheme({
  palette: {
    primary: {
      main: purple[500],
    },
    secondary: {
      main: green[500],
    },
  },
});

----------------------------------------

TITLE: Controlling Menu Open State in React
DESCRIPTION: This snippet shows how to control the open/close state of a menu programmatically from outside the Dropdown component. It uses the 'open' and 'onOpenChange' props of the Dropdown component.

LANGUAGE: jsx
CODE:
<Dropdown open={open} onOpenChange={handleOpenChange}>
  {/* Menu components */}
</Dropdown>

----------------------------------------

TITLE: Basic Tree-Shaking Import Example
DESCRIPTION: Demonstrates the standard named import syntax that supports tree-shaking in modern bundlers.

LANGUAGE: javascript
CODE:
import { Button, TextField } from '@mui/material';

----------------------------------------

TITLE: Creating Custom Color Theme in Material UI
DESCRIPTION: This snippet demonstrates how to create a custom color theme using the createTheme function from Material UI. It defines primary and secondary color palettes with light, main, dark, and contrastText variants.

LANGUAGE: js
CODE:
import { createTheme } from '@mui/material/styles';

const theme = createTheme({
  palette: {
    primary: {
      light: '#757ce8',
      main: '#3f50b5',
      dark: '#002884',
      contrastText: '#fff',
    },
    secondary: {
      light: '#ff7961',
      main: '#f44336',
      dark: '#ba000d',
      contrastText: '#000',
    },
  },
});

----------------------------------------

TITLE: Implementing Keyboard Navigation in React with MUI Base
DESCRIPTION: Demonstrates how to implement keyboard navigation in a MUI Base component. The code shows a Select component that can be navigated using various keyboard keys.

LANGUAGE: jsx
CODE:
{"demo": "KeyboardNavigation.js", "defaultCodeOpen": false}

----------------------------------------

TITLE: Installing Material UI dependencies for Next.js
DESCRIPTION: Commands for installing necessary dependencies to use Material UI with Next.js App Router.

LANGUAGE: bash
CODE:
npm install @mui/material-nextjs @emotion/cache

LANGUAGE: bash
CODE:
pnpm add @mui/material-nextjs @emotion/cache

LANGUAGE: bash
CODE:
yarn add @mui/material-nextjs @emotion/cache

----------------------------------------

TITLE: Styling MUI Base Switch Component with Emotion
DESCRIPTION: This snippet demonstrates how to style a MUI Base Switch component using Emotion, a CSS-in-JS library. It creates styled subcomponents for the root, thumb, input, and track parts of the Switch.

LANGUAGE: jsx
CODE:
import * as React from 'react';
import { Switch } from '@mui/base/Switch';
import { styled } from '@mui/system';

const StyledSwitch = styled(Switch)`
  font-size: 0;
  position: relative;
  display: inline-block;
  width: 32px;
  height: 20px;
  cursor: pointer;
  background: #b3c3d3;
  border-radius: 9999px;
  margin: 10px;
  transition: all 150ms;

  & .base-Switch-thumb {
    display: block;
    width: 14px;
    height: 14px;
    top: 3px;
    left: 3px;
    border-radius: 16px;
    background-color: #fff;
    position: relative;
    transition: all 200ms;
  }

  & .base-Switch-input {
    cursor: inherit;
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0;
    z-index: 1;
    margin: 0;
  }

  &:hover {
    background: #8796a5;
  }

  &.base-Switch-disabled {
    opacity: 0.4;
    cursor: not-allowed;
  }

  &.base-Switch-checked {
    background: #007fff;

    & .base-Switch-thumb {
      left: 14px;
      top: 3px;
      background-color: #fff;
    }

    &:hover {
      background: #0059b2;
    }
  }
`;

export default function StylingSlotsSingleComponent() {
  return <StyledSwitch defaultChecked />;
}

----------------------------------------

TITLE: Implementing Theme Registry for Joy UI with Next.js App Router
DESCRIPTION: Creates a custom ThemeRegistry component that combines Emotion's CacheProvider with Joy UI's CssVarsProvider for Next.js App Router integration. Handles server-side style injection using useServerInsertedHTML and implements emotion cache management.

LANGUAGE: tsx
CODE:
'use client';
import createCache from '@emotion/cache';
import { useServerInsertedHTML } from 'next/navigation';
import { CacheProvider } from '@emotion/react';
import { CssVarsProvider } from '@mui/joy/styles';
import CssBaseline from '@mui/joy/CssBaseline';
import theme from '/path/to/custom/theme'; // OPTIONAL

export default function ThemeRegistry(props) {
  const { options, children } = props;

  const [{ cache, flush }] = React.useState(() => {
    const cache = createCache(options);
    cache.compat = true;
    const prevInsert = cache.insert;
    let inserted: string[] = [];
    cache.insert = (...args) => {
      const serialized = args[1];
      if (cache.inserted[serialized.name] === undefined) {
        inserted.push(serialized.name);
      }
      return prevInsert(...args);
    };
    const flush = () => {
      const prevInserted = inserted;
      inserted = [];
      return prevInserted;
    };
    return { cache, flush };
  });

  useServerInsertedHTML(() => {
    const names = flush();
    if (names.length === 0) {
      return null;
    }
    let styles = '';
    for (const name of names) {
      styles += cache.inserted[name];
    }
    return (
      <style
        key={cache.key}
        data-emotion={`${cache.key} ${names.join(' ')}`}
        dangerouslySetInnerHTML={{
          __html: styles,
        }}
      />
    );
  });

  return (
    <CacheProvider value={cache}>
      <CssVarsProvider theme={theme}>
        <CssBaseline />
        {children}
      </CssVarsProvider>
    </CacheProvider>
  );
}

----------------------------------------

TITLE: Implementing Style Overrides in Material UI Theme
DESCRIPTION: Shows how to override default styles of Material UI components using the styleOverrides key in theme configuration. This example modifies the font size of all Button components.

LANGUAGE: javascript
CODE:
const theme = createTheme({
  components: {
    // Name of the component
    MuiButton: {
      styleOverrides: {
        // Name of the slot
        root: {
          // Some CSS
          fontSize: '1rem',
        },
      },
    },
  },
});

----------------------------------------

TITLE: Applying Different Styles per Color Scheme in Joy UI
DESCRIPTION: Demonstrates how to apply different styles for light and dark color schemes using the theme.getColorSchemeSelector utility.

LANGUAGE: javascript
CODE:
extendTheme({
  components: {
    JoyChip: {
      styleOverrides: {
        root: ({ ownerState, theme }) => ({
          boxShadow: theme.vars.shadow.sm,

          [theme.getColorSchemeSelector('dark')]: {
            boxShadow: 'none',
          },
        }),
      },
    },
  },
});

----------------------------------------

TITLE: Customizing Theme Tokens with Joy UI
DESCRIPTION: Demonstrates how to customize theme tokens using the extendTheme function to modify color schemes and font families. The customized tokens are deeply merged into the default theme and converted to CSS variables.

LANGUAGE: JavaScript
CODE:
import { CssVarsProvider, extendTheme } from '@mui/joy/styles';

const theme = extendTheme({
  colorSchemes: {
    light: {
      palette: {
        // affects all Joy components that has `color="primary"` prop.
        primary: {
          50: '#fffbeb',
          100: '#fef3c7',
          200: '#fde68a',
          // 300, 400, ..., 800,
          900: '#78350f',
        },
      },
    },
  },
  fontFamily: {
    display: 'Inter, var(--joy-fontFamily-fallback)',
    body: 'Inter, var(--joy-fontFamily-fallback)',
  },
});

function App() {
  return <CssVarsProvider theme={theme}>...</CssVarsProvider>;
}

----------------------------------------

TITLE: Creating Custom Switch Component with useSwitch Hook
DESCRIPTION: This example shows how to create a fully custom Switch component using the useSwitch hook from MUI Base. It demonstrates how to handle the component's state and accessibility props.

LANGUAGE: jsx
CODE:
import * as React from 'react';
import { useSwitch } from '@mui/base/useSwitch';
import { styled } from '@mui/system';

const BasicSwitch = styled('span')`
  font-size: 0;
  position: relative;
  display: inline-block;
  width: 32px;
  height: 20px;
  background: #B3C3D3;
  border-radius: 10px;
  margin: 10px;
  cursor: pointer;

  &.Switch-disabled {
    opacity: 0.4;
    cursor: not-allowed;
  }

  &.Switch-checked {
    background: #007FFF;
  }
`;

const Thumb = styled('span')`
  display: block;
  width: 14px;
  height: 14px;
  top: 3px;
  left: 3px;
  border-radius: 16px;
  background-color: #FFF;
  position: relative;
  transition: all 200ms ease;

  .Switch-checked & {
    left: 14px;
    top: 3px;
    background-color: #FFF;
  }
`;

export default function StylingHooks() {
  const { getInputProps, checked, disabled, focusVisible } = useSwitch();

  const stateClasses = {
    'Switch-checked': checked,
    'Switch-disabled': disabled,
    'Switch-focusVisible': focusVisible,
  };

  return (
    <BasicSwitch className={Object.entries(stateClasses)
      .filter(([, v]) => v)
      .map(([cls]) => cls)
      .join(' ')}>
      <Thumb />
      <input {...getInputProps()} aria-hidden={true} />
    </BasicSwitch>
  );
}

----------------------------------------

TITLE: Creating Custom Variants in Material UI Theme
DESCRIPTION: Demonstrates how to create and style custom variants for Material UI components. Includes examples of modifying existing variants and creating new ones with TypeScript support.

LANGUAGE: javascript
CODE:
const theme = createTheme({
  components: {
    MuiButton: {
      styleOverrides: {
        root: {
          variants: [
            {
              props: { variant: 'dashed', color: 'secondary' },
              style: {
                border: `4px dashed ${red[500]}`,
              },
            },
          ],
        },
      },
    },
  },
});

LANGUAGE: typescript
CODE:
declare module '@mui/material/Button' {
  interface ButtonPropsVariantOverrides {
    dashed: true;
  }
}

----------------------------------------

TITLE: Handling Button Clicks in React
DESCRIPTION: Demonstrates how to handle click events on a Button component using the onClick prop. The example shows an alert being triggered when the button is clicked.

LANGUAGE: jsx
CODE:
<Button
  onClick={() => {
    alert('clicked');
  }}
>
  Click me
</Button>

----------------------------------------

TITLE: Handling Button Clicks in React
DESCRIPTION: Demonstrates how to handle click events on a Button component using the onClick prop. The example shows an alert being triggered when the button is clicked.

LANGUAGE: jsx
CODE:
<Button
  onClick={() => {
    alert('clicked');
  }}
>
  Click me
</Button>

----------------------------------------

TITLE: Implementing Dark Mode in Next.js App Router with Joy UI
DESCRIPTION: This snippet demonstrates how to set up dark mode in a Next.js project using the App Router. It shows the use of InitColorSchemeScript, CssVarsProvider, and CssBaseline in the root layout file to prevent flickering and enable dark mode.

LANGUAGE: jsx
CODE:
import InitColorSchemeScript from '@mui/joy/InitColorSchemeScript';
import { CssVarsProvider } from '@mui/joy/styles';
import CssBaseline from '@mui/joy/CssBaseline';

export default function RootLayout(props) {
  return (
    <html lang="en" suppressHydrationWarning={true}>
      <body>
        <InitColorSchemeScript />
        <CssVarsProvider>
          <CssBaseline />
          {props.children}
        </CssVarsProvider>
      </body>
    </html>
  );
}

----------------------------------------

TITLE: Configuring Joy UI and Material UI Providers in React
DESCRIPTION: Sets up the necessary providers to use Joy UI and Material UI together. Uses ThemeProvider from Material UI as the outer wrapper and CssVarsProvider from Joy UI as the inner provider with proper theme separation.

LANGUAGE: javascript
CODE:
import {
  createTheme,
  ThemeProvider,
  THEME_ID as MATERIAL_THEME_ID,
} from '@mui/material/styles';
import { CssVarsProvider as JoyCssVarsProvider } from '@mui/joy/styles';
import CssBaseline from '@mui/material/CssBaseline';

const materialTheme = createTheme();

export default function App() {
  return (
    <ThemeProvider theme={{ [MATERIAL_THEME_ID]: materialTheme }}>
      <JoyCssVarsProvider>
        <CssBaseline enableColorScheme />
        ...Material UI and Joy UI components
      </JoyCssVarsProvider>
    </ThemeProvider>
  );
}

----------------------------------------

TITLE: Setting Responsive Meta Tag for Material UI
DESCRIPTION: HTML meta tag configuration required for proper mobile-first rendering and touch zooming across all devices when using Material UI components.

LANGUAGE: html
CODE:
<meta name="viewport" content="initial-scale=1, width=device-width" />

----------------------------------------

TITLE: Setting Up Dark Mode with ThemeProvider in Material UI
DESCRIPTION: Creates and applies a dark theme using Material UI's ThemeProvider and CssBaseline components. This demonstrates the basic setup for enabling dark mode application-wide.

LANGUAGE: js
CODE:
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});

export default function App() {
  return (
    <ThemeProvider theme={darkTheme}>
      <CssBaseline />
      <main>This app is using the dark mode</main>
    </ThemeProvider>
  );
}

----------------------------------------

TITLE: Customizing CSS Variable Prefix in Material UI
DESCRIPTION: Demonstrates how to change the default CSS variable prefix in Material UI using the createTheme function. It shows examples of setting a custom prefix and removing the prefix entirely.

LANGUAGE: javascript
CODE:
createTheme({ cssVariables: { cssVarPrefix: 'any' } });

// generated stylesheet:
// --any-palette-primary-main: ...;

LANGUAGE: javascript
CODE:
createTheme({ cssVariables: { cssVarPrefix: '' } });

// generated stylesheet:
// --palette-primary-main: ...;

----------------------------------------

TITLE: Creating Custom Theme Variables in Material UI
DESCRIPTION: Example of adding custom variables to Material UI theme using createTheme function. Shows how to extend the theme with custom status indicators.

LANGUAGE: jsx
CODE:
const theme = createTheme({
  status: {
    danger: orange[500],
  },
});

----------------------------------------

TITLE: Demonstrating sx Prop Usage in Material UI v5 with React
DESCRIPTION: This code snippet illustrates how to use the new sx prop in Material UI v5 for applying custom styles to a Box component. It showcases the ability to work with a superset of CSS, including responsive styles and pseudo-selectors.

LANGUAGE: tsx
CODE:
import * as React from 'react';
import Box from '@mui/material/Box';

export default function BoxSx() {
  return (
    <Box
      sx={{
        width: 300,
        height: 300,
        backgroundColor: 'primary.dark',
        '&:hover': {
          backgroundColor: 'primary.main',
          opacity: [0.9, 0.8, 0.7],
        },
      }}
    />
  );
}

----------------------------------------

TITLE: Adding Accessibility Attributes to React Modal
DESCRIPTION: Demonstrates how to add proper accessibility attributes to the Modal component, including aria-labelledby and aria-describedby for screen readers.

LANGUAGE: JSX
CODE:
<Modal aria-labelledby="modal-title" aria-describedby="modal-description">
  <h2 id="modal-title">My Title</h2>
  <p id="modal-description">My Description</p>
</Modal>

----------------------------------------

TITLE: TypeScript Theme Augmentation in Material UI
DESCRIPTION: Demonstrates how to extend Material UI theme types in TypeScript using module augmentation to add custom theme variables.

LANGUAGE: tsx
CODE:
declare module '@mui/material/styles' {
  interface Theme {
    status: {
      danger: string;
    };
  }
  interface ThemeOptions {
    status?: {
      danger?: string;
    };
  }
}

----------------------------------------

TITLE: Adding Material Icons Font via Google Web Fonts CDN
DESCRIPTION: HTML code to include the Material Icons font in a project using the Google Web Fonts CDN.

LANGUAGE: html
CODE:
<link
  rel="stylesheet"
  href="https://fonts.googleapis.com/icon?family=Material+Icons"
/>

----------------------------------------

TITLE: Cloning and Setting Up Repository for Material UI
DESCRIPTION: Commands to clone the Material UI repository, add the upstream remote, and install dependencies using pnpm.

LANGUAGE: bash
CODE:
git clone https://github.com/<your username>/material-ui.git
cd material-ui
git remote add upstream https://github.com/mui/material-ui.git
pnpm install

----------------------------------------

TITLE: Adding Button and Link Components
DESCRIPTION: Implementation of action elements including a login button and sign-up link with custom styling.

LANGUAGE: jsx
CODE:
<Button sx={{ mt: 1 /* margin top */ }}>
  Log in
</Button>
<Typography
  endDecorator={<Link href="/sign-up">Sign up</Link>}
  fontSize="sm"
  sx={{ alignSelf: 'center' }}
>
  Don't have an account?
</Typography>

----------------------------------------

TITLE: Creating a Performance-Optimized Option Component
DESCRIPTION: Example of creating a StableOption component using useOptionContextStabilizer for improved performance with many options.

LANGUAGE: tsx
CODE:
const StableOption = React.forwardRef(function StableOption<OptionValue>(
  props: OptionProps<OptionValue>,
  ref: React.ForwardedRef<Element>,
) {
  const { contextValue } = useOptionContextStabilizer(props.value);

  return (
    <ListContext.Provider value={contextValue}>
      <Option {...props} ref={ref} />
    </ListContext.Provider>
  );
});

----------------------------------------

TITLE: Creating Styled Component Slots in Material UI
DESCRIPTION: Demonstrates how to create styled component slots using the styled API with name and slot parameters. This allows for customization of individual elements through the theme.

LANGUAGE: javascript
CODE:
import * as React from 'react';
import { styled } from '@mui/material/styles';

const StatRoot = styled('div', {
  name: 'MuiStat', // The component name
  slot: 'root', // The slot name
})(({ theme }) => ({
  display: 'flex',
  flexDirection: 'column',
  gap: theme.spacing(0.5),
  padding: theme.spacing(3, 4),
  backgroundColor: theme.palette.background.paper,
  borderRadius: theme.shape.borderRadius,
  boxShadow: theme.shadows[2],
  letterSpacing: '-0.025em',
  fontWeight: 600,
}));

const StatValue = styled('div', {
  name: 'MuiStat',
  slot: 'value',
})(({ theme }) => ({
  ...theme.typography.h3,
}));

const StatUnit = styled('div', {
  name: 'MuiStat',
  slot: 'unit',
})(({ theme }) => ({
  ...theme.typography.body2,
  color: theme.palette.text.secondary,
}));

----------------------------------------

TITLE: Basic ButtonGroup Implementation in React
DESCRIPTION: Demonstrates how to group related buttons using the ButtonGroup component. Buttons must be immediate children of ButtonGroup.

LANGUAGE: jsx
CODE:
<ButtonGroup>\n  <Button>One</Button>\n  <Button>Two</Button>\n  <Button>Three</Button>\n</ButtonGroup>

----------------------------------------

TITLE: Disabling Transitions on Color Scheme Change in Material UI
DESCRIPTION: Shows how to disable CSS transitions when switching between color schemes in Material UI by applying the disableTransitionOnChange prop to the ThemeProvider component.

LANGUAGE: javascript
CODE:
<ThemeProvider disableTransitionOnChange />

----------------------------------------

TITLE: Customizing Switch Component with CSS Modules in TypeScript
DESCRIPTION: This snippet demonstrates how to customize a Switch component using CSS Modules in TypeScript. It uses the clsx utility to conditionally apply class names based on the component's state.

LANGUAGE: tsx
CODE:
import clsx from 'clsx';
import { Switch as BaseSwitch, SwitchOwnerState } from '@mui/base/Switch';
import classes from './styles.module.css';

export default function Switch(props) {
  const slotProps = {
    root: (ownerState: SwitchOwnerState) => ({
      className: clsx(classes.root, {
        [classes.checked]: ownerState.checked,
        [classes.disabled]: ownerState.disabled,
      }),
    }),
    thumb: { className: classes.thumb },
    track: { className: classes.track },
    input: { className: classes.input },
  };

  return <BaseSwitch {...props} slotProps={slotProps} />;
}

----------------------------------------

TITLE: Styling Material UI Component with ownerState
DESCRIPTION: Demonstrates how to use ownerState to style a component based on props or internal state. This example adds a variant prop to the Stat component.

LANGUAGE: javascript
CODE:
const Stat = React.forwardRef(function Stat(props, ref) {
  const { value, unit, variant, ...other } = props;

  const ownerState = { ...props, variant };

  return (
    <StatRoot ref={ref} ownerState={ownerState} {...other}>
      <StatValue ownerState={ownerState}>{value}</StatValue>
      <StatUnit ownerState={ownerState}>{unit}</StatUnit>
    </StatRoot>
  );
});

----------------------------------------

TITLE: Implementing Server-Side Rendering with Joy UI Dark Mode
DESCRIPTION: This snippet demonstrates how to implement server-side rendering with Joy UI's dark mode, avoiding hydration mismatches. It uses a useEffect hook to render the UI only after the component has mounted on the client side.

LANGUAGE: javascript
CODE:
function ModeToggle() {
  const { mode, setMode } = useColorScheme();
  const [mounted, setMounted] = React.useState(false);

  React.useEffect(() => {
    setMounted(true);
  }, []);

  if (!mounted) {
    // to avoid layout shift, render a placeholder button
    return <Button variant="outlined" color="neutral" sx={{ width: 120 }} />;
  }

  return (
    <Button
      variant="outlined"
      color="neutral"
      onClick={() => setMode(mode === 'dark' ? 'light' : 'dark')}
    >
      {mode === 'dark' ? 'Turn light' : 'Turn dark'}
    </Button>
  );
};

----------------------------------------

TITLE: Defining Primary Color Tokens in JavaScript
DESCRIPTION: This snippet demonstrates how to define the primary color tokens (main, light, dark, and contrastText) in the default Material UI theme.

LANGUAGE: javascript
CODE:
const primary = {
  main: '#1976d2',
  light: '#42a5f5',
  dark: '#1565c0',
  contrastText: '#fff',
};

----------------------------------------

TITLE: Basic Menu Implementation in React
DESCRIPTION: Demonstrates a basic menu that opens over an anchor element. The menu automatically realigns when near screen edges and closes upon option selection.

LANGUAGE: jsx
CODE:
{"demo": "BasicMenu.js"}

----------------------------------------

TITLE: Customizing Palette Colors Using Color Objects in JavaScript
DESCRIPTION: This example shows how to customize palette colors by importing and applying color objects from Material UI.

LANGUAGE: javascript
CODE:
import { createTheme } from '@mui/material/styles';
import { purple } from '@mui/material/colors';

const theme = createTheme({
  palette: {
    primary: purple,
  },
});

----------------------------------------

TITLE: Creating Custom Named Breakpoints in Material UI
DESCRIPTION: This snippet demonstrates how to create custom named breakpoints in the Material UI theme. It defines breakpoints for mobile, tablet, laptop, and desktop screens.

LANGUAGE: js
CODE:
const theme = createTheme({
  breakpoints: {
    values: {
      mobile: 0,
      tablet: 640,
      laptop: 1024,
      desktop: 1200,
    },
  },
});

----------------------------------------

TITLE: Installing MUI Base Package
DESCRIPTION: Commands to install @mui/base package using different package managers

LANGUAGE: bash
CODE:
npm install @mui/base

LANGUAGE: bash
CODE:
pnpm add @mui/base

LANGUAGE: bash
CODE:
yarn add @mui/base

----------------------------------------

TITLE: Creating Container Queries with Material UI Theme
DESCRIPTION: Demonstrates how to use theme.containerQueries to create CSS container queries based on theme breakpoints. The example shows how to use the 'up' method with a breakpoint key.

LANGUAGE: javascript
CODE:
theme.containerQueries.up('sm'); // => '@container (min-width: 600px)'