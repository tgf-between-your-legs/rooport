# Summary Templates for Context Resolver

These templates provide standard structures for common summary requests. Adapt them based on the specific query and available information. Always cite sources.

## Template: Task Status Summary

```markdown
**Context Summary (re: Task [TaskID]):**
*   🎯 **Goal:** [Extract goal/title from task TOML `title` or Markdown body] (from `[source_task_file.md]`)
*   📄 **Status:** [Extract status from task TOML `status`] (from `[source_task_file.md]`)
*   🧑‍💻 **Assigned:** [Extract assignee from task TOML `assigned_to`] (from `[source_task_file.md]`)
*   📝 **Latest Update/Notes:** [Summarize recent activity or key notes from Markdown body, if available] (from `[source_task_file.md]`)
*   🧱 **Blockers:** [Summarize any noted blockers from Markdown body, if available] (from `[source_task_file.md]`)
*   ➡️ **Next Steps:** [Summarize any explicit next steps from Markdown body, if available] (from `[source_task_file.md]`)
*   🔗 **Related:** [List `related_docs` or `depends_on` from TOML, if relevant] (from `[source_task_file.md]`)
*   *(Note: [Mention any critical source files that couldn't be read, e.g., requirements.md])*
```

## Template: Decision Summary

```markdown
**Context Summary (re: Decision on [Topic]):**
*   💡 **Decision:** [Summarize the core decision made] (from `[source_adr_file.md]`)
*   📅 **Date:** [Extract date from ADR filename or metadata] (from `[source_adr_file.md]`)
*   🤔 **Context/Problem:** [Briefly summarize the problem addressed] (from `[source_adr_file.md]`)
*   ⚖️ **Options Considered:** [List options briefly, if available] (from `[source_adr_file.md]`)
*   ✅ **Justification:** [Summarize the key reasons for the decision] (from `[source_adr_file.md]`)
*   🚀 **Consequences/Implications:** [Summarize expected consequences] (from `[source_adr_file.md]`)
*   *(Note: [Mention any related planning docs that couldn't be read])*
```

## Template: Mode Capability Summary

```markdown
**Context Summary (re: Mode `[mode_slug]`):**
*   🎯 **Purpose:** [Summarize mode's primary function/description] (from `[source_mode_file.md]`)
*   🛠️ **Key Capabilities:** [List 3-5 core capabilities] (from `[source_mode_file.md]`)
*   🔄 **Typical Workflow:** [Summarize high-level workflow steps] (from `[source_mode_file.md]`)
*   📚 **Context/Knowledge:** [Mention key context files it uses, if listed] (from `[source_mode_file.md]` or `custom-instructions/README.md`)
*   🔗 **Collaboration:** [Note key modes it delegates to, escalates to, or reports to] (from `[source_mode_file.md]`)
*   *(Note: [Mention if specific custom instruction files were unreadable])*
```

## Template: General Project Status Snippet

```markdown
**Project Status Snippet:**
*   **Overall Goal:** [Extract from `.planning/project_vision.md` or similar]
*   **Current Phase:** [Extract from `.planning/project_plan.md` or infer from active tasks]
*   **Recent Decisions:** [Summarize 1-2 key recent decisions from `.decisions/`]
*   **Active Blockers:** [Summarize any major blockers noted in recent `.tasks/` files]
*   *(Note: Based on reading [list key files read].)*
```

*(Adapt these templates based on the specific query. Prioritize conciseness and accurate source citation.)*