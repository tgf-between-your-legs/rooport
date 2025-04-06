TITLE: PostgreSQL Database Connection Command
DESCRIPTION: Shows how to connect to PostgreSQL database using psql client tool.

LANGUAGE: php
CODE:
psql -U postgres

----------------------------------------

TITLE: Installing Neon Serverless Driver
DESCRIPTION: Command to install the Neon serverless driver using npm package manager

LANGUAGE: shell
CODE:
npm install @neondatabase/serverless

----------------------------------------

TITLE: Connecting to Neon Database from Go Application
DESCRIPTION: This code snippet demonstrates how to establish a connection to a Neon database from a Go application using the sql/db package and the lib/pq driver. It includes error handling and a simple query to fetch the database version.

LANGUAGE: go
CODE:
package main

import (
    "database/sql"
    "fmt"

    _ "github.com/lib/pq"
)

func main() {
    connStr := "postgresql://[user]:[password]@[neon_hostname]/[dbname]?sslmode=require"
    db, err := sql.Open("postgres", connStr)
    if err != nil {
        panic(err)
    }
    defer db.Close()

    var version string
    if err := db.QueryRow("select version()").Scan(&version); err != nil {
        panic(err)
    }

    fmt.Printf("version=%s\n", version)
}

----------------------------------------

TITLE: Identifying Long-Running Queries in Postgres
DESCRIPTION: This SQL query lists the top 100 queries with the longest average execution time, including user ID, query text, execution count, and mean execution time.

LANGUAGE: sql
CODE:
SELECT
    userid,
    query,
    calls,
    mean_exec_time
FROM
    pg_stat_statements
ORDER BY
    mean_exec_time DESC
LIMIT 100;

----------------------------------------

TITLE: Using Multiple CTEs for Complex Statistics
DESCRIPTION: This example demonstrates the use of multiple CTEs to calculate various statistics related to films and customers. It shows how to define and use multiple CTEs in a single query to produce a comprehensive report.

LANGUAGE: SQL
CODE:
WITH film_stats AS (
    -- CTE 1: Calculate film statistics
    SELECT
        AVG(rental_rate) AS avg_rental_rate,
        MAX(length) AS max_length,
        MIN(length) AS min_length
    FROM film
),
customer_stats AS (
    -- CTE 2: Calculate customer statistics
    SELECT
        COUNT(DISTINCT customer_id) AS total_customers,
        SUM(amount) AS total_payments
    FROM payment
)
-- Main query using the CTEs
SELECT
    ROUND((SELECT avg_rental_rate FROM film_stats), 2) AS avg_film_rental_rate,
    (SELECT max_length FROM film_stats) AS max_film_length,
    (SELECT min_length FROM film_stats) AS min_film_length,
    (SELECT total_customers FROM customer_stats) AS total_customers,
    (SELECT total_payments FROM customer_stats) AS total_payments;

----------------------------------------

TITLE: Updating Project Settings with Neon API (Bash)
DESCRIPTION: This snippet demonstrates how to use the Neon API to update a project's maintenance window settings. It specifies the day of the week and time range for updates.

LANGUAGE: bash
CODE:
curl --request PATCH \
     --url https://console.neon.tech/api/v2/projects/fragrant-mode-99795914 \
     --header 'accept: application/json' \
     --header 'authorization: Bearer $NEON_API' \
     --header 'content-type: application/json' \
     --data '
{
  "project": {
    "settings": {
      "maintenance_window": {
        "weekdays": [
          7
        ],
        "start_time": "01:00",
        "end_time": "02:00"
      }
    }
  }
}
'

----------------------------------------

TITLE: Basic PostgreSQL CREATE TABLE Syntax
DESCRIPTION: Shows the fundamental syntax for creating a new table in PostgreSQL, including column definitions and table constraints.

LANGUAGE: sql
CODE:
CREATE TABLE [IF NOT EXISTS] table_name (
   column1 datatype(length) column_constraint,
   column2 datatype(length) column_constraint,
   ...
   table_constraints
);

----------------------------------------

TITLE: Creating Optuna Study for Hyperparameter Tuning in Python
DESCRIPTION: Demonstrates how to create an Optuna study for hyperparameter tuning, using a Neon Postgres database for storage and specifying optimization direction.

LANGUAGE: python
CODE:
if __name__ == "__main__":
    study = optuna.create_study(
        study_name="sklearn_example",
        storage=os.environ["DATABASE_URL"],
        load_if_exists=True,
        direction="maximize",
    )
    study.optimize(objective, n_trials=100)

----------------------------------------

