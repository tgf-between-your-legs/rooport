# Accessibility (A11y): Basic Checklist

Fundamental checks for improving web accessibility in core HTML, CSS, and JS development. This is not exhaustive; complex issues require the `accessibility-specialist`. Aim for WCAG AA compliance where feasible within the scope of generalist work.

## Core Principles (POUR)

*   **Perceivable:** Information and UI must be presentable in ways users can perceive (e.g., alt text, captions, contrast).
*   **Operable:** UI components and navigation must be operable (e.g., keyboard access, sufficient time, no seizure triggers).
*   **Understandable:** Information and UI operation must be understandable (e.g., clear language, predictable navigation, helpful errors).
*   **Robust:** Content must be reliably interpretable by various user agents, including assistive technologies (use valid HTML/CSS, standard patterns).

## Basic Checklist

**1. Semantic HTML:**
*   [ ] Use HTML elements for their intended purpose (`<nav>`, `<main>`, `<button>`, `<h1>`-`<h6>` hierarchically, etc.). (See `02-html-semantics.md`)
*   [ ] Use landmark elements (`<header>`, `<nav>`, `<main>`, `<aside>`, `<footer>`) appropriately.
*   [ ] Ensure page has a descriptive `<title>`.
*   [ ] Set the language attribute (`<html lang="en">`).

**2. Images:**
*   [ ] Provide descriptive `alt` text for all informative `<img>` elements (`alt="Description"`).
*   [ ] Use empty `alt=""` for purely decorative images.
*   [ ] If an image is the only content of a link, `alt` text must describe the link's destination/function.

**3. Links:**
*   [ ] Link text should be descriptive and make sense out of context (avoid "Click Here").
*   [ ] Ensure links have a clear visual focus indicator (`:focus`, `:focus-visible`).

**4. Forms:**
*   [ ] Every form control (`<input>`, `<textarea>`, `<select>`) must have an associated `<label>` using `for` matching the control's `id`.
    ```html
    <label for="user-email">Email:</label>
    <input type="email" id="user-email" name="email">
    ```
*   [ ] Group related controls (radio buttons, checkboxes) using `<fieldset>` and `<legend>`.
*   [ ] Indicate required fields clearly (visually and programmatically via `required` attribute, potentially `aria-required="true"`).
*   [ ] Provide clear instructions and helpful error messages (associate errors with inputs using `aria-describedby` if needed - consult specialist for complex forms).

**5. Keyboard Navigation:**
*   [ ] Ensure all interactive elements (links, buttons, form controls) are reachable and operable using only the keyboard (Tab, Shift+Tab, Enter, Space).
*   [ ] Ensure the focus order is logical and follows the visual flow.
*   [ ] Ensure interactive elements have a clear visual focus indicator (don't disable `outline` without a clear alternative).
*   [ ] Avoid "keyboard traps" where focus gets stuck.

**6. Color & Contrast:**
*   [ ] Ensure sufficient color contrast between text and background (WCAG AA: 4.5:1 normal text, 3:1 large text). Use online contrast checkers.
*   [ ] Ensure sufficient contrast for meaningful non-text elements (icons, input borders) (WCAG AA: 3:1).
*   [ ] Do not rely solely on color to convey information (use icons, text labels, patterns).

**7. Content & Readability:**
*   [ ] Use headings (`<h1>`-`<h6>`) correctly to structure content hierarchically.
*   [ ] Use lists (`<ul>`, `<ol>`) for list content.
*   [ ] Ensure text is resizable (e.g., up to 200%) without breaking layout significantly or loss of content/functionality.
*   [ ] Use clear and understandable language.

**8. Dynamic Content & Interactions (Basic):**
*   [ ] If content updates dynamically, ensure screen readers are notified if necessary (basic cases might use `aria-live="polite"`). Escalate complex cases.
*   [ ] Basic interactive components should manage focus appropriately. Escalate complex components (modals, tabs, custom selects).

**9. Motion & Animation:**
*   [ ] Avoid unnecessary or potentially triggering animations (flashing > 3 times/sec).
*   [ ] Consider respecting the `prefers-reduced-motion` media query.

## When to Escalate to `frontend-lead` (Suggesting `accessibility-specialist`)

*   Complex custom widgets/interactions (modals, tabs, carousels, custom selects, autocomplete).
*   Implementing ARIA live regions for complex dynamic updates.
*   Complex form validation and error association (linking errors to inputs programmatically).
*   Video/audio captions, transcripts, or audio descriptions.
*   Full accessibility audits or addressing specific WCAG criteria beyond these basics.
*   Implementing advanced focus management techniques.
*   Uncertainty about implementing specific WCAG criteria correctly.

Building with accessibility in mind from the start is crucial and often easier than retrofitting.