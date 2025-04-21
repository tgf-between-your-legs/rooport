+++
id = "CTX-RURU-REFACTOR-RISKS"
title = "Roo Commander Path Refactor: Considerations & Risks"
context_type = "analysis"
scope = "Potential challenges and important points for the path refactoring"
target_audience = ["ai_dev_team", "roo-commander", "core-architect"]
granularity = "overview"
status = "proposal"
last_updated = "2025-04-21"
tags = ["refactoring", "configuration", "paths", "ruru", "risks", "considerations"]
+++

# Roo Commander Path Refactor: Considerations & Risks

Implementing configurable paths is beneficial but involves several considerations and potential risks:

## 1. Considerations

*   **Refactoring Scope:** This is a large undertaking affecting most `.md` and `.js` files in the system. Requires significant, careful effort.
*   **Placeholder Strategy:** The `{{RURU_PLACEHOLDER_NAME}}` format must be used strictly and consistently across all modified files. Define and document the exact list of placeholders.
*   **Substitution Script Logic:** The script needs to be robust, handling potential file system errors, parsing errors in `ruru.config.toml`, and correctly resolving nested placeholders like `{WORKSPACE_BASE}`.
*   **Output Strategy:** Decide whether the substitution script overwrites source files (simpler for AI context, riskier for development) or writes to a separate processed directory (safer, adds build step complexity). A separate directory is generally recommended.
*   **Roo Code Extension Interaction:** How does Roo Code load `.rurumodes`? How does it resolve `kb_path` and `custom_instructions_path` if they *aren't* explicitly listed in `.rurumodes`? If Roo Code *can* read `ruru.config.toml`, it simplifies things. If not, the build script *must* generate correct, absolute/relative paths in `.rurumodes`. This is a critical dependency.
*   **Migration:** How will existing workspaces be updated? The substitution script becomes a necessary step.
*   **User Experience:** Adding a build/substitution step increases setup complexity for users compared to simply extracting files. Clear documentation is essential.

## 2. Risks

*   **Incomplete Refactoring:** Missing hardcoded path references during the update process will lead to runtime errors or incorrect behavior. Thorough searching (`grep`/IDE search) and testing are vital.
*   **Substitution Script Errors:** Bugs in the script could lead to incorrect paths being generated, breaking the system. Needs careful testing.
*   **Placeholder Collisions:** Ensure the chosen placeholder format (`{{RURU_...}}`) doesn't accidentally clash with existing content in Markdown files (e.g., code examples using similar syntax).
*   **Configuration Errors:** Incorrect paths in `ruru.config.toml` will lead to errors. Need validation or clear documentation.
*   **Broken Tooling:** Changes might break assumptions in external tools or scripts that interact with the Roo Commander file structure.
*   **AI Misinterpretation:** Although the goal is to provide concrete paths, unexpected interactions between the substituted paths and the AI's interpretation of instructions are still possible, though less likely than with placeholders.

**Recommendation:** Proceed cautiously, implement thorough testing for the substitution script and core workflows under different configurations, and document the new setup process clearly for users.