# D3.js Accessibility Guidelines

Making D3.js visualizations accessible to users of assistive technologies.

## Core Principles

*   **Provide Text Alternatives:** Offer non-visual ways to understand the data and chart structure.
*   **Ensure Keyboard Navigability:** Allow users to interact with and explore the visualization using only a keyboard.
*   **Sufficient Contrast:** Ensure visual elements have enough contrast.
*   **Semantic Structure:** Use appropriate HTML/SVG/ARIA roles to convey the structure and meaning.

## SVG Specific Techniques

1.  **`<title>` and `<desc>` Elements:**
    *   Add a `<title>` element as the first child of your main `<svg>` tag to provide a concise, accessible name for the chart.
    *   Add a `<desc>` element after the `<title>` to provide a longer description of the chart's content and purpose.
    ```html
    <svg width="600" height="400">
      <title>Bar Chart of Monthly Sales</title>
      <desc>A bar chart showing total sales for each month from January to June. June had the highest sales.</desc>
      {/* <!-- Rest of SVG content (axes, bars, etc.) --> */}
    </svg>
    ```

2.  **ARIA Roles for Structure:**
    *   Add `role="graphics-document"` or `role="img"` to the main `<svg>` element.
    *   Add `role="graphics-symbol"` to meaningful graphical elements like bars, points, or lines if they represent data points.
    *   Use `role="list"` and `role="listitem"` for legends if appropriate.
    *   Use `role="group"` for axes (`<g class="axis">`).

3.  **Accessible Names (`aria-label`, `aria-labelledby`):**
    *   Add `aria-label` to significant graphical elements (`<rect>`, `<circle>`, `<path>`) to describe the data point they represent (e.g., `aria-label="Sales for June: $5000"`). This is often generated dynamically during the data join.
    *   Alternatively, use `aria-labelledby` to reference existing text elements (like axis labels or tooltips) that describe the element.

4.  **Focus Management for Interaction:**
    *   If elements are interactive (e.g., clickable bars, points with tooltips), make them focusable by adding `tabindex="0"` to the SVG element (e.g., `<rect tabindex="0">`).
    *   Ensure a clear visual focus indicator (e.g., using CSS `outline` or changing `stroke`/`fill` on `:focus`).
    *   Handle keyboard events (Enter/Space) to trigger actions equivalent to mouse clicks.

## General Techniques (SVG & Canvas)

5.  **Color Contrast:** Ensure sufficient contrast between data elements (bars, lines, points) and the background, and between different data series if color is the primary distinction (WCAG 1.4.1, 1.4.11). Use contrast checking tools. Provide alternative ways to distinguish series (patterns, shapes, labels).
6.  **Alternative Data Representation:** For complex visualizations, consider providing the underlying data in an accessible HTML `<table>` alongside or linked from the chart. This provides direct access for screen reader users.
7.  **Tooltips:** Ensure tooltips are accessible:
    *   Triggerable via keyboard focus as well as hover.
    *   Content read by screen readers (potentially using `aria-describedby` linking the trigger element to the tooltip content, or using live regions if tooltips appear dynamically).
    *   Dismissible via the Escape key.
8.  **Simplicity:** Avoid overly complex charts that are inherently difficult to interpret non-visually. Choose chart types appropriate for the data and the message.

## Framework Integration

*   When using D3 within React/Vue/Svelte, ensure ARIA attributes and `tabindex` are correctly applied to the rendered SVG/HTML elements managed by the framework.

*(Implementing full accessibility can be complex. Consult WCAG guidelines, ARIA Authoring Practices, and collaborate with `accessibility-specialist`.)*