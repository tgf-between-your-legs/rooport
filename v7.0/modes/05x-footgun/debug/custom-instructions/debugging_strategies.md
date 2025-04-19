# Common Debugging Strategies & Checklists

This document outlines common strategies that can be used to formulate explicit diagnostic instructions for `footgun-debug`.

## General Approach

1.  **Understand the Problem:**
    *   What is the exact error message?
    *   When did it start happening?
    *   Can it be reproduced reliably? What are the steps?
    *   What was the expected behavior?
    *   What has changed recently? (Code deployments, config changes, infrastructure updates)
2.  **Gather Information (Based on Explicit Instructions):**
    *   Read relevant log files (`.logs/`).
    *   Read specific code sections (`read_file`).
    *   Search for error messages or relevant code patterns (`search_files`).
    *   Check system status or configuration (`execute_command` for specific, safe commands like `systemctl status`, `cat config.json`).
3.  **Formulate Hypothesis:** Based *only* on gathered information.
4.  **Test Hypothesis (Smallest Possible Step):**
    *   Instruct `footgun-debug` to perform a *specific* diagnostic action to confirm or deny the hypothesis (e.g., "Read line X of file Y", "Search logs for pattern Z", "Execute command A and report output").
5.  **Analyze Results & Refine:** Update hypothesis based on the outcome. Repeat steps 2-4.
6.  **Isolate the Cause:** Narrow down the problem to a specific component, line of code, or configuration setting.
7.  **Propose Fix (If Instructed):** Suggest a targeted code change (`apply_diff`) or configuration update.

## Specific Strategy Examples (for Orchestrator Reference)

*   **Log Analysis:**
    *   Instruct: "Read the last 100 lines of `.logs/app.log`."
    *   Instruct: "Search all files in `.logs/` for the exact error message '[Error Message]'."
    *   Instruct: "Search `*.log` files in `.logs/` for entries containing '[TransactionID]' around [Timestamp]."
*   **Code Inspection:**
    *   Instruct: "Read lines 50-75 of `src/feature/component.js`."
    *   Instruct: "Search `src/**/*.py` for the function definition `calculate_total`."
*   **Configuration Check:**
    *   Instruct: "Read `config/production.json`."
    *   Instruct: "Execute `cat /etc/nginx/sites-enabled/default` and report output." (Use with caution, explain purpose).
*   **Connectivity Test:**
    *   Instruct: "Execute `ping -c 3 api.example.com` and report output." (Explain purpose: check network connectivity).

*(Adapt and expand these strategies based on the project's technology and common issues. Remember to provide explicit instructions to `footgun-debug`.)*