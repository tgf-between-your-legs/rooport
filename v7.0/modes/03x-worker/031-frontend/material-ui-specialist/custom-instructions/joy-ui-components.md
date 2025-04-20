# Joy UI Components Quick Reference

Examples and key concepts for common Joy UI components. Joy UI is a separate design system from Material Design, focusing on customization and developer experience.

## Core Concepts

*   **Design System:** Joy UI has its own distinct aesthetic, separate from Material Design.
*   **CSS Variables:** Theming is primarily done using CSS variables, enabled via `<CssVarsProvider>`.
*   **`extendTheme`:** Use this function to customize the default Joy UI theme.
*   **`sx` Prop:** Widely used for component customization and responsive styles, similar to MUI Core.
*   **Components:** Offers a range of components, sometimes with slightly different names or props compared to MUI Core.

## Setup (`<CssVarsProvider>`)

Wrap your application (or relevant part) with `CssVarsProvider` and optionally provide a custom theme.

```jsx
import * as React from 'react';
import { CssVarsProvider, extendTheme } from '@mui/joy/styles';
import Button from '@mui/joy/Button';
// Import other Joy UI components

// Optional: Customize the theme
const theme = extendTheme({
  colorSchemes: {
    light: {
      palette: {
        primary: {
          solidBg: '#0b6bcb', // Example primary color
          // ... other primary shades
        },
      },
    },
    dark: {
       palette: {
        primary: {
          solidBg: '#65b3f0',
          // ... other primary shades
        },
      },
    },
  },
  fontFamily: {
    body: 'system-ui, sans-serif',
  },
  // ... other theme customizations
});

function App() {
  return (
    <CssVarsProvider theme={theme} defaultMode="system"> {/* Or "light", "dark" */}
      {/* Your application using Joy UI components */}
      <Button>Hello Joy UI</Button>
    </CssVarsProvider>
  );
}
```

## Common Components (Examples)

*   **Button:**
    ```jsx
    import Button from '@mui/joy/Button';
    <Button variant="solid" color="primary" size="lg">Solid Button</Button>
    <Button variant="outlined" color="neutral">Outlined</Button>
    <Button variant="soft" loading>Loading</Button>
    <Button startDecorator={<SomeIcon />}>With Icon</Button>
    ```
*   **Input:**
    ```jsx
    import Input from '@mui/joy/Input';
    import FormControl from '@mui/joy/FormControl';
    import FormLabel from '@mui/joy/FormLabel';
    import FormHelperText from '@mui/joy/FormHelperText';

    <FormControl error={/* condition */}>
      <FormLabel>Email</FormLabel>
      <Input type="email" placeholder="Enter email" required />
      <FormHelperText>This is required.</FormHelperText>
    </FormControl>
    ```
*   **Card:**
    ```jsx
    import Card from '@mui/joy/Card';
    import CardContent from '@mui/joy/CardContent';
    import CardOverflow from '@mui/joy/CardOverflow'; // For images/media
    import Typography from '@mui/joy/Typography';
    import AspectRatio from '@mui/joy/AspectRatio'; // For images

    <Card variant="outlined" sx={{ width: 320 }}>
      <CardOverflow>
        <AspectRatio ratio="2">
          <img src="..." alt="" />
        </AspectRatio>
      </CardOverflow>
      <CardContent>
        <Typography level="title-lg">Card Title</Typography>
        <Typography level="body-sm">Card description goes here.</Typography>
      </CardContent>
    </Card>
    ```
*   **Layout (`Box`, `Stack`, `Grid`):** Similar concepts to MUI Core, but import from `@mui/joy`.
    ```jsx
    import Box from '@mui/joy/Box';
    import Stack from '@mui/joy/Stack';
    import Grid from '@mui/joy/Grid'; // Note: Joy UI Grid might be less feature-rich than Core's

    <Stack direction="row" spacing={2}>
      <Button>One</Button>
      <Button>Two</Button>
    </Stack>
    ```
*   **Typography:** Uses `level` prop instead of `variant`.
    ```jsx
    import Typography from '@mui/joy/Typography';
    <Typography level="h1">Heading 1</Typography>
    <Typography level="body-md">Body text</Typography>
    ```
*   **Other Components:** `Sheet` (general purpose container), `Select`, `Checkbox`, `Radio`, `Switch`, `Textarea`, `Modal`, `Drawer`, `Menu`, `List`, `Table`, etc.

## Styling with `sx` Prop

Works similarly to MUI Core, allowing direct access to theme tokens and responsive styles.

```jsx
<Box
  sx={{
    p: 2, // theme.spacing(2)
    bgcolor: 'background.surface', // theme.palette.background.surface
    borderRadius: 'sm', // theme.radius.sm
    boxShadow: 'md', // theme.shadow.md
    mt: { xs: 1, md: 2 }, // Responsive margin-top
    '&:hover': { // Pseudo-selector
      bgcolor: 'primary.softHoverBg',
    }
  }}
>
  Styled Box
</Box>
```

*(Refer to the official Joy UI documentation for the full component list, APIs, and theming details: https://mui.com/joy-ui/getting-started/)*