# Astro: Astro DB

Using Astro's integrated database solution for serverless environments.

## Core Concept: Astro DB

Astro DB is a fully managed, serverless SQL database service built specifically for Astro projects, powered by LibSQL (an open-source fork of SQLite). It allows you to define schemas, seed data, and query your database directly within your Astro components, API routes, and middleware, especially when deploying to serverless or edge platforms.

**Key Features:**

*   **Serverless:** No database server to manage. Scales automatically.
*   **SQLite-Based:** Uses LibSQL, offering SQLite compatibility and performance.
*   **Schema Definition:** Define tables and columns using TypeScript in `db/config.ts`.
*   **Type Safety:** Provides a type-safe query client (`astro:db`).
*   **Migrations:** Handles schema changes and data migrations via `npx astro db push`.
*   **Seeding:** Populate your database with initial data using `db/seed.ts`.
*   **Local Development:** Works locally using a local SQLite file.
*   **Astro Studio:** Integrates with Astro Studio for cloud hosting, management, and data browsing.

## Setup

1.  **Enable Experimental DB Flag (If needed):** In older Astro versions, you might need to enable the experimental flag in `astro.config.mjs`:
    ```javascript
    // astro.config.mjs
    export default defineConfig({
      // ...
      experimental: {
        integrations: true, // May be needed for older versions
        db: true
      }
    });
    ```
    *(Check current Astro docs if this flag is still required)*
2.  **Create `db/config.ts`:** Define your database tables and columns.
3.  **Run `astro db push`:** Apply schema changes and create/update the database (local file or remote Astro Studio DB).

## Defining Schemas (`db/config.ts`)

*   Import `defineDb`, `defineTable`, and `column` types from `astro:db`.
*   Define tables using `defineTable` with a `columns` object.
*   Specify column types (`text`, `number`, `boolean`, `date`, `json`).
*   Add constraints like `primaryKey`, `unique`, `optional`, `default`.
*   Define relationships using `references`.

```typescript
// db/config.ts
import { defineDb, defineTable, column, NOW } from 'astro:db';

// Define the User table
const User = defineTable({
  columns: {
    id: column.number({ primaryKey: true }),
    email: column.text({ unique: true }),
    name: column.text(),
    isAdmin: column.boolean({ default: false }),
    createdAt: column.date({ default: NOW }), // Use NOW for default timestamp
  }
});

// Define the Post table with a reference to User
const Post = defineTable({
  columns: {
    id: column.number({ primaryKey: true }),
    authorId: column.number({ references: () => User.columns.id }), // Foreign key
    title: column.text(),
    body: column.text({ optional: true }), // Optional column
    publishedAt: column.date({ optional: true }),
  }
});

// Export the database configuration
export default defineDb({
  tables: { User, Post }
});
```

## Seeding Data (`db/seed.ts`) - Optional

*   Create a `db/seed.ts` file.
*   Import `db` and table definitions from `astro:db`.
*   Export an async `seed` function.
*   Use `db.insert()` to add initial data.
*   Run seeding via `npx astro db seed`.

```typescript
// db/seed.ts
import { db, User, Post } from 'astro:db';

export default async function seed() {
  console.log('Seeding database...');

  await db.insert(User).values([
    { id: 1, email: 'alice@example.com', name: 'Alice' },
    { id: 2, email: 'bob@example.com', name: 'Bob', isAdmin: true },
  ]);

  await db.insert(Post).values([
    { id: 101, authorId: 1, title: 'First Post', publishedAt: new Date() },
    { id: 102, authorId: 2, title: 'Admin Post', body: 'This is content.' },
  ]);

  console.log('Database seeded!');
}
```

## Querying Data (`astro:db`)

*   Import `db`, table definitions, and SQL helpers (like `eq`, `gt`, `like`, `and`, `or`) from `astro:db` in your `.astro`, API routes (`.ts`), or middleware files.
*   Use the `db` client with a Drizzle ORM-like syntax.

```astro
---
// src/pages/users.astro
import { db, User } from 'astro:db'; // Import db and table
import BaseLayout from '../layouts/BaseLayout.astro';

// Fetch all users on the server
const users = await db.select().from(User);
---
<BaseLayout pageTitle="Users">
  <h1>Users</h1>
  <ul>
    {users.map(user => (
      <li>{user.name} ({user.email}) {user.isAdmin ? '(Admin)' : ''}</li>
    ))}
  </ul>
</BaseLayout>
```

```typescript
// src/pages/api/posts.ts
import type { APIRoute } from 'astro';
import { db, Post, User, eq, desc } from 'astro:db'; // Import helpers like eq, desc

export const GET: APIRoute = async ({ url }) => {
  try {
    const limitParam = url.searchParams.get('limit');
    const limit = limitParam ? parseInt(limitParam) : 10;

    // Example: Select posts joined with users, ordered by date
    const posts = await db.select({
        postId: Post.id,
        title: Post.title,
        published: Post.publishedAt,
        authorName: User.name // Select author name from joined table
      })
      .from(Post)
      .innerJoin(User, eq(Post.authorId, User.id)) // Join condition
      .orderBy(desc(Post.publishedAt)) // Order by date descending
      .limit(limit);

    return new Response(JSON.stringify(posts), {
      status: 200,
      headers: { 'Content-Type': 'application/json' }
    });
  } catch (error) {
    console.error("API Error:", error);
    return new Response('Failed to fetch posts', { status: 500 });
  }
}
```

## Migrations

*   After changing your schema in `db/config.ts`, run `npx astro db push`.
*   This command compares your schema with the database state (local file or Astro Studio) and generates/applies the necessary SQL migration statements.

Astro DB provides a convenient and type-safe way to add database persistence to Astro projects, especially suitable for serverless and edge deployments via Astro Studio.

*(Refer to the official Astro DB documentation.)*