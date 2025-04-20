# Next.js: Image Optimization (`next/image`)

Using the built-in `next/image` component for optimized images.

## Core Concept: `<Image>` Component

Next.js provides a built-in `<Image>` component (imported from `next/image`) that extends the standard HTML `<img>` element with automatic image optimization features.

**Key Benefits:**

*   **Size Optimization:** Automatically serves correctly sized images for different devices and viewports, reducing file size.
*   **Format Modernization:** Converts images to modern formats like WebP or AVIF when the browser supports them, offering better compression than JPEG/PNG.
*   **Lazy Loading:** Images are loaded only when they enter the viewport (default behavior), improving initial page load performance. Can be disabled with `priority={true}`.
*   **Cumulative Layout Shift (CLS) Prevention:** Automatically reserves space for the image before it loads, preventing content from jumping around. Requires providing `width` and `height` props (or `fill` prop).
*   **On-Demand Optimization:** Images are optimized by the Next.js server (or at the edge) when first requested, rather than at build time (unless configured otherwise).

## Basic Usage

1.  **Import:** `import Image from 'next/image';`
2.  **`src` Prop:** Can be:
    *   A statically imported image file (e.g., `import profilePic from '../public/me.png';`). Next.js determines width/height automatically.
    *   A path string relative to the `public` directory (e.g., `/images/logo.png`). **Requires `width` and `height` props.**
    *   An absolute URL for remote images. **Requires `width`, `height`, and configuration in `next.config.js`**.
3.  **`alt` Prop:** **Required** for accessibility. Provide a descriptive alternative text for the image.
4.  **`width` & `height` Props:** **Required** when using path strings or remote URLs to prevent CLS. Specify the intrinsic dimensions of the source image in pixels. Next.js uses these for aspect ratio calculation and generating `srcset`.
5.  **`fill` Prop (Alternative to `width`/`height`):** Allows the image to fill its parent container. The parent element **must** have `position: relative`, `position: fixed`, or `position: absolute`. Often used with `object-fit` styles (`contain` or `cover`).
6.  **`priority` Prop:** Boolean. If `true`, the image is considered high-priority and preloaded. Lazy loading is disabled. Use for images Above The Fold (ATF), like LCP elements. Defaults to `false`.
7.  **`quality` Prop:** Number between 1 and 100 (default 75). Affects compression level.
8.  **`placeholder` Prop:** `'blur'` or `'empty'`. If `'blur'`, generates a small blurred version of the image as a placeholder while loading (requires static import or `blurDataURL`).

## Examples

**1. Static Import (Recommended):**

*   Place image in any folder (e.g., `src/assets`).
*   Import the image file directly.
*   `width` and `height` are inferred automatically.

```jsx
import Image from 'next/image';
import profilePic from '../assets/profile.jpg'; // Import image file

function MyComponent() {
  return (
    <div>
      <h2>Profile</h2>
      <Image
        src={profilePic} // Use imported image object
        alt="Picture of the author"
        // width and height are automatic
        placeholder="blur" // Optional: Use blur placeholder
        quality={80} // Optional: Adjust quality
      />
    </div>
  );
}
```

**2. Public Directory:**

*   Place image in the `public` directory (e.g., `public/images/hero.png`).
*   Use a root-relative path string for `src`.
*   **Must provide `width` and `height`**.

```jsx
import Image from 'next/image';

function HeroSection() {
  return (
    <Image
      src="/images/hero.png" // Path relative to public directory
      alt="Hero banner"
      width={1200} // Intrinsic width of source image
      height={400} // Intrinsic height of source image
      priority // Preload if it's the LCP element
    />
  );
}
```

**3. Remote Images:**

*   Use the absolute URL for `src`.
*   **Must provide `width` and `height`**.
*   **Must configure allowed domains/patterns** in `next.config.js` for security.

```javascript
// next.config.js
/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'images.unsplash.com',
        // port: '', // Optional
        // pathname: '/account123/**', // Optional path pattern
      },
      // Add other allowed domains/patterns
    ],
  },
};
module.exports = nextConfig;
```

```jsx
// Component using remote image
import Image from 'next/image';

function RemoteImageDemo({ imageUrl }) {
  return (
    <Image
      src={imageUrl} // Absolute URL
      alt="Description of remote image"
      width={500} // Intrinsic width
      height={300} // Intrinsic height
    />
  );
}
```

**4. Fill Parent Container:**

*   Parent element needs `position: relative` (or `fixed`/`absolute`).
*   Use `fill` prop instead of `width`/`height`.
*   Often combined with `object-fit` style.

```jsx
import Image from 'next/image';
import styles from './Card.module.css'; // Assume .cardImageWrapper has position: relative

function CardWithImage() {
  return (
    <div className={styles.card}>
      <div className={styles.cardImageWrapper}>
        <Image
          src="/images/card-bg.jpg"
          alt="Card background"
          fill // Fill the parent wrapper
          style={{ objectFit: 'cover' }} // CSS object-fit property
        />
      </div>
      <div className={styles.cardContent}>
        {/* ... card content ... */}
      </div>
    </div>
  );
}
```

The `next/image` component is crucial for delivering performant images in Next.js applications. Always provide `width`, `height`, and `alt`, or use the `fill` prop correctly. Use static imports where possible for automatic dimension detection and blur placeholders. Configure remote patterns for external images.

*(Refer to the official Next.js documentation for the `<Image>` component.)*