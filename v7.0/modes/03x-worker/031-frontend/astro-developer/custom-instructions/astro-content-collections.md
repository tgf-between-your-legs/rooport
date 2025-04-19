# Astro: Content Collections

Managing local content (Markdown, MDX, JSON, YAML) with type safety and helper utilities using `astro:content`.

## Core Concept

Content Collections provide a structured way to organize and query local content files within your Astro project, primarily intended for content like blog posts, documentation, author profiles, product data, etc.

**Key Features:**

*   **Organization:** Content files reside within subdirectories inside `src/content/` (e.g., `src/content/blog`, `src/content/authors`).
*   **Type Safety:** Define schemas for your collections in `src/content/config.ts` using Zod. Astro validates your frontmatter against these schemas at build time, catching errors early.
*   **Query API:** Astro provides utilities (`getCollection()`, `getEntry()`, `getEntries()`) to query content entries from your collections within `.astro` components and API routes.
*   **Content Rendering:** Astro automatically handles rendering Markdown (`.md`) and MDX (`.mdx`) content, providing access to both frontmatter and the rendered HTML or MDX component.

## Setup

1.  **Create `src/content/` Directory:** This is where your collections will live.
2.  **Create Collection Subdirectories:** Inside `src/content/`, create folders for each collection (e.g., `blog`, `docs`, `products`).
3.  **Add Content Files:** Place your `.md`, `.mdx`, `.json`, or `.yaml` files within their respective collection directories. Include frontmatter (YAML block at the top for MD/MDX) for metadata.
4.  **Define Schemas (`src/content/config.ts`):** This file is crucial for type safety.
    *   Import `defineCollection` and schema helpers (like `z` from Zod) from `astro:content`.
    *   Define an object mapping collection names (matching directory names) to `defineCollection` calls.
    *   Inside `defineCollection`, specify the `type` (`'content'` for MD/MDX, `'data'` for JSON/YAML) and a `schema` using Zod to validate frontmatter/data structure.

```typescript
// src/content/config.ts
import { defineCollection, z } from 'astro:content';

// Define schema for the 'blog' collection (Markdown/MDX files)
const blogCollection = defineCollection({
  type: 'content', // Type for Markdown/MDX
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
    author: z.string().default('Admin'),
    pubDate: z.date(),
    tags: z.array(z.string()).optional(),
    isDraft: z.boolean().default(false),
    // Reference other collections (e.g., authors)
    // authorRef: z.reference('authors').optional(),
  }),
});

// Define schema for 'authors' collection (JSON/YAML files)
const authorsCollection = defineCollection({
    type: 'data', // Type for JSON/YAML
    schema: z.object({
        name: z.string(),
        bio: z.string(),
        twitter: z.string().url().optional(),
    })
});

// Export collections object
export const collections = {
  'blog': blogCollection,
  'authors': authorsCollection,
};
```

## Querying Content

Use `astro:content` helper functions within `.astro` files (in the script fence).

*   **`getCollection(collectionName, filterFn?)`:** Retrieves an array of all entries within a collection. Optionally provide a filter function based on entry data/slug. Returns objects with `id`, `slug`, `body` (for MD/MDX), `collection`, `data` (parsed frontmatter), and a `render()` function (for MD/MDX).
*   **`getEntry(collectionName, slug)` or `getEntry({ collection, slug })`:** Retrieves a single entry by its collection and slug.
*   **`getEntries([...entries])`:** Retrieves multiple specific entries.
*   **`reference(collectionName)`:** Used within schemas (`config.ts`) to define relationships between collections.

```astro
---
// src/pages/blog/index.astro (Blog Listing Page)
import { getCollection } from 'astro:content';
import BaseLayout from '../../layouts/BaseLayout.astro';

// Get all non-draft blog posts, sorted by date
const posts = (await getCollection('blog', ({ data }) => {
  return data.isDraft !== true; // Filter out drafts
})).sort((a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf());
---
<BaseLayout pageTitle="Blog">
  <h1>My Blog</h1>
  <ul>
    {posts.map((post) => (
      <li>
        <a href={`/blog/${post.slug}/`}>{post.data.title}</a>
        <p>Published on: {post.data.pubDate.toDateString()}</p>
      </li>
    ))}
  </ul>
</BaseLayout>
```

```astro
---
// src/pages/blog/[slug].astro (Individual Blog Post Page)
import { getCollection, getEntry } from 'astro:content';
import BaseLayout from '../../layouts/BaseLayout.astro';

// Required for SSG: Generate paths for each post
export async function getStaticPaths() {
  const posts = await getCollection('blog', ({ data }) => !data.isDraft);
  return posts.map((post) => ({
    params: { slug: post.slug },
    props: { entry: post }, // Pass the full entry as props
  }));
}

const { entry } = Astro.props;
const { Content } = await entry.render(); // Get the rendered content component
---
<BaseLayout pageTitle={entry.data.title}>
  <h1>{entry.data.title}</h1>
  <p>Published: {entry.data.pubDate.toDateString()} by {entry.data.author}</p>
  <article>
    <Content /> {/* Render the MDX/Markdown content */}
  </article>
</BaseLayout>
```

## Rendering Content

*   For `.md` or `.mdx` entries retrieved via `getCollection` or `getEntry`, call the async `entry.render()` function.
*   This returns an object containing metadata (`headings`, `remarkPluginFrontmatter`) and, crucially, the `{ Content }` component.
*   Render the `<Content />` component in your template to display the processed HTML (for Markdown) or render the MDX content (including any imported components).

Content Collections provide a robust, type-safe way to manage and query local content, making Astro ideal for blogs, documentation sites, and other content-heavy projects.

*(Refer to the official Astro Content Collections documentation.)*