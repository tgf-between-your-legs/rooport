# MongoDB: Transactions & Change Streams

Implementing atomic multi-document operations and reacting to data changes in real-time.

## Transactions

*   **Concept:** MongoDB supports multi-document ACID (Atomicity, Consistency, Isolation, Durability) transactions on replica sets and sharded clusters. This allows you to perform a sequence of read and write operations across multiple documents and collections as a single, atomic unit. Either all operations succeed, or none of them do (rollback).
*   **Requirement:** Requires a replica set or sharded cluster deployment (not supported on standalone instances).
*   **Usage (Driver Syntax):** Transactions are managed through client sessions. The exact syntax varies slightly between drivers (PyMongo, Node.js driver, etc.), but the pattern is generally:
    1.  Start a client session (`client.start_session()`).
    2.  Start a transaction within the session (`session.with_transaction(...)` callback or explicit `session.start_transaction()`).
    3.  Perform your sequence of read and write operations *using the session object* passed to the database methods (e.g., `collection.insert_one(..., session=session)`).
    4.  Commit the transaction (`session.commit_transaction()`) or let the callback handle it.
    5.  The driver handles aborting the transaction (`session.abort_transaction()`) automatically on error within the callback, or you can call it manually.
    6.  End the session (`session.end_session()`).

```python
# Example using PyMongo (Python Driver)
from pymongo import MongoClient, ReadPreference, WriteConcern, ReadConcern

client = MongoClient('mongodb://localhost:27017/?replicaSet=rs0') # Connect to replica set

def update_product_and_order(session, product_id, order_id, quantity_change):
    products_coll = session.client.testdb.products # Use session.client
    orders_coll = session.client.testdb.orders

    # Get current product stock (read within transaction)
    product = products_coll.find_one({'_id': product_id}, session=session)
    if not product or product['stock'] < quantity_change:
        raise ValueError("Insufficient stock or product not found")

    # Update product stock
    result1 = products_coll.update_one(
        {'_id': product_id},
        {'$inc': {'stock': -quantity_change}},
        session=session
    )
    if result1.modified_count != 1:
        raise RuntimeError("Failed to update product stock")

    # Update order status
    result2 = orders_coll.update_one(
        {'_id': order_id},
        {'$set': {'status': 'Processed'}},
        session=session
    )
    if result2.modified_count != 1:
         raise RuntimeError("Failed to update order status")

    print(f"Transaction successful for order {order_id}")


# --- Using with_transaction (Recommended) ---
# The callback approach automatically handles commit/abort
try:
    with client.start_session() as session:
        # Define transaction options (optional)
        wc = WriteConcern("majority")
        rc = ReadConcern("snapshot") # Use snapshot isolation if needed
        # Execute the transaction
        session.with_transaction(
            lambda s: update_product_and_order(s, 'PRODUCT123', 'ORDER456', 2),
            read_concern=rc,
            write_concern=wc,
            read_preference=ReadPreference.PRIMARY
        )
    print("Transaction committed successfully.")
except Exception as e:
    print(f"Transaction aborted: {e}")

client.close()
```

*   **Considerations:**
    *   Transactions have performance overhead compared to individual operations.
    *   They have time limits and size limits.
    *   Use them only when atomicity across multiple documents/collections is strictly required. Many use cases can be handled by careful schema design (embedding) or application-level logic.

## Change Streams

*   **Concept:** A real-time stream of data changes (inserts, updates, deletes, replaces) occurring on a collection, database, or entire deployment. Applications can "watch" a stream to react to changes as they happen.
*   **Requirement:** Requires a replica set or sharded cluster.
*   **Use Cases:** Real-time notifications, data synchronization between systems, triggering actions based on specific changes, auditing.
*   **Usage (Driver Syntax):**
    1.  Open a change stream cursor using `collection.watch()`, `db.watch()`, or `client.watch()`.
    2.  Optionally provide a pipeline (`[...]`) to filter or transform the change events.
    3.  Iterate over the cursor (often in a loop or using async iteration) to process change event documents.

```python
# Example using PyMongo (Python Driver)

client = MongoClient('mongodb://localhost:27017/?replicaSet=rs0')
db = client.testdb
collection = db.inventory

# Watch for inserts and updates on the 'inventory' collection
pipeline = [
    {'$match': {'operationType': {'$in': ['insert', 'update']}}},
    {'$match': {'fullDocument.status': 'urgent'}} # Only watch urgent items
]

try:
    # resume_after = ... # Store token to resume stream after interruption
    # with collection.watch(pipeline, resume_after=resume_after) as stream:
    with collection.watch(pipeline) as stream:
        print("Watching for urgent inventory changes...")
        for change in stream:
            print("\nChange detected:")
            print(f"  Operation: {change['operationType']}")
            print(f"  Document Key (_id): {change['documentKey']['_id']}")
            # 'fullDocument' contains the document state after the change (for insert, replace, update)
            if 'fullDocument' in change:
                print(f"  Full Document: {change['fullDocument']}")
            # 'updateDescription' shows fields changed in an update
            if 'updateDescription' in change:
                print(f"  Updated Fields: {change['updateDescription']['updatedFields']}")
                print(f"  Removed Fields: {change['updateDescription']['removedFields']}")

            # Store resume token if needed
            # resume_token = stream.resume_token

except KeyboardInterrupt:
    print("\nStopping change stream watcher.")
finally:
    client.close()

```

*   **Change Event Document:** Contains details about the change, including:
    *   `_id`: Resume token.
    *   `operationType`: Type of operation (`insert`, `update`, `delete`, `replace`, `invalidate`, etc.).
    *   `ns`: Namespace (database and collection).
    *   `documentKey`: The `_id` of the document affected.
    *   `fullDocument`: (Optional, depends on configuration) The document state *after* the operation.
    *   `updateDescription`: (For `update` operations) Shows fields updated and removed.
*   **Resumability:** Change streams are resumable using the `_id` (resume token) from the last processed event. Store this token to restart the stream after interruptions.
*   **Filtering:** Use a pipeline (`[{ $match: ... }]`) in the `watch()` method to filter events server-side, reducing network traffic and client-side processing.

Transactions provide atomicity for complex operations, while Change Streams enable real-time reactivity to data modifications.

*(Refer to the official MongoDB documentation on Transactions and Change Streams.)*