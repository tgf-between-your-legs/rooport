# Further Improvements: Towards a More Collaborative Project Onboarding

**Date:** 2025-04-08
**Related Mode:** `roo-modes-dev/project-onboarding.json`
**Related Document:** `v6.0/changes/project-onboarding-context-awareness-improvement.md`

## 1. Goal

Building upon the idea of context-awareness, this document explores further enhancements to the `project-onboarding` mode. The goal is to transform it from a mostly deterministic process into a more collaborative and adaptive interaction that better leverages the user's initial request and offers more flexibility throughout the onboarding phase.

## 2. Current Limitations Recap

*   **Rigid Flow:** Follows a fixed path for "new" vs. "existing".
*   **Limited Context Use:** Doesn't fully utilize details potentially present in the initial user request (e.g., project name, technology).
*   **Assumptions:** Makes assumptions about delegation (e.g., always delegating requirements gathering immediately).
*   **Deterministic Questions:** Asks predefined questions without adapting them based on context.

## 3. Proposed Areas for Improvement

### 3.1. Enhanced Initial Intent Handling

*   **(As previously discussed)** Analyze the incoming message from Commander to potentially skip the "new vs. existing" question if intent is clear.
*   **Extract & Propose Details:**
    *   If the initial request mentions a potential project name (e.g., "website for 'All About Brick Laying'"), *propose* it instead of asking blankly: `ask_followup_question` "Should we name this new project 'all-about-brick-laying' (based on your request)? <suggest>Yes, use 'all-about-brick-laying'</suggest> <suggest>No, let me provide a different name</suggest>".
    *   If the request mentions technology (e.g., "new React app"), store this information to potentially influence later steps (like initialization).
*   **Nuanced Clarification for Ambiguity:** If intent is unclear, instead of just "new vs. existing", offer more specific options based on keywords: `ask_followup_question` "Your request mentions 'API'. Are you looking to: <suggest>Start a new API project from scratch?</suggest> <suggest>Work on an existing API project in this directory?</suggest> <suggest>Just discuss API design ideas?</suggest>".

### 3.2. More Flexible New Project Workflow

*   **User Control over Requirements:** After confirming a new project and getting a name, ask the user *how* they want to proceed with requirements: `ask_followup_question` "Project '[name]' is ready. How should we handle requirements? <suggest>Gather detailed requirements now (via Discovery Agent)</suggest> <suggest>Proceed with a basic setup first, requirements later</suggest> <suggest>Skip formal requirements for now</suggest>". This avoids immediate, potentially unwanted, delegation to `discovery-agent`.
*   **Initialization Choices:** Before delegating to `project-initializer`, offer choices based on context or ask:
    *   If technology was mentioned initially (e.g., React): `ask_followup_question` "Should I initialize a standard React project structure? <suggest>Yes, initialize a React project</suggest> <suggest>No, initialize a basic HTML/CSS structure</suggest> <suggest>No, let me choose a different type</suggest>".
    *   If no tech mentioned: `ask_followup_question` "What kind of project structure should I initialize? <suggest>Basic HTML/CSS/JS</suggest> <suggest>Standard React (Vite)</suggest> <suggest>Standard Python (Flask/Django - specify)</suggest> <suggest>Just the project journal and core files</suggest>".
    *   The chosen type would then be passed in the message to `project-initializer`.

### 3.3. Smarter Existing Project Analysis

*   **Expanded File Checks:** Look for a wider range of common project files (`docker-compose.yml`, `requirements.txt`, `go.mod`, `pom.xml`, `build.gradle`, specific framework configs) to improve type inference.
*   **Confirm Inferred Type:** Instead of just stating the summary, ask for confirmation: `ask_followup_question` "Based on `package.json` and `next.config.js`, this looks like a Next.js project. Is that correct? <suggest>Yes, that's correct</suggest> <suggest>No, it's something else</suggest>".
*   **Targeted Questions on Missing Info:** If key files are missing: `ask_followup_question` "I couldn't find standard configuration files like `package.json` or `requirements.txt`. Can you tell me what kind of project this is or its main technology? <suggest>It's a [Common Type] project</suggest> <suggest>It doesn't use a standard framework</suggest>".
*   **Leverage `ROO_COMMANDER_SYSTEM.md`:** If this file exists, attempt to `read_file` and extract key information (e.g., project name, primary technology) mentioned within it to enrich the context summary reported back to the Commander.

### 3.4. Overall Interaction Style

*   **More Conversational:** Frame questions and confirmations more collaboratively.
*   **Provide Rationale:** Briefly explain *why* certain information is being asked or checked (e.g., "Checking for `package.json` to understand the project type...").

## 4. Implementation Considerations

*   **Increased Complexity:** This significantly increases the logic within `project-onboarding`, requiring more sophisticated analysis of incoming messages and conditional branching.
*   **Prompt Engineering:** Crafting the `customInstructions` to reliably perform this analysis and choose the right follow-up questions is crucial and requires careful design.
*   **Maintaining Focus:** The mode's core role is *onboarding*. It shouldn't stray too far into requirements gathering or detailed technical setup itself, but rather guide the user and delegate appropriately based on the refined understanding.
*   **Error Handling:** More complex logic means more potential failure points that need robust handling.
*   **User Experience Trade-off:** While aiming for smoother flow, too many nuanced questions could also become tedious. Finding the right balance is key.

## 5. Conclusion

These improvements aim to make `project-onboarding` a more intelligent and user-centric starting point. By analyzing context, proposing inferred details, offering choices, and asking more targeted questions, it can move away from rigid assumptions and create a more collaborative setup experience before handing off control back to Roo Commander or other specialists. Implementation should be iterative, focusing on the highest-impact changes first (like leveraging initial context) and carefully testing the user experience.