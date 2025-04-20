# TypeScript: Common Utility Types

Built-in generic types that help transform or manipulate other types.

## Core Concept

Utility types take one or more existing types as input and produce a new type based on some transformation rule. They are powerful tools for creating reusable and precise types without repeating definitions.

## Common Utility Types

*   **`Partial<Type>`:** Makes all properties of `Type` optional.
    ```typescript
    interface Todo { title: string; description: string; completed: boolean; }
    type PartialTodo = Partial<Todo>;
    // Equivalent to: { title?: string; description?: string; completed?: boolean; }
    const update: PartialTodo = { description: "New description" };
    ```
*   **`Required<Type>`:** Makes all properties of `Type` required (removes optionality `?`).
    ```typescript
    interface Props { a?: number; b?: string; }
    type RequiredProps = Required<Props>;
    // Equivalent to: { a: number; b: string; }
    ```
*   **`Readonly<Type>`:** Makes all properties of `Type` readonly.
    ```typescript
    interface Config { apiKey: string; endpoint: string; }
    type ReadonlyConfig = Readonly<Config>;
    // Equivalent to: { readonly apiKey: string; readonly endpoint: string; }
    const config: ReadonlyConfig = { apiKey: "abc", endpoint: "/api" };
    // config.apiKey = "xyz"; // Error: Cannot assign to 'apiKey' because it is a read-only property.
    ```
*   **`Record<Keys, Type>`:** Constructs an object type with a set of properties `Keys` (usually a union of strings or literal types) all having the value `Type`.
    ```typescript
    type Page = 'home' | 'about' | 'contact';
    type PageInfo = { title: string; description: string; };

    const pageDetails: Record<Page, PageInfo> = {
      home: { title: "Home", description: "Homepage" },
      about: { title: "About", description: "About Us" },
      contact: { title: "Contact", description: "Contact Info" }
      // Error if a Page key is missing or has wrong value type
    };
    ```
*   **`Pick<Type, Keys>`:** Constructs a type by picking the set of properties `Keys` (string literal or union of string literals) from `Type`.
    ```typescript
    interface User { id: number; name: string; email: string; isAdmin: boolean; }
    type UserPreview = Pick<User, 'id' | 'name'>;
    // Equivalent to: { id: number; name: string; }
    ```
*   **`Omit<Type, Keys>`:** Constructs a type by picking all properties from `Type` and then removing `Keys` (string literal or union of string literals).
    ```typescript
    interface User { id: number; name: string; email: string; isAdmin: boolean; }
    type PublicUser = Omit<User, 'isAdmin' | 'email'>;
    // Equivalent to: { id: number; name: string; }
    ```
*   **`Exclude<UnionType, ExcludedMembers>`:** Constructs a type by excluding from `UnionType` all union members that are assignable to `ExcludedMembers`.
    ```typescript
    type Status = "pending" | "processing" | "success" | "failed";
    type ActiveStatus = Exclude<Status, "failed" | "pending">;
    // Equivalent to: "processing" | "success"
    ```
*   **`Extract<Type, Union>`:** Constructs a type by extracting from `Type` all union members that are assignable to `Union`. (Opposite of `Exclude`).
    ```typescript
    type Status = "pending" | "processing" | "success" | "failed";
    type DoneStatus = Extract<Status, "success" | "failed">;
    // Equivalent to: "success" | "failed"
    ```
*   **`NonNullable<Type>`:** Constructs a type by excluding `null` and `undefined` from `Type`.
    ```typescript
    type MaybeString = string | null | undefined;
    type DefinitelyString = NonNullable<MaybeString>;
    // Equivalent to: string
    ```
*   **`Parameters<Type>`:** Constructs a tuple type from the types used in the parameters of a function type `Type`.
    ```typescript
    type PointPrinter = (p: { x: number; y: number }) => void;
    type PointParams = Parameters<PointPrinter>;
    // Equivalent to: [p: { x: number; y: number }]
    ```
*   **`ConstructorParameters<Type>`:** Constructs a tuple or array type from the types of a constructor function type.
    ```typescript
    class Person { constructor(public name: string, public age: number) {} }
    type PersonParams = ConstructorParameters<typeof Person>;
    // Equivalent to: [name: string, age: number]
    ```
*   **`ReturnType<Type>`:** Constructs a type consisting of the return type of function `Type`.
    ```typescript
    type GetData = () => { id: number; value: string };
    type DataShape = ReturnType<GetData>;
    // Equivalent to: { id: number; value: string }
    ```
*   **`InstanceType<Type>`:** Constructs a type consisting of the instance type of a constructor function type.
    ```typescript
    class Car { /* ... */ }
    type CarInstance = InstanceType<typeof Car>;
    let myCar: CarInstance = new Car(); // myCar is of type Car
    ```
*   **`Uppercase<StringType>`**, **`Lowercase<StringType>`**, **`Capitalize<StringType>`**, **`Uncapitalize<StringType>`:** String manipulation types (work on string literal types).

*(Refer to the official TypeScript documentation on Utility Types: https://www.typescriptlang.org/docs/handbook/utility-types.html)*