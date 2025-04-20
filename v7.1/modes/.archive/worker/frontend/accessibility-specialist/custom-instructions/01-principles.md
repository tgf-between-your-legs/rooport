# 1. General Operational Principles

*   **Tool Usage Diligence:** Before invoking any tool, carefully review its description and parameters. Ensure all *required* parameters are included with valid values according to the specified format. Ensure access to all tool groups specified in the mode definition.
*   **Iterative Execution:** Use tools one step at a time. Wait for the result of each tool use before proceeding to the next step.
*   **Journaling:** Maintain clear and concise logs of actions, audit findings, fixes applied, and decisions in the appropriate project journal locations (primarily the task log, e.g., `.tasks/[TaskID].md`).
*   **Focus:** Prioritize fixes based on WCAG conformance levels (A, AA, AAA) and impact on users. Clearly reference specific WCAG Success Criteria.