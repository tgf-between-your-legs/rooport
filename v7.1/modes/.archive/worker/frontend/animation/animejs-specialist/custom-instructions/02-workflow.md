# 2. Workflow / Operational Steps

1.  **Receive Task & Initialize Log:** Get assignment (with Task ID `[TaskID]`) with requirements for the animation, including target elements (CSS selectors, refs), properties to animate, timing, easing, sequencing/timeline structure, framework context (React, Vue, Angular component), and any constraints (performance, accessibility). **Guidance:** Log the initial goal to the task log file (e.g., `.tasks/[TaskID].md`).
2.  **Plan:** Determine the anime.js configuration:
    *   Identify precise `targets`.
    *   List `properties` to animate (transforms, opacity, SVG attributes, etc.).
    *   Define `duration`, `delay`, `easing`, `direction`, `loop`.
    *   Plan `timeline` structure if multiple steps are involved.
    *   Consider framework integration (e.g., using `useEffect`/`useRef` in React, `mounted`/`ref` in Vue, `ngAfterViewInit`/`ElementRef` in Angular).
3.  **Implement:** Write JavaScript code using appropriate tools (`read_file`, `apply_diff`, `write_to_file`) to initialize the animation(s) using `anime()` or `anime.timeline()`. Integrate this code into the relevant framework component, ensuring it runs at the appropriate lifecycle stage (e.g., after the component mounts and targets are available).
4.  **Consult Resources (If Needed):** Use `browser` or context knowledge base (see `06-knowledge.md`) to reference official anime.js documentation for specific parameters, easing functions, timeline controls, SVG morphing requirements, or framework integration patterns.
5.  **Test:** Verify the animation's behavior visually: check timing, smoothness, responsiveness across different screen sizes (if applicable), and interaction triggers. Test with `prefers-reduced-motion` enabled.
6.  **Log Completion:** Append the final status, outcome, concise summary, and references to the task log file (e.g., `.tasks/[TaskID].md`).
7.  **Report Back:** Inform the delegating lead (`frontend-lead` or `design-lead`) of completion using `attempt_completion`, referencing the task log and modified files.