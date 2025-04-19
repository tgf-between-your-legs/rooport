# ARIA: Common Patterns & Attributes

Examples of using WAI-ARIA (Accessible Rich Internet Applications) roles, states, and properties to enhance accessibility for dynamic content and custom controls.

## Core Concept

ARIA provides attributes to add semantics and context to HTML elements, making web content and applications more accessible to people using assistive technologies (AT), especially when standard HTML semantics are insufficient (e.g., for custom JavaScript widgets).

**Key Principles:**

1.  **Use Native HTML First:** Prefer using standard HTML elements (`<button>`, `<nav>`, `<input type="checkbox">`, etc.) with their built-in semantics and keyboard behavior whenever possible. ARIA should supplement, not replace, native HTML semantics where they exist.
2.  **Don't Change Native Semantics:** Avoid adding ARIA roles that contradict the element's native role (e.g., don't put `role="button"` on an `<h1>`).
3.  **Ensure Keyboard Accessibility:** All interactive ARIA controls must be keyboard operable.
4.  **Manage Focus:** Ensure focus is appropriately managed for interactive controls, especially custom widgets.
5.  **Expose States & Properties:** Use ARIA state and property attributes (e.g., `aria-expanded`, `aria-selected`, `aria-disabled`, `aria-current`) to convey the current status of interactive elements.

## Common ARIA Roles

*   **Landmark Roles:** Define major regions of the page. Assistive technologies use these for navigation.
    *   `role="banner"` (Site header, often on `<header>`)
    *   `role="navigation"` (Main navigation links, often on `<nav>`)
    *   `role="main"` (Main content of the page, often on `<main>`)
    *   `role="complementary"` (Supporting content, often on `<aside>`)
    *   `role="contentinfo"` (Site footer info, often on `<footer>`)
    *   `role="search"` (Search form/widget)
    *   `role="region"` (Generic landmark, use with `aria-labelledby` if it needs a name)
*   **Widget Roles:** Define common interactive patterns. Often require JavaScript for behavior and state management.
    *   `role="button"` (For elements acting like buttons, e.g., `<div>` or `<span>` made clickable via JS. Native `<button>` is preferred).
    *   `role="checkbox"`, `role="radio"` (For custom styled checkboxes/radios. Need `aria-checked`).
    *   `role="tablist"`, `role="tab"`, `role="tabpanel"` (For tabbed interfaces).
    *   `role="dialog"`, `role="alertdialog"` (For modal dialogs. Need focus management and `aria-modal="true"`).
    *   `role="alert"` (For important, time-sensitive messages. Often used with `aria-live`).
    *   `role="status"` (For less critical status messages. Often used with `aria-live`).
    *   `role="menu"`, `role="menubar"`, `role="menuitem"`, `role="menuitemcheckbox"`, `role="menuitemradio"` (For application menus).
    *   `role="link"` (For elements acting like links. Native `<a>` is preferred).
    *   `role="slider"`, `role="spinbutton"` (For custom input widgets).
    *   `role="tooltip"` (For contextual help text).
*   **Document Structure Roles:** (Less common, often covered by HTML) `role="article"`, `role="document"`, `role="heading"`, `role="list"`, `role="listitem"`, `role="table"`, etc.

## Common ARIA States and Properties

*   **`aria-label="Visible label text"`:** Provides an accessible name when no visible label exists or the visible label isn't sufficient. Overrides element content for AT.
*   **`aria-labelledby="id_of_labeling_element"`:** Provides an accessible name by referencing the ID(s) of visible element(s) that act as the label. Preferred over `aria-label` if a visible label exists.
*   **`aria-describedby="id_of_describing_element"`:** Provides additional description or instructions by referencing the ID(s) of element(s) containing the description. Read after the label/content.
*   **`aria-hidden="true"`:** Hides the element and its children from assistive technologies (but not visually). Use carefully.
*   **`aria-disabled="true"`:** Indicates an element is interactive but currently disabled.
*   **`aria-expanded="true|false"`:** Indicates whether a grouping element (like a menu button or accordion header) is currently expanded or collapsed.
*   **`aria-haspopup="true|menu|listbox|tree|grid|dialog"`:** Indicates the element triggers a popup component.
*   **`aria-controls="id_of_controlled_element"`:** Indicates the element controls another element (e.g., a tab controls a tabpanel).
*   **`aria-selected="true|false"`:** Indicates the current selection state of elements within a composite widget (e.g., tabs in a tablist).
*   **`aria-checked="true|false|mixed"`:** Indicates the state of a checkbox or radio button.
*   **`aria-pressed="true|false|mixed"`:** Indicates the state of a toggle button.
*   **`aria-current="page|step|location|date|time|true"`:** Indicates the element represents the current item within a set (e.g., current page in navigation).
*   **`aria-live="polite|assertive"`:** Indicates a region whose content may update dynamically. `polite`: AT announces changes when idle. `assertive`: AT interrupts user to announce changes immediately (use sparingly). Often used with `role="alert"` or `role="status"`.
*   **`aria-atomic="true|false"`:** Used with `aria-live`. If `true`, AT reads the entire live region content when any part changes. If `false` (default), only the changed node is typically announced.
*   **`aria-relevant="additions|removals|text|all"`:** Used with `aria-live`. Indicates what types of changes within the live region should be announced. Default is `additions text`.
*   **`aria-modal="true"`:** Used on dialogs (`role="dialog"` or `role="alertdialog"`) to indicate that content outside the dialog is inert. Requires JS to manage focus trapping.
*   **`role="presentation"` or `role="none"`:** Removes the semantic meaning of an element (e.g., making a `<table>` used purely for layout not be announced as a table). Use native elements correctly first.

## Examples

**Custom Button:**

```html
<span role="button" tabindex="0" aria-label="Close" onclick="..." onkeydown="...">X</span>
<!-- Better: <button aria-label="Close" onclick="...">X</button> -->
```

**Accordion Header:**

```html
<h3>
  <button aria-expanded="false" aria-controls="section1">Section 1 Title</button>
</h3>
<div id="section1" role="region" aria-labelledby="section1-title" hidden>
  <p>Content for section 1...</p>
</div>
<!-- JS needed to toggle aria-expanded and hidden attribute -->
```

**Alert Message:**

```html
<div role="alert" aria-live="assertive">
  Your session will expire soon.
</div>
<!-- Content added dynamically via JS -->
```

**Form Field with Description:**

```html
<label for="pwd">Password:</label>
<input type="password" id="pwd" aria-describedby="pwd-hint">
<span id="pwd-hint">Must be at least 8 characters long.</span>
```

Use ARIA thoughtfully to bridge gaps in HTML semantics, especially for custom interactive components, ensuring they are understandable and operable via assistive technologies.

*(Refer to the WAI-ARIA Authoring Practices: https://www.w3.org/WAI/ARIA/apg/)*