// D3.js Axis Snippets (v7)
import { select } from 'd3-selection';
import { axisBottom, axisLeft, axisTop, axisRight } from 'd3-axis';
// Assuming you have scales defined (e.g., xScaleLinear, yScaleLinear from scales.js)

// --- Setup SVG Container ---
const margin = { top: 20, right: 30, bottom: 40, left: 50 };
const width = 600 - margin.left - margin.right;
const height = 400 - margin.top - margin.bottom;

const svg = select('#chart-container') // Select the container div
  .append('svg')
    .attr('width', width + margin.left + margin.right)
    .attr('height', height + margin.top + margin.bottom)
  .append('g')
    .attr('transform', `translate(${margin.left},${margin.top})`);

// --- Bottom Axis (X-axis) ---
// Create the axis generator
const xAxisGenerator = axisBottom(xScaleLinear) // Pass the corresponding scale
  .ticks(5) // Suggest number of ticks (D3 may adjust)
  .tickSizeOuter(0); // Hide outer ticks if desired
  // .tickFormat(d3.format(".1f")); // Optional: Format tick labels

// Append a 'g' element for the axis and call the generator
const xAxisGroup = svg.append('g')
  .attr('class', 'x-axis') // Add class for styling
  .attr('transform', `translate(0, ${height})`) // Position at the bottom
  .call(xAxisGenerator);

// Optional: Style axis elements (lines, text) using CSS or D3 .attr/.style
xAxisGroup.selectAll('line')
  .attr('stroke', '#ccc');

xAxisGroup.selectAll('text')
  .attr('fill', '#555')
  .attr('font-size', '10px');

// Optional: Add Axis Label
svg.append('text')
    .attr('class', 'x-axis-label')
    .attr('text-anchor', 'middle')
    .attr('x', width / 2)
    .attr('y', height + margin.bottom - 5) // Adjust position as needed
    .text('X Axis Label');


// --- Left Axis (Y-axis) ---
// Create the axis generator
const yAxisGenerator = axisLeft(yScaleLinear) // Pass the corresponding scale
  .ticks(height / 40) // Adjust tick count based on height
  // .tickFormat(d => `${d}%`); // Optional: Format tick labels

// Append a 'g' element for the axis and call the generator
const yAxisGroup = svg.append('g')
  .attr('class', 'y-axis')
  .call(yAxisGenerator);

// Optional: Remove domain line
// yAxisGroup.select('.domain').remove();

// Optional: Add grid lines (often done with y-axis)
yAxisGroup.selectAll('.tick line')
    .clone() // Clone the tick lines
    .attr('x2', width) // Extend to the right edge
    .attr('stroke-opacity', 0.1); // Make them faint

// Optional: Add Axis Label
svg.append('text')
    .attr('class', 'y-axis-label')
    .attr('text-anchor', 'middle')
    .attr('transform', 'rotate(-90)')
    .attr('x', -height / 2)
    .attr('y', -margin.left + 15) // Adjust position as needed
    .text('Y Axis Label');


// --- Other Axes ---
// axisTop(scale)
// axisRight(scale)
// Use similar .append('g').call(axisGenerator) pattern, adjusting transform attribute.

// --- Updating Axes ---
// If the scale's domain changes, update the axis by calling the generator again with a transition:
// xAxisGroup.transition().duration(500).call(xAxisGenerator);
// yAxisGroup.transition().duration(500).call(yAxisGenerator);