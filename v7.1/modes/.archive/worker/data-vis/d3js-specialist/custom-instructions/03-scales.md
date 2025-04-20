# D3.js: Scales

Mapping abstract data values to visual variables (position, length, color) using D3 scales.

## Core Concept: Scales

Scales are fundamental in D3.js for translating data values (the **domain**) into visual representations (the **range**, e.g., pixel positions, colors, sizes). They provide a mapping between your abstract data and the concrete visual properties needed for a chart.

**Key Steps:**

1.  **Choose Scale Type:** Select the appropriate scale based on the type of data (quantitative, ordinal, time) and the desired visual output.
2.  **Define Domain:** Specify the extent of your input data values (e.g., `[0, 100]`, `['A', 'B', 'C']`, `[minDate, maxDate]`).
3.  **Define Range:** Specify the extent of the desired output visual values (e.g., `[0, width]`, `[height, 0]`, `['red', 'blue']`).
4.  **Use the Scale:** Pass data values to the scale function to get the corresponding visual value.

**Importing:** `import { scaleLinear, scaleBand, ... } from 'd3-scale';`

## Common Scale Types

**1. Continuous Scales (Quantitative Data -> Quantitative Output):**

*   **`d3.scaleLinear()`:**
    *   **Purpose:** Maps a continuous numeric domain to a continuous numeric range using linear interpolation. The most common scale for quantitative axes (X or Y).
    *   **Methods:** `.domain([min, max])`, `.range([start, end])`, `.nice()` (extends domain to round values), `.clamp(true)` (clamps output to range).
    *   **Example:** Map values 0-100 to pixel positions 0-500.
        ```javascript
        const xScale = d3.scaleLinear()
          .domain([0, 100]) // Input data range
          .range([0, 500]); // Output pixel range

        xScale(0);   // -> 0
        xScale(50);  // -> 250
        xScale(100); // -> 500
        ```
*   **`d3.scaleLog()`:** Similar to linear, but uses a logarithmic transform. Useful when data spans several orders of magnitude. Domain values must be positive.
*   **`d3.scalePow().exponent(e)`:** Uses an exponential transform. `.exponent(0.5)` is `scaleSqrt()`.
*   **`d3.scaleTime()`:**
    *   **Purpose:** Maps continuous date/time objects to a continuous range. Use for time-based axes.
    *   **Methods:** `.domain([startDate, endDate])`, `.range([start, end])`, `.nice()` (extends domain to nice time boundaries).
    *   **Example:** Map dates over a year to an X-axis width.
        ```javascript
        const timeScale = d3.scaleTime()
          .domain([new Date(2023, 0, 1), new Date(2023, 11, 31)])
          .range([0, width]);

        timeScale(new Date(2023, 5, 15)); // -> Pixel position for mid-June
        ```
*   **`d3.scaleSequential(interpolator)` / `d3.scaleDiverging(interpolator)`:** Used for mapping continuous data to colors using D3 interpolators (e.g., `d3.interpolateViridis`, `d3.interpolateRdBu`).

**2. Ordinal Scales (Discrete Data -> Discrete/Continuous Output):**

*   **`d3.scaleBand()`:**
    *   **Purpose:** Maps a discrete domain (e.g., category names) to discrete, evenly spaced bands within a continuous range. Ideal for bar charts.
    *   **Methods:** `.domain(['A', 'B', 'C'])`, `.range([start, end])`, `.padding(p)` (space between bands, 0 to 1), `.paddingInner()`, `.paddingOuter()`, `.bandwidth()` (returns the width of each band).
    *   **Example:** Position bars for categories A, B, C along an X-axis.
        ```javascript
        const xBandScale = d3.scaleBand()
          .domain(['Apple', 'Banana', 'Cherry'])
          .range([0, width])
          .padding(0.1); // 10% padding between bars

        xBandScale('Apple');  // -> Starting pixel position of the 'Apple' band
        xBandScale('Banana'); // -> Starting pixel position of the 'Banana' band
        xBandScale.bandwidth(); // -> Width of each band in pixels
        ```
*   **`d3.scalePoint()`:** Similar to `scaleBand`, but maps to distinct points within the range (no bandwidth). Useful for scatter plots with categorical axes or line charts. `.padding()` affects spacing at the ends.
*   **`d3.scaleOrdinal()`:**
    *   **Purpose:** Maps a discrete domain to a discrete range (often colors or shapes). If the domain is larger than the range, the range values repeat.
    *   **Methods:** `.domain([...])`, `.range([...])`.
    *   **Example:** Assign colors to categories.
        ```javascript
        const colorScale = d3.scaleOrdinal()
          .domain(['Type A', 'Type B', 'Type C'])
          .range(['red', 'green', 'blue']); // Or use d3.schemeCategory10, etc.

        colorScale('Type A'); // -> 'red'
        colorScale('Type B'); // -> 'green'
        colorScale('Type D'); // -> 'red' (wraps around if domain > range)
        ```

## Using Scales in Visualizations

Scales are typically defined once based on your data and chart dimensions, then used repeatedly within data binding functions to set attributes like position (`x`, `y`), size (`width`, `height`, `r`), and color (`fill`, `stroke`).

```javascript
// Inside a D3 data join...
.attr('x', d => xBandScale(d.category)) // Use band scale for x position
.attr('y', d => yLinearScale(d.value)) // Use linear scale for y position
.attr('width', xBandScale.bandwidth()) // Use bandwidth for bar width
.attr('height', d => height - yLinearScale(d.value)) // Calculate height based on linear scale
.attr('fill', d => colorOrdinalScale(d.group)); // Use ordinal scale for color
```

Scales are essential for mapping your data domain to the visual range of your chart, forming the bridge between abstract numbers/categories and concrete visual representations. Choose the scale type that matches your data and the visual encoding you intend to use.

*(Refer to the official D3.js documentation for d3-scale.)*