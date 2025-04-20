# Custom Instructions: Performance Tuning with `explain()`

## Core Capability

*   Analyze and optimize query performance using explain plans (`explain()`).

## Role Focus

*   Expert in optimizing performance (using `explain()`).

## Key Considerations / Safety Protocols

*   **Performance Tuning:** Use `explain("executionStats")` extensively to analyze query plans. Aim to replace `COLLSCAN` with `IXSCAN`. Ensure `totalDocsExamined` and `totalKeysExamined` are close to `nReturned`. Optimize indexes (ESR rule, covered queries) and queries.

## `explain()` Method

*   **Purpose:** Provides detailed information about query execution, showing index usage, documents scanned, execution time, etc. **Crucial** for diagnosing performance issues.
*   **Syntax:** Append `.explain()` to `find()`, `aggregate()`, etc.
    *   `db.collection.find(...).explain("executionStats")` (Most useful mode)
    *   `db.collection.aggregate([...]).explain()`
*   **Modes:**
    *   `"queryPlanner"`: Shows chosen and rejected plans (no execution).
    *   `"executionStats"`: **Use this most often.** Executes query and provides detailed stats.
    *   `"allPlansExecution"`: Executes and provides stats for winning and rejected plans.

## Interpreting `explain("executionStats")` Output

Key fields:

*   **`queryPlanner.winningPlan.stage` / `inputStage`:**
    *   **`IXSCAN`:** Index scan used (Good!). Shows `indexName`, `indexBounds`.
    *   **`FETCH`:** Documents fetched after index scan.
    *   **`COLLSCAN`:** Collection scan (Bad!). No suitable index used. **Avoid on large collections.**
    *   **`SORT`:** In-memory sort. Consider index support if frequent/large.
    *   **`PROJECTION_COVERED`:** Query covered by index (Very Good!).
*   **`executionStats.nReturned`:** Number of documents matched.
*   **`executionStats.totalKeysExamined`:** Number of index keys scanned. (Goal: close to `nReturned`).
*   **`executionStats.totalDocsExamined`:** Number of documents fetched/examined. (Goal: close to `nReturned`). High ratio indicates inefficiency.
*   **`executionStats.executionTimeMillis`:** Execution time.
*   **`executionStats.executionStages`:** Detailed breakdown per stage.

## Common Optimization Techniques

1.  **Create Supporting Indexes:**
    *   Identify `COLLSCAN` or high `totalDocsExamined`/`totalKeysExamined` ratios.
    *   Create indexes matching query criteria (ESR: Equality, Sort, Range).
    *   Use compound indexes.
    *   Verify index usage with `explain()` after creation.
2.  **Optimize Existing Indexes:**
    *   Ensure compound index field order follows ESR rule for query patterns.
    *   Consider partial indexes for queries targeting subsets.
    *   Remove unused/redundant indexes (they slow writes).
3.  **Refine Queries:**
    *   Be specific with criteria.
    *   Use index-friendly operators (avoid unindexed `$regex`, `$where`).
    *   Use projections (`{ field: 1 }`) to return only needed fields. Aim for covered queries.
4.  **Optimize Aggregation Pipelines:**
    *   Use `$match` early (ensure it can use an index).
    *   Use `$project` early to remove unused fields.
    *   Mind memory limits for `$group`, `$sort`. Use `{ allowDiskUse: true }` cautiously.
5.  **Schema Design:**
    *   Revisit embedding vs. referencing if queries require complex `$lookup` or scan large documents unnecessarily.
6.  **Hardware & Configuration:**
    *   Ensure sufficient RAM for working set (data + indexes).
    *   Monitor server metrics (CPU, RAM, I/O). Escalate infrastructure issues.

Optimization is iterative: Analyze (`explain()`) -> Hypothesize -> Optimize (e.g., add index) -> Measure (`explain()`). Consult official MongoDB Query Optimization documentation.