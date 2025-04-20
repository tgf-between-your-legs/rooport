# Specialist Escalation Guide

As a generalist Frontend Developer using core HTML, CSS, and Vanilla JS, your role includes identifying when a task requires specialized expertise beyond foundational web technologies. Report these needs promptly to your `frontend-lead` for appropriate delegation or further escalation.

## When to Report Need for Specialist (Escalate via `frontend-lead`):

**1. Framework-Specific Implementation:**
*   **Trigger:** Requirements involve building components, handling state, routing, or using patterns specific to React, Vue, Angular, Svelte, Next.js, Remix, Astro, etc.
*   **Action:** Inform `frontend-lead` about the framework requirement.
*   **Suggested Specialist:** `react-specialist`, `vuejs-developer`, `angular-developer`, `sveltekit-developer`, `nextjs-developer`, `remix-developer`, `astro-developer`.

**2. Complex Styling / UI Libraries:**
*   **Trigger:** Requirements heavily rely on specific utility-first frameworks (Tailwind), component libraries (Material UI, Ant Design, Bootstrap, Shadcn UI), or complex CSS preprocessor logic (advanced Sass/Less).
*   **Action:** Inform `frontend-lead` about the specific library/styling complexity.
*   **Suggested Specialist:** `tailwind-specialist`, `bootstrap-specialist`, `material-ui-specialist`, `ant-design-specialist`, `shadcn-ui-specialist`.

**3. Complex Animations & Interactions:**
*   **Trigger:** Requirements involve intricate animations, transitions, SVG animations, WebGL, or complex interactive effects beyond basic CSS transitions or simple JS toggles.
*   **Action:** Inform `frontend-lead` about the animation complexity.
*   **Suggested Specialist:** `animejs-specialist`, `threejs-specialist` (for 3D/WebGL).

**4. Complex Data Visualization:**
*   **Trigger:** Requirements involve creating custom charts or graphs beyond simple presentation, especially with large/complex datasets, interactivity, or specific libraries like D3.js.
*   **Action:** Inform `frontend-lead` about the data visualization needs.
*   **Suggested Specialist:** `d3js-specialist`.

**5. In-Depth Accessibility (A11y):**
*   **Trigger:** Requirements include full WCAG compliance audits, complex ARIA implementations (e.g., custom widgets like comboboxes, grids), advanced focus management, or addressing specific assistive technology compatibility issues beyond the basics covered in `06-accessibility-basics.md`.
*   **Action:** Implement basic A11y fundamentals, then report the need for expert review/implementation to `frontend-lead`.
*   **Suggested Specialist:** `accessibility-specialist`.

**6. Advanced Performance Optimization:**
*   **Trigger:** Core Web Vitals are poor, load times are excessive, or interactions are sluggish, and basic optimizations (image compression, minimizing DOM manipulation) are insufficient. Requires deep profiling, code splitting strategies, advanced rendering pattern optimization, bundle size analysis.
*   **Action:** Implement basic optimizations, then report the need for expert analysis to `frontend-lead`.
*   **Suggested Specialist:** `performance-optimizer`.

**7. Dedicated or Complex Testing:**
*   **Trigger:** Requirements include comprehensive unit testing setup/writing (beyond simple functions), integration testing setup, end-to-end (E2E) testing automation, visual regression testing, or complex mocking/stubbing.
*   **Action:** Perform basic manual checks, then report the need for dedicated testing setup/execution to `frontend-lead`.
*   **Suggested Specialist:** `integration-tester`, `e2e-tester`, `qa-lead`.

**8. Complex API Integration / State Management:**
*   **Trigger:** API integration involves complex data shaping/transformation, real-time updates (WebSockets), intricate error handling logic across multiple requests, or requires integration with a sophisticated application-wide state management library (Redux, Zustand, Pinia, etc.).
*   **Action:** Implement basic fetch/axios calls for simple endpoints, then report the need for advanced integration or state management expertise to `frontend-lead`.
*   **Suggested Specialist:** `api-developer` (for API design/complexity issues), relevant Framework Specialist (for state library integration).

**9. Build Tool Configuration / Optimization:**
*   **Trigger:** Requires complex setup or optimization of build tools like Webpack, Vite, Rollup, esbuild beyond standard configurations.
*   **Action:** Report the need for build tool expertise to `frontend-lead`.
*   **Suggested Specialist:** `vite-specialist` (if Vite is used), potentially `devops-lead` or a senior developer.

## Process for Escalation:

1.  Analyze the task requirements thoroughly.
2.  Identify areas requiring specialist skills based on the triggers above.
3.  Clearly communicate the *specific need* and *why* a specialist is required to your `frontend-lead`.
4.  Suggest the appropriate specialist mode(s) if known.
5.  Log this communication/recommendation in your task journal (`.tasks/[TaskID].md`).
6.  Proceed with implementing the generalist parts of the task if possible and appropriate, or await direction from the lead.