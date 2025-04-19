# WCAG 2.1 AA Quick Summary

A condensed reference for key Web Content Accessibility Guidelines (WCAG) 2.1 principles and common AA Success Criteria (SC) relevant during development.

## POUR Principles

1.  **Perceivable:** Information and UI components must be presentable to users in ways they can perceive.
    *   Provide text alternatives for non-text content.
    *   Provide alternatives for time-based media.
    *   Create content that can be presented in different ways (e.g., simpler layout) without losing information or structure.
    *   Make it easier for users to see and hear content.
2.  **Operable:** UI components and navigation must be operable.
    *   Make all functionality available from a keyboard.
    *   Provide users enough time to read and use content.
    *   Do not design content in a way that is known to cause seizures.
    *   Provide ways to help users navigate, find content, and determine where they are.
3.  **Understandable:** Information and the operation of UI must be understandable.
    *   Make text content readable and understandable.
    *   Make web pages appear and operate in predictable ways.
    *   Help users avoid and correct mistakes.
4.  **Robust:** Content must be robust enough that it can be interpreted reliably by a wide variety of user agents, including assistive technologies.
    *   Maximize compatibility with current and future user agents.

## Common WCAG 2.1 AA Success Criteria (Examples)

*   **1.1.1 Non-text Content (Level A):** All non-text content (images, icons) has a text alternative (e.g., `alt` text) that serves the equivalent purpose. Decorative images should have empty `alt=""`.
*   **1.3.1 Info and Relationships (Level A):** Information, structure, and relationships conveyed through presentation can be programmatically determined or are available in text (e.g., use semantic HTML like `<nav>`, `<h1>`-`<h6>`, `<ul>`, `<table>`; associate labels with form controls using `<label for="...">`).
*   **1.4.1 Use of Color (Level A):** Color is not used as the only visual means of conveying information, indicating an action, prompting a response, or distinguishing a visual element.
*   **1.4.3 Contrast (Minimum) (Level AA):** Visual presentation of text and images of text has a contrast ratio of at least 4.5:1 (3:1 for large text). Use contrast checker tools.
*   **1.4.4 Resize text (Level AA):** Text can be resized without assistive technology up to 200 percent without loss of content or functionality. Use relative units (`rem`, `em`, `%`) for text and containers.
*   **1.4.11 Non-text Contrast (Level AA):** Visual presentation of UI components and graphical objects have a contrast ratio of at least 3:1 against adjacent color(s). This includes input borders and focus indicators.
*   **2.1.1 Keyboard (Level A):** All functionality is operable through a keyboard interface without requiring specific timings.
*   **2.1.2 No Keyboard Trap (Level A):** If keyboard focus can be moved to a component, then it can be moved away using only the keyboard.
*   **2.4.3 Focus Order (Level A):** If a page can be navigated sequentially, focusable components receive focus in an order that preserves meaning and operability. Check tab order.
*   **2.4.4 Link Purpose (In Context) (Level A):** The purpose of each link can be determined from the link text alone or from the link text together with its programmatically determined link context. Avoid "Click here".
*   **2.4.7 Focus Visible (Level AA):** Any keyboard operable user interface has a mode of operation where the keyboard focus indicator is visible. Ensure clear `:focus` styles.
*   **3.3.2 Labels or Instructions (Level A):** Labels or instructions are provided when content requires user input. Associate `<label>` with `<input>`.
*   **4.1.1 Parsing (Level A):** Content using markup languages has complete start and end tags, elements are nested according to their specifications, elements do not contain duplicate attributes, and any IDs are unique (Use HTML validators).
*   **4.1.2 Name, Role, Value (Level A):** For all UI components, the name and role can be programmatically determined; states, properties, and values that can be set by the user can be programmatically set; and notification of changes is available to assistive technologies (Use semantic HTML or appropriate ARIA).

*(This is a summary. Refer to the full WCAG 2.1 documentation for complete details and techniques: https://www.w3.org/TR/WCAG21/)*