# Potentially Risky Code Patterns

This document lists examples of code patterns or operations that might be requested but carry inherent risks. When instructing `footgun-code` to implement these, ensure the risks are understood and explicitly acknowledged. The mode should request clarification if these patterns are requested without such acknowledgment.

## Examples

1.  **Disabling Security Features:**
    *   **Pattern:** Code that explicitly disables security checks (e.g., CSRF protection, input validation, authentication middleware).
    *   **Risk:** Creates security vulnerabilities.
    *   **Required Acknowledgment:** Instruction must state *why* the security feature is being disabled and acknowledge the associated risk (e.g., "Temporarily disable CSRF for testing endpoint X, acknowledging security risk during test phase.").
2.  **Direct Database Manipulation without ORM/Validation:**
    *   **Pattern:** Generating raw SQL queries or directly modifying database entries without going through established data access layers or validation logic.
    *   **Risk:** SQL injection vulnerabilities, data corruption, bypassing business logic.
    *   **Required Acknowledgment:** Instruction must justify bypassing the standard data layer and acknowledge risks (e.g., "Perform direct DB update for migration script Y, acknowledging risk of bypassing validation.").
3.  **Hardcoding Sensitive Information:**
    *   **Pattern:** Embedding passwords, API keys, or other secrets directly into source code.
    *   **Risk:** Exposure of sensitive credentials if code is compromised or publicly accessible.
    *   **Required Acknowledgment:** Instruction must acknowledge this is generally bad practice and provide a reason (e.g., "Hardcode placeholder API key for initial local testing only, acknowledging this is insecure for production.").
4.  **Ignoring Error Handling:**
    *   **Pattern:** Code that explicitly catches errors but does nothing with them (empty catch blocks) or lacks necessary error handling for critical operations (file I/O, network calls).
    *   **Risk:** Silent failures, unstable application state, difficult debugging.
    *   **Required Acknowledgment:** Instruction should justify the lack of error handling if intentional (rarely advisable).
5.  **Large-Scale Unconditional File Operations:**
    *   **Pattern:** Instructions to delete, move, or overwrite large numbers of files without specific conditions or backups (e.g., `rm -rf /some/path/*`).
    *   **Risk:** Irreversible data loss.
    *   **Required Acknowledgment:** Instruction must confirm the target path is correct, acknowledge the risk of data loss, and confirm backups exist if necessary.

*(Add more project-specific risky patterns here. The key is that instructing the mode to implement these requires explicit acknowledgment of the deviation from standard safe practices.)*