# Bootstrap: Grid System (v4 & v5)

Understanding and using Bootstrap's powerful mobile-first flexbox grid system.

## Core Concept

Bootstrap's grid system uses a series of containers, rows, and columns to lay out and align content. It's built with flexbox and is fully responsive.

**Key Components:**

1.  **Containers (`.container`, `.container-fluid`, `.container-{breakpoint}`):**
    *   Wrap site contents.
    *   `.container`: Provides a responsive fixed width at each breakpoint.
    *   `.container-fluid`: Provides `width: 100%` at all breakpoints.
    *   `.container-{sm|md|lg|xl|xxl}` (v5): `width: 100%` until the specified breakpoint.
2.  **Rows (`.row`):**
    *   Wrappers for columns. Use flexbox (`display: flex`, `flex-wrap: wrap`).
    *   Apply negative margins to counteract the default padding on columns. **Must be placed within a `.container` (or similar) for proper alignment and padding.**
    *   Use **gutter classes** (`.g-*`, `.gx-*`, `.gy-*` in v5; `.no-gutters` or Sass variables in v4) on the `.row` to control spacing between columns.
3.  **Columns (`.col`, `.col-*`, `.col-{breakpoint}-*`):**
    *   The immediate children of `.row`. Content should be placed within columns.
    *   Specify the number of columns (out of 12) an element should span.
    *   Use breakpoint infixes (`sm`, `md`, `lg`, `xl`, `xxl`) for responsive adjustments.

## Basic Grid Structure

```html
<div class="container"> <!-- Or container-fluid -->
  <div class="row"> <!-- Gutter classes can be added here, e.g., g-3 -->
    <div class="col"> <!-- Auto-width column -->
      Column 1
    </div>
    <div class="col"> <!-- Auto-width column -->
      Column 2
    </div>
    <div class="col"> <!-- Auto-width column -->
      Column 3
    </div>
  </div>
  <div class="row">
    <div class="col-md-8"> <!-- Spans 8/12 on medium screens and up -->
      Column A (8)
    </div>
    <div class="col-md-4"> <!-- Spans 4/12 on medium screens and up -->
      Column B (4)
    </div>
  </div>
</div>
```

## Column Sizing

*   **Auto-layout (`.col`):** Columns automatically size equally within a row.
*   **Specific Width (`.col-*`):** Set a specific width (1-12). `.col-6` spans half the row width.
*   **Responsive Width (`.col-{breakpoint}-*`):** Define column width for specific breakpoints and larger.
    *   `.col-12 .col-md-6 .col-lg-4`: Full width on extra-small, half width on medium and up, third width on large and up.
*   **Variable Width Content (`.col-{breakpoint}-auto`):** Column sizes itself based on the natural width of its content.

```html
<div class="container">
  <div class="row">
    <div class="col">1 of 3</div>
    <div class="col-6">2 of 3 (Wider - col-6)</div>
    <div class="col">3 of 3</div>
  </div>
  <div class="row">
    <div class="col-12 col-md-4">.col-12 .col-md-4</div>
    <div class="col-6 col-md-4">.col-6 .col-md-4</div>
    <div class="col-6 col-md-4">.col-6 .col-md-4</div>
  </div>
</div>
```

## Gutters (Spacing Between Columns)

*   **Bootstrap 5 (`g-*`, `gx-*`, `gy-*`):** Apply gutter classes directly to the `.row`.
    *   `g-*`: Sets horizontal and vertical gutters (e.g., `.g-3` uses `$spacer * 0.5`). Values 0-5.
    *   `gx-*`: Sets horizontal gutters only.
    *   `gy-*`: Sets vertical gutters only.
    *   Responsive gutters: `.g-md-4`, `.gx-lg-5`.
*   **Bootstrap 4:**
    *   Use `.no-gutters` on the `.row` to remove default gutters.
    *   Customize gutters via Sass variables (`$grid-gutter-width`).
    *   Spacing utilities (`p-*`, `m-*`) can be used on columns, but gutters are generally preferred for column spacing.

```html
<!-- Bootstrap 5 Gutters -->
<div class="container">
  <div class="row g-3"> {/* Horizontal & Vertical Gutters */}
    <div class="col-6"><div class="p-3 border bg-light">Col 1</div></div>
    <div class="col-6"><div class="p-3 border bg-light">Col 2</div></div>
    <div class="col-6"><div class="p-3 border bg-light">Col 3</div></div>
    <div class="col-6"><div class="p-3 border bg-light">Col 4</div></div>
  </div>
</div>

<!-- Bootstrap 4 No Gutters -->
<!-- <div class="container">
  <div class="row no-gutters">
    <div class="col-6"><div class="p-3 border bg-light">Col 1</div></div>
    <div class="col-6"><div class="p-3 border bg-light">Col 2</div></div>
  </div>
</div> -->
```

## Alignment & Ordering

*   **Vertical Alignment (on `.row`):** Use flexbox alignment classes.
    *   `align-items-start`, `align-items-center`, `align-items-end`.
*   **Horizontal Alignment (on `.row`):** Use flexbox justification classes.
    *   `justify-content-start`, `justify-content-center`, `justify-content-end`, `justify-content-around`, `justify-content-between`, `justify-content-evenly` (v5).
*   **Column Ordering:** Change the visual order of columns.
    *   `.order-*` classes (e.g., `.order-2`, `.order-md-1`). Values 0-5 (v5) or 1-12 (v4).
    *   `.order-first`, `.order-last`.
*   **Column Offsetting:** Move columns to the right.
    *   `.offset-*` classes (e.g., `.offset-2`, `.offset-md-1`).

```html
<div class="container">
  <div class="row align-items-center" style="min-height: 100px; background-color: rgba(0,0,0,.1);">
    <div class="col">Vertically Centered</div>
    <div class="col">Vertically Centered</div>
    <div class="col">Vertically Centered</div>
  </div>
  <div class="row justify-content-center">
    <div class="col-4">Horizontally Centered</div>
    <div class="col-4">Horizontally Centered</div>
  </div>
   <div class="row">
    <div class="col order-md-2">First in DOM, second visually on MD+</div>
    <div class="col order-md-1">Second in DOM, first visually on MD+</div>
  </div>
  <div class="row">
    <div class="col-md-4 offset-md-4">.col-md-4 .offset-md-4</div>
  </div>
</div>
```

Mastering the grid system is fundamental to building effective and responsive layouts with Bootstrap. Remember to always place `.row`s inside `.container`s and content inside `.col`s.

*(Refer to the official Bootstrap Grid documentation for your target version.)*