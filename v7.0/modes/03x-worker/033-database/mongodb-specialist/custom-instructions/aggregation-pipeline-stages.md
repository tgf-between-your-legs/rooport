# MongoDB: Common Aggregation Pipeline Stages

Reference for frequently used stages in the MongoDB Aggregation Framework.

## Core Concept

The aggregation pipeline is a framework for data aggregation modeled on the concept of data processing pipelines. Documents enter a multi-stage pipeline that transforms the documents into aggregated results.

*   **Pipeline:** An array of stages (`[...]`).
*   **Stage:** Each stage performs an operation on the input documents (e.g., filtering, grouping, projecting). Documents flow sequentially through the stages.
*   **Operators:** Stages use operators (prefixed with `$`) to define their actions.

**Syntax:** `db.collection.aggregate([ { <stage1> }, { <stage2> }, ... ])`

## Common Stages

1.  **`$match`:**
    *   **Purpose:** Filters documents, passing only those that match the specified condition(s) to the next stage.
    *   **Syntax:** Uses standard MongoDB query operators (`$eq`, `$gt`, `$in`, `$and`, etc.).
    *   **Best Practice:** Place `$match` as early as possible in the pipeline to reduce the number of documents processed by subsequent stages. Can leverage indexes if placed first.
    *   **Example:** ` { $match: { status: "A", quantity: { $gte: 10 } } } `

2.  **`$project`:**
    *   **Purpose:** Reshapes documents in the stream. Used to include/exclude fields, rename fields, or compute new fields based on existing ones.
    *   **Syntax:** Specifies output fields. `1` includes, `0` excludes (`_id` is included by default unless excluded). Can use expressions and operators to compute new fields.
    *   **Example:**
        ```javascript
        {
          $project: {
            _id: 0, // Exclude default _id
            itemName: "$item", // Rename 'item' to 'itemName'
            totalValue: { $multiply: ["$price", "$quantity"] }, // Compute new field
            status: 1 // Include 'status' field
          }
        }
        ```

3.  **`$group`:**
    *   **Purpose:** Groups input documents by a specified identifier expression (`_id`) and applies accumulator expressions to each group.
    *   **Syntax:** Requires an `_id` field specifying the grouping key (can be a field reference `$fieldname`, a constant, or a computed expression). Uses accumulator operators for calculations within each group.
    *   **Accumulator Operators:** `$sum`, `$avg`, `$min`, `$max`, `$push` (creates array), `$addToSet` (creates array of unique values), `$first`, `$last`.
    *   **Example:** Group by status, calculate total quantity and average price for each status.
        ```javascript
        {
          $group: {
            _id: "$status", // Group by the 'status' field
            totalQuantity: { $sum: "$quantity" },
            avgPrice: { $avg: "$price" },
            itemsInGroup: { $push: "$item" } // Collect item names into an array
          }
        }
        ```

4.  **`$sort`:**
    *   **Purpose:** Sorts the documents in the pipeline.
    *   **Syntax:** Specifies fields to sort by and direction (`1` for ascending, `-1` for descending).
    *   **Best Practice:** Place `$sort` before `$limit` if possible. If sorting large datasets, ensure an index supports the sort order, especially if `$sort` occurs early in the pipeline. Be mindful of memory limits for sorting.
    *   **Example:** ` { $sort: { totalQuantity: -1, _id: 1 } } `

5.  **`$limit`:**
    *   **Purpose:** Restricts the number of documents passed to the next stage.
    *   **Syntax:** Specifies the maximum number of documents.
    *   **Example:** ` { $limit: 10 } `

6.  **`$skip`:**
    *   **Purpose:** Skips a specified number of documents. Often used with `$limit` for pagination (but can be inefficient on large datasets compared to range-based pagination).
    *   **Syntax:** Specifies the number of documents to skip.
    *   **Example:** ` { $skip: 20 } `

7.  **`$unwind`:**
    *   **Purpose:** Deconstructs an array field, outputting one document for *each* element in the array.
    *   **Syntax:** Specifies the path to the array field (prefixed with `$`).
    *   **Options:** `preserveNullAndEmptyArrays: true` (outputs the document even if the array is missing, null, or empty).
    *   **Example:** ` { $unwind: "$tags" } ` (If a doc has `tags: ["A", "B"]`, it outputs two docs, one with `tags: "A"` and one with `tags: "B"`)

8.  **`$lookup`:**
    *   **Purpose:** Performs a left outer join to another collection in the same database. Adds a new array field containing matching documents from the "foreign" collection.
    *   **Syntax:** Specifies the foreign collection, local field, foreign field, and output array name.
    *   **Best Practice:** `$lookup` can be resource-intensive. Ensure the foreign field (`foreignField`) is indexed on the joined collection. Consider schema denormalization (embedding) if joins are very frequent.
    *   **Example:** Join `orders` with `inventory` based on `item`.
        ```javascript
        {
          $lookup: {
            from: "inventory", // The collection to join
            localField: "item", // Field from the input documents (orders)
            foreignField: "sku", // Field from the documents of the "from" collection (inventory)
            as: "inventory_docs" // Name of the new array field to add
          }
        }
        ```

9.  **`$addFields` / `$set`:**
    *   **Purpose:** Adds new fields or overwrites existing fields. `$set` is an alias for `$addFields`.
    *   **Syntax:** Specifies new fields and their computed values using expressions/operators.
    *   **Example:** ` { $addFields: { totalValue: { $multiply: ["$price", "$quantity"] } } } `

10. **`$count`:**
    *   **Purpose:** Counts the number of documents remaining in the pipeline and outputs a single document with the count in a specified field.
    *   **Syntax:** Specifies the output field name.
    *   **Example:** ` { $count: "totalDocuments" } ` (Outputs `{ totalDocuments: 123 }`)

11. **`$out` / `$merge`:**
    *   **Purpose:** Writes the pipeline results to a collection.
    *   **`$out`:** *Replaces* the specified output collection entirely. Must be the *last* stage.
    *   **`$merge`:** Merges results into an existing collection (updates, inserts, or fails based on options). Can be used mid-pipeline or as the last stage. More flexible than `$out`.
    *   **Example:** ` { $out: "aggregated_results" } `
    *   **Example:** ` { $merge: { into: "monthly_summary", on: "_id", whenMatched: "replace", whenNotMatched: "insert" } } `

This covers many common stages. The aggregation framework is very powerful and includes many other stages and operators for complex data transformations.

*(Refer to the official MongoDB Aggregation Pipeline Stages documentation: https://www.mongodb.com/docs/manual/reference/operator/aggregation-pipeline/)*