TITLE: Defining Runtime Field in Elasticsearch Mapping
DESCRIPTION: Example of adding a runtime field in the mapping definition that extracts the day of the week from a timestamp field. The script uses the @timestamp field to calculate the day name and emits it as a keyword type.

LANGUAGE: console
CODE:
PUT my-index/
{
  "mappings": {
    "runtime": {
      "day_of_week": {
        "type": "keyword",
        "script": {
          "source":
          """emit(doc['@timestamp'].value.dayOfWeekEnum
          .getDisplayName(TextStyle.FULL, Locale.ROOT))"""
        }
      }
    },
    "properties": {
      "@timestamp": {"type": "date"}
    }
  }
}

----------------------------------------

TITLE: Analyzing Text with Simple Analyzer in Elasticsearch
DESCRIPTION: Example showing how to use the simple analyzer to process text. The analyzer breaks down the input text into tokens at non-letter characters and converts them to lowercase.

LANGUAGE: console
CODE:
POST _analyze
{
  "analyzer": "simple",
  "text": "The 2 QUICK Brown-Foxes jumped over the lazy dog's bone."
}

----------------------------------------

TITLE: Basic Significant Terms Query
DESCRIPTION: Example of using significant terms aggregation to analyze crime types for British Transport Police.

LANGUAGE: console
CODE:
GET /_search
{
  "query": {
    "terms": { "force": [ "British Transport Police" ] }
  },
  "aggregations": {
    "significant_crime_types": {
      "significant_terms": { "field": "crime_type" }
    }
  }
}

----------------------------------------

TITLE: Simplified Match Query Syntax
DESCRIPTION: Shortened version of the match query combining field and query parameters

LANGUAGE: console
CODE:
GET /_search
{
  "query": {
    "match": {
      "message": "this is a test"
    }
  }
}

----------------------------------------

TITLE: Basic Simple Query String Search in Elasticsearch
DESCRIPTION: Example of a simple query string search using field boosting and boolean operators. The query searches for 'fried eggs' as a phrase, must include either 'eggplant' or 'potato', and excludes 'frittata'.

LANGUAGE: console
CODE:
GET /_search
{
  "query": {
    "simple_query_string" : {
        "query": "\"fried eggs\" +(eggplant | potato) -frittata",
        "fields": ["title^5", "body"],
        "default_operator": "and"
    }
  }
}

----------------------------------------

TITLE: Mapping a Match-Only Text Field
DESCRIPTION: Example of creating an index with a 'match_only_text' field for space-efficient text storage.

LANGUAGE: console
CODE:
PUT logs
{
  "mappings": {
    "properties": {
      "@timestamp": {
        "type": "date"
      },
      "message": {
        "type": "match_only_text"
      }
    }
  }
}

----------------------------------------

TITLE: Basic Nested Query in Elasticsearch
DESCRIPTION: Demonstrates a nested query searching for objects with specific name and count criteria within the nested field.

LANGUAGE: console
CODE:
GET /my-index-000001/_search
{
  "query": {
    "nested": {
      "path": "obj1",
      "query": {
        "bool": {
          "must": [
            { "match": { "obj1.name": "blue" } },
            { "range": { "obj1.count": { "gt": 5 } } }
          ]
        }
      },
      "score_mode": "avg"
    }
  }
}

----------------------------------------

TITLE: Configuring Multi-Analyzer Text Analysis in Elasticsearch
DESCRIPTION: Example demonstrating how to set up multiple analyzers for different query types, specifically handling stop words differently for phrase and non-phrase queries. Shows configuration of custom analyzers, field mappings, and document indexing with search examples.

LANGUAGE: console
CODE:
PUT my-index-000001
{
   "settings":{
      "analysis":{
         "analyzer":{
            "my_analyzer":{
               "type":"custom",
               "tokenizer":"standard",
               "filter":[
                  "lowercase"
               ]
            },
            "my_stop_analyzer":{
               "type":"custom",
               "tokenizer":"standard",
               "filter":[
                  "lowercase",
                  "english_stop"
               ]
            }
         },
         "filter":{
            "english_stop":{
               "type":"stop",
               "stopwords":"_english_"
            }
         }
      }
   },
   "mappings":{
       "properties":{
          "title": {
             "type":"text",
             "analyzer":"my_analyzer",
             "search_analyzer":"my_stop_analyzer",
             "search_quote_analyzer":"my_analyzer"
         }
      }
   }
}

