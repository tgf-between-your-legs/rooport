# Firecrawl API `curl` Examples

Use these examples as a basis for constructing `execute_command` calls to the Firecrawl API. Remember to handle the API key securely (e.g., via environment variable `$FIRECRAWL_API_KEY`).

## 1. Scrape a Single URL (Default Markdown Extraction)

```bash
# Command for execute_command tool:
curl -X POST https://api.firecrawl.dev/v0/scrape \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://example.com"
  }'
```
*   **Expected Result:** JSON response containing `{"success": true, "data": "..."}` where `data` is the scraped content in Markdown format.

## 2. Scrape a Single URL (LLM Extraction with Schema)

```bash
# Command for execute_command tool:
# NOTE: The JSON payload needs careful escaping for the command line.
# It might be safer to write the payload to a temporary file and use curl -d @payload.json
# Example assuming direct embedding (requires careful shell escaping):
curl -X POST https://api.firecrawl.dev/v0/scrape \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://example.com/product/123",
    "extractorOptions": {
      "mode": "llm-extraction",
      "schema": {
        "type": "object",
        "properties": {
          "product_name": {"type": "string"},
          "price": {"type": "number"},
          "description": {"type": "string"}
        },
        "required": ["product_name", "price"]
      }
    }
  }'
```
*   **Expected Result:** JSON response containing `{"success": true, "data": {"product_name": "...", "price": ..., "description": "..."}}`.

## 3. Start a Crawl Job (Basic)

```bash
# Command for execute_command tool:
curl -X POST https://api.firecrawl.dev/v0/crawl \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://blog.example.com",
    "crawlerOptions": {
      "includes": ["blog.example.com/posts/.*"],
      "excludes": ["blog.example.com/category/.*"],
      "maxDepth": 2,
      "maxPages": 10
    }
  }'
```
*   **Expected Result:** JSON response: `{ "success": true, "jobId": "some-job-id-string" }`. The specialist should report this `jobId` back.

## 4. Check Crawl Job Status

```bash
# Command for execute_command tool:
# Replace {jobId} with the actual ID received from the /crawl request.
curl -X GET https://api.firecrawl.dev/v0/crawl/{jobId} \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY"
```
*   **Expected Result:** JSON response containing `status` ('active', 'completed', 'failed'), `total`, `current`, and potentially `data` array if completed.

*(Remember to replace placeholders like URLs and adapt options based on specific requirements. Ensure `$FIRECRAWL_API_KEY` is available in the environment where the command is executed.)*