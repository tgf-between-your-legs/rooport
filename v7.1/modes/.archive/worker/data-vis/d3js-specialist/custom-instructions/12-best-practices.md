# D3.js: Best Practices

Guidelines for writing effective, maintainable, and performant D3.js code (v4-v7+).

## Data Binding

*   **Use `.join()` (v6+):** Prefer the `.join()` method for handling enter, update, and exit selections concisely. It simplifies the older `.enter().append().merge()` pattern.
    ```javascript
    svg.selectAll('circle')
      .data(myData, d => d.id) // Use a key function if data objects change identity
      .join(
        enter => enter.append('circle')
                      .attr('cx', d => xScale(d.x))
                      .attr('cy', d => yScale(d.y))
                      .attr('r', 0)
                      .call(enter => enter.transition().duration(500).attr('r', 5)), // Enter transition
        update => update
                      .call(update => update.transition().duration(500) // Update transition
                                        .attr('cx', d => xScale(d.x))
                                        .attr('cy', d => yScale(d.y))),
        exit => exit
                      .call(exit => exit.transition().duration(500).attr('r', 0).remove()) // Exit transition
      );
    ```
*   **Key Functions:** Provide a key function as the second argument to `.data()` if your data objects might be replaced with new objects representing the same conceptual item. This helps D3 track elements correctly during updates and transitions, enabling object constancy. ` .data(myData, d => d.id)`

## Modularity

*   **Import Specific Modules:** Instead of importing the entire D3 library (`import * as d3 from 'd3'`), import only the modules you need to reduce bundle size, especially in module-based projects.
    ```javascript
    import { select } from 'd3-selection';
    import { scaleLinear } from 'd3-scale';
    import { axisBottom } from 'd3-axis';
    // etc.
    ```
*   **Reusable Chart Components:** Encapsulate chart logic into reusable functions or classes. Follow patterns like Mike Bostock's "Towards Reusable Charts" or create components within frameworks (React, Vue, Svelte).

## Performance

*   **SVG vs. Canvas:** Choose based on element count and interaction needs. SVG is easier for moderate elements and interaction; Canvas excels for vast numbers of elements where performance is paramount. (See `08-rendering-svg-canvas.md` and `11-performance.md`)
*   **Minimize DOM Manipulation:** Avoid unnecessary selections and attribute/style changes within loops or frequent updates. Batch updates where possible.
*   **Efficient Selectors:** Use specific CSS selectors.
*   **Transitions:** Be mindful of transition performance on complex charts. Limit the number of concurrent transitions. Animate performant properties (`transform`, `opacity`).
*   **Data Processing:** Perform data transformations *before* binding data to the DOM.

## Framework Integration (React/Vue/Svelte etc.)

*   **Let Framework Handle DOM (Simpler Cases):** Use D3 for calculations (scales, layouts, path data), let the framework render SVG/Canvas elements based on props/state derived from D3.
*   **D3 Controls Container (Complex Cases):** Use framework refs (`useRef`, `ref`) to get a container element. Use D3 (`d3.select`) inside lifecycle hooks (`useEffect`, `onMounted`) to manage the container's contents, enabling full use of D3 joins, transitions, and interactions. Requires careful lifecycle management and cleanup. (See `09-framework-integration.md`)

## Accessibility

*   **SVG Structure:** Use `<title>` and `<desc>` elements within your main `<svg>` tag.
*   **ARIA Roles:** Add appropriate ARIA roles (e.g., `role="graphics-document"`, `role="graphics-symbol"`, `aria-label`) to SVG elements.
*   **Color Contrast:** Ensure sufficient contrast. Don't rely solely on color.
*   **Focus Management:** Ensure interactive elements are keyboard-focusable with visible focus indicators.
*   **Data Tables:** Consider providing a fallback data table. (See `10-accessibility.md`)

## General Code Quality

*   **Clarity:** Write clear, well-commented code, especially for complex logic, scales, or data transformations.
*   **Consistency:** Maintain consistent coding style and naming conventions.
*   **Error Handling:** Handle potential errors during data loading or processing.

*(Always refer to the latest D3 documentation and community examples for specific patterns.)*