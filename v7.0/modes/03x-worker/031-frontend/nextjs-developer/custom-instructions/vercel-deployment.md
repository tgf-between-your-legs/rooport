# Next.js Deployment on Vercel

Key considerations for deploying Next.js applications (especially App Router) to Vercel.

## 1. Connecting Your Project

*   **Import Project:** Connect your Git repository (GitHub, GitLab, Bitbucket) to Vercel. Vercel automatically detects Next.js projects.
*   **Framework Preset:** Ensure Vercel correctly identifies the project as "Next.js". This usually happens automatically.

## 2. Build Configuration

*   **Build Command:** Vercel typically defaults to `next build`. This is usually correct.
*   **Output Directory:** Vercel automatically detects the `.next` directory. No configuration is usually needed.
*   **Install Command:** Defaults to `npm install`, `yarn install`, or `pnpm install` based on your lock file.

## 3. Environment Variables

*   **Crucial:** Configure all necessary environment variables (e.g., `CLERK_SECRET_KEY`, database URLs, API keys) in the Vercel project settings under "Settings" -> "Environment Variables".
*   **Security:** Never commit sensitive keys directly into your code or `.env.local`. Use Vercel's environment variable management.
*   **Frontend Exposure:** Remember to prefix variables needed by the browser with `NEXT_PUBLIC_` (e.g., `NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY`). Vercel automatically makes these available client-side. Non-prefixed variables are only available server-side (Server Components, Route Handlers, Server Actions).

## 4. Rendering & Adapters

*   **Automatic Detection:** Vercel automatically handles different rendering modes (Static, SSR, ISR) based on your Next.js configuration (`output` in `next.config.js` and usage of dynamic functions/caching).
*   **Adapter:** When deploying an SSR or ISR application (`output: 'server'` or `'hybrid'`), Vercel typically **does not require** an explicit adapter (like `@astrojs/vercel`) in `next.config.js`. Vercel's build output API handles this automatically for Next.js. Remove adapters like `@astrojs/node` if you added them previously for local SSR testing unless specifically needed for a non-Vercel Node environment.

## 5. Serverless & Edge Functions

*   **App Router:** By default, dynamically rendered pages, Route Handlers, and Server Actions are deployed as Vercel Serverless Functions.
*   **Edge Runtime:** You can opt specific Route Handlers or Middleware into Vercel's Edge Functions for lower latency by exporting `export const runtime = 'edge';`. Be aware of Edge runtime limitations (e.g., no native Node.js APIs).
    ```typescript
    // app/api/fast-endpoint/route.ts
    export const runtime = 'edge'; // 'nodejs' (default) | 'edge'

    export async function GET(request: Request) {
      return new Response('Hello from the edge!');
    }
    ```

## 6. Caching on Vercel

*   **Data Cache:** Vercel respects Next.js Data Cache controls (`fetch` options, `revalidate` settings). Cached fetch results are stored.
*   **Full Route Cache:** Statically generated pages and ISR pages are cached on Vercel's Edge Network (CDN).
*   **Revalidation:** `revalidatePath` and `revalidateTag` work on Vercel to purge relevant caches.

## 7. Domains & Previews

*   **Domains:** Configure custom domains in Vercel project settings.
*   **Preview Deployments:** Vercel automatically creates preview deployments for each Git branch and pull request, allowing you to test changes before merging to production. Environment variables can be configured separately for Preview environments.

## Common Issues

*   **Environment Variables:** Missing or incorrect environment variables are a common cause of deployment failures or runtime errors. Double-check names and values in Vercel settings. Ensure correct `NEXT_PUBLIC_` prefixing.
*   **Build Errors:** Check the Vercel deployment logs for build errors (e.g., type errors, missing dependencies).
*   **Runtime Errors:** Check Vercel's runtime logs (Serverless Function logs) for errors occurring during SSR, API route execution, or Server Actions.
*   **Caching Issues:** If content isn't updating as expected, check `fetch` caching options, `revalidate` settings, and consider using `revalidatePath`/`revalidateTag`.

*(Refer to Vercel's Next.js deployment documentation: https://vercel.com/docs/frameworks/nextjs)*