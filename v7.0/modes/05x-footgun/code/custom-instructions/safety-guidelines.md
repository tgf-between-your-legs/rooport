# Safety Guidelines for Footgun Code Mode

**Warning:** `footgun-code` operates with fewer safeguards than standard coding modes. Adherence to these guidelines is crucial when instructing this mode.

## Core Safety Principles

1.  **Verify Before Modifying:**
    *   **ALWAYS** instruct the mode to use `read_file` to confirm the current state of code (especially line numbers and exact content) before instructing it to use `apply_diff`. Assume the file may have changed.
    *   Review the `read_file` output carefully before crafting the `apply_diff` instruction.
2.  **Prefer `apply_diff` for Edits:**
    *   For modifying existing files, `apply_diff` is generally safer than `write_to_file` as it targets specific lines.
    *   Use `write_to_file` primarily for creating *new* files or when a *complete rewrite* is explicitly intended and reviewed.
3.  **Complete Content for `write_to_file`:**
    *   When using `write_to_file`, **YOU MUST** provide the *entire*, complete, final content of the file. Do not use placeholders or assume the mode will fill in gaps. Failure to do so *will* result in data loss or corrupted files.
4.  **Explicit Instructions for Risky Operations:**
    *   Operations like deleting files, overwriting critical configuration, or making widespread changes require explicit confirmation and clear justification in the instructions.
    *   If instructing the mode to perform potentially destructive actions, acknowledge the risk explicitly (e.g., "Proceed with overwriting `config.json` as discussed...").
5.  **Command Execution (`execute_command`):**
    *   Clearly explain the purpose and expected outcome of any command.
    *   Prefer commands that operate on specific files or directories rather than global system changes.
    *   Be cautious with commands involving `rm`, `mv`, or script execution (`sh`, `python`, `node`). Ensure paths are correct and scripts are trusted.
6.  **Review Output:**
    *   Carefully review the results reported by the mode after each operation, especially file modifications or command executions.
    *   Use `read_file` or other verification methods if unsure about the outcome.
7.  **Clarification is Mandatory:**
    *   If the mode asks for clarification (`ask_followup_question`) regarding a potentially unsafe or ambiguous instruction, provide a clear, explicit answer. Do not dismiss its concerns.

**Failure to follow these guidelines significantly increases the risk of errors, data loss, or unintended system modifications when using `footgun-code`.**