# Accessibility Audit Report Template

A basic structure for documenting accessibility audit findings.

---

**Audit Details**

*   **Date:** YYYY-MM-DD
*   **Auditor:** [Your Name/Mode Name]
*   **Scope:** [Specify the UI area, component, user flow, or page(s) audited]
*   **Target Standard:** WCAG [Version, e.g., 2.1] Level [Conformance Level, e.g., AA]
*   **Testing Environment:**
    *   Browser(s): [e.g., Chrome 1XX, Firefox 1XX]
    *   Screen Reader(s): [e.g., NVDA 202X.X, VoiceOver macOS 1X.X]
    *   Tool(s): [e.g., Axe DevTools, WAVE, Colour Contrast Analyser]

---

**Summary of Findings**

*   **Overall Conformance:** [e.g., Partially Supports, Does Not Support - based on findings]
*   **Key Issues Found:** [Brief summary of the most critical or prevalent issues]
    *   [Issue 1, e.g., Insufficient color contrast on primary buttons]
    *   [Issue 2, e.g., Missing alternative text for informative images]
    *   [Issue 3, e.g., Keyboard trap within the date picker widget]
*   **Positive Findings:** [Optional: Note areas where accessibility is well-implemented]

---

**Detailed Findings & Recommendations**

*(Repeat this section for each distinct issue found)*

**Issue #[Number]:** [Brief Title of Issue, e.g., Insufficient Button Contrast]

*   **Location:** [Describe where the issue occurs - URL, Component Name, Screenshot reference if applicable]
*   **Description:** [Detailed explanation of the problem and its impact on users, especially those using assistive technologies.]
    *   *Example:* The background color `#AAAAAA` used for the primary action button text (`#FFFFFF`) results in a contrast ratio of 2.1:1. This fails WCAG requirements. Users with low vision may have difficulty reading the button text.
*   **WCAG Success Criterion:** [List relevant SC number(s) and Level(s)]
    *   *Example:* 1.4.3 Contrast (Minimum) (Level AA)
*   **Testing Method:** [How was the issue identified? e.g., Manual Inspection (Color Contrast Analyser), Automated Scan (Axe), Screen Reader Testing (NVDA)]
*   **Recommendation:** [Specific, actionable steps to fix the issue.]
    *   *Example:* Change the button background color to a darker shade, such as `#777777` or darker, to achieve a contrast ratio of at least 4.5:1 with the white text. Verify the new color meets design requirements.
*   **Screenshot/Code Snippet:** [Optional: Include relevant visual aid or code]

---

*(... Repeat for Issue #2, Issue #3, etc. ...)*

---

**General Recommendations**

*   [Optional: Include broader recommendations not tied to specific issues, e.g., "Implement a consistent focus indicator style across all interactive elements."]
*   [Optional: Suggest training or process improvements.]

---

**Next Steps**

*   [Outline who is responsible for addressing the findings]
*   [Suggest timeline or priority for fixes]
*   [Plan for re-testing/verification]

---