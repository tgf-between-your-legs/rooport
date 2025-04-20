# Elasticsearch: Analyzers Reference

Understanding and configuring text analysis in Elasticsearch.

## Core Concept: Analysis

Analysis is the process Elasticsearch uses to convert full-text (`text` field type) into a structured format suitable for searching (the inverted index). This process happens at both index time (when a document is added) and query time (when a `match` query or similar is executed).

An **Analyzer** orchestrates this process. It's typically composed of:

1.  **Character Filter(s) (Optional):** Pre-process the raw text *before* tokenization (e.g., stripping HTML tags, replacing characters).
2.  **Tokenizer (Required):** Splits the text stream into individual tokens (words).
3.  **Token Filter(s) (Optional):** Process the tokens *after* tokenization (e.g., lowercasing, removing stop words, stemming).

## Built-in Analyzers

Elasticsearch provides several pre-configured analyzers:

*   **`standard` (Default):** The default for `text` fields. Uses the standard tokenizer (grammar-based, splits on word boundaries and punctuation), lowercase token filter, and stop token filter (removes common English stop words like "a", "the", "is"). Good general-purpose analyzer.
*   **`simple`:** Uses the lowercase tokenizer (splits on non-letters), converting everything to lowercase.
*   **`whitespace`:** Uses the whitespace tokenizer (splits only on whitespace). Does not lowercase.
*   **`stop`:** Like `simple`, but also removes stop words.
*   **`keyword`:** A "noop" analyzer that treats the entire input string as a single token. Useful for fields that should be searchable but not broken down (though the `keyword` field type is usually preferred for this).
*   **`pattern`:** Uses a regular expression pattern to split text into tokens.
*   **`fingerprint`:** Creates a single normalized token for complex values like IDs or URLs.
*   **Language Analyzers:** (`english`, `french`, `german`, `spanish`, etc.) Pre-configured analyzers optimized for specific languages, often including language-specific stop words and stemming rules.

## Custom Analyzers

You can define custom analyzers in the index settings (`analysis` section) by combining built-in or custom character filters, tokenizers, and token filters.

**Defining Custom Analyzer Structure:**

```json
// PUT /my-custom-index
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_custom_analyzer": { // Your custom analyzer name
          "type": "custom", // Required for custom analyzers
          "tokenizer": "standard", // Specify tokenizer (e.g., standard, whitespace, pattern, etc.)
          "char_filter": [ // Optional: List of character filters
            "html_strip"
          ],
          "filter": [ // Optional: List of token filters (order matters)
            "lowercase",
            "my_custom_stop_filter", // Reference custom or built-in filters
            "my_custom_stemmer"
          ]
        }
        // ... other custom analyzers ...
      },
      "tokenizer": { // Optional: Define custom tokenizers
        "my_ngram_tokenizer": {
          "type": "ngram",
          "min_gram": 3,
          "max_gram": 3,
          "token_chars": ["letter", "digit"]
        }
      },
      "filter": { // Optional: Define custom token filters
        "my_custom_stop_filter": {
          "type": "stop",
          "stopwords": ["and", "or", "but"] // Define custom stop words
        },
        "my_custom_stemmer": {
          "type": "stemmer",
          "language": "english"
        }
      },
      "char_filter": { // Optional: Define custom character filters
        // ...
      }
    }
  },
  "mappings": {
    "properties": {
      "title": {
        "type": "text",
        "analyzer": "my_custom_analyzer" // Apply the custom analyzer
      },
      "content": {
        "type": "text",
        "analyzer": "standard" // Use a built-in analyzer
      }
    }
  }
}
```

## Testing Analyzers (`_analyze` API)

Use the `_analyze` API to see how text would be tokenized by a specific analyzer (built-in or custom).

```json
// Test the standard analyzer
// POST /_analyze
// {
//   "analyzer": "standard",
//   "text": "The Quick Brown Fox!"
// }
// --> Output: { "tokens": [ { "token": "quick", ... }, { "token": "brown", ... }, { "token": "fox", ... } ] }

// Test a custom analyzer defined in an index
// POST /my-custom-index/_analyze
// {
//   "analyzer": "my_custom_analyzer",
//   "text": "<p>Some HTML text.</p>"
// }
// --> Output: { "tokens": [ { "token": "some", ... }, { "token": "html", ... }, { "token": "text", ... } ] }

// Test analyzer components individually
// POST /_analyze
// {
//   "tokenizer": "whitespace",
//   "filter": ["lowercase", "stop"],
//   "text": "This IS a Test"
// }
// --> Output: { "tokens": [ { "token": "test", ... } ] }
```

## Key Considerations

*   **Index vs. Search Analyzers:** You can specify different analyzers for indexing (`analyzer`) and searching (`search_analyzer`). This is useful if you want broader matching at query time than at index time, but ensure they produce compatible tokens.
*   **`keyword` vs `text`:** Remember that `keyword` fields are *not* analyzed by default. Use them for exact matches, sorting, and aggregations. Use `text` fields with appropriate analyzers for full-text search.
*   **Consistency:** Ensure the analyzer used at query time is compatible with the one used at index time for the field being searched.
*   **Performance:** Complex analysis (e.g., heavy stemming, many filters) adds overhead during indexing and querying.

Choosing and configuring the right analyzers is fundamental for effective full-text search in Elasticsearch.

*(Refer to the official Elasticsearch documentation on Text Analysis and Analyzers.)*