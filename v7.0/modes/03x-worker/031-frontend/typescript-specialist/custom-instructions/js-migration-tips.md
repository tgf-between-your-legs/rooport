# TypeScript: Migrating from JavaScript

Strategies and tips for incrementally migrating an existing JavaScript codebase to TypeScript.

## Goal

The aim is usually not to rewrite everything at once, but to gradually introduce TypeScript's benefits (static typing, improved tooling, better maintainability) into a JavaScript project with minimal disruption.

## Strategy: Incremental Migration

1.  **Setup TypeScript:**
    *   Install TypeScript: `npm install --save-dev typescript`
    *   Install Node types: `npm install --save-dev @types/node`
    *   Install types for libraries used (e.g., React, Express): `npm install --save-dev @types/react @types/express` (Check DefinitelyTyped for available types).
    *   Create `tsconfig.json`: Run `npx tsc --init` or create manually.

2.  **Configure `tsconfig.json` for JS Interop:**
    *   `allowJs: true`: **Crucial.** Allows TypeScript compiler to process JavaScript files alongside TypeScript files.
    *   `checkJs: true` (Optional but Recommended): Enables TypeScript to report potential errors in `.js` files based on JSDoc annotations or inference. Start with `false` if it reports too many errors initially.
    *   `outDir`: Specify an output directory for compiled JavaScript (e.g., `"./dist"`).
    *   `rootDir`: Specify the root directory of your source files (e.g., `"./src"`).
    *   `esModuleInterop: true`: Recommended for better compatibility with CommonJS modules.
    *   `skipLibCheck: true`: Often useful to avoid type checking all `.d.ts` files from `node_modules`.
    *   Start with `strict: false` or disable specific strict checks initially to reduce initial errors. You can enable them gradually later.

3.  **Start with `@ts-check` (Optional):**
    *   Add `// @ts-check` to the top of individual `.js` files.
    *   TypeScript (and VS Code) will start type-checking these files based on inference and JSDoc comments.
    *   Fix reported errors by adding JSDoc type annotations. This improves type safety even before renaming files.
    ```javascript
    // @ts-check

    /**
     * Adds two numbers.
     * @param {number} a The first number.
     * @param {number} b The second number.
     * @returns {number} The sum.
     */
    function add(a, b) {
      return a + b;
    }
    ```

4.  **Rename Files Incrementally (`.js` -> `.ts` / `.jsx` -> `.tsx`):**
    *   Start with files that have fewer dependencies (e.g., utility functions, types/constants).
    *   Rename the file extension.
    *   Run `tsc --noEmit` (or rely on IDE feedback) to see type errors.
    *   Fix errors by adding explicit type annotations (parameters, return types, variables, properties). Replace JSDoc types with TypeScript syntax.
    *   Address issues related to `strictNullChecks` (if enabled) by checking for `null`/`undefined`.
    *   Fix `noImplicitAny` errors by providing types. Use `unknown` instead of `any` where possible if the type isn't immediately clear.

5.  **Gradually Increase Strictness:**
    *   Once a significant portion is migrated, start enabling stricter checks in `tsconfig.json` (e.g., `noImplicitAny`, `strictNullChecks`, eventually `strict: true`).
    *   Fix the new errors that appear.

6.  **Refactor and Improve Types:**
    *   As you migrate, look for opportunities to create reusable `interface`s and `type` aliases.
    *   Use generics for reusable functions/classes.
    *   Replace implicit `any` types with more specific types or `unknown`.

## Tips

*   **Bottom-Up or Top-Down:** You can start migrating leaf modules (no dependencies) and work up, or start with entry points and work down. Choose what feels less disruptive.
*   **Focus on Boundaries:** Pay close attention to the boundaries between migrated TS code and existing JS code. Ensure data crossing the boundary is handled safely (potentially using assertion functions or runtime validation).
*   **Use JSDoc:** Leverage JSDoc annotations in `.js` files (`@param`, `@returns`, `@type`, `@typedef`) to get some type checking benefits even before renaming files, especially if using `@ts-check`.
*   **`any` as Escape Hatch:** Use `any` sparingly as a temporary measure if you're stuck on a complex type error and need to move forward. Add a `// TODO: Fix this any` comment to revisit it later. Prefer `unknown` if possible.
*   **Build Tools:** Ensure your build process (Webpack, Vite, Rollup, etc.) is configured to handle both `.js` and `.ts` files correctly during the migration.
*   **Testing:** Ensure your tests still pass after migration. Consider adding tests that specifically cover type-related edge cases if necessary.

*(Refer to the official TypeScript Migration Guide: https://www.typescriptlang.org/docs/handbook/migrating-from-javascript.html)*