# Customizing Bootstrap 5 with CSS Variables

Guide to overriding Bootstrap's default styles using CSS Custom Properties (Variables). This method does not require a Sass build process.

## Core Concept

Bootstrap 5 exposes many of its global options and component styles as CSS variables (prefixed with `--bs-`). You can override these variables in your own CSS to customize the look and feel without recompiling Bootstrap's source.

## How to Override

1.  **Include Bootstrap CSS:** Link the standard Bootstrap CSS file (e.g., from a CDN or local `node_modules`) in your HTML.
    ```html
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    ```
2.  **Define Overrides:** In your own CSS file (linked *after* Bootstrap's CSS), redefine the `--bs-*` variables within the `:root` selector (for global changes) or specific component selectors.

## Common Global Variables (`:root`)

Find the full list in Bootstrap's `_root.scss` file or documentation.

```css
/* Your custom CSS file (e.g., styles.css) */
:root {
  /* Color Palette */
  --bs-primary: #6f42c1; /* Change primary color to purple */
  --bs-secondary: #6c757d;
  --bs-success: #198754;
  --bs-info: #0dcaf0;
  --bs-warning: #ffc107;
  --bs-danger: #dc3545;
  --bs-light: #f8f9fa;
  --bs-dark: #212529;

  /* Body */
  --bs-body-font-family: 'Georgia', serif; /* Change base font */
  --bs-body-font-size: 1.1rem;
  --bs-body-line-height: 1.6;
  --bs-body-color: #333;
  --bs-body-bg: #f0f0f0; /* Change page background */

  /* Borders */
  --bs-border-radius: 0.5rem; /* Increase default border radius */
  --bs-border-radius-sm: 0.3rem;
  --bs-border-radius-lg: 0.8rem;
  --bs-border-color: #adb5bd;

  /* Links */
  --bs-link-color-rgb: 111, 66, 193; /* Set RGB version for link utilities */
  --bs-link-hover-color-rgb: 80, 40, 150;

  /* Add other global overrides as needed */
}

/* You can also override component-specific variables */
.btn-primary {
  --bs-btn-hover-bg: #5a3d9a; /* Darker purple on hover */
  --bs-btn-active-bg: #4a327d;
}

.card {
  --bs-card-border-color: rgba(0, 0, 0, 0.2);
  --bs-card-cap-bg: rgba(0, 0, 0, 0.05);
}
```

## Component Variables

Many components also have their own specific CSS variables that can be overridden directly on the component's class or a parent selector.

*   **Example:** Changing button padding:
    ```css
    .btn {
      --bs-btn-padding-y: 0.5rem;
      --bs-btn-padding-x: 1rem;
    }
    ```
*   **Example:** Changing modal header background:
    ```css
    .modal-header {
      --bs-modal-header-bg: var(--bs-primary);
      --bs-modal-header-color: var(--bs-white);
      --bs-modal-header-border-color: var(--bs-primary);
    }
    .modal-header .btn-close {
        filter: invert(1) grayscale(100%) brightness(200%); /* Make close button white */
    }
    ```

## Benefits & Drawbacks

*   **Benefits:**
    *   No Sass build process required.
    *   Easy to apply dynamic themes (e.g., by changing variables on the `<html>` or `<body>` tag with JavaScript).
    *   Allows for more targeted overrides than global Sass variables.
*   **Drawbacks:**
    *   Overrides happen at runtime in the browser, potentially less performant than build-time Sass compilation (though usually negligible).
    *   Doesn't allow access to Sass functions or mixins for more complex customizations.
    *   Might require more CSS rules compared to changing a single Sass variable that affects multiple components.

*(Refer to the official Bootstrap 5 Customize > CSS Variables documentation for details: https://getbootstrap.com/docs/5.3/customize/css-variables/)*