# D3.js Best Practices

Guidelines for writing effective, maintainable, and performant D3.js code.

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
*   **Key Functions:** Provide a key function as the second argument to `.data()` if your data objects might be replaced with new objects representing the same conceptual item. This helps D3 track elements correctly during updates and transitions. ` .data(myData, d => d.id)`

## Modularity

*   **Import Specific Modules:** Instead of importing the entire D3 library (`import * as d3 from 'd3'`), import only the modules you need to reduce bundle size.
    ```javascript
    import { select } from 'd3-selection';
    import { scaleLinear } from 'd3-scale';
    import { axisBottom } from 'd3-axis';
    // etc.
    ```
*   **Reusable Chart Components:** Encapsulate chart logic into reusable functions or classes. Follow patterns like Mike Bostock's "Towards Reusable Charts" or create components within frameworks (React, Vue, Svelte).

## Performance

*   **SVG vs. Canvas:**
    *   **SVG:** Good for interactivity, smaller datasets, declarative approach. Each element is a DOM node. Can become slow with thousands of elements.
    *   **Canvas:** Better for very large datasets (thousands/millions of points) where individual element interaction is less critical. Requires more imperative drawing logic.
*   **Minimize DOM Manipulation:** Avoid unnecessary selections and attribute/style changes within loops or frequent updates. Batch updates where possible.
*   **Efficient Selectors:** Use specific CSS selectors.
*   **Transitions:** Be mindful of transition performance on complex charts. Limit the number of concurrent transitions. Animate performant properties (`transform`, `opacity`).
*   **Data Processing:** Perform data transformations *before* binding data to the DOM.

## Framework Integration (React/Vue/Svelte etc.)

*   **Let Framework Handle DOM:** Use D3 primarily for calculations (scales, layouts, path data) and data binding logic. Let the framework (React/Vue/Svelte) manage the actual rendering and updates of SVG or Canvas elements based on the data/props derived from D3 calculations.
*   **Refs:** Use framework refs (`useRef` in React, `ref` in Vue) to get references to the SVG or Canvas container element.
*   **Lifecycle Hooks/Effects:** Perform D3 setup and data binding within appropriate lifecycle hooks (`useEffect` in React, `onMounted` in Vue). Ensure proper cleanup (removing event listeners, etc.) in unmount hooks (`useEffect` return function, `onUnmounted`).

## Accessibility

*   **SVG Structure:** Use `<title>` and `<desc>` elements within your main `<svg>` tag to describe the chart.
*   **ARIA Roles:** Add appropriate ARIA roles to SVG elements where semantics aren't clear (e.g., `role="graphics-document"`, `role="graphics-symbol"`). Use `aria-label` or `aria-labelledby` for elements like bars or points if they represent meaningful data.
*   **Color Contrast:** Ensure sufficient contrast between visual elements and the background, and between different data series if color is used to distinguish them.
*   **Focus Management:** If adding interactions (tooltips, zooming), ensure elements are keyboard-focusable and focus indicators are visible.
*   **Data Tables:** Consider providing a fallback data table representation for complex charts.

*(Always refer to the latest D3 documentation and community examples for specific patterns.)*