**Plan for KB Documents (`.ruru/modes/roo-commander/kb/initial_actions/`):**

You're absolutely right, the next step is to create a KB document for *each* of those 16 options. Each document will detail:

*   **Objective:** Restate the goal of the chosen option.
*   **Initial Clarification (if needed):** Specify any immediate follow-up questions Commander should ask the user (e.g., "What is the Git repository URL?", "Which files contain the existing plans?", "What is the specific command?").
*   **Core Procedure:** Outline the step-by-step actions Commander needs to take, including:
    *   Which mode(s) to delegate to (`new_task`).
    *   What specific information/context to provide in the delegation message.
    *   Whether to await completion signals.
*   **Expected Outcome:** What state should the system be in after this initial action is complete?
*   **Next Step Recommendation:** What is the logical next phase (e.g., "Proceed to detailed planning", "Hand off to Project Manager", "Await specialist completion")?

**Example KB file outline (`03_clone_onboard.md`):**

```markdown
# KB: Initial Action - Clone Git Repository & Onboard

**Objective:** Clone a remote Git repository into the current workspace and initiate the standard onboarding process for it.

**Procedure:**

1.  **Get Repo URL (Coordinator):**
    *   Use `ask_followup_question`: "Please provide the HTTPS or SSH URL of the Git repository you want to clone." Await response: `[Repo URL]`.
2.  **Delegate Clone Task (Coordinator -> dev-git):**
    *   Use `new_task`: `<mode>dev-git</mode><message>Clone the repository from '[Repo URL]' into the current directory '.' using 'git clone [Repo URL] .'. Report success or failure. Coordinator Task: [Your Task ID].</message>`
    *   Await `attempt_completion` from `dev-git`. Handle failure (log, report to user, stop).
3.  **Delegate Onboarding (Coordinator -> manager-onboarding):**
    *   If clone successful: Use `new_task`: `<mode>manager-onboarding</mode><message>🎯 Project Onboarding: Intent is 'existing' (cloned repo). Analyze project context in current directory '{Current Working Directory}'. Produce Stack Profile and Requirements Doc outline. Initialize task log. Coordinator Task: [Your Task ID].</message>`
    *   Await `attempt_completion` from `manager-onboarding`. Handle failure (log, report to user).
4.  **Transition:** Report cloning and onboarding initiation success to user. The next steps will be guided by `manager-onboarding`'s process or further user goals.