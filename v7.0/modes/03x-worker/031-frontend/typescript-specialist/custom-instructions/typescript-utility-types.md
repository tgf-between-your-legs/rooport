# TypeScript: Utility Types

Using built-in utility types to transform and manipulate existing types.

## Core Concept: Type Transformations

TypeScript provides several built-in **utility types** that allow you to create new types based on existing ones in common ways. These help reduce boilerplate and create more flexible and reusable type definitions. They often work with generic type parameters (`<T>`).

## Common Utility Types

1.  **`Partial<T>`:**
    *   Makes all properties of type `T` optional.
    *   **Use Case:** Creating objects for updates where only some fields might be provided.

    ```typescript
    interface User {
      id: number;
      name: string;
      email: string;
      isAdmin: boolean;
    }

    function updateUser(id: number, update: Partial<User>): void {
      // Allows passing { name: "New Name" } or { isAdmin: true } etc.
      console.log(`Updating user ${id} with:`, update);
      // ... find user and apply updates ...
    }

    updateUser(1, { name: "Alice Smith" });
    updateUser(2, { isAdmin: false, email: "bob@example.com" });
    // updateUser(3, { invalidProp: true }); // Error: 'invalidProp' does not exist in type 'Partial<User>'
    ```

2.  **`Required<T>`:**
    *   Makes all properties of type `T` required (removes optional `?`).

    ```typescript
    interface Config {
      port?: number;
      host?: string;
    }

    const fullConfig: Required<Config> = {
      port: 8080,
      host: "localhost", // Both properties must be provided
    };
    ```

3.  **`Readonly<T>`:**
    *   Makes all properties of type `T` read-only.

    ```typescript
    interface Point { x: number; y: number; }
    const origin: Readonly<Point> = { x: 0, y: 0 };
    // origin.x = 10; // Error: Cannot assign to 'x' because it is a read-only property.
    ```

4.  **`Pick<T, K>`:**
    *   Constructs a type by picking a set of properties `K` (string literal or union of string literals) from type `T`.
    *   **Use Case:** Creating a simpler type with only a subset of properties.

    ```typescript
    interface Todo {
      title: string;
      description: string;
      completed: boolean;
      createdAt: number;
    }

    type TodoPreview = Pick<Todo, "title" | "completed">;

    const preview: TodoPreview = {
      title: "Learn TypeScript",
      completed: false,
      // description: "...", // Error: Property 'description' does not exist on type 'TodoPreview'
    };
    ```

5.  **`Omit<T, K>`:**
    *   Constructs a type by picking all properties from `T` and then removing `K` (string literal or union of string literals).
    *   **Use Case:** Creating a type by removing specific properties from another type.

    ```typescript
    interface UserWithPassword {
      id: string;
      name: string;
      email: string;
      passwordHash: string;
    }

    // Create a type without the password hash
    type PublicUser = Omit<UserWithPassword, "passwordHash">;

    const publicProfile: PublicUser = {
      id: "user-123",
      name: "Charlie",
      email: "charlie@example.com",
      // passwordHash: "...", // Error: Property 'passwordHash' does not exist on type 'PublicUser'
    };
    ```

6.  **`Record<K, T>`:**
    *   Constructs an object type whose property keys are `K` (a union of string/number literals, or `string`, `number`, `symbol`) and whose property values are `T`.
    *   **Use Case:** Describing objects used as dictionaries or maps.

    ```typescript
    type UserRoles = "admin" | "editor" | "viewer";

    // An object where keys are UserRoles and values are boolean permissions
    const permissions: Record<UserRoles, boolean> = {
      admin: true,
      editor: true,
      viewer: false,
    };

    // A dictionary mapping user IDs (strings) to User objects
    interface User { name: string; }
    const usersById: Record<string, User> = {
      "user-1": { name: "Alice" },
      "user-2": { name: "Bob" },
    };
    ```

7.  **`Exclude<T, U>`:**
    *   Constructs a type by excluding from `T` all properties that are assignable to `U`. (Works on union types).

    ```typescript
    type Status = "pending" | "processing" | "success" | "failed";
    type NonPendingStatus = Exclude<Status, "pending">; // "processing" | "success" | "failed"
    ```

8.  **`Extract<T, U>`:**
    *   Constructs a type by extracting from `T` all properties that are assignable to `U`. (Works on union types).

    ```typescript
    type NumericStatus = 100 | 200 | 404 | 500;
    type SuccessStatus = Extract<NumericStatus, 200 | 300>; // 200
    ```

9.  **`NonNullable<T>`:**
    *   Constructs a type by excluding `null` and `undefined` from `T`.

    ```typescript
    type MaybeString = string | null | undefined;
    type DefinitelyString = NonNullable<MaybeString>; // string
    ```

10. **`ReturnType<T>`:**
    *   Constructs a type consisting of the return type of a function type `T`.

    ```typescript
    type AddFn = (a: number, b: number) => number;
    type AddResult = ReturnType<AddFn>; // number

    function createPoint() { return { x: 0, y: 0 }; }
    type PointType = ReturnType<typeof createPoint>; // { x: number, y: number }
    ```

11. **`Parameters<T>`:**
    *   Constructs a tuple type from the types used in the parameters of a function type `T`.

    ```typescript
    type GreetFn = (name: string, age?: number) => void;
    type GreetParams = Parameters<GreetFn>; // [name: string, age?: number | undefined]
    ```

12. **`Awaited<T>`:**
    *   Recursively unwraps `Promise` types. Useful for getting the resolved type of an async function or nested promises.

    ```typescript
    async function fetchData(): Promise<{ data: string[] }> { /* ... */ }
    type FetchedData = Awaited<ReturnType<typeof fetchData>>; // { data: string[] }
    ```

Utility types are powerful tools for manipulating and creating new types from existing ones without repetitive declarations, leading to more concise and maintainable TypeScript code.

*(Refer to the official TypeScript documentation on Utility Types.)*