TITLE: Initializing Postgres Vector Store in LlamaIndex
DESCRIPTION: Creates a new PGVectorStore instance using the Postgres connection URL from environment variables. This sets up the vector store for use with LlamaIndex.

LANGUAGE: typescript
CODE:
import 'dotenv/config';
import { PGVectorStore } from 'llamaindex';

export default new PGVectorStore({
  connectionString: process.env.POSTGRES_URL,
});

----------------------------------------

TITLE: Role and Privilege Management Commands
DESCRIPTION: Commands for managing user roles, privileges, and security settings in PostgreSQL.

LANGUAGE: sql
CODE:
CREATE ROLE
GRANT
REVOKE
ALTER ROLE
DROP ROLE
SET ROLE

----------------------------------------

TITLE: Basic Syntax of PostgreSQL Recursive CTE
DESCRIPTION: Demonstrates the basic syntax structure of a recursive common table expression in PostgreSQL. It includes an anchor member, a recursive term, and the final SELECT statement.

LANGUAGE: SQL
CODE:
WITH RECURSIVE cte_name (column1, column2, ...)
AS(
    -- anchor member
    SELECT select_list FROM table1 WHERE condition

    UNION [ALL]

    -- recursive term
    SELECT select_list FROM cte_name WHERE recursive_condition
)
SELECT * FROM cte_name;

----------------------------------------

TITLE: Creating Accounts Table Example
DESCRIPTION: Demonstrates creating a table named 'accounts' with various column types and constraints including PRIMARY KEY, UNIQUE, and NOT NULL constraints.

LANGUAGE: sql
CODE:
CREATE TABLE accounts (
  user_id SERIAL PRIMARY KEY,
  username VARCHAR (50) UNIQUE NOT NULL,
  password VARCHAR (50) NOT NULL,
  email VARCHAR (255) UNIQUE NOT NULL,
  created_at TIMESTAMP NOT NULL,
  last_login TIMESTAMP
);

----------------------------------------

TITLE: Inserting Single Row into PostgreSQL using Python
DESCRIPTION: Function to insert a single vendor record into the vendors table and return the generated vendor_id. Uses psycopg2 for database connection and implements proper error handling and transaction management.

LANGUAGE: python
CODE:
import psycopg2
from config import load_config


def insert_vendor(vendor_name):
    """ Insert a new vendor into the vendors table """

    sql = """INSERT INTO vendors(vendor_name)
             VALUES(%s) RETURNING vendor_id;"""

    vendor_id = None
    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(sql, (vendor_name,))

                # get the generated id back
                rows = cur.fetchone()
                if rows:
                    vendor_id = rows[0]

                # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return vendor_id


if __name__ == '__main__':
    insert_vendor("3M Co.")

----------------------------------------

TITLE: Defining Pydantic Models for Product Data Validation
DESCRIPTION: Creates Pydantic models for validating product data, including models for product creation, updates, and stock management.

LANGUAGE: python
CODE:
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class Product(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    price: float
    quantity: int
    description: Optional[str]

class ProductCreate(BaseModel):
    name: str
    price: float = Field(..., ge=0)
    quantity: int = Field(..., ge=0)
    description: Optional[str] = Field(None, max_length=255)

----------------------------------------

TITLE: Configuring Django Database Settings for Neon PostgreSQL
DESCRIPTION: Configuration code for Django's settings.py file to establish a connection with Neon PostgreSQL. Uses environment variables for secure credential management and includes required SSL settings.

LANGUAGE: python
CODE:
# Add these at the top of your settings.py
from os import getenv
from dotenv import load_dotenv

# Replace the DATABASES section of your settings.py with this
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': getenv('PGDATABASE'),
    'USER': getenv('PGUSER'),
    'PASSWORD': getenv('PGPASSWORD'),
    'HOST': getenv('PGHOST'),
    'PORT': getenv('PGPORT', 5432),
    'OPTIONS': {
      'sslmode': 'require',
    },
    'DISABLE_SERVER_SIDE_CURSORS': True,
  }
}

----------------------------------------

TITLE: Basic Exception Clause Syntax in PL/pgSQL
DESCRIPTION: Demonstrates the fundamental syntax structure for exception handling in PL/pgSQL blocks, showing how to declare conditions and handle multiple exception types.

LANGUAGE: sql
CODE:
<<label>>
declare
   ...
begin
    ...
exception
    when condition [or condition...] then
       handle_exception;
   [when condition [or condition...] then
       handle_exception;]
   [when others then
       handle_other_exceptions;
   ]
end;

----------------------------------------

