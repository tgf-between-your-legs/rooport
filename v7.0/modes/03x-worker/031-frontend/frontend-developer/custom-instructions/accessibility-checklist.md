# Basic Frontend Accessibility (A11y) Checklist

A quick checklist for fundamental accessibility considerations during frontend development. This is not exhaustive; consult WCAG guidelines and the `accessibility-specialist` for complex issues.

## 1. Semantic HTML

*   [ ] Use HTML tags according to their meaning (`<nav>`, `<main>`, `<article>`, `<button>`, `<h1>`-`<h6>` hierarchically, etc.).
*   [ ] Use landmark roles (`<header>`, `<footer>`, `<main>`, `<nav>`, `<aside>`) appropriately to define page structure.
*   [ ] Use lists (`<ul>`, `<ol>`, `<dl>`) for list content.
*   [ ] Use `<button>` for interactive controls that perform actions, `<a>` for navigation.

## 2. Images

*   [ ] Provide descriptive `alt` text for all informative images (`<img alt="Description of image">`).
*   [ ] Use empty `alt=""` for purely decorative images that don't convey meaning.
*   [ ] If an image is the sole content of a link, the `alt` text must describe the link's destination or purpose.

## 3. Forms

*   [ ] Associate labels explicitly with form controls (`<input>`, `<textarea>`, `<select>`) using `<label for="controlId">` and matching `id="controlId"`.
*   [ ] Group related controls using `<fieldset>` and provide a legend using `<legend>`. (Especially important for radio buttons and checkboxes).
*   [ ] Ensure clear instructions and indicate required fields.
*   [ ] Provide useful error messages linked programmatically to the invalid field (e.g., using `aria-describedby`).

## 4. Keyboard Navigation

*   [ ] Ensure all interactive elements (links, buttons, form controls) are focusable and operable using only the keyboard (typically via Tab, Shift+Tab, Enter, Space).
*   [ ] Ensure the focus order is logical and follows the visual flow.
*   [ ] Ensure a visible focus indicator is present for all focusable elements (don't disable `outline` without providing a clear alternative).
*   [ ] Avoid creating "keyboard traps" where focus cannot leave a component.

## 5. Color & Contrast

*   [ ] Ensure sufficient color contrast between text and its background (WCAG AA requires 4.5:1 for normal text, 3:1 for large text). Use contrast checking tools.
*   [ ] Ensure sufficient contrast for meaningful non-text elements (icons, borders on inputs) (WCAG AA requires 3:1).
*   [ ] Don't rely on color alone to convey information (use text, icons, patterns as well).

## 6. Content & Readability

*   [ ] Use clear and understandable language.
*   [ ] Structure content logically with headings and paragraphs.
*   [ ] Ensure text is resizable up to 200% without loss of content or functionality.

## 7. Dynamic Content & Interactions

*   [ ] If content updates dynamically (e.g., via JavaScript), ensure screen readers are notified if necessary (e.g., using ARIA live regions: `aria-live="polite"` or `aria-live="assertive"`).
*   [ ] Ensure interactive components (like modals, dropdowns, tabs) manage focus correctly and have appropriate ARIA roles and states (`aria-expanded`, `aria-selected`, `aria-hidden`). **Escalate complex components to `accessibility-specialist` via lead.**

## 8. Motion & Animation

*   [ ] Avoid unnecessary animations that could be distracting or cause issues.
*   [ ] Respect the `prefers-reduced-motion` media query to disable or reduce non-essential animations.
*   [ ] Avoid content that flashes more than 3 times per second.

**When in doubt, or for complex components/interactions, report the need for review by the `accessibility-specialist` to your `frontend-lead`.**