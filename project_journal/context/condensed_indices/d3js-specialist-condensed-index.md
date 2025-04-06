## D3.js v7 (inferred) - Condensed Context Index

### Overall Purpose
D3.js (Data-Driven Documents) is a JavaScript library for manipulating documents based on data, primarily used for creating dynamic, interactive data visualizations for the web using SVG, Canvas, and HTML. It emphasizes efficient data binding to the DOM and provides powerful tools for visual encoding (scales, axes, shapes), layout algorithms, transitions, and interactions.

### Core Concepts & Capabilities
*   **Selections & Data Binding:** Select DOM elements (`d3.select`, `d3.selectAll`), bind data (`.data()`), and manage entering/updating/exiting elements (`.join()`, `.enter()`, `.exit()`). Key for data-driven documents.
*   **Scales:** Map data domains (e.g., numbers, dates) to visual ranges (e.g., pixels, colors) using various scale types (`d3.scaleLinear`, `d3.scaleBand`, `d3.scaleUtc`). Essential for visual encoding.
*   **Axes:** Generate SVG axes based on scales, including ticks and labels (`d3.axisBottom`, `d3.axisLeft`, `.call()`, `.ticks()`, `.tickFormat()`).
*   **Shape Generators:** Create SVG `path` data for common chart elements like lines, areas, and arcs/sectors (`d3.line`, `d3.area`, `d3.arc`). `.curve()` modifies interpolation.
*   **Layouts:** Algorithms to position elements for specific chart types like stacked charts, treemaps, pack layouts, and force-directed graphs (`d3.stack`, `d3.treemap`, `d3.pack`, `d3.forceSimulation`).
*   **Transitions & Animations:** Animate changes to element attributes and styles smoothly over time (`.transition()`, `.duration()`, `.delay()`, `.attrTween()`).
*   **Interactions:** Implement user interactions like zooming and dragging (`d3.drag`).
*   **Data Manipulation:** Utilities for grouping, summarizing, and transforming data (`d3.group`, `d3.rollup`, `d3.count`).
*   **Geometric Utilities:** Tools for computational geometry like Delaunay triangulations and Voronoi diagrams (`d3.Delaunay`, `.voronoi()`).

