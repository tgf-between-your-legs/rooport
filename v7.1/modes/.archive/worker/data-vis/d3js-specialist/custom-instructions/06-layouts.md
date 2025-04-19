# D3.js: Layouts

Using D3 layout generators to calculate positions and structures for complex visualizations like hierarchies and networks.

## Core Concept: Layout Generators

D3 layouts take your raw data (often hierarchical or network-based) and compute additional properties needed for visualization, such as node positions (`x`, `y`), link coordinates, or arc angles. They don't draw anything themselves but transform your data into a structure that's easier to visualize using scales and shape generators.

**Key Steps:**

1.  **Prepare Data:** Ensure your data is in the format expected by the layout (e.g., a hierarchical structure for `d3.hierarchy`, an array of values for `d3.pie`).
2.  **Create Layout Generator:** Instantiate the layout function (e.g., `d3.hierarchy()`, `d3.pie()`, `d3.forceSimulation()`).
3.  **Configure Layout:** Set parameters specific to the layout (e.g., `.size()` for tree/pack, `.value()` for pie, `.nodes()` and `.force()` for force simulation).
4.  **Apply Layout:** Call the layout function, passing in your prepared data. This returns a new data structure with calculated layout properties.
5.  **Bind Transformed Data:** Use the transformed data (output from the layout function) in your D3 data binding (`.data().join()`).
6.  **Render Shapes:** Use scales and shape generators, referencing the properties added by the layout (e.g., `d.x`, `d.y`, `d.startAngle`, `link.source.x`). (See `05-shape-generators.md`)

**Importing:** `import { hierarchy, tree, pack, pie, forceSimulation, ... } from 'd3-hierarchy';` (or `d3-shape`, `d3-force` depending on the layout).

## Common Layout Generators

**1. `d3.hierarchy()` &amp; Tree Layouts (`d3.tree`, `d3.cluster`, `d3.treemap`, `d3.pack`):**

*   **Purpose:** Visualize hierarchical data (e.g., file systems, organizational charts).
*   **`d3.hierarchy(rootData, [childrenAccessor])`:** Creates a root node structure from your hierarchical data (needs a root object with a `children` array property, or provide an accessor function). Adds properties like `depth`, `height`, `parent`, `children`, `value` (if using `.sum()`).
*   **Tree Layouts:** Take the output of `d3.hierarchy()` as input.
    *   `d3.tree().size([width, height])`: Tidy tree layout (node-link). Calculates `node.x`, `node.y`.
    *   `d3.cluster().size([width, height])`: Similar to tree, but leaf nodes are at the same depth.
    *   `d3.treemap().size([width, height]).padding(p)`: Space-filling rectangular layout. Calculates `node.x0`, `node.y0`, `node.x1`, `node.y1`. Requires `.sum()` on hierarchy first.
    *   `d3.pack().size([width, height]).padding(p)`: Space-filling circular layout (circle packing). Calculates `node.x`, `node.y`, `node.r`. Requires `.sum()` on hierarchy first.
*   **Rendering:** Use `hierarchy.descendants()` to get an array of all nodes, `hierarchy.links()` to get link objects (with `source` and `target` nodes containing x/y coordinates) for node-link diagrams.

```javascript
import * as d3 from 'd3';

const hierarchicalData = { /* ... your nested data object ... */ };
const root = d3.hierarchy(hierarchicalData); // Create hierarchy structure
root.sum(d => d.value); // Optional: Calculate sum based on node values

const treeLayout = d3.tree().size([width, height]); // Create tree layout generator (assume width/height defined)
treeLayout(root); // Apply layout - adds x, y to each node in root

// Get nodes and links
const nodes = root.descendants();
const links = root.links();

// Render links (example using d3.linkHorizontal)
const linkGenerator = d3.linkHorizontal().x(d => d.y).y(d => d.x); // Note x/y swap for horizontal tree
svg.selectAll('.link') // Assume svg defined
  .data(links)
  .join('path')
    .attr('class', 'link')
    .attr('d', linkGenerator)
    .attr('fill', 'none')
    .attr('stroke', '#ccc');

// Render nodes
svg.selectAll('.node')
  .data(nodes)
  .join('circle')
    .attr('class', 'node')
    .attr('cx', d => d.y) // Note x/y swap
    .attr('cy', d => d.x)
    .attr('r', 4)
    .attr('fill', 'steelblue');
```

