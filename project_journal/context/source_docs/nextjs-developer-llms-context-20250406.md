TITLE: Manual Installation of Next.js Dependencies
DESCRIPTION: Manually install the required packages for a Next.js application using npm. This includes next, react, and react-dom.

LANGUAGE: bash
CODE:
npm install next@latest react@latest react-dom@latest

----------------------------------------

TITLE: Cached GET Request Handler with External API
DESCRIPTION: Example of a cached Route Handler fetching data from MongoDB API with force-static configuration.

LANGUAGE: typescript
CODE:
export const dynamic = 'force-static'

export async function GET() {
  const res = await fetch('https://data.mongodb-api.com/...', {
    headers: {
      'Content-Type': 'application/json',
      'API-Key': process.env.DATA_API_KEY,
    },
  })
  const data = await res.json()

  return Response.json({ data })
}

----------------------------------------

TITLE: Using Local Images with Next.js Image Component
DESCRIPTION: Shows how to use local images with the Next.js Image component. It imports the image file and automatically provides width, height, and blurDataURL properties.

LANGUAGE: tsx
CODE:
import Image from 'next/image'
import profilePic from './me.png'

export default function Page() {
  return (
    <Image
      src={profilePic}
      alt="Picture of the author"
      // width={500} automatically provided
      // height={500} automatically provided
      // blurDataURL="data:..." automatically provided
      // placeholder="blur" // Optional blur-up while loading
    />
  )
}

LANGUAGE: jsx
CODE:
import Image from 'next/image'
import profilePic from './me.png'

export default function Page() {
  return (
    <Image
      src={profilePic}
      alt="Picture of the author"
      // width={500} automatically provided
      // height={500} automatically provided
      // blurDataURL="data:..." automatically provided
      // placeholder="blur" // Optional blur-up while loading
    />
  )
}

----------------------------------------

TITLE: Fetching Blog Posts with getStaticProps in Next.js
DESCRIPTION: This example demonstrates how to fetch a list of blog posts from a CMS using getStaticProps. It shows both TypeScript and JavaScript versions of the code, illustrating how to pass the fetched data as props to the page component.

LANGUAGE: typescript
CODE:
// posts will be populated at build time by getStaticProps()
export default function Blog({ posts }) {
  return (
    <ul>
      {posts.map((post) => (
        <li>{post.title}</li>
      ))}
    </ul>
  )
}

// This function gets called at build time on server-side.
// It won't be called on client-side, so you can even do
// direct database queries.
export async function getStaticProps() {
  // Call an external API endpoint to get posts.
  // You can use any data fetching library
  const res = await fetch('https://.../posts')
  const posts = await res.json()

  // By returning { props: { posts } }, the Blog component
  // will receive `posts` as a prop at build time
  return {
    props: {
      posts,
    },
  }
}

LANGUAGE: javascript
CODE:
// posts will be populated at build time by getStaticProps()
export default function Blog({ posts }) {
  return (
    <ul>
      {posts.map((post) => (
        <li>{post.title}</li>
      ))}
    </ul>
  )
}

// This function gets called at build time on server-side.
// It won't be called on client-side, so you can even do
// direct database queries.
export async function getStaticProps() {
  // Call an external API endpoint to get posts.
  // You can use any data fetching library
  const res = await fetch('https://.../posts')
  const posts = await res.json()

  // By returning { props: { posts } }, the Blog component
  // will receive `posts` as a prop at build time
  return {
    props: {
      posts,
    },
  }
}

----------------------------------------

TITLE: Form Validation with Server Actions
DESCRIPTION: Example of implementing server-side form validation using zod with Server Actions.

LANGUAGE: typescript
CODE:
'use server'

import { z } from 'zod'

const schema = z.object({
  email: z.string({
    invalid_type_error: 'Invalid Email',
  }),
})

export default async function createUser(formData: FormData) {
  const validatedFields = schema.safeParse({
    email: formData.get('email'),
  })

  if (!validatedFields.success) {
    return {
      errors: validatedFields.error.flatten().fieldErrors,
    }
  }

  // Mutate data
}

----------------------------------------

TITLE: Implementing a Client-Side Counter Component in Next.js
DESCRIPTION: This snippet demonstrates how to create a Client Component in Next.js using the 'use client' directive. It implements a simple counter with state management and event handling, showcasing the interactivity possible with Client Components.

LANGUAGE: typescript
CODE:
'use client'

import { useState } from 'react'

