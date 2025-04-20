# UI Design: Accessibility (WCAG) Checklist

Key accessibility considerations for UI designers based on WCAG (Web Content Accessibility Guidelines).

**(Note: This is a simplified checklist for designers. Implementation details often fall to developers and accessibility specialists.)**

## POUR Principles

WCAG is organized around four main principles:

1.  **Perceivable:** Information and UI components must be presentable to users in ways they can perceive.
2.  **Operable:** UI components and navigation must be operable.
3.  **Understandable:** Information and the operation of the UI must be understandable.
4.  **Robust:** Content must be robust enough that it can be interpreted reliably by a wide variety of user agents, including assistive technologies.

## Design Checklist Items

### Perceivable

*   **Color Contrast (WCAG 1.4.3 AA / 1.4.6 AAA):**
    *   [ ] Ensure sufficient contrast between text color and background color. (AA: 4.5:1 for normal text, 3:1 for large text. AAA is stricter).
    *   [ ] Ensure sufficient contrast for UI components and graphical elements (e.g., button borders, input borders) against their background (AA: 3:1).
    *   **Tools:** Use contrast checker tools (browser extensions, Figma plugins, online checkers).
*   **Don't Rely Solely on Color (WCAG 1.4.1):**
    *   [ ] Don't use color alone to convey information, indicate an action, prompt a response, or distinguish a visual element. Provide additional cues (text labels, icons, patterns, underlines).
    *   *Example:* Don't just make error text red; add an error icon or prefix like "Error:". Don't just rely on link color; ensure links are underlined (especially in body text).
*   **Text Resizing (WCAG 1.4.4):**
    *   [ ] Design layouts that can accommodate text resized up to 200% without loss of content or functionality (handled mainly in development, but design should allow flexibility).
*   **Visual Presentation (General):**
    *   [ ] Ensure clear visual hierarchy.
    *   [ ] Use adequate spacing between elements.
    *   [ ] Choose readable fonts and appropriate font sizes.

### Operable

*   **Keyboard Navigation (WCAG 2.1.1):**
    *   [ ] Ensure all interactive elements (links, buttons, form fields, custom components) are conceptually reachable and operable via keyboard alone. (Implementation detail, but design should consider).
    *   [ ] Design clear visual focus indicators (`:focus-visible`) for all interactive elements. Ensure focus states have sufficient contrast. (WCAG 2.4.7)
*   **Clear Navigation & Headings (WCAG 2.4.6 / 2.4.1):**
    *   [ ] Use clear, descriptive headings to structure content logically.
    *   [ ] Ensure navigation menus are consistent and easy to understand.
    *   [ ] Provide clear link text that describes the destination or purpose. (WCAG 2.4.4)
*   **Touch Target Size (WCAG 2.5.5 - AAA):**
    *   [ ] Ensure interactive elements have a target size of at least 44x44 CSS pixels (or sufficient spacing) for touch interaction. (While AAA, good practice).
*   **No Timing (WCAG 2.2.1):**
    *   [ ] Avoid imposing time limits for tasks unless essential (or provide ways to extend/disable them). (Less common for pure UI design, but relevant for flows).
*   **Animations & Motion (WCAG 2.2.2):**
    *   [ ] Avoid unnecessary animations or motion that could trigger seizures (no flashing more than 3 times per second).
    *   [ ] Provide mechanisms to pause, stop, or hide non-essential animations (e.g., carousels, background videos).

### Understandable

*   **Readability (WCAG 3.1.5 - AAA):**
    *   [ ] Use clear and simple language appropriate for the audience.
    *   [ ] Ensure text line length is not excessive for comfortable reading.
*   **Consistent Navigation & Identification (WCAG 3.2.3 / 3.2.4):**
    *   [ ] Maintain consistent placement and behavior of navigation elements and key components across pages.
*   **Labels & Instructions (WCAG 3.3.2):**
    *   [ ] Provide clear labels or instructions for form inputs and controls.
*   **Error Identification & Suggestion (WCAG 3.3.1 / 3.3.3):**
    *   [ ] Clearly indicate input errors visually and textually.
    *   [ ] Provide helpful suggestions for correcting errors if possible.

### Robust

*   **(Primarily Development):** This principle mostly relates to using standard HTML semantics and ARIA attributes correctly so assistive technologies can interpret the content.
*   **Design Consideration:** Design components with clear semantic purpose in mind (e.g., design something that *looks* and *acts* like a button, so developers implement it as `<button>`).

## Documentation

*   Annotate mockups or design specifications with accessibility notes (e.g., "Focus state: blue ring", "Contrast ratio: 5.5:1", "Requires ARIA label: 'Close dialog'").
*   Collaborate with `accessibility-specialist` for reviews and complex cases.

*(Refer to the official WCAG guidelines for detailed success criteria: https://www.w3.org/TR/WCAG21/)*