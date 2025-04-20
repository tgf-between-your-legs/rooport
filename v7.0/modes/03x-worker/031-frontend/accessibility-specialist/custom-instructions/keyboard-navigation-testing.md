# Accessibility: Keyboard Navigation Testing Checklist

Manual checks to ensure content and functionality are fully operable via keyboard alone.

## Core Principles (WCAG)

*   **2.1.1 Keyboard (Level A):** All functionality available via keyboard.
*   **2.1.2 No Keyboard Trap (Level A):** User can always navigate *away* from any component using only the keyboard (typically `Tab`, `Shift+Tab`, `Esc`).
*   **2.4.3 Focus Order (Level A):** Navigation order is logical and predictable, usually matching the visual flow.
*   **2.4.7 Focus Visible (Level AA):** The component currently receiving keyboard focus has a clear visual indicator.

## Testing Steps

**Environment:** Use a standard browser (Chrome, Firefox, Edge, Safari) without any assistive technology running initially. Use only the keyboard for navigation.

**Key Controls:**

*   **`Tab`:** Move focus to the next focusable element (links, buttons, form inputs, elements with `tabindex="0"`).
*   **`Shift + Tab`:** Move focus to the previous focusable element.
*   **`Enter`:** Activate links and buttons. Submit forms (sometimes).
*   **`Space`:** Activate buttons, toggle checkboxes/radio buttons.
*   **Arrow Keys (`Up`, `Down`, `Left`, `Right`):** Navigate within composite widgets like menus, radio groups, sliders, grids, tree views (behavior depends on the widget pattern).
*   **`Esc`:** Dismiss menus, dialogs, or popups.
*   **`Home`, `End`, `PageUp`, `PageDown`:** Sometimes used within specific widgets (e.g., scrolling content, moving to start/end of lists/grids).

**Checklist:**

1.  **Can I reach everything?**
    *   [ ] Can you `Tab` to *every* interactive element (links, buttons, form fields, custom controls)?
    *   [ ] Can you `Shift+Tab` backwards through all interactive elements?
    *   [ ] Are any interactive elements skipped or inaccessible? (Common with non-semantic elements like `<div>` used as buttons without `tabindex="0"`).
2.  **Is the focus order logical?**
    *   [ ] Does the `Tab` order generally follow the visual reading order (e.g., left-to-right, top-to-bottom in LTR languages)?
    *   [ ] Does the focus move predictably, without unexpected jumps?
    *   [ ] When a modal dialog (`role="dialog"`) opens, does focus move *into* the dialog?
    *   [ ] When a modal dialog closes, does focus return to the element that triggered it?
3.  **Is the focus visible?**
    *   [ ] Is there a clear visual indicator (outline, background change, underline) showing which element currently has focus? (Check browser default styles and custom CSS `:focus` / `:focus-visible` rules).
    *   [ ] Is the focus indicator sufficiently visible against its background (consider contrast)?
4.  **Can I operate everything?**
    *   [ ] Can links be activated using `Enter`?
    *   [ ] Can buttons be activated using `Enter` and `Space`?
    *   [ ] Can checkboxes be toggled using `Space`?
    *   [ ] Can radio buttons within a group be navigated using arrow keys and selected using `Space`?
    *   [ ] Can `<select>` dropdowns be opened (`Enter` or `Space` or `Alt+DownArrow`) and options selected (arrow keys, `Enter`)?
    *   [ ] Can custom widgets (sliders, tabs, menus, tree views) be fully operated using standard keyboard patterns (often arrow keys, `Enter`, `Space`, `Esc`)? (Refer to ARIA Authoring Practices Guide for expected patterns).
5.  **Is there a keyboard trap?**
    *   [ ] Can you always `Tab` or `Shift+Tab` *out* of every component?
    *   [ ] Are there any components (especially complex widgets or embedded `<iframe>`s) where focus gets stuck?
    *   [ ] Can modal dialogs be closed using `Esc`?
6.  **Are character key shortcuts handled correctly? (WCAG 2.1.4)**
    *   [ ] If single-character keys trigger actions, is there a way to disable or remap them? (Less common, but important if present).
    *   [ ] Or, do they only activate when a specific component has focus?

**Common Failures:**

*   Clickable `<div>` or `<span>` elements without `tabindex="0"` or appropriate `role`.
*   Missing or low-contrast focus indicators (`outline: none;` in CSS is a common culprit).
*   Illogical focus order due to DOM structure not matching visual layout, or incorrect use of `tabindex` with positive values.
*   Custom widgets not implementing keyboard interaction patterns correctly.
*   Modal dialogs not trapping focus correctly or not returning focus on close.
*   Keyboard traps within iframes or complex plugins.

Keyboard testing is fundamental for ensuring basic operability for users who cannot use a mouse and for screen reader users.