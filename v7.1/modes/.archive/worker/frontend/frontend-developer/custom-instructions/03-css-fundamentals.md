# CSS: Fundamentals & Best Practices

Guidelines for writing clean, effective, maintainable, and responsive CSS.

## 1. Core Concepts

*   **Selectors:** Target HTML elements. Prefer **class selectors** (`.my-class`) for styling. Use ID selectors (`#my-id`) sparingly (JS hooks, page fragments). Avoid over-reliance on type selectors (`p`, `div`).
    *   Common types: Type, Class, ID, Attribute (`[type="text"]`), Pseudo-classes (`:hover`, `:focus`, `:nth-child()`), Pseudo-elements (`::before`, `::after`).
    *   Combinators: Descendant (`article p`), Child (`ul > li`), Adjacent Sibling (`h2 + p`), General Sibling (`h2 ~ p`).
*   **Specificity:** Determines which rule applies if multiple target the same element. Order (highest to lowest): Inline styles > IDs > Classes/Attributes/Pseudo-classes > Types/Pseudo-elements. Keep specificity low for easier overrides. Avoid complex, deeply nested selectors.
*   **Cascade:** Styles flow down from parents and earlier rules to later rules. Specificity and `!important` (use only as a last resort!) override the cascade.
*   **Box Model:** Elements are boxes: Content -> Padding -> Border -> Margin.
    *   **`box-sizing: border-box;` (Highly Recommended):** Makes `width`/`height` include padding and border. Set globally:
        ```css
        *, *::before, *::after {
          box-sizing: border-box;
        }
        ```
*   **Units:**
    *   Absolute: `px` (common for borders, fixed sizes).
    *   Relative:
        *   `%`: Relative to parent size.
        *   `rem`: Relative to **root** (`html`) font size. **Preferred for scalable typography and spacing.**
        *   `em`: Relative to element's font size.
        *   `vw`, `vh`: Relative to viewport width/height.

## 2. Layout Techniques

*   **Normal Flow:** Default block/inline stacking.
*   **`display` Property:** Controls layout behavior (`block`, `inline`, `inline-block`, `none`, `flex`, `grid`).
*   **Flexbox (`display: flex`):** 1D layout (row or column). Excellent for component layout, alignment, distribution.
    *   Container: `flex-direction`, `justify-content`, `align-items`, `flex-wrap`, `gap`.
    *   Items: `flex-grow`, `flex-shrink`, `flex-basis`, `order`, `align-self`.
    ```css
    .flex-container {
      display: flex;
      justify-content: space-between; /* Example */
      align-items: center;       /* Example */
      gap: 1rem;
    }
    ```
*   **Grid (`display: grid`):** 2D layout (rows & columns). Powerful for overall page structure.
    *   Container: `grid-template-columns`, `grid-template-rows`, `grid-template-areas`, `gap`, `justify-items`, `align-items`.
    *   Items: `grid-column`, `grid-row`, `grid-area`, `justify-self`, `align-self`.
    ```css
    .grid-container {
      display: grid;
      grid-template-columns: 1fr 200px; /* Example */
      gap: 1.5rem;
    }
    ```
*   **Positioning:**
    *   `static` (default): Normal flow.
    *   `relative`: Normal flow, allows offset (`top`/`left` etc.) relative to original position. Creates stacking context.
    *   `absolute`: Removed from flow. Positioned relative to nearest *positioned* ancestor.
    *   `fixed`: Removed from flow. Positioned relative to viewport. Stays fixed on scroll.
    *   `sticky`: Scrolls normally until hitting a threshold (`top`/`bottom`), then sticks.

## 3. Responsiveness (Mobile-First)

*   **Mobile-First Approach:** Write base styles for mobile. Use `min-width` media queries to add/override styles for larger screens.
    ```css
    /* Base mobile styles */
    .element { /* ... */ }

    /* Tablet and up */
    @media (min-width: 768px) {
      .element { /* Adjustments... */ }
    }

    /* Desktop and up */
    @media (min-width: 1024px) {
      .element { /* Further adjustments... */ }
    }
    ```
*   **Relative Units:** Use `rem`, `em`, `%`, `vw`/`vh` appropriately for fluid layouts.
*   **Flexbox & Grid:** Essential for creating flexible, responsive layouts.
*   **Fluid Media:** Use `max-width: 100%; height: auto;` for images/videos.

## 4. Best Practices for Maintainability

*   **Organization:**
    *   Use a consistent naming convention (e.g., BEM: `.block__element--modifier`).
    *   Structure CSS into logical files/modules (base, layout, components). Use Sass/Less partials if applicable.
    *   Use comments (`/* ... */`) for explanations.
*   **DRY (Don't Repeat Yourself):** Group common styles using shared classes or preprocessor features (mixins/extends).
*   **CSS Variables (Custom Properties):** Use `var(--my-variable)` for themeable values (colors, fonts, spacing). Define them typically on `:root` or a component scope.
    ```css
    :root {
      --primary-color: blue;
    }
    .button {
      background-color: var(--primary-color);
    }
    ```
*   **Low Specificity:** Prefer simple class selectors. Avoid `!important`.
*   **Reset/Normalize:** Use a CSS reset (like `normalize.css`) for browser consistency.
*   **Logical Property Order:** Consider a consistent order within rules (e.g., positioning, box model, typography, visual).

## 5. Performance Considerations

*   **Minimize Reflows/Repaints:** Prefer `transform` and `opacity` for animations over properties like `width`, `height`, `top`, `left`.
*   **Selector Efficiency:** Keep selectors reasonably simple (less critical now, but good practice).
*   **Reduce File Size:** Minify CSS for production. Consider tools to remove unused CSS.

*(Refer to MDN Web Docs and resources like CSS-Tricks for more details.)*