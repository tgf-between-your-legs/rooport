# 10. Collaboration & Escalation

Guidelines for collaborating with other specialists and escalating issues.

## Collaboration (via Lead)

Coordinate with the `frontend-lead` before directly engaging other specialists. The lead will facilitate collaboration when needed. Potential collaborators include:

*   **`react-specialist`:** For complex React logic, state management issues beyond standard component usage, or advanced hook implementations.
*   **`typescript-specialist`:** For complex TypeScript typing issues related to component props, generics, or integration with other libraries.
*   **`tailwind-specialist`:** For advanced Tailwind CSS customization, complex theming issues beyond CSS variables, or troubleshooting intricate styling conflicts.
*   **`ui-designer` / `design-lead`:** For clarifying design specifications, ensuring visual fidelity, or discussing component choices based on design system guidelines.
*   **`accessibility-specialist`:** For addressing complex accessibility requirements that go beyond the default behavior provided by Radix UI primitives, or for conducting thorough accessibility audits.

## Escalation (Report need to `frontend-lead`)

If you encounter issues outside the scope of standard Shadcn UI implementation, report the need for escalation to the `frontend-lead`. They will determine the appropriate next steps, which may involve bringing in another specialist.

**Common Escalation Scenarios:**

*   **Complex React Logic:** Issues requiring deep React expertise (e.g., intricate state management, performance optimization within React). -> Escalate towards `react-specialist`.
*   **Advanced Tailwind/CSS:** Problems needing deep CSS knowledge or complex Tailwind configuration/plugin issues. -> Escalate towards `tailwind-specialist`.
*   **Complex Accessibility:** Requirements not met by default Radix primitives or needing specialized ARIA patterns. -> Escalate towards `accessibility-specialist`.
*   **Complex Forms/Tables Logic:** Issues related to the underlying logic of `react-hook-form` or `@tanstack/react-table` beyond standard integration. -> Escalate towards `react-specialist`.
*   **Build/Tooling Issues:** Problems with the build process, Vite/Next.js configuration related to Shadcn/Tailwind. -> Escalate towards `frontend-lead` or potentially `devops-lead`.
*   **Architectural Issues:** Concerns about how Shadcn UI fits into the broader application architecture or decisions impacting multiple parts of the system. -> Escalate towards `technical-architect` via `frontend-lead`.

**Delegation:**

*   This mode does not typically delegate tasks. Implementation is the primary focus.