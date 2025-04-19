# TypeScript: Advanced Type Manipulation

Exploring more complex type features like Conditional Types, Mapped Types, and Template Literal Types.

## 1. Conditional Types (`T extends U ? X : Y`)

*   **Purpose:** Select one of two possible types based on a condition involving a type relationship (`extends`).
*   **Syntax:** `SomeType extends OtherType ? TrueType : FalseType`
*   **Use Case:** Creating types that change based on the input type, filtering types within unions, inferring types within conditions.

```typescript
// Example: Flatten array or keep type as is
type Flatten<T> = T extends Array<infer Item> ? Item : T;

type Str = Flatten<string[]>; // Type is string
type Num = Flatten<number>;   // Type is number

// Example: Extract function return type or never
type GetReturnType<T> = T extends (...args: any[]) => infer R ? R : never;

type Fn = () => number;
type FnReturn = GetReturnType<Fn>; // Type is number

type NotFn = string;
type NotFnReturn = GetReturnType<NotFn>; // Type is never

// Example: Filtering properties in a union
type NonFunctionKeys<T> = {
  [K in keyof T]: T[K] extends Function ? never : K;
}[keyof T];

interface User {
  id: number;
  name: string;
  getName(): string;
}

type UserDataKeys = NonFunctionKeys<User>; // Type is "id" | "name"
```

*   **`infer` Keyword:** Used within the `extends` clause of a conditional type to declare a type variable that captures a type inferred from the "true" branch.

## 2. Mapped Types (`{ [P in K]: T }`)

*   **Purpose:** Create new object types by transforming properties from an existing object type (`T`) or a union of keys (`K`).
*   **Syntax:** Uses `in` keyword similar to `for...in` loop, iterating over keys (`P`) in a union (`K`, often `keyof T`).
*   **Modifiers:** Can use `+` or `-` prefixes with `readonly` and `?` modifiers to add or remove them during mapping.

```typescript
// Example: Make all properties readonly (Equivalent to Readonly<T>)
type ReadonlyProps<T> = {
  readonly [P in keyof T]: T[P];
};

interface Point { x: number; y: number; }
type ReadonlyPoint = ReadonlyProps<Point>; // { readonly x: number; readonly y: number; }

// Example: Make all properties optional (Equivalent to Partial<T>)
type OptionalProps<T> = {
  [P in keyof T]?: T[P]; // Add '?' modifier
};
type OptionalPoint = OptionalProps<Point>; // { x?: number; y?: number; }

// Example: Remove readonly modifier
type Mutable<T> = {
  -readonly [P in keyof T]: T[P]; // Use '-readonly'
};
type MutableReadonlyPoint = Mutable<ReadonlyPoint>; // { x: number; y: number; }

// Example: Mapping keys to different value types
type StringifyProps<T> = {
  [P in keyof T]: string;
};
type StringifiedPoint = StringifyProps<Point>; // { x: string; y: string; }

// Example: Filtering/Renaming keys during mapping (using 'as' clause)
type Getters<T> = {
    [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K]
};
interface Person { name: string; age: number; }
type PersonGetters = Getters<Person>; // { getName: () => string; getAge: () => number; }
```

## 3. Template Literal Types

*   **Purpose:** Create specific string literal types by concatenating string literals and other primitive types within a template literal syntax.
*   **Syntax:** Uses backticks `` ` `` like JavaScript template literals, but at the type level.

```typescript
type EventName = "click" | "scroll" | "mousemove";
type ElementId = "btn" | "container" | "input";

// Create all combinations like "btn-click", "container-scroll", etc.
type ElementEvent = `${ElementId}-${EventName}`;

let event1: ElementEvent = "btn-click";
let event2: ElementEvent = "container-scroll";
// let event3: ElementEvent = "input-focus"; // Error: Type '"input-focus"' is not assignable...

// Can combine with other types
type Padding = `p-${1 | 2 | 4 | 8}`; // "p-1" | "p-2" | "p-4" | "p-8"
type MarginAxis = `m${'x' | 'y'}-${number}`; // "mx-10", "my-3", etc.

// Can be used in Mapped Types with 'as'
type PropGetters<T> = {
  [K in keyof T & string as `get${Capitalize<K>}`]: () => T[K]
};
interface Circle { radius: number; color: string; }
type CircleGetters = PropGetters<Circle>; // { getRadius: () => number; getColor: () => string; }
```

These advanced type features provide powerful tools for creating highly specific, flexible, and reusable types, enabling more sophisticated type manipulation and stronger guarantees in complex codebases.

*(Refer to the official TypeScript documentation on Advanced Types like Conditional Types, Mapped Types, and Template Literal Types.)*