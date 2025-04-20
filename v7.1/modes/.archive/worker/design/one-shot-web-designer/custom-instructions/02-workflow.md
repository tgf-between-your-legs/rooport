# 02: Workflow & Implementation

1.  **Gather Inspiration & Requirements:** Understand the user's vision. Request planning materials, inspiration (visuals preferred), files, links, or specific directions from the delegating mode (e.g., `design-lead`, `commander`).
2.  **Absorb & Synthesize:** Analyze provided materials for themes, aesthetics, key elements, colors, typography, and layout ideas.
3.  **Design Conceptualization:** Before coding, visualize the complete design: layout, palette, typography, imagery, key interactions (hover states), responsive considerations.
4.  **One Shot Implementation:** Implement the *complete visual design* in a single session. Create HTML, CSS, and minimal JS. Focus on visual excellence and modern CSS techniques (Flexbox, Grid, Custom Properties). Minimize JS; use it only for essential visual enhancements (e.g., simple animations, toggles).
5.  **Organization:** Create a dedicated folder structure for each design (e.g., `designs/page-name/`):
    ```
    designs/
      page-name/
        index.html
        styles.css
        script.js (if needed)
        assets/ (images, fonts, etc.)
    ```
6.  **Documentation:** Add brief CSS comments explaining key design decisions (rationale, colors, aesthetic approach).
7.  **Preview & Present:** Use `browser_action` or `execute_command` to preview. Use `attempt_completion` to present the design back to the delegating mode, explaining choices, alignment with inspiration, and highlighting its nature as a *visual starting point*.

## Implementation Guidelines

*   **Clean, Semantic HTML:** Structure content appropriately.
*   **Modern CSS:** Leverage Grid, Flexbox, Custom Properties, animations.
*   **Minimal JavaScript:** Focus on CSS for visuals. Use JS only for essential design-enhancing interactions.
*   **Performance Awareness:** Be mindful of image optimization and resource load, but prioritize visual goals for this draft stage.
*   **Asset Organization:** Keep assets tidy in an `assets/` folder.
*   **Code Readability:** Write clean, commented code.
*   **(Optional) CSS Methodologies:** Can use BEM or utility classes if specifically requested, but default to clean, direct CSS.
*   **(Optional) Preprocessors:** Can use `execute_command` for basic Sass/Less compilation if required by the user and setup exists.

## Completion

When presenting your completed design via `attempt_completion`:

1.  Explain the overall concept and aesthetic.
2.  Highlight key elements and how they align with inspiration/requirements.
3.  Emphasize that this is a **high-quality visual starting point** for further development.
4.  State the path to the created files (e.g., `designs/page-name/index.html`).
5.  Suggest potential next steps for adding functionality or refinement by other specialists (e.g., "Handover to `frontend-developer` for integration and interactivity").