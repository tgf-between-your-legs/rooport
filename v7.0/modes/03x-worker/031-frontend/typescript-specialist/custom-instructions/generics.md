# TypeScript: Generics

Creating reusable components, functions, and types that can work over a variety of types rather than a single one.

## Core Concept

Generics allow you to write code that works with different types without losing type safety. You define a type variable (conventionally `T`, `U`, `K`, `V`, etc.) that acts as a placeholder for the actual type, which is specified when the generic function, class, or type alias is used.

## Generic Functions

*   Define a type variable in angle brackets `<T>` after the function name.
*   Use the type variable `T` in parameter types and return types.
*   TypeScript infers the type `T` based on the arguments passed, or you can specify it explicitly.

```typescript
// Identity function - returns whatever is passed in
function identity<T>(arg: T): T {
  return arg;
}

// Type is inferred as 'string'
let output1 = identity("myString");

// Type is inferred as 'number'
let output2 = identity(123);

// Explicitly set the type (less common when inference works)
let output3 = identity<boolean>(true);

// Generic function with multiple type variables and constraints
function mergeObjects<T extends object, U extends object>(obj1: T, obj2: U): T & U {
  return { ...obj1, ...obj2 };
}

const merged = mergeObjects({ name: "Alice" }, { age: 30 });
// merged type is { name: string } & { age: number }
console.log(merged.name, merged.age);

// Generic function working with arrays
function getFirstElement<ElementType>(arr: ElementType[]): ElementType | undefined {
    return arr[0];
}

const firstNum = getFirstElement([1, 2, 3]); // Type is number | undefined
const firstStr = getFirstElement(["a", "b"]); // Type is string | undefined
```

## Generic Interfaces & Type Aliases

*   Define type variables in angle brackets `<T>` after the interface/type name.
*   Use the type variable within the definition.
*   Specify the actual type when using the interface/type alias.

```typescript
// Generic Interface
interface KeyValuePair<K, V> {
  key: K;
  value: V;
}

let pair1: KeyValuePair<string, number> = { key: "age", value: 30 };
let pair2: KeyValuePair<number, boolean> = { key: 123, value: true };

// Generic Type Alias
type ApiResponse<DataType> = {
  data: DataType;
  status: 'success' | 'error';
  errorMessage?: string;
};

type User = { id: number; name: string };

let userResponse: ApiResponse<User> = {
  data: { id: 1, name: "Bob" },
  status: 'success'
};

let errorResponse: ApiResponse<null> = {
  data: null,
  status: 'error',
  errorMessage: 'Failed to load'
};
```

## Generic Classes

*   Define type variables in angle brackets `<T>` after the class name.
*   Use the type variable for properties, method parameters, and return types.
*   Specify the actual type when instantiating the class.

```typescript
class DataStorage<T> {
  private data: T[] = [];

  addItem(item: T): void {
    this.data.push(item);
  }

  getItem(index: number): T | undefined {
    return this.data[index];
  }

  getAll(): T[] {
    return [...this.data];
  }
}

// Store numbers
const numberStore = new DataStorage<number>();
numberStore.addItem(10);
// numberStore.addItem("hello"); // Error: Argument of type 'string' is not assignable to parameter of type 'number'.
console.log(numberStore.getItem(0));

// Store strings
const stringStore = new DataStorage<string>();
stringStore.addItem("apple");
console.log(stringStore.getAll());
```

## Generic Constraints (`extends`)

*   You can constrain the types that can be used for a type variable using the `extends` keyword. This ensures the type variable has certain properties or methods.

```typescript
interface Lengthwise {
  length: number; // Require a .length property
}

// T must have a .length property
function logLength<T extends Lengthwise>(arg: T): void {
  console.log(arg.length);
}

logLength("hello"); // OK (string has length)
logLength([1, 2, 3]); // OK (array has length)
logLength({ length: 10, value: 3 }); // OK (object has length)
// logLength(123); // Error: Argument of type 'number' is not assignable to parameter of type 'Lengthwise'.
```

## Benefits of Generics

*   **Reusability:** Write code once that works for multiple types.
*   **Type Safety:** Maintain type checking even when working with different types. Avoids using `any`.
*   **Flexibility:** Allows consumers of your functions/classes/types to specify the exact types they need.

*(Refer to the official TypeScript documentation on Generics: https://www.typescriptlang.org/docs/handbook/2/generics.html)*