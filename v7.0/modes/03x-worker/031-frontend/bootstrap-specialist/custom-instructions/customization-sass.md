# Customizing Bootstrap with Sass

Guide to overriding Bootstrap's default styles using Sass variables and custom builds. Requires a Sass build process (e.g., using Dart Sass, Node Sass via Webpack/Vite plugin).

## Core Concept

Bootstrap is built with Sass, and its default styles are defined using Sass variables. By overriding these variables *before* importing Bootstrap's main Sass file, you can customize the framework globally.

## Setup

1.  **Install Bootstrap Source:** Ensure you have Bootstrap's source Sass files installed (`npm install bootstrap`).
2.  **Install Sass Compiler:** Install a Sass compiler (`npm install -D sass`).
3.  **Create Custom Sass File:** Create a main Sass file (e.g., `src/styles/main.scss`).
4.  **Configure Build Process:** Set up your build tool (Webpack, Vite, Parcel, etc.) to compile your `main.scss` file into CSS.

## Overriding Variables

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
    $enable-gradients: true; // Example: Enable gradients globally

    // Example: Modify theme colors map
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
    // OR import only needed parts:
    // @import "~bootstrap/scss/root";
    // @import "~bootstrap/scss/reboot";
    // @import "~bootstrap/scss/type";
    // ... import other required parts ...
    // @import "~bootstrap/scss/grid";
    // @import "~bootstrap/scss/buttons";
    // ... etc ...
    // @import "~bootstrap/scss/utilities/api"; // Important for utility API
    ```
4.  **(Optional) Add Custom Styles:** Add your own project-specific Sass/CSS rules after importing Bootstrap.

## Example `main.scss`

```scss
// 1. Import functions (optional)
@import "~bootstrap/scss/functions";

// 2. Your variable overrides
$primary: purple;
$font-family-sans-serif: "Verdana", sans-serif;
$border-radius: 0;

// 3. Import Bootstrap (all or parts)
@import "~bootstrap/scss/bootstrap";

// 4. Your custom styles
body {
  background-color: #eee;
}
.my-custom-component {
  border: 1px solid $primary;
}
```

## Custom Builds (Importing Parts)

Instead of importing the entire `bootstrap.scss`, you can import only the parts you need to potentially reduce final CSS size. You *must* include `functions`, `variables`, `mixins`, `root`, `reboot`, and `utilities/api` at a minimum for most functionality.

```scss
// Import functions first
@import "~bootstrap/scss/functions";

// Your variable overrides here
$primary: #007bff;

// Import required Bootstrap parts
@import "~bootstrap/scss/variables";
@import "~bootstrap/scss/mixins";
@import "~bootstrap/scss/root";
@import "~bootstrap/scss/reboot";
@import "~bootstrap/scss/type";
// @import "~bootstrap/scss/images";
@import "~bootstrap/scss/containers";
@import "~bootstrap/scss/grid";
// @import "~bootstrap/scss/tables";
@import "~bootstrap/scss/forms";
@import "~bootstrap/scss/buttons";
// ... import other needed components ...
@import "~bootstrap/scss/nav";
@import "~bootstrap/scss/navbar";
// ... etc ...

// Import utilities LAST
@import "~bootstrap/scss/utilities";
@import "~bootstrap/scss/utilities/api"; // Crucial for responsive utilities
```

*(Refer to the official Bootstrap Theming and Customize > Sass documentation for details: https://getbootstrap.com/docs/5.3/customize/sass/)*