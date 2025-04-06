## anime.js (v: unknown) - Condensed Context Index

### Overall Purpose
anime.js is a lightweight JavaScript animation library focused on creating complex animations for web elements, CSS properties, and JavaScript objects with a simple API. It supports keyframes, timelines, staggering, springs, and integration with frameworks like React.

### Core Concepts & Capabilities:
*   **Core Animation:** Define animations using `animate(targets, parameters)` targeting CSS selectors, DOM elements, or JS objects. Animate CSS properties (transforms, colors, filters) and object properties. Key concepts: `targets`, `parameters`, `duration`, `delay`, `ease`.
*   **Tween Values:** Specify animation values using strings (e.g., `'6rem'`), functions (`$el => $el.dataset.y`), relative values (`'+=.25'`), or explicit `from`/`to` objects.
*   **Keyframes:** Sequence multiple animation states using the `keyframes` array property, allowing complex multi-step animations with individual timing/easing per step or global settings.
*   **Timelines:** Orchestrate multiple animations using `createTimeline()`. Sequence animations with `add()`, synchronize with `sync()`, and control timing with labels and relative offsets (e.g., `'start'`, `'<+=500'`).
*   **Advanced Features:** Create physics-based animations with `createSpring()`, make elements interactive with `createDraggable()`, trigger animations on scroll with `onScroll()`, apply staggered delays with `stagger()`, and use the lightweight `waapi.animate()` for direct transform control.
*   **Utilities:** Helper functions under `utils` for DOM selection (`$`), math operations (`round`, `clamp`, `mapRange`), and setting properties (`set`).
*   **Integration & Scoping:** Use `createScope()` for managing animations within specific DOM roots (useful for frameworks like React) and applying responsive logic via `mediaQueries`.
*   **Controls & Callbacks:** Manage animation playback with `play()`, `pause()`, `resume()`, `alternate()`, `restart()`. Use callbacks (`onBegin`, `onLoop`, `onUpdate`, `onLeave`) for side effects during animation lifecycle.

### Key APIs / Components / Configuration / Patterns:
*   `import { animate, utils, createSpring, createDraggable, createTimeline, stagger, waapi, onScroll, createScope, createAnimatable, createTimer } from 'animejs';`: Core import statement.
*   `animate(targets, parameters)`: Primary function to create animations. Targets: CSS selectors, DOM nodes, NodeLists, JS objects. Params: object defining properties & control settings.
*   `waapi.animate(targets, parameters)`: Lightweight alternative using WAAPI, recommended for direct `transform` property animation.
*   `createTimeline(parameters)`: Creates a timeline instance. Methods: `add()`, `sync()`, `label()`, `pause()`, `play()`, `restart()`.
*   `createScope({ root, mediaQueries })`: Creates a scope for managing animations (React, responsiveness). Methods: `add()`, `revert()`, `methods`.
*   `createSpring({ stiffness, damping, mass })`: Creates a spring physics-based easing function.
*   `createDraggable(target, { container, releaseEase })`: Makes an element draggable.
*   `createAnimatable(target, initialState)`: Creates an object for direct control of animatable properties (interactive animations).
*   `createTimer({ duration, loop, frameRate, onUpdate, onLoop })`: Creates a timer independent of element animation.
*   `stagger(value, options)`: Utility to apply staggered delays or values across multiple targets.
*   `onScroll({ container, enter, leave, sync, debug, ... })`: Creates scroll-triggered playback control.
*   `utils`: Namespace for helpers (`$`, `round`, `clamp`, `mapRange`, `set`).
*   **Parameters Object Keys:** `targets`, `duration`, `delay`, `ease`, `loop`, `alternate`, `autoplay`, `keyframes`, `[CSS/JS Property]`, Callbacks (`onBegin`, `onLoop`, `onUpdate`, `onComplete`).
*   **Timeline Methods:** `.add(target, params, position)`, `.sync(animationInstance, position)`, `.label(name)`.
*   **React Pattern:** Use `useEffect`, `useRef`, `createScope`, `scope.revert()` for cleanup.

### Common Patterns & Best Practices / Pitfalls:
*   **Installation:** Use `npm install animejs`.
*   **Import:** Use ES6 imports: `import { ... } from 'animejs';`.
*   **Transforms:** Use individual properties (`x`, `scale`) with `animate()`, or `waapi.animate()` for direct `transform` string (recommended).
*   **Framework Integration (React):** Use `createScope` within `useEffect` for lifecycle management and cleanup (`scope.revert()`).
*   **CSS Properties:** Use camelCase (`backgroundColor`) or quoted strings (`'background-color'`).
*   **Responsiveness:** Use `createScope` with `mediaQueries`.
*   **Interactivity:** Use `createAnimatable` for direct control based on events.

This index summarizes the core concepts, APIs, and patterns for anime.js (version unknown). Consult the full source documentation (project_journal/context/source_docs/animejs-specialist-llms-context-20250406.md) for exhaustive details.