**2. `d3.pie()`:**

*   **Purpose:** Calculates start and end angles for pie or donut chart segments.
*   **Input Data:** An array of data values or objects.
*   **Configuration:**
    *   `.value(d => d.value)`: Accessor function to get the numeric value for each data point `d`.
    *   `.sort(null)`: Disable sorting by value (maintains original order).
    *   `.startAngle()`, `.endAngle()`, `.padAngle()`: Control overall angles and padding.
*   **Output:** Transforms the input array into an array of objects, each containing the original `data`, the `value`, `index`, `startAngle`, and `endAngle`.
*   **Rendering:** Use the output data with `d3.arc()` shape generator. (See `05-shape-generators.md`).

**3. `d3.forceSimulation()` (Network/Graph Layouts):**

*   **Purpose:** Positions nodes in a network graph based on simulated physical forces (links act like springs, nodes repel each other).
*   **Input Data:** An array of node objects. Links are added separately.
*   **Configuration:**
    *   `.nodes(nodeArray)`: Sets the nodes for the simulation.
    *   `.force(name, force)`: Adds forces:
        *   `d3.forceLink(linkArray).id(d => d.id)`: Link force (springs). Requires `linkArray` with `{source: id, target: id}` objects.
        *   `d3.forceManyBody()`: Node repulsion (charge). `.strength(-value)`.
        *   `d3.forceCenter(x, y)`: Attracts nodes towards a center point.
        *   `d3.forceCollide(radius)`: Prevents nodes from overlapping.
        *   `d3.forceX()`, `d3.forceY()`: Attract nodes towards an X or Y position.
    *   `.on('tick', tickedFn)`: Registers a callback function (`tickedFn`) that runs on each step (tick) of the simulation. Use this function to update the positions (`cx`/`cy` for circles, `x1`/`y1`/`x2`/`y2` for lines) of your SVG elements based on the calculated `node.x` and `node.y` properties.
*   **Rendering:** Create SVG elements for nodes (e.g., `<circle>`) and links (e.g., `<line>`). Update their positions within the `tick` handler.

```javascript
import * as d3 from 'd3';

const nodes = [ {id: 'A'}, {id: 'B'}, {id: 'C'} ];
const links = [ {source: 'A', target: 'B'}, {source: 'B', target: 'C'} ];

const simulation = d3.forceSimulation(nodes)
  .force('link', d3.forceLink(links).id(d => d.id).distance(50)) // Link force
  .force('charge', d3.forceManyBody().strength(-100)) // Repulsion
  .force('center', d3.forceCenter(width / 2, height / 2)); // Centering (assume width/height defined)

// Create SVG elements (lines for links, circles for nodes)
const link = svg.selectAll('.link').data(links).join('line').attr('class', 'link').attr('stroke', '#999');
const node = svg.selectAll('.node').data(nodes).join('circle').attr('class', 'node').attr('r', 5).attr('fill', 'steelblue').call(drag(simulation)); // Add drag behavior (see 07-transitions-interactions.md)

// Tick function to update positions
simulation.on('tick', () => {
  link
    .attr('x1', d => d.source.x)
    .attr('y1', d => d.source.y)
    .attr('x2', d => d.target.x)
    .attr('y2', d => d.target.y);
  node
    .attr('cx', d => d.x)
    .attr('cy', d => d.y);
});

// Drag helper function (see d3-drag documentation)
function drag(simulation) { /* ... implementation ... */ }
```

D3 layouts handle the complex geometric calculations for positioning elements in specialized visualizations, allowing you to focus on binding the resulting data and rendering the shapes.

*(Refer to the official D3.js documentation for d3-hierarchy, d3-shape (pie), and d3-force.)*