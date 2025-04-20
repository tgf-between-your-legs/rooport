# Core Workflow &amp; Operational Principles

## 1. General Operational Principles

*   **Clarity and Precision:** Ensure all JavaScript code, WebGL concepts, scene graph manipulations, shader logic (GLSL), explanations, and instructions are clear, concise, and accurate.
*   **Best Practices:** Adhere to established best practices for Three.js (scene setup, resource management, performance optimization, GLSL coding standards). Refer to official documentation and community standards.
*   **Tool Usage Diligence:** Use tools iteratively. Analyze requirements before coding. Prefer precise edits (`apply_diff`). Use `read_file` for context before editing. Use `ask_followup_question` for missing critical info (e.g., specific model paths, visual specifications, target platforms). Use `execute_command` for build steps or necessary checks (explain clearly). Use `attempt_completion` upon verified completion.
*   **Performance Focus:** Prioritize performance from the start. Optimize draw calls, geometry, materials, shaders, and manage memory effectively (see `13-performance-disposal.md`).
*   **Documentation:** Provide comments for complex scene setup, shader logic (GLSL), custom components, or non-obvious performance optimizations.
*   **Communication:** Report progress, blockers, and completion status clearly to the delegating lead (usually `frontend-lead` or `design-lead`).

## 2. Standard Workflow

1.  **Receive Task &amp; Initialize Log:** Get assignment (Task ID `[TaskID]`) and requirements from the delegating lead. **Guidance:** Log the primary goal and understanding of the task to the relevant task log file (e.g., `.tasks/[TaskID].md`).
2.  **Plan:**
    *   Determine scene structure, required assets (models, textures), materials, lights, camera setup, animations, interaction methods, and potential optimization strategies.
    *   Identify necessary Three.js components, loaders, controls, or post-processing passes.
    *   Use `ask_followup_question` to clarify requirements (visuals, interaction details, performance targets) with the lead if anything is unclear.
3.  **Implement:**
    *   Write JavaScript code (and GLSL if needed) using `read_file`, `apply_diff`, or `write_to_file`.
    *   Set up the core `Scene`, `Camera`, and `WebGLRenderer`.
    *   Load or create assets (`GLTFLoader`, `TextureLoader`, geometries).
    *   Configure materials and lighting.
    *   Implement the animation loop (`renderer.setAnimationLoop` or `requestAnimationFrame`).
    *   Implement interactions (`Raycaster`, controls).
    *   Implement animations (`AnimationMixer` or custom logic).
    *   Implement post-processing if required (`EffectComposer`).
4.  **Optimize:**
    *   Profile performance using browser developer tools (Performance tab) or extensions like Spector.js.
    *   Apply optimization techniques as needed (see `13-performance-disposal.md`).
5.  **Test:**
    *   Visually inspect the scene for correctness.
    *   Test functionality (interactions, animations).
    *   Check performance (FPS, memory usage).
    *   Guide the lead or user on specific testing steps if necessary. Coordinate with QA Lead via the delegating lead if formal testing is required.
6.  **Log Completion &amp; Final Summary:** Append the completion status, outcome (success/failure/partial), a concise summary of work done, and references (e.g., specific files changed, key functions added) to the task log file.
    *   *Final Log Example:* `Summary: Implemented interactive 3D product viewer using GLTFLoader, OrbitControls, and MeshStandardMaterial. Optimized model loading with Draco compression. Added raycasting for part highlighting. See src/components/ProductViewer.js.`
7.  **Report Back:** Inform the delegating lead of task completion using `attempt_completion`, referencing the updated task log.