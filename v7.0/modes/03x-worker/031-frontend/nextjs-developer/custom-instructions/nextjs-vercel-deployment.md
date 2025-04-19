# Next.js: Vercel Deployment Basics

Deploying Next.js applications to Vercel.

## Core Concept: Vercel Platform

Vercel is the company behind Next.js and provides a hosting platform highly optimized for Next.js applications. It offers features like automatic deployments via Git integration, serverless functions, edge functions (for middleware), global CDN, image optimization, and more.

**Key Advantages for Next.js:**

*   **Seamless Integration:** Built by the same team, ensuring optimal compatibility and performance.
*   **Zero Configuration (Often):** Vercel automatically detects Next.js projects and applies appropriate build settings and optimizations.
*   **Serverless & Edge Functions:** Automatically deploys API routes (Route Handlers) as Serverless Functions and Middleware as Edge Functions.
*   **Global CDN:** Static assets and cached pages/data are served from Vercel's edge network for fast global delivery.
*   **Automatic CI/CD:** Integrates with GitHub, GitLab, and Bitbucket for automatic builds and deployments on push/merge.
*   **Preview Deployments:** Creates unique preview URLs for every Git branch or pull request, allowing easy testing and collaboration before merging to production.
*   **Image Optimization:** Integrates seamlessly with `next/image`.

## Basic Deployment Steps

1.  **Push to Git:** Ensure your Next.js project code is pushed to a Git repository (GitHub, GitLab, Bitbucket).
2.  **Import Project on Vercel:**
    *   Sign up/log in to Vercel (https://vercel.com).
    *   Click "Add New..." -> "Project".
    *   Select your Git provider and authorize Vercel access.
    *   Choose the repository containing your Next.js project and click "Import".
3.  **Configure Project (Usually Automatic):**
    *   Vercel typically auto-detects Next.js and sets the Framework Preset correctly.
    *   Build Command: Usually `next build`.
    *   Output Directory: Usually `.next`.
    *   Install Command: Usually `npm install`, `yarn install`, or `pnpm install`.
    *   Root Directory: Set if your Next.js app is in a subdirectory of the repo.
4.  **Environment Variables:**
    *   Go to the project's **Settings** -> **Environment Variables** section on Vercel.
    *   Add any required environment variables (like `CLERK_SECRET_KEY`, database connection strings, third-party API keys).
    *   **Crucially:** Ensure variables needed by the browser (like `NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY`) are prefixed correctly (`NEXT_PUBLIC_`). Vercel makes these available during the build and on the client-side. Secret keys (without the prefix) are only available server-side (Server Components, Route Handlers, Server Actions, Middleware).
    *   Select the environments (Production, Preview, Development) where each variable should apply.
5.  **Deploy:** Click the "Deploy" button. Vercel will clone the repository, install dependencies, build the Next.js application, and deploy it to its infrastructure.
6.  **Access Deployment:** Vercel provides a unique URL for the deployment (and updates the production domain if deploying the main branch).

## Subsequent Deployments

*   After the initial setup, Vercel automatically triggers new deployments whenever you push changes to the connected Git repository branches (e.g., `main` for production, other branches for previews).

## Key Vercel Concepts for Next.js

*   **Serverless Functions:** API routes (`route.ts`) are deployed as serverless functions, typically running in a specific region. They have execution time limits.
*   **Edge Functions:** Middleware (`middleware.ts`) runs on Vercel's Edge Network, closer to the user, for faster execution (e.g., for redirects or auth checks). Edge functions have stricter runtime limitations (no native Node.js APIs). Route Handlers can also be configured to run at the edge.
*   **Caching:** Vercel's Edge Network caches static assets, SSG pages, ISR pages, and Data Cache results (`fetch` cache) for fast delivery. `revalidatePath`/`revalidateTag` integrates with Vercel's cache invalidation.
*   **Build Logs:** Monitor build progress and diagnose errors in the Vercel dashboard.
*   **Runtime Logs:** View logs from Serverless Functions and Edge Functions in the Vercel dashboard for debugging deployed code.

Deploying Next.js to Vercel is generally straightforward due to the tight integration between the framework and the platform. Ensure environment variables are configured correctly and securely.

*(Refer to the official Vercel documentation for Next.js.)*