PUT my-index-000001/_doc/1
{
   "title":"The Quick Brown Fox"
}

PUT my-index-000001/_doc/2
{
   "title":"A Quick Brown Fox"
}

GET my-index-000001/_search
{
   "query":{
      "query_string":{
         "query":"\"the quick brown fox\""
      }
   }
}

----------------------------------------

TITLE: Rule Retriever Example in Elasticsearch
DESCRIPTION: Shows how to use a rule retriever to apply query rules on top of search results.

LANGUAGE: console
CODE:
GET movies/_search
{
  "retriever": {
    "rule": {
      "match_criteria": {
        "query_string": "harry potter"
      },
      "ruleset_ids": [
        "my-ruleset"
      ],
      "retriever": {
        "standard": {
          "query": {
            "query_string": {
              "query": "harry potter"
            }
          }
        }
      }
    }
  }
}

----------------------------------------

TITLE: Basic Multi-Index Search in Elasticsearch
DESCRIPTION: Demonstrates how to search across multiple specific indices using comma-separated values in the search API path. The example searches for a user ID across two indices.

LANGUAGE: console
CODE:
GET /my-index-000001,my-index-000002/_search
{
  "query": {
    "match": {
      "user.id": "kimchy"
    }
  }
}

----------------------------------------

TITLE: Creating an Index with Aggregate Metric Double Field in Elasticsearch
DESCRIPTION: This snippet demonstrates how to create an Elasticsearch index with an aggregate_metric_double field. The field is configured with min, max, sum, and value_count metrics, with max set as the default metric.

LANGUAGE: console
CODE:
PUT my-index
{
  "mappings": {
    "properties": {
      "my-agg-metric-field": {
        "type": "aggregate_metric_double",
        "metrics": [ "min", "max", "sum", "value_count" ],
        "default_metric": "max"
      }
    }
  }
}

----------------------------------------

TITLE: Executing Match Phrase Prefix Query in Elasticsearch
DESCRIPTION: This snippet demonstrates how to use the match_phrase_prefix query to search for documents containing phrases beginning with 'quick brown f' in the 'message' field.

LANGUAGE: console
CODE:
GET /_search
{
  "query": {
    "match_phrase_prefix": {
      "message": {
        "query": "quick brown f"
      }
    }
  }
}

----------------------------------------

TITLE: Executing Variable Width Histogram Aggregation in Elasticsearch
DESCRIPTION: This snippet demonstrates how to request a variable width histogram aggregation with a target of 2 buckets on the 'price' field in Elasticsearch. The aggregation dynamically determines bucket intervals based on document distribution.

LANGUAGE: console
CODE:
POST /sales/_search?size=0
{
  "aggs": {
    "prices": {
      "variable_width_histogram": {
        "field": "price",
        "buckets": 2
      }
    }
  }
}

----------------------------------------

TITLE: Creating Vector Search Index in Elasticsearch
DESCRIPTION: Creates an index with dense vector mapping for image vectors, including configuration for dimensions, similarity metric, and additional fields.

LANGUAGE: console
CODE:
PUT my-image-index
{
  "mappings": {
    "properties": {
       "image-vector": {
        "type": "dense_vector",
        "dims": 3,
        "index": true,
        "similarity": "l2_norm"
      },
      "file-type": {
        "type": "keyword"
      },
      "title": {
        "type": "text"
      }
    }
  }
}

----------------------------------------

TITLE: Executing a Combined Fields Query in Elasticsearch
DESCRIPTION: This snippet demonstrates how to use the combined_fields query to search across multiple text fields (title, abstract, body) for specific terms with an AND operator.

LANGUAGE: json
CODE:
GET /_search
{
  "query": {
    "combined_fields" : {
      "query":      "database systems",
      "fields":     [ "title", "abstract", "body"],
      "operator":   "and"
    }
  }
}

----------------------------------------

TITLE: Mapping a Completion Field in Elasticsearch
DESCRIPTION: This snippet demonstrates how to map a field of type 'completion' in Elasticsearch. The example creates an index named 'music' with a 'suggest' field of type 'completion', which is used for generating fast completions.

LANGUAGE: json
CODE:
PUT music
{
  "mappings": {
    "properties": {
      "suggest": {
        "type": "completion"
      }
    }
  }
}

----------------------------------------

TITLE: Basic Boolean Query Example in Elasticsearch
DESCRIPTION: Demonstrates a boolean query combining multiple clause types including must, filter, must_not and should. Shows usage of minimum_should_match and boost parameters.

