# Directus: Core Concepts

Understanding the fundamental building blocks of Directus as a Headless CMS and Data Platform.

## 1. Headless CMS & Data Platform

*   **Headless CMS:** Directus separates the content management backend (where you define data structures and manage content) from the presentation layer (frontend website/app). It provides APIs (REST, GraphQL) for your frontend to fetch and display content, giving you complete control over the presentation.
*   **Data Platform:** Beyond typical CMS features, Directus acts as a flexible backend-as-a-service (BaaS). It can manage *any* structured data, not just traditional web content, making it suitable for various application backends. It provides tools for data modeling, access control, and API generation on top of your database.

## 2. Database Introspection & Abstraction

*   **SQL Database:** Directus sits on top of a standard SQL database (PostgreSQL, MySQL, SQLite, MS SQL Server, etc.).
*   **Introspection:** It can connect to an *existing* SQL database and automatically understand its tables and columns, creating corresponding collections and fields within Directus.
*   **Abstraction:** It can also manage the database schema *for* you. When you create collections and fields within the Directus Data Studio (UI), Directus creates the underlying SQL tables and columns.
*   **No Vendor Lock-in:** Because it uses standard SQL databases, you always have direct access to your data and are not locked into a proprietary format.

## 3. Collections & Fields (Data Modeling)

*   **Collections:** Represent tables in your SQL database. They define the structure for a specific type of data (e.g., `articles`, `products`, `users`, `events`).
    *   Directus includes system collections (prefixed with `directus_`) for managing users, roles, permissions, files, settings, etc.
    *   You define custom collections for your project's specific data needs.
*   **Fields:** Represent columns within a collection's table. Each field has a specific **Data Type** (e.g., String, Number, Boolean, DateTime, JSON) and an **Interface** (how the field is displayed and interacted with in the Data Studio UI).
    *   **Data Types:** Define how data is stored in the database (e.g., `VARCHAR`, `INT`, `BOOLEAN`, `TIMESTAMP`).
    *   **Interfaces:** Provide rich UI controls for content editors (e.g., WYSIWYG editor for a Text field, Color picker, Map interface, Relational dropdowns). Directus offers many built-in interfaces, and custom ones can be developed.

## 4. Relationships

Directus allows you to define relationships between collections, mirroring SQL foreign key concepts:

*   **Many-to-One (M2O):** A field in one collection links to a single item in another collection (e.g., an `article` has one `author` from the `users` collection). Creates a foreign key column.
*   **One-to-Many (O2M):** The inverse of M2O, displayed as a relational list on the "one" side (e.g., a `user` has many `articles`). Managed via the corresponding M2O field.
*   **Many-to-Many (M2M):** Links items in two collections through an intermediary "junction" collection (e.g., `articles` can have many `tags`, and `tags` can be applied to many `articles`). Directus manages the junction table automatically.
*   **One-to-One (O2O):** A field in one collection links to a single unique item in another collection. Often implemented using a unique foreign key.

## 5. APIs (REST & GraphQL)

*   Directus automatically generates secure and powerful **REST** and **GraphQL** APIs based on your data model (collections, fields, relationships) and configured permissions.
*   These APIs allow your frontend applications or other services to perform CRUD (Create, Read, Update, Delete) operations on your data.
*   APIs support filtering, sorting, pagination, aggregation, and deep relational querying.

## 6. Authentication & Permissions

*   **Authentication:** Manages user login. Supports local email/password authentication and various SSO providers (OAuth 2.0, OpenID Connect, LDAP).
*   **Permissions (RBAC):** Robust Role-Based Access Control system. Define roles (e.g., `Admin`, `Editor`, `Public`) and configure granular permissions for each role, controlling CRUD access to specific collections and fields, including custom validation rules and presets.

## 7. Files & Assets

*   Built-in digital asset management.
*   Supports various storage adapters (local filesystem, S3, Google Cloud Storage, Azure Blob Storage, etc.).
*   Automatic thumbnail generation and configurable image transformations via API parameters.

## 8. Extensibility

*   Directus is highly extensible via custom code:
    *   **Hooks:** Run custom logic before/after API events (e.g., validating data before saving, sending notifications after creation).
    *   **Endpoints:** Add custom REST API routes to implement specific business logic.
    *   **Interfaces:** Create custom UI controls for fields in the Data Studio.
    *   **Displays:** Customize how field data is shown in list views.
    *   **Layouts:** Create custom page layouts within the Data Studio.
    *   **Modules:** Add entirely new sections/pages to the Data Studio.
    *   Extensions are typically built using Node.js/TypeScript.

Directus provides a comprehensive backend by combining database abstraction, a user-friendly content management interface (Data Studio), automatically generated APIs, and a powerful extension system.