# anime.js: Scroll-Triggered Animations

Techniques for starting animations based on element visibility or scroll position.

## Core Concept

Scroll-triggered animations start playing when an element enters the viewport or when the user scrolls to a specific point on the page. This is often used for "animate on scroll" effects. anime.js itself doesn't have built-in scroll triggers, but it integrates well with browser APIs or third-party libraries designed for this purpose.

## 1. Using `Intersection Observer` API (Recommended)

*   **Concept:** A modern browser API that efficiently detects when a target element enters or exits the browser's viewport (or another specified root element). This is the **preferred method** for triggering animations when an element becomes visible.
*   **Workflow:**
    1.  Create an `IntersectionObserver` instance, providing a callback function.
    2.  Observe the target element(s) you want to animate.
    3.  In the callback function, check the `isIntersecting` property of the observed entries.
    4.  If `isIntersecting` is true, create and play the anime.js animation.
    5.  Optionally, `unobserve` the element after the animation starts if it should only play once.

```javascript
import anime from 'animejs/lib/anime.es.js';

const elementsToAnimate = document.querySelectorAll('.animate-on-scroll');

const observerOptions = {
  root: null, // Use the viewport as the root
  rootMargin: '0px',
  threshold: 0.1 // Trigger when 10% of the element is visible
};

const observerCallback = (entries, observer) => {
  entries.forEach(entry => {
    // Check if the element is intersecting (entering the viewport)
    if (entry.isIntersecting) {
      const targetElement = entry.target;

      // Prevent re-triggering if already animated (optional)
      if (targetElement.classList.contains('has-animated')) {
        return;
      }
      targetElement.classList.add('has-animated');

      console.log('Element intersecting:', targetElement);

      // Create and play the anime.js animation
      anime({
        targets: targetElement,
        translateY: [50, 0], // Example: Slide up
        opacity: [0, 1],     // Example: Fade in
        duration: 1000,
        easing: 'easeOutExpo',
        delay: parseInt(targetElement.dataset.delay || '0') // Optional delay from data attribute
      });

      // Optional: Stop observing the element after animation starts
      observer.unobserve(targetElement);
    }
    // Optional: Add logic here if you want to reverse animation when exiting viewport
    // else {
    //   // Element is NOT intersecting
    // }
  });
};

// Create the observer
const intersectionObserver = new IntersectionObserver(observerCallback, observerOptions);

// Observe each target element
elementsToAnimate.forEach(el => {
  intersectionObserver.observe(el);
});
```

## 2. Using Scroll Event Listener (Less Performant)

*   **Concept:** Attach an event listener to the window's `scroll` event. In the handler, calculate the element's position relative to the viewport and trigger the animation when it reaches a certain point.
*   **Performance Issue:** Scroll events fire very frequently, and performing calculations (like `getBoundingClientRect()`) inside the handler can cause performance jank and layout thrashing. **`Intersection Observer` is strongly preferred.**
*   **Throttling/Debouncing:** If using scroll events, it's crucial to throttle or debounce the event handler to limit how often the calculations run.

```javascript
// --- Scroll Event Listener (Less Recommended) ---
// import anime from 'animejs/lib/anime.es.js';
// import { throttle } from 'lodash-es'; // Example using lodash throttle

// const elements = document.querySelectorAll('.animate-on-scroll-event');

// function checkVisibility() {
//   elements.forEach(el => {
//     if (el.classList.contains('has-animated')) return;

//     const rect = el.getBoundingClientRect();
//     const windowHeight = window.innerHeight || document.documentElement.clientHeight;

//     // Check if element top is within viewport (adjust threshold as needed)
//     if (rect.top <= windowHeight * 0.8 && rect.bottom >= 0) {
//       el.classList.add('has-animated');
//       anime({
//         targets: el,
//         opacity: [0, 1],
//         translateY: [30, 0],
//         duration: 800,
//         easing: 'easeOutCubic'
//       });
//       // Potentially remove listener for this element if only animating once
//     }
//   });
// }

// // Throttle the checkVisibility function to run at most once every 100ms
// const throttledCheck = throttle(checkVisibility, 100);

// window.addEventListener('scroll', throttledCheck);
// window.addEventListener('resize', throttledCheck); // Also check on resize
// checkVisibility(); // Initial check on load
// --- End Scroll Event Listener ---
```

## 3. Using Third-Party Scroll Animation Libraries

*   **Concept:** Libraries like GSAP (GreenSock Animation Platform) with its ScrollTrigger plugin, or ScrollMagic, provide more advanced features for scroll-based animations, including scrubbing (linking animation progress directly to scroll position), pinning elements, and complex sequencing.
*   **Integration:** You can often use these libraries to *trigger* anime.js animations or timelines at specific scroll points, or use the library's own animation engine.
*   **Pros:** More features, potentially smoother scrubbing effects.
*   **Cons:** Adds another library dependency. Steeper learning curve for advanced features.

## Accessibility (`prefers-reduced-motion`)

*   Always respect the user's motion preferences. Wrap animation triggers in a check for `prefers-reduced-motion`.

```javascript
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

// Inside Intersection Observer callback or other trigger logic:
if (!prefersReducedMotion.matches) {
  // Only play animation if user HAS NOT requested reduced motion
  anime({
    targets: targetElement,
    // ... animation parameters ...
  });
} else {
  // Optionally apply a static end state instantly if motion is reduced
  targetElement.style.opacity = '1';
  targetElement.style.transform = 'translateY(0)';
}
```

For most "animate when visible" scenarios, the `Intersection Observer` API provides the most performant and straightforward approach to integrate with anime.js.

*(Refer to MDN documentation for Intersection Observer API.)*