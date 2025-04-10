# Roo Mode System Improvement Strategy (v6.3)

## Introduction

Based on the analysis of individual modes within `roo-modes-dev/` and the previous investigation into the Tailwind setup failure, this document outlines a strategic approach to enhance the overall effectiveness, collaboration, and robustness of the Roo multi-mode system. The core goal is to move towards a more proactive, context-aware, and specialist-driven workflow, reducing reliance on explicit user intervention for optimal task execution.

Individual mode improvement suggestions can be found in `v6.3/improvements/`.

## Overarching Strategic Aims

1.  **Maximize Specialist Utilization:** Proactively identify opportunities to leverage specialist modes based on project context and task requirements, rather than waiting for user requests or encountering failures with generalist modes.
2.  **Enhance Context Awareness:** Ensure all modes, especially Roo Commander and delegating modes, have accurate, up-to-date context about the project's technical stack, dependencies, and ongoing task statuses before making decisions or assigning work.
3.  **Standardize Collaboration & Escalation:** Define clear, consistent pathways for modes to delegate sub-tasks, request assistance, or escalate issues they cannot handle effectively.
4.  **Increase System Robustness:** Minimize errors caused by modes operating outside their core expertise or lacking necessary context (e.g., incorrect build commands, framework misuse). Improve error handling and reporting across modes.
5.  **Maintain User Control & Transparency:** Balance increased automation with mechanisms for user oversight, intervention, and understanding of the system's actions.

## Core Implementation Strategies

To achieve the strategic aims, the following core changes and enhancements are recommended:

1.  **Mandatory & Enhanced Discovery Phase:**
    *   **Action:** The `project-onboarding` mode MUST always delegate to the `discovery-agent` at the beginning of any project interaction (new or existing).
    *   **Action:** The `discovery-agent` MUST be enhanced to perform **automated analysis** (reading configs, scanning files for keywords/imports) in addition to user interaction.
    *   **Output:** Discovery Agent will produce a **Stack Profile** (listing detected languages, frameworks, tools, databases, potential specialists) alongside the **Requirements Document**.
    *   **Rationale:** Provides essential, verified context about the technical landscape *before* major planning or delegation occurs, preventing incorrect assumptions (like the Tailwind issue).

2.  **Metadata-Driven Delegation (`tags`):**
    *   **Action:** Implement a `tags` array (e.g., `["react", "frontend", "ui-library"]`) in the JSON definition of *all* modes, accurately reflecting their core competencies and associated technologies.
    *   **Action:** Roo Commander (and potentially Project Manager or other coordinating modes) will use these tags, matched against the Stack Profile from the Discovery Agent, to identify the most suitable specialist(s) for a given task or sub-task.
    *   **Rationale:** Enables automated, intelligent matching of tasks to expert modes.

3.  **Dynamic Task Splitting & Proactive Delegation:**
    *   **Action:** Enhance Roo Commander's `Delegate Tasks` logic (Phase 2, Step 7). After receiving the Stack Profile, Commander should analyze upcoming tasks and proactively **split larger goals** into sub-tasks aligned with specialist capabilities identified via tags.
    *   **Action:** Delegate these sub-tasks directly to the relevant specialists.
    *   **Example:** If a task involves creating a React component styled with Tailwind and fetching data from a Supabase backend, Commander (using the Stack Profile) should delegate:
        *   Component structure/logic to `react-specialist`.
        *   Styling to `tailwind-specialist`.
        *   Backend interaction setup (if needed beyond simple fetching) to `supabase-developer`.
    *   **Rationale:** Ensures the right expert handles the right part of the job from the start, improving quality and efficiency.

4.  **Clear Escalation Pathways:**
    *   **Action:** Update `customInstructions` for all modes to define clear scenarios where they should **escalate** (e.g., task complexity exceeds capability, missing critical information, encountering errors outside their domain) and **to whom** (e.g., escalate complex DB issues to `database-specialist`, architectural conflicts to `technical-architect`, unresolved bugs to `complex-problem-solver`).
    *   **Rationale:** Provides explicit guidance for modes when they hit limitations, preventing them from getting stuck or producing suboptimal results.

5.  **Improved Context Management:**
    *   **Action:** Encourage more frequent use of `context-resolver` by coordinating modes (Commander, PM) before delegating complex or dependent tasks.
    *   **Action:** Ensure task delegation messages (`new_task`) include not only the goal and acceptance criteria but also references to relevant context files (requirements, architecture docs, ADRs, previous task logs, Stack Profile).
    *   **Rationale:** Reduces the chance of modes operating with outdated or incomplete information.

6.  **Comprehensive Context Indices:**
    *   **Action:** Ensure all specialist modes have high-quality, up-to-date Condensed Context Indices embedded in their `customInstructions`. Regenerate the Tailwind index.
    *   **Action:** Establish a process for regularly updating these indices or generating new ones via `context-condenser` as technologies evolve.
    *   **Rationale:** Improves specialist mode performance and robustness, especially when external documentation access is limited.

7.  **Robust Testing & Verification:**
    *   **Action:** Strengthen instructions for all modes performing code modifications to **run existing tests** after changes.
    *   **Action:** Define clear procedures for `refactor-specialist` and `bug-fixer` when tests are missing or fail (block vs. proceed with caution/characterization tests).
    *   **Rationale:** Prevents regressions and ensures code changes are safe.

## Cross-Cutting Considerations

*   **Mode Granularity:** Continuously evaluate if the current set of specialists is appropriate. Is there a need for new specialists (e.g., State Management, Webpack, specific DBs)? Are some modes too broad or too narrow?
*   **Handling Unknown Technologies:** Define a fallback strategy when the Discovery Agent detects technologies for which no specialist mode exists. This likely involves delegating to generalist modes (Frontend/Backend Developer) with clear notification of the potential knowledge gap.
*   **User Experience:** While automating delegation, ensure the process remains transparent. Roo Commander should clearly communicate *why* specific specialists are being chosen. Provide mechanisms for the user to override or guide specialist selection if desired.
*   **Maintenance:** Implementing tags and improved instructions requires an initial effort across all modes. A process for keeping tags, context indices, and escalation logic up-to-date as the mode library evolves is necessary.
*   **System Testing:** Develop scenarios to test the improved orchestration logic, ensuring correct specialist identification, delegation, and escalation occur as expected.

## Conclusion

Implementing these strategic improvements – centered around enhanced discovery, metadata-driven delegation, and clear escalation paths – will transform the Roo mode system from a primarily reactive model to a more proactive, intelligent, and collaborative ecosystem. This will leverage specialist expertise more effectively, reduce errors, improve efficiency, and ultimately lead to higher quality project outcomes.