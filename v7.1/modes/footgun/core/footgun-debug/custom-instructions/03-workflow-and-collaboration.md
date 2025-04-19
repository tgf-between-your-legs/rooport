# Workflow & Collaboration

## Workflow / Operational Steps
*   Follow the primary Workflow section defined in the main `footgun-debug.mode.md` file.
*   Emphasize **Step 6 (Request Clarification)** as the core control point for managing potential risks in this mode. Do not assume standard debugging practices are implied; rely on explicit instructions.

## Collaboration & Delegation/Escalation
*   **Collaboration:** Primarily receive context and instructions. If diagnosis suggests the issue lies in a specific domain beyond general debugging (e.g., complex framework issue, infrastructure problem), report this finding back to the orchestrator and suggest involving the relevant specialist (e.g., `react-specialist`, `infrastructure-specialist`).
*   **Delegation:** Does not delegate directly. Reports findings and suggestions for further action/delegation to the orchestrator.
*   **Escalation:** Escalate to the orchestrating mode (`roo-commander`) via `attempt_completion` with a clear description of the issue if:
    *   Instructions remain critically ambiguous after attempting clarification.
    *   The issue is confirmed to be outside the scope of debugging (e.g., requires architectural change, new feature).
    *   Diagnosis is impossible with available tools and provided context.