export default function Counter() {
  const [count, setCount] = useState(0)

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>Click me</button>
    </div>
  )
}

LANGUAGE: javascript
CODE:
'use client'

import { useState } from 'react'

export default function Counter() {
  const [count, setCount] = useState(0)

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>Click me</button>
    </div>
  )
}

----------------------------------------

TITLE: Server-Side Data Fetching with ORM or Database in Next.js
DESCRIPTION: Shows how to fetch data on the server using an ORM or database. The component queries a database for blog posts and renders them in an unordered list. The response is not cached by default.

LANGUAGE: tsx
CODE:
import { db, posts } from '@/lib/db'

export default async function Page() {
  const allPosts = await db.select().from(posts)
  return (
    <ul>
      {allPosts.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  )
}

----------------------------------------

TITLE: Implementing a Root Layout in Next.js
DESCRIPTION: This snippet shows how to create a required root layout for a Next.js application. The root layout applies to all routes and must contain html and body tags. It's used to modify the initial HTML returned from the server.

LANGUAGE: typescript
CODE:
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>
        {/* Layout UI */}
        <main>{children}</main>
      </body>
    </html>
  )
}

LANGUAGE: javascript
CODE:
export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        {/* Layout UI */}
        <main>{children}</main>
      </body>
    </html>
  )
}

----------------------------------------

TITLE: Configuring Static Export in Next.js Configuration
DESCRIPTION: This snippet shows how to enable static export mode in the Next.js configuration file. It demonstrates setting the output mode to 'export' and includes optional configuration for trailing slashes and output directory.

LANGUAGE: javascript
CODE:
/**
 * @type {import('next').NextConfig}
 */
const nextConfig = {
  output: 'export',

  // Optional: Change links `/me` -> `/me/` and emit `/me.html` -> `/me/index.html`
  // trailingSlash: true,

  // Optional: Prevent automatic `/me` -> `/me/`, instead preserve `href`
  // skipTrailingSlashRedirect: true,

  // Optional: Change the output directory `out` -> `dist`
  // distDir: 'dist',
}

module.exports = nextConfig

----------------------------------------

TITLE: Generating Static Params for Dynamic Routes in Next.js
DESCRIPTION: This code snippet shows how to use the generateStaticParams function to statically generate routes at build time for dynamic segments. It fetches posts data and maps it to generate slug parameters.

LANGUAGE: typescript
CODE:
export async function generateStaticParams() {
  const posts = await fetch('https://.../posts').then((res) => res.json())

  return posts.map((post) => ({
    slug: post.slug,
  }))
}

LANGUAGE: jsx
CODE:
export async function generateStaticParams() {
  const posts = await fetch('https://.../posts').then((res) => res.json())

  return posts.map((post) => ({
    slug: post.slug,
  }))
}

----------------------------------------

TITLE: Basic Server-Side Data Fetching in Next.js
DESCRIPTION: Demonstrates a simple server-side data fetch using the fetch API in an asynchronous React Server Component. The component fetches blog posts and renders them in an unordered list.

LANGUAGE: tsx
CODE:
export default async function Page() {
  const data = await fetch('https://api.vercel.app/blog')
  const posts = await data.json()
  return (
    <ul>
      {posts.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  )
}

----------------------------------------

TITLE: Installing Next.js with create-next-app
DESCRIPTION: Use the create-next-app CLI to automatically set up a new Next.js project. This command initiates the installation process and prompts for project configuration options.

LANGUAGE: bash
CODE:
npx create-next-app@latest

----------------------------------------

TITLE: Handling Expected Errors in Server Components (TypeScript)
DESCRIPTION: This snippet demonstrates how to handle expected errors when fetching data inside a Server Component using TypeScript. It shows conditional rendering based on the response status.

LANGUAGE: typescript
CODE:
export default async function Page() {
  const res = await fetch(`https://...`)
  const data = await res.json()

  if (!res.ok) {
    return 'There was an error.'
  }

  return '...'
}

----------------------------------------

TITLE: Next.js Link Component Usage
DESCRIPTION: Demonstrates how to use the built-in Link component for client-side navigation between routes. The Link component extends the HTML anchor tag with prefetching capabilities.

LANGUAGE: typescript
CODE:
import Link from 'next/link'

export default function Page() {
  return <Link href="/dashboard">Dashboard</Link>
}

LANGUAGE: javascript
CODE:
import Link from 'next/link'

export default function Page() {
  return <Link href="/dashboard">Dashboard</Link>
}

----------------------------------------

TITLE: Implementing Error Boundary Component in Next.js (TypeScript)
DESCRIPTION: Creates a client-side error boundary component that handles runtime errors and provides a fallback UI with error logging and reset functionality. Uses TypeScript with proper type definitions for error and reset props.

LANGUAGE: tsx
CODE:
'use client' // Error boundaries must be Client Components

import { useEffect } from 'react'

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string }
  reset: () => void
}) {
  useEffect(() => {
    // Log the error to an error reporting service
    console.error(error)
  }, [error])

  return (
    <div>
      <h2>Something went wrong!</h2>
      <button
        onClick={
          // Attempt to recover by trying to re-render the segment
          () => reset()
        }
      >
        Try again
      </button>
    </div>
  )
}

