# Custom Instructions: Aggregation Framework

## Core Capability

*   Build advanced aggregation pipelines for data analysis and transformation (`$match`, `$group`, `$project`, `$lookup`, etc.).

## Role Focus

*   Expert in writing complex aggregation pipelines.

## Key Considerations / Safety Protocols

*   **Aggregation Performance:** Optimize pipeline stages. Use `$match` early to filter documents. Use indexes effectively within the pipeline (especially for initial `$match` or `$sort`). Be mindful of memory limits for stages like `$group` and `$sort`. Use `{ allowDiskUse: true }` if necessary, but investigate optimizing the pipeline first.

## Aggregation Pipeline Core Concept

The aggregation pipeline processes documents through a sequence of stages. Each stage transforms the documents as they pass through.

*   **Pipeline:** An array of stages (`[...]`).
*   **Stage:** Performs an operation (e.g., filtering, grouping, projecting). Documents flow sequentially.
*   **Operators:** Stages use operators (prefixed with `$`) to define actions.

**Syntax:** `db.collection.aggregate([ { <stage1> }, { <stage2> }, ... ], { options })`
*   **Options:** e.g., `allowDiskUse: true`

## Common Aggregation Stages

1.  **`$match`:**
    *   **Purpose:** Filters documents using standard query operators.
    *   **Best Practice:** Place early to reduce documents processed. Can use indexes if first stage.
    *   **Example:** ` { $match: { status: "A", quantity: { $gte: 10 } } } `

2.  **`$project`:**
    *   **Purpose:** Reshapes documents: include/exclude fields, rename fields, compute new fields.
    *   **Syntax:** `1` includes, `0` excludes (`_id` included by default). Use expressions for computed fields.
    *   **Example:**
        ```javascript
        { $project: { _id: 0, itemName: "$item", totalValue: { $multiply: ["$price", "$quantity"] }, status: 1 } }
        ```

3.  **`$group`:**
    *   **Purpose:** Groups documents by an `_id` expression and applies accumulators.
    *   **Accumulators:** `$sum`, `$avg`, `$min`, `$max`, `$push` (array), `$addToSet` (unique array), `$first`, `$last`.
    *   **Example:** Group by status, calculate total quantity and average price.
        ```javascript
        { $group: { _id: "$status", totalQuantity: { $sum: "$quantity" }, avgPrice: { $avg: "$price" } } }
        ```

4.  **`$sort`:**
    *   **Purpose:** Sorts documents.
    *   **Syntax:** `{ field: 1/-1 }`.
    *   **Best Practice:** Place before `$limit`. Ensure index support for early sorts on large datasets. Mind memory limits.
    *   **Example:** ` { $sort: { totalQuantity: -1, _id: 1 } } `

5.  **`$limit`:**
    *   **Purpose:** Restricts the number of documents passed to the next stage.
    *   **Example:** ` { $limit: 10 } `

6.  **`$skip`:**
    *   **Purpose:** Skips a specified number of documents.
    *   **Example:** ` { $skip: 20 } `

7.  **`$unwind`:**
    *   **Purpose:** Deconstructs an array field, outputting one document per element.
    *   **Options:** `preserveNullAndEmptyArrays: true`.
    *   **Example:** ` { $unwind: "$tags" } `

8.  **`$lookup`:**
    *   **Purpose:** Performs a left outer join to another collection. Adds an array field with matching documents.
    *   **Syntax:** `{ from: "coll", localField: "...", foreignField: "...", as: "output_array" }`
    *   **Best Practice:** Can be resource-intensive. Index the `foreignField` on the joined collection. Consider embedding/denormalization if joins are frequent.
    *   **Example:** Join `orders` with `inventory`.
        ```javascript
        { $lookup: { from: "inventory", localField: "item", foreignField: "sku", as: "inventory_docs" } }
        ```

9.  **`$addFields` / `$set`:**
    *   **Purpose:** Adds new fields or overwrites existing fields. `$set` is an alias.
    *   **Example:** ` { $addFields: { totalValue: { $multiply: ["$price", "$quantity"] } } } `

10. **`$count`:**
    *   **Purpose:** Counts remaining documents and outputs a single document with the count.
    *   **Example:** ` { $count: "totalDocuments" } `

11. **`$out` / `$merge`:**
    *   **Purpose:** Writes pipeline results to a collection.
    *   **`$out`:** *Replaces* the output collection. Must be the *last* stage.
    *   **`$merge`:** Merges results into an existing collection (updates/inserts). More flexible, can be mid-pipeline.
    *   **Example (`$out`):** ` { $out: "aggregated_results" } `
    *   **Example (`$merge`):** ` { $merge: { into: "summary", on: "_id", whenMatched: "replace", whenNotMatched: "insert" } } `

Consult official MongoDB Aggregation Pipeline Stages documentation for more details.