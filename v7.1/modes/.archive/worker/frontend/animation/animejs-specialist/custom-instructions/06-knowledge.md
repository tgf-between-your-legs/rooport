# 6. Context / Knowledge Base

**Core anime.js Concepts:**
*   **Targets:** CSS selectors, DOM elements, JS Objects, Arrays.
*   **Properties:** Animatable CSS properties (especially `transform`, `opacity`), transforms (`translateX`, `scale`, `rotate`), Object properties, SVG attributes (`d`, `points`, `fill`).
*   **Parameters:** `targets`, `properties`, `duration`, `delay`, `easing` (built-in functions, cubic bezier, steps, custom), `direction`, `loop`, `autoplay`.
*   **Values:** Direct values (`100px`, `#FFF`), relative values (`+=100`, `*=2`), function-based values (`(el, i) => ...`), unitless values for transforms.
*   **Advanced Features:** Keyframes (`keyframes: [...]`), timelines (`anime.timeline()`, `.add()`), staggering (`stagger()`), controls (`play`, `pause`, `restart`, `seek`), callbacks (`begin`, `update`, `complete`, `loopComplete`).
*   **Framework Integration:** Understanding component lifecycle hooks (e.g., React's `useEffect`/`useRef`, Vue's `mounted`/`ref`, Angular's `ngAfterViewInit`/`ElementRef`) for safe DOM manipulation and animation cleanup.

**Best Practices & Patterns:**
*   Performance optimization (prioritizing transforms/opacity, minimizing reflows).
*   Framework-specific integration patterns (using refs, cleanup).
*   Accessibility considerations (`prefers-reduced-motion`).
*   Creating reusable animation functions or components.
*   Structuring complex timelines.

**Resources:**
*   Official anime.js Documentation: https://animejs.com/documentation/
*   Context files within the `context/` directory.