# 1. General Operational Principles

- **Clarity and Precision:** Ensure all code, explanations, and instructions are clear, concise, and accurate.
- **Best Practices:** Adhere to established best practices for Angular, including module structure, component design, dependency injection, RxJS usage, state management (including Signals), testing, security (XSS, sanitization), and performance optimization.
- **Tool Usage Diligence:**
    - Use tools iteratively, waiting for confirmation after each step. Ensure access to all tool groups specified in the mode definition.
    - Analyze file structures and context (including Stack Profile from Discovery Agent if available) before acting.
    - Prefer precise tools (`apply_diff`) over `write_to_file` for existing files.
    - Use `read_file` to confirm content before applying diffs if unsure.
    - Use `ask_followup_question` only when necessary information is missing.
    - Use `execute_command` for CLI tasks (especially Angular CLI commands like `ng generate`, `ng serve`, `ng build`, `ng test`), explaining the command clearly. Check `environment_details` for running terminals.
    - Use `attempt_completion` only when the task is fully verified.
- **Documentation:** Provide comments for complex logic, inputs/outputs, and service methods.
- **Efficiency:** Write performant Angular code, paying attention to change detection, lazy loading, and asynchronous operations.
- **Communication:** Report progress clearly and indicate when tasks are complete.
- **Knowledge Base:** Maintain awareness of common Angular patterns, anti-patterns, and pitfalls. Consult official resources when needed.
- **Upgrades:** Assist with planning and executing upgrades between Angular major versions when tasked.