# WCAG 2.1 AA Quick Reference Checklist

A condensed checklist focusing on common issues related to WCAG 2.1 Level AA conformance. This is **not exhaustive**; always refer to the full WCAG guidelines.

## Principle 1: Perceivable

Information and user interface components must be presentable to users in ways they can perceive.

*   **1.1 Text Alternatives:**
    *   **1.1.1 Non-text Content (Level A):** All non-text content (images, icons, charts) has a text alternative (`alt` attribute for `<img>`, `aria-label`, visually hidden text) that serves the equivalent purpose, unless purely decorative (`alt=""`).
*   **1.3 Adaptable:**
    *   **1.3.1 Info and Relationships (Level A):** Information, structure, and relationships conveyed through presentation can be programmatically determined or are available in text (e.g., use semantic HTML: headings `<h1>`-`<h6>`, lists `<ul>`/`<ol>`/`<dl>`, landmarks `<nav>`, `<main>`, `<aside>`, `<footer>`, table structure `<th>`, `scope`). Don't rely on visual formatting alone. Ensure correct label association for form controls (`<label for="...">`).
    *   **1.3.2 Meaningful Sequence (Level A):** Content reading/navigation sequence is logical and intuitive (check DOM order vs visual order).
    *   **1.3.5 Identify Input Purpose (Level AA):** Input fields collecting user information have appropriate `autocomplete` attributes (e.g., `autocomplete="name"`, `autocomplete="email"`).
*   **1.4 Distinguishable:**
    *   **1.4.1 Use of Color (Level A):** Color is not used as the *only* visual means of conveying information, indicating an action, prompting a response, or distinguishing a visual element. Provide alternatives (text labels, icons, patterns).
    *   **1.4.3 Contrast (Minimum) (Level AA):** Text and images of text have a contrast ratio of at least **4.5:1** against their background. Large text (18pt+ or 14pt+ bold) requires **3:1**. Logos and incidental text are exempt.
    *   **1.4.4 Resize text (Level AA):** Text can be resized up to 200% without loss of content or functionality (use relative units like `rem`/`em`, avoid fixed heights on containers with text).
    *   **1.4.11 Non-text Contrast (Level AA):** Visual information required to identify UI components (e.g., input borders, button boundaries) and states (e.g., focus, selected) has a contrast ratio of at least **3:1** against adjacent colors. Graphical objects conveying information (e.g., icons, chart segments) also require 3:1 contrast.

## Principle 2: Operable

User interface components and navigation must be operable.

*   **2.1 Keyboard Accessible:**
    *   **2.1.1 Keyboard (Level A):** All functionality is operable through a keyboard interface without requiring specific timings.
    *   **2.1.2 No Keyboard Trap (Level A):** Keyboard focus can be moved away from any component using only the keyboard.
    *   **2.1.4 Character Key Shortcuts (Level A):** If single-character key shortcuts are used, provide a mechanism to turn them off or remap them, or ensure they only activate when the component has focus.
*   **2.4 Navigable:**
    *   **2.4.3 Focus Order (Level A):** Focus order is logical and preserves meaning.
    *   **2.4.4 Link Purpose (In Context) (Level A):** The purpose of each link can be determined from the link text alone or from the link text together with its programmatically determined link context. Avoid "Click Here".
    *   **2.4.6 Headings and Labels (Level AA):** Headings (`<h1>`-`<h6>`) and labels (`<label>`) describe topic or purpose. Use headings hierarchically.
    *   **2.4.7 Focus Visible (Level AA):** Any keyboard operable user interface has a mode of operation where the keyboard focus indicator is visible. Ensure clear `:focus` or `:focus-visible` styles.
*   **2.5 Input Modalities:**
    *   **2.5.3 Label in Name (Level A):** For UI components with labels that include text or images of text, the accessible name (e.g., `aria-label`) contains the text that is presented visually.

## Principle 3: Understandable

Information and the operation of user interface must be understandable.

*   **3.1 Readable:**
    *   **3.1.1 Language of Page (Level A):** The default human language of the page is programmatically set (`<html lang="...">`).
*   **3.2 Predictable:**
    *   **3.2.1 On Focus (Level A):** When any UI component receives focus, it does not initiate a change of context (e.g., automatically submitting a form or launching a new window).
    *   **3.2.2 On Input (Level A):** Changing the setting of any UI component does not automatically cause a change of context unless the user has been advised of the behavior before using the component.
*   **3.3 Input Assistance:**
    *   **3.3.1 Error Identification (Level A):** If an input error is automatically detected, the item that is in error is identified and the error is described to the user in text.
    *   **3.3.2 Labels or Instructions (Level A):** Labels or instructions are provided when content requires user input. Ensure clear, visible labels for form controls.

## Principle 4: Robust

Content must be robust enough that it can be interpreted reliably by a wide variety of user agents, including assistive technologies.

*   **4.1 Compatible:**
    *   **4.1.1 Parsing (Level A):** Content uses valid HTML according to specification (check for duplicate IDs, nesting errors, etc.).
    *   **4.1.2 Name, Role, Value (Level A):** For all UI components (including custom controls), their name and role can be programmatically determined; states, properties, and values that can be set by the user can be programmatically set; and notification of changes is available to assistive technologies (often achieved via semantic HTML and correct ARIA usage).

*(This is a simplified reference. Always consult the full WCAG 2.1/2.2 documentation for complete details and techniques: https://www.w3.org/TR/WCAG21/)*