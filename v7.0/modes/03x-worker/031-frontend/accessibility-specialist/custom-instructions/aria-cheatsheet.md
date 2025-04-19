# ARIA (Accessible Rich Internet Applications) Quick Reference

A cheatsheet for common WAI-ARIA roles, states, and properties used to enhance accessibility, especially for dynamic content and custom UI components. **Use semantic HTML first whenever possible.** ARIA should supplement, not replace, native HTML semantics.

## Core Concepts

*   **Roles:** Define the type or purpose of a UI element (widget, landmark, etc.). Added via the `role="..."` attribute.
*   **States:** Describe the current condition of an element (e.g., checked, expanded, disabled). Added via `aria-*` attributes (e.g., `aria-checked="true"`). Often change dynamically with user interaction.
*   **Properties:** Define characteristics or relationships of an element (e.g., labels, descriptions, relationships). Added via `aria-*` attributes (e.g., `aria-label="..."`). Usually less dynamic than states.

## Common Roles

### Widget Roles (for interactive elements)
*   `role="button"`: For elements acting like buttons (e.g., styled `<div>`s). Prefer native `<button>`.
*   `role="checkbox"`: For custom checkboxes. Needs `aria-checked` state.
*   `role="radio"`: For custom radio buttons. Needs `aria-checked`. Use with `role="radiogroup"`.
*   `role="tablist"`, `role="tab"`, `role="tabpanel"`: For tabbed interfaces. Manage `aria-selected` on tabs and visibility of tabpanels.
*   `role="dialog"`, `role="alertdialog"`: For modal dialogs. Manage focus trapping and use `aria-modal="true"`. `alertdialog` implies critical info.
*   `role="link"`: For elements acting like links. Prefer native `<a>`.
*   `role="menu"`, `role="menubar"`, `role="menuitem"`, `role="menuitemcheckbox"`, `role="menuitemradio"`: For custom menus. Requires keyboard navigation handling.
*   `role="slider"`: For slider controls. Needs `aria-valuenow`, `aria-valuemin`, `aria-valuemax`.
*   `role="tooltip"`: For tooltips providing descriptive text. Often linked via `aria-describedby`.

### Landmark Roles (for page structure/navigation)
*   `role="banner"`: Site header (often contains logo, site title, main nav). Use `<header>`.
*   `role="navigation"`: Groups of navigation links. Use `<nav>`.
*   `role="main"`: Main content of the document. Use `<main>`.
*   `role="complementary"`: Supporting section, related but separate from main content. Use `<aside>`.
*   `role="contentinfo"`: Footer information (copyright, privacy links). Use `<footer>`.
*   `role="search"`: Contains search functionality.
*   `role="region"`: A significant section, requires `aria-label` or `aria-labelledby` if generic. Use `<section>` with a heading.
*   `role="form"`: A form section. Use `<form>` with a label.

## Common States & Properties

*   **`aria-label="[text]"`:** Provides an accessible name when no visible label exists. Overrides other naming methods.
*   **`aria-labelledby="[id]"`:** Provides an accessible name by referencing the ID(s) of visible label element(s). Preferred over `aria-label` if visible label exists.
*   **`aria-describedby="[id]"`:** Provides additional description or context by referencing the ID(s) of descriptive element(s).
*   **`aria-hidden="true"`:** Hides the element from assistive technologies. Use carefully (e.g., for purely decorative icons if `alt=""` isn't possible, or offscreen content).
*   **`aria-expanded="true|false"`:** Indicates whether a collapsible element (like accordion header, menu button) is currently expanded or collapsed.
*   **`aria-selected="true|false"`:** Indicates the current selection state of elements within a composite widget (like tabs in a `tablist`).
*   **`aria-checked="true|false|mixed"`:** Indicates the state of a checkbox or radio button.
*   **`aria-disabled="true|false"`:** Indicates an element is interactive but currently disabled. Use native `disabled` attribute on form controls where possible.
*   **`aria-current="page|step|location|date|time|true|false"`:** Indicates the current item within a set (e.g., current page in navigation).
*   **`aria-live="polite|assertive|off"`:** Indicates a region whose content may update dynamically. `polite`: announce when user is idle. `assertive`: announce immediately (interrupts). Use `assertive` sparingly for critical alerts.
*   **`aria-modal="true"`:** Indicates a dialog prevents interaction with content outside it. Requires focus trapping script.
*   **`aria-required="true"`:** Indicates a form field is required. Use native `required` attribute where possible.
*   **`aria-invalid="true|false"`:** Indicates the value entered into a form field is invalid. Often used with `aria-describedby` pointing to an error message.

*(Refer to WAI-ARIA Authoring Practices for detailed implementation patterns: https://www.w3.org/WAI/ARIA/apg/)*