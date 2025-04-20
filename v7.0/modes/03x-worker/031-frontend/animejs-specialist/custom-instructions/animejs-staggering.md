# anime.js: Staggering Animations

Applying incremental delays or value changes to multiple targets using `anime.stagger()`.

## Core Concept: Staggering

Staggering is a powerful feature in anime.js that allows you to apply animations to multiple targets with incremental delays or value changes based on their index or position. This creates visually appealing sequential or distributed effects without manually calculating delays for each element.

**`anime.stagger(value, [options])`:**

*   **`value`:** The base value for the stagger (e.g., delay amount, starting value).
*   **`options` (Optional Object):**
    *   `grid`: An array `[columns, rows]` defining a grid layout for position-based staggering.
    *   `axis`: `'x'` or `'y'`. Used with `grid` to determine stagger direction.
    *   `from`: Specifies the starting point for the stagger calculation:
        *   `'first'` (default): Staggers from the first target.
        *   `'last'`: Staggers from the last target.
        *   `'center'`: Staggers from the center outwards.
        *   `index`: Staggers from the target at the specified index.
    *   `direction`: `'normal'` (default) or `'reverse'`. Reverses the stagger order.
    *   `easing`: Apply an easing function to the stagger distribution itself (e.g., `'easeOutQuad'`).
    *   `start`: A starting value added to the stagger calculation (e.g., `start: 500` adds a 500ms base delay).

## Common Use Cases

**1. Staggering Delay:**

*   Apply an incremental delay to each target element.

```javascript
import anime from 'animejs/lib/anime.es.js';

anime({
  targets: '.stagger-delay .el',
  translateX: 250,
  // Each element starts 100ms after the previous one
  delay: anime.stagger(100)
});

anime({
  targets: '.stagger-reverse .el',
  translateX: 250,
  delay: anime.stagger(100, { direction: 'reverse' }) // Stagger starts from the last element
});

anime({
  targets: '.stagger-center .el',
  translateX: 250,
  delay: anime.stagger(100, { from: 'center' }) // Stagger outwards from the center
});

anime({
  targets: '.stagger-easing .el',
  translateX: 250,
  // Apply an easing curve to the delay distribution itself
  delay: anime.stagger(200, { easing: 'easeOutQuad' })
});

anime({
  targets: '.stagger-grid .el',
  scale: [
    { value: .1, easing: 'easeOutSine', duration: 500 },
    { value: 1, easing: 'easeInOutQuad', duration: 1200 }
  ],
  // Stagger delay based on grid position (assuming 10x10 grid)
  delay: anime.stagger(200, { grid: [10, 10], from: 'center' })
});
```

**2. Staggering Property Values:**

*   Apply incremental changes to property values across targets.

```javascript
anime({
  targets: '.stagger-values .el',
  translateX: 250,
  // Start rotation from 0deg, incrementing by 10deg for each element
  rotate: anime.stagger([0, 90]), // Equivalent to anime.stagger([0, 90], { from: 'first' })
  // Start scale from 0.5, ending at 1, distributed across elements
  scale: anime.stagger([.5, 1], { from: 'center' })
});
```

**3. Staggering within Timelines:**

*   Staggering can be used effectively within timeline `.add()` calls, often combined with relative offsets.

```javascript
const tl = anime.timeline({
  targets: '.timeline-stagger .el',
  delay: anime.stagger(200, { grid: [14, 5], from: 'center' }),
  loop: true,
  direction: 'alternate'
});

tl.add({
  scale: [
    { value: .1, easing: 'easeOutSine', duration: 500 },
    { value: 1, easing: 'easeInOutQuad', duration: 1200 }
  ]
})
.add({
  translateX: () => anime.random(-50, 50), // Add random horizontal movement after scaling
  translateY: () => anime.random(-50, 50),
  delay: anime.stagger(10), // Small stagger for the movement
  offset: '-=800' // Overlap with the scaling animation
});
```

Staggering provides a concise way to create complex, distributed animations across multiple elements without manual calculations. Experiment with different `value`, `from`, `easing`, and `grid` options to achieve various effects.

*(Refer to the official anime.js Staggering documentation.)*