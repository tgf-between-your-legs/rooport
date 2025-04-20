// D3.js Scale Snippets (v7)
import { scaleLinear, scaleBand, scaleTime, scaleOrdinal, schemeCategory10 } from 'd3-scale';
import { extent, max } from 'd3-array';

// --- Linear Scale ---
// Maps a continuous numeric domain to a continuous range (e.g., data values to pixel positions)
const data = [10, 20, 5, 50, 35];
const width = 500;
const height = 300; // Assuming height is relevant for y-scale

const xScaleLinear = scaleLinear()
  // .domain([0, d3.max(data)]) // Domain from 0 to max value
  .domain(extent(data)) // Domain from min to max value
  .range([0, width]) // Output range (e.g., pixel width)
  .nice(); // Adjust domain to nice round values

// Usage:
// const xPosition = xScaleLinear(dataValue);

// --- Band Scale ---
// Maps a discrete domain (categories) to a continuous range, calculating bands for bars/columns
const categories = ["A", "B", "C", "D"];
const xScaleBand = scaleBand()
  .domain(categories)
  .range([0, width])
  .padding(0.1); // Adjust padding between bands (0 to 1)

// Usage:
// const xPosition = xScaleBand("A");
// const bandwidth = xScaleBand.bandwidth();

// --- Time Scale ---
// Maps Date objects to a continuous range
const timeData = [new Date(2023, 0, 1), new Date(2023, 5, 15), new Date(2023, 11, 31)];
const xScaleTime = scaleTime()
  .domain(extent(timeData)) // Domain from earliest to latest date
  .range([0, width])
  .nice();

// Usage:
// const xPosition = xScaleTime(dateObject);

// --- Ordinal Scale ---
// Maps a discrete domain (categories) to a discrete range (e.g., colors)
const categoryColors = ["A", "B", "C"];
const colorScale = scaleOrdinal()
  .domain(categoryColors)
  // .range(["red", "green", "blue"]); // Explicit range
  .range(schemeCategory10); // Use a built-in color scheme

// Usage:
// const color = colorScale("B");

// --- Log Scale ---
// Maps a continuous, positive numeric domain to a continuous range, useful for wide value ranges
const logData = [1, 10, 100, 1000, 10000];
const xScaleLog = d3.scaleLog() // Assuming d3 is imported as *
    .domain(extent(logData))
    .range([0, width])
    .base(10) // Default base is 10
    .nice();

// --- Common Methods ---
// scale.domain([min, max]) - Sets the input domain
// scale.range([start, end]) - Sets the output range
// scale(value) - Maps a domain value to a range value
// scale.invert(value) - Maps a range value back to a domain value (for continuous scales)
// scale.bandwidth() - (For scaleBand) Gets the width of each band
// scale.padding() - (For scaleBand) Sets padding between bands
// scale.nice() - Extends the domain to nice round numbers