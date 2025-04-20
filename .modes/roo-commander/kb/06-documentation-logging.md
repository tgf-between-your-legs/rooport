# 06: Documentation & Logging

This section outlines the procedures for maintaining project documentation and logging key decisions.

**Formal Document Maintenance:**

*   **Responsibility:** Oversee high-level project documents stored in `.planning/` and potentially `.docs/` (though `.docs/` is primarily managed by specialists like `util-writer`).
*   **Guidance (Create):** Create *new* high-level planning documents (e.g., `.planning/project_plan.md`, `.planning/strategy_notes.md`) using `write_to_file`.
*   **Guidance (Update):** For *updates* to existing formal documents (especially in `.docs/`), prefer delegating the update task to a relevant specialist (e.g., `util-writer`, `core-architect`). If direct, minor modifications to *planning* documents are necessary, consider using `apply_diff` or `insert_content` for targeted changes. **Avoid using `write_to_file` to overwrite large existing documents.**

**Decision Record Creation (ADRs):**

*   **Purpose:** Log all significant architectural, technological, or strategic decisions to maintain transparency and traceability.
*   **Guidance:** Create decision records using `write_to_file` targeting `.decisions/YYYYMMDD-brief-topic-summary.md`. Use an ADR-like format.
*   **Example Content:**
    ```markdown
    # ADR: Technology Choice for Backend API

    **Date:** 2025-04-15
    **Status:** Accepted

    ## Context
    The project requires a backend API. The Stack Profile indicates team familiarity with Python and JavaScript/Node.js. Performance and rapid development are key requirements.

    ## Decision
    We will use FastAPI (Python) for the backend API.

    ## Rationale
    - High performance benchmarks suitable for expected load.
    - Excellent developer experience and built-in data validation align with rapid development goals.
    - Strong Python expertise noted in the Stack Profile.
    - `framework-fastapi` specialist mode is available for implementation.
    - Considered Node.js (e.g., Express/NestJS), but FastAPI's automatic docs and type hinting provide advantages for this project.

    ## Consequences
    - Requires Python environment setup.
    - Team members less familiar with Python/FastAPI may need ramp-up time (mitigated by specialist availability).
    - Integration patterns with the frontend (e.g., React) need to be defined.
    ```
*   **Logging:** Log the creation of the ADR in the relevant Commander task log (`.tasks/TASK-CMD-...`) using `insert_content`.