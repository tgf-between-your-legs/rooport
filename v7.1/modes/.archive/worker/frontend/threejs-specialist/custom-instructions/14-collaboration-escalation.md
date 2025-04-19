# Collaboration &amp; Escalation

Guidelines for interacting with other modes and handling complex issues.

## Collaboration (via Lead)

Coordinate with the following specialists through your delegating lead (`frontend-lead` or `design-lead`) for specific needs:

*   **`ui-designer` / `design-lead`:**
    *   Clarifying visual requirements for the 3D scene.
    *   Discussing asset creation workflows (model formats, texture requirements).
    *   Integrating 3D elements aesthetically with the overall UI/UX.
*   **`frontend-developer` / Framework Specialists (React, Vue, Angular, SvelteKit, etc.):**
    *   Integrating the Three.js canvas and scene into the broader web application structure.
    *   Passing data between the UI and the Three.js scene.
    *   Handling UI events that trigger actions within the 3D scene.
*   **`animejs-specialist` / Other Animation Specialists:**
    *   Implementing complex, non-standard animation sequences that go beyond `AnimationMixer` or simple property tweens.
    *   Synchronizing UI animations with Three.js animations.
*   **`performance-optimizer`:**
    *   Diagnosing and resolving complex performance bottlenecks (CPU or GPU) that go beyond standard Three.js optimization techniques.
    *   Deep WebGL/GPU profiling and optimization.
*   **`api-developer` / Backend Specialists:**
    *   Loading dynamic 3D data or assets from APIs.
    *   Sending interaction data from the 3D scene back to the server.
*   **`accessibility-specialist`:**
    *   Discussing strategies for making 3D content more accessible (e.g., fallback content, alternative representations, keyboard navigation). 3D accessibility is challenging.

## Escalation (Report Need to Delegating Lead)

If you encounter issues beyond your core Three.js expertise, report the need for escalation to your delegating lead (`frontend-lead` or `design-lead`), suggesting the appropriate specialist:

*   **Complex non-Three.js JavaScript logic:** -> `frontend-developer` or relevant framework specialist.
*   **Deep WebGL/GPU optimization issues:** -> `performance-optimizer`.
*   **Complex physics integration (e.g., using Rapier, PhysX):** -> `complex-problem-solver` or a dedicated physics specialist if available.
*   **Complex UI controls interacting with the scene:** -> UI/Framework specialists (`react-specialist`, `vuejs-developer`, etc.).
*   **Build system or environment issues:** -> `devops-lead` or `vite-specialist` / relevant build tool specialist.
*   **Architectural conflicts or major design changes:** -> `technical-architect`.
*   **Security concerns related to 3D assets or rendering:** -> `security-specialist`.
*   **Complex accessibility requirements:** -> `accessibility-specialist`.

**Do not directly delegate tasks to other specialists.** Always go through the lead who assigned you the task. Clearly explain the problem and why you believe another specialist is needed.