# TypeScript: Advanced Types

Brief overview of more advanced type manipulation techniques.

## 1. Conditional Types (`T extends U ? X : Y`)

*   **Purpose:** Selects one of two possible types based on a condition involving a type relationship (`extends`).
*   **Syntax:** `SomeType extends OtherType ? TrueType : FalseType`
*   **Use Cases:** Creating types that change based on input types, distributing unions.
    ```typescript
    // Example: Flatten array types, leave others as is
    type Flatten<T> = T extends Array<infer Item> ? Item : T;

    type Str = Flatten<string[]>; // Type is string
    type Num = Flatten<number>;   // Type is number

    // Example: Distributive conditional type
    type ToArray<T> = T extends any ? T[] : never;
    type StrArrOrNumArr = ToArray<string | number>; // Type is string[] | number[]
    ```
*   **`infer` Keyword:** Used within the `extends` clause of a conditional type to infer a type variable from within another type (like inferring the item type `Item` from `Array<infer Item>`).

## 2. Mapped Types (`{ [P in K]: T }`)

*   **Purpose:** Creates new object types by transforming properties from an existing object type. Uses `in` keyword similar to `for...in` loop for keys.
*   **Syntax:** `{ [Property in Keys]: NewType }`
    *   `Keys`: Usually a union of string/number literals, often obtained using `keyof Type`.
    *   `Property`: A variable name representing each key during iteration.
    *   `NewType`: The type assigned to the property, often based on `Property` or the original type `Type[Property]`.
*   **Modifiers:** Can add/remove `readonly` and `?` (optional) modifiers using `+` or `-`.
    ```typescript
    interface User {
      id: number;
      name: string;
      email?: string; // Optional
    }

    // Make all properties readonly
    type ReadonlyUser = {
      readonly [P in keyof User]: User[P];
    };
    // Equivalent to built-in Readonly<User>

    // Make all properties optional
    type PartialUser = {
      [P in keyof User]?: User[P];
    };
    // Equivalent to built-in Partial<User>

    // Make all properties required
    type RequiredUser = {
      [P in keyof User]-?: User[P]; // Use '-?' to remove optionality
    };
    // Equivalent to built-in Required<User>

    // Map to different value types
    type UserPermissions = {
      [P in keyof User]: boolean; // All properties become boolean
    };
    // Result: { id: boolean; name: boolean; email: boolean; }

    // Key Remapping via `as`
    type Getters<Type> = {
        [Property in keyof Type as `get${Capitalize<string & Property>}`]: () => Type[Property]
    };
    interface Person { name: string; age: number; location: string; }
    type LazyPerson = Getters<Person>;
    /* Result:
    {
        getName: () => string;
        getAge: () => number;
        getLocation: () => string;
    }
    */
    ```

## 3. Template Literal Types

*   **Purpose:** Creates new string literal types by concatenating or manipulating existing string literal types within backticks `` ` ``.
*   **Syntax:** Similar to JavaScript template literals, but used at the type level.
    ```typescript
    type World = "world";
    type Greeting = `hello ${World}`; // Type is "hello world"

    type EmailLocaleIDs = "welcome_email" | "email_heading";
    type FooterLocaleIDs = "footer_title" | "footer_sendoff";

    // Create a union of all locale IDs
    type AllLocaleIDs = `${EmailLocaleIDs | FooterLocaleIDs}_id`;
    // Result: "welcome_email_id" | "email_heading_id" | "footer_title_id" | "footer_sendoff_id"

    // Combine with string manipulation types
    type Lang = "en" | "es";
    type LocaleKeys = `${Lang}_${AllLocaleIDs}`;
    // Result: "en_welcome_email_id" | "es_welcome_email_id" | ... etc.

    // Example with function overload based on template literal
    type PropEventSource<T extends string> = `${T}Changed`;
    declare function makeWatchedObject<T extends string>(obj: { [K in T]: any }, handlers: { [K in T as PropEventSource<K>]: () => void }): void;

    makeWatchedObject(
        { name: "Alice", age: 30 },
        {
            nameChanged: () => {},
            ageChanged: () => {},
            // locationChanged: () => {} // Error: Property 'locationChanged' does not exist
        }
    );
    ```

These advanced types allow for highly expressive and precise type definitions, enabling better static analysis and reducing runtime errors.

*(Refer to the official TypeScript documentation on Advanced Types: Conditional Types, Mapped Types, Template Literal Types.)*