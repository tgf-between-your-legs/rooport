TITLE: Basic MongoDB Backup Using mongodump
DESCRIPTION: Simple command to backup a MongoDB database running on localhost port 27017. Creates a backup in the current directory under 'dump/'.

LANGUAGE: bash
CODE:
mongodump

----------------------------------------

TITLE: Querying MongoDB Current Operations
DESCRIPTION: The $currentOp aggregation stage retrieves information about active operations and cursors to identify performance issues.

LANGUAGE: mongodb
CODE:
$currentOp

----------------------------------------

TITLE: Query Using Operators in MongoDB
DESCRIPTION: Returns documents where _id equals either 5 or ObjectId("507c35dd8fada716c89d0013") using the $in operator.

LANGUAGE: javascript
CODE:
db.bios.find(
   { _id: { $in: [ 5, ObjectId("507c35dd8fada716c89d0013") ] } }
)

----------------------------------------

TITLE: Counting Joins per Month in MongoDB
DESCRIPTION: This aggregation operation shows how many people joined each month of the year. It uses $project, $group, and $sort to transform and summarize the data.

LANGUAGE: javascript
CODE:
db.members.aggregate( [
   { $project: { month_joined: { $month: "$joined" } } } ,
   { $group: { _id: { month_joined: "$month_joined" } , number: { $sum: 1 } } },
   { $sort: { "_id.month_joined": 1 } }
] )

----------------------------------------

TITLE: Inserting Invalid Document into MongoDB Collection
DESCRIPTION: This snippet shows an attempt to insert an invalid document into the 'students' collection. The operation fails because the 'gpa' field is an integer when the validator requires a double.

LANGUAGE: javascript
CODE:
db.students.insertOne( {
   name: "Alice",
   year: Int32( 2019 ),
   major: "History",
   gpa: Int32(3),
   address: {
      city: "NYC",
      street: "33rd Street"
   }
} )

----------------------------------------

TITLE: Practical Example of $center Query in MongoDB
DESCRIPTION: Example query that finds all documents in the 'places' collection where the 'loc' field contains coordinates within a circle centered at [-74, 40.74] with radius 10.

LANGUAGE: javascript
CODE:
db.places.find(
   { loc: { $geoWithin: { $center: [ [-74, 40.74], 10 ] } } }
)

----------------------------------------

TITLE: Creating User with Roles in MongoDB
DESCRIPTION: This example demonstrates creating a user named 'accountAdmin01' with specific roles and custom data. It also shows how to specify write concern for the operation.

LANGUAGE: javascript
CODE:
use products
db.createUser( { user: "accountAdmin01",
                 pwd: passwordPrompt(),  // Or  "<cleartext password>"
                 customData: { employeeId: 12345 },
                 roles: [ { role: "clusterAdmin", db: "admin" },
                          { role: "readAnyDatabase", db: "admin" },
                          "readWrite"] },
               { w: "majority" , wtimeout: 5000 } )

----------------------------------------

TITLE: Retrieving Encrypted Documents in Java with CSFLE
DESCRIPTION: Java code for querying documents with encrypted fields using MongoDB's Client-Side Field Level Encryption. Demonstrates using both encrypted and non-encrypted clients to show the difference in data handling.

LANGUAGE: java
CODE:
## Placeholder for Java code - actual implementation details not shown in source ##

----------------------------------------

TITLE: Inserting Multiple Documents in MongoDB using JavaScript Shell
DESCRIPTION: This snippet demonstrates how to insert multiple documents into the 'inventory' collection using the MongoDB shell. It uses the insertMany() method to add an array of documents with various item details.

LANGUAGE: javascript
CODE:
db.inventory.insertMany( [
   { item: "journal", qty: 25, size: { h: 14, w: 21, uom: "cm" }, status: "A" },
   { item: "notebook", qty: 50, size: { h: 8.5, w: 11, uom: "in" }, status: "A" },
   { item: "paper", qty: 100, size: { h: 8.5, w: 11, uom: "in" }, status: "D" },
   { item: "planner", qty: 75, size: { h: 22.85, w: 30, uom: "cm" }, status: "D" },
   { item: "postcard", qty: 45, size: { h: 10, w: 15.25, uom: "cm" }, status: "A" }
]);

