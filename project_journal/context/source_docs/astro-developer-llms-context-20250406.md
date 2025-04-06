TITLE: Basic Astro Component Structure
DESCRIPTION: Shows the fundamental structure of an Astro component with a component script section and template section separated by code fence.

LANGUAGE: astro
CODE:
---
// Component Script (JavaScript)
---
<!-- Component Template (HTML + JS Expressions) -->

----------------------------------------

TITLE: Using TypeScript with Markdown Layouts in Astro
DESCRIPTION: This example demonstrates how to use TypeScript with Markdown layouts in Astro, including type definitions for frontmatter properties.

LANGUAGE: astro
CODE:
---
import type { MarkdownLayoutProps } from 'astro';

type Props = MarkdownLayoutProps<{
  // Define frontmatter props here
  title: string;
  author: string;
  date: string;
}>;

// Now, `frontmatter`, `url`, and other Markdown layout properties
// are accessible with type safety
const { frontmatter, url } = Astro.props;
---
<html>
  <head>
    <meta charset="utf-8">
    <link rel="canonical" href={new URL(url, Astro.site).pathname}>
    <title>{frontmatter.title}</title>
  </head>
  <body>
    <h1>{frontmatter.title} by {frontmatter.author}</h1>
    <slot />
    <p>Written on: {frontmatter.date}</p>
  </body>
</html>

----------------------------------------

TITLE: Fetching user session with Auth.js
DESCRIPTION: Retrieving the user's session information using Auth.js in an Astro component.

LANGUAGE: astro
CODE:
---
import Layout from 'src/layouts/Base.astro';
import { getSession } from 'auth-astro/server';

const session = await getSession(Astro.request);
---
<Layout>
  {
    session ? (
      <p>Welcome {session.user?.name}</p>
    ) : (
      <p>Not logged in</p>
    )
  }
</Layout>

----------------------------------------

TITLE: Slots Implementation
DESCRIPTION: Demonstrates the usage of named and default slots for content projection in Astro components.

LANGUAGE: astro
CODE:
---
import Header from './Header.astro';
import Logo from './Logo.astro';
import Footer from './Footer.astro';

const { title } = Astro.props;
---
<div id="content-wrapper">
  <Header />
  <slot name="after-header" />
  <Logo />
  <h1>{title}</h1>
  <slot />
  <Footer />
  <slot name="after-footer" />
</div>

----------------------------------------

TITLE: Creating Interactive Confetti Button Component in Astro
DESCRIPTION: Demonstrates how to create a button component that triggers a confetti animation using the canvas-confetti npm module and event listeners.

LANGUAGE: astro
CODE:
<button data-confetti-button>Celebrate!</button>

<script>
  // Import npm modules.
  import confetti from 'canvas-confetti';

  // Find our component DOM on the page.
  const buttons = document.querySelectorAll('[data-confetti-button]');

  // Add event listeners to fire confetti when a button is clicked.
  buttons.forEach((button) => {
    button.addEventListener('click', () => confetti());
  });
</script>

----------------------------------------

TITLE: Component Template Features
DESCRIPTION: Shows various features available in the component template including HTML, JavaScript expressions, and component imports.

LANGUAGE: astro
CODE:
---
import Banner from '../components/Banner.astro';
import Avatar from '../components/Avatar.astro';
import ReactPokemonComponent from '../components/ReactPokemonComponent.jsx';
const myFavoritePokemon = [/* ... */];
const { title } = Astro.props;
---
<!-- HTML comments supported! -->
{/* JS comment syntax is also valid! */}

<Banner />
<h1>Hello, world!</h1>

<p>{title}</p>

<Avatar server:defer>
  <svg slot="fallback" class="generic-avatar" transition:name="avatar">...</svg>
</Avatar>

<ReactPokemonComponent client:visible />

<ul>
  {myFavoritePokemon.map((data) => <li>{data.name}</li>)}
</ul>

<p class:list={["add", "dynamic", { classNames: true }]} />

----------------------------------------

TITLE: Custom Greeting Component with Data Attributes
DESCRIPTION: Creates a reusable greeting component that passes server-side variables to client-side JavaScript using data attributes.

LANGUAGE: astro
CODE:
---
const { message = 'Welcome, world!' } = Astro.props;
---

<astro-greet data-message={message}>
  <button>Say hi!</button>
</astro-greet>

<script>
  class AstroGreet extends HTMLElement {
    connectedCallback() {
      const message = this.dataset.message;
      const button = this.querySelector('button');
      button.addEventListener('click', () => {
        alert(message);
      });
    }
  }

  customElements.define('astro-greet', AstroGreet);