LANGUAGE: console
CODE:
POST _search
{
  "query": {
    "bool" : {
      "must" : {
        "term" : { "user.id" : "kimchy" }
      },
      "filter": {
        "term" : { "tags" : "production" }
      },
      "must_not" : {
        "range" : {
          "age" : { "gte" : 10, "lte" : 20 }
        }
      },
      "should" : [
        { "term" : { "tags" : "env1" } },
        { "term" : { "tags" : "deployed" } }
      ],
      "minimum_should_match" : 1,
      "boost" : 1.0
    }
  }
}

----------------------------------------

TITLE: Monitoring User Outbound Connections with ESQL
DESCRIPTION: Query that identifies users with high numbers of outbound connections to non-private IP addresses. Includes CIDR filtering, LDAP enrichment, and conditional evaluation for follow-up flagging.

LANGUAGE: esql
CODE:
FROM logs-*
| WHERE NOT CIDR_MATCH(destination.ip, "10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16")
| STATS destcount = COUNT(destination.ip) BY user.name, host.name
| ENRICH ldap_lookup_new ON user.name
| WHERE group.name IS NOT NULL
| EVAL follow_up = CASE(destcount >= 100, "true","false")
| SORT destcount DESC
| KEEP destcount, host.name, user.name, group.name, follow_up

----------------------------------------

TITLE: Executing a Disjunction Max Query in Elasticsearch
DESCRIPTION: This snippet demonstrates how to use the dis_max query to search for documents matching either 'Quick pets' in the title or body fields. It includes a tie_breaker parameter to adjust relevance scores for documents matching multiple clauses.

LANGUAGE: console
CODE:
GET /_search
{
  "query": {
    "dis_max": {
      "queries": [
        { "term": { "title": "Quick pets" } },
        { "term": { "body": "Quick pets" } }
      ],
      "tie_breaker": 0.7
    }
  }
}

----------------------------------------

TITLE: Basic Multi-match Query in Elasticsearch
DESCRIPTION: Example of a basic multi_match query searching across multiple fields. The query looks for 'this is a test' in both subject and message fields.

LANGUAGE: json
CODE:
{
  "query": {
    "multi_match" : {
      "query": "this is a test",
      "fields": [ "subject", "message" ]
    }
  }
}

----------------------------------------

TITLE: Rank Feature Query Example
DESCRIPTION: Demonstrates a bool query combining match query with rank feature queries to boost scores based on pagerank, url_length and sports topic.

LANGUAGE: console
CODE:
GET /test/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "content": "2016"
          }
        }
      ],
      "should": [
        {
          "rank_feature": {
            "field": "pagerank"
          }
        },
        {
          "rank_feature": {
            "field": "url_length",
            "boost": 0.1
          }
        },
        {
          "rank_feature": {
            "field": "topics.sports",
            "boost": 0.4
          }
        }
      ]
    }
  }
}

----------------------------------------

TITLE: Indexing and Querying Date Fields in Elasticsearch
DESCRIPTION: This example demonstrates how to define a mapping with a date field, index documents with various date formats, and perform a search query with date sorting.

LANGUAGE: console
CODE:
PUT my-index-000001
{
  "mappings": {
    "properties": {
      "date": {
        "type": "date"
      }
    }
  }
}

PUT my-index-000001/_doc/1
{ "date": "2015-01-01" }

PUT my-index-000001/_doc/2
{ "date": "2015-01-01T12:10:30Z" }

PUT my-index-000001/_doc/3
{ "date": 1420070400001 }

GET my-index-000001/_search
{
  "sort": { "date": "asc"}
}

----------------------------------------

TITLE: Querying Nested Aggregation for Minimum Price
DESCRIPTION: Performs a nested aggregation to find the minimum price across all resellers for a product.

LANGUAGE: console
CODE:
GET /products/_search?size=0
{
  "query": {
    "match": {
      "name": "led tv"
    }
  },
  "aggs": {
    "resellers": {
      "nested": {
        "path": "resellers"
      },
      "aggs": {
        "min_price": {
          "min": {
            "field": "resellers.price"
          }
        }
      }
    }
  }
}

----------------------------------------

TITLE: Indexing Vector Data in Elasticsearch
DESCRIPTION: Bulk indexes sample vector data with associated metadata using the _bulk API endpoint.

