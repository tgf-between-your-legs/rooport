# Plan: Mode Revisions for Flexible Workflow & Proactive Intent

## 1. Introduction

**Goal:** This document outlines a plan for revising existing Roo modes and potentially identifying new ones to implement the concepts defined in the following documents, aiming for a more flexible, adaptive, and user-friendly experience:

*   [../ideas/personas.md](../ideas/personas.md)
*   [../ideas/flexible_workflow_concept.md](../ideas/flexible_workflow_concept.md)
*   [../ideas/proactive_intent_roo_commander.md](../ideas/proactive_intent_roo_commander.md)

**Audience:** Roo Commander Developers/Maintainers

## 2. Analysis of Requirements

Based on the concept documents, the key requirements impacting mode design are:

*   **Proactive Intent (Roo Commander):** The `roo-commander` mode needs robust initial interaction logic to analyze user intent, map to personas/workflows, handle direct mode requests, ask clarifying questions, and optionally gather user context. (Note: Initial implementation completed in `roo-modes-dev/roo-commander.json`).
*   **Flexible Workflow Mechanisms:** Modes need to support:
    *   *Mode Switching:* Facilitated by the core system, but modes can suggest relevant next modes.
    *   *Optional Planning:* Modes like `code` or `project-initializer` should function without prior planning steps. `technical-architect` and `project-manager` should support being invoked later in the process.
    *   *Context Persistence:* `secretary` needs clear instructions for logging decisions, user details, task summaries, etc. All modes should leverage the `project_journal` where appropriate.
    *   *Retrospective Structuring:* `technical-architect`, `diagramer`, `project-manager`, `technical-writer` need to support documenting/planning based on *existing* code/work.
    *   *On-Demand Analysis:* `research-context-builder`, `discovery-agent`, `code-reviewer` should be easily invokable at various workflow stages.
    *   *Goal-Oriented Guidance:* Modes (especially `roo-commander`, but potentially others) should suggest logical next steps or modes based on context and completed actions.
    *   *Checkpointing:* `git-manager` plays a key role. `secretary` can log checkpoints.
*   **Persona Support:** Each defined persona (Planner, Vibe Coder, Adopter, Explorer, Brainstormer, Fixer, Learner, Documenter, Prototyper) relies on specific modes. We need to ensure these modes' instructions and capabilities align with the "How Roo Helps" descriptions in `personas.md`.

## 3. Proposed Mode Revisions

The following existing modes require review and potential revision:

*   **`roo-commander`:**
    *   **Status:** Initial revision implemented.
    *   **Action:** Verify implementation fully matches `proactive_intent_roo_commander.md`. Ensure robust handling of all paths (A-F) and optional detail gathering delegation.

*   **`project-onboarding`:**
    *   **Requirement:** Handle diverse entry points (Adopter, potentially Planner/Vibe Coder starting fresh). Needs to differentiate between setting up a new project vs. analyzing an existing one.
    *   **Action:** Revise `customInstructions` to include logic for detecting existing project structures vs. new project requests. Guide users accordingly, potentially delegating to `project-initializer` for new projects or `research-context-builder` for existing ones after initial setup/verification.

*   **`discovery-agent`:**
    *   **Requirement:** Support "Explorer" and "Brainstormer" personas. Needs to go beyond simple search/retrieval to stimulate ideas and ask probing questions.
    *   **Action:** Enhance `customInstructions` to include techniques for idea generation (e.g., asking "what if", suggesting related domains, prompting for different angles) and structured brainstorming support (e.g., suggesting a mind map structure for `diagramer`).

*   **`research-context-builder`:**
    *   **Requirement:** Core tool for "Adopter", "Explorer", "Fixer".
    *   **Action:** Review `customInstructions` to ensure they emphasize summarizing code, identifying components, and analyzing dependencies effectively for users needing to understand existing codebases quickly.

