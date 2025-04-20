# D3.js: Core Concepts (Selections, Data Binding)

Understanding D3's fundamental concepts for manipulating the DOM based on data.

## Core Concept: Selections & Data Binding

D3.js (Data-Driven Documents) allows you to bind arbitrary data to the Document Object Model (DOM), and then apply data-driven transformations to the document. Its core strength lies in efficiently manipulating DOM elements (often SVG or Canvas) based on data.

**1. Selections (`d3.select`, `d3.selectAll`):**

*   **Purpose:** Select existing DOM elements using CSS selectors. Similar to `querySelector` and `querySelectorAll`, but returns a D3 "selection" object.
*   **`d3.select(selector)`:** Selects the *first* matching element.
*   **`d3.selectAll(selector)`:** Selects *all* matching elements.
*   **Selection Methods:** D3 selections provide methods to modify the selected elements:
    *   `.attr(name, value)`: Set an attribute (e.g., `fill`, `cx`, `width`). Value can be a constant or a function `(d, i, nodes) => value`.
    *   `.style(name, value)`: Set a CSS style property. Value can be constant or function.
    *   `.text(value)`: Set the text content. Value can be constant or function.
    *   `.html(value)`: Set the inner HTML. Use with caution.
    *   `.append(tagName)`: Append a new element inside each selected element.
    *   `.remove()`: Remove the selected elements.
    *   `.on(eventName, listener)`: Attach an event listener.
    *   `.each(function)`: Call a function for each selected element.

```javascript
import * as d3 from 'd3'; // Import necessary D3 modules or the whole library

// Select the body and change background
d3.select('body').style('background-color', 'lightblue');

// Select all paragraphs and change color
d3.selectAll('p').style('color', 'purple');

// Select an SVG element and append a circle
const svg = d3.select('#my-svg');
svg.append('circle')
  .attr('cx', 50)
  .attr('cy', 50)
  .attr('r', 20)
  .attr('fill', 'red');
```

**2. Data Binding (`.data()`, `.join()`):**

*   **Purpose:** Bind an array of data to a selection of DOM elements. D3 determines which elements need to be created, updated, or removed to match the data.
*   **`.data(dataArray, [keyFunction])`:** Binds the `dataArray` to the selected elements.
    *   `keyFunction` (Optional): A function `(d, i) => key` that returns a unique key for each data point `d`. This helps D3 track elements correctly when data changes, enabling object constancy and smoother transitions. Crucial for dynamic data.
*   **`.join(enterFn, [updateFn], [exitFn])` (Modern D3 v6+ - Recommended):** The preferred method for handling the enter, update, and exit selections after binding data.
    *   `enterFn`: A function called for each data point that doesn't have a corresponding DOM element. Typically appends the new element (`selection => selection.append('tag')`).
    *   `updateFn` (Optional): A function called for elements that already exist and correspond to data points. Used to update attributes/styles based on the new data. Defaults to returning the existing selection.
    *   `exitFn` (Optional): A function called for existing elements that no longer have corresponding data points. Typically removes the element (`selection => selection.remove()`). Defaults to removing elements.

```javascript
import * as d3 from 'd3';

const myData = [10, 20, 30, 40, 50];
const svg = d3.select('#chart-svg');

// Bind data to circle elements (create/update/remove as needed)
svg.selectAll('circle') // Select potential circles
  .data(myData, d => d) // Bind data, using data value as key
  .join(
    // Enter: Create new circles for new data points
    enter => enter.append('circle')
      .attr('cy', 50)
      .attr('r', 5)
      .attr('fill', 'blue')
      .attr('cx', (d, i) => (i + 1) * 60), // Initial position for entering elements

    // Update: Update existing circles (optional, could merge with enter)
    // update => update
    //   .attr('fill', 'lightblue'), // Example: Change color on update

    // Exit: Remove circles that no longer have data
    exit => exit.remove()
  )
  // Attributes applied to BOTH entering and updating elements AFTER join
  .attr('cx', (d, i) => (i + 1) * 60) // Ensure position is set/updated correctly
  .attr('r', d => d / 2); // Update radius based on data
```

**Enter/Update/Exit Pattern (Classic D3 < v6):**

*   Before `.join()`, data binding returned three selections:
    *   `.enter()`: Placeholder selection for data points needing new elements. Use `.append()` here.
    *   `.exit()`: Selection for elements to be removed. Use `.remove()` here.
    *   The *update* selection (the original selection after `.data()`): Elements that existed before and still have data.
*   Required manual merging of enter and update selections for common attribute/style updates. `.join()` simplifies this significantly.

```javascript
// Classic Enter/Update/Exit (Less common now)
// const circles = svg.selectAll('circle').data(myData, d => d);

// // Exit
// circles.exit().remove();

// // Enter + Update
// circles.enter().append('circle')
//     .attr('cy', 50)
//     .attr('r', 5)
//     .attr('fill', 'blue')
//   .merge(circles) // Merge enter and update selections
//     .attr('cx', (d, i) => (i + 1) * 60)
//     .attr('r', d => d / 2);
```

**Data Function Context (`d`, `i`, `nodes`):**

When setting attributes or styles using functions, D3 provides arguments:

*   `d`: The data point bound to the current element.
*   `i`: The index of the current element within the selection.
*   `nodes`: The array of all DOM nodes in the current selection group. `this` also refers to the current DOM node.

Selections and the data join (`.data().join()`) are the heart of D3, enabling declarative updates to the DOM based on your data.

*(Refer to the official D3.js documentation on Selections and Joining Data.)*