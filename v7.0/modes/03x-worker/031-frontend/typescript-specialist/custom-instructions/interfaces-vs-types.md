# TypeScript: Interfaces vs. Type Aliases

Understanding the differences and similarities between `interface` and `type` for defining shapes in TypeScript.

## Core Concept

Both `interface` and `type` can be used to describe the "shape" of an object or a function. In many simple cases, they are interchangeable.

```typescript
// Using Interface
interface Point {
  x: number;
  y: number;
}

interface SetPoint {
  (x: number, y: number): void;
}

// Using Type Alias
type PointType = {
  x: number;
  y: number;
};

type SetPointType = (x: number, y: number) => void;

// Usage is similar
let p1: Point = { x: 10, y: 20 };
let p2: PointType = { x: 5, y: 15 };

const setPointFn: SetPoint = (x, y) => { console.log(x, y); };
const setPointFn2: SetPointType = (x, y) => { console.log(x, y); };
```

## Key Differences

1.  **Declaration Merging (Interfaces Only):**
    *   `interface` declarations with the same name in the same scope are automatically merged. This is useful for augmenting existing interfaces or for declaration files (`.d.ts`).
    *   `type` aliases cannot be merged; declaring the same `type` name twice results in an error.
    ```typescript
    interface Box {
      height: number;
      width: number;
    }
    interface Box { // Merged with the above
      scale: number;
    }
    let box: Box = { height: 5, width: 6, scale: 10 }; // All properties required

    // type BoxType = { height: number; width: number; };
    // type BoxType = { scale: number; }; // Error: Duplicate identifier 'BoxType'.
    ```

2.  **Extending / Implementing (Syntax Difference):**
    *   Both can extend/implement other interfaces or types, but the syntax differs slightly. Interfaces use `extends`, while types use intersection (`&`).
    ```typescript
    // Interface extends Interface
    interface Animal { name: string; }
    interface Bear extends Animal { honey: boolean; }

    // Type extends Type (using intersection)
    type AnimalType = { name: string; };
    type BearType = AnimalType & { honey: boolean; };

    // Interface extends Type
    interface Dog extends AnimalType { breed: string; }

    // Type extends Interface
    type Cat = Animal & { lives: number; };

    // Class implements Interface or Type (using implements)
    class LivingBear implements Bear { // Or implements BearType
        name = "Paddington";
        honey = true;
    }
    ```

3.  **Type Aliases Can Define More:**
    *   `type` aliases are more versatile and can define not just object shapes, but also:
        *   **Union Types:** `type StringOrNumber = string | number;`
        *   **Intersection Types:** `type NameAndAge = { name: string } & { age: number };`
        *   **Primitive Aliases:** `type UserID = string;`
        *   **Tuple Types:** `type PointTuple = [number, number];`
        *   **Mapped Types:** `type ReadonlyPoint = { readonly [K in keyof Point]: Point[K] };`
        *   **Conditional Types:** `type IsString<T> = T extends string ? true : false;`
    *   `interface` can primarily only describe object shapes or function types.

## Recommendation / When to Use Which

*   **Consistency is Key:** Choose one style (`interface` or `type`) for object shapes within your project and stick to it for consistency.
*   **Use `interface` for Object Shapes (Common Practice):** Many developers prefer using `interface` for defining the shape of objects and classes because:
    *   Declaration merging can be useful for extensibility, especially when working with external libraries or augmenting global types.
    *   The `extends` keyword is often considered more intuitive for inheritance-like relationships.
*   **Use `type` for Other Cases:** Use `type` aliases when you need:
    *   Unions (`|`)
    *   Intersections (`&`) (though interfaces can achieve similar results with `extends`)
    *   Aliases for primitive types
    *   Tuples
    *   Mapped Types
    *   Conditional Types
    *   Function types (can use either, `type` is slightly more concise: `type MyFn = () => void;` vs `interface MyFn { (): void; }`)

**Summary Table:**

| Feature              | `interface`                     | `type` alias                       | Recommendation                                  |
| :------------------- | :------------------------------ | :--------------------------------- | :---------------------------------------------- |
| Object Shape         | ✅ Yes                          | ✅ Yes                             | Use `interface` (common convention) or `type` |
| Function Shape       | ✅ Yes                          | ✅ Yes                             | Use `type` (more concise) or `interface`      |
| Declaration Merging  | ✅ Yes                          | ❌ No                              | Use `interface` if needed                     |
| Extends/Implements   | `extends`                       | `&` (Intersection)                 | Both work, syntax differs                     |
| Unions               | ❌ No                           | ✅ Yes                             | Use `type`                                      |
| Intersections        | (via `extends`)                 | ✅ Yes (`&`)                       | Use `type` (explicit) or `interface`          |
| Primitives/Tuples    | ❌ No                           | ✅ Yes                             | Use `type`                                      |
| Mapped/Conditional   | ❌ No                           | ✅ Yes                             | Use `type`                                      |

Ultimately, for simple object shapes, the choice is largely stylistic. Follow project conventions if they exist.

*(Refer to the official TypeScript documentation on Interfaces and Type Aliases.)*