*   **`technical-architect`:**
    *   **Requirement:** Support "Planner" and retrospective structuring ("Vibe Coder").
    *   **Action:** Update `customInstructions` to explicitly mention the ability to document *existing* designs (not just plan new ones). Emphasize interaction with `diagramer` for visualization and `project-manager` for task breakdown (either before or after coding). Ensure file permissions (`\\.md$`) are appropriate for planning/documentation outputs.

*   **`project-manager`:**
    *   **Requirement:** Support "Planner" and optional/retrospective planning.
    *   **Action:** Revise `customInstructions` to handle task creation/management both before implementation (planning) and after (organizing completed work). Ensure integration with `project_journal` for task lists.

*   **`secretary`:**
    *   **Requirement:** Central role in context persistence.
    *   **Action:** Enhance `customInstructions` to clearly define its role in logging: key decisions (ADR format), task summaries, user profile details (if provided), workflow checkpoints, errors/failures reported by other modes. Define standard locations within `project_journal` (e.g., `/tasks`, `/decisions`, `/context`).

*   **`diagramer`:**
    *   **Requirement:** Support "Planner", "Brainstormer", retrospective documentation.
    *   **Action:** Update `customInstructions` to include support for different diagram types relevant to these tasks (e.g., mind maps for brainstorming, flowcharts/sequence diagrams for existing logic).

*   **`project-initializer`:**
    *   **Requirement:** Support "Vibe Coder", "Learner", "Prototyper" needing quick starts.
    *   **Action:** Ensure `customInstructions` focus on creating minimal, runnable project skeletons quickly based on user requests (e.g., basic web app, simple API, specific framework).

*   **`code` / Specialist Modes (e.g., `react-specialist`, `api-developer`):**
    *   **Requirement:** Support flexible workflow via suggestions.
    *   **Action:** Consider adding optional suggestions in `customInstructions` or `attempt_completion` logic. E.g., after successfully writing code, suggest related next steps: "Code saved. Consider: documenting (Technical Writer), refactoring (Refactor Specialist), or writing tests (Integration Tester)?". This needs careful implementation to avoid being overly chatty.

## 4. Proposed New Modes (If Any)

Based on the analysis, the current set of modes seems reasonably comprehensive, especially with the revisions above. The "Brainstormer" persona can likely be supported by enhancing `discovery-agent` and `diagramer`. An "Ask" mode for general Q&A/learning could be valuable but might overlap with `discovery-agent` or specific specialist modes; this warrants further consideration based on usage patterns.

*   **Recommendation:** Focus on revising existing modes first. Re-evaluate the need for new modes after observing the revised system in action.

## 5. Cross-Mode Interaction Strategy

*   **Suggestions:** Modes should primarily suggest transitions via `ask_followup_question` upon task completion or at logical decision points identified in their instructions. `roo-commander` handles the initial workflow suggestion.
*   **Context:** The `project_journal`, managed actively by `secretary`, `project-manager`, `technical-writer`, etc., serves as the primary shared context. Modes like `research-context-builder` or `context-resolver` can be used to query this context.
*   **Delegation:** `roo-commander` remains the primary delegator using `new_task`. Modes should focus on their core competency and report results clearly.

## 6. Implementation Considerations

*   **Priority:**
    1.  Verify `roo-commander` implementation.
    2.  Revise `project-onboarding`, `discovery-agent`, `secretary`, `technical-architect`, `project-manager`.
    3.  Revise other modes (`research-context-builder`, `diagramer`, `project-initializer`).
    4.  Consider adding suggestions to `code`/specialist modes (lower priority).
*   **Testing:** Test each revised mode individually, then test end-to-end workflows for each key persona.

## 7. Conclusion

This plan outlines necessary revisions to align existing Roo modes with the flexible workflow and proactive intent concepts. By enhancing modes like `roo-commander`, `project-onboarding`, `discovery-agent`, and `secretary`, and ensuring others support optional/retrospective actions, we can create a significantly more adaptive and user-friendly experience. The next step is to review this plan and then proceed with implementing the proposed revisions.