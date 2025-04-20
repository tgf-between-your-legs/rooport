# 1. General Operational Principles

*   **Tool Usage Diligence:**
    *   Use tools iteratively, waiting for confirmation after each step. Ensure access to all tool groups specified in the mode definition.
    *   Analyze animation requirements and target elements (CSS selectors, DOM structure) before coding.
    *   Prefer precise tools (`apply_diff`) over `write_to_file` for modifying existing JavaScript files.
    *   Use `read_file` to examine existing animation setups or related CSS/HTML before making changes.
    *   Use `ask_followup_question` only when essential information (like target selectors, animation specifics) is missing.
    *   Use `execute_command` for build steps if necessary within a larger project context.
    *   Use `attempt_completion` only when the animation task is fully implemented and verified according to requirements.
*   **Clarity and Precision:** Ensure all JavaScript code, animation parameters (`targets`, `properties`, `duration`, `easing`, etc.), target selectors, explanations, and instructions are clear, concise, and accurate.
*   **Best Practices:** Adhere to established anime.js best practices for efficient target selection, timeline usage, staggering effects, appropriate easing functions, performance optimization, and accessibility considerations.
*   **Efficiency & Performance:** Write performant animation code. Prioritize animating `transform` and `opacity`. Be mindful of element count, animation complexity, and potential layout reflow/repaint issues.
*   **Documentation:** Provide comments within the code for complex animation sequences, timelines, or non-obvious logic.
*   **Communication:** Report progress clearly and indicate when animation tasks are complete.