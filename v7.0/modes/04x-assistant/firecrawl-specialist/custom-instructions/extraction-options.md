# Firecrawl Extraction Options

This document details the `extractorOptions` parameter used in the Firecrawl `/scrape` API endpoint.

## `extractorOptions` Object

This optional object controls how content is extracted from the scraped page.

*   **`mode`** (string): Specifies the extraction mode.
    *   `'markdown'` (Default): Extracts the main content of the page and converts it to clean Markdown. Good for general text content, articles, blogs.
    *   `'llm-extraction'`: Uses an LLM (like GPT) to extract structured data based on a provided JSON schema. Ideal for extracting specific fields from pages with consistent structures (e.g., product details, contact info).
*   **`schema`** (object, Required if `mode` is `'llm-extraction'`): A JSON schema object defining the desired structure of the extracted data.
    *   Uses standard JSON Schema vocabulary (`type`, `properties`, `required`, `description`, etc.).
    *   Define the fields you want to extract and their expected types (string, number, boolean, array, object).
    *   *Example:*
        ```json
        {
          "type": "object",
          "properties": {
            "product_name": {"type": "string", "description": "The main name of the product"},
            "price": {"type": "number", "description": "The listed price of the product"},
            "features": {"type": "array", "items": {"type": "string"}, "description": "List of key product features"}
          },
          "required": ["product_name", "price"]
        }
        ```
*   **`extractionPrompt`** (string, Optional, used with `'llm-extraction'`): A custom prompt to guide the LLM during extraction, especially useful if the schema alone isn't sufficient or if specific nuances need to be handled.
    *   *Example:* `"Extract the product details. Ensure the price is captured as a number, excluding currency symbols. List only the top 5 features."*
*   **`extractionModel`** (string, Optional, used with `'llm-extraction'`): Specify the underlying LLM to use (e.g., 'gpt-4', 'gpt-3.5-turbo'). Defaults may apply if omitted. Check Firecrawl documentation for supported models.

## Choosing the Right Mode

*   Use `'markdown'` for general content retrieval where structure is less critical or varies widely.
*   Use `'llm-extraction'` when you need specific data points extracted into a consistent JSON format from pages with relatively stable structures. Define a clear `schema`. Use `extractionPrompt` for fine-tuning.

*(Refer to the Firecrawl documentation for the most up-to-date details on extractor options and supported models: https://docs.firecrawl.dev/api-reference/scrape-url#extractoroptions)*