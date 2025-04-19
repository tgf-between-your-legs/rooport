# TypeScript: Migrating from JavaScript

Strategies and steps for gradually introducing TypeScript into an existing JavaScript codebase.

## Core Concept: Gradual Adoption

Migrating a large JavaScript project to TypeScript doesn't have to be an all-or-nothing process. TypeScript is designed for gradual adoption, allowing you to introduce type checking incrementally.

**Benefits of Migration:**

*   Catch errors earlier in the development cycle.
*   Improve code maintainability and refactoring confidence.
*   Enhance developer experience with better autocompletion and code navigation.
*   Provide clearer contracts for functions and components.

## Migration Strategies

1.  **Start Small:** Begin migrating a small, relatively isolated part of the codebase first (e.g., utility functions, specific components).
2.  **Bottom-Up:** Start with files that have fewer dependencies, then work your way up to files that depend on them.
3.  **Top-Down:** Start with higher-level files and add types, potentially using `any` or `unknown` initially for complex dependencies, then refine types downwards.
4.  **Enable `@ts-check`:** Add `// @ts-check` to the top of JavaScript files. This enables TypeScript checking in JS files within supported editors (like VS Code) without full compilation, helping identify potential issues early.
5.  **Incremental Strictness:** Start with less strict `tsconfig.json` settings (e.g., `strict: false` or specific strict flags disabled) and gradually enable stricter checks (`noImplicitAny`, `strictNullChecks`, etc.) as you fix type errors.

## Migration Steps (Typical Flow)

1.  **Add TypeScript Dependency:**
    ```bash
    npm install --save-dev typescript @types/node @types/react @types/react-dom # Add framework/node types
    # or
    yarn add --dev typescript @types/node @types/react @types/react-dom
    ```
    *   Install `@types/*` packages for any third-party libraries you use that don't bundle their own types.

2.  **Create `tsconfig.json`:**
    *   Run `npx tsc --init` to generate a basic `tsconfig.json`.
    *   **Key Initial Settings:**
        *   `"allowJs": true`: **Crucial.** Allows TypeScript to compile JavaScript files alongside TypeScript files.
        *   `"checkJs": false`: (Recommended initially) Don't type-check JS files by default during compilation (use `@ts-check` selectively).
        *   `"jsx": "react-jsx"` (or appropriate setting for your framework).
        *   `"module": "ESNext"`, `"moduleResolution": "NodeNext"` (or appropriate module system). See `11-modules.md` and `12-tsconfig-options.md`.
        *   `"target": "ES2016"` (or later).
        *   `"outDir"`: Specify an output directory for compiled JS (e.g., `"./dist"`).
        *   `"rootDir"`: Specify the root directory of your source files (e.g., `"./src"`).
        *   `"include"` / `"exclude"`: Define which files to process.
        *   Start with `"strict": false` or specific strict flags disabled initially.

3.  **Integrate with Build Process:**
    *   Update your build scripts (`package.json`) to use `tsc` or integrate TypeScript compilation into your existing bundler (Vite, Webpack, Rollup, Parcel usually handle `.ts`/`.tsx` files automatically if TypeScript is installed). Often, setting `"noEmit": true` in `tsconfig.json` is preferred, letting the bundler handle JavaScript generation while `tsc` is used only for type checking.

4.  **Rename Files (`.js` -> `.ts`, `.jsx` -> `.tsx`):**
    *   Start renaming files one by one or folder by folder.
    *   As you rename, TypeScript will likely show many initial errors (implicit `any`, potential `null`/`undefined` issues if `strictNullChecks` is enabled later).

5.  **Fix Type Errors & Add Annotations:**
    *   **Implicit `any`:** Add explicit types to function parameters, variables, etc., where TypeScript cannot infer them. Use `unknown` if the type is truly unknown and add type guards. Avoid `any` if possible.
    *   **Property '...' does not exist:** Define `interface` or `type` aliases for object shapes. See `03-interfaces-vs-types.md`.
    *   **Null/Undefined Errors (if `strictNullChecks` enabled):** Use optional chaining (`?.`), nullish coalescing (`??`), non-null assertions (`!`, use sparingly), or explicit checks (`if (value != null)`). See `08-type-narrowing-guards.md`.
    *   **Third-Party Libraries:** Ensure you have `@types/*` packages installed for libraries without built-in types. If types are missing or incorrect, you might need to create custom declaration files (`.d.ts`).

6.  **Gradually Increase Strictness:**
    *   Once a significant portion is migrated and basic errors are fixed, consider enabling stricter options in `tsconfig.json` one by one (e.g., `"noImplicitAny": true`, then `"strictNullChecks": true`) and fixing the resulting errors. Aim for `"strict": true`. See `12-tsconfig-options.md`.

7.  **Refine Types:** Replace initial `any` or overly broad types with more specific interfaces, generics, and utility types as you gain a better understanding of the data structures. See `07-generics.md` and `09-utility-types.md`.

Migrating requires patience. Start small, leverage `allowJs`, fix errors incrementally, and gradually increase strictness. The benefits of improved type safety and developer experience are often worth the effort.

*(Refer to the official TypeScript Migration Guide.)*