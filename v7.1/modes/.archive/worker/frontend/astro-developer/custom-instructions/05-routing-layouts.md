# Astro: Routing & Layouts

## 1. File-Based Routing

Astro uses a strategy called **file-based routing**. Every `.astro`, `.md`, `.mdx` file located inside the `src/pages/` directory automatically becomes a page or endpoint on your site. The URL path corresponds to the file path.

**Examples:**

*   `src/pages/index.astro`       -> `/`
*   `src/pages/about.astro`       -> `/about`
*   `src/pages/blog/index.astro`  -> `/blog`
*   `src/pages/blog/first-post.mdx` -> `/blog/first-post`

## 2. Dynamic Routing

Create pages based on dynamic data (e.g., blog posts, products) using parameters in filenames.

**a) Single Parameter (`[param].astro`):**

*   **Filename:** Use `[]` (e.g., `[slug].astro`).
*   **`getStaticPaths()` (Required for SSG):** Export this async function to define paths to pre-render. It returns an array of objects: `{ params: { slug: 'value' }, props: { ... } }`.
*   **Accessing Params:** Use `Astro.params` (e.g., `Astro.params.slug`).

```astro
---
// src/pages/posts/[slug].astro
import { getCollection } from 'astro:content';

export async function getStaticPaths() {
  const blogPosts = await getCollection('blog');
  return blogPosts.map(post => ({
    params: { slug: post.slug },
    props: { postData: post.data, body: post.body },
  }));
}

const { postData, body } = Astro.props;
const { slug } = Astro.params;
---
<!-- Use postData, body, slug -->
```

**b) Rest Parameters (`[...rest].astro`):**

*   **Filename:** Use `[...]` (e.g., `[...path].astro`). Matches multiple segments.
*   **`getStaticPaths()`:** `params` value is the full path string (e.g., `{ path: 'a/b/c' }`) or `undefined` for root match.
*   **Accessing Params:** `Astro.params.rest` contains the matched path string.

```astro
---
// src/pages/files/[...path].astro
export async function getStaticPaths() {
  return [
    { params: { path: 'a/b' }, props: { content: '...' } },
    { params: { path: undefined }, props: { content: '...' } } // Root match
  ];
}
const { path } = Astro.params; // 'a/b' or undefined
---
<!-- Use path -->
```

**c) SSR Mode:**

*   `getStaticPaths` is **not** used.
*   Routes are matched at request time.
*   Access params via `Astro.params`. Fetch data directly in the component script.

```astro
---
// src/pages/products/[id].astro (SSR mode)
import { fetchProductById } from '../../api/products';
const { id } = Astro.params;
const product = await fetchProductById(id);
if (!product) { return new Response(null, { status: 404 }); }
---
<!-- Use product -->
```

## 3. Layouts (`src/layouts/`)

Layout components (`.astro` files in `src/layouts/`) define reusable page structures.

**Creating a Layout:**

```astro
---
// src/layouts/BaseLayout.astro
import Header from '../components/Header.astro';
import Footer from '../components/Footer.astro';
interface Props { pageTitle: string; }
const { pageTitle } = Astro.props;
---
<!doctype html>
<html lang="en">
<head>
  <title>{pageTitle}</title>
  <slot name="head" /> {/* Named slot for extra head elements */}
</head>
<body>
  <Header />
  <main>
    <slot /> {/* Default slot for page content */}
  </main>
  <Footer />
</body>
</html>
```

**Using a Layout:**

**a) `.md` / `.mdx` Pages:** Use `layout` frontmatter property. Props are passed from frontmatter.

```markdown
---
# src/pages/about.md
layout: ../layouts/BaseLayout.astro
pageTitle: "About Us"
---
Page content goes here...
```

**b) `.astro` Pages:** Import and wrap content. Pass props as attributes.

```astro
---
// src/pages/contact.astro
import BaseLayout from '../layouts/BaseLayout.astro';
---
<BaseLayout pageTitle="Contact Us">
  {/* Default slot content */}
  <h2>Get in Touch</h2>

  {/* Named slot content */}
  <Fragment slot="head">
    <meta name="keywords" content="contact" />
  </Fragment>
</BaseLayout>
```

*(Refer to the official Astro Routing and Layouts documentation.)*