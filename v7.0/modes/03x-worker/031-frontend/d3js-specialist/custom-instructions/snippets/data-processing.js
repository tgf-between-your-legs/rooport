// D3.js Data Processing Snippets (v7)
// Using d3-array module primarily
import { group, rollup, sum, mean, max, extent, descending } from 'd3-array';
import { csvParse, autoType } from 'd3-dsv'; // For parsing CSV data

// --- Sample Data ---
const data = [
  { category: 'A', value: 10, region: 'North' },
  { category: 'B', value: 25, region: 'South' },
  { category: 'A', value: 15, region: 'North' },
  { category: 'C', value: 30, region: 'East' },
  { category: 'B', value: 20, region: 'North' },
  { category: 'C', value: 35, region: 'West' },
  { category: 'A', value: 12, region: 'South' },
];

// --- Grouping Data ---
// Groups data into a Map based on one or more keys
const groupedByCategory = group(data, d => d.category);
// groupedByCategory is a Map: Map(3) { 'A' => [...], 'B' => [...], 'C' => [...] }

const groupedByRegionAndCategory = group(data, d => d.region, d => d.category);
// groupedByRegionAndCategory is a nested Map: Map(4) { 'North' => Map(3), 'South' => Map(2), ... }

// --- Rolling Up Data (Aggregation) ---
// Groups data and applies a reduction function to each group
const sumByCategory = rollup(data, v => sum(v, d => d.value), d => d.category);
// sumByCategory is a Map: Map(3) { 'A' => 37, 'B' => 45, 'C' => 65 }

const averageByRegion = rollup(data, v => mean(v, d => d.value), d => d.region);
// averageByRegion is a Map: Map(4) { 'North' => 18.33, 'South' => 18.5, ... }

// --- Basic Statistics ---
const maxValue = max(data, d => d.value); // 35
const valueExtent = extent(data, d => d.value); // [10, 35]
const averageValue = mean(data, d => d.value); // ~21.71

// --- Sorting ---
// Sorts the array in place
data.sort((a, b) => descending(a.value, b.value)); // Sort by value descending
// data is now sorted: [{ category: 'C', value: 35, ... }, { category: 'C', value: 30, ... }, ...]

data.sort((a, b) => a.category.localeCompare(b.category)); // Sort by category ascending (alphabetical)

// --- Parsing CSV/DSV Data ---
const csvString = `category,value,region
A,10,North
B,25,South
A,15,North`;

// Use csvParse with autoType to infer types (number, date)
const parsedData = csvParse(csvString, autoType);
// parsedData = [ { category: 'A', value: 10, region: 'North' }, ... ]

// --- Loading External Data (using Fetch API - D3 v7+ relies on native Fetch) ---
async function loadData() {
  try {
    const response = await fetch('path/to/your/data.csv');
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const csvText = await response.text();
    const loadedData = csvParse(csvText, autoType);
    console.log(loadedData);
    // ... use loadedData in your visualization ...
  } catch (error) {
    console.error('Error loading data:', error);
  }
}

// loadData(); // Call the async function

// Note: For older D3 versions (v5 and below), use d3.csv(), d3.json() which return Promises directly.
// import { csv } from 'd3-fetch';
// csv('path/to/your/data.csv', autoType).then(loadedData => { ... });