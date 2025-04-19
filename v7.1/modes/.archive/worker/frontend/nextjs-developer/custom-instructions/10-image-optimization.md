# App Router: Image Optimization (`next/image`)

Using the built-in `next/image` component for optimized images.

## Core Concept: `<Image>` Component

Use `<Image>` from `next/image` instead of `<img>` for automatic optimization.

**Key Benefits:**

*   **Size Optimization:** Serves correctly sized images for different viewports.
*   **Format Modernization:** Converts to WebP/AVIF if browser supports.
*   **Lazy Loading:** Default behavior, loads images only when they enter viewport. Disable with `priority={true}`.
*   **CLS Prevention:** Reserves space, preventing layout shifts. Requires `width`/`height` or `fill`.
*   **On-Demand Optimization:** Images optimized by server/edge on first request (default).

## Basic Usage

1.  **Import:** `import Image from 'next/image';`
2.  **`src` Prop:**
    *   Static import: `import profilePic from '../assets/me.png';` (Width/height inferred).
    *   Public path: `/images/logo.png` (Requires `width`/`height`).
    *   Remote URL: `https://...` (Requires `width`/`height` and `next.config.js` config).
3.  **`alt` Prop:** **Required** for accessibility. Descriptive text.
4.  **`width` & `height` Props:** **Required** for public paths/remote URLs. Intrinsic dimensions of source image.
5.  **`fill` Prop (Alternative):** Fills parent container. Parent needs `position: relative/fixed/absolute`. Use with `object-fit` style.
6.  **`priority` Prop:** Boolean (default `false`). Set `true` for Above The Fold (ATF) / LCP images to preload and disable lazy loading.
7.  **`quality` Prop:** Number 1-100 (default 75). Compression level.
8.  **`placeholder` Prop:** `'blur'` (requires static import or `blurDataURL`) or `'empty'`.

## Examples

**1. Static Import (Recommended):**
```jsx
import Image from 'next/image';
import profilePic from '../assets/profile.jpg';

<Image src={profilePic} alt="Author" placeholder="blur" />
```

**2. Public Directory:**
```jsx
import Image from 'next/image';

<Image src="/images/hero.png" alt="Hero" width={1200} height={400} priority />
```

**3. Remote Images:**
*   Configure `next.config.js`:
    ```javascript
    // next.config.js
    const nextConfig = {
      images: {
        remotePatterns: [ { protocol: 'https', hostname: 'images.example.com' } ],
      },
    };
    module.exports = nextConfig;
    ```
*   Use in component:
    ```jsx
    import Image from 'next/image';

    <Image src="https://images.example.com/image.jpg" alt="Remote" width={500} height={300} />
    ```

**4. Fill Parent Container:**
```jsx
// CSS: .wrapper { position: relative; width: 100%; height: 300px; }
import Image from 'next/image';
import styles from './styles.module.css';

<div className={styles.wrapper}>
  <Image
    src="/images/background.jpg"
    alt="Background"
    fill
    style={{ objectFit: 'cover' }}
  />
</div>
```

Always use `next/image`. Provide `width`/`height` (or `fill`) and `alt`. Prefer static imports. Configure remote patterns.

*(Refer to the official Next.js documentation for the `<Image>` component.)*