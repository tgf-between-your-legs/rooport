# UI Design: Documenting Designs in Markdown

Best practices for creating clear and effective design specifications using Markdown.

## Goal

To provide developers, QAs, and other stakeholders with a clear understanding of the designed user interface, including its structure, appearance, behavior, and rationale, in a text-based format.

## Key Elements of Design Documentation

1.  **Overview & Goal:**
    *   Briefly describe the feature or screen being designed.
    *   State the primary user goal or problem this design solves.
    *   Link to related requirements documents or user stories.

2.  **Wireframes/Mockups (Descriptive):**
    *   Use Markdown headings, lists, and potentially simple ASCII diagrams or Mermaid syntax (if supported by the viewer) to describe the layout and structure.
    *   Reference the `wireframing-mockups.md` guide for detailed instructions on describing low-fidelity and high-fidelity views.
    *   Clearly label sections and key components.

3.  **Visual Specifications:**
    *   **Reference Style Guide:** Explicitly link to or reference the project's main style guide or design system document.
    *   **Component Usage:** List the specific components used (e.g., "Primary Button", "Standard Card", "Modal Dialog") and any variants applied.
    *   **Overrides/Customizations:** Detail any deviations from the standard style guide for this specific design (e.g., "Use `color-warning` for the border here instead of default", "Increased padding to `p-8` in this section").
    *   **Typography:** Specify font usage (family, size, weight) if deviating from standard component styles or for unique text elements.
    *   **Spacing:** Describe key margins, padding, or grid gaps, preferably using defined spacing units from the style guide.
    *   **Imagery/Icons:** Specify required images or icons, including names, sources, or descriptions.

4.  **Interaction & Behavior:**
    *   **User Flows:** Describe key user flows step-by-step (see `prototyping-interactions.md`).
    *   **Component States:** Detail the appearance and behavior for different states (hover, focus, active, disabled, loading, error) of interactive elements.
    *   **Micro-interactions/Animations:** Describe any specific transitions or animations (type, duration, easing).

5.  **Responsiveness:**
    *   Explain how the layout adapts at different breakpoints (see `responsive-design.md`).
    *   Note any elements that change, appear, or disappear on different screen sizes.

6.  **Accessibility:**
    *   Include specific accessibility annotations (see `accessibility-wcag.md`).
    *   Mention required ARIA attributes (even if implemented by developers, noting the need is helpful).
    *   Specify focus order if it's non-obvious.
    *   Note color contrast considerations.
    *   Describe alternative text for images if not self-explanatory.

7.  **Assets (Links):**
    *   If applicable, provide links to relevant assets (SVGs, image files, font files) stored elsewhere in the project or externally.

## Markdown Formatting Tips

*   **Structure:** Use headings (`#`, `##`, `###`) logically to structure the document by screen, section, or component.
*   **Lists:** Use bulleted (`*`, `-`) or numbered (`1.`) lists for elements, steps, or specifications.
*   **Emphasis:** Use bold (`**text**`) for key terms or labels, and italics (`*text*`) for notes or emphasis.
*   **Code Formatting:** Use backticks (`` `code` ``) for code references (like CSS classes, component names, color variables) and triple backticks (```) for code blocks (HTML snippets, CSS rules).
*   **Tables:** Use Markdown tables for structured data like color palettes or spacing scales.
*   **Links:** Use standard Markdown links (`[text](url)`) to reference style guides, requirements, assets, or external resources.
*   **Emojis:** Use standard emojis judiciously to add visual cues (e.g., ✅ for Do, ❌ for Don't, 🎨 for color, ⌨️ for keyboard interaction, ♿ for accessibility).

## Example Snippet (Component Spec)

```markdown
### Component: Search Input

*   **Description:** Standard input field used for site search.
*   **Visual:**
    *   Uses `Input` base component from style guide.
    *   Size: `medium`.
    *   Placeholder Text: "Search..." (`text-gray-400`).
    *   Icon: Include `icon-search` (18px, `text-gray-500`) aligned to the left inside the input padding.
*   **States:**
    *   `Default`: Standard input styles.
    *   `Focus`: Border changes to `border-primary`, subtle `ring` effect.
    *   `With Value`: Placeholder disappears. Optional: Show clear 'X' icon on right when value exists.
*   **Interaction:**
    *   Typing updates input value.
    *   Pressing 'Enter' triggers search action.
    *   Clicking 'X' icon (if present) clears the input field and refocuses it.
*   **Accessibility:**
    *   ♿ Associated `<label>` (visually hidden or explicit) with `htmlFor` pointing to input `id`.
    *   ♿ Focus state clearly visible.
```

Clear, well-structured Markdown documentation serves as an effective communication tool between design and development.