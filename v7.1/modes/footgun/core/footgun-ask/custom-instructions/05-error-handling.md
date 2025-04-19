# 5. Error Handling

*   If a tool use fails (e.g., `read_file` on non-existent path, `browser` error), report the specific error clearly using `attempt_completion` and state how it prevents answering the question.
*   If unable to answer due to lack of information or ambiguity after attempting clarification, state this clearly via `attempt_completion`.
*   If instructed to access a file in `.roo/context/ask/` that doesn't exist, report this specifically and suggest that the orchestrator may need to create or provide the appropriate context file.