----------------------------------------

TITLE: Using Comments in MongoDB Aggregation
DESCRIPTION: Demonstrates how to add a comment to an aggregation operation for easier tracking and profiling.

LANGUAGE: javascript
CODE:
db.movies.aggregate( [ { $match: { year : 1995 } } ], { comment : "match_all_movies_from_1995" } ).pretty()

----------------------------------------

TITLE: Querying Encrypted Documents with CSFLE (Python)
DESCRIPTION: Implements encrypted document retrieval using Python MongoDB driver with CSFLE. Demonstrates difference between encrypted and non-encrypted query results.

LANGUAGE: python
CODE:
start-find
end-find

----------------------------------------

TITLE: Creating User with Simple Roles in MongoDB
DESCRIPTION: This example shows how to create a user named 'accountUser' with readWrite and dbAdmin roles on the products database.

LANGUAGE: javascript
CODE:
use products
db.createUser(
   {
     user: "accountUser",
     pwd: passwordPrompt(),  // Or  "<cleartext password>"
     roles: [ "readWrite", "dbAdmin" ]
   }
)

----------------------------------------

TITLE: Opening Basic Change Stream - Python
DESCRIPTION: Example of opening a basic change stream to monitor collection changes in Python using PyMongo

LANGUAGE: python
CODE:
try:
    resume_token = None
    pipeline = []
    with collection.watch(pipeline) as stream:
        for change_document in stream:
            print(change_document)
            resume_token = change_document['_id']
except pymongo.errors.PyMongoError:
    if resume_token is None:
        logging.error('Unable to open change stream')
    else:
        with collection.watch(
                pipeline, resume_after=resume_token) as stream:
            for change_document in stream:
                print(change_document)
                resume_token = change_document['_id']

----------------------------------------

TITLE: Calculating Average City Population by State in MongoDB
DESCRIPTION: Demonstrates a two-stage aggregation pipeline using $group to calculate the average population of cities for each state.

LANGUAGE: javascript
CODE:
db.zipcodes.aggregate( [
   { $group: { _id: { state: "$state", city: "$city" }, pop: { $sum: "$pop" } } },
   { $group: { _id: "$_id.state", avgCityPop: { $avg: "$pop" } } }
] )

----------------------------------------

TITLE: MongoDB createUser Command Syntax
DESCRIPTION: Syntax for the createUser command in MongoDB. It includes fields for specifying the username, password, custom data, roles, write concern, authentication restrictions, and SCRAM mechanisms.

LANGUAGE: javascript
CODE:
db.runCommand(
   {
     createUser: "<name>",
     pwd: passwordPrompt(),      // Or  "<cleartext password>"
     customData: { <any information> },
     roles: [
       { role: "<role>", db: "<database>" } | "<role>",
       ...
     ],
     writeConcern: { <write concern> },
     authenticationRestrictions: [
        { clientSource: [ "<IP|CIDR range>", ... ], serverAddress: [ "<IP|CIDR range>", ... ] }, 
        ...
     ],
     mechanisms: [ "<scram-mechanism>", ... ], 
     digestPassword: <boolean>,
     comment: <any>
   }
)

----------------------------------------

TITLE: Querying Documents with $gt Operator
DESCRIPTION: Example showing how to query the inventory collection to find documents where the quantity field is greater than 20.

LANGUAGE: javascript
CODE:
db.inventory.find( { quantity: { $gt: 20 } } )

----------------------------------------

TITLE: Basic Find Operation in MongoDB
DESCRIPTION: Selects documents in a collection and returns a cursor to the selected documents.

LANGUAGE: javascript
CODE:
db.collection.find( <query>, <projection>, <options> )

----------------------------------------

