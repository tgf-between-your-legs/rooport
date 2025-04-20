# D3.js: Axes

Generating and rendering chart axes using D3's axis components.

## Core Concept: Axis Generators

D3 provides convenient functions (axis generators) that take a **scale** function (like `d3.scaleLinear` or `d3.scaleTime`) as input and produce the necessary SVG elements (lines, ticks, text labels) to render a human-readable axis.

**Key Steps:**

1.  **Create Scale:** Define the scale (`d3.scaleLinear`, `d3.scaleBand`, etc.) for the dimension the axis represents. Set its `domain` and `range`.
2.  **Create Axis Generator:** Create an axis generator function, specifying its orientation and associating it with the scale.
    *   `d3.axisBottom(scale)`
    *   `d3.axisLeft(scale)`
    *   `d3.axisTop(scale)`
    *   `d3.axisRight(scale)`
3.  **Append SVG Group:** Append an SVG `<g>` element to your main SVG container to hold the axis elements.
4.  **Position Group:** Use a `transform` attribute (typically `translate`) on the `<g>` element to position the axis correctly within the chart area (e.g., move the X-axis to the bottom, the Y-axis to the left).
5.  **Call Axis Generator:** Select the `<g>` element and use the `.call()` method to invoke the axis generator function. D3 will then generate the necessary `<path>` (for the axis line) and `<g class="tick">` elements (each containing a `<line>` and `<text>`) inside the selected group.

**Importing:** `import { axisBottom, axisLeft, ... } from 'd3-axis';` (or access via `d3.axisBottom` if using full `d3` import).

## Example: Creating X and Y Axes

```javascript
import * as d3 from 'd3'; // Includes d3-scale, d3-axis, d3-selection

// Assume svg, width, height, margin are defined
// const margin = { top: 20, right: 30, bottom: 40, left: 50 };
// const width = 600 - margin.left - margin.right;
// const height = 400 - margin.top - margin.bottom;
// const svg = d3.select('#chart-svg')
//   .append('g') // Main chart group, translated by margin
//   .attr('transform', `translate(${margin.left},${margin.top})`);

// Sample data and scales
const data = [/* ... your data ... */];
const xScale = d3.scaleLinear()
  .domain([0, d3.max(data, d => d.xValue)]) // Example domain
  .range([0, width])
  .nice(); // Adjust domain to nice round numbers

const yScale = d3.scaleLinear()
  .domain([0, d3.max(data, d => d.yValue)]) // Example domain
  .range([height, 0]) // Y range is inverted (0 is at top)
  .nice();

// --- Create Axis Generators ---
const xAxisGenerator = d3.axisBottom(xScale) // Use xScale for bottom axis
  .ticks(5) // Suggest number of ticks (D3 may adjust)
  .tickSizeOuter(0); // Remove outer ticks if desired

const yAxisGenerator = d3.axisLeft(yScale) // Use yScale for left axis
  .tickFormat(d => `${d}%`); // Example: Format ticks as percentages

// --- Render Axes ---
// X Axis
svg.append('g') // Append a group for the X axis
  .attr('class', 'x-axis') // Optional class for styling
  // Position the X axis group at the bottom of the chart area
  .attr('transform', `translate(0, ${height})`)
  .call(xAxisGenerator); // Call the generator to create elements

// Y Axis
svg.append('g') // Append a group for the Y axis
  .attr('class', 'y-axis') // Optional class
  // No transform needed if positioned at x=0
  .call(yAxisGenerator); // Call the generator

// Optional: Add Axis Labels
svg.append('text')
    .attr('class', 'x-axis-label')
    .attr('text-anchor', 'middle')
    .attr('x', width / 2)
    .attr('y', height + margin.bottom - 5) // Position below x-axis
    .text('X Axis Title');

svg.append('text')
    .attr('class', 'y-axis-label')
    .attr('text-anchor', 'middle')
    .attr('transform', 'rotate(-90)') // Rotate for vertical label
    .attr('y', -margin.left + 15) // Position left of y-axis
    .attr('x', -height / 2)
    .text('Y Axis Title');
```

## Customizing Axes

Axis generators provide methods to customize appearance and behavior:

*   **`.ticks(count)`:** Suggests the approximate number of ticks. D3 determines the final number based on the scale and range. Can also take time intervals for `scaleTime` (e.g., `d3.timeMonth.every(3)`).
*   **`.tickValues(arrayOfValues)`:** Explicitly sets the values where ticks should appear. Overrides `.ticks()`.
*   **`.tickFormat(formatterFn)`:** Specifies a function to format the tick labels (e.g., adding units, changing date format). Takes the tick value `d` as input. D3 provides formatters like `d3.format` and `d3.timeFormat`.
*   **`.tickSize(size)`:** Sets the length of the tick lines.
*   **`.tickSizeInner(size)`:** Sets the length of inner tick lines (default).
*   **`.tickSizeOuter(size)`:** Sets the length of the outer ticks at the ends of the axis line. Often set to 0.
*   **`.tickPadding(padding)`:** Sets the padding (in pixels) between the tick line and its text label.

```javascript
// Example Customization
const xAxis = d3.axisBottom(xScale)
  .tickValues([0, 25, 50, 75, 100]) // Specific tick values
  .tickFormat(d => d + " units") // Add units to labels
  .tickSizeInner(-height) // Make inner ticks act as grid lines across the chart
  .tickSizeOuter(0)
  .tickPadding(10); // Add padding between tick and label

svg.select('.x-axis').call(xAxis); // Re-call the generator to apply changes
```

## Updating Axes

When your data or scales change, you typically update the axis by:

1.  Updating the scale's domain: `myScale.domain(...)`.
2.  Selecting the existing axis group (`svg.select('.x-axis')`).
3.  Optionally adding a transition: `.transition().duration(...)`.
4.  Re-calling the axis generator: `.call(myAxisGenerator)`.

D3's axis components abstract away the complexity of drawing ticks and labels, integrating seamlessly with scales to provide essential context for your visualizations.

*(Refer to the official D3.js documentation for d3-axis.)*