TITLE: Defining Django Models for AI Marketplace
DESCRIPTION: Creates Python classes representing database tables for ModelAuthor, AIModel, ModelPurchase, UsageScenario, and ModelBenchmark entities.

LANGUAGE: python
CODE:
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class ModelAuthor(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    contact_info = models.EmailField()
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return self.name

class AIModel(models.Model):
    MODEL_TYPES = [
        ('NLP', 'Natural Language Processing'),
        ('CV', 'Computer Vision'),
        ('RL', 'Reinforcement Learning'),
        ('OTHER', 'Other'),
    ]
    FRAMEWORKS = [
        ('PT', 'PyTorch'),
        ('TF', 'TensorFlow'),
        ('KRS', 'Keras'),
        ('OTHER', 'Other'),
    ]
    name = models.CharField(max_length=200)
    model_type = models.CharField(max_length=5, choices=MODEL_TYPES)
    description = models.TextField()
    framework = models.CharField(max_length=5, choices=FRAMEWORKS)
    version = models.CharField(max_length=50)
    download_url = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tags = models.JSONField()
    author = models.ForeignKey(ModelAuthor, on_delete=models.CASCADE, related_name='models_uploaded')

    def __str__(self):
        return f"{self.name} - {self.version}"

class ModelPurchase(models.Model):
    user = models.CharField(max_length=200)  # Simplified for this example
    ai_model = models.ForeignKey(AIModel, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    price_paid = models.DecimalField(max_digits=10, decimal_places=2)
    license_key = models.CharField(max_length=100)
    download_link = models.URLField()

    def __str__(self):
        return f"{self.user} - {self.ai_model.name}"

class UsageScenario(models.Model):
    ai_model = models.ForeignKey(AIModel, on_delete=models.CASCADE, related_name='usage_scenarios')
    title = models.CharField(max_length=200)
    description = models.TextField()
    code_snippet = models.TextField()
    usage_frequency = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.ai_model.name} - {self.title}"

class ModelBenchmark(models.Model):
    ai_model = models.ForeignKey(AIModel, on_delete=models.CASCADE, related_name='benchmarks')
    metric_name = models.CharField(max_length=100)
    value = models.FloatField()
    benchmark_date = models.DateTimeField(auto_now_add=True)
    hardware_used = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.ai_model.name} - {self.metric_name}: {self.value}"

----------------------------------------

TITLE: Using ROW_NUMBER() Window Function in PostgreSQL
DESCRIPTION: This SQL query demonstrates the ROW_NUMBER() window function. It assigns a sequential number to each row within partitions defined by product groups, ordered by price.

LANGUAGE: SQL
CODE:
SELECT
	product_name,
	group_name,
	price,
	ROW_NUMBER () OVER (
		PARTITION BY group_name
		ORDER BY
			price
	)
FROM
	products
INNER JOIN product_groups USING (group_id);

----------------------------------------

TITLE: Implementing Django REST Framework Serializers
DESCRIPTION: Creates serializer classes for each model to handle conversion between complex data types and JSON representations.

LANGUAGE: python
CODE:
from rest_framework import serializers
from .models import ModelAuthor, AIModel, ModelPurchase, UsageScenario, ModelBenchmark

class ModelAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelAuthor
        fields = ['id', 'name', 'bio', 'contact_info', 'rating']

class AIModelSerializer(serializers.ModelSerializer):
    author = ModelAuthorSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=ModelAuthor.objects.all(), source='author', write_only=True
    )

    class Meta:
        model = AIModel
        fields = ['id', 'name', 'model_type', 'description', 'framework', 'version',
                  'download_url', 'price', 'tags', 'author', 'author_id']

class ModelPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelPurchase
        fields = ['id', 'user', 'ai_model', 'purchase_date', 'price_paid', 'license_key', 'download_link']

class UsageScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsageScenario
        fields = ['id', 'ai_model', 'title', 'description', 'code_snippet', 'usage_frequency']

class ModelBenchmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelBenchmark
        fields = ['id', 'ai_model', 'metric_name', 'value', 'benchmark_date', 'hardware_used']

----------------------------------------

TITLE: Retrieving Cities in the United States Using a Subquery
DESCRIPTION: This example uses a subquery to first find the country_id for the United States, then uses that result in the main query to retrieve all cities in that country.

LANGUAGE: SQL
CODE:
SELECT
  city
FROM
  city
WHERE
  country_id = (
    SELECT
      country_id
    FROM
      country
    WHERE
      country = 'United States'
  )
ORDER BY
  city;

----------------------------------------

