# anime.js: Timelines

Creating and controlling complex, synchronized animation sequences using `anime.timeline()`.

## Core Concept: Timelines

Timelines allow you to orchestrate multiple animations together, defining their order, timing, and relationship to each other. Instead of managing multiple `anime()` instances with complex delays, you add animations to a timeline instance.

*   **`anime.timeline(parameters)`:** Creates a new timeline instance. It accepts most standard animation parameters (like `duration`, `easing`, `direction`, `loop`, `autoplay`) which act as defaults for animations added to the timeline.
*   **`.add(parameters, [offset])`:** Adds an animation segment to the timeline.
    *   **`parameters`:** An object defining the animation targets, properties, and specific parameters (duration, easing, delay *relative to its position in the timeline*). These override timeline defaults.
    *   **`offset` (Optional):** Controls when this animation starts relative to the previous animation or specific points in the timeline.
        *   **No Offset (Default):** Starts immediately after the previous animation in the timeline finishes.
        *   **Absolute Time:** `offset: 1000` (Starts at 1000ms from the beginning of the timeline).
        *   **Relative Offset:** `offset: '+=500'` (Starts 500ms after the *previous* animation *starts*).
        *   **Relative Offset (End):** `offset: '-=500'` (Starts 500ms *before* the *previous* animation *ends*). Creates overlaps.
        *   **Label Offset:** `offset: 'labelName+=100'` (Starts 100ms after a defined label - see below).

## Creating a Basic Timeline

```javascript
import anime from 'animejs/lib/anime.es.js';

// Create a timeline instance
const tl = anime.timeline({
  easing: 'easeOutExpo', // Default easing for animations in this timeline
  duration: 750, // Default duration
  loop: true,
  direction: 'alternate'
});

// Add animations sequentially
tl.add({
  targets: '.box1',
  translateX: 250,
  backgroundColor: '#FF0000'
})
.add({ // Starts after the first animation completes
  targets: '.box2',
  translateY: 200,
  scale: 1.2,
  rotate: '10deg',
  backgroundColor: '#00FF00'
})
.add({ // Starts after the second animation completes
  targets: '.box3',
  translateX: -100,
  opacity: 0.5,
  backgroundColor: '#0000FF'
});

// Timeline controls are the same as single animation controls
// tl.play();
// tl.pause();
// tl.restart();
// tl.seek(percentage);
```

## Using Offsets for Overlap and Timing

```javascript
const tl = anime.timeline({
  easing: 'easeInOutSine',
  duration: 500
});

tl.add({
  targets: '.element1',
  translateX: 200
})
.add({
  targets: '.element2',
  translateX: 200,
  offset: '-=300' // Start 300ms before element1 animation ENDS (overlap)
})
.add({
  targets: '.element3',
  translateX: 200,
  offset: '+=100' // Start 100ms after element2 animation STARTS
})
.add({
  targets: '.element4',
  translateX: 200,
  offset: 1500 // Start exactly at 1500ms from the beginning of the timeline
});
```

## Timeline Labels

*   **Purpose:** Define named points in time within the timeline, making it easier to reference start times for subsequent animations using relative label offsets.
*   **`.add(labelName, [offset])`:** Adds a label at a specific point. The offset works the same way as for animation segments.

```javascript
const tl = anime.timeline({ easing: 'easeOutExpo', duration: 1000 });

tl.add({
  targets: '.intro-text',
  opacity: [0, 1],
  translateY: [50, 0]
})
// Add a label named 'fadeInComplete' right after the intro text finishes fading in
.add('fadeInComplete')
.add({
  targets: '.main-content',
  opacity: [0, 1],
  scale: [0.8, 1],
  // Start this animation 200ms after the 'fadeInComplete' label
  offset: 'fadeInComplete+=200'
})
.add({
  targets: '.buttons .btn',
  translateY: [20, 0],
  opacity: [0, 1],
  delay: anime.stagger(100), // Stagger button animations
  // Start staggering 100ms after the 'fadeInComplete' label
  offset: 'fadeInComplete+=100'
});
```

Timelines are essential for building complex, multi-step animation sequences with precise control over timing and synchronization.

*(Refer to the official anime.js Timeline documentation.)*