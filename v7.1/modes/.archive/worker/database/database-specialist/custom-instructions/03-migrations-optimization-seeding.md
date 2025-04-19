# Custom Instruction: Migrations, Optimization & Seeding

## 1. Database Migrations

*   **Purpose:** Manage incremental and reversible changes to the database schema.
*   **Tooling:** Use project-specified migration tools (e.g., **Flyway, Alembic, Prisma Migrate, built-in ORM migration tools**).
*   **Generation:** Generate migration scripts using tool commands (e.g., `npx prisma migrate dev`, `alembic revision --autogenerate`).
*   **Manual Creation:** Write SQL migration scripts if required, ensuring they are idempotent or correctly sequenced.
*   **Execution:** Apply migrations using tool commands (e.g., `prisma migrate deploy`, `alembic upgrade head`).
*   **Tool Usage:** Use `execute_command` for CLI tools or `write_to_file`/`apply_diff` for manual SQL scripts.
*   **Logging:** Log migration script details (filenames, paths, purpose) and execution status in the task log (`.tasks/[TaskID].md`).
*   **Best Practices:** Follow best practices for safe schema migrations, including testing migrations in development/staging environments and considering zero-downtime strategies for production.

## 2. Query Optimization

*   **Goal:** Improve the performance of slow database queries.
*   **Analysis:**
    *   Use database-specific tools to analyze query execution plans (e.g., `EXPLAIN`, `EXPLAIN ANALYZE` in PostgreSQL/MySQL).
    *   Identify bottlenecks such as full table scans, inefficient joins, or missing indexes.
*   **Techniques:**
    *   **Indexing:** Add, modify, or remove indexes based on analysis. Implement via schema changes/migrations.
    *   **Query Rewriting:** Refactor SQL queries or ORM query builder calls for better efficiency.
    *   **Schema Changes:** Sometimes, optimizing queries requires schema adjustments (e.g., denormalization for specific read patterns, changing data types). Implement via schema changes/migrations.
*   **Logging:** Document the analysis performed, the identified bottleneck, the optimization technique applied, and the resulting performance improvement (if measurable) in the task log (`.tasks/[TaskID].md`).

## 3. Data Seeding

*   **Purpose:** Populate the database with initial data (for development/testing) or default data (for production).
*   **Methods:**
    *   **Scripts:** Write custom scripts (e.g., SQL `INSERT` statements, scripts using an ORM) to insert data.
    *   **Tools:** Utilize ORM-specific seeding tools or libraries if available.
*   **Tool Usage:** Use `write_to_file`/`apply_diff` to create/modify seeding scripts, or `execute_command` to run them.
*   **Logging:** Log the seeding approach, script paths, and execution status in the task log (`.tasks/[TaskID].md`).