# MongoDB: Query & Projection Operators Reference

Quick reference for common MongoDB query and projection operators used with `find()` and aggregation pipelines (`$match`, `$project`).

## Comparison Query Operators

*   **`$eq`**: Matches values that are equal to a specified value.
    *   `db.collection.find({ status: { $eq: "A" } })` (Often implicit: `db.collection.find({ status: "A" })`)
*   **`$gt`**: Matches values greater than a specified value.
    *   `db.collection.find({ quantity: { $gt: 20 } })`
*   **`$gte`**: Matches values greater than or equal to a specified value.
    *   `db.collection.find({ quantity: { $gte: 20 } })`
*   **`$lt`**: Matches values less than a specified value.
    *   `db.collection.find({ quantity: { $lt: 20 } })`
*   **`$lte`**: Matches values less than or equal to a specified value.
    *   `db.collection.find({ quantity: { $lte: 20 } })`
*   **`$ne`**: Matches values not equal to a specified value.
    *   `db.collection.find({ status: { $ne: "Closed" } })`
*   **`$in`**: Matches any of the values specified in an array.
    *   `db.collection.find({ status: { $in: ["Open", "In Progress"] } })`
*   **`$nin`**: Matches none of the values specified in an array.
    *   `db.collection.find({ status: { $nin: ["Closed", "Cancelled"] } })`

## Logical Query Operators

*   **`$and`**: Joins query clauses with a logical AND. Returns documents matching *all* conditions. (Often implicit when specifying multiple fields in a query object).
    *   `db.collection.find({ $and: [ { status: "A" }, { qty: { $lt: 30 } } ] })`
    *   Implicit: `db.collection.find({ status: "A", qty: { $lt: 30 } })`
*   **`$or`**: Joins query clauses with a logical OR. Returns documents matching *at least one* condition. Requires an index for efficient performance on large collections.
    *   `db.collection.find({ $or: [ { status: "A" }, { qty: { $lt: 30 } } ] })`
*   **`$nor`**: Joins query clauses with a logical NOR. Returns documents matching *none* of the conditions.
    *   `db.collection.find({ $nor: [ { price: 1.99 }, { sale: true } ] })`
*   **`$not`**: Inverts the effect of a query expression.
    *   `db.collection.find({ price: { $not: { $gt: 1.99 } } })` (Matches price <= 1.99)

## Element Query Operators

*   **`$exists`**: Matches documents that have (or do not have) the specified field.
    *   `db.collection.find({ notes: { $exists: true } })` (Has 'notes' field)
    *   `db.collection.find({ notes: { $exists: false } })` (Does not have 'notes' field)
*   **`$type`**: Selects documents where a field is of the specified BSON type (string, number, boolean, array, object, ObjectId, etc.).
    *   `db.collection.find({ zipCode: { $type: "string" } })`
    *   `db.collection.find({ scores: { $type: "array" } })`

## Evaluation Query Operators

*   **`$regex`**: Selects documents where values match a specified regular expression. Use PCRE syntax.
    *   `db.collection.find({ name: { $regex: /^A/i } })` (Name starts with 'A', case-insensitive)
    *   `db.collection.find({ name: /bc/ })` (Simpler syntax)
*   **`$text`**: Performs text search on the content of fields indexed with a text index.
    *   `db.collection.find({ $text: { $search: "bake coffee shop" } })` (Requires text index)
*   **`$where`**: Matches documents using a JavaScript expression. **Use with caution**, slower than native operators, cannot use indexes effectively.
    *   `db.collection.find({ $where: "this.credits == this.debits" })`

## Array Query Operators

*   **`$all`**: Matches arrays containing *all* specified elements.
    *   `db.collection.find({ tags: { $all: ["ssl", "security"] } })`
*   **`$elemMatch`**: Matches documents containing an array field with *at least one element* matching *all* specified query criteria. Used for querying elements within an array of documents.
    *   `db.collection.find({ scores: { $elemMatch: { studentId: 123, score: { $gte: 80 } } } })`
*   **`$size`**: Selects documents where the array field is a specified size.
    *   `db.collection.find({ tags: { $size: 3 } })`

## Projection Operators (`find()` second argument or `$project` stage)

Used to specify which fields to include or exclude in the returned documents.

*   **Inclusion:** `1` or `true`
    *   `db.collection.find({ status: "A" }, { item: 1, status: 1 })` (Returns only `item`, `status`, and `_id`)
*   **Exclusion:** `0` or `false`
    *   `db.collection.find({ status: "A" }, { notes: 0, history: 0 })` (Returns all fields *except* `notes`, `history`)
*   **`_id` Field:** Included by default unless explicitly excluded (`_id: 0`). Cannot mix inclusion and exclusion modes in one projection, *except* for excluding `_id`.
*   **Array Operators:**
    *   `$elemMatch`: Project only the *first* element in an array that matches the criteria.
        *   `db.collection.find({ }, { students: { $elemMatch: { school: 102 } } })`
    *   `$slice`: Limit the number of elements projected from an array (first N, last N, skip N + limit M).
        *   `db.collection.find({ }, { comments: { $slice: 5 } })` (First 5 comments)
        *   `db.collection.find({ }, { comments: { $slice: -5 } })` (Last 5 comments)
        *   `db.collection.find({ }, { comments: { $slice: [10, 5] } })` (Skip 10, return next 5)

This is not exhaustive. Refer to the official MongoDB documentation for the full list and detailed behavior.

*(Refer to: https://www.mongodb.com/docs/manual/reference/operator/query/ and https://www.mongodb.com/docs/manual/reference/operator/projection/)*