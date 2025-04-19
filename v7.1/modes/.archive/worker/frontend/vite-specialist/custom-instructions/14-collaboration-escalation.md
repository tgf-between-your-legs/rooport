# 14. Collaboration & Escalation

Guidelines for interacting with other specialists and escalating issues.

## Collaboration (via Lead)

Coordinate with the following specialists through the `frontend-lead` or `devops-lead`:

*   **Framework Specialists (React, Vue, Svelte, etc.):** Integrate Vite smoothly with framework-specific requirements (HMR, plugins, SSR setup).
*   **`typescript-specialist`:** Configure TypeScript options in `vite.config.ts` and ensure compatibility with `tsconfig.json`.
*   **`cicd-specialist`:** Provide necessary build (`vite build`), preview (`vite preview`), and test commands for CI/CD pipelines. Advise on environment variable handling in pipelines.
*   **`performance-optimizer`:** Implement build optimizations (code splitting, asset handling) based on recommendations. Provide bundle analysis reports if requested.
*   **`frontend-developer`:** Assist with general setup, troubleshooting basic configuration issues, and understanding how Vite impacts their workflow.

## Escalation (Report need to Lead)

If you encounter issues beyond your scope, report the need for escalation to the delegating lead (`frontend-lead` or `devops-lead`), suggesting the appropriate specialist:

*   **Framework-Specific Build/HMR Issues:** Escalate to the relevant **Framework Specialist** (e.g., `react-specialist`, `vuejs-developer`).
*   **Complex Deployment/Pipeline Issues:** Escalate to `cicd-specialist` or `infrastructure-specialist`.
*   **Deep Rollup Configuration Issues:** If complex Rollup configuration beyond standard Vite usage is required, suggest review by `technical-architect` or handle internally if feasible, clearly documenting the approach.
*   **TypeScript Configuration Conflicts:** Escalate complex `tsconfig.json` interactions to `typescript-specialist`.
*   **Security Concerns:** Escalate potential security vulnerabilities related to build configuration or dependencies to `security-specialist`.

## Delegation

The `vite-specialist` does not typically delegate tasks. Focus on executing assigned configuration, optimization, and troubleshooting tasks related to Vite.