LANGUAGE: console
CODE:
POST my-image-index/_bulk?refresh=true
{ "index": { "_id": "1" } }
{ "image-vector": [1, 5, -20], "file-type": "jpg", "title": "mountain lake" }
{ "index": { "_id": "2" } }
{ "image-vector": [42, 8, -15], "file-type": "png", "title": "frozen lake"}
{ "index": { "_id": "3" } }
{ "image-vector": [15, 11, 23], "file-type": "jpg", "title": "mountain lake lodge" }

----------------------------------------

TITLE: Basic ESQL Query Structure
DESCRIPTION: Demonstrates the basic structure of an ESQL query with a source command and optional processing commands separated by pipe characters.

LANGUAGE: esql
CODE:
source-command
| processing-command1
| processing-command2

LANGUAGE: esql
CODE:
source-command | processing-command1 | processing-command2

----------------------------------------

TITLE: Configuring Arabic Analyzer in Elasticsearch
DESCRIPTION: Example of reimplementing the Arabic analyzer as a custom analyzer in Elasticsearch. It includes stopword removal, stemming, and keyword marking for excluding words from stemming.

LANGUAGE: JSON
CODE:
PUT /arabic_example
{
  "settings": {
    "analysis": {
      "filter": {
        "arabic_stop": {
          "type":       "stop",
          "stopwords":  "_arabic_"
        },
        "arabic_keywords": {
          "type":       "keyword_marker",
          "keywords":   ["مثال"]
        },
        "arabic_stemmer": {
          "type":       "stemmer",
          "language":   "arabic"
        }
      },
      "analyzer": {
        "rebuilt_arabic": {
          "tokenizer":  "standard",
          "filter": [
            "lowercase",
            "decimal_digit",
            "arabic_stop",
            "arabic_normalization",
            "arabic_keywords",
            "arabic_stemmer"
          ]
        }
      }
    }
  }
}

----------------------------------------

TITLE: Configuring Percolator Field Mapping
DESCRIPTION: Example showing how to configure a percolator field type in an Elasticsearch index mapping.

LANGUAGE: console
CODE:
PUT my-index-000001
{
  "mappings": {
    "properties": {
      "query": {
        "type": "percolator"
      },
      "field": {
        "type": "text"
      }
    }
  }
}

----------------------------------------

TITLE: Configuring Range Field Mappings in Elasticsearch
DESCRIPTION: This snippet demonstrates how to configure mappings for various range field types in Elasticsearch, including integer_range and date_range. It also shows how to index a document with range values.

LANGUAGE: console
CODE:
PUT range_index
{
  "settings": {
    "number_of_shards": 2
  },
  "mappings": {
    "properties": {
      "expected_attendees": {
        "type": "integer_range"
      },
      "time_frame": {
        "type": "date_range",
        "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
      }
    }
  }
}

PUT range_index/_doc/1?refresh
{
  "expected_attendees" : {
    "gte" : 10,
    "lt" : 20
  },
  "time_frame" : {
    "gte" : "2015-10-31 12:00:00",
    "lte" : "2015-11-01"
  }
}

----------------------------------------

TITLE: Creating and Querying an IP Field in Elasticsearch
DESCRIPTION: This snippet demonstrates how to create an index with an IP field, insert a document with an IP address, and perform a query using CIDR notation.

LANGUAGE: console
CODE:
PUT my-index-000001
{
  "mappings": {
    "properties": {
      "ip_addr": {
        "type": "ip"
      }
    }
  }
}

PUT my-index-000001/_doc/1
{
  "ip_addr": "192.168.1.1"
}

GET my-index-000001/_search
{
  "query": {
    "term": {
      "ip_addr": "192.168.0.0/16"
    }
  }
}

----------------------------------------

TITLE: Basic Average Aggregation in Elasticsearch
DESCRIPTION: Demonstrates how to compute a basic average over numeric fields in documents. This example calculates the average grade across exam documents.

LANGUAGE: console
CODE:
POST /exams/_search?size=0
{
  "aggs": {
    "avg_grade": { "avg": { "field": "grade" } }
  }
}

LANGUAGE: console-result
CODE:
{
  ...
  "aggregations": {
    "avg_grade": {
      "value": 75.0
    }
  }
}

----------------------------------------

TITLE: Basic Prefix Query in Elasticsearch
DESCRIPTION: Example of a basic prefix query that searches for documents where the user.id field contains terms beginning with 'ki'. Shows the standard query structure with field and value parameters.

