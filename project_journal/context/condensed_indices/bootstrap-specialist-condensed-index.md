## Bootstrap v5.3.3 - Condensed Context Index

### Overall Purpose

Bootstrap is a popular, open-source front-end framework for developing responsive, mobile-first websites and web applications quickly. It provides a collection of pre-built CSS and JavaScript components, a powerful grid system, utility classes, and Sass variables/mixins for rapid development and customization.

### Core Concepts & Capabilities

*   **Setup & Configuration:** Includes methods for adding Bootstrap (CDN, npm, Webpack), essential HTML structure (`<!doctype html>`, `<meta name="viewport">`), and customization via Sass variables (`$primary`, `$spacer`) or CSS variables (`--bs-blue`). Supports Dark Mode (`data-bs-theme="dark"`).
*   **Layout System:** Features a responsive 12-column Grid (`.container`, `.row`, `.col-*`) for structuring content across different screen sizes. Includes Flexbox utilities (`.d-flex`, `align-items-*`, `justify-content-*`) for fine-grained control over alignment and distribution.
*   **Core Components:** Offers ready-made UI elements like Forms (`.form-control`, validation), Buttons (`.btn`, `.btn-*`), Navbars (`.navbar`), Cards (`.card`), Modals (`.modal`), Accordions (`.accordion`), Button Groups (`.btn-group`), and Input Groups (`.input-group`).
*   **Utilities:** Provides helper classes for common styling needs like spacing (`.m-*`, `.p-*`), colors (`.text-*`, `.bg-*`), borders, display, position, and visibility (`.visually-hidden` for accessibility).
*   **JavaScript Integration:** Components like Modals, Dropdowns, Tooltips, Popovers, and Accordions rely on Bootstrap's JavaScript (often requiring Popper.js). Can be included via CDN bundle (`bootstrap.bundle.min.js`), separate files, or imported as ES modules (`import * as bootstrap from 'bootstrap'`).

### Key APIs / Components / Configuration / Patterns

*   **HTML Setup:**
    *   `<!doctype html>`: Required HTML5 doctype.
    *   `<meta name="viewport" content="width=device-width, initial-scale=1">`: Essential for responsive behavior.
*   **Installation:**
    *   `npm install bootstrap@5.3.3`: Install via npm.
    *   CDN Links: Include CSS (`<link>`) and JS (`<script>`) via CDN (jsDelivr recommended).
*   **Layout:**
    *   `.container`, `.container-fluid`: Main content wrappers (fixed-width responsive vs. full-width).
    *   `.row`: Wrapper for grid columns.
    *   `.col`, `.col-{breakpoint}-{size}` (e.g., `.col-md-6`): Grid columns.
    *   `.d-flex`, `.align-items-*`, `.justify-content-*`: Flexbox utilities.
*   **Components:**
    *   **Forms:** `.form-control`, `.form-label`, `.form-select`, `.form-check`, `.needs-validation`, `.was-validated`, `.input-group`.
    *   **Buttons:** `.btn`, `.btn-{color}` (e.g., `.btn-primary`), `.btn-{lg|sm}`, `.btn-outline-{color}`.
    *   **Navbar:** `.navbar`, `.navbar-expand-{breakpoint}`, `.navbar-brand`, `.navbar-nav`, `.nav-link`, `.navbar-toggler`, `.navbar-collapse`, `#id` + `data-bs-target`.
    *   **Cards:** `.card`, `.card-body`, `.card-title`, `.card-text`, `.card-img-top`.
    *   **Modals:** `.modal`, `.modal-dialog`, `.modal-content`, `data-bs-toggle="modal"`, `data-bs-target="#myModal"`.
    *   **Accordion:** `.accordion`, `.accordion-item`, `.accordion-button`, `.accordion-collapse`, `data-bs-toggle="collapse"`.
*   **Utilities:**
    *   Spacing: `.m-{size}`, `.p-{size}` (margin/padding, 0-5).
    *   Colors: `.text-{color}`, `.bg-{color}`, CSS Variables (`--bs-primary-rgb`).
    *   Visibility: `.visually-hidden`, `.d-none`, `.d-{breakpoint}-block`.
*   **Customization:**
    *   Sass: Override variables (`$primary: ...;`) before importing Bootstrap (`@import ".../bootstrap/scss/bootstrap";`). Import parts selectively.
    *   CSS Variables: Override root variables (`:root { --bs-primary: ...; }`).
    *   Dark Mode: `data-bs-theme="dark"` on `<html>` or component element.
*   **JavaScript:**
    *   `bootstrap.bundle.min.js`: Includes Popper.js.
    *   `import * as bootstrap from 'bootstrap'`: ES Module import.
    *   `new bootstrap.Modal('#myModal')`: Programmatic component instantiation.

### Common Patterns & Best Practices / Pitfalls

*   **Responsiveness:** Always use the viewport meta tag and leverage the grid system.
*   **Accessibility:** Use `.visually-hidden` for accessible hidden text. Ensure proper `aria-*` attributes and keyboard navigation for interactive components.
*   **Performance:** Use CDN for simplicity or npm/Sass imports for optimized builds (import only needed components/utilities).
*   **JS Dependencies:** Popper.js is needed for dropdowns, tooltips, popovers. Use the bundle or include it separately.
*   **Validation:** Combine HTML5 attributes with Bootstrap classes (`.needs-validation`) and JS for custom feedback.
*   **Customization:** Prefer overriding Sass variables or CSS variables over writing custom CSS to override Bootstrap styles directly.

---
This index summarizes the core concepts, APIs, and patterns for Bootstrap v5.3.3. Consult the full source documentation (project_journal/context/source_docs/bootstrap-specialist-llms-context-20250406.md) for exhaustive details.