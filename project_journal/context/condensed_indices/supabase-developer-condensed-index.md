## Supabase - Condensed Context Index

### Overall Purpose
Supabase is an open-source Firebase alternative offering a suite of backend tools built primarily on PostgreSQL. It provides developers with a managed Postgres database, Authentication, instant APIs, Edge Functions, Realtime subscriptions, Storage, and Vector embeddings (via pgvector) accessible through client libraries for various platforms and direct SQL interaction.

### Core Concepts & Capabilities
*   **Database (PostgreSQL):** Leverages PostgreSQL as its core. Supports standard SQL, database functions (`CREATE FUNCTION`), triggers (`CREATE TRIGGER`), and extensions (`CREATE EXTENSION`). Key extensions include `pgvector` for AI/vector operations and `pg_stat_statements` for query analysis. Common tables include `auth.users` and user-defined tables (e.g., `profiles`, `documents`).
*   **Authentication:** Provides robust user management (`auth.users`) and authentication flows. Supports email/password, OAuth providers (e.g., Spotify), Magic Links/OTP (`signInWithOtp`), and Multi-Factor Authentication (MFA). Managed via `supabase.auth` client methods and integrated with database security via RLS. Includes UI components like `@supabase/auth-ui-react`.
*   **Authorization (Row Level Security - RLS):** Relies heavily on PostgreSQL's RLS (`CREATE POLICY`, `ALTER TABLE ... ENABLE ROW LEVEL SECURITY`). Enables fine-grained data access control based on user identity (via `auth.uid()`) or JWT claims (via `auth.jwt() ->> 'claim'`). Policies define `USING` (read) and `WITH CHECK` (write) conditions.
*   **Client Libraries & SDKs:** Offers official libraries for JavaScript/TypeScript (`supabase-js`), Python (`supabase-py`), Dart (`supabase-dart`), Swift (`supabase-swift`), Kotlin (`supabase-kt`). Provide idiomatic interfaces for Database CRUD (`from().select()`, `.insert()`, `.update()`, `.delete()`), function calls (`.rpc()`), Auth, Realtime, and Storage. Framework-specific helpers (e.g., `@supabase/ssr`, `@supabase/auth-helpers-nextjs`) simplify integration.
*   **Vector Search (pgvector):** Integrates the `pgvector` PostgreSQL extension for AI applications. Supports storing `vector` data types, creating similarity search indexes (`USING ivfflat/hnsw` with `vector_l2_ops`, `vector_ip_ops`, `vector_cosine_ops`), and querying via SQL or client libraries.
*   **Realtime:** Broadcasts database changes (inserts, updates, deletes) and custom events over WebSockets. Clients subscribe to channels (`client.channel('topic').subscribe(...)`) to receive updates.
*   **Framework Integration:** Provides tools and guides for integration with frameworks like Next.js, React, SvelteKit, Vue, Angular etc., often including helpers for server-side rendering (SSR) and authentication management (e.g., middleware, cookie handling).
*   **CLI:** `supabase` CLI tool for local development (`init`, `start`, `db push`), managing migrations, and interacting with the Supabase platform.

### Key APIs / Components / Configuration / Patterns
*   `create extension vector with schema extensions;`: SQL command to enable pgvector.
*   `supabase.auth.signInWith...({ provider?, email?, password?, phone?, options? })`: JS client: Core methods for user login (OAuth, OTP, Password, Phone).
*   `supabase.auth.signUp({ email?, password?, phone?, options? })`: JS client: Method for user registration.
*   `supabase.auth.getSession()` / `supabase.auth.getUser()`: JS client: Retrieve current user session/details.
*   `supabase.auth.onAuthStateChange((event, session) => ...)`: JS client: Listener for authentication state changes (SIGNED_IN, SIGNED_OUT, etc.).
*   `create policy "name" on table for {SELECT|INSERT|UPDATE|DELETE} using ( (select auth.uid()) = user_id )`: Common RLS pattern for user-specific data access.
*   `auth.uid()`: SQL function: Returns the UUID of the currently authenticated user (essential for RLS).
*   `auth.jwt()`: SQL function: Returns the JWT claims of the current user (useful for role/MFA checks in RLS, e.g., `auth.jwt() ->> 'aal'`).
*   `supabase.from('table_name').select('columns')`: JS client: Basic data retrieval. Supports filtering, ordering, limiting.
*   `supabase.from('table_name').insert([{ col: val }, ...])`: JS client: Data insertion.
*   `supabase.rpc('function_name', { arg1: val })`: JS client: Call a PostgreSQL database function.
*   `supabase.channel('channel_name').on(...).subscribe(...)`: JS client: Subscribe to Realtime broadcasts/DB changes.
*   `createClient<Database>(url, key)`: JS/TS client: Initialize the Supabase client, optionally with generated TypeScript types for enhanced safety.
*   `createServerClient()` / `createMiddlewareClient()`: JS/TS client: Specialized helpers for server-side (e.g., Next.js API routes, middleware) authentication and session handling.
*   `.textSearch('column', 'query', { type?, config? })`: JS client: Perform full-text search using `to_tsvector` and `to_tsquery`.
*   `vector(dimensions)`: SQL data type for storing vector embeddings (from pgvector).
*   `create index ... using ivfflat (column vector_ip_ops) with (lists = N);`: SQL example for creating a vector index (inner product).
*   `supabase init`: CLI: Initialize Supabase configuration in a local project directory.
*   `.env.local` / `NEXT_PUBLIC_SUPABASE_URL`, `NEXT_PUBLIC_SUPABASE_ANON_KEY`: Common pattern for storing Supabase credentials as environment variables.
*   `create function handle_new_user() returns trigger ... create trigger ... after insert on auth.users ...`: Common SQL pattern to automatically create related data (e.g., a user profile) when a new user signs up.

### Common Patterns & Best Practices / Pitfalls
*   **RLS is Default Security:** Always enable RLS on tables containing sensitive data (`alter table ... enable row level security;`) and define appropriate `create policy` statements. Default is denial.
*   **Use `auth.uid()` for Ownership:** Base RLS policies on `auth.uid()` for user-specific data access.
*   **Leverage `auth.jwt()` for Claims:** Use `auth.jwt()` to access custom claims or standard claims like `aal` (Assurance Level for MFA) within policies.
*   **Server-Side Auth Handling:** Use framework-specific helpers (`createServerClient`, middleware) for correct session management in server environments (SSR, API routes).
*   **Indexing:** Create standard PostgreSQL indexes (`create index`) on columns frequently used in RLS policy `WHERE` clauses or query filters (e.g., `user_id`, foreign keys) to optimize performance. Create vector indexes (`using ivfflat/hnsw`) for similarity searches.
*   **Database Functions & Triggers:** Encapsulate business logic in SQL functions (`create function`) and automate actions using triggers (`create trigger`) for consistency and performance (e.g., creating profiles on signup).
*   **Typed Client (TypeScript):** Generate database types (`supabase gen types typescript`) and use `createClient<Database>(...)` for improved type safety and developer experience.
*   **Environment Variables:** Securely manage Supabase URL and API keys using environment variables. Distinguish between public (`NEXT_PUBLIC_...` or equivalent) and secret keys.
*   **Restrictive Policies:** Use `as restrictive` policies carefully, as they can override permissive policies and deny access unexpectedly, especially useful for enforcing conditions like MFA (`using ((select auth.jwt()->>'aal') = 'aal2')`).

---
This index summarizes the core concepts, APIs, and patterns for Supabase based on the provided snippets. Consult the full official Supabase documentation for exhaustive details.