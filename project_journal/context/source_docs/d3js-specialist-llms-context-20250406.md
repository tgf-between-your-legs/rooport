TITLE: Creating and Positioning a D3.js Axis
DESCRIPTION: This snippet demonstrates how to create a bottom-oriented axis using D3.js and position it within an SVG element. It uses the axisBottom function and applies a transform to set the axis position.

LANGUAGE: javascript
CODE:
const gx = svg.append("g")
    .attr("transform", `translate(0,${height - marginBottom})`)
    .call(d3.axisBottom(x));

----------------------------------------

TITLE: Creating an HTML table from a matrix using D3.js data joining
DESCRIPTION: This snippet demonstrates how to use selection.data() and selection.join() to create an HTML table from a matrix of numbers. It shows the process of binding data to DOM elements and creating new elements based on the data.

LANGUAGE: JavaScript
CODE:
const matrix = [
  [11975,  5871, 8916, 2868],
  [ 1951, 10048, 2060, 6171],
  [ 8010, 16145, 8090, 8045],
  [ 1013,   990,  940, 6907]
];

d3.select("body")
  .append("table")
  .selectAll("tr")
  .data(matrix)
  .join("tr")
  .selectAll("td")
  .data(d => d)
  .join("td")
    .text(d => d);

----------------------------------------

TITLE: Creating a Line Plot with D3 in React
DESCRIPTION: This React component creates a line plot using D3. It demonstrates how to use D3's scale and line functions within a React component, and how to create SVG elements using JSX.

LANGUAGE: jsx
CODE:
import * as d3 from "d3";

export default function LinePlot({
  data,
  width = 640,
  height = 400,
  marginTop = 20,
  marginRight = 20,
  marginBottom = 20,
  marginLeft = 20
}) {
  const x = d3.scaleLinear([0, data.length - 1], [marginLeft, width - marginRight]);
  const y = d3.scaleLinear(d3.extent(data), [height - marginBottom, marginTop]);
  const line = d3.line((d, i) => x(i), y);
  return (
    <svg width={width} height={height}>
      <path fill="none" stroke="currentColor" strokeWidth="1.5" d={line(data)} />
      <g fill="white" stroke="currentColor" strokeWidth="1.5">
        {data.map((d, i) => (<circle key={i} cx={x(i)} cy={y(d)} r="2.5" />))}
      </g>
    </svg>
  );
}

----------------------------------------

TITLE: Creating a Blank Chart with D3 in JavaScript
DESCRIPTION: This snippet demonstrates how to create a basic chart structure using D3. It sets up the chart dimensions, scales for x and y axes, creates an SVG container, and adds x and y axes.

LANGUAGE: javascript
CODE:
{
  // Declare the chart dimensions and margins.
  const width = 640;
  const height = 400;
  const marginTop = 20;
  const marginRight = 20;
  const marginBottom = 30;
  const marginLeft = 40;

  // Declare the x (horizontal position) scale.
  const x = d3.scaleUtc()
      .domain([new Date("2023-01-01"), new Date("2024-01-01")])
      .range([marginLeft, width - marginRight]);

  // Declare the y (vertical position) scale.
  const y = d3.scaleLinear()
      .domain([0, 100])
      .range([height - marginBottom, marginTop]);

  // Create the SVG container.
  const svg = d3.create("svg")
      .attr("width", width)
      .attr("height", height);

  // Add the x-axis.
  svg.append("g")
      .attr("transform", `translate(0,${height - marginBottom})`)
      .call(d3.axisBottom(x));

  // Add the y-axis.
  svg.append("g")
      .attr("transform", `translate(${marginLeft},0)`)
      .call(d3.axisLeft(y));

  // Return the SVG element.
  return svg.node();
}

----------------------------------------

TITLE: Using selection.join() for enter, update, and exit in D3.js
DESCRIPTION: This snippet demonstrates the use of selection.join() as a convenient alternative to the explicit general update pattern. It shows how to handle enter, update, and exit selections in a single method call.

LANGUAGE: JavaScript
CODE:
svg.selectAll("circle")
  .data(data)
  .join(
    enter => enter.append("circle").attr("fill", "green"),
    update => update.attr("fill", "blue")
  )
    .attr("stroke", "black");

