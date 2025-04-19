# Astro: Content Collections & MDX

## 1. Content Collections (`astro:content`)

Manage local content (Markdown, MDX, JSON, YAML) with type safety.

**Core Concepts:**

*   **Location:** `src/content/`, organized into collection subdirectories (e.g., `src/content/blog`).
*   **Schema:** Define frontmatter/data structure and types using Zod in `src/content/config.ts`.
*   **Querying:** Use `getCollection()`, `getEntry()` in `.astro` files.
*   **Rendering:** Astro handles rendering. Use dynamic routes (`[slug].astro`) for individual entries.

**Setup (`src/content/config.ts`):**

```typescript
import { defineCollection, z } from 'astro:content';

const blogCollection = defineCollection({
  type: 'content', // 'content' for md/mdx, 'data' for json/yaml
  schema: z.object({
    title: z.string(),
    pubDate: z.date(),
    tags: z.array(z.string()).optional(),
    isDraft: z.boolean().default(false),
  }),
});

export const collections = { 'blog': blogCollection };
```

**Content Files (`src/content/blog/post.md`):**

```markdown
---
title: "My Post"
pubDate: 2024-01-15
tags: ["astro"]
---
Content here...
```

**Querying (`getCollection()`):**

```astro
---
import { getCollection } from 'astro:content';
const posts = await getCollection('blog', ({ data }) => !data.isDraft);
posts.sort((a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf());
---
<ul>
  {posts.map(post => (
    <li><a href={`/blog/${post.slug}/`}>{post.data.title}</a></li>
  ))}
</ul>
```

**Dynamic Routes (`src/pages/blog/[slug].astro`):**

```astro
---
import { getCollection } from 'astro:content';
export async function getStaticPaths() {
  const posts = await getCollection('blog', ({ data }) => !data.isDraft);
  return posts.map(entry => ({
    params: { slug: entry.slug },
    props: { entry },
  }));
}
const { entry } = Astro.props;
const { Content } = await entry.render(); // Render MD/MDX
---
<article>
  <h1>{entry.data.title}</h1>
  <Content /> {/* Render content */}
</article>
```

**Key API:**
*   `defineCollection({ type, schema })`
*   `z` (Zod schema builder)
*   `getCollection(name, ?filterFn)` -> `CollectionEntry[]`
*   `getEntry(name, id)` / `getEntryBySlug(name, slug)` -> `CollectionEntry`
*   `CollectionEntry`: `{ id, slug, body, collection, data, render() }`
*   `render()` -> `{ Content, headings, ... }`

## 2. MDX (`.mdx`)

Combine Markdown with embedded JSX components.

**Setup:**

1.  Install integration: `npx astro add mdx`
2.  Install framework integrations if needed (e.g., `npx astro add react`).

**Writing MDX (`src/content/blog/post.mdx`):**

```mdx
---
layout: ../../layouts/BaseLayout.astro
title: MDX Post
pubDate: 2024-01-16
import InteractiveCounter from '../../components/ReactCounter.jsx';
import Callout from '../../components/Callout.astro';
---
import { SITE_AUTHOR } from '../../config';

# {frontmatter.title} by {SITE_AUTHOR}

<Callout type="info">Markdown works!</Callout>

<InteractiveCounter client:visible />
```

**Usage:**
*   Works seamlessly with Content Collections (`type: 'content'`).
*   Query and render like standard Markdown using `getCollection` and `entry.render()`.
*   Import components (Astro or framework) using ESM `import`.
*   Use components as JSX tags `<MyComponent />`.
*   Add `client:*` directives to framework components for interactivity.

*(Refer to the official Astro Content Collections and MDX documentation.)*