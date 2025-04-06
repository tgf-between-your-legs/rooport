## TypeScript (Version Unknown) - Condensed Context Index

### Overall Purpose
TypeScript is a strongly typed programming language that builds on JavaScript, giving you better tooling at any scale. It adds optional static types to JavaScript, enabling compile-time error checking, improved code maintainability, and enhanced developer productivity via features like autocompletion and refactoring.

### Core Concepts & Capabilities

*   **Static Typing:** Define types for variables, parameters, and return values (`string`, `number`, `boolean`, `Date`, `Array<T>`, `T[]`, object literals `{ key: Type }`, `any`, `unknown`, `void`, `never`). Catches type errors during compilation.
*   **Type Inference:** TypeScript automatically infers types when not explicitly annotated (e.g., `let x = 3;` infers `number`).
*   **Interfaces:** Define contracts for object shapes using `interface Name { prop: Type; }`. Supports optional (`?`), readonly (`readonly`) properties, and merging declarations. Enables structural typing (compatibility based on shape).
*   **Classes:** Implement object-oriented patterns with `class Name { ... }`. Includes `constructor`, properties, methods, inheritance (`extends`, `super`), access modifiers (`public`, `private`, `protected`), and accessors (`get`/`set`). Can merge with `namespace`.
*   **Functions:** Define named or anonymous functions. Supports type annotations for parameters and return values (`function fn(arg: Type): ReturnType`), full function types (`(arg: Type) => ReturnType`), and `void` return type for callbacks whose result is ignored.
*   **Generics:** Create reusable code components (functions, classes, interfaces) that work with multiple types using type parameters (`<Type>`). Supports constraints (`<T extends Constraint>`), default types (`<T = Default>`), and type argument inference.
*   **Union Types:** Allow a variable to hold values of multiple types (`TypeA | TypeB`). Requires type narrowing for safe access to specific members.
*   **Intersection Types:** Combine multiple types into one (`TypeA & TypeB`). Useful for mixins or combining interfaces.
*   **Type Narrowing & Guards:** Refine types within conditional blocks using `typeof`, `instanceof`, the `in` operator, and custom type predicates (`arg is Type`). Ensures type safety when working with unions or `unknown`.
*   **Advanced Types:** Includes Tuples (`[TypeA, TypeB]`), Conditional Types (`T extends U ? X : Y`), Mapped Types (`{ [P in keyof T]: ... }`), Template Literal Types (`` `prefix-${Type}` ``).
*   **Utility Types:** Built-in types for common transformations: `Partial<T>`, `Readonly<T>`, `ReadonlyArray<T>`, `Pick<T, K>`, `Omit<T, K>`, `Awaited<T>`, `Record<K, T>`, etc.
*   **Modules:** Organize code using ES Modules syntax (`import`, `export`). Can export types (`export type`, `export interface`).
*   **Tooling:** `tsc` (TypeScript Compiler CLI) for compiling `.ts` files to `.js`. Configuration via `tsconfig.json` (e.g., `"strict": true`).

### Key APIs / Components / Configuration / Patterns

*   **Type Annotation:** `: Type` (e.g., `let name: string;`, `function greet(name: string): void`)
*   **Interface Declaration:** `interface Point { x: number; y: number; }`
*   **Class Declaration:** `class Greeter { constructor(message: string) {} greet() {} }`
*   **Generic Function:** `function identity<T>(arg: T): T { return arg; }`
*   **Generic Class/Interface:** `class Box<T> { contents: T; }`, `interface Collection<T> { add(item: T): void; }`
*   **Generic Constraint:** `function logLength<T extends { length: number }>(obj: T) { ... }`
*   **Union Type:** `type StringOrNumber = string | number;`
*   **Intersection Type:** `type Combined = TypeA & TypeB;`
*   **Type Alias:** `type ID = string | number;`
*   **Tuple Type:** `type Pair = [string, number];`
*   **Mapped Type (Example: Readonly):** `type Readonly<T> = { readonly [P in keyof T]: T[P]; };`
*   **Conditional Type:** `type IsString<T> = T extends string ? true : false;`
*   **Template Literal Type:** `` type EventName = `on${Capitalize<string>}` ``
*   **Type Guard (`typeof`):** `if (typeof value === "string") { ... }`
*   **Type Guard (`in`):** `if ("property" in object) { ... }`
*   **Type Predicate:** `function isFish(pet: Fish | Bird): pet is Fish { return ... }`
*   **Access Modifiers:** `public`, `private`, `protected` (used on class members)
*   **`readonly` Modifier:** `readonly prop: Type;`, `ReadonlyArray<T>`
*   **Optional Property/Parameter:** `prop?: Type`, `param?: Type`
*   **`tsc` CLI:** `tsc`, `tsc index.ts`, `tsc --project tsconfig.json`
*   **`tsconfig.json` (Strict Mode):** `{ "compilerOptions": { "strict": true } }`
*   **`never` Type:** Used for exhaustiveness checking in `switch` or conditional types.
*   **`Awaited<T>`:** Unwraps `Promise<T>` to `T`.
*   **`Omit<T, K>`:** Creates a type by removing keys `K` from type `T`.

### Common Patterns & Best Practices / Pitfalls

*   **Enable Strict Mode:** Use `"strict": true` in `tsconfig.json` for robust type checking.
*   **Prefer `unknown` over `any`:** Use `unknown` when type is uncertain; it forces type checking before use, unlike `any`.
*   **Use Type Guards:** Employ `typeof`, `instanceof`, `in`, or type predicates for safe type narrowing with union types or `unknown`.
*   **Leverage Utility Types:** Use built-in types like `Partial`, `Readonly`, `Pick`, `Omit` for common type transformations.
*   **Structural Typing:** Be aware that compatibility is based on shape (properties/methods), not explicit `implements` clauses.
*   **`void` for Callbacks:** Use `void` return type for callbacks when the return value should be ignored.
*   **Exhaustiveness Checking:** Use the `never` type in `default` switch cases or conditional types to ensure all possibilities are handled.

---
This index summarizes the core concepts, syntax, and patterns for TypeScript based on the provided examples. Consult the official TypeScript documentation for exhaustive details. Source: `project_journal/context/source_docs/typescript-specialist-llms-context-20250406.md`