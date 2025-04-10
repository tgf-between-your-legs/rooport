# Proposed Refinements: Tool Usage Guidance in Roo Commander Instructions

**Date:** 2025-04-08
**Related Mode:** `roo-modes-dev/roo-commander.json`
**Related Analysis:** Discussion on `write_to_file` and `apply_diff` usage based on tool documentation.

## 1. Goal

To refine the `customInstructions` within `roo-commander.json` to provide clearer and more appropriate guidance on using file modification tools, particularly `write_to_file`, aligning better with documented best practices and tool capabilities.

## 2. Identified Issue

The current `customInstructions` contain potentially problematic guidance in the **Formal Document Maintenance** section:

```
**Formal Document Maintenance:**
- **Responsibility:** Oversee high-level docs in `project_journal/planning/` or `project_journal/formal_docs/`.
- **Guidance:** Save/update these documents using `write_to_file`.
```

The issue lies with instructing the Commander to **"update"** existing documents using `write_to_file`. According to the tool's documentation (`project_journal/knowledge/write-to-file.md`):
*   `write_to_file` completely overwrites existing files.
*   It is "Not suitable for existing files" and "Much slower and less efficient than `apply_diff` for modifying existing files".
*   Performance degrades significantly with larger files.

Instructing the Commander to use `write_to_file` for updates encourages an inefficient workflow (read entire file, modify, write entire file) that is prone to errors, especially with potentially large planning or formal documents.

## 3. Proposed Change to `customInstructions`

Modify the **Formal Document Maintenance** section as follows:

**Current:**

```
**Formal Document Maintenance:**
- **Responsibility:** Oversee high-level docs in `project_journal/planning/` or `project_journal/formal_docs/`.
- **Guidance:** Save/update these documents using `write_to_file`.
```

**Proposed:**

```diff
 **Formal Document Maintenance:**
 - **Responsibility:** Oversee high-level docs in `project_journal/planning/` or `project_journal/formal_docs/`.
+- **Guidance (Create):** Create *new* formal documents using `write_to_file`.
+- **Guidance (Update):** For *updates* to existing formal documents, prefer delegating the update task to a relevant specialist (e.g., `technical-writer`). If direct, minor modifications are necessary, consider using `apply_diff` or `insert_content` for targeted changes. **Avoid using `write_to_file` to update large existing documents.**
- **Guidance:** Save/update these documents using `write_to_file`.

```

## 4. Rationale

*   **Alignment:** This change aligns the guidance with the documented strengths and weaknesses of `write_to_file` (for creation/overwrite) and other editing tools (`apply_diff`, `insert_content` for targeted modifications).
*   **Efficiency:** Prevents the Commander from attempting inefficient full read/write cycles for simple updates to large files.
*   **Reduced Risk:** Minimizes the chance of errors associated with handling large file content for overwrites and potential state confusion from inefficient operations.
*   **Role Reinforcement:** Encourages the Commander's primary role as a coordinator by suggesting delegation for complex updates.

## 5. Other Notes

*   The `customInstructions` currently lack explicit guidance for the Commander to use `apply_diff` itself. While the proposed change mentions it as an option for *minor* direct updates, the primary path remains delegation, which is consistent with the Commander's role.
*   The usage guidance for `write_to_file` for creating decision records and user profiles remains appropriate.

## 6. Next Steps

Review these proposed changes. If approved, update the `customInstructions` within the `roo-modes-dev/roo-commander.json` file accordingly.