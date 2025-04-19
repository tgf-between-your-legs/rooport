# Information Extraction Tips for Context Resolver

These tips help in efficiently extracting key information from common project artifact types.

## MDTM Task Files (`.tasks/**/*.md`)

*   **Primary Goal:** Look for the `title` field in the TOML frontmatter. Also check for a `## Goal` or `## Description` section in the Markdown body.
*   **Current Status:** Check the `status` field in the TOML frontmatter (e.g., `status = "🟡 To Do"`).
*   **Assignee:** Check the `assigned_to` field in the TOML frontmatter.
*   **Blockers:** Scan the Markdown body for sections like `## Blockers`, `## Issues`, or keywords like "blocked", "waiting for", "cannot proceed". Also check if `status` is `"⚪ Blocked"`.
*   **Recent Activity:** Look for dated entries or `## Log` sections in the Markdown body. Check the `updated_date` in the TOML frontmatter.
*   **Next Steps:** Scan the Markdown body for sections like `## Next Steps` or concluding remarks.
*   **Related Items:** Check `depends_on` and `related_docs` arrays in the TOML frontmatter.

## Architecture Decision Records (ADRs) (`.decisions/*.md`)

*   **Decision:** Look for a clear statement of the decision, often under a heading like `## Decision` or `## Resolution`.
*   **Date:** Check the filename (often dated) or metadata within the ADR (e.g., `Date:` field).
*   **Status:** Look for a `Status:` field (e.g., `Proposed`, `Accepted`, `Superseded`).
*   **Context/Problem:** Read the `## Context` or `## Problem Statement` section.
*   **Options:** Look for sections like `## Options Considered` or similar.
*   **Justification/Consequences:** Read sections like `## Rationale`, `## Justification`, `## Consequences`.

## Planning Documents (`.planning/*.md`)

*   **Overall Vision/Goals:** Look for introductory sections, `## Goals`, `## Vision`.
*   **Roadmap/Phases:** Scan for headings related to timelines, phases, quarters (Q1, Q2), or milestones.
*   **Requirements:** Look for specific requirement IDs, user stories, or functional descriptions, often in lists or tables.
*   **Architecture Overview:** Check for high-level descriptions of components and their interactions, potentially linking to diagrams or ADRs.

## General Tips

*   **Use Emojis:** Leverage the standard emojis (🎯, 📄, 💡, 🧱, ➡️) defined in the summary templates for quick identification.
*   **Scan Headings:** Use Markdown headings (`##`, `###`) to quickly navigate document structure.
*   **Focus on Query:** Extract only the information directly relevant to the user's query. Avoid including tangential details.
*   **Cite Sources:** Always mention the source file (`(from [filename])`) for each piece of information.
*   **Be Concise:** Summarize findings briefly. Use bullet points. Avoid long paragraphs.
*   **Note Missing Info:** If a relevant file cannot be read or information isn't found, explicitly state this limitation.