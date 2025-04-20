# Custom Instructions for 🎨 Material UI Specialist Mode

This directory contains specific instructions and guidelines for the `material-ui-specialist` mode, covering the MUI ecosystem (Core, Joy, Base).

## Instruction Files

1.  **`01-core-workflow.md`**: Core concepts of MUI Core (v5+), installation, basic usage, general operational principles, and standard workflow.
2.  **`02-setup-theming.md`**: How to set up and customize themes for both MUI Core (`createTheme`, `ThemeProvider`) and Joy UI (`extendTheme`, `CssVarsProvider`). Covers palette, typography, spacing, components overrides, etc.
3.  **`03-styling-sx-styled.md`**: Details on applying custom styles using the `sx` prop (for one-off styles, theme access, responsiveness) and the `styled()` API (for reusable styled components). Compares the two approaches.
4.  **`04-core-layout.md`**: Guide to using MUI Core layout components: `Box`, `Container`, `Grid`, and `Stack` for structuring pages and components.
5.  **`05-core-inputs.md`**: Covers common MUI Core input and control components: `Button`, `TextField`, `Checkbox`, `Radio`, `Switch`, `Select`, `Slider`, `Autocomplete`.
6.  **`06-core-navigation.md`**: Details on MUI Core navigation components: `AppBar`, `Toolbar`, `Drawer`, `Menu`, `Tabs`, `Breadcrumbs`, `Link`, `BottomNavigation`.
7.  **`07-core-data-display.md`**: Guide to MUI Core components for displaying data: `Typography`, `List`, `Table`, `Card`, `Avatar`, `Badge`, `Chip`, `Tooltip`, `Divider`.
8.  **`08-core-feedback.md`**: Covers MUI Core feedback components: `Alert`, `Dialog`, `Snackbar`, `LinearProgress`, `CircularProgress`, `Skeleton`.
9.  **`09-joy-ui-intro.md`**: Introduction to Joy UI, its design system differences, CSS variable theming (`CssVarsProvider`, `extendTheme`), setup, and common component examples (`Button`, `Input`, `Card`, `Typography`, etc.).
10. **`10-base-ui-intro.md`**: Introduction to MUI Base, focusing on its unstyled components and hooks (`useSwitch`, `useButton`, etc.) for building custom design systems. Covers installation and usage patterns.
11. **`11-accessibility.md`**: Accessibility (a11y) principles and best practices when using MUI components, including keyboard navigation, focus management, labels, contrast, and ARIA attributes. Includes testing tips.
12. **`12-react-nextjs-integration.md`**: Patterns for integrating MUI components with React state management (controlled components, open/close state) and specific setup instructions for Next.js (App Router and Pages Router) to handle SSR and styling correctly.