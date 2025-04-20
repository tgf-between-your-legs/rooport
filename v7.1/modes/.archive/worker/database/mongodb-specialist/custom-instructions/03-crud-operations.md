# Custom Instructions: CRUD Operations &amp; Querying

## Core Capability

*   Perform CRUD operations with complex queries and operators (`find`, `insertOne/Many`, `updateOne/Many`, `deleteOne/Many`).

## Role Focus

*   Expert in writing complex queries.

## CRUD Operations (Shell Equivalents &amp; Concepts)

*   **Insert:**
    *   `db.collection.insertOne({ field: "value", ... })`
    *   `db.collection.insertMany([{ field: "value1" }, { field: "value2" }])`
*   **Find:**
    *   `db.collection.find({ query })`: Find documents matching the query. Returns a cursor.
    *   `db.collection.findOne({ query })`: Find the first document matching the query.
    *   `.pretty()`: Append to `find()` in `mongosh` to format the output nicely.
    *   `.limit(N)`: Limit the number of documents returned.
    *   `.skip(N)`: Skip N documents.
    *   `.sort({ field: 1/-1 })`: Sort documents.
    *   `db.collection.countDocuments({ query })`: Accurate count based on query.
    *   `db.collection.estimatedDocumentCount()`: Faster count using metadata (no query).
*   **Update:**
    *   `db.collection.updateOne({ filter }, { $set: { field: "new_value" }, ... }, { upsert: true/false })`
    *   `db.collection.updateMany({ filter }, { $set: { field: "new_value" }, ... })`
    *   `db.collection.replaceOne({ filter }, { new_document }, { upsert: true/false })`
    *   **Update Operators:** `$set`, `$unset`, `$inc`, `$push`, `$pull`, `$rename`, etc.
*   **Delete:**
    *   `db.collection.deleteOne({ filter })`
    *   `db.collection.deleteMany({ filter })`

## Query &amp; Projection Operators Reference

### Comparison Query Operators

*   **`$eq`**: Equal to (often implicit). ` { status: "A" } `
*   **`$gt`**: Greater than. ` { quantity: { $gt: 20 } } `
*   **`$gte`**: Greater than or equal to. ` { quantity: { $gte: 20 } } `
*   **`$lt`**: Less than. ` { quantity: { $lt: 20 } } `
*   **`$lte`**: Less than or equal to. ` { quantity: { $lte: 20 } } `
*   **`$ne`**: Not equal to. ` { status: { $ne: "Closed" } } `
*   **`$in`**: Matches any value in an array. ` { status: { $in: ["Open", "In Progress"] } } `
*   **`$nin`**: Matches none of the values in an array. ` { status: { $nin: ["Closed", "Cancelled"] } } `

### Logical Query Operators

*   **`$and`**: Matches all conditions (often implicit). ` { status: "A", qty: { $lt: 30 } } `
*   **`$or`**: Matches at least one condition. ` { $or: [ { status: "A" }, { qty: { $lt: 30 } } ] } `
*   **`$nor`**: Matches none of the conditions. ` { $nor: [ { price: 1.99 }, { sale: true } ] } `
*   **`$not`**: Inverts the effect of an expression. ` { price: { $not: { $gt: 1.99 } } } `

### Element Query Operators

*   **`$exists`**: Field exists or does not exist. ` { notes: { $exists: true } } `
*   **`$type`**: Field is of a specific BSON type. ` { zipCode: { $type: "string" } } `

### Evaluation Query Operators

*   **`$regex`**: Matches a regular expression. ` { name: { $regex: /^A/i } } ` or ` { name: /bc/ } `
*   **`$text`**: Performs text search (requires text index). ` { $text: { $search: "bake coffee shop" } } `
*   **`$where`**: Uses JavaScript expression (Use cautiously, slow). ` { $where: "this.credits == this.debits" } `

### Array Query Operators

*   **`$all`**: Array contains all specified elements. ` { tags: { $all: ["ssl", "security"] } } `
*   **`$elemMatch`**: Array contains at least one element matching all criteria. ` { scores: { $elemMatch: { studentId: 123, score: { $gte: 80 } } } } `
*   **`$size`**: Array is a specific size. ` { tags: { $size: 3 } } `

### Projection Operators (`find()` second argument or `$project` stage)

Used to specify which fields to include or exclude.

*   **Inclusion:** `1` or `true`. ` { item: 1, status: 1 } ` (Returns `item`, `status`, and `_id`)
*   **Exclusion:** `0` or `false`. ` { notes: 0, history: 0 } ` (Returns all fields *except* `notes`, `history`)
*   **`_id` Field:** Included by default unless excluded (`_id: 0`). Cannot mix inclusion/exclusion except for `_id`.
*   **Array Operators:**
    *   `$elemMatch`: Project only the *first* matching array element. ` { students: { $elemMatch: { school: 102 } } } `
    *   `$slice`: Limit projected array elements (first N, last N, skip/limit). ` { comments: { $slice: 5 } } `

Refer to official MongoDB documentation for full details on operators and methods.