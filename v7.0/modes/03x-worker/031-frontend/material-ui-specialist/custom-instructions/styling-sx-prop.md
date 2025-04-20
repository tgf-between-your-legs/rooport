# MUI Styling: The `sx` Prop

Guide to using the `sx` prop for applying custom styles and overrides to MUI components (Core, Joy, Base).

## Core Concept

The `sx` prop provides a convenient and powerful way to add **one-off** or **responsive** styles directly to an MUI component instance. It acts as a superset of CSS, allowing access to theme values and providing shorthand properties. It's processed by the `@mui/system` package.

## Basic Usage

Pass an object to the `sx` prop where keys are CSS properties (camelCase or kebab-case) and values are valid CSS values.

```jsx
import Box from '@mui/material/Box'; // Or '@mui/joy/Box'

<Box
  sx={{
    // Standard CSS properties
    color: 'darkgreen',
    backgroundColor: 'lightyellow',
    padding: '16px', // Can use strings
    fontSize: 14, // Or numbers (often treated as px)
    border: '1px solid black',
    // CamelCase or kebab-case
    marginTop: '8px',
    'margin-bottom': '8px', // Kebab-case needs quotes
  }}
>
  Styled Box
</Box>
```

## Accessing Theme Values

You can directly access values defined in your MUI theme (palette, spacing, typography, breakpoints, etc.) within the `sx` prop object.

```jsx
import Box from '@mui/material/Box';
import Button from '@mui/joy/Button'; // Works with Joy UI too

<Box
  sx={{
    // Palette colors
    color: 'primary.main', // Access theme.palette.primary.main
    bgcolor: 'secondary.light', // Access theme.palette.secondary.light
    border: '1px solid',
    borderColor: 'divider', // Access theme.palette.divider

    // Spacing (multiplies theme.spacing value, default 8px)
    p: 2, // padding: theme.spacing(2) => 16px
    m: 1, // margin: theme.spacing(1) => 8px
    mt: 3, // margin-top: theme.spacing(3) => 24px
    px: 4, // padding-left & padding-right: theme.spacing(4) => 32px

    // Typography
    typography: 'body1', // Apply theme.typography.body1 styles
    fontSize: 'h6.fontSize', // Access theme.typography.h6.fontSize

    // Breakpoints (used in responsive styles, see below)

    // Z-Index
    zIndex: 'modal', // Access theme.zIndex.modal

    // Border Radius
    borderRadius: 1, // Access theme.shape.borderRadius * 1 (if theme.shape.borderRadius is number)
    // Or use theme tokens directly if available (Joy UI)
    // borderRadius: 'md', // Access theme.radius.md in Joy UI
  }}
>
  Theme-aware Box
</Box>

<Button
  variant="solid" // Joy UI example
  sx={{
    bgcolor: 'primary.400', // Access specific shade from Joy UI palette
    '&:hover': { // Pseudo-selector
      bgcolor: 'primary.500',
    }
  }}
>
  Joy Button
</Button>
```

## Responsive Styles

Use breakpoint keys (`xs`, `sm`, `md`, `lg`, `xl`) within the style value, either as an object or an array. Styles apply from the specified breakpoint *upwards* (mobile-first).

```jsx
import Box from '@mui/material/Box';

<Box
  sx={{
    width: {
      xs: 100, // width: 100px on xs screens and up
      sm: 200, // width: 200px on sm screens and up
      md: 300, // width: 300px on md screens and up
    },
    p: [1, 2, 3], // Array syntax: p: 8px (xs), 16px (sm), 24px (md and up)
    display: 'flex',
    flexDirection: ['column', 'row'], // column (xs), row (sm and up)
    bgcolor: { xs: 'red', sm: 'blue', md: 'green' },
  }}
>
  Responsive Box
</Box>
```

## Pseudo-Selectors & Nested Selectors

Target pseudo-classes (`:hover`, `:focus`, etc.) and child elements using the `&` symbol (similar to Sass/Less).

```jsx
<Box
  sx={{
    color: 'primary.main',
    '&:hover': { // Target hover state of the Box itself
      color: 'secondary.main',
      cursor: 'pointer',
    },
    '& .child-element': { // Target descendant elements
      fontWeight: 'bold',
    },
    '> p': { // Target direct child paragraphs
      margin: 0,
    }
  }}
>
  <p>Some text</p>
  <span className="child-element">Child</span>
</Box>
```

## When to Use `sx`

*   **One-off Styles:** Applying unique styles to a single component instance.
*   **Responsive Overrides:** Quickly applying responsive variations to a component.
*   **Accessing Theme:** Convenient way to use theme tokens (spacing, palette, etc.) directly.

**Avoid `sx` for:**

*   **Highly Reusable Styles:** If the same set of styles needs to be applied to multiple components, prefer creating a reusable styled component using the `styled` API or defining a custom theme variant.
*   **Very Complex Styles:** For extremely complex CSS, a dedicated CSS file or CSS Modules might be more manageable.

*(Refer to the official MUI System `sx` prop documentation: https://mui.com/system/getting-started/the-sx-prop/)*