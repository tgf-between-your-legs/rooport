+++
id = "PRIME-TXT-RULE-CONFIDENCE-CONFIRM-V1"
title = "Prime Documenter: Rule - Confidence-Based Write Confirmation"
context_type = "rules"
scope = "Confidence assessment and confirmation logic before file modification"
target_audience = ["prime-txt"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-21"
tags = ["rules", "safety", "confirmation", "confidence", "risk", "write", "edit", "prime-txt"]
related_context = [".modes/prime-txt/prime-txt.mode.md"]
+++

# Rule: Confidence-Based Write Confirmation

**Applies To:** All tasks involving file modification (`write_to_file`, `apply_diff`) on paths provided by Prime Coordinator.

**Procedure:**

1.  **Prepare Change:** Based on instructions, read the target file (`read_file`) and prepare the exact content or diff for modification. Ensure valid Markdown syntax.
2.  **Self-Assess Confidence & Risk:** Critically evaluate your proposed change:
    *   **Confidence:** Are you highly confident (>95%) that the change *exactly* matches the instruction and is free from errors or unintended consequences?
    *   **Risk - Ambiguity:** Were the instructions perfectly clear, or is there potential for misinterpretation?
    *   **Risk - Impact:** Does the change involve deleting significant sections of text, altering core structural headings, or modifying complex formatting in a way that might break rendering or lose information?
    *   **Risk - Explicit Request:** Did the Coordinator specifically ask you to confirm this change?
3.  **Determine Confirmation Need:**
    *   **IF** you have **any significant doubt** about your confidence (not >95% sure), OR if instructions were ambiguous, OR if the potential impact seems high (large deletion/structural change), OR if confirmation was explicitly requested...
    *   **THEN:** Proceed to Step 4 (Generate Confirmation Prompt).
    *   **ELSE (High Confidence / Low Risk):** Proceed directly to Step 5 (Propose Edit via Tool).
4.  **Generate Confirmation Prompt (If Needed):**
    *   You **MUST** use `<ask_followup_question>` to present the proposed change and the target file path.
    *   **Crucially, include a brief reason why you are seeking confirmation** (e.g., "Large change proposed," "Instructions slightly ambiguous," "Confirming significant deletion").
    *   Include clear "Yes, apply" and "No, cancel" suggestions.
        ```xml
        <ask_followup_question>
        <question>
        Proposed change to file: `[TARGET_FILE_PATH]`
        Reason for Confirmation: [State reason, e.g., Large deletion proposed]

        ```diff
        [OR ```markdown]
        [PROPOSED_DIFF_OR_CONTENT_SNIPPET]
        ```

        Apply this change?
        </question>
        <follow_up>
        <suggest>Yes, apply the change to `[TARGET_FILE_PATH]`</suggest>
        <suggest>No, cancel the change</suggest>
        </follow_up>
        </ask_followup_question>
        ```
    *   **Await User Response:** Do not proceed until the user responds.
    *   **If Approved:** Proceed to Step 5.
    *   **If Cancelled:** Abort the operation and report the cancellation to Prime Coordinator via `attempt_completion`.
5.  **Propose Edit via Tool:**
    *   Propose the change using the appropriate tool (`apply_diff` or `write_to_file`).
    *   **Note:** The standard Roo Code approval/auto-approval flow will still apply to the tool's proposal itself.
6.  **Report Outcome:** Report the final outcome (success after tool proposal, failure during tool proposal, or prior cancellation by user) back to the Prime Coordinator using `attempt_completion`.

**Rationale:** This balances user efficiency with safety by relying on AI self-assessment for potentially risky or uncertain changes. Low-risk, high-confidence changes proceed directly to the standard tool approval flow, reducing interruptions.