----------------------------------------

TITLE: Creating a Line Plot with D3 in Svelte
DESCRIPTION: This Svelte component creates a line plot using D3. It shows how to use D3's scale and line functions within a Svelte component, and how to create SVG elements using Svelte's template syntax.

LANGUAGE: svelte
CODE:
<script>
  import * as d3 from 'd3';

  export let data;
  export let width = 640;
  export let height = 400;
  export let marginTop = 20;
  export let marginRight = 20;
  export let marginBottom = 20;
  export let marginLeft = 20;

  $: x = d3.scaleLinear([0, data.length - 1], [marginLeft, width - marginRight]);
  $: y = d3.scaleLinear(d3.extent(data), [height - marginBottom, marginTop]);
  $: line = d3.line((d, i) => x(i), y);
</script>
<svg width={width} height={height}>
  <path fill="none" stroke="currentColor" stroke-width="1.5" d={line(data)} />
  <g fill="white" stroke="currentColor" stroke-width="1.5">
    {#each data as d, i}
      <circle key={i} cx={x(i)} cy={y(d)} r="2.5" />
    {/each}
  </g>
</svg>

----------------------------------------

TITLE: Formatting D3.js Axis Ticks
DESCRIPTION: These snippets show different ways to format axis ticks in D3.js. The first uses a custom format function, while the second uses a format specifier with the ticks method.

LANGUAGE: javascript
CODE:
axis.tickFormat(d3.format(",.0f"));

LANGUAGE: javascript
CODE:
axis.ticks(10, ",f");

----------------------------------------

TITLE: Using D3 in Vanilla HTML with ES Modules
DESCRIPTION: This example shows how to use D3 in a vanilla HTML file using ES modules. It creates a basic chart structure similar to the previous example, but in the context of an HTML page.

LANGUAGE: html
CODE:
<!DOCTYPE html>
<div id="container"></div>
<script type="module">

import * as d3 from "https://cdn.jsdelivr.net/npm/d3@7/+esm";

// Declare the chart dimensions and margins.
const width = 640;
const height = 400;
const marginTop = 20;
const marginRight = 20;
const marginBottom = 30;
const marginLeft = 40;

// Declare the x (horizontal position) scale.
const x = d3.scaleUtc()
    .domain([new Date("2023-01-01"), new Date("2024-01-01")])
    .range([marginLeft, width - marginRight]);

// Declare the y (vertical position) scale.
const y = d3.scaleLinear()
    .domain([0, 100])
    .range([height - marginBottom, marginTop]);

// Create the SVG container.
const svg = d3.create("svg")
    .attr("width", width)
    .attr("height", height);

// Add the x-axis.
svg.append("g")
    .attr("transform", `translate(0,${height - marginBottom})`)
    .call(d3.axisBottom(x));

// Add the y-axis.
svg.append("g")
    .attr("transform", `translate(${marginLeft},0)`)
    .call(d3.axisLeft(y));

// Append the SVG element.
container.append(svg.node());

</script>

----------------------------------------

TITLE: Basic D3 Element Selection and Modification
DESCRIPTION: Demonstrates how to select all paragraph elements and modify their class and color using method chaining.

LANGUAGE: javascript
CODE:
d3.selectAll("p")
    .attr("class", "graf")
    .style("color", "red");

----------------------------------------

TITLE: Applying Linear Scale for Position
DESCRIPTION: Demonstrates using a linear scale to map domain values to pixel positions in a range of 0-960

LANGUAGE: javascript
CODE:
const x = d3.scaleLinear([10, 130], [0, 960]);
x(20); // 80
x(50); // 320

----------------------------------------

TITLE: Rendering a Line Path in D3.js
DESCRIPTION: Shows how to use a line generator to create an SVG path element with the generated line data.

LANGUAGE: javascript
CODE:
svg.append("path").attr("d", line(data)).attr("stroke", "currentColor");

----------------------------------------

TITLE: Creating Basic D3 Transition in JavaScript
DESCRIPTION: Demonstrates how to create a simple transition that changes the background color of the body element. This example shows the basic transition syntax using d3.select() followed by transition() and style() methods.

LANGUAGE: javascript
CODE:
d3.select("body")
  .transition()
    .style("background-color", "red");

----------------------------------------

TITLE: Handling enter and exit selections in D3.js
DESCRIPTION: This example demonstrates the use of selection.enter() and selection.exit() to handle new and removed data points. It shows how to create new elements for entering data and remove elements for exiting data.

LANGUAGE: JavaScript
CODE:
div = div.data([1, 2, 4, 8, 16, 32], d => d);

div.enter().append("div").text(d => d);

div.exit().remove();

----------------------------------------

TITLE: Configuring Force Simulation with Multiple Forces
DESCRIPTION: Example of creating a force simulation with multiple forces including many-body force, link force, and centering force for graph layout.

LANGUAGE: javascript
CODE:
const simulation = d3.forceSimulation(nodes)
    .force("charge", d3.forceManyBody())
    .force("link", d3.forceLink(links))
    .force("center", d3.forceCenter());

----------------------------------------

TITLE: Joining data by key in D3.js
DESCRIPTION: This example shows how to use a key function with selection.data() to join data to DOM elements based on a unique identifier. It demonstrates handling both the datum and the DOM element's properties in the key function.

LANGUAGE: HTML
CODE:
<div id="Ford"></div>
<div id="Jarrah"></div>
<div id="Kwon"></div>
<div id="Locke"></div>
<div id="Reyes"></div>
<div id="Shephard"></div>

LANGUAGE: JavaScript
CODE:
const data = [
  {name: "Locke", number: 4},
  {name: "Reyes", number: 8},
  {name: "Ford", number: 15},
  {name: "Jarrah", number: 16},
  {name: "Shephard", number: 23},
  {name: "Kwon", number: 42}
];

d3.selectAll("div")
  .data(data, function(d) { return d ? d.name : this.id; })
    .text(d => d.number);

----------------------------------------

TITLE: Rendering Stacked Bar Chart with D3.js
DESCRIPTION: Shows how to use the generated stacked data to create a stacked bar chart using SVG rectangles. This snippet includes positioning and styling of the bars.

LANGUAGE: JavaScript
CODE:
svg.append("g")
  .selectAll("g")
  .data(series)
  .join("g")
    .attr("fill", d => color(d.key))
  .selectAll("rect")
  .data(D => D)
  .join("rect")
    .attr("x", d => x(d.data[0]))
    .attr("y", d => y(d[1]))
    .attr("height", d => y(d[0]) - y(d[1]))
    .attr("width", x.bandwidth());

----------------------------------------

TITLE: Grouping Data with D3.js group() Function
DESCRIPTION: Demonstrates how to use d3.group() to group an iterable of values into an InternMap. The example shows grouping a penguins dataset by species and accessing grouped data.

LANGUAGE: javascript
CODE:
const species = d3.group(penguins, (d) => d.species);

LANGUAGE: javascript
CODE:
species.get("Adelie") // Array(152)

LANGUAGE: javascript
CODE:
const speciesSex = d3.group(penguins, (d) => d.species, (d) => d.sex)

LANGUAGE: javascript
CODE:
speciesSex.get("Adelie").get("FEMALE") // Array(73)

----------------------------------------

TITLE: HTML Structure of a D3.js Axis
DESCRIPTION: This HTML snippet shows the typical structure of a D3.js-generated axis. It includes the main group element, domain path, and individual tick groups with lines and text elements.

LANGUAGE: html
CODE:
<g fill="none" font-size="10" font-family="sans-serif" text-anchor="middle">
  <path class="domain" stroke="currentColor" d="M0.5,6V0.5H880.5V6"></path>
  <g class="tick" opacity="1" transform="translate(0.5,0)">
    <line stroke="currentColor" y2="6"></line>
    <text fill="currentColor" y="9" dy="0.71em">0.0</text>
  </g>
  <g class="tick" opacity="1" transform="translate(176.5,0)">
    <line stroke="currentColor" y2="6"></line>
    <text fill="currentColor" y="9" dy="0.71em">0.2</text>
  </g>
  <g class="tick" opacity="1" transform="translate(352.5,0)">
    <line stroke="currentColor" y2="6"></line>
    <text fill="currentColor" y="9" dy="0.71em">0.4</text>
  </g>
  <g class="tick" opacity="1" transform="translate(528.5,0)">
    <line stroke="currentColor" y2="6"></line>
    <text fill="currentColor" y="9" dy="0.71em">0.6</text>
  </g>
  <g class="tick" opacity="1" transform="translate(704.5,0)">
    <line stroke="currentColor" y2="6"></line>
    <text fill="currentColor" y="9" dy="0.71em">0.8</text>
  </g>
  <g class="tick" opacity="1" transform="translate(880.5,0)">
    <line stroke="currentColor" y2="6"></line>
    <text fill="currentColor" y="9" dy="0.71em">1.0</text>
  </g>
</g>

----------------------------------------

TITLE: Generating Stacked Data with D3.js
DESCRIPTION: Demonstrates how to use the stack generator to create stacked data from a dataset. This example shows data preparation, key selection, and value computation for fruit sales data.

LANGUAGE: JavaScript
CODE:
const series = d3.stack()
    .keys(d3.union(data.map(d => d.fruit))) // apples, bananas, cherries, …
    .value(([, group], key) => group.get(key).sales)
  (d3.index(data, d => d.date, d => d.fruit));

----------------------------------------

TITLE: Grouping and Reducing Data with D3.js rollup() Function
DESCRIPTION: Demonstrates the use of d3.rollup() to group and reduce an iterable of values into an InternMap. The example shows grouping and counting penguins by species and sex.

LANGUAGE: javascript
CODE:
const speciesCount = d3.rollup(penguins, (D) => D.length, (d) => d.species);

LANGUAGE: javascript
CODE:
speciesCount.get("Adelie") // 152

LANGUAGE: javascript
CODE:
const speciesSexCount = d3.rollup(penguins, (D) => D.length, (d) => d.species, (d) => d.sex);

LANGUAGE: javascript
CODE:
speciesSexCount.get("Adelie").get("FEMALE") // 73

----------------------------------------

TITLE: Linear Scale with Color Interpolation
DESCRIPTION: Shows how to create and use a linear scale for color interpolation between brown and steelblue

LANGUAGE: javascript
CODE:
const color = d3.scaleLinear([10, 100], ["brown", "steelblue"]);
color(20); // "rgb(154, 52, 57)"
color(50); // "rgb(123, 81, 103)"

----------------------------------------

TITLE: Applying D3 Drag Behavior to Selection in JavaScript
DESCRIPTION: Shows how to apply a drag behavior to a D3 selection using the call() method. This example also demonstrates setting an event listener for the 'start' event.

LANGUAGE: JavaScript
CODE:
d3.selectAll(".node").call(d3.drag().on("start", started));

----------------------------------------

TITLE: Creating a Band Scale in D3
DESCRIPTION: Demonstrates how to construct a new band scale with a specified domain and range.

LANGUAGE: javascript
CODE:
const x = d3.scaleBand(["a", "b", "c"], [0, 960]);

----------------------------------------

TITLE: Linear Scale Inversion
DESCRIPTION: Demonstrates inverting a linear scale to get domain values from range values

LANGUAGE: javascript
CODE:
const x = d3.scaleLinear([10, 130], [0, 960]);
x.invert(80); // 20
x.invert(320); // 50

----------------------------------------

TITLE: D3 Element Creation and Insertion
DESCRIPTION: Shows different approaches to creating and appending elements using D3.

LANGUAGE: javascript
CODE:
d3.selectAll("div").append("p");

LANGUAGE: javascript
CODE:
d3.selectAll("div").append(() => document.createElement("p"));

LANGUAGE: javascript
CODE:
d3.selectAll("div").select(function() {
  return this.appendChild(document.createElement("p"));
});

----------------------------------------

TITLE: Iterating over Selection Elements with each() in D3
DESCRIPTION: Demonstrates how to use the each() method to iterate over selected elements, accessing both parent and child data simultaneously.

LANGUAGE: javascript
CODE:
parent.each(function(p, j) {
  d3.select(this)
    .selectAll(".child")
      .text(d => `child ${d.name} of ${p.name}`);
});

----------------------------------------

TITLE: Creating Delaunay Triangulation and Voronoi Diagram with D3
DESCRIPTION: Demonstrates how to create a Delaunay triangulation from a set of points and then generate the corresponding Voronoi diagram with specified bounds using D3.

LANGUAGE: javascript
CODE:
const delaunay = d3.Delaunay.from([[0, 0], [0, 100], [100, 0], [100, 100]]);
const voronoi = delaunay.voronoi([0, 0, 640, 480]);

----------------------------------------

TITLE: Creating Basic Area Generator
DESCRIPTION: Demonstrates how to create a basic area generator with x, y0, and y1 accessors for mapping data points to coordinates.

LANGUAGE: javascript
CODE:
const area = d3.area((d) => x(d.Date), y(0), (d) => y(d.Close));

----------------------------------------

TITLE: Basic Arc Generator Initialization
DESCRIPTION: Creates a new arc generator with default settings that can be used to generate SVG path data for circular or annular sectors.

LANGUAGE: javascript
CODE:
const arc = d3.arc();

----------------------------------------

TITLE: Selecting Elements with D3 in JavaScript
DESCRIPTION: Demonstrates various ways to select elements using D3's select and selectAll methods.

LANGUAGE: javascript
CODE:
const svg = d3.select("#chart");
const anchor = d3.select("a");
d3.select(document.body).style("background", "red");
d3.selectAll("p").on("click", (event) => d3.select(event.currentTarget).style("color", "red"));
const p = d3.selectAll("p");
d3.selectAll(document.links).style("color", "red");

----------------------------------------

TITLE: Chaining Transitions in D3.js
DESCRIPTION: This example demonstrates how to chain multiple transitions to create a sequence of color changes and removal of elements.

LANGUAGE: javascript
CODE:
d3.selectAll(".apple")
  .transition() // First fade to green.
    .style("fill", "green")
  .transition() // Then red.
    .style("fill", "red")
  .transition() // Wait one second. Then brown, and remove.
    .delay(1000)
    .style("fill", "brown")
    .remove();

----------------------------------------

TITLE: Defining Missing Data Handler
DESCRIPTION: Shows how to configure the area generator to handle missing or invalid data points.

LANGUAGE: javascript
CODE:
const area = d3.area().defined((d) => !isNaN(d.Close));

----------------------------------------

TITLE: Constructing a Treemap Layout with D3 Hierarchy
DESCRIPTION: Shows how to create a treemap layout using d3.treemap(), including sizing, padding, summing values, and sorting nodes.

LANGUAGE: javascript
CODE:
// Construct the treemap layout.
const treemap = d3.treemap();
treemap.size([width, height]);
treemap.padding(2);

// Sum and sort the data.
root.sum((d) => d.value);
root.sort((a, b) => b.height - a.height || b.value - a.value);

// Compute the treemap layout.
treemap(root);

// Retrieve all descendant nodes.
const nodes = root.descendants();

----------------------------------------

TITLE: Interpolating Fill Attribute with D3 Transition
DESCRIPTION: Examples of using attrTween() to interpolate the fill attribute between colors. Shows three approaches: interpolating between fixed colors, interpolating from current color, and using a custom rainbow interpolator.

LANGUAGE: javascript
CODE:
transition.attrTween("fill", () => d3.interpolateRgb("red", "blue"));

transition.attrTween("fill", function() {
  return d3.interpolateRgb(this.getAttribute("fill"), "blue");
});

transition.attrTween("fill", () => (t) => `hsl(${t * 360},100%,50%)`);

----------------------------------------

TITLE: Creating Force Simulation in D3
DESCRIPTION: Creates a new force simulation with specified nodes array. The simulation starts automatically and mutates the passed-in nodes with position and velocity data.

LANGUAGE: javascript
CODE:
const simulation = d3.forceSimulation(nodes);

----------------------------------------

TITLE: Filtering D3 Selections in JavaScript
DESCRIPTION: Demonstrates different ways to filter D3 selections using strings and functions.

LANGUAGE: javascript
CODE:
const even = d3.selectAll("tr").filter(":nth-child(even)");
const even = d3.selectAll("tr:nth-child(even)");
const even = d3.selectAll("tr").filter((d, i) => i & 1);
const even = d3.selectAll("tr").select(function(d, i) { return i & 1 ? this : null; });

----------------------------------------

TITLE: Setting Curve Type
DESCRIPTION: Demonstrates how to set a different curve interpolation type for the area generator.

LANGUAGE: javascript
CODE:
const area = d3.area().curve(d3.curveStep);

----------------------------------------

TITLE: Creating a Reusable Function with call() in D3
DESCRIPTION: Shows how to create a reusable function that sets multiple attributes on a selection using the call() method for method chaining.

LANGUAGE: javascript
CODE:
function name(selection, first, last) {
  selection
      .attr("first-name", first)
      .attr("last-name", last);
}

LANGUAGE: javascript
CODE:
d3.selectAll("div").call(name, "John", "Snow");

LANGUAGE: javascript
CODE:
name(d3.selectAll("div"), "John", "Snow");

----------------------------------------

TITLE: Applying Pack Layout to Hierarchy
DESCRIPTION: Lays out a hierarchical data structure, assigning x, y coordinates and radius to each node. Requires calling root.sum() before layout and optionally root.sort() for ordering.

LANGUAGE: javascript
CODE:
pack(root)

----------------------------------------

TITLE: Setting Curve Type for Line Generator in D3.js
DESCRIPTION: Demonstrates how to specify a custom curve type for the line generator.

LANGUAGE: javascript
CODE:
const line = d3.line().curve(d3.curveStep);

----------------------------------------

TITLE: Applying a Line Generator to SVG Path in D3.js
DESCRIPTION: This code shows how to use a previously defined line generator to compute the 'd' attribute of an SVG path element, binding data to the path.

LANGUAGE: javascript
CODE:
path.datum(data).attr("d", line);

----------------------------------------

TITLE: Implementing Drag Event Listeners in D3 JavaScript
DESCRIPTION: Shows how to implement drag event listeners for start, drag, and end events. This example raises the dragged element and updates its position.

LANGUAGE: JavaScript
CODE:
function started(event) {
  const circle = d3.select(this).classed("dragging", true);
  const dragged = (event, d) => circle.raise().attr("cx", d.x = event.x).attr("cy", d.y = event.y);
  const ended = () => circle.classed("dragging", false);
  event.on("drag", dragged).on("end", ended);
}

----------------------------------------

TITLE: Summing Node Values in D3 Hierarchy
DESCRIPTION: Demonstrates how to use the sum() method to calculate and assign values to nodes based on their descendants.

LANGUAGE: javascript
CODE:
root.sum((d) => d.value ? 1 : 0);

----------------------------------------

TITLE: Computing Projected Planar Bounding Box in D3
DESCRIPTION: Illustrates how to use the bounds method of a path generator to compute the projected planar bounding box of a GeoJSON object.

LANGUAGE: javascript
CODE:
path.bounds(california) // [[18.48513821663947, 159.95146883594333], [162.7651668852596, 407.09641570706725]]

----------------------------------------

TITLE: Computing Basic Statistics with D3 Count
DESCRIPTION: Demonstrates using d3.count() to count valid numeric values in a dataset while ignoring null, NaN and undefined values.

LANGUAGE: javascript
CODE:
d3.count(penguins, (d) => d.body_mass_g) // 342

----------------------------------------

TITLE: Updating a D3.js Axis with Transition
DESCRIPTION: This code shows how to update an existing D3.js axis with a smooth transition. It applies a duration to the transition and calls the axis function again to update the axis based on new data.

LANGUAGE: javascript
CODE:
gx.transition()
    .duration(750)
    .call(d3.axisBottom(x));

----------------------------------------

TITLE: Applying Treemap Layout to Hierarchy in D3
DESCRIPTION: Lays out the specified root hierarchy, assigning position properties to each node. This method requires the hierarchy to have values assigned using root.sum() beforehand.

LANGUAGE: javascript
CODE:
*treemap*(*root*)