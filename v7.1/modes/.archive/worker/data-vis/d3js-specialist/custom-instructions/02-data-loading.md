# D3.js: Data Loading

Fetching and parsing external data files (CSV, JSON, etc.) using D3 fetch modules.

## Core Concept: Fetching Data

D3 provides convenient functions in the `d3-fetch` module for loading data from external files or APIs. These functions return Promises that resolve with the parsed data.

**Key Features:**

*   **Promise-Based:** Integrates easily with modern JavaScript `async/await` syntax or `.then()` chains.
*   **Parsing Included:** Automatically parses common formats like CSV, TSV, JSON.
*   **Convenience:** Simplifies the process compared to using the standard `fetch` API directly and then parsing manually.

**Importing:** `import { csv, json, tsv, ... } from 'd3-fetch';` (or access via `d3.csv`, `d3.json` if using full `d3` import).

## Common Fetch Functions

*   **`d3.csv(url, [rowConversionFn], [init])`:**
    *   Fetches a comma-separated values (CSV) file from the specified `url`.
    *   Returns a Promise that resolves with an array of objects, where keys are determined by the header row. Values are strings by default.
    *   `rowConversionFn` (Optional): A function `(rawRow, index, columns) => convertedRow` called for each row *after* initial parsing. Use this to convert string values to numbers, dates, etc.
    *   `init` (Optional): An options object passed to the underlying `fetch` call (e.g., for setting headers).

*   **`d3.tsv(url, [rowConversionFn], [init])`:**
    *   Similar to `d3.csv`, but parses tab-separated values.

*   **`d3.json(url, [init])`:**
    *   Fetches a JSON file from the `url`.
    *   Returns a Promise that resolves with the parsed JSON object or array.

*   **`d3.text(url, [init])`:**
    *   Fetches a plain text file. Returns a Promise resolving with the text content as a string.

*   **`d3.blob(url, [init])`:**
    *   Fetches a file as a Blob object.

*   **`d3.buffer(url, [init])`:**
    *   Fetches a file as an ArrayBuffer.

## Examples

**1. Loading CSV Data:**

```javascript
import * as d3 from 'd3'; // Includes d3-fetch

const dataUrl = '/data/my-data.csv'; // Use workspace-relative path

async function loadAndProcessCsv() {
  try {
    // Define a row conversion function to parse strings into numbers/dates
    const rowConverter = (d) => {
      return {
        category: d.Category, // Keep category as string
        value: +d.Value, // Convert 'Value' column to number using +
        date: new Date(d.Timestamp) // Convert 'Timestamp' column to Date object
      };
    };

    const data = await d3.csv(dataUrl, rowConverter);
    console.log('Parsed CSV Data:', data);
    // Now use the 'data' array (with correct types) in your D3 visualization
    // createChart(data);

  } catch (error) {
    console.error('Error loading or parsing CSV data:', error);
  }
}

loadAndProcessCsv();

// Alternative using .then()
// d3.csv(dataUrl, rowConverter)
//   .then(data => {
//     console.log('Parsed CSV Data:', data);
//     // createChart(data);
//   })
//   .catch(error => {
//     console.error('Error loading or parsing CSV data:', error);
//   });
```

**2. Loading JSON Data:**

```javascript
import * as d3 from 'd3';

const jsonUrl = '/api/hierarchy.json'; // Use workspace-relative path

async function loadJson() {
  try {
    const data = await d3.json(jsonUrl);
    console.log('Loaded JSON Data:', data);
    // Use the JSON data (e.g., pass to d3.hierarchy)
    // createHierarchyChart(data);
  } catch (error) {
    console.error('Error loading JSON data:', error);
  }
}

loadJson();
```

**3. Loading Multiple Files (`Promise.all`):**

Use `Promise.all` to load multiple data sources concurrently before proceeding.

```javascript
import * as d3 from 'd3';

async function loadMultiple() {
  try {
    const [populationData, geoData] = await Promise.all([
      d3.csv('/data/population.csv', d => ({ state: d.State, pop: +d.Population })), // Use workspace-relative path
      d3.json('/data/us-states.json') // Example GeoJSON, use workspace-relative path
    ]);

    console.log('Population:', populationData);
    console.log('GeoJSON:', geoData);
    // Create a map visualization using both datasets
    // createChoroplethMap(populationData, geoData);

  } catch (error) {
    console.error('Error loading multiple files:', error);
  }
}

loadMultiple();
```

## Row Conversion Function (`rowConverter`)

This function is crucial when loading CSV/TSV data because values are initially parsed as strings.

*   **Input:** Receives the raw row object (keys from header, values as strings), the row index, and an array of column names.
*   **Output:** Should return a new object with the desired structure and data types (numbers, Dates, Booleans).
*   **Type Conversion:** Use `+` prefix or `parseInt()`/`parseFloat()` for numbers, `new Date()` for dates.

The `d3-fetch` module simplifies loading and parsing common data formats, integrating smoothly with D3's data-driven approach. Remember to handle potential errors during the fetch/parse process.

*(Refer to the official D3.js documentation for d3-fetch.)*