# Astro: Using MDX

Writing content with Markdown and embedded components using MDX in Astro.

## Core Concept: MDX

MDX (`.mdx`) combines the simplicity of Markdown with the power of JSX, allowing you to import and use components (Astro, React, Vue, Svelte, etc.) directly within your content files.

**Key Features:**

*   **Markdown Syntax:** Write content using standard Markdown syntax.
*   **Component Imports:** Import components (Astro or UI framework) in a `setup` script or directly in the main body using ESM `import` statements.
*   **JSX Expressions:** Use JSX syntax `{}` to embed JavaScript expressions and render components like `<MyComponent prop="value" />`.
*   **Frontmatter:** Use YAML frontmatter (like standard Markdown) to define metadata (title, layout, date, etc.).
*   **Layouts:** Apply Astro layouts using the `layout` frontmatter property.

## Setup

1.  **Install MDX Integration:** If not already present (it's often included in starters), add the official MDX integration:
    ```bash
    npx astro add mdx
    ```
    This installs `@astrojs/mdx` and updates `astro.config.mjs`.
2.  **Framework Integrations (Optional):** If you want to use React, Vue, Svelte, etc., components within your MDX, ensure their respective integrations are also added (`npx astro add react`, etc.).

## Writing MDX Content (`.mdx`)

Create `.mdx` files, typically within `src/pages/` (to create pages) or `src/content/` (for Content Collections).

```mdx
---
# src/pages/posts/my-first-mdx-post.mdx
layout: ../../layouts/BlogPostLayout.astro # Apply a layout
title: My First MDX Post
pubDate: 2024-01-15
description: Exploring the power of MDX in Astro.
tags: ["astro", "mdx", "components"]

# Import components needed within the MDX content
import InteractiveCounter from '../../components/ReactCounter.jsx'; // React component
import Chart from '../../components/Chart.astro'; // Astro component
import Callout from '../../components/Callout.astro';
---
import { SITE_AUTHOR } from '../../config'; // Import JS variables

# {frontmatter.title}

*Published on: {new Date(frontmatter.pubDate).toLocaleDateString()} by {SITE_AUTHOR}*

This is an MDX file! It combines **Markdown** syntax with embedded JSX components.

<Callout type="info">
  You can use standard Markdown features like lists, links, and code blocks.
</Callout>

## Interactive Component Example

Here's a React counter component embedded directly:

<InteractiveCounter client:visible />

## Astro Component Example

You can also use `.astro` components:

<Chart data={[10, 40, 20, 50]} title="Sample Data" />

> MDX allows for richer content experiences compared to plain Markdown.

Remember to add `client:*` directives if your imported framework components need to be interactive on the client.
```

## Using MDX with Content Collections

MDX works seamlessly with Astro's Content Collections.

1.  **Schema (`src/content/config.ts`):** Define your collection with `type: 'content'`. The schema validates the MDX frontmatter.
2.  **Content Files:** Place `.mdx` files in the collection directory (e.g., `src/content/blog/`).
3.  **Querying:** Use `getCollection` or `getEntry` as usual.
4.  **Rendering:** Call `entry.render()` and use the returned `{ Content }` component in your Astro template. Astro automatically handles rendering the MDX content, including any imported components.

```astro
---
// src/pages/blog/[slug].astro (Example using Content Collections)
import { getCollection } from 'astro:content';
import BaseLayout from '../../layouts/BaseLayout.astro';

export async function getStaticPaths() {
  const posts = await getCollection('blog', ({ id }) => id.endsWith('.mdx')); // Filter for MDX files
  return posts.map((post) => ({
    params: { slug: post.slug },
    props: { entry: post },
  }));
}

const { entry } = Astro.props;
const { Content, headings } = await entry.render(); // Get Content component and headings
---
<BaseLayout pageTitle={entry.data.title}>
  <h1>{entry.data.title}</h1>
  <p>Published: {entry.data.pubDate.toDateString()}</p>

  {/* Optional: Render a Table of Contents */}
  <nav>
    <h2>On this page</h2>
    <ul>
      {headings.map(heading => (
        <li class={`depth-${heading.depth}`}>
          <a href={`#${heading.slug}`}>{heading.text}</a>
        </li>
      ))}
    </ul>
  </nav>

  <article>
    <Content /> {/* Render the MDX content */}
  </article>
</BaseLayout>
```

MDX provides a powerful way to author content in Astro, blending the ease of Markdown with the dynamic capabilities of components.

*(Refer to the official Astro MDX Integration documentation.)*