TITLE: Creating and Populating a Blog Posts Table with tsvector in PostgreSQL
DESCRIPTION: This example shows how to create a table with a tsvector column for full-text search, insert sample data, update the search vector, and create an index for improved search performance.

LANGUAGE: sql
CODE:
CREATE TABLE blog_posts (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    search_vector tsvector
);

INSERT INTO blog_posts (title, content)
VALUES
    ('PostgreSQL Full-Text Search', 'PostgreSQL offers powerful full-text search capabilities using tsvector and tsquery.'),
    ('Indexing in Databases', 'Proper indexing is crucial for database performance. It can significantly speed up query execution.'),
    ('ACID Properties', 'ACID (Atomicity, Consistency, Isolation, Durability) properties ensure reliable processing of database transactions.');

UPDATE blog_posts
SET search_vector = to_tsvector('english', title || ' ' || content);

CREATE INDEX idx_search_vector ON blog_posts USING GIN (search_vector);

----------------------------------------

TITLE: Defining Objective Function for TensorFlow/Keras Model Optimization
DESCRIPTION: Implements an objective function for optimizing hyperparameters of a TensorFlow/Keras convolutional neural network model using Optuna, including number of filters, kernel size, and learning rate.

LANGUAGE: python
CODE:
import urllib
import os

import optuna
from tensorflow.keras.backend import clear_session
from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import RMSprop

N_TRAIN_EXAMPLES = 3000
N_VALID_EXAMPLES = 1000
BATCHSIZE = 128
CLASSES = 10
EPOCHS = 10


def objective(trial):
    clear_session()

    (x_train, y_train), (x_valid, y_valid) = mnist.load_data()
    img_x, img_y = x_train.shape[1], x_train.shape[2]
    x_train = x_train.reshape(-1, img_x, img_y, 1)[:N_TRAIN_EXAMPLES].astype("float32") / 255
    x_valid = x_valid.reshape(-1, img_x, img_y, 1)[:N_VALID_EXAMPLES].astype("float32") / 255
    y_train = y_train[:N_TRAIN_EXAMPLES]
    y_valid = y_valid[:N_VALID_EXAMPLES]
    input_shape = (img_x, img_y, 1)

    model = Sequential()
    model.add(
        Conv2D(
            filters=trial.suggest_categorical("filters", [32, 64]),
            kernel_size=trial.suggest_categorical("kernel_size", [3, 5]),
            strides=trial.suggest_categorical("strides", [1, 2]),
            activation=trial.suggest_categorical("activation", ["relu", "linear"]),
            input_shape=input_shape,
        )
    )
    model.add(Flatten())
    model.add(Dense(CLASSES, activation="softmax"))

    learning_rate = trial.suggest_float("learning_rate", 1e-5, 1e-1, log=True)
    model.compile(
        loss="sparse_categorical_crossentropy",
        optimizer=RMSprop(learning_rate=learning_rate),
        metrics=["accuracy"],
    )

    model.fit(
        x_train,
        y_train,
        validation_data=(x_valid, y_valid),
        shuffle=True,
        batch_size=BATCHSIZE,
        epochs=EPOCHS,
        verbose=False,
    )

    score = model.evaluate(x_valid, y_valid, verbose=0)
    return score[1]

if __name__ == "__main__":
    study = optuna.create_study(
        study_name="tfkeras_example",
        storage=os.environ["DATABASE_URL"],
        load_if_exists=True,
        direction="maximize",
    )
    study.optimize(objective, n_trials=100, timeout=600)

----------------------------------------

TITLE: Hashing Password with crypt Function
DESCRIPTION: Example of using the crypt function to hash a password. It uses the gen_salt function to generate a salt for the MD5 algorithm.

LANGUAGE: sql
CODE:
SELECT crypt('user_password', gen_salt('md5'));

----------------------------------------

TITLE: Using date_trunc() with Interval Types
DESCRIPTION: This query demonstrates how date_trunc() can be used with interval data types and for calculating differences between timestamps.

LANGUAGE: sql
CODE:
SELECT
  date_trunc('hour', INTERVAL '2 days 3 hours 40 minutes') AS truncated_interval,
  date_trunc('day', '2024-03-15 23:30:00+00'::TIMESTAMPTZ - '2023-09-14 11:20:00+00'::TIMESTAMPTZ) AS truncated_day;

----------------------------------------

TITLE: Synchronous Python Database Connection
DESCRIPTION: Python script using psycopg2 to connect to Neon database and retrieve time and version information using connection pooling

LANGUAGE: python
CODE:
import os
from psycopg2 import pool
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get the connection string from the environment variable
connection_string = os.getenv('DATABASE_URL')

