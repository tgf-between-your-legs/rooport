# Proposed Improvement: Context-Aware Project Onboarding

**Date:** 2025-04-08
**Related Mode:** `roo-modes-dev/project-onboarding.json`

## 1. Problem Statement

Currently, the `project-onboarding` mode, when activated by Roo Commander, immediately asks the user to choose between "Start a new project" and "Work on an existing project". This happens regardless of the content of the initial user request passed down from the Commander.

While reliable, this can feel redundant if the user's initial request clearly indicated the intent (e.g., "Create a new website for X"). It forces an extra interaction step that might be unnecessary.

## 2. Goal

To enhance the `project-onboarding` mode to be more considerate of the user's initial request context. The aim is to allow the mode to potentially *skip* the "new vs. existing" question if the intent for a new project is sufficiently clear from the message received from Roo Commander, leading to a smoother onboarding experience.

## 3. Proposed Solution: Intent Analysis within Onboarding

Modify the `customInstructions` of `project-onboarding.json` to include an initial analysis step *before* asking the standard clarification question.

**Proposed Workflow Change:**

1.  **Receive Task & Context:** The mode receives the task delegation from Roo Commander, including the original user request message (or a summary of it).
2.  **Analyze Incoming Message:**
    *   Examine the message content for keywords strongly indicating a *new* project (e.g., "create", "new", "build", "start", "initialize", "website for", "app for").
    *   Assess confidence: Is the intent clearly "new project"?
3.  **Conditional Clarification:**
    *   **If High Confidence (New Project):** *Skip* the "new vs. existing" question. Proceed directly to asking for the project name (current Step 3a in its workflow).
    *   **If Low/Medium Confidence or Ambiguous:** *Fallback* to the current behavior: Use `ask_followup_question` to ask "Welcome! Are we starting a brand new project or working on an existing one?".
4.  **Proceed:** Continue with the rest of the onboarding workflow based on the determined path (either directly asking for name or after the user answers the clarification question).

## 4. Implementation Details (Conceptual Changes to `customInstructions`)

The beginning of the `project-onboarding.json` workflow would change conceptually like this:

```diff
 **Workflow:**

 1.  **Receive Task:** The Roo Commander will delegate the initial user request to you (including the original message context).
+2.  **Analyze Initial Intent:**
+    *   Review the message context received from Commander.
+    *   Check for strong keywords indicating a new project (e.g., "create", "new", "build", "start").
+    *   **If** intent for a *new project* is clear:
+        *   Proceed directly to Step 4a (Ask for project name).
+    *   **Else (intent is unclear or suggests existing project):**
+        *   Proceed to Step 3 (Clarify Intent - Ask 'new vs. existing').
-2.  **Clarify Intent:** Immediately use `ask_followup_question`:\\n    *   **Question:** \\\"Welcome! Are we starting a brand new project or working on an existing one?\\\"\\n    *   **Suggestions:** \\\"🚀 Start a new project.\\\", \\\"📂 Work on an existing project.\\\"
+3.  **Clarify Intent (Fallback):** Use `ask_followup_question`:\\n    *   **Question:** \\\"Welcome! Are we starting a brand new project or working on an existing one?\\\"\\n    *   **Suggestions:** \\\"🚀 Start a new project.\\\", \\\"📂 Work on an existing project.\\\"
-3.  **Branch based on user response:**
+4.  **Branch based on user response (or direct path from Step 2):**
     *   **If 'New Project':**
-        a.  Use `ask_followup_question`: \\\"Great! What should we name this new project? ...
+        a.  *(Now potentially reached directly from Step 2)* Use `ask_followup_question`: \\\"Great! What should we name this new project? ...
     *   **If 'Existing Project':**
         ... (rest of workflow follows) ...
```
*(Note: Step numbers would need re-adjusting in the actual implementation)*

## 5. Benefits

*   **Improved User Experience:** Reduces unnecessary questions when the user's intent is already clear.
*   **Faster Onboarding:** Gets to the core task (naming the project, gathering requirements) more quickly in obvious "new project" scenarios.
*   **More "Intelligent" Feel:** Makes the onboarding process seem more responsive to the initial request.

## 6. Potential Downsides & Considerations

*   **Risk of Misinterpretation:** The analysis logic might incorrectly infer a "new project" when the user meant something else (e.g., "create a *component* for my existing website"). This could lead to confusion if it skips the clarification question inappropriately.
*   **Keyword Tuning:** Defining the "strong indicators" and confidence threshold requires careful tuning. What keywords are reliable? How many are needed?
*   **Complexity:** Adds a layer of analysis logic to what is currently a very simple, deterministic mode.
*   **Edge Cases:** How to handle requests like "Work on my new project 'xyz'"? This implies both "new" and potentially "existing" if the user already created a folder. The fallback question might still be safer in ambiguous cases.

## 7. Recommendation

Consider implementing this change cautiously.
*   Start with a conservative set of keywords for inferring "new project" intent.
*   Ensure the fallback to the explicit "new vs. existing" question remains robust for any ambiguity.
*   Thoroughly test scenarios where the intent might be mixed or unclear to ensure the fallback works correctly.
*   Perhaps initially log when the skip occurs, allowing for monitoring and refinement of the analysis logic.

This change aims to balance efficiency with the reliability of explicit user confirmation.