# CSS: Common Patterns & Best Practices

Fundamental CSS concepts for styling web pages.

## Core Concepts

*   **Selectors:** Target HTML elements to apply styles.
    *   **Type:** `p`, `h1`, `div` (Selects all elements of that type)
    *   **Class:** `.my-class` (Selects elements with `class="my-class"`) - **Preferred method for styling.**
    *   **ID:** `#my-id` (Selects the single element with `id="my-id"`) - Use sparingly, mainly for JS hooks or page fragments. High specificity.
    *   **Attribute:** `[type="text"]`, `[data-status="active"]`
    *   **Pseudo-classes:** `:hover`, `:focus`, `:nth-child(n)`, `:first-child`, `:last-child`, `:not(...)`
    *   **Pseudo-elements:** `::before`, `::after`, `::first-letter`, `::placeholder`
    *   **Combinators:**
        *   Descendant: `article p` (Selects `p` inside `article`)
        *   Child: `ul > li` (Selects `li` directly inside `ul`)
        *   Adjacent Sibling: `h2 + p` (Selects `p` immediately following `h2`)
        *   General Sibling: `h2 ~ p` (Selects any `p` following `h2` at the same level)
*   **Specificity:** Determines which CSS rule applies if multiple rules target the same element. Generally: ID > Class/Attribute/Pseudo-class > Type/Pseudo-element. Inline styles (`style="..."`) have the highest specificity. Avoid overly specific selectors (e.g., `#main-nav ul li a.active`) as they are hard to override. Prefer class-based selectors.
*   **Cascade:** Styles "cascade" down from parent elements and from earlier rules to later rules in the stylesheet. Specificity and `!important` (use sparingly!) override the cascade.
*   **Box Model:** Every HTML element is treated as a rectangular box.
    *   **Content:** The text, image, etc.
    *   **Padding:** Space between content and border.
    *   **Border:** Line around the padding.
    *   **Margin:** Space outside the border, separating the element from others.
    *   **`box-sizing: border-box;` (Recommended):** Makes `width` and `height` properties include padding and border, simplifying layout calculations. Often set globally:
        ```css
        *, *::before, *::after {
          box-sizing: border-box;
        }
        ```
*   **Units:**
    *   **Absolute:** `px` (pixels), `pt` (points), `cm`, `in`, etc. `px` is common for fixed sizes like borders.
    *   **Relative:**
        *   `%`: Relative to the parent element's size.
        *   `em`: Relative to the element's own font size (or parent's font size if used for `font-size`).
        *   `rem`: Relative to the **root** element's (`html`) font size. **Often preferred for scalable layouts and typography.**
        *   `vw`, `vh`: Relative to the viewport's width and height.
        *   `vmin`, `vmax`: Relative to the smaller or larger viewport dimension.

## Common Layout Techniques

*   **Normal Flow:** Default layout (block elements stack vertically, inline elements flow horizontally).
*   **`display` Property:**
    *   `block`: Takes full width, starts on new line (`div`, `p`, `h1`).
    *   `inline`: Flows with text, width/height determined by content (`span`, `a`, `strong`). Cannot set vertical margin/padding effectively.
    *   `inline-block`: Flows like inline, but allows setting width, height, vertical margin/padding.
    *   `none`: Hides the element and removes it from layout.
    *   `flex`: Enables Flexbox layout for child elements.
    *   `grid`: Enables Grid layout for child elements.
*   **Flexbox (`display: flex`):** One-dimensional layout system (row or column).
    *   **Container Properties:** `flex-direction`, `justify-content`, `align-items`, `flex-wrap`, `gap`.
    *   **Item Properties:** `flex-grow`, `flex-shrink`, `flex-basis`, `order`, `align-self`.
    *   Excellent for component layout, navigation bars, aligning items.
    ```css
    .flex-container {
      display: flex;
      justify-content: space-between; /* Space items horizontally */
      align-items: center; /* Center items vertically */
      gap: 1rem; /* Space between items */
    }
    ```
*   **Grid (`display: grid`):** Two-dimensional layout system (rows and columns).
    *   **Container Properties:** `grid-template-columns`, `grid-template-rows`, `grid-template-areas`, `gap`, `justify-items`, `align-items`.
    *   **Item Properties:** `grid-column-start`/`end`, `grid-row-start`/`end`, `grid-area`, `justify-self`, `align-self`.
    *   Powerful for overall page layouts and complex grids.
    ```css
    .grid-container {
      display: grid;
      grid-template-columns: 1fr 2fr; /* Two columns, second twice as wide */
      gap: 1rem;
    }
    ```
*   **Positioning:**
    *   `static` (default): Normal flow.
    *   `relative`: Normal flow, but `top`/`right`/`bottom`/`left` offset relative to its normal position. Creates stacking context.
    *   `absolute`: Removed from normal flow. Positioned relative to the nearest *positioned* ancestor (non-`static`). Uses `top`/`right`/`bottom`/`left`.
    *   `fixed`: Removed from normal flow. Positioned relative to the *viewport*. Stays in place during scroll.
    *   `sticky`: Mix of relative and fixed. Scrolls with flow until it hits a specified offset relative to the viewport, then sticks. Requires `top`, `bottom`, etc.

## Responsiveness (`@media` Queries)

Apply different styles based on screen size, device capabilities, etc.

```css
/* Default styles (mobile-first) */
.container {
  width: 95%;
  margin: 0 auto;
}

.sidebar {
  display: none; /* Hidden on small screens */
}

/* Medium screens and up */
@media (min-width: 768px) {
  .container {
    max-width: 720px;
  }
  .sidebar {
    display: block; /* Show sidebar */
    width: 200px;
    float: left; /* Example layout change */
  }
  .main-content {
    margin-left: 210px; /* Adjust main content */
  }
}

/* Large screens and up */
@media (min-width: 992px) {
  .container {
    max-width: 960px;
  }
}
```
*   **Mobile-First:** Design styles for small screens first, then use `min-width` media queries to add/override styles for larger screens. Generally recommended.
*   **Breakpoints:** Choose sensible breakpoints based on common device sizes or where your layout naturally breaks.

## Best Practices

*   **Use Classes:** Prefer styling via classes over IDs or type selectors for better reusability and lower specificity.
*   **Keep Specificity Low:** Avoid deeply nested selectors or overuse of IDs.
*   **DRY (Don't Repeat Yourself):** Group common styles, use variables (CSS Custom Properties or Sass/Less variables).
*   **Organization:** Structure your CSS logically (e.g., by component, layout section). Consider methodologies like BEM (Block, Element, Modifier) for naming conventions.
*   **Comments:** Explain complex selectors or non-obvious styles.
*   **Use `rem` for Scalability:** Use `rem` units for `font-size`, `padding`, `margin` where scalability with root font size is desired.
*   **Use `box-sizing: border-box;`**.

Mastering these fundamentals is key to writing effective, maintainable, and responsive CSS.