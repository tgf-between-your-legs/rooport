# TypeScript: `tsconfig.json` Key Options

Understanding important compiler options in the TypeScript configuration file.

## Core Concept

`tsconfig.json` in the root of a TypeScript project specifies the root files and the compiler options required to compile the project. Frameworks like Next.js, Vite, or Create React App often generate a base `tsconfig.json` with sensible defaults.

## Key Sections

*   **`compilerOptions`:** The most important section, containing flags to control how TypeScript checks and compiles your code.
*   **`include`:** An array of glob patterns specifying which files TypeScript should include in the compilation.
*   **`exclude`:** An array of glob patterns specifying files TypeScript should *exclude* from compilation (e.g., `node_modules`, build output folders).
*   **`extends`:** Allows inheriting configuration from another `tsconfig.json` file (e.g., base configurations provided by frameworks or shared configs in a monorepo).

## Important `compilerOptions`

*   **Type Checking (`strict` Mode Recommended):**
    *   `strict`: (boolean) Enables all strict type-checking options. **Highly recommended** for robust type safety. Setting `strict: true` enables all of the following (and more):
        *   `noImplicitAny`: (boolean) Raise error on expressions and declarations with an implied `any` type. Forces explicit type annotations.
        *   `strictNullChecks`: (boolean) When true, `null` and `undefined` have their own distinct types and you'll get errors where you might be using a value that could be `null` or `undefined`. You must explicitly check for them (type narrowing).
        *   `strictFunctionTypes`: (boolean) Enables stricter checking of function type parameters.
        *   `strictBindCallApply`: (boolean) Enables stricter checking on `bind`, `call`, and `apply` methods on functions.
        *   `strictPropertyInitialization`: (boolean) Ensure class properties are initialized in the constructor or have an explicit `undefined` type.
        *   `noImplicitThis`: (boolean) Raise error on `this` expressions with an implied `any` type.
        *   `alwaysStrict`: (boolean) Parse in strict mode and emit `"use strict"` for each source file.
    *   `noUnusedLocals`: (boolean) Report errors on unused local variables.
    *   `noUnusedParameters`: (boolean) Report errors on unused parameters.
    *   `noImplicitReturns`: (boolean) Report error when not all code paths in function return a value.
*   **Modules:**
    *   `module`: (string) Specifies the module code generation standard (e.g., `"NodeNext"`, `"Node16"`, `"ESNext"`, `"CommonJS"`). Should align with your runtime environment and bundler.
    *   `moduleResolution`: (string) How modules get resolved (e.g., `"NodeNext"`, `"Node16"`, `"Bundler"`, `"Classic"`). `"Bundler"` is often best for modern bundlers like Vite/Webpack.
    *   `baseUrl`: (string) Base directory to resolve non-relative module names.
    *   `paths`: (object) Specify path mappings relative to `baseUrl` (e.g., `"@/*": ["src/*"]`). Requires runtime support (e.g., via bundler plugins).
    *   `rootDir`: (string) Specifies the root directory of input files. Used with `outDir` to control output directory structure.
    *   `typeRoots`: (string[]) List of folders to include type definitions from.
    *   `types`: (string[]) List of type definition package names to include (e.g., `["node", "jest"]`). If specified, only these packages are included.
*   **Emit (Output):**
    *   `target`: (string) Specifies the ECMAScript target version for the output JavaScript (e.g., `"ES2016"`, `"ESNext"`). Choose based on your target runtime environment.
    *   `outDir`: (string) Redirect output structure to the specified directory.
    *   `sourceMap`: (boolean) Generate corresponding `.map` source map files for debugging.
    *   `declaration`: (boolean) Generate corresponding `.d.ts` declaration files (useful for libraries).
    *   `declarationMap`: (boolean) Generate source maps for declaration files.
    *   `removeComments`: (boolean) Remove comments from output JavaScript.
    *   `noEmit`: (boolean) Do not emit output files (JavaScript, source maps, declarations). Useful for type checking only (`tsc --noEmit`).
    *   `emitDeclarationOnly`: (boolean) Only emit `.d.ts` files.
*   **JavaScript Support:**
    *   `allowJs`: (boolean) Allow JavaScript files to be compiled.
    *   `checkJs`: (boolean) Report errors in `.js` files (often used with `allowJs`).
*   **JSX Support:**
    *   `jsx`: (string) Controls JSX emit (`"preserve"`, `"react-jsx"`, `"react-jsxdev"`, `"react-native"`, `"react"`). `"react-jsx"` is common for modern React without needing `import React`.
*   **Interop Constraints:**
    *   `esModuleInterop`: (boolean) Enables compatibility helpers for importing CommonJS modules like ES modules. **Recommended** for better interoperability.
    *   `forceConsistentCasingInFileNames`: (boolean) Disallow inconsistently-cased references to the same file.

## Example `tsconfig.json` (React/Vite Project)

```json
{
  "compilerOptions": {
    "target": "ESNext", // Target modern JS
    "useDefineForClassFields": true,
    "lib": ["DOM", "DOM.Iterable", "ESNext"], // Include DOM and modern JS APIs
    "allowJs": false, // Disallow JS files
    "skipLibCheck": true, // Skip type checking of declaration files
    "esModuleInterop": true, // Recommended for compatibility
    "allowSyntheticDefaultImports": true,
    "strict": true, // Enable all strict checks (recommended)
    "forceConsistentCasingInFileNames": true,
    "module": "ESNext", // Use modern ES Modules
    "moduleResolution": "Bundler", // Or "NodeNext" / "Node16"
    "resolveJsonModule": true, // Allow importing JSON files
    "isolatedModules": true, // Ensure files can be safely transpiled individually
    "noEmit": true, // Let Vite handle emit, tsc only for type checking
    "jsx": "react-jsx", // Use modern JSX transform
    "baseUrl": ".", // Base for path aliases
    "paths": {
      "@/*": ["src/*"] // Example path alias
    }
  },
  "include": ["src"], // Compile files in src
  "references": [{ "path": "./tsconfig.node.json" }] // Example for Vite config file itself
}
```

*(Refer to the official TypeScript `tsconfig.json` reference for all options: https://www.typescriptlang.org/tsconfig)*