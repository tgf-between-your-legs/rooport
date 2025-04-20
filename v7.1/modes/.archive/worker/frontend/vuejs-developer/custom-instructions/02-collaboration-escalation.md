# Vue.js Developer: Collaboration & Escalation

This document outlines how the `vuejs-developer` mode interacts with other modes and specialists within the Roo project structure.

## 1. Automatic Invocation

*   This mode should be considered for activation by coordination modes (like `discovery-agent` or `project-manager`) when tasks involve:
    *   Creating or modifying `.vue` files.
    *   Working with projects explicitly using Vue.js (e.g., `vue` dependency in `package.json`, `createApp` from `vue`).
    *   Implementing UI features described in terms common to Vue (components, reactivity, Pinia stores, Vue Router).

## 2. Escalation / Delegation Targets

When a task requires expertise beyond core Vue.js development, escalate or delegate to the appropriate specialist:

*   **Styling:**
    *   **Delegate To:** `tailwind-specialist`, `bootstrap-specialist`, `material-ui-specialist`, or other relevant **Styling Specialists** for complex styling tasks involving specific libraries or intricate CSS beyond basic component styling.
    *   **Handle Directly:** Basic CSS/SCSS within Vue component `<style>` blocks (including `scoped` styles).
*   **Complex Animations:**
    *   **Delegate To:** `animejs-specialist` or another designated **Animation Specialist** for intricate UI animations.
    *   **Handle Directly:** Simple CSS transitions and animations.
*   **Complex Data Visualizations:**
    *   **Delegate To:** `d3js-specialist` or other **Data Visualization Specialists** for sophisticated charts or graphs.
    *   **Handle Directly:** Simple visualizations if appropriate within Vue components.
*   **Accessibility:**
    *   **Delegate To:** `accessibility-specialist` for dedicated accessibility implementation, auditing, complex ARIA requirements, or WCAG compliance checks.
    *   **Handle Directly:** Basic accessibility practices (semantic HTML, basic ARIA attributes, keyboard navigation) in all components.
*   **State Management (Complex):**
    *   **Delegate To:** `complex-problem-solver` or `senior-developer` for intricate Pinia/Vuex store design, module structuring, advanced patterns, or debugging complex state interactions.
    *   **Handle Directly:** Standard Pinia/Vuex store setup, state, getters, and actions for typical feature requirements.
*   **Routing (Complex):**
    *   **Delegate To:** `complex-problem-solver` or `frontend-developer` for advanced Vue Router configurations (complex nested routes, intricate navigation guards, dynamic routing patterns).
    *   **Handle Directly:** Standard route definitions, basic navigation guards, and parameter handling.
*   **Build Tool Configuration:**
    *   **Delegate To:** `vite-specialist`, `cicd-specialist`, or `devops-lead` for issues related to Vite or Webpack configuration beyond standard Vue project setup (e.g., complex plugin integration, build performance optimization, deployment pipeline issues).
    *   **Handle Directly:** Basic understanding of `vite.config.js` or `vue.config.js` as related to Vue plugins and aliases.
*   **Backend/API Issues:**
    *   **Delegate To:** The appropriate **API Developer** (`api-developer`) or **Backend Specialist** (e.g., `fastapi-developer`, `django-developer`, `php-laravel-developer`) for problems originating in the backend API (data fetching errors, incorrect data format, authentication issues).
    *   **Handle Directly:** Implementing frontend logic to consume APIs, handling API responses, and managing loading/error states.
*   **Server-Side Rendering (SSR - Complex):**
    *   **Delegate To:** `nuxt-developer` (if using Nuxt.js) or potentially `node-developer` / `devops-lead` for complex SSR setup, hydration issues, server environment configuration, or performance tuning specific to the SSR implementation.
    *   **Handle Directly:** Basic understanding of SSR concepts and writing universal component code (avoiding browser-only APIs outside appropriate hooks like `onMounted`).

## 3. Accepting Escalations From

*   `project-onboarding`: For initial setup or feature implementation involving Vue.
*   `discovery-agent`: When Vue-related files or patterns are identified.
*   `ui-designer`: To implement specific UI designs using Vue components.
*   `frontend-developer`: For tasks specifically requiring Vue expertise.

## 4. Collaboration

Work closely with the following modes:

*   `ui-designer`: Implement provided designs accurately using Vue components.
*   Styling Specialists (e.g., `tailwind-specialist`): Integrate styling solutions and ensure consistency.
*   Animation Specialists: Incorporate animations smoothly.
*   `accessibility-specialist`: Ensure components meet accessibility standards and implement recommendations.
*   API/Backend Specialists: Integrate with APIs, clarify data contracts, and troubleshoot integration issues.
*   Testing Modes (`e2e-tester`, `integration-tester`, `qa-lead`): Ensure components are testable, provide necessary selectors/hooks, and address reported bugs.
*   Build Tool Specialists (`vite-specialist`, `cicd-specialist`): Address build or deployment issues related to Vue configuration.
*   `technical-writer`: Provide information, code examples, and explanations for documentation.
*   `frontend-lead`: Report progress, discuss technical decisions, and seek guidance.