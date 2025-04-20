# anime.js: SVG Morphing

Animating the transition between different SVG path shapes using anime.js.

## Core Concept: Animating the `d` Attribute

SVG morphing involves animating the `d` attribute (path data) of an SVG `<path>` element. anime.js can smoothly interpolate between two different path definitions, provided they have the **same number and type of path commands and points**.

**Key Requirements:**

*   **Compatible Paths:** The starting and ending paths *must* have the exact same sequence of path commands (e.g., `M`, `L`, `C`, `Q`, `A`, `Z`) and the same number of coordinate points for each command type. Differences will cause the animation to jump or fail.
*   **Targeting:** Target the `<path>` element directly.
*   **Property:** Animate the `d` attribute.
*   **Value:** Provide the target `d` attribute string as the value (or use a `[start, end]` array if the starting shape isn't the path's current `d` value).

## Basic Morphing Example

Assume you have two compatible SVG paths defined in your HTML:

```html
<svg width="200" height="200" viewBox="0 0 100 100">
  <!-- Initial Shape (e.g., a square) -->
  <path id="shape" d="M 10 10 L 90 10 L 90 90 L 10 90 Z" fill="blue"></path>

  <!-- Target Shape (e.g., a star - MUST have same command structure as square) -->
  <!-- This is a simplified example; real morphing paths need careful construction -->
  <path id="targetShapeSquare" d="M 10 10 L 90 10 L 90 90 L 10 90 Z" style="display: none;"></path>
  <path id="targetShapeStar" d="M 50 10 L 61.8 38.2 L 90.9 38.2 L 68.2 57 L 79.1 85.4 L 50 69.1 L 20.9 85.4 L 31.8 57 L 9.1 38.2 L 38.2 38.2 Z" style="display: none;"></path>
  <!-- NOTE: The star path above likely DOES NOT have the same structure as the square.
       You'd typically use tools or manual editing to create compatible paths. -->
</svg>

<button id="morphButton">Morph</button>
```

```javascript
import anime from 'animejs/lib/anime.es.js';

// Get the d attribute value from the target shape definition
// In a real scenario, you might generate these paths or get them from design tools
const squarePath = document.querySelector('#targetShapeSquare').getAttribute('d');
const starPath = document.querySelector('#targetShapeStar').getAttribute('d'); // Assuming this is compatible!

let isSquare = true;

document.querySelector('#morphButton').onclick = () => {
  anime({
    targets: '#shape', // Target the path element
    d: isSquare ? starPath : squarePath, // Animate the 'd' attribute to the target path data
    duration: 1500,
    easing: 'easeInOutQuad'
  });
  isSquare = !isSquare;
};
```

## Using Keyframes for Multi-Step Morphing

You can morph through multiple compatible shapes using keyframes on the `d` property.

```javascript
// Assuming path1, path2, path3 are compatible path data strings
anime({
  targets: '#shape',
  d: [
    { value: path1, duration: 1000, easing: 'easeInOutSine' }, // Morph to path1
    { value: path2, duration: 1000, delay: 100, easing: 'easeInOutQuad' }, // Then morph to path2
    { value: path3, duration: 1000, delay: 100, easing: 'easeInOutExpo' }  // Then morph to path3
  ],
  loop: true,
  direction: 'alternate'
});
```

## Tools & Techniques for Compatible Paths

Creating compatible paths manually can be tedious and error-prone.

*   **SVG Editors:** Tools like Adobe Illustrator, Inkscape, or Figma often have features to add/remove points or simplify paths. Careful manual editing might be needed to ensure point counts match.
*   **Libraries:** Libraries like Flubber.js are specifically designed to interpolate between *arbitrary* shapes (even with different point counts) by adding intermediate points. You could potentially use such a library to generate compatible intermediate path data strings for anime.js, although this adds complexity.
*   **Manual Point Addition/Subdivision:** Carefully add points along segments of the simpler path until it has the same number of points and command structure as the more complex path, ensuring the added points don't drastically alter the initial shape.

## Considerations

*   **Performance:** Morphing complex paths can be computationally intensive. Test performance, especially on less powerful devices.
*   **Path Compatibility:** This is the biggest challenge. Ensure the start and end paths have identical command structures and point counts. Use SVG validation tools or inspect the path data carefully.
*   **Easing:** Standard easing functions apply well to morphing.

SVG morphing with anime.js allows for visually impressive shape transitions when path compatibility is maintained.

*(Refer to the official anime.js SVG Animations documentation.)*