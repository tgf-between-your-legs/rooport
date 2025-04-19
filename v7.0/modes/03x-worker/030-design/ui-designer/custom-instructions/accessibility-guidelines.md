# Accessibility (WCAG) Design Guidelines

Key principles from Web Content Accessibility Guidelines (WCAG) to consider during the UI design phase. Aim for WCAG 2.1 AA compliance as a baseline.

## Perceivable

1.  **Text Alternatives:** Provide text alternatives (e.g., `alt` text) for non-text content like images. (Consider during wireframing/mockups).
2.  **Adaptable:** Create content that can be presented in different ways (e.g., simpler layout) without losing information or structure. Use semantic HTML.
3.  **Distinguishable:** Make it easier for users to see and hear content.
    *   **Color Contrast:** Ensure sufficient contrast between text and background (AA requires 4.5:1 for normal text, 3:1 for large text). Use contrast checker tools.
    *   **Don't Rely Solely on Color:** Provide other indicators besides color to convey information (e.g., icons, text labels for status).
    *   **Text Resizing:** Ensure text can be resized up to 200% without loss of content or functionality.
    *   **Audio Control:** If audio plays automatically, provide controls to stop or pause it.

## Operable

4.  **Keyboard Accessible:** All functionality should be operable through a keyboard interface.
    *   **Focus Visible:** Ensure keyboard focus indicators are clearly visible on interactive elements (links, buttons, form fields). Design clear `:focus` states.
    *   **No Keyboard Trap:** Users should never get stuck in a component using only the keyboard.
5.  **Enough Time:** Provide users enough time to read and use content. (Less relevant for static design, more for interactions).
6.  **Seizures and Physical Reactions:** Do not design content in a way that is known to cause seizures (e.g., flashing content).
7.  **Navigable:** Provide ways to help users navigate, find content, and determine where they are.
    *   **Clear Headings & Labels:** Use descriptive headings (`<h1>`-`<h6>`) and labels for form elements.
    *   **Link Purpose:** The purpose of each link should be clear from its text alone or from context.

## Understandable

8.  **Readable:** Make text content readable and understandable.
    *   **Language of Page:** Specify the page language (`<html lang="...">`).
    *   **Predictable:** Make web pages appear and operate in predictable ways. Consistent navigation and component behavior.
9.  **Input Assistance:** Help users avoid and correct mistakes.
    *   **Error Identification:** Clearly identify input errors.
    *   **Labels & Instructions:** Provide clear labels and instructions for forms.
    *   **Error Suggestion:** Suggest corrections if input errors are detected (if possible).

## Robust

10. **Compatible:** Maximize compatibility with current and future user agents, including assistive technologies. (Primarily an implementation concern, but design should use standard patterns).
    *   **Use Semantic HTML:** Structure content correctly using appropriate HTML5 elements (`<nav>`, `<main>`, `<button>`, etc.).

## Design Phase Checklist

*   [ ] Is there sufficient color contrast? (Use checker tool)
*   [ ] Is information conveyed by more than just color?
*   [ ] Are interactive elements clearly identifiable?
*   [ ] Are focus states (`:focus`) clearly designed for all interactive elements?
*   [ ] Is the layout logical and easy to navigate?
*   [ ] Are headings used correctly for structure?
*   [ ] Are form labels clear and associated with inputs?
*   [ ] Is text readable (font choice, size, line height)?
*   [ ] Is the design adaptable to different screen sizes (responsive)?

*(Consult the full WCAG 2.1 guidelines for detailed success criteria: https://www.w3.org/TR/WCAG21/)*