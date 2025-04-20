# OpenAPI Specification (Swagger) Basics

Understanding the structure and purpose of the OpenAPI Specification for describing REST APIs.

## Core Concept: API Contract Definition

The **OpenAPI Specification (OAS)**, formerly known as Swagger Specification, defines a standard, language-agnostic interface description for RESTful APIs. It allows both humans and computers to discover and understand the capabilities of a service without requiring access to source code, documentation, or network traffic inspection.

**Key Benefits:**

*   **Contract:** Defines a clear contract between the API provider and consumers.
*   **Documentation:** Can be used to automatically generate interactive API documentation (e.g., using Swagger UI, Redoc).
*   **Code Generation:** Tools can generate client SDKs and server stubs in various languages from an OpenAPI spec.
*   **Testing:** Can be used to generate API tests or validate requests/responses during testing.
*   **Discoverability:** Provides a machine-readable description of the API's capabilities.

**Formats:** OpenAPI definitions can be written in **YAML** or **JSON**. YAML is often preferred for its readability.

**Swagger vs. OpenAPI:** "Swagger" originally referred to the specification and a set of tools. The specification was donated to the Linux Foundation and renamed the OpenAPI Specification. "Swagger" now generally refers to the tooling ecosystem around OAS (like Swagger UI, Swagger Editor, Swagger Codegen).

## Basic Structure (OpenAPI 3.x)

An OpenAPI document is typically a single YAML or JSON file with the following top-level sections:

```yaml
# openapi.yaml
openapi: 3.0.3 # Version of the OpenAPI Specification used

info: # Metadata about the API
  title: My Awesome Pet Store API
  description: API for managing pets in our store.
  version: 1.0.0 # API version (distinct from OAS version)
  contact:
    email: api-support@example.com
  license:
    name: Apache 2.0
    url: http://www.apache.org/licenses/LICENSE-2.0.html

servers: # List of base URLs where the API is hosted
  - url: https://api.example.com/v1
    description: Production server
  - url: http://localhost:3000/v1
    description: Development server

tags: # Optional grouping for operations in documentation tools
  - name: pets
    description: Operations about pets
  - name: users
    description: User management

paths: # REQUIRED. Defines the available API endpoints (paths) and operations (HTTP methods)
  /pets: # Path Item Object
    summary: Operations related to the collection of pets. # Optional summary for the path
    get: # Operation Object (HTTP GET method)
      tags: [pets] # Assign tags for grouping
      summary: List all pets
      description: Returns a list of all pets, optionally filtered.
      operationId: listPets # Unique ID for the operation (useful for code generation)
      parameters: # List of parameters for this operation
        - name: limit
          in: query # Parameter location (query, path, header, cookie)
          description: Maximum number of pets to return
          required: false
          schema:
            type: integer
            format: int32
            minimum: 1
            maximum: 100
            default: 20
      responses: # REQUIRED. Possible responses for this operation
        '200': # HTTP status code
          description: A list of pets.
          content: # Describes the response body format(s)
            application/json: # Media type
              schema: # Defines the structure of the response body
                type: array
                items:
                  $ref: '#/components/schemas/Pet' # Reference to a reusable schema
        '400':
          description: Invalid input parameters
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'

    post: # Operation Object (HTTP POST method)
      tags: [pets]
      summary: Create a pet
      operationId: createPet
      requestBody: # Describes the request body
        description: Pet object to add to the store
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/NewPet' # Reference to request body schema
      responses:
        '201':
          description: Pet created successfully
          headers:
            Location: # Example: Describe response headers
              description: URL of the newly created pet
              schema:
                type: string
                format: uri
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Pet'
        '400':
          description: Invalid input
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'

  /pets/{petId}: # Path with a parameter
    parameters: # Parameters applicable to all operations under this path
      - name: petId
        in: path # Path parameter
        required: true
        description: ID of the pet to operate on
        schema:
          type: string # Or integer, depending on ID format
    get:
      tags: [pets]
      summary: Info for a specific pet
      operationId: getPetById
      responses:
        '200':
          description: Information about the pet
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Pet'
        '404':
          description: Pet not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
    # ... other methods like PUT, DELETE for /pets/{petId}

components: # Reusable definitions
  schemas: # Reusable data models (request/response bodies)
    Pet:
      type: object
      required:
        - id
        - name
      properties:
        id:
          type: string
          format: uuid
          readOnly: true # Indicates property is not expected in requests (e.g., POST)
        name:
          type: string
          example: Fido
        tag:
          type: string
        createdAt:
          type: string
          format: date-time
          readOnly: true
    NewPet:
      type: object
      required:
        - name
      properties:
        name:
          type: string
          example: Buddy
        tag:
          type: string
    Error:
      type: object
      required:
        - code
        - message
      properties:
        code:
          type: integer
          format: int32
        message:
          type: string

  securitySchemes: # Reusable security definitions (e.g., API Key, JWT, OAuth2)
    ApiKeyAuth:
      type: apiKey
      in: header
      name: X-API-KEY

security: # Global security requirements (can be overridden per operation)
  - ApiKeyAuth: [] # Requires ApiKeyAuth (defined in components.securitySchemes)

```

**Key Sections Explained:**

*   **`openapi`**: Version of the OAS.
*   **`info`**: General API metadata.
*   **`servers`**: Base URLs for accessing the API.
*   **`tags`**: Used to group operations in documentation tools.
*   **`paths`**: Defines API endpoints and the HTTP operations (`get`, `post`, `put`, `delete`, etc.) available on them.
    *   **`parameters`**: Describes parameters accepted by an operation (in query, path, header, or cookie).
    *   **`requestBody`**: Describes the payload sent in the request body (e.g., for `POST`, `PUT`).
    *   **`responses`**: Describes possible HTTP status codes and the structure (`content`, `schema`) of the response body for each.
*   **`components`**: Contains reusable definitions.
    *   **`schemas`**: Defines reusable data structures (objects) used in request/response bodies or parameters. Uses JSON Schema subset. `$ref` is used to link to these definitions.
    *   **`securitySchemes`**: Defines authentication/authorization methods (API Key, JWT Bearer, OAuth2, etc.).
*   **`security`**: Specifies which security schemes apply globally or per operation.

Writing and maintaining an accurate OpenAPI specification is crucial for modern API development, enabling better documentation, tooling, testing, and client integration.

*(Refer to the official OpenAPI Specification documentation: https://swagger.io/specification/)*