</script>

----------------------------------------

TITLE: Basic Middleware Implementation in Astro
DESCRIPTION: Creates a basic middleware function that intercepts requests and modifies locals object to share data across components.

LANGUAGE: javascript
CODE:
export function onRequest (context, next) {
    context.locals.title = "New title";
    return next();
};

----------------------------------------

TITLE: Interactive Framework Components with Hydration
DESCRIPTION: Shows different hydration patterns using client directives to make framework components interactive. Includes examples of load, visible, and client-only rendering strategies.

LANGUAGE: astro
CODE:
---
import InteractiveButton from '../components/InteractiveButton.jsx';
import InteractiveCounter from '../components/InteractiveCounter.jsx';
import InteractiveModal from '../components/InteractiveModal.svelte';
---
<!-- This component's JS will begin importing when the page loads -->
<InteractiveButton client:load />

<!-- This component's JS will not be sent to the client until
the user scrolls down and the component is visible on the page -->
<InteractiveCounter client:visible />

<!-- This component won't render on the server, but will render on the client when the page loads -->
<InteractiveModal client:only="svelte" />

----------------------------------------

TITLE: Creating a Basic Astro Layout Component
DESCRIPTION: This snippet demonstrates how to create a basic layout component in Astro, including a page shell, navigation, and a slot for content injection.

LANGUAGE: astro
CODE:
---
// src/layouts/MySiteLayout.astro
import BaseHead from '../components/BaseHead.astro';
import Footer from '../components/Footer.astro';
const { title } = Astro.props;
---
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <BaseHead title={title}/>
  </head>
  <body>
    <nav>
      <a href="#">Home</a>
      <a href="#">Posts</a>
      <a href="#">Contact</a>
    </nav>
    <h1>{title}</h1>
    <article>
      <slot /> <!-- your content is injected here -->
    </article>
    <Footer />
  </body>
  <style>
    h1 {
      font-size: 2rem;
    }
  </style>
</html>

----------------------------------------

TITLE: Fetching and Rendering Data in Astro Component
DESCRIPTION: This snippet demonstrates how to fetch data from an API in an Astro component, render it in HTML, and pass it to other components as props. It uses top-level await and the fetch API to make an HTTP request.

LANGUAGE: astro
CODE:
---
// src/components/User.astro
import Contact from "../components/Contact.jsx";
import Location from "../components/Location.astro";

const response = await fetch("https://randomuser.me/api/");
const data = await response.json();
const randomUser = data.results[0];
---
<!-- Data fetched at build can be rendered in HTML -->
<h1>User</h1>
<h2>{randomUser.name.first} {randomUser.name.last}</h2>

<!-- Data fetched at build can be passed to components as props -->
<Contact client:load email={randomUser.email} />
<Location city={randomUser.location.city} />

----------------------------------------

TITLE: Installing Astro via yarn
DESCRIPTION: Command to create a new Astro project using yarn.

LANGUAGE: bash
CODE:
# create a new project with yarn
yarn create astro

----------------------------------------

TITLE: Implementing Theme Toggle Functionality with JavaScript
DESCRIPTION: Client-side script that handles theme toggling, local storage management, and system preference detection.

LANGUAGE: javascript
CODE:
const theme = (() => {
  const localStorageTheme = localStorage?.getItem("theme") ?? '';
  if (['dark', 'light'].includes(localStorageTheme)) {
    return localStorageTheme;
  }
  if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
    return 'dark';
  }
    return 'light';
})();
        
if (theme === 'light') {
  document.documentElement.classList.remove('dark');
} else {
  document.documentElement.classList.add('dark');
}

window.localStorage.setItem('theme', theme);

const handleToggleClick = () => {
  const element = document.documentElement;
  element.classList.toggle("dark");
  
  const isDark = element.classList.contains("dark");
  localStorage.setItem("theme", isDark ? "dark" : "light");
}

document.getElementById("themeToggle")?.addEventListener("click", handleToggleClick);

----------------------------------------

TITLE: Installing Astro using npm
DESCRIPTION: Command to create a new Astro project using npm. This is part of the quick start guide for setting up an Astro project.

LANGUAGE: sh
CODE:
# create a new project with npm
npm create astro@latest

----------------------------------------

TITLE: Creating Better Auth client for React
DESCRIPTION: Setting up a Better Auth client for use with React in an Astro project.

LANGUAGE: typescript
CODE:
import { createAuthClient } from 'better-auth/react';

export const authClient = createAuthClient();

