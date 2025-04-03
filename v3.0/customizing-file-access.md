# 🚀 Roo Code Custom Modes - File Access Permissions

This repository contains a set of sophisticated custom modes for Roo Code, designed to work together as a multi-agent system for planning, developing, testing, and deploying websites.

**This guide focuses on understanding and potentially customizing file access permissions for specific modes like the `secretary` and `technical-writer` to adapt the system to your project's unique structure.**

**Note:** Modifying mode configurations requires understanding JSON and Roo Code's custom mode system. Proceed with caution.

## ✨ Core Concepts & Default Permissions

Our default mode set operates with a strong emphasis on safety and predictability, particularly regarding file modifications:

1.  **Orchestration (`roo-commander`):** Coordinates tasks.
2.  **Specialization:** Each mode focuses on its role (design, code, test, etc.).
3.  **Project Journal (`project_journal/`):** The central hub for logs, plans, and formal documents. By default, this is the *primary* location where modes are expected to write persistent information.
4.  **`logger` (Log Appender):** Strictly appends to `project_journal/activity_log.md` (via delegation).
5.  **`secretary` (File Writer):** By default, this mode is **strictly confined** to writing/overwriting files *only within* the `project_journal/` directory (specifically excluding the `activity_log.md`). It handles formal docs, diagrams, decision logs, and memories.
    *   **Default `secretary` Permission Rationale:** Prevents accidental overwriting of source code or critical configuration files outside the designated documentation/journal area.
6.  **`technical-writer`:** By default, this mode can write common documentation files (`.md`, `README*`, etc.) *outside* the `project_journal` (e.g., root README, component-level docs) but delegates writes *inside* the `project_journal` to the `secretary`.

## 🤔 Why Customize Permissions?

The default setup prioritizes safety. However, you might encounter situations where you need more flexibility:

*   **Existing Project Structures:** Your project might already have a well-established `docs/` folder at the root or within specific subdirectories *outside* the `project_journal/`.
*   **Component-Level Documentation:** You might prefer `README.md` files directly within source code folders (`src/components/MyComponent/README.md`).
*   **Specific File Types:** You might need the `secretary` or `technical-writer` to handle additional documentation file types (e.g., `.txt`, specific config formats used for documentation).

**Option 3 allows you, the user, to adjust the file access rules (`fileRegex`) for specific modes to match your project's needs.**

## 🔧 How to Customize File Access (`fileRegex`)

You can override the default permissions by editing the custom mode configuration file used by Roo Code.

**Steps:**

1.  **Identify the Configuration File:**
    *   **Global:** If you loaded the modes globally, you'll edit your main `custom_modes.json` file (location depends on your Roo Code setup).
    *   **Project-Specific:** If you are using modes for a specific project, you'll edit the `.roomodes` file in your project's root directory. *Creating a project-specific `.roomodes` file is recommended for customization, as it won't affect other projects.*
2.  **Locate the Mode Definition:** Find the JSON object for the mode you want to modify (e.g., `"slug": "secretary"` or `"slug": "technical-writer"`).
3.  **Find the `groups` Array:** Inside the mode object, locate the `groups` array.
4.  **Find the `edit` Permission:** Within the `groups` array, find the element that defines the `edit` permission. It will look something like this:
    ```json
        [
          "edit",
          {
            "fileRegex": "...", // <-- The pattern to modify
            "description": "..."
          }
        ]
    ```
5.  **Modify the `fileRegex`:** This is the crucial step. You need to adjust the regular expression pattern to match the files you want the mode to be able to write/overwrite.
    *   **Remember:** JSON requires backslashes (`\`) in regex patterns to be escaped with another backslash (`\\`).
    *   **Use a Regex Tester:** Use an online regex tester (like regex101.com) to experiment with patterns against example file paths from your project *before* putting them in the JSON.

**Example Customizations:**

*   **Example 1: Allowing `secretary` to write Markdown in a root `docs/` folder:**
    *   Find the `secretary` mode definition.
    *   Modify its `fileRegex` within the `edit` group.
    *   **Original (Strict):** `"fileRegex": "^project_journal\\/(?!activity_log\\.md$).*\\.(md|puml|mmd|txt|json|yaml|sql|drawio)$"`
    *   **Modified (Allows `docs/`):** `"fileRegex": "^(project_journal\\/(?!activity_log\\.md$)|docs\\/).*\\.(md|puml|mmd|txt|json|yaml|sql|drawio)$"`
        *   *Explanation:* `(project_journal\\/(?!activity_log\\.md$)|docs\\/)` uses `|` (OR) to match paths starting with `project_journal/` (excluding the activity log) OR paths starting with `docs/`.

*   **Example 2: Allowing `technical-writer` to edit *any* README file in the project:**
    *   Find the `technical-writer` mode definition.
    *   Modify its `fileRegex`.
    *   **Original (Excludes sensitive dirs):** `^(?!.*(\\.git|node_modules|dist|build|vendor)\\/)(?!.*activity_log\\.md).*(?:\\/(README|LICENSE)(\\.[^./]+)?|\\.(md|rst))$`
    *   **Modified (Broader README access):** `^(?!.*(\\.git|node_modules|dist|build|vendor)\\/)(?!.*activity_log\\.md).*(?:\\/README(\\.[^./]+)?|\\.(md|rst))$`
        *   *Explanation:* Simplified the README part to `\\/README(\\.[^./]+)?` which matches `/README` potentially followed by an extension. Adjust based on exact needs.

*   **Example 3: Adding `.txt` file support for the `technical-writer` outside the journal:**
    *   Find `technical-writer`.
    *   Modify `fileRegex`.
    *   **Modified:** `^(?!.*(\\.git|...)\\/)...|\\.(md|rst|txt))$` (Added `|txt` to the allowed extensions).

6.  **Save the Configuration File:** Save your changes to `custom_modes.json` or `.roomodes`.
7.  **Restart/Reload Roo Code (If Necessary):** Depending on your setup, Roo Code might need a reload or restart to pick up the modified configuration.

## ⚠️ Important Considerations When Customizing

*   **Test Thoroughly:** After modifying `fileRegex`, test carefully to ensure the mode can access the files you intended *and* cannot access files it shouldn't.
*   **Regex Complexity:** Complex regex patterns can be hard to read and maintain. Start simple and test iteratively.
*   **Security Risks:** Broadening permissions increases the risk of accidental overwrites. Understand the implications before significantly loosening restrictions. For instance, allowing edits to `package.json` or `*.config.js` could break your project if the LLM makes a mistake.
*   **Stick to Documentation Files:** It's generally recommended to limit broad write access primarily to documentation-related file types (`.md`, `.rst`, `README*`, etc.) rather than source code files, unless the mode is specifically a developer/refactor mode.
*   **Backup:** Always have version control (like Git) in place before making significant changes or allowing AI agents to modify files broadly.

By carefully adjusting the `fileRegex` patterns, you can tailor this powerful mode set to integrate seamlessly with your specific project structures and documentation habits, while still benefiting from the organized workflow and context management provided by the `project_journal` system.
