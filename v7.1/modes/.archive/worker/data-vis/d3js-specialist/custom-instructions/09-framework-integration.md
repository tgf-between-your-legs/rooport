# D3.js: Framework Integration (React, Vue, Svelte, Angular)

Patterns for using D3.js within modern JavaScript frameworks.

## Core Concept: Managing the DOM

The main challenge when integrating D3 with frameworks like React, Vue, Svelte, or Angular is managing DOM manipulation. These frameworks typically have their own virtual DOM or rendering mechanisms, while D3 directly manipulates the actual DOM (usually SVG elements). Letting both control the same DOM elements can lead to conflicts and unexpected behavior.

**General Strategies:**

1.  **D3 for Calculations, Framework for Rendering (Recommended for Simpler Cases):**
    *   Use D3 primarily for its powerful data processing, scales, and shape/layout *calculations*.
    *   Use the framework's templating syntax (JSX, Vue templates, Svelte syntax, Angular templates) to render the SVG elements (`<circle>`, `<rect>`, `<path>`).
    *   Pass the calculated values (positions, path data `d` strings, colors) from D3 scales/generators as props or state to the framework components.
    *   **Pros:** Leverages the framework's rendering optimizations and lifecycle management. Easier state management.
    *   **Cons:** Can be verbose for complex D3 layouts or interactions. Doesn't easily leverage D3's data join or transitions for DOM updates.

2.  **D3 Controls a Specific DOM Element (Container):**
    *   Let the framework render a container element (usually an `<svg>` or a `<g>`).
    *   Use the framework's ref mechanism (`useRef`, `ref`, `@ViewChild`) to get a reference to this container DOM node.
    *   In a lifecycle hook that runs *after* the container is mounted (`useEffect`, `onMounted`, `ngAfterViewInit`), use D3's `d3.select()` on the container ref to let D3 take control of everything *inside* that container.
    *   Use D3's data binding (`.data().join()`), transitions, and interaction modules within this container.
    *   **Pros:** Allows full use of D3's data binding, transitions, and interaction modules. Better for complex D3-centric visualizations.
    *   **Cons:** Requires careful lifecycle management (setup in mount hook, cleanup in unmount hook). D3 manipulations happen outside the framework's direct control. Need to handle updates carefully (e.g., re-running D3 code when props change).

## Examples (Strategy 2: D3 Controls Container)

**1. React (`useEffect`, `useRef`)**

```jsx
import React, { useRef, useEffect, useState } from 'react';
import * as d3 from 'd3';

function D3ChartReact({ data }) { // Receive data as prop
  const svgRef = useRef(null); // Ref for the SVG container

  useEffect(() => {
    if (!svgRef.current || !data) return; // Ensure ref and data exist

    const svg = d3.select(svgRef.current);
    const width = 300; // Example dimensions
    const height = 150;
    svg.attr('width', width).attr('height', height);

    // --- D3 Logic ---
    const xScale = d3.scaleBand().domain(data.map(d => d.label)).range([0, width]).padding(0.1);
    const yScale = d3.scaleLinear().domain([0, d3.max(data, d => d.value)]).range([height, 0]);

    svg.selectAll('rect')
      .data(data, d => d.label) // Key function important for updates
      .join(
        enter => enter.append('rect')
          .attr('x', d => xScale(d.label))
          .attr('y', height) // Start at bottom
          .attr('width', xScale.bandwidth())
          .attr('height', 0)
          .attr('fill', 'orange')
          .call(enter => enter.transition().duration(500) // Enter transition
            .attr('y', d => yScale(d.value))
            .attr('height', d => height - yScale(d.value))
          ),
        update => update
          .call(update => update.transition().duration(500) // Update transition
            .attr('x', d => xScale(d.label))
            .attr('width', xScale.bandwidth())
            .attr('y', d => yScale(d.value))
            .attr('height', d => height - yScale(d.value))
            .attr('fill', 'steelblue')
          ),
        exit => exit
          .call(exit => exit.transition().duration(500) // Exit transition
            .attr('y', height)
            .attr('height', 0)
            .remove()
          )
      );
    // --- End D3 Logic ---

    // No explicit cleanup needed for simple .join() if elements are removed on exit
    // For complex interactions or timers, return a cleanup function from useEffect

  }, [data]); // Re-run effect if data prop changes

  return (
    <div>
      <h3>D3 Chart (React)</h3>
      <svg ref={svgRef}></svg> {/* SVG container managed by D3 */}
    </div>
  );
}
export default D3ChartReact;
```

**2. Vue (`onMounted`, `onUnmounted`, `ref`, `watch`)**