export const { signIn, signOut } = authClient;

----------------------------------------

TITLE: Defining an Astro Action
DESCRIPTION: Example of defining a basic Astro Action in the server object exported from src/actions/index.ts. It uses defineAction to create a getGreeting action with input validation and a handler function.

LANGUAGE: typescript
CODE:
import { defineAction } from 'astro:actions';
import { z } from 'astro:schema';

export const server = {
  getGreeting: defineAction({
    input: z.object({
      name: z.string(),
    }),
    handler: async (input) => {
      return `Hello, ${input.name}!`
    }
  })
}

----------------------------------------

TITLE: Importing Content Collection APIs in Astro
DESCRIPTION: Shows the main imports available from the astro:content module including utilities for collection definition, querying, and rendering.

LANGUAGE: javascript
CODE:
import { 
  z,
  defineCollection,
  getCollection,
  getEntry,
  getEntries,
  reference,
  render
 } from 'astro:content';

----------------------------------------

TITLE: Creating Base Layout Component in Astro
DESCRIPTION: Defines a basic layout component with header, footer, and global styles. Includes meta tags and script imports for a standard HTML page structure.

LANGUAGE: astro
CODE:
---
import Header from '../components/Header.astro';
import Footer from '../components/Footer.astro';
import '../styles/global.css';
const pageTitle = "Home Page";
---
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <meta name="viewport" content="width=device-width" />
    <meta name="generator" content={Astro.generator} />
    <title>{pageTitle}</title>
  </head>
  <body>
    <Header />
    <h1>{pageTitle}</h1>
    <Footer />
    <script>
      import "../scripts/menu.js";
    </script>
  </body>
</html>

----------------------------------------

TITLE: Defining Content Collections in TypeScript
DESCRIPTION: Example of defining content collections using the defineCollection function and specifying loaders and schemas.

LANGUAGE: typescript
CODE:
import { defineCollection, z } from 'astro:content';
import { glob, file } from 'astro/loaders';

const blog = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/data/blog" }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
  })
});

const dogs = defineCollection({
  loader: file("src/data/dogs.json"),
  schema: z.object({
    id: z.string(),
    breed: z.string(),
    temperament: z.array(z.string()),
  }),
});

export const collections = { blog, dogs };

----------------------------------------

TITLE: Adding Integrations to Astro Configuration
DESCRIPTION: This snippet demonstrates how to add integrations to an Astro project's configuration file. It shows three different ways to import and use integrations: from an installed npm package, from a local file, and as an inline object.

LANGUAGE: javascript
CODE:
// astro.config.mjs
import { defineConfig } from 'astro/config';
import installedIntegration from '@astrojs/vue';
import localIntegration from './my-integration.js';

export default defineConfig({
  integrations: [
    // 1. Imported from an installed npm package
    installedIntegration(),
    // 2. Imported from a local JS file
    localIntegration(),
    // 3. An inline object
    {name: 'namespace:id', hooks: { /* ... */ }},
  ]
});

----------------------------------------

TITLE: Defining Content Collections in TypeScript
DESCRIPTION: Example of defining content collections using the defineCollection function and specifying loaders and schemas.

LANGUAGE: typescript
CODE:
import { defineCollection, z } from 'astro:content';
import { glob, file } from 'astro/loaders';

const blog = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/data/blog" }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
  })
});

const dogs = defineCollection({
  loader: file("src/data/dogs.json"),
  schema: z.object({
    id: z.string(),
    breed: z.string(),
    temperament: z.array(z.string()),
  }),
});

export const collections = { blog, dogs };

----------------------------------------

TITLE: Defining Astro Configuration in JavaScript
DESCRIPTION: Demonstrates how to create and use the Astro configuration file (astro.config.mjs) to set project-wide options using the defineConfig helper function.

LANGUAGE: javascript
CODE:
// astro.config.mjs
import { defineConfig } from "astro/config";

export default defineConfig({
  // your configuration options here...
});

----------------------------------------

TITLE: Defining Content Collections in TypeScript
DESCRIPTION: Example of defining content collections using the defineCollection function and specifying loaders and schemas.

LANGUAGE: typescript
CODE:
import { defineCollection, z } from 'astro:content';
import { glob, file } from 'astro/loaders';

const blog = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/data/blog" }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
  })
});

const dogs = defineCollection({
  loader: file("src/data/dogs.json"),
  schema: z.object({
    id: z.string(),
    breed: z.string(),
    temperament: z.array(z.string()),
  }),
});

export const collections = { blog, dogs };

----------------------------------------

