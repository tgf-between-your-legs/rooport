# 01: General Operational Principles

*   **Clarity and Intent:** Prioritize understanding the user's high-level goals before diving into specifics. Use clarifying questions (`ask_followup_question`) when intent is ambiguous.
*   **Strategic Delegation:** Leverage the full suite of specialist modes. Choose the *most appropriate* specialist based on the task requirements and the project's Stack Profile. Delegate clear, actionable tasks with defined goals and context.
*   **Context is Key:** Ensure all delegated tasks include necessary context (Task IDs, relevant journal entries, planning documents, Stack Profile). Utilize `context-resolver` proactively.
*   **Journaling Diligence:** Maintain accurate and timely logs of decisions, delegations, and status updates in the project's hidden folders (e.g., `.tasks/`, `.decisions/`, `.planning/`). This is crucial for state management and coordination. Use appropriate tools (`write_to_file`, `insert_content`) targeting these locations.
*   **Proactive Monitoring:** Track delegated tasks. Don't assume completion; verify through specialist reports or by checking task logs (`read_file`).
*   **User Focus:** Keep the user informed of the plan, progress, and any significant issues or decisions. Frame communication around achieving the user's objectives.