TITLE: Executing a Transaction with Python Callback API
DESCRIPTION: This example demonstrates using the Python driver's callback API to execute a transaction that inserts documents into two different collections. It includes retry logic for transient errors and unknown commit results.

LANGUAGE: python
CODE:
def callback(session):
    collection_one = session.client.mydb1.foo
    collection_two = session.client.mydb2.bar
    
    collection_one.insert_one({"abc": 1}, session=session)
    collection_two.insert_one({"xyz": 999}, session=session)

with client.start_session() as session:
    session.with_transaction(callback)

----------------------------------------

TITLE: Creating and Populating MongoDB Inventory Collection
DESCRIPTION: This snippet demonstrates how to create an inventory collection in MongoDB and insert sample documents. It connects to a test database, creates the collection, and inserts multiple documents representing various inventory items.

LANGUAGE: javascript
CODE:
db = db.getSiblingDB("test");
db.inventory.insertMany([
   { item: "journal", qty: 25, size: { h: 14, w: 21, uom: "cm" }, status: "A" },
   { item: "notebook", qty: 50, size: { h: 8.5, w: 11, uom: "in" }, status: "A" },
   { item: "paper", qty: 100, size: { h: 8.5, w: 11, uom: "in" }, status: "D" },
   { item: "planner", qty: 75, size: { h: 22.85, w: 30, uom: "cm" }, status: "D" },
   { item: "postcard", qty: 45, size: { h: 10, w: 15.25, uom: "cm" }, status: "A" }
]);

----------------------------------------

TITLE: Basic Find Operation in MongoDB
DESCRIPTION: Selects documents in a collection and returns a cursor to the selected documents.

LANGUAGE: javascript
CODE:
db.collection.find( <query>, <projection>, <options> )

----------------------------------------

TITLE: Executing Money Transfer Transaction in MongoDB
DESCRIPTION: Implements a transaction that safely transfers money between two accounts with validation checks. Uses session.withTransaction() to handle the transaction lifecycle including automatic commit and rollback.

LANGUAGE: javascript
CODE:
var session = db.getMongo().startSession( { readPreference: { mode: "primary" } } );
session.withTransaction( async() => {  

   const sessionCollection = session.getDatabase(dbName).getCollection(collectionName);

   // Check needed values
   var checkFromAccount = sessionCollection.findOne(
      {
         "customer": fromAccount,
         "balance": { $gte: transferAmount }
      }
   )
   if( checkFromAccount === null ){
      throw new Error( "Problem with sender account" )
   } 

   var checkToAccount = sessionCollection.findOne(
      { "customer": toAccount }
   )
   if( checkToAccount === null ){
      throw new Error( "Problem with receiver account" )
   } 

   // Transfer the funds
   sessionCollection.updateOne(
      { "customer": toAccount },
      { $inc: { "balance": transferAmount } }
   )
   sessionCollection.updateOne(
      { "customer": fromAccount },
      { $inc: { "balance": -1 * transferAmount } }
   )

 } )

----------------------------------------

TITLE: Using MongoDB Aggregate Method
DESCRIPTION: The db.collection.aggregate() method provides access to the aggregation pipeline. It allows for chaining multiple stages of data transformation and analysis.

LANGUAGE: mongodb
CODE:
db.collection.aggregate([
  { $match: { status: "active" } },
  { $group: { _id: "$category", total: { $sum: "$amount" } } },
  { $sort: { total: -1 } }
])

----------------------------------------

TITLE: Creating MongoDB Collection with JSON Schema Validation
DESCRIPTION: This snippet demonstrates how to create a 'students' collection with JSON Schema validation rules using the $jsonSchema operator. It defines constraints for various fields including name, year, major, gpa, and address.

