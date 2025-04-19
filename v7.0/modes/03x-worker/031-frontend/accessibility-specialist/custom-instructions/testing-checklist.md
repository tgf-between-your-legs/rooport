# Accessibility Testing Checklist (Manual)

A checklist for manual accessibility testing. Combine with automated tools for better coverage.

## Keyboard Navigation

*   [ ] **Tab Order:** Can all interactive elements (links, buttons, form fields, custom widgets) be reached using the Tab key? Is the order logical and intuitive? (WCAG 2.4.3)
*   [ ] **Focus Visible:** Is the keyboard focus indicator clearly visible on every interactive element when it receives focus? (WCAG 2.4.7)
*   [ ] **Interaction:** Can all functions be performed using only the keyboard? (e.g., activating buttons/links with Enter/Space, selecting options in dropdowns, operating custom widgets). (WCAG 2.1.1)
*   [ ] **No Keyboard Trap:** Can you tab *out* of every interactive element or widget without getting stuck? (WCAG 2.1.2)

## Screen Reader Testing (e.g., VoiceOver, NVDA)

*   [ ] **Readability:** Does the screen reader announce page content in a logical order?
*   [ ] **Headings:** Are headings (`<h1>`-`<h6>`) used correctly to structure the page? Can you navigate by headings?
*   [ ] **Links:** Is the purpose of each link clear from its text when read out of context? (WCAG 2.4.4)
*   [ ] **Images:** Do meaningful images have descriptive `alt` text announced? Are decorative images skipped or announced appropriately (e.g., empty `alt=""`)? (WCAG 1.1.1)
*   [ ] **Forms:** Are labels correctly associated with and announced for form fields? Are instructions and error messages announced? Are required fields indicated? (WCAG 1.3.1, 3.3.2, 4.1.2)
*   [ ] **Buttons:** Are buttons announced as buttons with clear accessible names? (WCAG 4.1.2)
*   [ ] **Dynamic Content / ARIA:**
    *   Are dynamic changes (e.g., content revealed, error messages) announced appropriately (using `aria-live`)?
    *   Do custom widgets (tabs, accordions, modals) announce their role, state (e.g., expanded, selected), and name correctly? (WCAG 4.1.2)
    *   Are dialogs (`role="dialog"`) handled correctly (focus management, announcement)?

## Visual Inspection & Zoom

*   [ ] **Color Contrast:** Check key text/background and UI component/background contrasts using a color contrast checker tool. (WCAG 1.4.3, 1.4.11)
*   [ ] **Color Reliance:** Is information conveyed by means other than color alone? (WCAG 1.4.1)
*   [ ] **Text Resize:** Zoom the browser text size up to 200%. Does content reflow without loss of information or functionality? Is horizontal scrolling avoided for main content? (WCAG 1.4.4)
*   [ ] **Layout:** Does the layout remain usable and understandable at different viewport sizes (responsive check)?

## Other Checks

*   [ ] **Motion:** Are there options to reduce or disable non-essential animations (`prefers-reduced-motion`)? (WCAG 2.2.2 - Level A for flashing, consider AA for others)
*   [ ] **Page Titles:** Does each page have a unique and descriptive `<title>`? (WCAG 2.4.2)

*(This checklist provides a starting point. Refer to WCAG guidelines for detailed requirements.)*