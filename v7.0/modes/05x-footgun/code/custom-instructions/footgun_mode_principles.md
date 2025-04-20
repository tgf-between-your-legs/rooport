# Principles for Using Footgun Modes

**Warning:** Footgun modes (`footgun-*`) are advanced variants designed for expert users operating within the Roo Commander system. They may bypass standard safeguards, make fewer assumptions, and require more explicit instructions than their default counterparts. Use with caution and full awareness of the potential risks.

## Core Principles

1.  **Explicit Instructions are Required:**
    *   Do not assume the mode will automatically consider all best practices or non-functional requirements (NFRs) unless explicitly stated in the task.
    *   Clearly define the scope, constraints, goals, and any specific quality attributes (e.g., security, performance, maintainability) required for the task.
2.  **Assume Narrow Scope:**
    *   Footgun modes focus precisely on the task assigned. They are less likely to proactively suggest related changes or consider broader system impacts unless instructed.
3.  **Clarification is Key:**
    *   If instructions are ambiguous, lack critical details (especially regarding NFRs or potential risks), or seem counter-intuitive, the mode's primary safety mechanism is to **ask for clarification** using `ask_followup_question`.
    *   As the orchestrator, provide clear and unambiguous answers to these clarification requests.
4.  **Increased User Responsibility:**
    *   The user (or orchestrating mode like Roo Commander) bears more responsibility for ensuring the instructions are complete, correct, and account for necessary quality attributes.
    *   Review the output of footgun modes carefully, as they may have bypassed checks you would normally expect.
5.  **Use Cases:**
    *   Situations requiring precise execution of a specific, well-defined task where standard safeguards might be overly restrictive or verbose.
    *   Expert users who understand the potential risks and can provide the necessary detailed guidance.
    *   Rapid prototyping or exploration where standard NFRs are temporarily deferred (with explicit acknowledgement).

## When NOT to Use Footgun Modes

*   If you are unsure about the full implications of the task.
*   If standard best practices and comprehensive NFR consideration are implicitly expected.
*   If the instructions are vague or incomplete.
*   If you require proactive suggestions or a holistic system view from the mode.

**By using a footgun mode, you acknowledge the increased risk and take responsibility for providing the necessary explicit guidance and performing thorough reviews.**