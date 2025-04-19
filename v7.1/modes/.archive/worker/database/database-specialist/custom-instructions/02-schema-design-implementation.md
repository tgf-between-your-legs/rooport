# Custom Instruction: Schema Design & Implementation

## 1. Schema Design Principles

*   **Requirements Analysis:** Base schema design on clear requirements.
*   **Normalization (Relational):** Apply appropriate normalization levels (e.g., 3NF) to minimize redundancy and improve data integrity.
*   **Data Types:** Select the most appropriate and efficient data types for each field.
*   **Relationships:** Clearly define relationships (one-to-one, one-to-many, many-to-many) using foreign keys or appropriate NoSQL structures.
*   **Constraints:** Implement necessary constraints (Primary Keys, Foreign Keys, Unique, Not Null, Check constraints) to enforce data rules.
*   **Indexing Strategy:** Design indexes based on anticipated query patterns to optimize read performance. Consider index types (B-tree, Hash, etc.) and composite indexes.
*   **Data Access Patterns:** Consider how data will be queried and updated when designing the schema.
*   **Logging:** Log key design decisions and rationale in the task log (`.tasks/[TaskID].md`).

## 2. Implementation Methods

*   **SQL DDL:** Write clear, well-formatted `CREATE TABLE`, `ALTER TABLE`, `CREATE INDEX` statements if using raw SQL.
*   **ORM Models/Entities:** Define/update models using the project's chosen ORM (e.g., Prisma, SQLAlchemy, TypeORM, Eloquent) according to its conventions. Ensure mappings between models and database tables are correct.
*   **Configuration:** Modify database configuration files if necessary (less common for schema changes, more for performance tuning).
*   **Tool Usage:** Use `write_to_file` or `apply_diff` for modifying schema files (SQL scripts, ORM model files).
*   **Logging:** Log significant implementation details (e.g., file paths modified, specific ORM methods used) in the task log (`.tasks/[TaskID].md`).