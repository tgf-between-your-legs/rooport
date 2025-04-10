# Roo Commander: Proactive Intent Analysis Implementation

This document details how the "Proactive Intent Analysis with Direct Paths" concept is implemented within the `customInstructions` of the `roo-modes-dev/roo-commander.json` mode definition file.

## Goal

The primary goal is to make the initial interaction with Roo Commander more efficient and adaptive. It prioritizes direct user commands while offering guidance when the user's intent is less clear.

## Implementation in `customInstructions`

The logic is primarily contained within **Phase 1: Initial Interaction & Intent Clarification** of the `customInstructions`.

### 1. Analyze Initial Request

Upon receiving the first user message, Roo Commander performs two checks:

*   **Check for Directives:** Does the message explicitly request a specific mode (e.g., "switch to git manager") or ask for options ("list modes")?
*   **Analyze Intent (if no directive):** If no direct command is found, it attempts to infer the user's goal based on keywords and phrasing, assessing its confidence in the inference.

### 2. Determine Response Path

Based on the analysis, Roo Commander follows one of these paths:

*   **Path A (Direct Mode Request):**
    *   **Trigger:** User explicitly names a mode.
    *   **Action:** Confirms and attempts `switch_mode` or delegates via `new_task`. Bypasses further analysis.
    *   **Example:** User: "Switch to git manager". Roo: "Okay, switching to Git Manager mode." `<switch_mode>...`

*   **Path B (Request for Options):**
    *   **Trigger:** User asks "what can you do?" or similar.
    *   **Action:** Uses `ask_followup_question` to present a concise list of common starting modes/workflows (Plan, Code, Fix, Explore, Manage Git, See all modes).
    *   **Example:** User: "What can you do?". Roo: "I can help coordinate tasks... <suggest>Plan a new project (Architect)</suggest> ..."

*   **Path C (High Confidence Intent):**
    *   **Trigger:** Analysis strongly suggests a specific workflow (e.g., "fix bug" -> Bug Fixer).
    *   **Action:** Proposes the relevant mode via `ask_followup_question`, offering confirmation or alternatives.
    *   **Example:** User: "I need to fix a bug...". Roo: "It sounds like you want to fix a bug... <suggest>Yes, use Bug Fixer</suggest> ..."

*   **Path D (Medium Confidence / Ambiguity):**
    *   **Trigger:** Analysis is uncertain or suggests multiple possibilities (e.g., "work on API project").
    *   **Action:** Uses `ask_followup_question` to clarify the goal, providing suggestions mapped to likely workflows.
    *   **Example:** User: "Let's work on the API project". Roo: "Okay, what would you like to do first... <suggest>Implement a new feature (Code/API Dev)</suggest> ..."

*   **Path E (Low Confidence / Generic Greeting):**
    *   **Trigger:** No clear intent detected (e.g., "Hi").
    *   **Action:** States uncertainty and asks for a clearer goal or offers common starting points (similar to Path B) via `ask_followup_question`.
    *   **Example:** User: "Hi". Roo: "Hello! I'm Roo Commander... What would you like to achieve today? ..."

*   **Path F (Setup/Existing Project):**
    *   **Trigger:** Request clearly involves project setup or onboarding.
    *   **Action:** Delegates immediately to `project-onboarding` via `new_task`.

### 3. Optional Detail Gathering

*   **Trigger:** After the initial path/goal is confirmed.
*   **Action:** Optionally uses `ask_followup_question` to ask for user details (name, project context), explaining the benefits and providing opt-out suggestions.
*   **Storage:** If provided, details are saved using `write_to_file` to `project_journal/context/user_profile.md`.

## Conclusion

The `customInstructions` in `roo-modes-dev/roo-commander.json` directly implement the proactive intent analysis flow, ensuring Roo Commander handles initial interactions efficiently by prioritizing user directives while providing helpful guidance when needed.