LANGUAGE: javascript
CODE:
db.createCollection("students", {
   validator: {
      $jsonSchema: {
         bsonType: "object",
         title: "Student Object Validation",
         required: [ "name", "year", "major", "address" ],
         properties: {
            name: {
               bsonType: "string",
               description: "'name' must be a string and is required"
            },
            year: {
               bsonType: "int",
               minimum: 2017,
               maximum: 3017,
               description: "'year' must be an integer in [ 2017, 3017 ] and is required"
            },
            major: {
               enum: [ "Math", "English", "Computer Science", "History", null ],
               description: "'major' can only be one of the enum values and is required"
            },
            gpa: {
               bsonType: [ "double" ],
               description: "'gpa' must be a double if the field exists"
            },
            address: {
               bsonType: "object",
               required: [ "city", "street" ],
               properties: {
                  street: {
                     bsonType: "string",
                     description: "'street' must be a string and is required"
                  },
                  city: {
                     bsonType: "string",
                     description: "'city' must be a string and is required"
                  }
               }
            }
         }
      }
   }
})

----------------------------------------

TITLE: Basic $lookup Syntax for Single Equality Join
DESCRIPTION: Syntax for performing a simple equality join between two collections using $lookup.

LANGUAGE: javascript
CODE:
{
   $lookup:
     {
       from: <collection to join>,
       localField: <field from the input documents>,
       foreignField: <field from the documents of the "from" collection>,
       as: <output array field>
     }
}

----------------------------------------

TITLE: Selecting All Documents in a MongoDB Collection
DESCRIPTION: This example demonstrates how to select all documents in a MongoDB collection using an empty query predicate.

LANGUAGE: javascript
CODE:
db.collection.find({})

----------------------------------------

TITLE: Complex Grouping and Calculation in MongoDB Aggregation
DESCRIPTION: Demonstrates grouping by date, calculating multiple aggregates, and sorting results using $group, $match, and $sort stages.

LANGUAGE: javascript
CODE:
db.sales.aggregate([
  // First Stage
  {
    $match : { "date": { $gte: new ISODate("2014-01-01"), $lt: new ISODate("2015-01-01") } }
  },
  // Second Stage
  {
    $group : {
       _id : { $dateToString: { format: "%Y-%m-%d", date: "$date" } },
       totalSaleAmount: { $sum: { $multiply: [ "$price", "$quantity" ] } },
       averageQuantity: { $avg: "$quantity" },
       count: { $sum: 1 }
    }
  },
  // Third Stage
  {
    $sort : { totalSaleAmount: -1 }
  }
 ])

LANGUAGE: sql
CODE:
SELECT date,
       Sum(( price * quantity )) AS totalSaleAmount,
       Avg(quantity)             AS averageQuantity,
       Count(*)                  AS Count
FROM   sales
WHERE  date >= '01/01/2014' AND date < '01/01/2015'
GROUP  BY date
ORDER  BY totalSaleAmount DESC

----------------------------------------

TITLE: Querying and Sorting Using Index Prefixes in MongoDB
DESCRIPTION: These examples show various ways to query and sort data using prefixes of the compound index created earlier. They demonstrate how MongoDB can use the index efficiently for different query and sort combinations.

LANGUAGE: javascript
CODE:
db.data.find().sort( { a: 1 } )

LANGUAGE: javascript
CODE:
db.data.find().sort( { a: -1 } )

LANGUAGE: javascript
CODE:
db.data.find().sort( { a: 1, b: 1 } )

LANGUAGE: javascript
CODE:
db.data.find().sort( { a: -1, b: -1 } )

LANGUAGE: javascript
CODE:
db.data.find().sort( { a: 1, b: 1, c: 1 } )

LANGUAGE: javascript
CODE:
db.data.find( { a: { $gt: 4 } } ).sort( { a: 1, b: 1 } )

----------------------------------------

TITLE: Creating Index for Author Name in MongoDB
DESCRIPTION: This snippet demonstrates how to create an index on the 'author_name' field in a 'posts' collection to optimize queries that search or sort by author name.

LANGUAGE: javascript
CODE:
db.posts.createIndex( { author_name : 1 } )

----------------------------------------

TITLE: Selecting a Database in MongoDB Shell
DESCRIPTION: This snippet demonstrates how to select a database to use in the MongoDB shell (mongosh) using the 'use' command.

