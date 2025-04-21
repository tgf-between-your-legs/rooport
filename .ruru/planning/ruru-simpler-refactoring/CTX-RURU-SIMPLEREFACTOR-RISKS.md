+++
id = "CTX-RURU-SIMPLEREFACTOR-RISKS"
title = "Roo Commander Path Refactor (Simplified): Considerations & Risks"
context_type = "analysis"
scope = "Potential challenges and important points for the fixed .ruru/ path refactoring"
target_audience = ["ai_dev_team", "roo-commander", "core-architect"]
granularity = "overview"
status = "proposal"
last_updated = "2025-04-21"
tags = ["refactoring", "paths", "ruru", "risks", "considerations", "fixed-path"]
+++

# Roo Commander Path Refactor (Simplified): Considerations & Risks

While consolidating folders under `.ruru/` simplifies the approach compared to full path configuration, it still requires careful consideration.

## 1. Considerations

*   **Refactoring Scope:** Still affects a large number of Markdown and JavaScript files. Careful execution is needed.
*   **Fixed Structure:** This approach mandates the `.ruru/` structure. Users lose the option to keep folders at the root. This might be undesirable for some workflows or simpler projects.
*   **Search & Replace Accuracy:** The success hinges heavily on the accuracy of global search-and-replace operations. Needs meticulous checking to avoid unintended changes in code examples or text.
*   **Build Script Logic (`create_build.js`):** The build script needs careful adjustment to ensure the *output zip file* contains the correct folder structure (likely with `.modes`, `.roo`, etc., at the *root* of the zip) even though the source files are now under `.ruru/`.
*   **`.rurumodes` Path Generation:** Ensure the paths generated within `.rurumodes` for `kb_path` and `custom_instructions_path` are correct relative to the workspace root, as expected by the Roo Code extension.
*   **User Communication:** Clearly document the new mandatory `.ruru/` structure and the updated installation process (extracting creates `.ruru/`).

## 2. Risks

*   **Incomplete Path Updates:** Missing even a few hardcoded path references during the find/replace will lead to runtime errors (file not found, incorrect context loading). **This is the primary risk.**
*   **Incorrect Replacements:** Overly broad search/replace could modify paths within code examples or documentation text, causing confusion or errors.
*   **Build Script Errors:** Errors in the modified build scripts could lead to incorrect `.rurumodes` files or malformed build archives.
*   **Testing Gaps:** Failure to test all core workflows after the refactor might leave hidden path-related bugs undiscovered.
*   **Assumption about Roo Code:** Assumes the Roo Code extension correctly resolves relative paths starting with `.ruru/` within the `.rurumodes` file.

**Recommendation:** Proceed with extreme caution. Use tools that allow previewing find/replace operations. Perform thorough manual code review after automated replacements. Implement comprehensive testing covering all major workflows and modes that interact heavily with the file system.