----------------------------------------

TITLE: Using Authorization Header in Next.js API Request
DESCRIPTION: Example showing how to forward an authorization header from an incoming request to another API fetch call within a Next.js Server Component.

LANGUAGE: javascript
CODE:
import { headers } from 'next/headers'

export default async function Page() {
  const authorization = (await headers()).get('authorization')
  const res = await fetch('...', {
    headers: { authorization }, // Forward the authorization header
  })
  const user = await res.json()

  return <h1>{user.name}</h1>
}

----------------------------------------

TITLE: Implementing Modal with Parallel Routes
DESCRIPTION: Example of using parallel routes to create a modal component with deep linking support.

LANGUAGE: typescript
CODE:
'use client'

import { useRouter } from 'next/navigation'

export function Modal({ children }: { children: React.ReactNode }) {
  const router = useRouter()

  return (
    <>
      <button
        onClick={() => {
          router.back()
        }}
      >
        Close modal
      </button>
      <div>{children}</div>
    </>
  )
}

----------------------------------------

TITLE: Configuring VS Code Debugging for Next.js
DESCRIPTION: This JSON configuration sets up debugging tasks for Next.js in VS Code. It includes configurations for server-side debugging, client-side debugging (Chrome and Firefox), and full-stack debugging.

LANGUAGE: json
CODE:
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Next.js: debug server-side",
      "type": "node-terminal",
      "request": "launch",
      "command": "npm run dev"
    },
    {
      "name": "Next.js: debug client-side",
      "type": "chrome",
      "request": "launch",
      "url": "http://localhost:3000"
    },
    {
      "name": "Next.js: debug client-side (Firefox)",
      "type": "firefox",
      "request": "launch",
      "url": "http://localhost:3000",
      "reAttach": true,
      "pathMappings": [
        {
          "url": "webpack://_N_E",
          "path": "${workspaceFolder}"
        }
      ]
    },
    {
      "name": "Next.js: debug full stack",
      "type": "node",
      "request": "launch",
      "program": "${workspaceFolder}/node_modules/.bin/next",
      "runtimeArgs": ["--inspect"],
      "skipFiles": ["<node_internals>/**"],
      "serverReadyAction": {
        "action": "debugWithEdge",
        "killOnServerStop": true,
        "pattern": "- Local:.+(https?://.+)",
        "uriFormat": "%s",
        "webRoot": "${workspaceFolder}"
      }
    }
  ]
}

----------------------------------------

TITLE: Installing Next.js with create-next-app
DESCRIPTION: Use the create-next-app CLI to automatically set up a new Next.js project. This command initiates the installation process and prompts for project configuration options.

LANGUAGE: bash
CODE:
npx create-next-app@latest

----------------------------------------

TITLE: Implementing Sign-up Form in Next.js
DESCRIPTION: Example of a sign-up form component using Server Actions in Next.js. It demonstrates how to capture user credentials and handle form submission.

LANGUAGE: tsx
CODE:
import { signup } from '@/app/actions/auth'

export function SignupForm() {
  return (
    <form action={signup}>
      <div>
        <label htmlFor="name">Name</label>
        <input id="name" name="name" placeholder="Name" />
      </div>
      <div>
        <label htmlFor="email">Email</label>
        <input id="email" name="email" type="email" placeholder="Email" />
      </div>
      <div>
        <label htmlFor="password">Password</label>
        <input id="password" name="password" type="password" />
      </div>
      <button type="submit">Sign Up</button>
    </form>
  )
}

----------------------------------------

