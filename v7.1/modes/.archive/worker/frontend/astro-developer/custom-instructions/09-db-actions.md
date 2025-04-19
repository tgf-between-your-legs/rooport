# Astro: Astro DB & Astro Actions

Using Astro's integrated database and server actions features. Requires `output: 'server'` or `'hybrid'` mode and an adapter.

## 1. Astro DB (`astro:db`)

Managed, serverless SQL database (LibSQL/SQLite) integrated with Astro.

**Setup:**

1.  Run `npx astro add db`.
2.  Define schema in `db/config.ts`.
3.  Run `npx astro db push` to apply schema changes.

**Schema Definition (`db/config.ts`):**

*   Use `defineTable`, `column` helpers from `astro:db`.
*   Define tables and columns with types (`text`, `number`, `boolean`, `date`, `json`).
*   Specify constraints (`primaryKey`, `unique`, `optional`, `default`, `references`).

```typescript
// db/config.ts
import { defineTable, column, defineDb, NOW } from 'astro:db';

const User = defineTable({
  columns: {
    id: column.number({ primaryKey: true }),
    email: column.text({ unique: true }),
    createdAt: column.date({ default: NOW }),
  }
});

const Post = defineTable({
  columns: {
    id: column.number({ primaryKey: true }),
    authorId: column.number({ references: () => User.columns.id }),
    title: column.text(),
  }
});

export default defineDb({ tables: { User, Post } });
```

**Querying (`db` object from `astro:db`):**

*   Import `db`, tables (e.g., `User`), and helpers (`eq`, `gt`, `like`) from `astro:db`.
*   Use Drizzle ORM-like syntax in `.astro` scripts, API routes, or middleware.

```astro
---
import { db, User, eq } from 'astro:db';
const user = await db.select().from(User).where(eq(User.id, 123)).get();
---
<p>User: {user?.email}</p>
```

**Mutations:**
*   Use `db.insert()`, `db.update()`, `db.delete()`.
*   **Best Practice:** Perform mutations within Astro Actions.

**Seeding (`db/seed.ts` - Optional):**
*   Export async `seed` function. Use `db.insert()` to add initial data. Run with `npx astro db seed`.

## 2. Astro Actions (`astro:actions`)

Type-safe server functions (RPC) callable from client or server code, ideal for form submissions and mutations.

**Setup:**

1.  Enable experimental flag if needed (`experimental: { actions: true }` in `astro.config.mjs`).
2.  Define actions in `src/actions/index.ts`.

**Defining Actions (`src/actions/index.ts`):**

*   Use `defineAction` from `astro:actions`.
*   Define input schema using Zod (`z`).
*   Implement the `handler` function (`async ({ args, context }) => { ... }`).
*   Perform server-side logic (validation, DB mutations). Return data or handle errors.

```typescript
// src/actions/index.ts
import { defineAction, z } from 'astro:actions';
import { db, Post } from 'astro:db';

export const server = { // MUST be named 'server'
  createPost: defineAction({
    accept: 'form', // or 'json'
    input: z.object({
      title: z.string().min(1),
      authorId: z.number(), // Assume comes from context/session
    }),
    handler: async ({ title }, context) => {
      // const authorId = context.locals.user?.id; // Get from middleware
      // if (!authorId) { return { success: false, error: 'Unauthorized' }; }
      const authorId = 1; // Placeholder

      try {
        const result = await db.insert(Post).values({ title, authorId }).returning();
        return { success: true, postId: result[0]?.id };
      } catch (e) {
        return { success: false, error: 'Failed to create post' };
      }
    },
  }),
};
```

**Calling Actions (Client-side):**

*   Import `actions` from `astro:actions`.
*   Call like an async function: `await actions.createPost(formData)` or `await actions.createPost({ title: '...', authorId: 1 })`.
*   Handles `FormData` automatically if `accept: 'form'`. Returns a Promise.

```jsx
// Example in React island
import { actions } from 'astro:actions';

async function handleSubmit(event) {
  event.preventDefault();
  const formData = new FormData(event.target);
  const result = await actions.createPost(formData);
  if (result.error) { /* Handle error */ }
  else { /* Handle success */ }
}
```

*(Refer to official Astro DB and Astro Actions documentation.)*