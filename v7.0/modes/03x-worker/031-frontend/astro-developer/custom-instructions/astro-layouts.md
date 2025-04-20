# Astro: Layouts

Creating reusable page structures using Astro layout components.

## Core Concept: Layout Components

Layout components are special `.astro` components located in the `src/layouts/` directory (by convention). Their primary purpose is to define the common structure (like HTML boilerplate, header, footer, navigation) shared across multiple pages. Pages then "wrap" themselves in a layout.

**Key Features:**

*   **Reusable Structure:** Define `<html>`, `<head>`, `<body>`, common headers, footers, navigation, etc., in one place.
*   **`<slot />` Element:** A placeholder within the layout's template where the content of the individual page using the layout will be injected.
*   **Props:** Layouts can accept props (defined in their script fence) just like regular components, allowing pages to pass data like page titles or metadata.
*   **Named Slots:** Use `<slot name="..." />` in the layout and the `slot="..."` attribute on elements within the page to inject content into specific named locations in the layout.

## Creating a Layout

```astro
---
// src/layouts/BaseLayout.astro
import Header from '../components/Header.astro';
import Footer from '../components/Footer.astro';
import '../styles/global.css'; // Import global styles

// Define props the layout accepts
interface Props {
	pageTitle: string;
	pageDescription?: string;
}
const { pageTitle, pageDescription = 'Default description' } = Astro.props;
---
<!doctype html>
<html lang="en">
	<head>
		<meta charset="UTF-8" />
		<meta name="description" content={pageDescription} />
		<meta name="viewport" content="width=device-width" />
		<link rel="icon" type="image/svg+xml" href="/favicon.svg" />
		<meta name="generator" content={Astro.generator} />
		<title>{pageTitle}</title>

    {/* Slot for additional head elements from the page */}
    <slot name="head" />
	</head>
	<body>
    <Header /> {/* Reusable header component */}

		<main>
      {/* Default slot: Page content goes here */}
			<slot />
		</main>

    <aside>
      {/* Named slot: Optional sidebar content from the page */}
      <slot name="sidebar" />
    </aside>

    <Footer /> {/* Reusable footer component */}

    {/* Example: Script common to all pages using this layout */}
    <script>
      console.log('Base layout script loaded');
    </script>
	</body>
</html>
```

## Using a Layout in a Page

**Method 1: `layout` Frontmatter Property (for `.md` and `.mdx` pages)**

*   In the frontmatter (YAML block at the top) of your Markdown or MDX file, specify the relative path to the layout component.
*   Props for the layout are passed directly in the frontmatter.

```markdown
---
# src/pages/about.md
layout: ../layouts/BaseLayout.astro
title: "About Us"
description: "Learn more about our company."
---
# About Us

This is the content of the about page. It will be injected into the default `<slot />`
of the `BaseLayout.astro` component.

The `title` and `description` frontmatter values are passed as props to the layout.
```

**Method 2: Importing and Wrapping (for `.astro` pages)**

*   Import the layout component in the page's script fence.
*   Wrap the page's content within the imported layout component tags in the template.
*   Pass props to the layout as attributes on the layout component tag.

```astro
---
// src/pages/contact.astro
import BaseLayout from '../layouts/BaseLayout.astro';
import ContactForm from '../components/ContactForm.astro';

const pageTitle = "Contact Us";
---
<BaseLayout pageTitle={pageTitle}>
  {/* Content here is passed to the default slot */}
  <h2>Get in Touch</h2>
  <p>Use the form below.</p>
  <ContactForm />

  {/* Content for named slots */}
  <Fragment slot="head">
    {/* Add specific meta tags or links for this page only */}
    <meta name="keywords" content="contact, form, support" />
  </Fragment>

  <div slot="sidebar">
    <h3>Contact Info</h3>
    <p>Phone: 123-456-7890</p>
  </div>
</BaseLayout>
```

Layouts are fundamental for maintaining consistency and reducing repetition across the pages of your Astro site.

*(Refer to the official Astro Layouts documentation.)*