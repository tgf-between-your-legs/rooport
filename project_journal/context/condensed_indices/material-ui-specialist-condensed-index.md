## Material UI (MUI) v5+ - Condensed Context Index

### Overall Purpose

Material UI (MUI) is a comprehensive suite of React UI components. It includes:
*   **MUI Core:** Pre-built components following Material Design guidelines (`@mui/material`).
*   **Joy UI:** A distinct design system with its own components and theming (`@mui/joy`).
*   **MUI Base:** Unstyled ("headless") components and hooks for maximum customization (`@mui/base`).
Relies heavily on Emotion for styling (`@emotion/react`, `@emotion/styled`).

### Core Concepts & Capabilities

*   **Installation & Setup:** Install packages (`@mui/material`, `@mui/joy`, `@mui/base`, `@emotion/*`) via npm/pnpm/yarn. Requires specific setup for frameworks like Next.js (`@mui/material-nextjs`, `@emotion/cache`).
*   **Theming:** Highly customizable themes using `createTheme` (Material) or `extendTheme` (Joy). Define `palette` (colors, modes), `typography`, `breakpoints`, `components` (overrides/variants), custom tokens, and CSS variables (`cssVarPrefix`).
*   **Styling:** Multiple approaches:
    *   `sx` prop: Inline styles with theme access, responsive values, pseudo-selectors.
    *   `styled` API (Emotion): Create reusable styled components (CSS-in-JS).
    *   Theme `components` object: Global style overrides (`styleOverrides`) and custom `variants`.
    *   CSS Modules: Use with `clsx` for conditional classes, especially with MUI Base.
    *   `ownerState`: Access component props/state within styling functions.
*   **Component Library:** Rich set of pre-built components (e.g., `Button`, `TextField`, `Modal`, `Menu`, `Switch`, `Box`, `ButtonGroup`). MUI Base provides unstyled primitives and hooks (e.g., `useSwitch`).
*   **Dark Mode:** Supported via theme `palette.mode` (Material) or `CssVarsProvider` / `InitColorSchemeScript` (Joy UI, SSR).
*   **Responsiveness:** Built-in support via theme `breakpoints` and responsive syntax in `sx` prop. Requires `<meta name="viewport">`. Container queries via `theme.containerQueries`.
*   **Joy UI & MUI Core Integration:** Can be used together using separate theme providers (`ThemeProvider`, `JoyCssVarsProvider`).
*   **Next.js Integration:** Specific packages (`@mui/material-nextjs`) and patterns (`ThemeRegistry`, `useServerInsertedHTML`, `InitColorSchemeScript`) for App Router compatibility, SSR, and styling.
*   **Accessibility:** Components often include basic accessibility, but manual additions (e.g., `aria-*` for `Modal`) are sometimes needed.
*   **Performance:** Tree-shaking via named imports is crucial. Hooks like `useOptionContextStabilizer` exist for specific scenarios.

### Key APIs / Components / Configuration / Patterns

*   **Packages:** `@mui/material`, `@mui/joy`, `@mui/base`, `@emotion/react`, `@emotion/styled`, `@mui/material-nextjs`, `@emotion/cache`.
*   **Theme Creation:**
    *   `createTheme` (@mui/material/styles): Core function for Material UI theme definition.
    *   `extendTheme` (@mui/joy/styles): Core function for Joy UI theme definition (uses CSS variables).
*   **Theme Providers:**
    *   `ThemeProvider` (@mui/material/styles): Applies Material UI theme. Prop: `theme`, `disableTransitionOnChange`.
    *   `CssVarsProvider` (@mui/joy/styles): Applies Joy UI theme (CSS variables). Prop: `theme`.
    *   `CssBaseline` (@mui/material/CssBaseline, @mui/joy/CssBaseline): Applies baseline browser styles.
*   **Theme Structure Keys:**
    *   `palette`: Defines color schemes (e.g., `primary`, `secondary`, `mode: 'dark'`).
    *   `components`: Defines global `styleOverrides` and `variants` for components.
    *   `breakpoints`: Defines responsive breakpoints (`values: { xs, sm, md, lg, xl }`).
    *   `typography`: Defines font settings.
    *   `cssVariables`: Configuration for CSS variable generation (e.g., `cssVarPrefix`).
*   **Styling:**
    *   `sx` prop: Object for direct styling on components.
    *   `styled('element', { name, slot })`: Emotion API for creating styled components/slots.
    *   `ownerState`: Object passed to style functions containing component state/props.
*   **Core Components:** `Button`, `ButtonGroup`, `Box`, `Typography`, `TextField`, `Modal`, `Menu`, `Switch` (Material & Base versions).
*   **MUI Base Hooks:** `useSwitch`, `useOptionContextStabilizer`.
*   **Next.js:**
    *   `InitColorSchemeScript` (@mui/joy/InitColorSchemeScript): Prevents theme flicker on SSR page load.
    *   `ThemeRegistry` (Pattern): Component combining Emotion cache and theme providers for App Router.
    *   `useServerInsertedHTML` (next/navigation): Hook for SSR style injection.
*   **Accessibility:** `aria-labelledby`, `aria-describedby` attributes.
*   **Imports:** `import { Component } from '@mui/material';` (Supports tree-shaking).

### Common Patterns & Best Practices / Pitfalls

*   **Dependencies:** Emotion (`@emotion/react`, `@emotion/styled`) is fundamental for styling.
*   **Tree-shaking:** Always use named imports (`import { Button } from ...`) to minimize bundle size.
*   **Styling Choice:** Use `sx` for one-off styles, `styled` for reusable components, theme overrides for global consistency.
*   **MUI Base:** Ideal for fully custom designs; requires manual styling (Emotion, Tailwind, CSS Modules).
*   **Joy UI:** Use `CssVarsProvider` and `extendTheme`. Styles often leverage CSS variables.
*   **Next.js:** Follow specific App Router setup (`ThemeRegistry`, `InitColorSchemeScript`) carefully to avoid SSR/hydration issues.
*   **Responsiveness:** Configure `breakpoints` and use responsive syntax in `sx` or media queries in `styled`. Ensure `<meta name="viewport">` is present.
*   **Accessibility:** Add necessary `aria-*` attributes, especially for interactive components like `Modal`.

---
This index summarizes the core concepts, APIs, and patterns for Material UI (v5+), Joy UI, and MUI Base based on the provided snippets. Consult the full official documentation for exhaustive details.