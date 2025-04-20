# Astro: File-Based Routing & Dynamic Routes

Understanding how Astro creates page routes from files in `src/pages/`.

## Core Concept: File-Based Routing

Astro uses a strategy called **file-based routing**. Every `.astro`, `.md`, `.mdx` file located inside the `src/pages/` directory automatically becomes a page or endpoint on your site. The URL path of the page directly corresponds to the file path relative to `src/pages/`.

**Examples:**

*   `src/pages/index.astro`       -> `/`
*   `src/pages/about.astro`       -> `/about`
*   `src/pages/contact.md`        -> `/contact`
*   `src/pages/blog/index.astro`  -> `/blog`
*   `src/pages/blog/first-post.mdx` -> `/blog/first-post`

This makes creating new pages simple: just add a file to the `src/pages/` directory.

## Dynamic Routing

Often, you need to create pages based on dynamic data, like blog posts, product details, or user profiles, where the URL includes a parameter (e.g., `/posts/[slug]`, `/products/[id]`). Astro handles this using dynamic route parameters in filenames.

**1. Single Parameter (`[param].astro`):**

*   **Filename:** Use square brackets `[]` around a parameter name (e.g., `[slug].astro`, `[id].astro`).
*   **`getStaticPaths()` (Required for SSG):** In Static Site Generation (SSG) mode (default), you **must** export an async function called `getStaticPaths` from the dynamic route file. This function tells Astro which specific paths to pre-render at build time.
    *   It must return an array of objects, where each object has:
        *   `params`: An object containing the values for the dynamic parameters in the filename (e.g., `{ slug: 'post-1' }`).
        *   `props` (Optional): An object containing additional data to be passed as props to the page component for that specific path.
*   **Accessing Params (`Astro.params`):** Inside the `.astro` component (in the script fence or template), access the matched parameter values using `Astro.params`.

```astro
---
// src/pages/posts/[slug].astro
import BaseLayout from '../../layouts/BaseLayout.astro';
import { getCollection } from 'astro:content'; // Example: Fetching from content collections

// Required for SSG: Define which paths to generate
export async function getStaticPaths() {
  const blogPosts = await getCollection('blog'); // Fetch all blog entries
  return blogPosts.map(post => ({
    params: { slug: post.slug }, // The 'slug' matches the [slug] filename part
    props: { postData: post.data, body: post.body }, // Pass post data as props
  }));
}

// Access props passed from getStaticPaths
const { postData, body } = Astro.props;
// Access the 'slug' parameter from the URL
const { slug } = Astro.params;
---
<BaseLayout pageTitle={postData.title}>
  <h1>{postData.title}</h1>
  <p>Published on: {postData.pubDate.toDateString()}</p>
  <p>Slug: {slug}</p>
  <hr />
  {/* Render Markdown/MDX body if applicable */}
  <Fragment set:html={body} /> {/* Example for Markdown, MDX might use <Content /> */}
</BaseLayout>
```

**2. Rest Parameters (`[...rest].astro`):**

*   **Filename:** Use square brackets with three dots `[...]` around a parameter name (e.g., `[...path].astro`, `[...slugs].astro`). This matches *multiple* path segments.
*   **`getStaticPaths()`:** The `params` object should contain the rest parameter name as a key, with its value being the full path string (e.g., `{ path: 'a/b/c' }`) or `undefined` for the root match within the directory.
*   **Accessing Params (`Astro.params`):** `Astro.params.rest` (or whatever name you used) will contain the matched path string (e.g., `'a/b/c'`).

```astro
---
// src/pages/files/[...path].astro
// Matches /files/a, /files/a/b, /files/a/b/c, etc.
import BaseLayout from '../../layouts/BaseLayout.astro';

export async function getStaticPaths() {
  // Example: Generate paths based on some file structure logic
  return [
    { params: { path: 'a/b' }, props: { content: 'Content for a/b' } },
    { params: { path: 'x/y/z' }, props: { content: 'Content for x/y/z' } },
    { params: { path: undefined }, props: { content: 'Content for /files root' } } // Root match
  ];
}

const { path } = Astro.params;
const { content } = Astro.props;
---
<BaseLayout pageTitle={`File: ${path ?? 'Root'}`}>
  <h1>Path: /{path ?? ''}</h1>
  <p>{content}</p>
</BaseLayout>
```

**3. SSR Mode:**

*   In Server-Side Rendering (SSR) mode, `getStaticPaths` is **not** required or used.
*   Dynamic routes are matched on the server at request time.
*   You still access parameters via `Astro.params`.
*   You typically fetch data needed for the page directly within the component script using `Astro.params`.

```astro
---
// src/pages/products/[id].astro (Running in SSR mode)
import BaseLayout from '../../layouts/BaseLayout.astro';
// Assume fetchProductById is a function to get product data
import { fetchProductById } from '../../api/products';

// No getStaticPaths needed in SSR

const { id } = Astro.params;
const product = await fetchProductById(id); // Fetch data at request time

if (!product) {
  // Handle product not found, e.g., return a 404 response
  return new Response(null, { status: 404, statusText: 'Not Found' });
}
---
<BaseLayout pageTitle={product.name}>
  <h1>{product.name}</h1>
  <p>Price: ${product.price}</p>
  <p>{product.description}</p>
</BaseLayout>
```

Astro's file-based routing, combined with dynamic route parameters and `getStaticPaths` (for SSG), provides a flexible way to structure site navigation and generate pages from data.

*(Refer to the official Astro Routing documentation.)*