TITLE: Creating a Reusable Head Component in Astro
DESCRIPTION: Demonstrates how to create a reusable Head component in Astro for managing common metadata and SEO tags across multiple pages.

LANGUAGE: astro
CODE:
---
import Favicon from "../assets/Favicon.astro";
import SomeOtherTags from "./SomeOtherTags.astro";

const { title = "My Astro Website", ...props } = Astro.props;
---
<link rel="sitemap" href="/sitemap-index.xml">
<title>{title}</title>
<meta name="description" content="Welcome to my new Astro site!">

<!-- Web analytics -->
<script data-goatcounter="https://my-account.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>

<!-- Open Graph tags -->
<meta property="og:title" content="My New Astro Website" />
<meta property="og:type" content="website" />
<meta property="og:url" content="http://www.example.com/" />
<meta property="og:description" content="Welcome to my new Astro site!" />
<meta property="og:image" content="https://www.example.com/_astro/seo-banner.BZD7kegZ.webp">
<meta property="og:image:alt" content="">

<SomeOtherTags />

<Favicon />

----------------------------------------

TITLE: Initial Blocking Data Fetch Implementation
DESCRIPTION: Basic Astro page implementation that blocks rendering while awaiting data from two API endpoints. This approach delays the initial page render until all data is fetched.

LANGUAGE: astro
CODE:
---
const personResponse = await fetch('https://randomuser.me/api/');
const personData = await personResponse.json();
const randomPerson = personData.results[0];
const factResponse = await fetch('https://catfact.ninja/fact');
const factData = await factResponse.json();
---
<html>
  <head>
    <title>A name and a fact</title>
  </head>
  <body>
    <h2>A name</h2>
    <p>{randomPerson.name.first}</p>
    <h2>A fact</h2>
    <p>{factData.fact}</p>
  </body>
</html>

----------------------------------------

TITLE: Testing Astro Components with Container API
DESCRIPTION: Example of testing Astro components using the experimental Container API with Vitest.

LANGUAGE: javascript
CODE:
import { experimental_AstroContainer as AstroContainer } from 'astro/container';
import { expect, test } from 'vitest';
import Card from '../src/components/Card.astro';

test('Card with slots', async () => {
	const container = await AstroContainer.create();
	const result = await container.renderToString(Card, {
		slots: {
			default: 'Card content',
		},
	});

	expect(result).toContain('This is a card');
	expect(result).toContain('Card content');
});

----------------------------------------

TITLE: Installing Astro DB Integration
DESCRIPTION: Install the @astrojs/db integration using the astro add command.

LANGUAGE: bash
CODE:
npx astro add db

----------------------------------------

TITLE: Component Props with TypeScript
DESCRIPTION: Shows how to define and use props in an Astro component using TypeScript interfaces.

LANGUAGE: astro
CODE:
---
interface Props {
  name: string;
  greeting?: string;
}

const { greeting = "Hello", name } = Astro.props;
---
<h2>{greeting}, {name}!</h2>

----------------------------------------

TITLE: Server Island Component in Astro
DESCRIPTION: Demonstrates creation of a server island using the server:defer directive for parallel server-side rendering.

LANGUAGE: astro
CODE:
---
import Avatar from "../components/Avatar.astro";
---
<Avatar server:defer />

----------------------------------------

TITLE: Implementing Feedback Form Component
DESCRIPTION: Creates a form component with name, email, and message fields, including form submission handling and response display. Available in multiple UI frameworks including React, Preact, Solid, Vue, and Svelte.

LANGUAGE: tsx
CODE:
import { useState } from "react";
import type { FormEvent } from "react";

export default function Form() {
  const [responseMessage, setResponseMessage] = useState("");

  async function submit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    const formData = new FormData(e.target as HTMLFormElement);
    const response = await fetch("/api/feedback", {
      method: "POST",
      body: formData,
    });
    const data = await response.json();
    if (data.message) {
      setResponseMessage(data.message);
    }
  }

  return (
    <form onSubmit={submit}>
      <label htmlFor="name">
        Name
        <input type="text" id="name" name="name" autoComplete="name" required />
      </label>
      <label htmlFor="email">
        Email
        <input type="email" id="email" name="email" autoComplete="email" required />
      </label>
      <label htmlFor="message">
        Message
        <textarea id="message" name="message" autoComplete="off" required />
      </label>
      <button>Send</button>
      {responseMessage && <p>{responseMessage}</p>}
    </form>
  );
}

----------------------------------------

TITLE: Defining Astro DB Tables in TypeScript
DESCRIPTION: Shows how to define database tables using the defineTable() and column utilities from astro:db. This example configures a Comment table with required text columns for author and body.

