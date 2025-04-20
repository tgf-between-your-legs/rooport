# anime.js: Interactive Animations

Triggering and controlling animations based on user interactions like clicks, hover, and mouse movements.

## Core Concept

Interactive animations respond directly to user input. This typically involves:

1.  **Setting up Event Listeners:** Attach standard JavaScript event listeners (`addEventListener`) to the target elements or related trigger elements.
2.  **Creating Animation Instances:** Define anime.js animations, often with `autoplay: false` so they don't run immediately.
3.  **Controlling Playback:** Use anime.js control functions (`play()`, `pause()`, `reverse()`, `restart()`, `seek()`) within the event listener callbacks to manipulate the animation based on the user's action.

## Common Patterns

**1. Click/Tap to Trigger:**

*   Start an animation when an element is clicked or tapped.

```javascript
import anime from 'animejs/lib/anime.es.js';

const box = document.querySelector('.click-box');
const boxAnimation = anime({
  targets: box,
  scale: [1, 1.2, 1], // Scale up and back down
  rotate: '10deg',
  duration: 500,
  easing: 'easeInOutSine',
  autoplay: false, // Don't play on load
  complete: () => console.log('Click animation complete')
});

box.addEventListener('click', () => {
  // Restart animation from beginning on each click
  boxAnimation.restart();
});
```

**2. Hover Effects:**

*   Play an animation on `mouseenter` and potentially reverse or reset it on `mouseleave`.

```javascript
import anime from 'animejs/lib/anime.es.js';

const hoverTarget = document.querySelector('.hover-target');

// It's often better to create the animation instance *inside* the event handler
// if parameters depend on state at the time of hover, but for simple cases:
let hoverAnimation; // Keep track of the animation instance

hoverTarget.addEventListener('mouseenter', () => {
  // Ensure previous animation is stopped if needed, or create new one
  if (hoverAnimation) hoverAnimation.pause(); // Optional: pause if re-hovering quickly

  hoverAnimation = anime({
    targets: hoverTarget,
    scale: 1.1,
    backgroundColor: '#F0A', // Change color on hover
    duration: 300,
    easing: 'easeOutQuad'
  });
});

hoverTarget.addEventListener('mouseleave', () => {
  if (hoverAnimation) hoverAnimation.pause(); // Optional

  // Animate back to original state
  anime({
    targets: hoverTarget,
    scale: 1.0,
    backgroundColor: '#AAA', // Original color
    duration: 400,
    easing: 'easeOutQuad'
  });
});
```

**3. Mouse Tracking / Parallax:**

*   Update animation properties (like transforms) based on the mouse cursor's position relative to an element or the viewport.
*   **Performance:** This requires frequent updates within the `mousemove` event. It's crucial to **throttle** the event handler and animate performant properties (`transform`, `opacity`).

```javascript
import anime from 'animejs/lib/anime.es.js';
import { throttle } from 'lodash-es'; // Example using lodash throttle

const container = document.querySelector('.mouse-container');
const elementToMove = container.querySelector('.move-target');

const handleMouseMove = throttle((event) => {
  const rect = container.getBoundingClientRect();
  // Calculate mouse position relative to container center (-1 to 1 range)
  const mouseX = event.clientX - rect.left;
  const mouseY = event.clientY - rect.top;
  const centerX = rect.width / 2;
  const centerY = rect.height / 2;
  const moveX = (mouseX - centerX) / centerX; // -1 to 1
  const moveY = (mouseY - centerY) / centerY; // -1 to 1

  const maxMove = 15; // Max pixels to move

  // Use anime.set for direct property updates (no duration needed)
  anime.set(elementToMove, {
    translateX: moveX * maxMove,
    translateY: moveY * maxMove,
    // Example: rotate slightly based on horizontal position
    rotate: moveX * 5 // degrees
  });

  // Alternatively, use anime() with short duration for smoother easing effect
  // anime({
  //   targets: elementToMove,
  //   translateX: moveX * maxMove,
  //   translateY: moveY * maxMove,
  //   rotate: moveX * 5,
  //   duration: 100, // Short duration for smoothing
  //   easing: 'linear'
  // });

}, 16); // Throttle to roughly 60fps

container.addEventListener('mousemove', handleMouseMove);

// Reset position when mouse leaves
container.addEventListener('mouseleave', () => {
  anime({
    targets: elementToMove,
    translateX: 0,
    translateY: 0,
    rotate: 0,
    duration: 300,
    easing: 'easeOutQuad'
  });
});
```

**4. Controlling Timelines Interactively:**

*   Use timeline controls (`play`, `pause`, `reverse`, `seek`) in response to events. `seek()` is useful for linking animation progress to input controls like sliders or scroll position (scrubbing).

```javascript
const timeline = anime.timeline({
  targets: '.path-drawing path',
  strokeDashoffset: [anime.setDashoffset, 0],
  easing: 'easeInOutSine',
  duration: 1500,
  autoplay: false // Control playback manually
});

timeline.add({ targets: '.other-element', opacity: 1 });

const slider = document.querySelector('#progressSlider');

slider.addEventListener('input', () => {
  // Seek animation based on slider value (0-100)
  timeline.seek(timeline.duration * (slider.value / 100));
});

document.querySelector('#playBtn').onclick = timeline.play;
document.querySelector('#pauseBtn').onclick = timeline.pause;
```

## Considerations

*   **Performance:** Be mindful of how many animations are running and how often event handlers fire, especially for `scroll` and `mousemove`. Throttle/debounce handlers. Animate performant properties (`transform`, `opacity`).
*   **User Experience:** Ensure interactions are intuitive. Provide clear visual cues. Avoid overly distracting or jarring animations.
*   **Accessibility:** Ensure interactive elements triggering animations are keyboard accessible. Respect `prefers-reduced-motion`.
*   **State Management:** For complex interactions, manage the animation state carefully (e.g., preventing multiple clicks from running animations concurrently if not desired).

Interactive animations can significantly enhance user engagement when implemented thoughtfully and performantly.