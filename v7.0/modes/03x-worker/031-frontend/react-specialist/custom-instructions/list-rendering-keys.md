# React List Rendering & Keys

Best practices for rendering lists of elements in React and the importance of the `key` prop.

## Rendering Lists

*   **`.map()`:** The standard way to render a list of components from an array of data is using the JavaScript `.map()` method within JSX.
    ```jsx
    function NumberList({ numbers }) {
      const listItems = numbers.map((number) =>
        // WRONG: No key provided!
        // <li>{number}</li>

        // Correct: Key is provided
        <li key={number.toString()}> {/* Use a stable, unique ID */}
          {number}
        </li>
      );
      return <ul>{listItems}</ul>;
    }

    const numbers = [1, 2, 3, 4, 5];
    // Usage: <NumberList numbers={numbers} />
    ```

## The `key` Prop

*   **Purpose:** Keys help React identify which items in a list have changed, been added, or been removed. They give each element in the list a stable identity across renders.
*   **Requirement:** You **must** provide a `key` prop whenever you render a list of elements using `.map()` or similar iteration methods.
*   **Value:**
    *   Keys must be **strings** or **numbers**.
    *   Keys must be **unique among siblings** in the list. They don't need to be globally unique.
    *   Keys should be **stable** – they shouldn't change between renders for the same logical item.
*   **Where to Get Keys:**
    *   **Data IDs (Best):** If your data items have unique IDs (e.g., from a database), use those IDs as keys. This is the most reliable approach.
        ```jsx
        users.map(user => <UserComponent key={user.id} user={user} />)
        ```
    *   **Content-Derived (If Stable & Unique):** If items don't have IDs but their content is unique and stable, you might use a hash of the content or the content itself (if it's a simple string/number). Use with caution.
    *   **Array Index (Last Resort):** Using the array index (`map((item, index) => <li key={index}>...`)`) is **strongly discouraged** if the list order can change, items can be added/removed from the middle, or the list is filtered. Using the index as a key can lead to:
        *   Performance issues.
        *   Bugs with component state (e.g., state associated with the wrong item if order changes).
        *   Problems with uncontrolled inputs.
        **Only use the index as a key if:**
        1.  The list and items are static – they never reorder or get filtered.
        2.  The items have no IDs.
        3.  The component has no state that depends on the item's position.

## Why Keys Are Important

*   **Efficient Updates:** React uses keys to match elements between the previous and current renders. Without keys, React might have to destroy and recreate DOM nodes unnecessarily, which is inefficient. With stable keys, React can efficiently update, move, or remove only the necessary elements.
*   **Preserving State:** Keys ensure that the internal state of components within a list is preserved correctly when the list is reordered, filtered, or items are added/removed. If you use index as a key and reorder items, components might receive the wrong state because their position (index) changed, but React thinks it's the same component due to the key matching.

*(Refer to the official React documentation on Lists and Keys: https://react.dev/learn/rendering-lists)*