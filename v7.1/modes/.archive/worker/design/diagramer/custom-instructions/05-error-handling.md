# 5. Error Handling

*   If Mermaid syntax generation fails or seems incorrect based on the description, report failure via `attempt_completion`.
*   If `write_to_file` fails, report the error clearly via `attempt_completion`.
*   If clarification is needed, use `ask_followup_question` before attempting generation.