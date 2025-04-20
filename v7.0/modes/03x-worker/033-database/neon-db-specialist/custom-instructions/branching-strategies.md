# Neon: Branching Strategies

Leveraging Neon's copy-on-write branching for development, testing, and migrations.

## Core Concept: Copy-on-Write Branching

*   **Instantaneous & Cheap:** Neon allows you to create branches of your PostgreSQL database almost instantly. Branches are initially just pointers to the parent's state at a specific Log Sequence Number (LSN).
*   **Copy-on-Write:** Storage is shared between branches. When a change is made on a branch, only the modified data pages are copied and stored specifically for that branch. This makes branching very storage-efficient.
*   **Isolation:** Each branch gets its own independent compute endpoint (unless configured otherwise), ensuring operations on one branch do not affect others.
*   **Data:** Branches contain a full, independent copy of the data *as it existed* at the point of branching (or specified LSN). Subsequent changes are isolated.

## Common Use Cases & Strategies

1.  **Development Branches:**
    *   **Workflow:** Create a new branch for each feature or bug fix (`dev/feature-xyz`, `dev/bugfix-123`) directly from the main development or production branch.
    *   **Benefits:** Provides an isolated environment for development without interfering with others or the main branch. Allows testing schema changes and code against a realistic data snapshot. Easy to discard if the feature is abandoned.
    *   **Management:** Create via Neon Console UI, `neonctl` CLI, or Neon API. Delete when the feature branch is merged/closed.
    ```bash
    # Example using neonctl CLI
    neonctl branches create --project-id <project_id> --name dev/new-feature --parent <parent_branch_id_or_name>
    # Get connection string for the new branch's endpoint
    neonctl endpoints list --project-id <project_id> --branch dev/new-feature
    ```

2.  **Schema Migrations:**
    *   **Workflow:**
        1.  Create a new branch from your production (or staging) branch (`migration/add-new-table`).
        2.  Connect to this new branch.
        3.  Apply schema migration scripts (using `psql` or a framework migration tool like Alembic, Django migrations, Laravel migrations).
        4.  Test the migration and verify the schema changes on the branch.
        5.  **(Option 1 - Promote Branch):** If satisfied, potentially promote this branch to become the new primary/production branch (requires careful planning and potential downtime coordination). This is less common for simple migrations.
        6.  **(Option 2 - Apply to Production):** Once tested on the branch, schedule and apply the *same* migration scripts directly to the production branch during a maintenance window. The branch served as a safe testing ground.
    *   **Benefits:** Safely test potentially complex or risky schema changes against production-like data without impacting the live database. Allows verifying `up` and `down` migration paths.

3.  **Testing Environments:**
    *   **CI/CD:** Automate the creation of temporary branches for running integration tests or end-to-end tests in CI pipelines. Each test run gets a fresh, isolated database snapshot. Delete branches after tests complete. Use the Neon API or `neonctl`.
    *   **QA/Staging:** Maintain longer-lived branches for QA or staging environments, potentially refreshing them periodically from the production branch.

4.  **Point-in-Time Recovery / Exploration:**
    *   Create a branch from a specific LSN or timestamp in the past (using Neon's point-in-time recovery features) to investigate past data states or recover specific data without restoring the entire primary database.

## Managing Branches

*   **Neon Console:** Provides a visual interface for creating, viewing, and deleting branches.
*   **`neonctl` CLI:** Command-line tool for managing branches and other Neon resources.
    *   `neonctl projects list`
    *   `neonctl branches list --project-id ...`
    *   `neonctl branches create --project-id ... --name ... --parent ...`
    *   `neonctl branches delete --project-id ... <branch_id_or_name>`
    *   `neonctl endpoints list --project-id ... --branch ...` (Get connection string)
*   **Neon API:** Programmatically manage branches via REST API calls (useful for automation/CI/CD).

## Considerations

*   **Branch Limits:** Neon projects have limits on the number of concurrent branches (check Neon pricing/docs). Delete unused development/testing branches.
*   **Compute Endpoints:** Each active branch typically has its own compute endpoint, which incurs costs when active. Neon's autoscaling helps manage this, suspending inactive endpoints.
*   **Data Synchronization:** Branches are independent after creation. There's no built-in "merge" functionality like Git for data. Changes made on one branch need to be reapplied to others (e.g., re-running migration scripts).
*   **Primary Branch:** The main branch of your project cannot typically be deleted.

Neon's branching is a powerful feature for improving development workflows, enabling safe testing, and simplifying schema migrations compared to traditional database setups.

*(Refer to the official Neon Branching documentation: https://neon.tech/docs/introduction/branching)*