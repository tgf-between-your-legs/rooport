// D3.js Transition Snippets (v7)
import { select } from 'd3-selection';
import { transition } from 'd3-transition'; // Often implicitly used via selection.transition()
import { easeBounce } from 'd3-ease'; // Import specific easing functions

// --- Basic Transition ---
// Select elements, start a transition, then specify target attributes/styles

select('#myRect')
  .transition() // Start a transition
    .duration(1000) // Duration in milliseconds
    .delay(500) // Wait 500ms before starting
    .attr('fill', 'blue') // Target attribute value
    .attr('width', 200); // Another target attribute

// --- Transition with Easing ---
select('#myCircle')
  .transition()
    .duration(1500)
    .ease(easeBounce) // Apply an easing function
    .attr('cy', 250);

// --- Staggered Transitions ---
// Apply delays incrementally to multiple elements
selectAll('.bar')
  .transition()
    .duration(800)
    .delay((d, i) => i * 100) // Delay each bar by 100ms * its index
    .attr('height', d => yScale(d.value))
    .attr('y', d => yScale(d.value));

// --- Chained Transitions ---
// Start a new transition after the first one ends (less common now, often handled by .join or separate logic)
select('#myElement')
  .transition() // First transition
    .duration(1000)
    .attr('opacity', 1)
  .transition() // Second transition (starts after the first ends)
    .duration(500)
    .attr('fill', 'green');

// --- Transitions with .join() ---
// Apply transitions during enter, update, or exit phases
svg.selectAll('circle')
  .data(myData, d => d.id)
  .join(
    enter => enter.append('circle')
                  .attr('cx', d => xScale(d.x))
                  .attr('cy', height) // Start below the chart
                  .attr('r', 0)
                  .attr('fill', 'green')
                  .call(enter => enter.transition() // Enter transition
                                    .duration(1000)
                                    .delay((d, i) => i * 50)
                                    .attr('cy', d => yScale(d.y))
                                    .attr('r', 5)),
    update => update
                  .call(update => update.transition() // Update transition
                                    .duration(750)
                                    .attr('cx', d => xScale(d.x))
                                    .attr('cy', d => yScale(d.y))
                                    .attr('fill', 'blue')), // Change color on update
    exit => exit
                  .call(exit => exit.transition() // Exit transition
                                  .duration(500)
                                  .attr('r', 0)
                                  .attr('fill', 'red')
                                  .remove())
  );

// --- Attribute Tweening (for complex attributes like paths) ---
// Used when the attribute value itself needs interpolation, not just start/end values
// Example: Transitioning an arc path
import { arc } from 'd3-shape';
import { interpolate } from 'd3-interpolate';

const arcGenerator = arc().innerRadius(50).outerRadius(100);

function arcTween(newAngleData) {
  return function(d) { // 'd' is the bound data, often holds the current angle
    const interpolateAngle = interpolate(d.endAngle, newAngleData.endAngle); // Interpolate the angle
    return function(t) { // 't' is the transition progress (0 to 1)
      d.endAngle = interpolateAngle(t); // Update the data object during transition
      return arcGenerator(d); // Generate path data for the intermediate angle
    };
  };
}

select('.arcPath')
  .transition()
    .duration(1000)
    .attrTween('d', arcTween({ startAngle: 0, endAngle: Math.PI })); // Pass target data/angles

// --- Transition Events ---
// Listen for start/end/interrupt of transitions
const t = select('#myRect').transition().duration(1000);
t.on('start', () => console.log('Transition started!'));
t.on('end', () => console.log('Transition ended!'));
t.on('interrupt', () => console.log('Transition interrupted!'));