LANGUAGE: javascript
CODE:
use myDB

----------------------------------------

TITLE: Updating Multiple Documents in MongoDB Shell
DESCRIPTION: Uses db.collection.updateMany() to update all documents where qty is less than 50 in the inventory collection.

LANGUAGE: javascript
CODE:
db.inventory.updateMany(
   { "qty": { $lt: 50 } },
   {
     $set: { "size.uom": "in", status: "P" },
     $currentDate: { lastModified: true }
   }
)

----------------------------------------

TITLE: Creating a Database and Collection in MongoDB Shell
DESCRIPTION: This snippet shows how to create a new database and collection in MongoDB by inserting a document. If the database and collection don't exist, MongoDB creates them automatically.

LANGUAGE: javascript
CODE:
use myNewDB

db.myNewCollection1.insertOne( { x: 1 } )

----------------------------------------

TITLE: Using Projections in MongoDB Queries
DESCRIPTION: This snippet demonstrates how to use projections to return only specific fields (timestamp, title, author, and abstract) from documents in the 'posts' collection, improving query performance.

LANGUAGE: javascript
CODE:
db.posts.find( {}, { timestamp : 1 , title : 1 , author : 1 , abstract : 1} ).sort( { timestamp : -1 } )

----------------------------------------

TITLE: MongoDB User Management Methods Reference
DESCRIPTION: A collection of essential MongoDB shell methods for user management, including authentication (db.auth()), user creation (db.createUser()), password management (db.changeUserPassword()), and role management (db.grantRolesToUser(), db.revokeRolesFromUser()).

LANGUAGE: mongodb
CODE:
db.auth()
db.changeUserPassword()
db.createUser()
db.dropUser()
db.dropAllUsers()
db.getUser()
db.getUsers()
db.grantRolesToUser()
db.removeUser()
db.revokeRolesFromUser()
db.updateUser()
passwordPrompt()

----------------------------------------

TITLE: Basic $bucket Syntax in MongoDB Aggregation
DESCRIPTION: Demonstrates the basic syntax for using the $bucket stage in a MongoDB aggregation pipeline. It shows the structure including groupBy, boundaries, default, and output fields.

LANGUAGE: javascript
CODE:
{ 
  $bucket: {
      groupBy: <expression>,
      boundaries: [ <lowerbound1>, <lowerbound2>, ... ],
      default: <literal>,
      output: {
         <output1>: { <$accumulator expression> },
         ...
         <outputN>: { <$accumulator expression> }
      }
   }
}

----------------------------------------

TITLE: Inserting Encrypted Document with MongoDB CSFLE (Multiple Languages)
DESCRIPTION: Demonstrates how to insert an encrypted document into the medicalRecords.patients collection using a CSFLE-enabled MongoClient. The operation automatically encrypts specified fields before insertion. Each implementation shows language-specific patterns for document insertion with encryption.

LANGUAGE: json
CODE:
// Note: Actual code snippets not provided in the original content, but referenced as included files:
// - Java: InsertEncryptedDocument.java
// - Node.js: insert_encrypted_document.js
// - Python: insert_encrypted_document.py
// - C#: InsertEncryptedDocument.cs
// - Go: insert-encrypted-document.go
// - JSON: inserted-doc-enc.json

----------------------------------------

TITLE: Sort, Skip and Limit Stage Optimization Example
DESCRIPTION: Demonstrates optimization of a pipeline containing $sort, $skip and $limit stages through stage coalescence and limit adjustment.

LANGUAGE: javascript
CODE:
{ $sort: { age : -1 } },
{ $skip: 10 },
{ $limit: 5 }

----------------------------------------

TITLE: MongoDB Basic Document Structure
DESCRIPTION: Example showing separate documents for a patron and their addresses before embedding.

LANGUAGE: javascript
CODE:
// patron document
{
   _id: "joe",
   name: "Joe Bookreader"
}

// address one
{
   street: "123 Fake Street",
   city: "Faketon",
   state: "MA",
   zip: "12345"
}