TITLE: create-next-app CLI Options for Non-interactive Setup
DESCRIPTION: Comprehensive list of command-line options for create-next-app, allowing non-interactive project setup with specific configurations such as TypeScript, Tailwind CSS, ESLint, and more.

LANGUAGE: bash
CODE:
Usage: create-next-app [project-directory] [options]

Options:
  -V, --version                        output the version number
  --ts, --typescript

    Initialize as a TypeScript project. (default)

  --js, --javascript

    Initialize as a JavaScript project.

  --tailwind

    Initialize with Tailwind CSS config. (default)

  --eslint

    Initialize with ESLint config.

  --app

    Initialize as an App Router project.

  --src-dir

    Initialize inside a `src/` directory.

  --turbopack

    Enable Turbopack by default for development.

  --import-alias <alias-to-configure>

    Specify import alias to use (default "@/*").

  --empty

    Initialize an empty project.

  --use-npm

    Explicitly tell the CLI to bootstrap the application using npm

  --use-pnpm

    Explicitly tell the CLI to bootstrap the application using pnpm

  --use-yarn

    Explicitly tell the CLI to bootstrap the application using Yarn

  --use-bun

    Explicitly tell the CLI to bootstrap the application using Bun

  -e, --example [name]|[github-url]

    An example to bootstrap the app with. You can use an example name
    from the official Next.js repo or a GitHub URL. The URL can use
    any branch and/or subdirectory

  --example-path <path-to-example>

    In a rare case, your GitHub URL might contain a branch name with
    a slash (e.g. bug/fix-1) and the path to the example (e.g. foo/bar).
    In this case, you must specify the path to the example separately:
    --example-path foo/bar

  --reset-preferences

    Explicitly tell the CLI to reset any stored preferences

  --skip-install

    Explicitly tell the CLI to skip installing packages

  --disable-git

    Explicitly tell the CLI to skip initializing a git repository.

  --yes

    Use previous preferences or defaults for all options that were not
    explicitly specified, without prompting.

  -h, --help                           display help for command

----------------------------------------

TITLE: Implementing Dynamic Routes in Next.js
DESCRIPTION: This code snippet demonstrates how to create a dynamic route for a blog post using the [slug] parameter. It shows how to access the dynamic segment value from the params prop in both TypeScript and JavaScript.

LANGUAGE: typescript
CODE:
export default async function Page({
  params,
}: {
  params: Promise<{ slug: string }>
}) {
  const { slug } = await params
  return <div>My Post: {slug}</div>
}

LANGUAGE: jsx
CODE:
export default async function Page({ params }) {
  const { slug } = await params
  return <div>My Post: {slug}</div>
}

----------------------------------------

TITLE: Passing Server Components to Client Components as Props
DESCRIPTION: Demonstrates the supported pattern of passing Server Components as props to Client Components, using the children prop as an example.

LANGUAGE: typescript
CODE:
'use client'

import { useState } from 'react'

export default function ClientComponent({
  children,
}: {
  children: React.ReactNode
}) {
  const [count, setCount] = useState(0)

  return (
    <>
      <button onClick={() => setCount(count + 1)}>{count}</button>
      {children}
    </>
  )
}

----------------------------------------

TITLE: Implementing Streaming with Suspense in Next.js
DESCRIPTION: This snippet shows how to implement streaming using React's Suspense component in a Next.js page. It allows for granular control over which parts of the page are streamed, improving initial load time and user experience.

LANGUAGE: tsx
CODE:
import { Suspense } from 'react'
import BlogList from '@/components/BlogList'
import BlogListSkeleton from '@/components/BlogListSkeleton'

export default function BlogPage() {
  return (
    <div>
      {/* This content will be sent to the client immediately */}
      <header>
        <h1>Welcome to the Blog</h1>
        <p>Read the latest posts below.</p>
      </header>
      <main>
        {/* Any content wrapped in a <Suspense> boundary will be streamed */}
        <Suspense fallback={<BlogListSkeleton />}>
          <BlogList />
        </Suspense>
      </main>
    </div>
  )
}

LANGUAGE: jsx
CODE:
import { Suspense } from 'react'
import BlogList from '@/components/BlogList'
import BlogListSkeleton from '@/components/BlogListSkeleton'

export default function BlogPage() {
  return (
    <div>
      {/* This content will be sent to the client immediately */}
      <header>
        <h1>Welcome to the Blog</h1>
        <p>Read the latest posts below.</p>
      </header>
      <main>
        {/* Any content wrapped in a <Suspense> boundary will be streamed */}
        <Suspense fallback={<BlogListSkeleton />}>
          <BlogList />
        </Suspense>
      </main>
    </div>
  )
}

