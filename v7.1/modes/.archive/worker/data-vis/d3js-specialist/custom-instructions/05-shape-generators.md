# D3.js: Shape Generators

Creating complex SVG shapes like lines, areas, and arcs from data using D3 generators.

## Core Concept: Shape Generators

D3 provides **shape generator** functions that take data (often an array of points or a specific value) and return the string value needed for an SVG element's attribute (typically the `d` attribute of a `<path>` element). They abstract the complex calculations needed to draw lines, areas, arcs (for pie/donut charts), symbols, etc.

**Key Steps:**

1.  **Create Generator:** Instantiate a shape generator function (e.g., `d3.line()`, `d3.arc()`).
2.  **Configure Accessors:** Configure the generator using methods like `.x()`, `.y()`, `.innerRadius()`, `.startAngle()`, etc. These methods tell the generator how to access the relevant data points from your data objects. They usually accept a function `(d, i) => value`.
3.  **Bind Data (Optional but common):** Bind your data array to the SVG element(s) that will use the shape (e.g., bind an array of points to a single `<path>` for a line chart, or bind an array of values to multiple `<path>` elements for arcs in a pie chart).
4.  **Apply Generator:** Call the generator function, passing in the relevant data point(s). Set the result to the appropriate SVG attribute (usually `d` for `<path>`).

**Importing:** `import { line, arc, area, symbol, ... } from 'd3-shape';`

## Common Shape Generators

**1. `d3.line()`:**

*   **Purpose:** Generates the `d` attribute string for a `<path>` element representing a line connecting multiple points.
*   **Input Data:** Typically an array of data points `[point1, point2, ...]`.
*   **Accessors:**
    *   `.x((d, i) => xValue)`: Function to get the x-coordinate for data point `d`. Often uses an X scale.
    *   `.y((d, i) => yValue)`: Function to get the y-coordinate for data point `d`. Often uses a Y scale.
    *   `.defined((d, i) => boolean)`: Optional function to determine if a point should be included (e.g., skip missing data).
    *   `.curve(curveType)`: Specifies how points are interpolated (e.g., `d3.curveLinear`, `d3.curveStep`, `d3.curveBasis`, `d3.curveMonotoneX`).

```javascript
import * as d3 from 'd3';

const lineData = [ {x: 0, y: 5}, {x: 1, y: 9}, {x: 2, y: 3}, {x: 3, y: 7} ];
const xScale = d3.scaleLinear().domain([0, 3]).range([0, width]); // Assume width defined
const yScale = d3.scaleLinear().domain([0, 10]).range([height, 0]); // Assume height defined

// Create the line generator
const lineGenerator = d3.line()
  .x(d => xScale(d.x)) // Use scales to position points
  .y(d => yScale(d.y))
  .curve(d3.curveMonotoneX); // Apply smoothing

// Append path and set 'd' attribute using the generator
svg.append('path') // Assume svg defined
  .datum(lineData) // Bind the array of points to the single path
  .attr('fill', 'none')
  .attr('stroke', 'steelblue')
  .attr('stroke-width', 1.5)
  .attr('d', lineGenerator); // Call generator with the data array
```

**2. `d3.area()`:**

*   **Purpose:** Generates a filled area shape, typically defined by a top line and a baseline. Similar to `d3.line()`, but creates a closed shape.
*   **Input Data:** Array of data points.
*   **Accessors:**
    *   `.x((d, i) => xValue)` or `.x0()`, `.x1()` (for vertical areas).
    *   `.y0((d, i) => yValue)`: Defines the baseline of the area (often the bottom axis or 0).
    *   `.y1((d, i) => yValue)`: Defines the top line of the area.
    *   `.curve(curveType)`

```javascript
const areaGenerator = d3.area()
  .x(d => xScale(d.x))
  .y0(height) // Baseline at the bottom of the chart
  .y1(d => yScale(d.y)) // Top line based on data value
  .curve(d3.curveBasis);

svg.append('path')
  .datum(lineData)
  .attr('fill', 'lightsteelblue')
  .attr('d', areaGenerator);
```

**3. `d3.arc()`:**

*   **Purpose:** Generates the `d` attribute for arc shapes, commonly used for pie charts, donut charts, or radial plots.
*   **Input Data:** Typically used with data processed by `d3.pie()`, which adds `startAngle` and `endAngle` properties to each data object. (See `06-layouts.md`)
*   **Accessors:**
    *   `.innerRadius(radius)`: Inner radius (0 for pie chart, >0 for donut).
    *   `.outerRadius(radius)`: Outer radius.
    *   `.startAngle(d => d.startAngle)`: (Usually set by `d3.pie`).
    *   `.endAngle(d => d.endAngle)`: (Usually set by `d3.pie`).
    *   `.padAngle(angle)`: Padding between arcs.
    *   `.cornerRadius(radius)`: Rounds arc corners.

```javascript
const pieData = [ {label: 'A', value: 10}, {label: 'B', value: 20}, {label: 'C', value: 15} ];
const radius = Math.min(width, height) / 2;

// Pie layout generator: calculates start/end angles
const pie = d3.pie()
  .value(d => d.value) // Tell pie layout which property holds the value
  .sort(null); // Optional: disable sorting

// Arc generator: draws the arc shape based on angles/radii
const arcGenerator = d3.arc()
  .innerRadius(radius * 0.5) // Example: Donut chart
  .outerRadius(radius * 0.9);

const colorScale = d3.scaleOrdinal(d3.schemeCategory10);

// Create groups for each arc, positioned at the center
const arcs = svg.selectAll('.arc')
  .data(pie(pieData)) // Pass data to pie layout first
  .join('g')
    .attr('class', 'arc')
    .attr('transform', `translate(${width / 2}, ${height / 2})`);

// Append path for each arc
arcs.append('path')
  .attr('d', arcGenerator) // Use arc generator to draw path
  .attr('fill', (d, i) => colorScale(i)); // Use color scale

// Optional: Add labels
arcs.append('text')
  .attr('transform', d => `translate(${arcGenerator.centroid(d)})`) // Position text at arc centroid
  .attr('dy', '0.35em')
  .attr('text-anchor', 'middle')
  .text(d => d.data.label);
```

**4. `d3.symbol()`:**

*   **Purpose:** Generates path data for predefined symbol shapes (circle, cross, diamond, square, star, triangle, wye). Used in scatter plots.
*   **Accessors:**
    *   `.type(symbolType)`: Sets the symbol type (e.g., `d3.symbolCircle`, `d3.symbolStar`). Can be a function `(d, i) => type`.
    *   `.size(size)`: Sets the area of the symbol in square pixels. Can be a function.

```javascript
const scatterData = [ /* ... { x: ..., y: ..., type: 'A'|'B', value: ... } ... */ ];
const symbolGenerator = d3.symbol()
  .type(d => d.type === 'A' ? d3.symbolCircle : d3.symbolSquare) // Different symbol based on data
  .size(d => d.value * 10); // Size based on data

svg.selectAll('.symbol')
  .data(scatterData)
  .join('path')
    .attr('class', 'symbol')
    .attr('transform', d => `translate(${xScale(d.x)}, ${yScale(d.y)})`) // Position symbol
    .attr('d', symbolGenerator) // Generate path data for the symbol
    .attr('fill', 'purple');
```

Shape generators are powerful tools for drawing complex SVG shapes based on data, forming the visual core of many D3 visualizations.

*(Refer to the official D3.js documentation for d3-shape.)*