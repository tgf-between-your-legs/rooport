# D3.js: SVG vs. Canvas Rendering

Choosing the appropriate rendering technology (SVG or Canvas) for D3 visualizations.

## Core Concept

D3.js itself doesn't render graphics directly; it primarily manipulates the DOM. The two main technologies used with D3 for rendering visualizations in the browser are SVG (Scalable Vector Graphics) and HTML Canvas.

**1. SVG (Scalable Vector Graphics):**

*   **Mechanism:** An XML-based markup language for describing two-dimensional vector graphics. D3 creates and manipulates SVG elements (`<svg>`, `<circle>`, `<rect>`, `<path>`, `<g>`, `<text>`, etc.) within the DOM.
*   **Pros:**
    *   **DOM Integration:** Each visual element is a distinct DOM node, making it easy to inspect, style with CSS, and attach individual event listeners (hover, click) using D3's `.on()`.
    *   **Resolution Independent:** Vector graphics scale without losing quality (good for zooming, printing, high-resolution displays).
    *   **Accessibility:** SVG elements are part of the DOM and can be made accessible using standard HTML/ARIA techniques (`<title>`, `<desc>`, `aria-label`, `role`). (See `10-accessibility.md`)
    *   **Simpler for Standard Charts:** Generally easier to work with for common chart types with a moderate number of elements.
*   **Cons:**
    *   **Performance with Many Elements:** Performance degrades significantly as the number of DOM elements increases (thousands to tens of thousands). Each element adds overhead to the DOM tree and browser rendering. (See `11-performance.md`)
    *   **Pixel Manipulation:** Not suitable for direct pixel-level manipulation.

**2. HTML Canvas (`<canvas>`):**

*   **Mechanism:** A single DOM element (`<canvas>`) that provides a low-level, pixel-based drawing surface via JavaScript APIs (typically the 2D rendering context, `getContext('2d')`). D3 is used to calculate positions, sizes, and colors, but the actual drawing commands (`ctx.fillRect()`, `ctx.beginPath()`, `ctx.arc()`, `ctx.stroke()`, etc.) are executed using the Canvas API.
*   **Pros:**
    *   **Performance with Many Elements:** Handles a very large number of graphical elements (tens of thousands to millions) much more efficiently than SVG because it's a single DOM element with immediate-mode rendering (drawing pixels directly).
    *   **Pixel Manipulation:** Allows direct reading and writing of pixel data.
*   **Cons:**
    *   **No DOM Elements:** Individual shapes (circles, bars) are just pixels on the canvas; they don't exist as distinct DOM nodes.
    *   **Interaction Complexity:** Handling interactions like hover or click requires manually tracking element positions and implementing hit detection logic (e.g., checking if mouse coordinates fall within a shape's bounds). D3 libraries like `d3-quadtree` can help, but it's more complex than SVG's `.on()`.
    *   **Styling:** Styling is done via Canvas API properties (`ctx.fillStyle`, `ctx.strokeStyle`, `ctx.lineWidth`) set before drawing commands, not CSS.
    *   **Accessibility:** Less accessible out-of-the-box. Requires alternative representations (like a parallel DOM structure or fallback content within the `<canvas>` tags) and ARIA attributes on the `<canvas>` element itself or related controls.
    *   **Resolution Dependent:** Pixel-based, can appear blurry on high-resolution displays unless scaled appropriately (requires drawing at higher resolution and scaling down the canvas element via CSS).

## Choosing Between SVG and Canvas

*   **Use SVG when:**
    *   You have a small to moderate number of elements (up to a few thousand).
    *   You need easy interaction with individual graphical elements (tooltips, clicks, drag).
    *   You need to style elements easily using CSS.
    *   Accessibility is a primary concern and DOM-based semantics are beneficial.
    *   Resolution independence and sharp scaling are critical.
    *   Creating standard charts like bar, line, pie, scatter (with moderate points).

*   **Use Canvas when:**
    *   You need to render a very large number of elements (tens of thousands or more), e.g., dense scatter plots, complex network graphs, particle systems.
    *   Pixel-level manipulation is required.
    *   Maximum rendering performance is the absolute priority over ease of interaction or accessibility implementation.
    *   You are comfortable implementing hit detection and interaction logic manually.

## Hybrid Approach

It's also possible to use both SVG and Canvas together. For example:

*   Render the main data points (e.g., thousands of scatter plot dots) on a Canvas layer for performance.
*   Overlay an SVG layer on top for rendering axes, labels, tooltips, or interactive elements that need DOM events.

## D3 Integration

D3's core modules (scales, shapes, layouts, data binding) work independently of the rendering target.

*   **SVG:** Use `d3.select`/`selectAll` to create/update SVG elements (`circle`, `rect`, `path`) and set attributes (`cx`, `cy`, `d`, `fill`) based on scales and generators.
*   **Canvas:** Use D3 scales/layouts to calculate coordinates and sizes. Then, use the Canvas 2D context API (`ctx.beginPath()`, `ctx.arc()`, `ctx.fill()`, `ctx.stroke()`, etc.) to draw the shapes based on those calculations, often within a loop over your data or within a D3 `.each()` call.

```javascript
// --- Canvas Example Snippet ---
import * as d3 from 'd3';

const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');
const data = [ {x: 10, y: 20, r: 5}, {x: 50, y: 60, r: 8} /* ... */ ];

// Assume xScale, yScale are defined D3 scales

ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear canvas
ctx.fillStyle = 'steelblue';

data.forEach(d => {
  ctx.beginPath();
  ctx.arc(xScale(d.x), yScale(d.y), d.r, 0, 2 * Math.PI); // Use scales for position
  ctx.fill();
});
// --- End Canvas Snippet ---
```

The choice between SVG and Canvas depends heavily on the specific requirements of your visualization, particularly the number of elements and the need for interaction and accessibility. SVG is often the easier starting point, while Canvas offers better performance for large-scale datasets.

*(Refer to D3 documentation and examples demonstrating both SVG and Canvas rendering.)*