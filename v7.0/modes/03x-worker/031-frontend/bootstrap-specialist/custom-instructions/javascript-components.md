# Bootstrap JavaScript Components & Dependencies

Notes on using Bootstrap's JavaScript components and managing dependencies.

## Core Requirement: Popper.js

*   **Purpose:** Popper.js is required for positioning elements like dropdowns, tooltips, and popovers correctly.
*   **Version:**
    *   **Bootstrap 5:** Requires **Popper.js v2.x**.
    *   **Bootstrap 4:** Requires **Popper.js v1.x**.
*   **Inclusion:** Ensure Popper.js is included *before* Bootstrap's JavaScript.
    *   **Using Bootstrap Bundle:** The `bootstrap.bundle.min.js` file **includes** Popper.js. If you use this, you don't need to include Popper separately.
        ```html
        <!-- Bootstrap 5 Bundle (includes Popper) -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>

        <!-- Bootstrap 4 Bundle (includes Popper v1) -->
        <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.min.js"></script>
        <!-- OR -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"></script>
        ```
    *   **Using Separate Files:** If using `bootstrap.min.js` (without "bundle"), you must include Popper.js separately *before* it.
        ```html
        <!-- Bootstrap 5 Separate + Popper v2 -->
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js"></script>
        ```

## Bootstrap 4 Requirement: jQuery

*   **Bootstrap 4** JavaScript components require **jQuery** (slim version is usually sufficient). Include it *before* Popper.js and Bootstrap JS.
*   **Bootstrap 5** does **NOT** require jQuery.

## Initialization Methods

1.  **Via `data-*` Attributes (Recommended for Simplicity):**
    *   Most components can be initialized and controlled using `data-bs-*` attributes (v5) or `data-*` attributes (v4) directly in HTML.
    *   *Example (v5 Modal Trigger):* `data-bs-toggle="modal" data-bs-target="#myModal"`
    *   *Example (v4 Tooltip Trigger):* `data-toggle="tooltip" title="My Tooltip"` (Requires JS initialization - see below)
2.  **Via JavaScript:**
    *   You can initialize components manually using JavaScript, which offers more control.
    *   **Get Instance (v5):** `bootstrap.Modal.getOrCreateInstance(element)`
    *   **Initialize (v4):** `$('#myTooltip').tooltip()` (Requires jQuery)
    *   **Methods:** Call methods on the instance (e.g., `myModal.show()`, `myModal.hide()`, `$('#myTooltip').tooltip('show')`).

## Common Components Requiring JS

*   **Alerts (Dismissing):** `data-bs-dismiss="alert"` (v5), `data-dismiss="alert"` (v4)
*   **Collapse:** `data-bs-toggle="collapse"` (v5), `data-toggle="collapse"` (v4)
*   **Dropdowns:** `data-bs-toggle="dropdown"` (v5), `data-toggle="dropdown"` (v4) - Requires Popper.js.
*   **Modals:** `data-bs-toggle="modal"` (v5), `data-toggle="modal"` (v4)
*   **Popovers:** `data-bs-toggle="popover"` (v5), `data-toggle="popover"` (v4) - Requires Popper.js and JS initialization.
*   **Scrollspy:** Requires JS initialization and specific HTML structure.
*   **Tabs:** `data-bs-toggle="tab"` (v5), `data-toggle="tab"` (v4)
*   **Toasts:** Requires JS initialization (`new bootstrap.Toast(element)`) and specific HTML structure.
*   **Tooltips:** `data-bs-toggle="tooltip"` (v5), `data-toggle="tooltip"` (v4) - Requires Popper.js and JS initialization.

## JS Initialization Example (v5 Tooltips)

Even with `data-bs-*` attributes, Tooltips and Popovers need explicit initialization for performance reasons.

```html
<button type="button" class="btn btn-secondary"
        data-bs-toggle="tooltip" data-bs-placement="top"
        title="Tooltip on top">
  Tooltip on top
</button>
```

```javascript
// Initialize all tooltips on the page
const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));
```

*(Always check the specific component documentation for the target Bootstrap version regarding JavaScript usage and dependencies.)*