# anime.js Performance & Accessibility

Tips for creating performant and accessible animations.

## Performance Optimization

*   **Animate Transforms & Opacity:** Prioritize animating CSS `transform` (`translateX`, `translateY`, `scale`, `rotate`) and `opacity`. These properties can often be hardware-accelerated by the browser and minimize expensive layout recalculations (reflow) and repainting.
*   **Avoid Layout-Triggering Properties:** Be cautious animating properties like `width`, `height`, `margin`, `padding`, `top`, `left`, `font-size`, as they often trigger layout recalculations for the element and potentially others, which is computationally expensive.
*   **Minimize Target Count:** Animating a large number of elements simultaneously can impact performance. Consider:
    *   Staggering animations (`anime.stagger()`) to distribute the load over time.
    *   Animating a single parent container instead of many children if appropriate.
    *   Using techniques like virtual scrolling if animating items in a very long list.
*   **Hardware Acceleration Hints:** While browsers are good at this, explicitly adding `transform: translateZ(0);` or `will-change: transform, opacity;` via CSS *might* hint to the browser to use hardware acceleration, but use `will-change` sparingly as it can consume memory. Test its impact.
*   **Debounce/Throttle Interactions:** For animations triggered by frequent events (like `scroll` or `mousemove`), use debouncing or throttling techniques to limit how often the animation logic runs.
*   **Test Performance:** Use browser developer tools (Performance tab) to profile animations and identify bottlenecks. Look for long frames, excessive layout shifts, or high CPU usage.

## Accessibility Considerations (`a11y`)

*   **Respect Reduced Motion (`prefers-reduced-motion`):** Users may enable a system setting to request reduced motion. Detect this preference using a CSS media query or JavaScript (`matchMedia`) and disable or significantly reduce non-essential animations.
    ```css
    /* Example: Disable animations if user prefers reduced motion */
    @media (prefers-reduced-motion: reduce) {
      .animated-element,
      .stagger-item {
        animation: none !important; /* Disable CSS animations */
        transition: none !important; /* Disable CSS transitions */
        /* For JS animations, check preference before running */
      }
    }
    ```
    ```javascript
    const motionQuery = window.matchMedia('(prefers-reduced-motion: reduce)');

    if (!motionQuery || !motionQuery.matches) {
      // Only run animation if motion is NOT reduced
      anime({ targets: '.my-element', ... });
    }
    ```
*   **Avoid Flashing Content:** Do not create animations that flash rapidly (more than 3 times per second), as this can trigger seizures (WCAG 2.2.2).
*   **Focus Management:** If animations move or hide interactive elements, ensure keyboard focus is managed correctly. Focus should move logically and not be lost or trapped. Consult `accessibility-specialist` if complex focus management is needed.
*   **Readability:** Ensure animations don't make text difficult to read (e.g., excessive movement, low contrast during transitions).
*   **Provide Control (If Necessary):** For longer or potentially distracting animations, consider providing user controls to pause, stop, or hide the animation.

*(Prioritize user experience and inclusivity. Test with accessibility features enabled.)*