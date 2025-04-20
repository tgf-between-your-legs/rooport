# Astro DB & Astro Actions

Guide to using Astro's integrated database and server actions features. Requires `output: 'server'` or `'hybrid'` mode and an adapter.

## Astro DB (`astro:db`)

*   **Concept:** A managed database service provided by Astro for Studio users (local development uses LibSQL/SQLite). Integrates directly with Astro projects.
*   **Setup:**
    1.  Run `npx astro add db` (if not already done).
    2.  Define schema in `db/config.ts`.
    3.  Run `npx astro db push` to apply schema changes (local and Studio).
*   **Schema Definition (`db/config.ts`):**
    *   Use `defineTable` and `column` helpers from `astro:db`.
    *   Define tables and their columns with types (e.g., `text`, `number`, `boolean`, `date`).
    *   Specify primary keys, indexes, and relationships (optional).
    ```typescript
    import { defineTable, column, defineDb } from 'astro:db';

    const User = defineTable({
      columns: {
        id: column.text({ primaryKey: true }),
        email: column.text({ unique: true }),
        name: column.text(),
        createdAt: column.date({ default: new Date() }),
      }
    });

    const Post = defineTable({
      columns: {
        id: column.number({ primaryKey: true }),
        title: column.text(),
        body: column.text(),
        authorId: column.text({ references: () => User.columns.id }), // Foreign key
        publishedAt: column.date({ optional: true }),
      },
      indexes: [{ on: ["authorId"] }], // Example index
    });

    // https://astro.build/db/config
    export default defineDb({
      tables: { User, Post }
    });
    ```
*   **Querying (`db` object from `astro:db`):**
    *   Import `db`, table definitions (e.g., `User`, `Post`) from `astro:db`.
    *   Use Drizzle ORM-like syntax for queries within `.astro` script fences or API routes.
    ```astro
    ---
    import { db, User, eq } from 'astro:db';

    // Get all users
    const allUsers = await db.select().from(User);

    // Get specific user
    const userId = 'user123';
    const user = await db.select().from(User).where(eq(User.id, userId)).get(); // .get() for single result
    ---
    <ul>
      {allUsers.map(u => <li>{u.name} ({u.email})</li>)}
    </ul>
    ```
*   **Mutations:** Use `db.insert()`, `db.update()`, `db.delete()`. **Best practice:** Perform mutations within Astro Actions for security and validation.

## Astro Actions (`astro:actions`)

*   **Concept:** Type-safe server functions (RPC) callable from client-side code or server-side code. Ideal for form submissions, mutations, and server logic triggered by user interactions. Automatically handles serialization and provides type safety.
*   **Setup:**
    1.  Enable experimental flags in `astro.config.mjs` (may change in future Astro versions):
        ```js
        export default defineConfig({
          experimental: {
            actions: true,
          },
          // ... other config
        });
        ```
    2.  Create action definitions in `src/actions/index.ts` (or similar).
*   **Defining Actions (`src/actions/index.ts`):**
    *   Use `defineAction` from `astro:actions`.
    *   Define input schema using Zod (`z`).
    *   Implement the `handler` function, which receives `input` and `context` (including `locals`, `cookies`).
    *   Perform server-side logic (validation, database mutations, calling external APIs).
    *   Return data or handle errors.
    ```typescript
    // src/actions/index.ts
    import { defineAction, z } from 'astro:actions';
    import { db, Post } from 'astro:db';

    export const server = {
      createPost: defineAction({
        accept: 'form', // or 'json'
        input: z.object({
          title: z.string().min(1),
          body: z.string().min(10),
          authorId: z.string(), // Assume authorId comes from context/session
        }),
        handler: async ({ title, body }, context) => {
          // TODO: Add proper authentication/authorization check using context.locals.user
          const authorId = context.locals.user?.id;
          if (!authorId) {
            return { success: false, error: 'Unauthorized' };
          }

          try {
            const result = await db.insert(Post).values({ title, body, authorId }).returning();
            return { success: true, postId: result[0]?.id };
          } catch (e) {
            console.error("Error creating post:", e);
            return { success: false, error: 'Failed to create post' };
          }
        },
      }),
      // Add other actions...
    };
    ```
*   **Calling Actions (Client-side):**
    *   Import `actions` from `astro:actions`.
    *   Call the action function directly (e.g., in an event handler). It returns a Promise with the action's result.
    *   Handles form data automatically if `accept: 'form'` and called from a `<form>` submission.
    ```jsx
    // Example in a React component island
    import { actions } from 'astro:actions';
    import { useState } from 'react';

    function PostForm() {
      const [error, setError] = useState('');
      const [success, setSuccess] = useState('');

      const handleSubmit = async (event) => {
        event.preventDefault();
        setError('');
        setSuccess('');
        const formData = new FormData(event.target);
        const result = await actions.createPost(formData); // Astro handles FormData

        if (result.error) {
          setError(result.error);
        } else {
          setSuccess(`Post created with ID: ${result.postId}`);
          event.target.reset();
        }
      };

      return (
        <form onSubmit={handleSubmit}>
          {/* Form inputs for title, body */}
          <input type="text" name="title" required />
          <textarea name="body" required></textarea>
          {error && <p style={{ color: 'red' }}>{error}</p>}
          {success && <p style={{ color: 'green' }}>{success}</p>}
          <button type="submit">Create Post</button>
        </form>
      );
    }
    ```

## Key Benefits

*   **Astro DB:** Simple, integrated database solution for content-heavy sites or basic data needs. Type-safe queries. Works locally and syncs with Astro Studio.
*   **Astro Actions:** Type-safe, easy way to handle server-side logic triggered from the client (like form submissions) without manually creating API routes. Simplifies mutations and validation.

*(Refer to official Astro DB and Astro Actions documentation for full details and latest updates.)*