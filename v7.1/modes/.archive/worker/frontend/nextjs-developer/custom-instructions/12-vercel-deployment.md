# App Router: Vercel Deployment Basics

Deploying Next.js applications to Vercel.

## Core Concept: Vercel Platform

Vercel is the hosting platform built by the creators of Next.js, optimized for its features.

**Key Advantages:**

*   **Seamless Integration:** Optimal compatibility and performance.
*   **Zero Config (Often):** Auto-detects Next.js, applies correct build settings.
*   **Serverless/Edge Functions:** Auto-deploys Route Handlers (Serverless) and Middleware (Edge).
*   **Global CDN:** Caches static assets, SSG/ISR pages, Data Cache results.
*   **Automatic CI/CD:** Deploys on Git push/merge (GitHub, GitLab, Bitbucket).
*   **Preview Deployments:** Unique URLs for branches/PRs for testing.
*   **Image Optimization:** Integrates with `next/image`.

## Basic Deployment Steps

1.  **Push to Git:** Ensure code is in a supported Git provider repository.
2.  **Import Project on Vercel:** Connect Git provider, select repo, click "Import".
3.  **Configure Project (Usually Automatic):** Vercel detects Next.js preset. Verify Build Command (`next build`), Output Directory (`.next`), Install Command (`npm install` etc.). Set Root Directory if needed.
4.  **Environment Variables:**
    *   Add in Vercel project **Settings -> Environment Variables**.
    *   Use correct prefix (`NEXT_PUBLIC_`) for browser-accessible variables.
    *   Secrets (no prefix) are server-only.
    *   Assign to Production, Preview, Development environments.
5.  **Deploy:** Click "Deploy". Vercel clones, installs, builds, and deploys.
6.  **Access:** Use the provided Vercel URL.

## Subsequent Deployments

Automatic on push to connected Git branches.

## Key Vercel Concepts

*   **Serverless Functions:** Route Handlers, dynamic pages, Server Actions run as serverless functions (region-based, time limits).
*   **Edge Functions:** Middleware runs on Edge Network (faster, stricter runtime limits - no Node APIs). Route Handlers can opt-in (`export const runtime = 'edge';`).
*   **Caching:** Vercel Edge Network caches static assets, SSG/ISR pages, Data Cache (`fetch`) results. Integrates with `revalidatePath`/`revalidateTag`.
*   **Logs:** Monitor build and runtime logs in the Vercel dashboard.

## Common Issues

*   **Environment Variables:** Missing, incorrect, or wrongly prefixed variables.
*   **Build Errors:** Check Vercel build logs (type errors, missing deps).
*   **Runtime Errors:** Check Vercel runtime logs (Serverless/Edge function errors).
*   **Caching:** Content not updating? Check `fetch` options, `revalidate` settings, use `revalidatePath`/`revalidateTag`.

*(Refer to the official Vercel documentation for Next.js.)*