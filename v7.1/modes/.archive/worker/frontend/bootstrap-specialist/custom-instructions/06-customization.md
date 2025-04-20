# Customizing Bootstrap (v4 & v5)

Guide to overriding Bootstrap's default styles using Sass variables (requires build process) or CSS variables (v5 only, no build process needed).

## Method 1: Customizing with Sass (v4 & v5)

Requires a Sass build process (e.g., using Dart Sass, Node Sass via Webpack/Vite plugin).

### Core Concept

Bootstrap is built with Sass, and its default styles are defined using Sass variables. By overriding these variables *before* importing Bootstrap's main Sass file, you can customize the framework globally.

### Setup

1.  **Install Bootstrap Source:** Ensure you have Bootstrap's source Sass files installed (`npm install bootstrap`).
2.  **Install Sass Compiler:** Install a Sass compiler (`npm install -D sass`).
3.  **Create Custom Sass File:** Create a main Sass file (e.g., `src/styles/main.scss`).
4.  **Configure Build Process:** Set up your build tool (Webpack, Vite, Parcel, etc.) to compile your `main.scss` file into CSS.

### Overriding Variables

In your `main.scss` (or a dedicated `_variables.scss` file imported by it):

1.  **(Optional but Recommended) Import Bootstrap Functions:** Import functions first if you need to use them in your variable overrides.
    ```scss
    // Optional: Import Bootstrap functions first
    @import "~bootstrap/scss/functions";
    ```
2.  **Override Variables:** Define your custom values for Bootstrap's Sass variables *before* importing the rest of Bootstrap. Find default variables in `node_modules/bootstrap/scss/_variables.scss`.
    ```scss
    // Your variable overrides
    $primary: #7952B3; // Example: Change primary color to Bootstrap purple
    $secondary: #6c757d;
    $font-family-base: 'Roboto', sans-serif; // Example: Change base font
    $border-radius: 0.25rem; // Example: Slightly rounder corners
    $enable-gradients: true; // Example: Enable gradients globally (v4/v5)

    // Example: Modify theme colors map (v5 syntax, v4 is similar)
    $theme-colors: (
      "primary": $primary,
      "secondary": $secondary,
      "success": #198754,
      "info": #0dcaf0,
      "warning": #ffc107,
      "danger": #dc3545,
      "light": #f8f9fa,
      "dark": #212529,
      "custom-color": #900 // Add a custom theme color
    );
    ```
3.  **Import Bootstrap Core:** Import the main Bootstrap Sass file *after* your variable overrides.
    ```scss
    // Import the rest of Bootstrap core styles
    @import "~bootstrap/scss/bootstrap";
    // OR import only needed parts (see Custom Builds below)
    ```
4.  **(Optional) Add Custom Styles:** Add your own project-specific Sass/CSS rules after importing Bootstrap.

### Custom Builds (Importing Parts)

Instead of importing the entire `bootstrap.scss`, you can import only the parts you need to potentially reduce final CSS size. You *must* include `functions`, `variables`, `mixins`, `root`, `reboot`, and `utilities/api` (v5) at a minimum for most functionality.

```scss
// Import functions first
@import "~bootstrap/scss/functions";

// Your variable overrides here
$primary: #007bff;

// Import required Bootstrap parts
@import "~bootstrap/scss/variables";
@import "~bootstrap/scss/mixins";
@import "~bootstrap/scss/root"; // v5
@import "~bootstrap/scss/reboot";
@import "~bootstrap/scss/type";
// ... import other required parts ...
@import "~bootstrap/scss/grid";
@import "~bootstrap/scss/buttons";
// ... etc ...

// Import utilities LAST
@import "~bootstrap/scss/utilities";
@import "~bootstrap/scss/utilities/api"; // Crucial for responsive utilities (v5)
```

---

## Method 2: Customizing with CSS Variables (v5 Only)

This method does not require a Sass build process.

### Core Concept

Bootstrap 5 exposes many of its global options and component styles as CSS variables (prefixed with `--bs-`). You can override these variables in your own CSS to customize the look and feel without recompiling Bootstrap's source.

### How to Override

1.  **Include Bootstrap CSS:** Link the standard Bootstrap CSS file (e.g., from a CDN or local `node_modules`) in your HTML.
    ```html
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    ```
2.  **Define Overrides:** In your own CSS file (linked *after* Bootstrap's CSS), redefine the `--bs-*` variables within the `:root` selector (for global changes) or specific component selectors.

### Common Global Variables (`:root`)

Find the full list in Bootstrap's `_root.scss` file or documentation.

```css
/* Your custom CSS file (e.g., styles.css) */
:root {
  /* Color Palette */
  --bs-primary: #6f42c1; /* Change primary color to purple */
  --bs-secondary: #6c757d;
  /* ... other theme colors ... */

  /* Body */
  --bs-body-font-family: 'Georgia', serif; /* Change base font */
  --bs-body-font-size: 1.1rem;
  --bs-body-bg: #f0f0f0; /* Change page background */

  /* Borders */
  --bs-border-radius: 0.5rem; /* Increase default border radius */
  --bs-border-color: #adb5bd;

  /* Links (RGB version needed for utilities) */
  --bs-link-color-rgb: 111, 66, 193;
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
}
```

### Component Variables

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
    }
    ```

### Benefits & Drawbacks (CSS Variables)

*   **Benefits:** No Sass build process required; easy dynamic theming.
*   **Drawbacks:** Runtime overrides (potentially less performant, usually negligible); no access to Sass functions/mixins; might require more CSS rules than Sass overrides.

*(Refer to the official Bootstrap Customize documentation for Sass and CSS Variables for your target version.)*