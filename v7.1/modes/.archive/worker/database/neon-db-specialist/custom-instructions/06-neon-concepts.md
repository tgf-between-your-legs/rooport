# 6. Neon Concepts & Knowledge Base

*   **Official Documentation:**
    *   Neon: https://neon.tech/docs
    *   PostgreSQL: https://www.postgresql.org/docs/
    *   Neon API: https://api-docs.neon.tech/reference/getting-started-with-neon-api
    *   Neon CLI (`neonctl`): https://github.com/neondatabase/neonctl
*   **Key Concepts:**
    *   Serverless PostgreSQL platform.
    *   Branching (copy-on-write).
    *   Connection Pooling (esp. `@neondatabase/serverless`).
    *   Standard PostgreSQL compatibility (SQL, PL/pgSQL, extensions like `pgvector`, `pgcrypto`).
    *   Neon API for management.
    *   `sslmode=require` is mandatory for connections.
    *   Framework integration (Django, LlamaIndex, etc.).
    *   `neonctl` CLI tool.
*   **Extensions:** Be familiar with common PostgreSQL extensions, especially `pgvector` for vector database capabilities.
*   **Language Reference:** SQL and PL/pgSQL.
*   **Serverless Concepts:** Understand implications of serverless architecture, connection pooling strategies.