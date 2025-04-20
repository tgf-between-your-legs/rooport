# Accessibility: Color Contrast Checking Tools

Tools and techniques for verifying sufficient color contrast (WCAG 1.4.3 & 1.4.11).

## Core Concept: Contrast Ratios

WCAG (Web Content Accessibility Guidelines) requires minimum contrast ratios between text and its background, and between graphical elements/UI components and their adjacent colors, to ensure readability for people with moderately low vision or color deficiencies.

*   **WCAG 2.1 Level AA Requirements:**
    *   **Normal Text (1.4.3):** **4.5:1** ratio.
    *   **Large Text (1.4.3):** **3:1** ratio. (Large text is defined as 18pt/24px or 14pt/18.5px bold).
    *   **UI Components & Graphical Objects (1.4.11):** **3:1** ratio for visual information needed to identify components/states (e.g., input borders, focus indicators) and parts of graphics needed to understand content.
*   **Level AAA Requirements:** 7:1 for normal text, 4.5:1 for large text. (Stricter, often not a hard requirement unless specified).
*   **Exemptions:** Logos, decorative elements, disabled controls (though good contrast is still helpful), user agent default focus indicators (though custom ones must meet 3:1).

## Tools for Checking Contrast

1.  **Browser Developer Tools (Built-in Color Pickers):**
    *   **How:** Most modern browsers (Chrome, Firefox, Edge, Safari) have a color picker integrated into their developer tools (usually in the 'Styles' or 'Computed' pane when inspecting an element's `color` or `background-color`).
    *   **Functionality:** When inspecting a color, the dev tools often display the contrast ratio against the computed background color directly within the color picker UI. They usually indicate whether the ratio passes WCAG AA and/or AAA for normal and large text.
    *   **Pros:** Convenient, readily available, checks against the actual rendered background (including gradients or images if computed correctly).
    *   **Cons:** Might require inspecting individual elements. May not easily check non-text contrast (UI components) directly.

2.  **WebAIM Contrast Checker (Web Tool):**
    *   **URL:** https://webaim.org/resources/contrastchecker/
    *   **How:** Enter foreground and background color values (hex codes, RGB).
    *   **Functionality:** Calculates the contrast ratio and shows pass/fail status for WCAG AA/AAA (normal and large text). Includes lightness sliders.
    *   **Pros:** Simple, widely used, reliable calculation.
    *   **Cons:** Requires manually inputting or copy-pasting color values.

3.  **TPGi Colour Contrast Analyser (CCA) (Desktop App):**
    *   **URL:** https://www.tpgi.com/color-contrast-checker/
    *   **How:** Installable application (Windows/macOS). Provides eyedropper tools to select colors directly from anywhere on your screen.
    *   **Functionality:** Calculates ratio, shows pass/fail status for AA/AAA. Includes color blindness simulators.
    *   **Pros:** Eyedropper is very convenient for checking any visual element (text, UI components, graphics, images of text). Works across applications, not just browsers. Color blindness simulation.
    *   **Cons:** Requires installation.

4.  **Browser Extensions (e.g., WAVE, Axe DevTools, Accessibility Insights):**
    *   **How:** Install the extension in your browser. Run an analysis on the current page.
    *   **Functionality:** These automated tools often include color contrast checks as part of their broader accessibility audit. They typically flag elements with insufficient contrast based on computed styles.
    *   **Pros:** Can identify multiple contrast issues across a page quickly. Integrated into the browser.
    *   **Cons:** Automated checks can sometimes miss issues (e.g., text over complex backgrounds/images) or produce false positives. Still requires manual verification. May not thoroughly check non-text contrast (1.4.11).

5.  **Figma Plugins (for Designers):**
    *   **Examples:** Stark, Contrast, A11y - Color Contrast Checker.
    *   **How:** Integrate directly into Figma design files.
    *   **Functionality:** Allow designers to check contrast ratios directly within their mockups before development begins.
    *   **Pros:** Catches issues early in the design phase.
    *   **Cons:** Checks design intent, not necessarily the final rendered code.

## Testing Workflow

1.  **Identify Key Elements:** Check body text, headings, links, button text, placeholder text, text within images.
2.  **Check UI Components:** Check borders of inputs, boundaries of buttons/controls, state indicators (focus rings, selected states, toggles), icons conveying information, important parts of charts/graphs.
3.  **Use Tools:** Employ a combination of browser dev tools (quick checks), CCA (eyedropper for complex cases/non-text), and automated extensions (broad scan).
4.  **Verify:** Manually verify flagged issues, especially those involving gradients, background images, or non-text elements.

Ensuring sufficient color contrast is a fundamental aspect of accessible design, making content readable for a wider range of users.