----------------------------------------

TITLE: Basic Server Action in Server Component
DESCRIPTION: Demonstrates how to create a basic Server Action within a Server Component using the 'use server' directive.

LANGUAGE: typescript
CODE:
export default function Page() {
  async function create() {
    'use server'
    // Mutate data
  }

  return '...'
}

----------------------------------------

TITLE: Importing CSS Module in Next.js App Router
DESCRIPTION: This snippet demonstrates how to import and use a CSS Module in a Next.js app using the App Router. It shows the usage of the styles object to apply scoped CSS classes.

LANGUAGE: tsx
CODE:
import styles from './styles.module.css'

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return <section className={styles.dashboard}>{children}</section>
}

LANGUAGE: css
CODE:
.dashboard {
  padding: 24px;
}

----------------------------------------

TITLE: Using revalidatePath in a Next.js Server Action
DESCRIPTION: This example shows how to use revalidatePath within a server action. It defines an async function that submits a form and then revalidates the root path.

LANGUAGE: ts
CODE:
'use server'

import { revalidatePath } from 'next/cache'

export default async function submit() {
  await submitForm()
  revalidatePath('/')
}

----------------------------------------

TITLE: Defining a Dashboard Layout in Next.js
DESCRIPTION: This snippet demonstrates how to create a basic layout component for a dashboard in Next.js. It accepts children as a prop and wraps them in a section element.

LANGUAGE: tsx
CODE:
export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return <section>{children}</section>
}

LANGUAGE: jsx
CODE:
export default function DashboardLayout({ children }) {
  return <section>{children}</section>
}

----------------------------------------

TITLE: Importing and Using next/image Component in Next.js
DESCRIPTION: This snippet demonstrates how to import and use the Image component from next/image in a Next.js application. It shows how to use local images with automatic size detection.

LANGUAGE: jsx
CODE:
import Image from 'next/image'
import profilePic from './me.png'

export default function Page() {
  return (
    <Image
      src={profilePic}
      alt="Picture of the author"
      // width={500} automatically provided
      // height={500} automatically provided
      // blurDataURL="data:..." automatically provided
      // placeholder="blur" // Optional blur-up while loading
    />
  )
}

----------------------------------------

TITLE: Implementing Partial Prerendering in a Next.js Page
DESCRIPTION: Example of a Next.js page using Partial Prerendering with static and dynamic components.

LANGUAGE: typescript
CODE:
import { Suspense } from 'react'
import { StaticComponent, DynamicComponent, Fallback } from '@/app/ui'

export const experimental_ppr = true

export default function Page() {
  return (
    <>
      <StaticComponent />
      <Suspense fallback={<Fallback />}>
        <DynamicComponent />
      </Suspense>
    </>
  )
}

LANGUAGE: javascript
CODE:
import { Suspense } from "react"
import { StaticComponent, DynamicComponent, Fallback } from "@/app/ui"

export const experimental_ppr = true

export default function Page() {
  return {
     <>
      <StaticComponent />
      <Suspense fallback={<Fallback />}>
        <DynamicComponent />
      </Suspense>
     </>
  };
}

----------------------------------------

TITLE: Implementing Partial Prerendering with Dynamic User Component
DESCRIPTION: Example of a Next.js page using Partial Prerendering with a dynamic User component wrapped in Suspense.

LANGUAGE: typescript
CODE:
import { Suspense } from 'react'
import { User, AvatarSkeleton } from './user'

export const experimental_ppr = true

export default function Page() {
  return (
    <section>
      <h1>This will be prerendered</h1>
      <Suspense fallback={<AvatarSkeleton />}>
        <User />
      </Suspense>
    </section>
  )
}

LANGUAGE: javascript
CODE:
import { Suspense } from 'react'
import { User, AvatarSkeleton } from './user'

export const experimental_ppr = true

export default function Page() {
  return (
    <section>
      <h1>This will be prerendered</h1>
      <Suspense fallback={<AvatarSkeleton />}>
        <User />
      </Suspense>
    </section>
  )
}

----------------------------------------

TITLE: Accessing NextRequest Object in Next.js Route Handlers
DESCRIPTION: This snippet demonstrates how to access the NextRequest object in a Next.js route handler, which extends the Web Request API and provides additional functionality like easy access to cookies and parsed URL object.

