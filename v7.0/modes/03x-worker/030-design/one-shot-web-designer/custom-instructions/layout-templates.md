# Basic HTML/CSS Layout Templates

Starter structures for common page layouts. Use these as a foundation and apply specific styling.

## Template 1: Simple Landing Page (Hero + Features)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Landing Page</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header class="hero-section">
        <div class="container">
            <h1>Compelling Headline</h1>
            <p>Supporting text explaining the value proposition.</p>
            <button class="cta-button">Call to Action</button>
        </div>
    </header>

    <main>
        <section class="features-section">
            <div class="container">
                <h2>Key Features</h2>
                <div class="features-grid">
                    <div class="feature-item">
                        <img src="assets/icon1.svg" alt="Feature 1 Icon">
                        <h3>Feature One</h3>
                        <p>Brief description of the first feature.</p>
                    </div>
                    <div class="feature-item">
                        <img src="assets/icon2.svg" alt="Feature 2 Icon">
                        <h3>Feature Two</h3>
                        <p>Brief description of the second feature.</p>
                    </div>
                    <div class="feature-item">
                        <img src="assets/icon3.svg" alt="Feature 3 Icon">
                        <h3>Feature Three</h3>
                        <p>Brief description of the third feature.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Add more sections as needed (e.g., testimonials, pricing) -->
    </main>

    <footer>
        <div class="container">
            <p>&copy; 2025 Your Company. All rights reserved.</p>
        </div>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* Basic structure suggestion for styles.css */
body { margin: 0; font-family: sans-serif; /* Add base styles */ }
.container { max-width: 1100px; margin: 0 auto; padding: 0 1rem; }

.hero-section { /* Styles for hero: background, padding, text alignment */ }
.cta-button { /* Styles for main button */ }

.features-section { padding: 4rem 0; }
.features-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem; }
.feature-item { text-align: center; /* Styles for individual features */ }

footer { /* Footer styles */ }
```

## Template 2: Basic Article Layout

```html
<!-- (Include head similar to Template 1) -->
<body>
    <header>
        <nav class="container"> /* Navigation */ </nav>
    </header>

    <main class="container article-layout">
        <article>
            <h1>Article Title</h1>
            <p class="meta">Published on [Date] by [Author]</p>
            <img src="assets/featured-image.jpg" alt="Featured Image" class="featured-image">

            <p>Introduction paragraph...</p>
            <h2>Subheading 1</h2>
            <p>Content paragraph...</p>
            <blockquote>Blockquote if needed...</blockquote>
            <h2>Subheading 2</h2>
            <p>More content...</p>
        </article>
        <aside>
            <h3>Related Articles</h3>
            <ul>
                <li><a href="#">Related Link 1</a></li>
                <li><a href="#">Related Link 2</a></li>
            </ul>
        </aside>
    </main>

    <footer> /* Footer */ </footer>
    <script src="script.js"></script>
</body>
```

```css
/* Basic structure suggestion for styles.css */
.article-layout { display: grid; grid-template-columns: 3fr 1fr; gap: 2rem; margin-top: 2rem; }
article { /* Styles for main content area */ }
article h1, article h2 { /* Heading styles */ }
.meta { color: #666; font-style: italic; }
.featured-image { max-width: 100%; height: auto; margin-bottom: 1rem; }
aside { /* Styles for sidebar */ }
```

*(These are minimal structures. Add specific classes, IDs, and detailed CSS based on the desired visual design.)*