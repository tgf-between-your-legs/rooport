# 4. Key Considerations / Safety Protocols

*   **Performance:** Prioritize animating CSS `transform` and `opacity` properties as they are typically handled more efficiently by the browser (often GPU-accelerated) and less likely to cause layout reflows. Avoid animating layout-triggering properties (e.g., `width`, `height`, `top`, `left`, `margin`, `padding`) excessively, especially on many elements simultaneously.
*   **Targeting:** Use specific and efficient CSS selectors for the `targets` parameter. In framework contexts (React, Vue, Angular), prefer using refs (`useRef`, `ref`, `ElementRef`) to get direct DOM element references instead of relying solely on potentially fragile global selectors.
*   **Units:** Be consistent with units for CSS properties (e.g., `px`, `em`, `rem`, `%`). Note that `transform` properties like `translateX`, `scale`, etc., often don't require units for pixel values but might for others (e.g., `rotate: '45deg'`).
*   **SVG Morphing:** Ensure source and target SVG paths have the same number of points and compatible point order for smooth morphing animations. Use tools or manual inspection to verify path compatibility.
*   **Cleanup:** In Single Page Applications (SPAs), ensure anime.js instances are properly controlled or destroyed when components unmount to prevent memory leaks or unexpected behavior. Use framework lifecycle hooks (`useEffect` cleanup, `ngOnDestroy`, `beforeUnmount`). Consider using `anime.remove(targets)` if necessary.
*   **Accessibility:**
    *   Respect the `prefers-reduced-motion` media query. Wrap animations in a check for this preference or provide alternative, reduced-motion versions.
    *   Ensure animations don't interfere with keyboard navigation or focus management.
    *   Avoid animations that flash excessively (more than 3 times per second) which can trigger seizures.