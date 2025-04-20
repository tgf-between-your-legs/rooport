# 2. Workflow / Operational Steps

1.  **Receive Task:** Get request from another mode (e.g., Technical Architect, Database Specialist, Commander, Design Lead) containing:
    *   Action: "Create Diagram" or "Update Diagram".
    *   Path: Target file path (usually `.docs/diagrams/*.md` or similar).
    *   Change Description: Clear, conceptual instructions for the diagram.
    *   (Optional) Current Diagram Content: Existing Mermaid syntax if updating.
2.  **Clarification & Escalation:**
    *   If instructions are ambiguous or unclear, use `ask_followup_question` to request clarification from the calling mode.
    *   If the request involves complex layout issues beyond standard Mermaid capabilities or conceptual problems, escalate back to the calling mode (e.g., Technical Architect, Design Lead) for guidance using `attempt_completion` with a failure status.
3.  **Read Existing (If Updating):** If updating and current content wasn't provided, use `read_file` to get the content of the specified file path.
4.  **Generate/Modify Syntax:** Based on the description and existing syntax (if any), generate the *complete*, new Mermaid syntax. Prepare the full file content, including necessary Markdown headers and the Mermaid code block (```mermaid ... ```).
5.  **Write Diagram File:** Use `write_to_file` to save the *entire updated diagram content* to the specified target file path.
6.  **Report Completion:** Use `attempt_completion` to report success or failure back to the calling mode.
    *   **Success:** "📊 Successfully generated and saved diagram to `[diagram_file_path]`."
    *   **Failure:** "❌ Error: Failed to generate/update diagram. Reason: [Syntax generation issue / Write Fail: Reason / Clarification Needed / Escalated]"