```vue
<template>
  <div>
    <h3>D3 Chart (Vue)</h3>
    <svg ref="svgElement"></svg> <!-- Template ref -->
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch } from 'vue';
import * as d3 from 'd3';

const props = defineProps({
  data: Array // Receive data as prop
});

const svgElement = ref(null); // Template ref

let simulation = null; // Example: hold force simulation instance

function renderChart(chartData) {
  if (!svgElement.value || !chartData) return;

  const svg = d3.select(svgElement.value);
  // Clear previous rendering if needed (simple approach)
  svg.selectAll('*').remove();
  const width = 300; // Example dimensions
  const height = 150;
  svg.attr('width', width).attr('height', height);

  // --- D3 Logic (e.g., force simulation) ---
  const nodes = chartData.nodes;
  const links = chartData.links;

  simulation = d3.forceSimulation(nodes)
    .force('link', d3.forceLink(links).id(d => d.id).distance(30))
    .force('charge', d3.forceManyBody())
    .force('center', d3.forceCenter(width / 2, height / 2));

  const link = svg.append('g').attr('stroke', '#999').selectAll('line')
    .data(links).join('line');

  const node = svg.append('g').attr('stroke', '#fff').attr('stroke-width', 1.5)
    .selectAll('circle').data(nodes).join('circle').attr('r', 5).attr('fill', 'steelblue');

  simulation.on('tick', () => {
    link.attr('x1', d => d.source.x).attr('y1', d => d.source.y)
        .attr('x2', d => d.target.x).attr('y2', d => d.target.y);
    node.attr('cx', d => d.x).attr('cy', d => d.y);
  });
  // --- End D3 Logic ---
}

// Watch for changes in the data prop
watch(() => props.data, (newData) => {
  renderChart(newData);
}, { deep: true }); // Use deep watch if data structure might change internally

onMounted(() => {
  renderChart(props.data); // Initial render
});

onUnmounted(() => {
  // Cleanup: Stop simulation if running
  if (simulation) {
    simulation.stop();
  }
  console.log('D3 Simulation stopped');
});
</script>
```

**3. Angular (`AfterViewInit`, `OnDestroy`, `ElementRef`, `OnChanges`)**

```typescript
import { Component, Input, ViewChild, ElementRef, AfterViewInit, OnDestroy, OnChanges, SimpleChanges } from '@angular/core';
import * as d3 from 'd3';

@Component({
  selector: 'app-d3-angular-chart',
  standalone: true,
  template: `<svg #chartContainer></svg>`, // Template reference variable
})
export class D3AngularChartComponent implements AfterViewInit, OnDestroy, OnChanges {
  @Input() data: any[] = []; // Input data
  @ViewChild('chartContainer') private chartContainer!: ElementRef<SVGSVGElement>;
  private svg: any; // D3 selection type can be complex

  ngOnChanges(changes: SimpleChanges): void {
    // Re-render if data changes AFTER initial view init
    if (changes['data'] && this.svg) {
      this.createChart(changes['data'].currentValue);
    }
  }

  ngAfterViewInit(): void {
    // Render initially after view is ready
    this.createChart(this.data);
  }

  ngOnDestroy(): void {
    // Cleanup if needed (e.g., remove global listeners, stop simulations)
    d3.select(this.chartContainer.nativeElement).selectAll('*').remove(); // Simple cleanup
  }

  private createChart(chartData: any[]): void {
    if (!chartData || !this.chartContainer?.nativeElement) return;

    this.svg = d3.select(this.chartContainer.nativeElement);
    // Clear previous rendering
    this.svg.selectAll('*').remove();

    const width = 300; // Example dimensions
    const height = 150;
    this.svg.attr('width', width).attr('height', height);
    const g = this.svg.append('g'); // Group for margins if needed

    // --- D3 Logic ---
    // Example: Simple bars
    const xScale = d3.scaleBand().domain(chartData.map(d => d.label)).range([0, width]).padding(0.1);
    const yScale = d3.scaleLinear().domain([0, d3.max(chartData, d => d.value)]).range([height, 0]);

    g.selectAll('rect')
      .data(chartData, d => d.label)
      .join('rect')
        .attr('x', d => xScale(d.label))
        .attr('y', d => yScale(d.value))
        .attr('width', xScale.bandwidth())
        .attr('height', d => height - yScale(d.value))
        .attr('fill', 'teal');
    // --- End D3 Logic ---
  }
}
```

Choose the integration strategy based on the complexity of the visualization and the desired level of control between D3 and the framework. Using D3 within a container managed by the framework is often necessary for complex charts leveraging D3's transitions and interactions. Remember lifecycle hook cleanup!

*(Refer to framework-specific D3 integration guides and examples.)*