## Proposal: Adapting MDTM to use TOML Frontmatter

**Version:** 1.0
**Date:** 2025-04-14

**1. Goal:**

To modify the existing MDTM - Feature Structure specification to utilize **TOML** (Tom's Obvious, Minimal Language) for the structured metadata (frontmatter) section of each task file, replacing the current implicit or explicit YAML frontmatter. The goal is to retain the benefits of human readability while improving parsing robustness and reducing ambiguity compared to YAML, especially for automated processing by scripts and AI.

**2. Core Proposal:**

Replace the use of YAML (`--- ... ---`) for the frontmatter block in every task `.md` file (`tasks/**/*.md`) with TOML syntax. The Markdown body content, including GFM checklists, descriptions, etc., will remain unchanged.

**3. Detailed Changes to Frontmatter Implementation:**

*   **Removal of Delimiters:** TOML does not use `---` delimiters. The TOML metadata block will simply start at the beginning of the file and end before the first Markdown heading (`#`) or main body content.
*   **Syntax Change:** Replace `key: value` syntax with `key = value`.
*   **Strings:** Standard strings will be enclosed in double quotes (`"`). Escaping rules are simpler than YAML.
    ```toml
    title = "Implement Login UI (Vue)"
    assigned_to = "🤖 AI"
    ```
*   **Multi-line Strings:** For fields like `ai_prompt_log` or potentially long descriptions moved to frontmatter (not recommended), use triple double-quotes (`"""`).
    ```toml
    ai_prompt_log = """
    Prompt 1: Generate component structure...
    Prompt 2: Refine styling based on related_docs...
    """
    ```
*   **Arrays (Lists):** Use square brackets `[]` with comma-separated values. This is crucial for `tags`, `depends_on`, `related_docs`, `review_checklist`. Values inside should be strings (or other TOML types as appropriate).
    ```toml
    tags = ["ui", "vue", "auth", "critical"]
    depends_on = ["FEAT-AUTH-002", "API-TASK-010"]
    related_docs = ["docs/PRD.md#login-reqs", "docs/API.md#auth"]
    # Empty list:
    review_checklist = []
    ```
*   **Dates:** Represent dates as TOML strings using the `YYYY-MM-DD` format for consistency with your current spec and simplest parsing, although native TOML dates are also possible.
    ```toml
    created_date = "2025-04-05"
    updated_date = "2025-04-14"
    # Optional native date (requires parser support):
    # due_date = 2025-04-20
    ```
*   **Comments:** Use the hash symbol (`#`) for comments. These are useful for adding explanations directly within the metadata.
    ```toml
    # 🆔 Task Identification & Core Metadata
    id = "FEAT-AUTH-001" # REQUIRED. Unique ID (e.g., FEAT-AUTH-001, BUG-123).
    ```
*   **Booleans/Integers/Floats:** Use standard TOML syntax (`true`, `false`, `123`, `1.23`) if these types are needed for fields like `estimated_effort` (if points) or potential future boolean flags.

**4. Example TOML Frontmatter Block (Based on `implementing.md`):**

```toml
# ⬇️ Start of TOML Frontmatter ⬇️

# 🆔 Task Identification & Core Metadata
id = "FEAT-AUTH-001"             # REQUIRED. Unique ID (e.g., FEAT-AUTH-001, BUG-123). Convention: {TYPE_PREFIX}-{FEATURE_NAME_ABBR}-{NNN}
title = "Implement Login UI (Vue)" # REQUIRED. Human-readable title (String).
status = "🟡 To Do"              # REQUIRED. Current workflow state (String, from standard list). See Statuses below.
type = "🌟 Feature"              # REQUIRED. Category of work (String, from standard list). See Types below.

# ⏳ Scheduling & Effort
priority = "🔼 High"             # Recommended. Task importance (String, from standard list). See Priorities below.
created_date = "2025-04-05"      # Recommended. Date created (YYYY-MM-DD String).
updated_date = "2025-04-14"      # Recommended. Date last modified (YYYY-MM-DD String).
due_date = "2025-04-12"          # Optional. Target completion date (YYYY-MM-DD String).
estimated_effort = "M"           # Optional. Size estimate (String/Number). E.g., "M", "L", "3", "5"

# 🧑‍💻 Assignment & Responsibility
assigned_to = "🤖 AI"             # Recommended. Who tackles the next action (String). "🤖 AI", "🧑‍💻 User:Alice", "👥 Team:Frontend"
reporter = "🧑‍💻 User:Bob"          # Optional. Who created/reported the task (String). (Especially for Bugs)

# 🔗 Relationships & Context
parent_task = "FEATURE_authentication/_overview.md" # Optional. Path/ID of parent feature/epic (String).
depends_on = ["FEAT-AUTH-002"]   # Optional. List of task IDs this waits for (List of Strings). Empty: []
related_docs = ["docs/PRD.md#login-reqs", "docs/API.md#auth"] # Optional. Links to external docs/sections (List of Strings). Empty: []
tags = ["ui", "vue", "auth", "critical"] # Optional. Keywords for filtering (List of Strings). Empty: []

# 🤖 AI & Review Specific Fields
ai_prompt_log = """
Generate component X...
Refine Y...
"""  # Optional. Log of key prompts used (Multiline String or List of Strings).
review_checklist = ["[ ] Code Style", "[ ] Tests Pass"] # Optional. Standard review checks (List of Strings). Empty: []
reviewed_by = "🧑‍💻 User:Charlie"   # Optional. Who reviewed the task (String).

# ⬆️ End of TOML Frontmatter ⬆️

# Start of Markdown Body
# ======================

# Implement Login UI (Vue)

## Description ✍️
... Markdown Body ...

## Acceptance Criteria ✅
- [ ] Criterion 1
- [ ] Criterion 2

## Implementation Notes / Sub-Tasks 📝
... etc ...
```


It is crucial to use the following standardized string values and associated emojis within the TOML frontmatter fields for consistency and visual parsing. These definitions remain unchanged from the original MDTM specification.

4.1. Statuses (status field)

⚪ Blocked: 🚧 Cannot proceed (explain why in body).

🟡 To Do: 📥 Ready to be started.

🔵 In Progress: 🏗️ Actively being worked on (human).

🤖 Generating: ✨ AI actively generating code/content.

🟣 Review: 👀 Output needs human review.

🧪 Testing: 🔬 Passed review, undergoing tests.

🟢 Done: ✅ Completed, verified, merged.

4.2. Types (type field & Filename Emoji)

The type field uses the full string (e.g., "🌟 Feature"). The corresponding emoji is also used in the filename (NNN_➕_short_description.md).

🌟 Feature: (_➕_ in filename) New user-facing functionality.

🐞 Bug: (_🐞_ in filename) Fixing incorrect behavior.

🧹 Chore: (_🧹_ in filename) Maintenance, refactoring, updates, non-visible improvements.

📖 Documentation: (_📖_ in filename) Writing or updating docs.

🧪 Test: (_🧪_ in filename) Creating or improving tests.

🎨 UI/UX: (_🎨_ in filename) Design or user experience improvements.

💡 Spike/Research: (_💡_ in filename) Investigation or technical exploration.

🗺️ Epic/Overview: (_🗺️_ in filename) High-level feature summary file (_overview.md).

4.3. Priorities (priority field)

🔥 Highest: Must be done immediately.

🔼 High: Important, tackle soon.

▶️ Medium: Normal priority.

🔽 Low: Can wait, optional.

🧊 Lowest: Icebox, do if time permits.




**5. What Stays the Same in MDTM:**

*   **Folder Structure:** `tasks/`, `tasks/FEATURE_xxx/`, `tasks/_templates/`, `archive/` conventions remain.
*   **File Naming:** `NNN_➕_short_description.md` convention remains.
*   **Markdown Body:** All content *after* the TOML block remains standard GFM Markdown. Headings (`## Description`, `## Acceptance Criteria`), checklists (`- [ ]`), embedded diagrams, etc., are unchanged.
*   **Workflow Logic:** The defined statuses (`🟡 To Do`, `🟢 Done`, etc.) and the overall task lifecycle remain the same conceptually.
*   **Linking Logic:** The *meaning* and use of `parent_task`, `depends_on`, `related_docs` remain the same; only the syntax of the list in the frontmatter changes.
*   **Standardized Values & Emojis:** The defined lists for `status`, `type`, `priority` and their associated emojis remain essential for consistency.

**6. Benefits of Switching to TOML:**

*   **Improved Robustness vs. YAML:** Eliminates errors caused by sensitivity to indentation. Parsing is less ambiguous.
*   **Better Readability vs. JSON:** Retains much of the human-friendly aspect of YAML, includes comments, and avoids JSON's syntactic noise (excessive quotes, commas, braces).
*   **Clear Structure:** Explicit syntax for tables (if needed later), arrays, and key-value pairs is easy for both humans and AI/scripts to follow.
*   **Good Fit for Metadata:** TOML was designed for configuration/metadata, making it conceptually well-suited for this task.

**7. Potential Drawbacks/Considerations:**

*   **Tooling:** Requires ensuring your parsing scripts (e.g., `populate_roomodes.js` if it reads tasks) and potentially IDE integrations use a TOML parsing library (many good ones exist for Node.js, Python, etc., but it's an extra dependency compared to potentially built-in JSON).
*   **Migration Effort:** Existing task files will need their frontmatter converted from YAML to TOML. This could be done manually or via a migration script.
*   **Familiarity:** Team members and AI might be slightly less familiar with TOML than with JSON or YAML, though it's generally easy to learn.

**8. Implementation Steps:**

1.  **Decision & Communication:** Confirm the switch to TOML and inform any relevant team members or stakeholders.
2.  **Update Documentation:** Modify `implementing.md` and `README.md` to reflect the TOML syntax, replacing YAML examples. Update the standard field definitions if needed.
3.  **Update Templates:** Convert the `.md` files in `tasks/_templates/` to use TOML frontmatter.
4.  **Develop Migration Strategy:**
    *   **Option A (Scripted):** Write a script to read existing `.md` files, parse the YAML frontmatter, and rewrite the files with TOML frontmatter. **(Recommended for many files)**
    *   **Option B (Manual):** Manually edit existing task files to convert the frontmatter syntax. (Feasible for a small number of tasks).
5.  **Execute Migration:** Run the script or perform the manual conversion.
6.  **Update Parsing Logic:** Modify any scripts (like `populate_roomodes.js`) or IDE tools that read the task frontmatter to use a TOML parser instead of a YAML parser.
7.  **Create/Update AI Context:** Develop the concise "MDTM TOML Context for AI" document (as discussed previously) to guide AI interactions. Ensure relevant AI modes reference this new context.
8.  **Testing:** Thoroughly test the updated system: task creation from templates, AI reading/updating tasks, script parsing, IDE integration (if any).
9.  **Rollout:** Merge changes and begin using TOML frontmatter for all new and existing tasks.

**9. Updated Context for AI:**

A dedicated context file for the AI modes will be crucial, explaining:
*   That frontmatter is TOML.
*   The basic TOML syntax used (`key = value`, `""`, `[]`, `#`).
*   The specific fields defined in the MDTM spec.
*   An example TOML block specific to MDTM.
*   Instructions on how to read/update the TOML block correctly.

**10. Conclusion:**

Adapting MDTM to use TOML frontmatter offers a compelling balance between human readability and machine parsing robustness. It directly addresses potential ambiguities found in YAML while avoiding the verbosity of JSON. By following the outlined steps, you can transition your sophisticated MDTM system to TOML, creating a clearer, potentially more reliable foundation for managing tasks directly within your repository, especially when interacting with AI assistants and automated tooling.