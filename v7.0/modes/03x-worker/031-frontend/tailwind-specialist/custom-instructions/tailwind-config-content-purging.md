# Tailwind CSS: Content Configuration & Purging

Optimizing production CSS bundles by removing unused styles using the `content` configuration.

## Core Concept: Removing Unused Styles (Purging)

Tailwind generates a vast number of utility classes by default. To keep your final production CSS bundle small, Tailwind scans your project files to determine which classes you are *actually* using and removes (purges) the unused ones during the production build.

**How it Works:**

*   **`content` Array:** You specify the files Tailwind should scan in the `content` array within your `tailwind.config.js`.
*   **Scanning:** During the production build (`NODE_ENV=production`), Tailwind scans these files for class names that look like Tailwind utilities (using regular expressions).
*   **Generating CSS:** Only the CSS rules corresponding to the found utility classes (and their variants) are included in the final CSS output.

**Importance:**

*   **Drastically Reduces File Size:** Production CSS bundles can go from megabytes down to kilobytes.
*   **Improves Load Performance:** Smaller CSS files download and parse faster.
*   **Essential for Production:** Purging is a critical optimization step for any Tailwind project.

## Configuring `content`

The `content` key in `tailwind.config.js` accepts an array of glob patterns matching the files where you use Tailwind classes.

**Key Considerations:**

*   **Be Specific:** Include all file types where you might use Tailwind classes (HTML, JS, JSX, TSX, Svelte, Vue, PHP, Blade, etc.).
*   **Include Full Class Names:** Tailwind scans for *complete, unbroken* class names. Avoid constructing class names dynamically using string concatenation in ways that Tailwind cannot detect statically.
    *   **Bad:** `<div class="text-{{ error ? 'red' : 'green' }}-500">` (Tailwind won't see `text-red-500` or `text-green-500`)
    *   **Good:** `<div class="{{ error ? 'text-red-500' : 'text-green-500' }}">` (Tailwind sees both full class names)
    *   **Good (Mapping):**
        ```jsx
        const statusClasses = { error: 'text-red-500', success: 'text-green-500' };
        <div className={statusClasses[status]}>
        ```
*   **Framework Presets:** Some frameworks (like Next.js, Vite) might configure basic content paths automatically, but it's usually best to explicitly define them.

**Example `tailwind.config.js`:**

```javascript
// tailwind.config.js
module.exports = {
  // Configure paths to all template files using Tailwind classes
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}", // Example for Next.js pages router
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}", // Example for Next.js app router
    "./src/**/*.html", // Include plain HTML files if any
    "./src/**/*.svelte", // Include Svelte files if using SvelteKit/Svelte
    "./resources/views/**/*.blade.php", // Example for Laravel Blade
    // Add paths for any other file types where you use Tailwind
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

## Verifying Purging

*   Run your production build command (e.g., `npm run build`).
*   Inspect the generated CSS file (often in `.next/static/css`, `dist/assets`, or `public/build/assets`).
*   The file size should be significantly smaller than the development CSS (which includes all utilities).
*   Check your application in the browser to ensure styles haven't disappeared unexpectedly. If styles are missing, it usually means the `content` path configuration missed the file where the class was used, or the class name was constructed dynamically in an undetectable way.

Correctly configuring the `content` paths is crucial for Tailwind's production optimization. Ensure all files containing Tailwind classes are included in the glob patterns to prevent necessary styles from being purged.

*(Refer to the official Tailwind CSS documentation on Optimizing for Production / Content Configuration.)*