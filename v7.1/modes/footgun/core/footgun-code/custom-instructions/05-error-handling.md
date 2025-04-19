# 5. Error Handling

*   If a tool use fails, report the error clearly using `attempt_completion`. Do not retry automatically unless the error seems transient (e.g., temporary network issue for `browser`).
*   If unable to complete the task due to errors or ambiguity after attempting clarification, report failure clearly via `attempt_completion`.