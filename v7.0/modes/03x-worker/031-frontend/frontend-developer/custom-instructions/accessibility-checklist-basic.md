# Accessibility (a11y): Basic Checklist

Fundamental checks for improving web accessibility in core HTML, CSS, and JS development. This is not exhaustive; complex issues require the `accessibility-specialist`.

## Core Principles (POUR)

*   **Perceivable:** Information and UI components must be presentable to users in ways they can perceive (e.g., alt text for images, captions for media, sufficient color contrast).
*   **Operable:** UI components and navigation must be operable (e.g., keyboard navigation, sufficient time limits, no seizure triggers).
*   **Understandable:** Information and the operation of the UI must be understandable (e.g., clear language, predictable navigation, consistent layout, helpful error messages).
*   **Robust:** Content must be robust enough that it can be interpreted reliably by a wide variety of user agents, including assistive technologies. (Primarily means using valid HTML/CSS and standard patterns).

## Basic Checklist

**1. Semantic HTML:**

*   [ ] Use HTML elements for their intended purpose (`<nav>`, `<main>`, `<button>`, `<h1>`-`<h6>` hierarchically, etc.). (See `html-semantic-elements.md`)
*   [ ] Use landmark elements (`<header>`, `<nav>`, `<main>`, `<aside>`, `<footer>`) appropriately to define page regions.
*   [ ] Ensure page has a descriptive `<title>`.
*   [ ] Set the language attribute (`<html lang="en">`).

**2. Images:**

*   [ ] Provide descriptive `alt` text for all informative `<img>` elements (`alt="Description of image"`).
*   [ ] Use empty `alt=""` for purely decorative images that screen readers should ignore.
*   [ ] If an image is the only content of a link, the `alt` text must describe the link's destination or function.

**3. Links:**

*   [ ] Link text should be descriptive and make sense out of context (avoid "Click Here").
*   [ ] Ensure links have a clear visual focus indicator (`:focus` or `:focus-visible` style).

**4. Forms:**

*   [ ] Every form control (`<input>`, `<textarea>`, `<select>`) must have an associated `<label>` using the `for` attribute matching the control's `id`.
    ```html
    <label for="user-email">Email:</label>
    <input type="email" id="user-email" name="email">
    ```
*   [ ] Group related controls (like radio buttons or checkboxes) using `<fieldset>` and provide a caption with `<legend>`.
*   [ ] Indicate required fields clearly (visually and programmatically, e.g., using `required` attribute and potentially `aria-required="true"`).
*   [ ] Provide clear instructions and helpful error messages (associate errors with inputs using `aria-describedby` if needed for complex forms - consult specialist).

**5. Keyboard Navigation:**

*   [ ] Ensure all interactive elements (links, buttons, form controls) are reachable and operable using only the keyboard (typically via `Tab` key).
*   [ ] Ensure the focus order is logical and follows the visual flow.
*   [ ] Ensure interactive elements have a clear visual focus indicator (browser default or custom `:focus`/`:focus-visible` style).
*   [ ] Avoid "keyboard traps" where focus gets stuck in an element.

**6. Color & Contrast:**

*   [ ] Ensure sufficient color contrast between text and its background (WCAG AA: 4.5:1 for normal text, 3:1 for large text). Use online contrast checkers.
*   [ ] Do not rely solely on color to convey information (e.g., use icons, text labels, or patterns in addition to color for status indicators or chart data).

**7. Basic Structure & Readability:**

*   [ ] Use headings (`<h1>`-`<h6>`) correctly to structure content hierarchically.
*   [ ] Use lists (`<ul>`, `<ol>`) for list content.
*   [ ] Ensure text is resizable without breaking layout significantly.

**When to Escalate:**

This checklist covers fundamentals. Escalate to `frontend-lead` (suggesting `accessibility-specialist`) for:

*   Complex custom widgets or interactions (modals, tabs, carousels, custom selects).
*   Dynamic content updates requiring ARIA live regions.
*   Complex form validation and error association.
*   Video/audio captions and transcripts.
*   Full accessibility audits.
*   Uncertainty about implementing specific WCAG criteria.

Building with accessibility in mind from the start is easier than retrofitting it later.