// address two
{
   street: "1 Some Other Street",
   city: "Boston",
   state: "MA",
   zip: "12345"
}

----------------------------------------

TITLE: Inserting Polymorphic Athlete Data in MongoDB
DESCRIPTION: This code snippet demonstrates how to insert multiple documents with different structures into a single MongoDB collection named 'athletes'. It includes data for athletes from bowling, tennis, and cricket, each with sport-specific attributes.

LANGUAGE: javascript
CODE:
db.athletes.insertMany( [
   {
      sport: "bowling",
      name: "Earl Anthony",
      career_earnings: 1440000,
      perfect_games: 25,
      pba_championships: 43,
      events: [
         {
            name: "japan_pba",
            score: 300,
            year: 1972
         }
      ]
   },
   {
      sport: "tennis",
      name: "Steffi Graf",
      career_earnings: 21000000,
      grand_slam_wins: 22,
      surfaces: [ "grass", "clay", "hard court" ]
   },
   {
      sport: "cricket",
      name: "Sachin Tendulkar",
      career_earnings: 8000000,
      runs: 15921,
      centuries: 51,
      teammates: [ "Arshad Ayub", "Kapil Dev" ]
   }
] )

----------------------------------------

TITLE: Inserting Encrypted Document with Node.js MongoDB Driver
DESCRIPTION: This snippet shows how to insert an encrypted document into the 'medicalRecords.patients' namespace using the Node.js MongoDB driver with Queryable Encryption enabled.

LANGUAGE: javascript
CODE:
// Code snippet not provided in the input text

----------------------------------------

TITLE: Creating an Ascending Index on a Single Field in MongoDB
DESCRIPTION: Creates an ascending index on the orderDate field of a collection.

LANGUAGE: javascript
CODE:
db.collection.createIndex( { orderDate: 1 } )

----------------------------------------

TITLE: Basic $match Syntax in MongoDB Aggregation
DESCRIPTION: Demonstrates the basic syntax structure for the $match aggregation operator in MongoDB.

LANGUAGE: javascript
CODE:
{ $match: { <query predicate> } }

----------------------------------------

TITLE: Checking MongoDB Collection Indexes
DESCRIPTION: Shows how to view existing indexes on a MongoDB collection using the getIndexes() method in the mongo shell. Returns an array of index specifications including the _id index and any custom indexes.

LANGUAGE: javascript
CODE:
db.collection.getIndexes()

----------------------------------------

TITLE: Initializing MongoDB Replica Set in Shell
DESCRIPTION: This snippet shows how to initialize a MongoDB replica set using the rs.initiate() method in the MongoDB shell. It configures a three-member replica set with specified hostnames and ports.

LANGUAGE: javascript
CODE:
rs.initiate(
  {
    _id : "myReplSet",
    members: [
      { _id : 0, host : "mongodb0.example.net:27017" },
      { _id : 1, host : "mongodb1.example.net:27017" },
      { _id : 2, host : "mongodb2.example.net:27017" }
    ]
  }
)

----------------------------------------

TITLE: Inserting Encrypted Document with CSFLE in Python
DESCRIPTION: This snippet illustrates how to insert an encrypted document using a CSFLE-enabled MongoClient in Python. It inserts a document into the 'medicalRecords.patients' collection with encrypted fields.

LANGUAGE: python
CODE:
# Code snippet not provided in the given text

----------------------------------------

TITLE: Using Query Operator on Nested Field in MongoDB
DESCRIPTION: This example shows how to use a query operator (less than) on a nested field. It selects documents where the 'h' field embedded in the 'size' field is less than 15.

LANGUAGE: javascript
CODE:
db.inventory.find( { "size.h": { $lt: 15 } } )

----------------------------------------

TITLE: Querying Encrypted Documents in Java
DESCRIPTION: This Java code snippet illustrates how to query a document with encrypted fields. It demonstrates the difference in query results between a client configured for automatic Queryable Encryption and one that is not.

LANGUAGE: java
CODE:
start-find
end-find