LANGUAGE: console
CODE:
GET /_search
{
  "query": {
    "prefix": {
      "user.id": {
        "value": "ki"
      }
    }
  }
}

----------------------------------------

TITLE: Creating Index with Mapped Properties in Elasticsearch
DESCRIPTION: Demonstrates creating an Elasticsearch index with explicitly defined properties for both object and nested field types. The example shows mapping configuration for a manager object and nested employees array, including age and name fields for each.

LANGUAGE: console
CODE:
PUT my-index-000001
{
  "mappings": {
    "properties": {
      "manager": {
        "properties": {
          "age":  { "type": "integer" },
          "name": { "type": "text"  }
        }
      },
      "employees": {
        "type": "nested",
        "properties": {
          "age":  { "type": "integer" },
          "name": { "type": "text"  }
        }
      }
    }
  }
}

PUT my-index-000001/_doc/1
{
  "region": "US",
  "manager": {
    "name": "Alice White",
    "age": 30
  },
  "employees": [
    {
      "name": "John Smith",
      "age": 34
    },
    {
      "name": "Peter Brown",
      "age": 26
    }
  ]
}

----------------------------------------

TITLE: Performing Semantic Search in Elasticsearch
DESCRIPTION: This snippet demonstrates how to use the semantic query type to perform a semantic search on a semantic_text field. It searches for "Best surfing places" in the "inference_field".

LANGUAGE: console
CODE:
GET my-index-000001/_search
{
  "query": {
    "semantic": {
      "field": "inference_field",
      "query": "Best surfing places"
    }
  }
}

----------------------------------------

TITLE: ACL Filter Index Document Structure
DESCRIPTION: Example document structure from the access control index showing user permissions and query template for DLS

LANGUAGE: json
CODE:
{
  "_index": ".search-acl-filter-search-sharepoint",
  "_id": "john@example.co",
  "_version": 1,
  "_seq_no": 0,
  "_primary_term": 1,
  "found": true,
  "_source": {
    "identity": {
      "email": "john@example.co",
      "access_control": [
        "john@example.co",
        "Engineering Members"
      ]
    },
    "query": {
      "template": {
        "params": {
          "access_control": [
            "john@example.co",
            "Engineering Members"
            ]
        },
        "source": """
        {
          "bool": {
            "should": [
              {
                "bool": {
                  "must_not": {
                    "exists": {
                      "field": "_allow_access_control"
                    }
                  }
                }
              },
              {
                "terms": {
                  "_allow_access_control.enum": {{#toJson}}access_control{{/toJson}}
                }
              }
            ]
          }
        }
        """
      }
    }
  }
}

----------------------------------------

TITLE: Basic Match Query in Elasticsearch
DESCRIPTION: Simple example of a match query searching for text in a message field

LANGUAGE: console
CODE:
GET /_search
{
  "query": {
    "match": {
      "message": {
        "query": "this is a test"
      }
    }
  }
}

----------------------------------------

TITLE: Grouping Sales by Type with Top Hits in Elasticsearch
DESCRIPTION: This example demonstrates how to use the top_hits aggregation to group sales by type and show the last sale for each type. It includes source filtering to return only date and price fields.

LANGUAGE: json
CODE:
{
  "aggs": {
    "top_tags": {
      "terms": {
        "field": "type",
        "size": 3
      },
      "aggs": {
        "top_sales_hits": {
          "top_hits": {
            "sort": [
              {
                "date": {
                  "order": "desc"
                }
              }
            ],
            "_source": {
              "includes": [ "date", "price" ]
            },
            "size": 1
          }
        }
      }
    }
  }
}

----------------------------------------

TITLE: Configuring Custom Date Format in Elasticsearch Mapping
DESCRIPTION: This snippet demonstrates how to set up a custom date format for a field in an Elasticsearch index mapping. It uses the 'yyyy-MM-dd' format for the 'date' field.

LANGUAGE: console
CODE:
PUT my-index-000001
{
  "mappings": {
    "properties": {
      "date": {
        "type":   "date",
        "format": "yyyy-MM-dd"
      }
    }
  }
}

----------------------------------------

TITLE: Basic Terms Query Example in Elasticsearch
DESCRIPTION: Example of a terms query that searches for documents where user.id field matches either 'kimchy' or 'elkbee'. Includes optional boost parameter.

LANGUAGE: console
CODE:
GET /_search
{
  "query": {
    "terms": {
      "user.id": [ "kimchy", "elkbee" ],
      "boost": 1.0
    }
  }
}