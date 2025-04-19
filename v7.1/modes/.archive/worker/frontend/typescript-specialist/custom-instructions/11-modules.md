# TypeScript: Modules (ES Modules)

Organizing TypeScript code into reusable modules using ES Module syntax (`import`/`export`).

## Core Concept

Modules allow you to break down your code into separate files. Each file is its own module with its own scope. You can explicitly choose which variables, functions, classes, types, or interfaces to make available to other modules using `export`, and bring code from other modules into the current scope using `import`.

TypeScript uses the standard ES Module syntax.

## Exporting

*   **Named Exports:** Export specific declarations by prefixing them with `export`. Multiple named exports are allowed per file.
    ```typescript
    // src/mathUtils.ts
    export const PI = 3.14159;

    export function add(a: number, b: number): number {
      return a + b;
    }

    export interface Point {
      x: number;
      y: number;
    }
    ```
*   **Default Exports:** Export a single "main" declaration from a module. Only one default export is allowed per file.
    ```typescript
    // src/MyClass.ts
    export default class MyClass {
      // ... class implementation ...
    }

    // src/utilityFunction.ts
    export default function utilityFunction() {
      // ... function implementation ...
    }
    ```
*   **Export Statements:** Export existing declarations separately. Can rename exports using `as`.
    ```typescript
    // src/constants.ts
    const MAX_USERS = 100;
    const API_ENDPOINT = "/api";

    export { MAX_USERS, API_ENDPOINT as endpoint }; // Renames API_ENDPOINT to endpoint on export
    ```
*   **Re-Exports:** Export declarations from another module.
    ```typescript
    // src/index.ts (barrel file)
    export { add } from './mathUtils'; // Re-export 'add'
    export * from './constants'; // Re-export everything from constants.ts
    export { default as MyClass } from './MyClass'; // Re-export default export as a named export
    ```
*   **Exporting Types (`export type`):** Use `export type` to explicitly export only type information. This ensures that build tools can safely remove the export if the type is only used in type annotations (doesn't affect runtime code).
    ```typescript
    // src/types.ts
    export type User = { id: number; name: string; };
    export interface Options { /* ... */ }

    // src/main.ts
    import type { User, Options } from './types'; // Import only types

    let user: User; // OK
    // let opts = new Options(); // Error if Options only has type info
    ```

## Importing

*   **Named Imports:** Import specific named exports using curly braces `{}`. Can rename imports using `as`.
    ```typescript
    // src/app.ts
    import { add, PI, type Point } from './mathUtils'; // Import named exports, 'Point' as type-only
    import { MAX_USERS, endpoint as apiEndpoint } from './constants'; // Import renamed export

    console.log(add(PI, 5));
    console.log(MAX_USERS, apiEndpoint);
    let p: Point = { x: 1, y: 1 };
    ```
*   **Default Imports:** Import the default export using any name directly after `import`.
    ```typescript
    // src/app.ts
    import MyCoolClass from './MyClass'; // Import default export
    import doSomething from './utilityFunction';

    const instance = new MyCoolClass();
    doSomething();
    ```
*   **Namespace Imports:** Import everything from a module into a single namespace object using `* as name`.
    ```typescript
    // src/app.ts
    import * as math from './mathUtils';
    import * as constants from './constants';

    console.log(math.add(math.PI, 1));
    console.log(constants.MAX_USERS);
    ```
*   **Side Effect Imports:** Import a module only for its side effects (e.g., polyfills, global setup). Rarely needed.
    ```typescript
    import './polyfills';
    ```
*   **Type-Only Imports (`import type`):** Import only type information. This guarantees the import is removed at compile time and has no runtime cost. Useful for separating type dependencies from value dependencies.
    ```typescript
    import type { User } from './types';

    function processUser(user: User) { /* ... */ }
    // const u = new User(); // Error: 'User' cannot be used as a value because it was imported using 'import type'.
    ```

## Module Resolution

*   TypeScript needs to know how to find modules specified in `import` statements. This is configured in `tsconfig.json` under `compilerOptions`:
    *   `moduleResolution`: Typically `"NodeNext"` or `"Node16"` for modern Node.js environments, or `"Bundler"` when using modern bundlers like Vite/Webpack. `"Classic"` is older and less common.
    *   `baseUrl`: Specifies the base directory for non-relative module imports.
    *   `paths`: Creates path aliases (e.g., `@/*` mapping to `src/*`). Requires build tool support (like `vite-tsconfig-paths` or `tsconfig-paths-webpack-plugin`) to work at runtime.

*(Refer to the official TypeScript documentation on Modules: https://www.typescriptlang.org/docs/handbook/modules.html)*