# Create a connection pool
connection_pool = pool.SimpleConnectionPool(
    1,  # Minimum number of connections in the pool
    10,  # Maximum number of connections in the pool
    connection_string
)

# Check if the pool was created successfully
if connection_pool:
    print("Connection pool created successfully")

# Get a connection from the pool
conn = connection_pool.getconn()

# Create a cursor object
cur = conn.cursor()

# Execute SQL commands to retrieve the current time and version from PostgreSQL
cur.execute('SELECT NOW();')
time = cur.fetchone()[0]

cur.execute('SELECT version();')
version = cur.fetchone()[0]

# Close the cursor and return the connection to the pool
cur.close()
connection_pool.putconn(conn)

# Close all connections in the pool
connection_pool.closeall()

# Print the results
print('Current time:', time)
print('PostgreSQL version:', version)

----------------------------------------

TITLE: Two-Table JOIN Example with Customer and Payment
DESCRIPTION: Practical example showing how to join customer and payment tables to retrieve customer information along with their payment details.

LANGUAGE: sql
CODE:
SELECT
  customer.customer_id,
  customer.first_name,
  customer.last_name,
  payment.amount,
  payment.payment_date
FROM
  customer
  INNER JOIN payment ON payment.customer_id = customer.customer_id
ORDER BY
  payment.payment_date;

----------------------------------------

TITLE: Basic PostgreSQL INSERT Statement Syntax
DESCRIPTION: Demonstrates the basic syntax of the PostgreSQL INSERT statement for inserting a new row into a table.

LANGUAGE: sql
CODE:
INSERT INTO table1(column1, column2, …)
VALUES (value1, value2, …);

----------------------------------------

TITLE: Creating a Table with GENERATED ALWAYS AS IDENTITY Column
DESCRIPTION: This snippet demonstrates how to create a table named 'color' with an identity column 'color_id' using the GENERATED ALWAYS AS IDENTITY constraint.

LANGUAGE: sql
CODE:
CREATE TABLE color (
    color_id INT GENERATED ALWAYS AS IDENTITY,
    color_name VARCHAR NOT NULL
);

----------------------------------------

TITLE: Node.js Lambda Function Implementation
DESCRIPTION: AWS Lambda function implementation using Node.js and the pg library to connect to Neon database and retrieve user data. Includes error handling and connection management.

LANGUAGE: javascript
CODE:
'use strict';
const { Client } = require('pg');

let client;

module.exports.getAllUsers = async () => {
  if (!client) {
    console.log('Initializing new database client');
    client = new Client({ connectionString: process.env.DATABASE_URL });
    try {
      await client.connect();
    } catch (error) {
      console.error('Error connecting to the database:', error);
      return {
        statusCode: 500,
        body: JSON.stringify({
          error: 'Failed to connect to the database',
        }),
      };
    }
  }

  try {
    const { rows } = await client.query('SELECT * FROM users');
    return {
      statusCode: 200,
      body: JSON.stringify({
        data: rows,
      }),
    };
  } catch (error) {
    console.error('Error executing query:', error);
    return {
      statusCode: 500,
      body: JSON.stringify({
        error: 'Failed to fetch users',
      }),
    };
  }
};

----------------------------------------

TITLE: Basic PL/pgSQL Block Structure Syntax
DESCRIPTION: Shows the fundamental syntax structure of a PL/pgSQL block including optional label, declaration section, and body section

LANGUAGE: sql
CODE:
[ <<label>> ]
[ declare
    declarations ]
begin
    statements;
    ...
end [ label ];

----------------------------------------

TITLE: Using max() with GROUP BY in SQL
DESCRIPTION: This SQL query demonstrates using max() with GROUP BY to find the largest order amount for each customer. It also includes ORDER BY and LIMIT clauses to show the top 5 customers.

LANGUAGE: sql
CODE:
SELECT customer_id, max(order_amount) AS largest_order
FROM orders
GROUP BY customer_id
ORDER BY largest_order DESC
LIMIT 5;

----------------------------------------

TITLE: Creating Table with Multi-Column Primary Key in PostgreSQL
DESCRIPTION: This example shows how to define a primary key constraint using multiple columns ('order_id' and 'item_no') when creating a table.

LANGUAGE: sql
CODE:
CREATE TABLE order_items(
  order_id INT,
  item_no SERIAL,
  item_description VARCHAR NOT NULL,
  quantity INTEGER NOT NULL,
  price DEC(10, 2),
  PRIMARY KEY (order_id, item_no)
);