# Information Extraction Tips for Session Summarizer

Tips for extracting key information for the handover summary from coordination logs and planning documents.

## Coordination Logs (`.tasks/TASK-CMD-...md`)

*   **Current Goal (🎯):** Look for the most recent `## Goal` section or explicit statements like "Current objective is..." in the log entries.
*   **Recent Actions:** Scan the last few log entries or checklist items (`- [x] ...`). Summarize the *completed* actions.
*   **Active Delegated Tasks:** Look for log entries indicating delegation via `new_task` (e.g., "Delegated TASK-FE-123 to react-specialist..."). Cross-reference with the provided list of active tasks if available. If needing status, this might require reading the specific task file (though Session Summarizer usually relies on the coordination log).
*   **Blockers / Issues (🧱):** Search for keywords like "Blocked", "Issue", "Waiting for", "Cannot proceed", or explicit `## Blockers` sections in recent log entries.
*   **Open Questions:** Look for questions posed to the user or other modes that haven't been marked as answered in the log.

## Planning Documents (`.planning/*.md`)

*   **Next Steps (➡️):** Look for sections like `## Next Steps`, `## Immediate Priorities`, or the next unchecked item in a high-level plan/checklist.
*   **Overall Goal:** Reconfirm the high-level project goal if needed, often found in introductory sections.

## General Tips

*   **Focus on Recency:** Prioritize the most recent entries in logs and the current state in planning documents.
*   **Use Template Keywords:** Extract information specifically matching the placeholders in `handover_summary_template.md` (Goal, Last Action, Active Task, Next Step, Blocker, Open Question).
*   **Be Concise:** Summarize findings briefly. Use bullet points.
*   **Attribute (Implicitly):** While the final summary doesn't require inline citations like research reports, know which document provided each piece of information (Coordination Log vs. Planning Doc vs. Task File).
*   **Handle Missing Info:** If a piece of information (e.g., explicit next step) isn't found in the provided documents, state "None identified" or similar in the summary template. Do not guess.