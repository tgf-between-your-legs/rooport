# anime.js API Quick Reference

A condensed guide to core anime.js functions and parameters.

## Core Function: `anime(options)`

Creates and controls animations. Takes an options object.

```javascript
import anime from 'animejs/lib/anime.es.js'; // ES module import

anime({
  targets: '.css-selector', // CSS Selector, DOM Node, NodeList, Object, Array
  // --- Properties ---
  translateX: 250, // Animate CSS transform
  opacity: [0, 1], // Animate from 0 to 1
  color: '#FFF', // Animate CSS color
  value: 100, // Animate JS Object property
  points: '...new path data...', // Animate SVG attribute

  // --- Parameters ---
  duration: 1000, // Milliseconds
  delay: 500, // Milliseconds or function (el, i) => i * 100
  easing: 'easeInOutQuad', // Easing function name (see easing section)
  direction: 'alternate', // 'normal', 'reverse', 'alternate'
  loop: true, // true, false, or number of loops
  autoplay: true, // true or false
  round: 1, // Round values to N decimal places

  // --- Callbacks ---
  begin: (anim) => { console.log('Animation started'); },
  update: (anim) => { console.log(anim.progress); },
  complete: (anim) => { console.log('Animation completed'); },
  // loopBegin, loopComplete, changeBegin, changeComplete
});
```

## Timeline: `anime.timeline(options)`

Creates a timeline instance for sequencing multiple animations. Inherits default parameters.

```javascript
const tl = anime.timeline({
  easing: 'easeOutExpo',
  duration: 750
});

// Add animations to the timeline
tl
  .add({
    targets: '.element1',
    translateX: 250
  })
  .add({
    targets: '.element2',
    translateY: 100,
    // Relative offset: starts 100ms before previous animation ends
    offset: '-=100'
  })
  .add({
    targets: '.element3',
    opacity: [0, 1],
    // Absolute offset: starts at 1000ms from timeline start
    offset: 1000
  });

// Timeline controls: tl.play(), tl.pause(), tl.restart(), tl.seek(ms)
```

## Common Parameters

*   **`targets`**: The element(s) or object(s) to animate.
*   **Properties**: CSS properties (camelCase), CSS Transforms (`translateX`, `rotate`, `scale`), Object properties, SVG attributes.
*   **`duration`**: Animation length in ms.
*   **`delay`**: Wait time before animation starts in ms. Can be a function `(el, i, total) => ...` for staggering.
*   **`easing`**: Acceleration curve. Common: `linear`, `easeInQuad`, `easeOutQuad`, `easeInOutQuad`, `easeInCubic`, `easeOutCubic`, `easeInOutCubic`, `easeInExpo`, `easeOutExpo`, `easeInOutExpo`, `spring(...)`. (See animejs.com/documentation/#pennerFunctions)
*   **`direction`**: `normal`, `reverse`, `alternate`.
*   **`loop`**: `true`, `false`, or number.
*   **`autoplay`**: `true` or `false`.
*   **`round`**: Round values to N decimal places.

## Value Types

*   **Unitless**: `translateX: 250` (defaults to `px` for CSS transforms).
*   **Specific Units**: `width: '100%'`, `rotate: '1turn'`.
*   **From/To**: `opacity: [0, 1]`, `translateX: ['100px', '200px']`.
*   **Relative**: `translateX: '+=100px'`.
*   **Function-based**: `translateX: (el, i) => i * 50`. Staggering often uses this.
*   **Keyframes**: `translateX: [{ value: 100, duration: 500 }, { value: 0, duration: 800 }]`.

## Staggering

Apply delays incrementally across multiple targets.

```javascript
anime({
  targets: '.stagger-el',
  translateX: 270,
  delay: anime.stagger(100) // 100ms delay between each element
  // delay: anime.stagger(100, { from: 'center', grid: [10, 5], axis: 'x' }) // Advanced
});
```

## SVG Animation

*   **Morphing:** Animate the `d` attribute of `<path>` elements. Paths must have the same number of points. Use tools like flubber.js or preprocessing if needed.
    ```javascript
    anime({ targets: 'path', d: [{ value: 'M...'}, { value: 'M...' }] });
    ```
*   **Line Drawing:** Animate `strokeDashoffset`. Requires setting `strokeDasharray` first.
    ```javascript
    // CSS: path { stroke-dasharray: 1000; stroke-dashoffset: 1000; }
    anime({ targets: 'path', strokeDashoffset: [anime.setDashoffset, 0] });
    ```

*(Consult the official anime.js documentation for full details: https://animejs.com/documentation/)*