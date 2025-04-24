+++
# --- Metadata ---
id = "PLAN-KB-ENRICH-PHASE4-V1"
title = "KB Enrichment Plan: Phase 4 - Mode Integration"
status = "draft"
created_date = "2025-04-24"
updated_date = "2025-04-24"
version = "1.0"
tags = ["plan", "kb", "enrichment", "phase4", "integration", "modes", "prompts"]
related_docs = [".ruru/planning/kb-enrichment/00-kb-enrichment-plan.md"]
objective = "Update the target specialist mode's configuration and prompts to enable it to discover and utilize its newly enriched knowledge base."
scope = "Modifying the mode's `.mode.md` file."
# --- Plan Specific Fields ---
target_mode_file_template = ".ruru/modes/{mode_slug}/{mode_slug}.mode.md"
target_mode_kb_index_template = ".ruru/modes/{mode_slug}/kb/index.toml" # Master index for the mode
+++

# KB Enrichment Plan: Phase 4 - Mode Integration

**Objective:** Instruct the target specialist mode (e.g., `framework-astro`) on how to access and use the synthesized knowledge base created in the previous phases.

**Procedure (for a given `[mode_slug]`):**

1.  **Update Mode Definition File (Delegate to `prime-coordinator` or `util-mode-maintainer`):**
    *   Tool: `new_task`
    *   Mode: `prime-coordinator` (safer for config changes) or `util-mode-maintainer`.
    *   Message: "Modify the mode definition file `[target_mode_file_template]`.
        *   **Update `system_prompt` / Role:** Add text explaining that the mode has access to a specialized, synthesized knowledge base for specific libraries located in its `kb/` directory. Instruct it to consult this KB for core concepts, API overviews, patterns, etc., related to those libraries *before* relying solely on general knowledge or external search.
        *   **Add KB Index to `related_context`:** Ensure the path to the mode's master KB index (`[target_mode_kb_index_template]`) is listed in the `related_context` array within the mode's TOML frontmatter.
        *   **Add Specific Library KB to `related_context` (Optional):** If the mode *always* needs context for a primary library (e.g., `framework-astro` always needs Astro context), consider adding the specific library index `kb/[library_name]/index.toml` to `related_context` as well for easier access, but the master index is generally preferred for discoverability.
    *   Action: Delegate task. Await confirmation. Handle errors.

2.  **Add Mode-Specific KB Usage Rule (Optional - Alternative to Prompt Update):**
    *   Alternatively, create a rule specific to the mode (e.g., in `.roo/rules-[mode_slug]/01-use-internal-kb.md`) that explicitly instructs it:
        *   "When performing tasks related to library X, first consult your internal knowledge base index at `kb/index.toml`."
        *   "Use the index to find relevant synthesized documents (e.g., `core-concepts.md`, `api-overview.md`)."
        *   "Use `read_file` to load the content of these documents into your context."
        *   "Prioritize information from this internal KB over general knowledge."
    *   Ensure this rule is loaded by the mode.

**Completion:** The target specialist mode is now configured and instructed to utilize its enriched knowledge base.

**Verification:** Test the mode by giving it tasks related to the library for which the KB was enriched. Observe if it references consulting its internal KB (`read_file` on files within its `kb/` directory) during its reasoning process.