LANGUAGE: typescript
CODE:
import { defineDb, defineTable, column } from 'astro:db';

const Comment = defineTable({
  columns: {
    author: column.text(),
    body: column.text(),
  }
})

export default defineDb({
  tables: { Comment },
})

----------------------------------------

TITLE: Inserting Data in Astro DB
DESCRIPTION: Insert data into database tables using form submissions or Astro actions.

LANGUAGE: astro
CODE:
---
import { db, Comment } from 'astro:db';

if (Astro.request.method === 'POST') {
  const formData = await Astro.request.formData();
  const author = formData.get('author');
  const body = formData.get('body');
  if (typeof author === 'string' && typeof body === 'string') {
    await db.insert(Comment).values({ author, body });
  }
}

const comments = await db.select().from(Comment);
---

<form method="POST" style="display: grid">
	<label for="author">Author</label>
	<input id="author" name="author" />

	<label for="body">Body</label>
	<textarea id="body" name="body"></textarea>

	<button type="submit">Submit</button>
</form>

<!-- Render `comments` -->

----------------------------------------

TITLE: Accessing Markdown Content in Astro Components
DESCRIPTION: Example showing how to import and display Markdown content in Astro components using dynamic expressions and file imports.

LANGUAGE: markdown
CODE:
---
title: 'The greatest post of all time'
author: 'Ben'
---

Here is my _great_ post!

LANGUAGE: astro
CODE:
---
import * as greatPost from './posts/great-post.md';
const posts = Object.values(import.meta.glob('./posts/*.md', { eager: true }));
---

<p>{greatPost.frontmatter.title}</p>
<p>Written by: {greatPost.frontmatter.author}</p>

<p>Post Archive:</p>
<ul>
  {posts.map(post => <li><a href={post.url}>{post.frontmatter.title}</a></li>)}
</ul>

----------------------------------------

TITLE: Dynamic Multi-Level Page Generation
DESCRIPTION: Example of generating multiple pages at different URL depths using rest parameters and props.

LANGUAGE: astro
CODE:
---
export function getStaticPaths() {
  const pages = [
    {
      slug: undefined,
      title: "Astro Store",
      text: "Welcome to the Astro store!",
    },
    {
      slug: "products",
      title: "Astro products",
      text: "We have lots of products for you",
    },
    {
      slug: "products/astro-handbook",
      title: "The ultimate Astro handbook",
      text: "If you want to learn Astro, you must read this book.",
    },
  ];
  
  return pages.map(({ slug, title, text }) => {
    return {
      params: { slug },
      props: { title, text },
    };
  });
}

const { title, text } = Astro.props;
---
<html>
  <head>
    <title>{title}</title>
  </head>
  <body>
    <h1>{title}</h1>
    <p>{text}</p>
  </body>
</html>

----------------------------------------

TITLE: Implementing Server-Side Validation in Astro
DESCRIPTION: This snippet shows comprehensive server-side validation for the registration form. It checks for valid input, performs database checks, and handles error messages.

LANGUAGE: astro
CODE:
---
import { isRegistered, registerUser } from "../../data/users"
import { isValidEmail } from "../../utils/isValidEmail";

const errors = { username: "", email: "", password: "" };
if (Astro.request.method === "POST") {
  try {
    const data = await Astro.request.formData();
    const name = data.get("username");
    const email = data.get("email");
    const password = data.get("password");
    if (typeof name !== "string" || name.length < 1) {
      errors.username += "Please enter a username. ";
    }
    if (typeof email !== "string" || !isValidEmail(email)) {
      errors.email += "Email is not valid. ";
    } else if (await isRegistered(email)) {
      errors.email += "Email is already registered. ";
    }
    if (typeof password !== "string" || password.length < 6) {
      errors.password += "Password must be at least 6 characters. ";
    }
    const hasErrors = Object.values(errors).some(msg => msg)
    if (!hasErrors) {
      await registerUser({name, email, password});
      return Astro.redirect("/login");
    }
  } catch (error) {
    if (error instanceof Error) {
      console.error(error.message);
    }
  }
}
---

----------------------------------------

TITLE: Using an Astro Layout Component
DESCRIPTION: This snippet shows how to use a layout component in an Astro page file, wrapping the page content within the layout.

LANGUAGE: astro
CODE:
---
import MySiteLayout from '../layouts/MySiteLayout.astro';
---
<MySiteLayout title="Home Page">
  <p>My page content, wrapped in a layout!</p>
</MySiteLayout>