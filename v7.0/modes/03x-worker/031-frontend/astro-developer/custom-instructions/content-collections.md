# Astro Content Collections (`astro:content`)

Guide to using Astro's built-in system for managing local Markdown and MDX content.

## Core Concepts

*   **Purpose:** Organize, validate, and query Markdown (`.md`) and MDX (`.mdx`) files within your project, typically for blogs, documentation, or other content-heavy sections.
*   **Location:** Content files reside within the `src/content/` directory, organized into subdirectories representing different collections (e.g., `src/content/blog/`, `src/content/docs/`).
*   **Schema Definition:** Define the expected frontmatter structure and types for each collection using Zod in `src/content/config.ts` (or `.js`). This provides type safety and validation.
*   **Querying:** Use `getCollection()` within `.astro` files to fetch and filter entries from a collection.
*   **Rendering:** Astro automatically renders Markdown/MDX content when you link to it or query it. You can create dynamic routes based on collection slugs.

## Setup (`src/content/config.ts`)

Define schemas for each collection using `defineCollection` and Zod (`z`).

```typescript
// src/content/config.ts
import { defineCollection, z } from 'astro:content';

// Define schema for the 'blog' collection
const blogCollection = defineCollection({
  type: 'content', // 'content' for md/mdx, 'data' for json/yaml
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
    publishDate: z.date(),
    tags: z.array(z.string()).optional(),
    isDraft: z.boolean().default(false),
    // Add other frontmatter fields as needed
  }),
});

// Define schema for the 'docs' collection
const docsCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    section: z.string(),
    order: z.number().optional(),
  }),
});

// Export collections object
export const collections = {
  'blog': blogCollection,
  'docs': docsCollection,
};
```

## Content Files (`src/content/[collection]/...`)

Create `.md` or `.mdx` files within collection directories. Include frontmatter matching the defined schema.

```markdown
---
# src/content/blog/my-first-post.md
title: "My First Astro Post"
description: "Learning about content collections."
publishDate: 2025-04-15
tags: ["astro", "learning"]
isDraft: false
layout: ../../layouts/BlogPostLayout.astro # Optional: Specify layout
---

## Introduction

This is my first post using Astro Content Collections!

It's **easy** to write content here.
```

## Querying Content (`getCollection()`)

Use `getCollection()` in the script fence (`---`) of `.astro` files to fetch entries.

```astro
---
// src/pages/blog/index.astro
import { getCollection } from 'astro:content';
import BaseLayout from '../../layouts/BaseLayout.astro';

// Get all published blog posts, sorted by date
const publishedPosts = await getCollection('blog', ({ data }) => {
  return data.isDraft !== true; // Filter out drafts
});
publishedPosts.sort((a, b) => b.data.publishDate.valueOf() - a.data.publishDate.valueOf());
---
<BaseLayout title="Blog">
  <h1>My Blog</h1>
  <ul>
    {publishedPosts.map(post => (
      <li>
        <a href={`/blog/${post.slug}/`}>{post.data.title}</a>
        <p>Published on: {post.data.publishDate.toLocaleDateString()}</p>
      </li>
    ))}
  </ul>
</BaseLayout>
```

## Dynamic Routes (`src/pages/[collection]/[...slug].astro`)

Create pages that dynamically render individual collection entries.

```astro
---
// src/pages/blog/[...slug].astro
import { getCollection } from 'astro:content';
import BlogPostLayout from '../../layouts/BlogPostLayout.astro';

// 1. Generate static paths for all blog posts
export async function getStaticPaths() {
  const blogEntries = await getCollection('blog', ({ data }) => !data.isDraft);
  return blogEntries.map(entry => ({
    params: { slug: entry.slug }, // The slug is used in the URL
    props: { entry }, // Pass the full entry data to the component
  }));
}

// 2. Get the entry for the current page
const { entry } = Astro.props;
const { Content } = await entry.render(); // Render the MD/MDX content
---
<BlogPostLayout frontmatter={entry.data}>
  <h1>{entry.data.title}</h1>
  <Content /> {/* Render the Markdown/MDX content here */}
</BlogPostLayout>
```

## Key Properties/Functions

*   `defineCollection({ type, schema })`: Defines a collection in `config.ts`.
*   `z` (Zod): Used to define the schema for frontmatter validation.
*   `getCollection('collectionName', ?filterFn)`: Fetches entries. Returns an array of `CollectionEntry` objects.
*   `CollectionEntry`: Object representing a content file.
    *   `id`: Filename without extension.
    *   `slug`: URL-friendly identifier (usually derived from filename).
    *   `body`: Raw Markdown/MDX content string.
    *   `collection`: Name of the collection.
    *   `data`: Parsed frontmatter object (typed according to schema).
    *   `render()`: Async function returning `{ Content, headings, remarkPluginFrontmatter }`. `Content` is the rendered component.
*   `getEntryBySlug('collectionName', slug)` / `getEntry('collectionName', id)`: Fetch a single entry.

*(Refer to the official Astro Content Collections documentation: https://docs.astro.build/en/guides/content-collections/)*