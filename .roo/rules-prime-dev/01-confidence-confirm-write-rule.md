+++
id = "PRIME-DEV-RULE-CONFIDENCE-CONFIRM-V1"
title = "Prime Config Editor: Rule - Confidence-Based Write Confirmation"
context_type = "rules"
scope = "Confidence assessment and confirmation logic before file modification"
target_audience = ["prime-dev"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-21"
tags = ["rules", "safety", "confirmation", "confidence", "risk", "write", "edit", "prime-dev", "config", "toml", "javascript", "json"]
related_context = [".modes/prime-dev/prime-dev.mode.md", "02-format-adherence-rule.md"] # Still need format rule
+++

# Rule: Confidence-Based Write Confirmation

**Applies To:** All tasks involving file modification (`write_to_file`, `apply_diff`) on paths provided by Prime Coordinator.

**Procedure:**

1.  **Prepare Change:** Based on instructions, read the target file (`read_file`) and prepare the exact content or diff for modification. Consult Rule `02-format-adherence-rule.md` to ensure the proposed changes maintain valid syntax for the target file type.
2.  **Self-Assess Confidence & Risk:** Critically evaluate your proposed change:
    *   **Confidence:** Are you highly confident (>95%) that the change *exactly* matches the instruction, is syntactically valid, and free from errors or unintended consequences?
    *   **Risk - Ambiguity:** Were the instructions perfectly clear, or is there potential for misinterpretation?
    *   **Risk - Impact:** Does the change involve deleting significant sections, modifying core function signatures/config structures, altering fundamental TOML tables/keys, or potentially breaking syntax despite checks? (Use best judgment).
    *   **Risk - Explicit Request:** Did the Coordinator specifically ask you to confirm this change?
3.  **Determine Confirmation Need:**
    *   **IF** you have **any significant doubt** about your confidence (not >95% sure), OR if instructions were ambiguous, OR if the potential impact seems high (large deletion/structural change), OR if you suspect potential syntax issues despite checks, OR if confirmation was explicitly requested...
    *   **THEN:** Proceed to Step 4 (Generate Confirmation Prompt).
    *   **ELSE (High Confidence / Low Risk):** Proceed directly to Step 5 (Propose Edit via Tool).
4.  **Generate Confirmation Prompt (If Needed):**
    *   You **MUST** use `<ask_followup_question>` to present the proposed change and the target file path.
    *   **Crucially, include a brief reason why you are seeking confirmation** (e.g., "Low confidence due to ambiguous instruction," "Potential high impact on TOML structure," "Confirming large code deletion").
    *   Include clear "Yes, apply" and "No, cancel" suggestions. Use appropriate language identifiers in Markdown code fences.
        ```xml
        <ask_followup_question>
        <question>
        Proposed change to file: `[TARGET_FILE_PATH]`
        Reason for Confirmation: [State reason]

        ```[language|diff]
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

**Rationale:** This balances user efficiency with safety by relying on AI self-assessment for potentially risky or uncertain changes. Low-risk, high-confidence changes proceed directly to the standard tool approval flow, reducing interruptions. Maintaining syntax validity (Rule `02`) is essential before assessment.