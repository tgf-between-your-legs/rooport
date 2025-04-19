# Directus: File Storage & Asset Management

Configuring how Directus stores and serves uploaded files and digital assets.

## Core Concept: Abstracted File Storage

Directus provides a robust system for managing files and other digital assets, abstracting the underlying storage mechanism. This means you can configure Directus to store files on the local filesystem, or use cloud storage providers like AWS S3, Google Cloud Storage, Azure Blob Storage, etc., without changing how users interact with files in the Data Studio or how you query file information via the API.

**Key Components:**

*   **`directus_files` Collection:** A system collection that stores metadata about each uploaded file (filename, type, size, title, description, storage adapter used, etc.).
*   **Storage Adapters:** Modules responsible for interacting with the actual storage location (local disk, S3 bucket, etc.). Directus includes built-in adapters and supports custom ones.
*   **Asset Transformation:** Directus can generate thumbnails and perform image transformations (resizing, format conversion, quality adjustments) on the fly via API query parameters.

## Configuration (Environment Variables)

Storage adapter settings are configured via environment variables in your `.env` file.

**1. Local Storage (Default):**

*   Stores files on the same server where Directus is running.
*   Simple setup but not ideal for scaled or stateless deployments.
*   **Variables:**
    ```dotenv
    # .env
    STORAGE_LOCATIONS="local" # Comma-separated list if using multiple, default is 'local'

    STORAGE_LOCAL_DRIVER="local"
    STORAGE_LOCAL_ROOT="./uploads" # Path relative to Directus root directory
    # Optional: Set public URL for direct file access if needed (ensure web server serves this path)
    # PUBLIC_URL="http://localhost:8055" # Base URL of your Directus instance
    # ASSETS_URL_NAMING="uuid" # How asset URLs are generated ('uuid' or 'filename', default 'uuid')
    ```

**2. AWS S3 Storage:**

*   Stores files in an AWS S3 bucket. Scalable and durable.
*   Requires AWS credentials and bucket configuration.
*   **Variables:**
    ```dotenv
    # .env
    STORAGE_LOCATIONS="s3" # Or "local,s3" if using both

    STORAGE_S3_DRIVER="s3"
    STORAGE_S3_KEY="YOUR_AWS_ACCESS_KEY_ID"
    STORAGE_S3_SECRET="YOUR_AWS_SECRET_ACCESS_KEY"
    STORAGE_S3_REGION="us-east-1" # Your bucket region
    STORAGE_S3_BUCKET="your-directus-bucket-name"
    # Optional: Endpoint URL for S3-compatible services (MinIO, DigitalOcean Spaces)
    # STORAGE_S3_ENDPOINT="https://your-s3-compatible-endpoint.com"
    # Optional: Set ACL for uploaded files (e.g., 'public-read')
    # STORAGE_S3_ACL="private"
    # Optional: Custom base URL for serving files (e.g., via CloudFront CDN)
    # STORAGE_S3_PUBLIC_URL="https://cdn.example.com"
    # Optional: Force path style access (needed for some S3-compatible services)
    # STORAGE_S3_FORCE_PATH_STYLE="true"
    ```

**3. Other Adapters (Google Cloud Storage, Azure Blob, etc.):**

*   Similar environment variable patterns exist (`STORAGE_GCS_*`, `STORAGE_AZURE_*`).
*   Consult the official Directus documentation for the specific variables required for each adapter.

## Accessing Files via API

*   **Metadata:** File metadata is stored in the `directus_files` collection and can be queried like any other collection via REST (`/files`) or GraphQL (`files`).
*   **Serving Files:**
    *   Directus provides an `/assets` endpoint to serve files and perform transformations.
    *   `GET /assets/{file-id}`: Serves the original file.
    *   `GET /assets/{file-id}?key=thumbnail`: Serves a pre-configured thumbnail (defined in Directus settings).
    *   `GET /assets/{file-id}?width=300&height=200&fit=cover&format=webp`: Performs on-the-fly transformations (resizing, cropping, format conversion).
*   **Direct URLs:** If the storage adapter is configured with a public URL (e.g., `STORAGE_S3_PUBLIC_URL` or using the default `PUBLIC_URL` with local storage served correctly), the `directus_files` items might contain a direct URL field you can use. However, using the `/assets` endpoint allows for permission checks and transformations.

## Key Considerations

*   **Permissions:** Access to files (metadata via `/files` and assets via `/assets`) is controlled by permissions set on the `directus_files` collection for different roles. You can restrict who can view, upload, or modify files.
*   **Transformations:** Configure image transformation presets (keys like `thumbnail`) in Directus settings for commonly used sizes. On-the-fly transformations can consume server resources, especially for large images or high traffic; consider caching transformed assets (Directus might do this internally or you might use a CDN).
*   **Security:** For cloud storage (S3, GCS, Azure), configure bucket policies and credentials securely. Limit public access unless necessary. Use signed URLs for temporary access to private files if needed (Directus might support this depending on version/adapter).
*   **Migration:** If changing storage adapters, you'll need to migrate existing files from the old location to the new one. Directus doesn't automatically do this.

Choose the storage adapter that best suits your project's scalability, cost, and infrastructure requirements. Configure permissions carefully and leverage the `/assets` endpoint for serving files and performing transformations.

*(Refer to the official Directus documentation on File Storage and Assets.)*