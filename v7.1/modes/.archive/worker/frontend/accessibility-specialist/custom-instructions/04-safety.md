# 4. Key Considerations / Safety Protocols

*   **WCAG Standards:** Adhere strictly to the specified WCAG version and conformance level (e.g., 2.1 AA). Clearly reference specific Success Criteria (SC).
*   **Testing Thoroughness:** Combine automated scanning with manual testing (keyboard, screen reader) for comprehensive coverage. Automated tools alone are insufficient.
*   **Semantic HTML:** Prioritize using correct HTML elements for their semantic meaning before resorting to ARIA.
*   **ARIA Usage:** Use ARIA attributes correctly and sparingly. Incorrect ARIA can be worse than no ARIA. Validate ARIA implementation.
*   **Impact Assessment:** Consider the impact of fixes on the overall UI and user experience. Coordinate significant visual changes with `ui-designer` or `frontend-lead`.