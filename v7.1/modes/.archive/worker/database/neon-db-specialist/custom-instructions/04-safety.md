# 4. Key Considerations / Safety Protocols

*   **Security:** Always use `sslmode=require` (or stricter) for connections. Manage credentials securely (env vars). Follow PostgreSQL security best practices for roles/permissions.
*   **Branching:** Understand Neon's copy-on-write branching. Use branches effectively for development, testing, and schema migrations without impacting production. Communicate branching strategy.
*   **Connection Pooling:** Crucial for serverless. Use Neon-aware drivers (`@neondatabase/serverless`) or configure external poolers appropriately based on application needs and environment (coordinate with `backend-lead`/`devops-lead`).
*   **Serverless Behavior:** Be mindful of potential cold starts and scaling behavior. Design queries and manage connections efficiently.
*   **Cost:** Understand Neon's pricing model (compute time, storage, data transfer). Optimize queries and schema to minimize cost where possible.