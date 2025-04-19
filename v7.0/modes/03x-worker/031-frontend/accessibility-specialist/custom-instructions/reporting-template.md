# Accessibility Audit Report Template

Use this template for documenting accessibility audit findings and remediation efforts.

```markdown
# Accessibility Audit Report: [UI Area / Component / Flow]

**Task ID:** `[TaskID]` (Link to `.tasks/[TaskID].md`)
**Date:** [YYYY-MM-DD]
**Auditor:** `accessibility-specialist`
**Target WCAG Level:** [e.g., WCAG 2.1 AA]

## 📝 Executive Summary
*(Brief overview: Area audited, overall compliance status, number of major issues found/fixed, key remaining concerns.)*

## 🎯 Scope
*   [Clearly define the specific UI area, component, or user flow that was audited.]
*   [Mention any specific user scenarios tested.]

## 🛠️ Methodology
*   **Manual Testing:** Keyboard navigation, Screen Reader ([Specify reader, e.g., VoiceOver/NVDA]), Zoom, Visual Inspection.
*   **Automated Tools:** [List tools used, e.g., Axe DevTools, Lighthouse].
*   **Browsers/Platforms:** [Specify environments tested, e.g., Chrome/macOS, Firefox/Windows].

## ✅ Findings & Remediation

*(Group findings by WCAG Success Criterion. For each finding, describe the issue, its impact, the fix applied (if any), and verification status.)*

### WCAG [SC Number]: [SC Name] (Level [A/AA/AAA])

*   **Issue 1:** [Description of the specific problem found.]
    *   **Impact:** [How does this affect users with disabilities?]
    *   **Location(s):** [Specific file(s), line number(s), or UI element description.]
    *   **Fix Applied:** [Describe the code change made. Include code snippets if helpful.]
    *   **Verification:** [Confirmed fix via manual/automated test.]
*   **Issue 2:** [Description...]
    *   **Impact:** ...
    *   **Location(s):** ...
    *   **Fix Applied:** ...
    *   **Verification:** ...

### WCAG [SC Number]: [SC Name] (Level [A/AA/AAA])

*   **Issue 3:** [Description...]
    *   ...

*(Repeat for each identified WCAG failure.)*

## 🧱 Remaining Issues / Recommendations
*(List any issues that were not fixed, require further investigation, or need architectural/design changes. Provide recommendations.)*

*   **Issue:** [Description of remaining issue.]
    *   **Reason Not Fixed:** [e.g., Requires significant refactoring, Needs design input, Technical limitation].
    *   **Recommendation:** [e.g., Escalate to `technical-architect`, Discuss with `ui-designer`, Create follow-up task].
*   ...

## ✔️ Conclusion
*(Overall assessment of the accessibility status of the audited area after remediation efforts.)*

---
*This report details findings based on testing conducted on [Date]. Automated tools catch only a subset of potential issues.*
```

*(Adapt this template as needed. Ensure WCAG SC numbers are accurate and findings are clearly described.)*