# Mode Review: project-onboarding

**Mode File:** `roo-modes-dev/project-onboarding.json`

## Analysis Summary

This mode handles the initial user interaction for new or existing projects. It clarifies intent, gathers basic project details (name, type), optionally delegates requirements gathering, performs initial project setup (directory structure, git, basic files), and reports back to the Commander.

## Findings & Concerns

1.  **Obsolete File Reference:** The `customInstructions` still contain references to `ROO_COMMANDER_SYSTEM.md` in Step 4.B.b (reading key files) and 4.B.c (synthesizing summary). These were missed previously and need removal.
2.  **MDTM Alignment:** The mode correctly acts as an initial handler without maintaining its own MDTM task log. It delegates tasks using `new_task` and reports completion using `attempt_completion`.

## Recommendations for Change

1.  **Remove `ROO_COMMANDER_SYSTEM.md` References:**
    *   Modify Step 4.B.b to remove `ROO_COMMANDER_SYSTEM.md` from the list of key files to read.
    *   Modify Step 4.B.c to remove the reference to `[system_md_info]` when synthesizing the summary.

## Other Notes/Ideas

*   The mode now correctly performs initialization directly instead of delegating to the removed `project-initializer`.
*   The workflow for distinguishing new vs. existing projects and gathering initial info seems sound.

## Proposed Changes (JSON `customInstructions`)

*   **Search 1:** `Attempt \\`read_file\\` on key files (\\`README.md\\`, \\`package.json\\`, \\`composer.json\\`, \\`requirements.txt\\`, \\`pom.xml\\`, \\`go.mod\\`, \\`docker-compose.yml\\`, \\`.git/config\\`, \\`ROO_COMMANDER_SYSTEM.md\\`). Handle errors gracefully.\\\\n            *   If \\`ROO_COMMANDER_SYSTEM.md\\` found, try to extract key info (project name, tech) from its content. Store as \\`[system_md_info]\\`.\\\\n`
*   **Replace 1:** `Attempt \\`read_file\\` on key files (\\`README.md\\`, \\`package.json\\`, \\`composer.json\\`, \\`requirements.txt\\`, \\`pom.xml\\`, \\`go.mod\\`, \\`docker-compose.yml\\`, \\`.git/config\\`). Handle errors gracefully.\\\\n            *   (Removed reading ROO_COMMANDER_SYSTEM.md for project-specific info)\\\\n`
*   **Search 2:** `Synthesize summary based on files found and \\`[system_md_info]\\``
*   **Replace 2:** `Synthesize summary based on files found`