LANGUAGE: typescript
CODE:
import type { NextRequest } from 'next/server'

export async function GET(request: NextRequest) {
  const url = request.nextUrl
}

LANGUAGE: javascript
CODE:
export async function GET(request) {
  const url = request.nextUrl
}

----------------------------------------

TITLE: Implementing Shared Layout Component
DESCRIPTION: Shows how to create a reusable layout component that includes navigation and footer, wrapped around page content using the children prop.

LANGUAGE: jsx
CODE:
import Navbar from './navbar'
import Footer from './footer'

export default function Layout({ children }) {
  return (
    <>
      <Navbar />
      <main>{children}</main>
      <Footer />
    </>
  )
}

----------------------------------------

TITLE: Creating a Nested Layout for Dashboard in Next.js
DESCRIPTION: This code demonstrates how to create a nested layout for the /dashboard route in a Next.js application. Nested layouts allow for more granular control over the UI structure for specific route segments.

LANGUAGE: typescript
CODE:
export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return <section>{children}</section>
}

LANGUAGE: javascript
CODE:
export default function DashboardLayout({ children }) {
  return <section>{children}</section>
}

----------------------------------------

TITLE: Creating a Font Definitions File in Next.js
DESCRIPTION: Demonstrates how to create a font definitions file to centralize font loading and improve reusability across the application.

LANGUAGE: typescript
CODE:
import { Inter, Lora, Source_Sans_3 } from 'next/font/google'
import localFont from 'next/font/local'

const inter = Inter()
const lora = Lora()
const sourceCodePro400 = Source_Sans_3({ weight: '400' })
const sourceCodePro700 = Source_Sans_3({ weight: '700' })
const greatVibes = localFont({ src: './GreatVibes-Regular.ttf' })

export { inter, lora, sourceCodePro400, sourceCodePro700, greatVibes }

----------------------------------------

TITLE: Creating a Global Error Handler (TypeScript)
DESCRIPTION: This snippet demonstrates how to create a global error handler component in TypeScript for handling errors in the root layout. It includes custom HTML and body tags.

LANGUAGE: typescript
CODE:
'use client' // Error boundaries must be Client Components

export default function GlobalError({
  error,
  reset,
}: {
  error: Error & { digest?: string }
  reset: () => void
}) {
  return (
    // global-error must include html and body tags
    <html>
      <body>
        <h2>Something went wrong!</h2>
        <button onClick={() => reset()}>Try again</button>
      </body>
    </html>
  )
}

----------------------------------------

TITLE: Creating a Root Layout in Next.js
DESCRIPTION: Shows how to create a root layout in Next.js by exporting a default React component from a 'layout' file in the app directory. The layout includes html and body tags and accepts children as a prop.

LANGUAGE: typescript
CODE:
export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>
        {/* Layout UI */}
        {/* Place children where you want to render a page or nested layout */}
        <main>{children}</main>
      </body>
    </html>
  )
}

LANGUAGE: javascript
CODE:
export default function DashboardLayout({ children }) {
  return (
    <html lang="en">
      <body>
        {/* Layout UI */}
        {/* Place children where you want to render a page or nested layout */}
        <main>{children}</main>
      </body>
    </html>
  )
}

----------------------------------------

TITLE: Revalidating Cache after Server Function Execution in Next.js
DESCRIPTION: Shows how to revalidate the Next.js cache after performing an update using a Server Function by calling revalidatePath within the function.

LANGUAGE: typescript
CODE:
'use server'

import { revalidatePath } from 'next/cache'

export async function createPost(formData: FormData) {
  // Update data
  // ...

  revalidatePath('/posts')
}

LANGUAGE: javascript
CODE:
'use server'

import { revalidatePath } from 'next/cache'

export async function createPost(formData) {
  // Update data
  // ...
  revalidatePath('/posts')
}

----------------------------------------

TITLE: Basic Cookie Reading in Next.js Server Component
DESCRIPTION: Demonstrates how to read a cookie named 'theme' using the cookies() function in a Next.js Server Component.

LANGUAGE: typescript
CODE:
import { cookies } from 'next/headers'

export default async function Page() {
  const cookieStore = await cookies()
  const theme = cookieStore.get('theme')
  return '...'
}

LANGUAGE: javascript
CODE:
import { cookies } from 'next/headers'

export default async function Page() {
  const cookieStore = await cookies()
  const theme = cookieStore.get('theme')
  return '...'
}