### Key APIs / Components / Configuration / Patterns
*   `d3.select(selector)` / `d3.selectAll(selector)`: Select DOM elements using CSS selectors.
*   `selection.data(data, [key])`: Bind an array of data to selected elements. Use key function for object constancy.
*   `selection.join(enter[, update][, exit])`: Efficiently handle enter/update/exit selections in one call.
*   `selection.enter()`: Returns placeholder nodes for data points with no corresponding DOM element.
*   `selection.exit()`: Returns DOM elements with no corresponding data point. `.remove()` deletes them.
*   `selection.append(type)`: Append a new element of the given type (e.g., "g", "circle", "path").
*   `selection.attr(name, value)`: Set an attribute value (e.g., `cx`, `cy`, `fill`, `d`).
*   `selection.style(name, value)`: Set a style property value (e.g., `background-color`, `color`).
*   `selection.text(value)`: Set the text content.
*   `selection.call(function[, args...])`: Call a function once for the selection. Used for axes (`.call(axis)`), drag (`.call(drag)`), and reusable code.
*   `selection.each(function)`: Call a function for each selected element, accessing data (`d`) and index (`i`).
*   `selection.filter(selector)`: Filter selection based on a selector string or function.
*   `d3.scaleLinear([domain], [range])`: Create a continuous linear scale. `.invert(value)` finds domain value.
*   `d3.scaleBand([domain], [range])`: Create an ordinal scale with uniform bands (bar charts). `.bandwidth()` gives band width. `.padding(p)` adds spacing.
*   `d3.scaleUtc([domain], [range])`: Create a linear scale for UTC dates.
*   `d3.axisBottom(scale)` / `d3.axisLeft(scale)` / `d3.axisTop(scale)` / `d3.axisRight(scale)`: Create axis generators. Apply with `.call(axis)`.
*   `axis.ticks([count[, specifier]])`: Suggest tick count/format.
*   `axis.tickFormat(format)`: Specify tick label format (e.g., `d3.format(",.0f")`).
*   `d3.line([x][, y])`: Create a line generator. Returns path data string. `.curve(curve)` sets interpolation (e.g., `d3.curveStep`).
*   `d3.area([x][, y0][, y1])`: Create an area generator. `.defined(boolean)` handles gaps. `.curve(curve)` sets interpolation.
*   `d3.arc()`: Create an arc/pie slice generator. Configure `innerRadius`, `outerRadius`, `startAngle`, `endAngle`.
*   `d3.stack().keys(keys).value(value)`: Create a stack layout generator for stacked bar/area charts.
*   `d3.treemap().size([w, h]).padding(p)`: Create a treemap layout generator. Requires `root.sum()` and `root.sort()`.
*   `d3.pack().size([w, h])`: Create a circle-packing layout generator. Requires `root.sum()`.
*   `d3.forceSimulation(nodes)`: Create a physics-based force simulation for network graphs.
*   `d3.forceLink(links)`: Force to maintain link distances between nodes.
*   `d3.forceManyBody()`: Force for node repulsion (negative strength) or attraction (positive strength).
*   `d3.forceCenter([x, y])`: Force to attract nodes towards a center point.
*   `selection.transition([name])`: Start a transition on selected elements.
*   `transition.duration(ms)`: Set transition duration.
*   `transition.delay(ms)`: Set transition delay.
*   `transition.attrTween(name, interpolator)`: Interpolate attribute values (e.g., `d3.interpolateRgb`).
*   `d3.drag().on(type, listener)`: Create drag behavior. Listeners: `start`, `drag`, `end`. Apply with `.call(drag)`.
*   `d3.group(iterable, ...keys)`: Group data into a nested Map based on key functions.
*   `d3.rollup(iterable, reduce, ...keys)`: Group and reduce data into a nested Map.
*   `d3.count(iterable, [accessor])`: Count valid numbers in data, ignoring null/NaN/undefined.
*   `d3.Delaunay.from(points)`: Create Delaunay triangulation. `.voronoi([bounds])` gets Voronoi diagram.
*   `path.bounds(object)`: Compute bounding box for GeoJSON object using a D3 path generator.

### Common Patterns & Best Practices / Pitfalls
*   **Method Chaining:** D3 heavily relies on method chaining for concise code (`d3.select(...).attr(...).style(...)`).
*   **Data Joining (Enter/Update/Exit):** The core pattern is selecting elements, binding data (`.data()`), and handling enter/update/exit states (`.join()` or `.enter()`/`.exit()`). Use key functions with `.data()` for object constancy when data changes.
*   **SVG Structure & Margins:** Charts are typically built within an `<svg>` element, using `<g>` for grouping (e.g., axes, chart elements). Define margins (`marginTop`, `marginLeft`, etc.) to create space for axes. Position elements using `transform="translate(x,y)"`.
*   **Scales as Functions:** Scales map data to visual attributes. Use them like functions: `x(dataValue)` returns pixel position, `color(dataValue)` returns color string.
*   **Generators:** Shape and Layout generators compute positions or path data. Apply their output to element attributes (e.g., `path.attr("d", line(data))`, `circles.attr("cx", d => d.x)`).
*   **Transitions:** Use `.transition()` for smooth visual updates. Chain transitions (`.transition()...transition()...`) for sequences. Use `.attrTween` for complex interpolations.
*   **Framework Integration (React/Svelte/etc.):** Use D3 for calculations (scales, layouts, generators) and let the framework manage DOM updates, or use D3's selections within lifecycle hooks/effects.
*   **ES Modules:** Use `import * as d3 from "d3";` or import specific modules (`import { scaleLinear } from "d3-scale";`). Can load from CDNs via `<script type="module">`.

---
This index summarizes the core concepts, APIs, and patterns for D3.js v7 based on the provided snippets. Consult the full source documentation (project_journal/context/source_docs/d3js-specialist-llms-context-20250406.md or official D3 docs) for exhaustive details.