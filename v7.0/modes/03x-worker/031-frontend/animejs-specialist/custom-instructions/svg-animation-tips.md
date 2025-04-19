# anime.js SVG Animation Tips

Notes on animating SVG elements, particularly paths and morphing.

## 1. Animating Attributes

Most SVG attributes can be animated directly like CSS properties.

```javascript
anime({
  targets: 'circle',
  cx: 200, // Animate center x
  r: 50, // Animate radius
  fill: '#FF0000', // Animate fill color
  duration: 1500,
  easing: 'easeInOutQuad'
});
```

## 2. Path Morphing (`d` attribute)

*   **Concept:** Animating the `d` attribute of `<path>` elements to smoothly transition between shapes.
*   **Requirement:** Paths **must** have the exact same number of points and commands for smooth morphing.
*   **Implementation:** Provide an array of `d` attribute strings as the value.
    ```javascript
    anime({
      targets: '#morphingPath',
      d: [
        { value: 'M10 10 L90 10 L90 90 L10 90 Z' }, // Square path data
        { value: 'M50 10 C 77.6 10, 100 32.4, 100 60 S 77.6 110, 50 110 S 0 87.6, 0 60 S 22.4 10, 50 10 Z' } // Circle path data (ensure point compatibility!)
      ],
      duration: 2000,
      easing: 'easeInOutSine',
      loop: true,
      direction: 'alternate'
    });
    ```
*   **Point Compatibility:** If paths don't have the same number of points, the animation will likely jump or look incorrect.
    *   **Solution 1 (Manual):** Manually edit SVG paths in a vector editor to add/remove points until they match.
    *   **Solution 2 (Libraries):** Use libraries like **Flubber.js** (https://github.com/veltman/flubber) to interpolate between paths with different point counts *before* passing the interpolated path data to anime.js (often requires generating many intermediate path strings). This is more complex.
    *   **Solution 3 (Preprocessing):** Prepare compatible SVG paths during the asset creation phase.

## 3. Line Drawing / Stroke Animation

*   **Concept:** Animating the `stroke-dashoffset` property to make lines appear as if they are being drawn.
*   **Setup (CSS):**
    1.  Calculate the total length of the path (use `getTotalLength()` in JS).
    2.  Set `stroke-dasharray` to the path length.
    3.  Set `stroke-dashoffset` initially to the path length.
    ```css
    .drawing-path {
      /* Calculate length via JS */
      /* stroke-dasharray: [pathLength]; */
      /* stroke-dashoffset: [pathLength]; */
    }
    ```
*   **Implementation (JS + anime.js):**
    ```javascript
    const path = document.querySelector('.drawing-path');
    const pathLength = path.getTotalLength();

    // Set initial styles via JS (or CSS)
    path.style.strokeDasharray = pathLength;
    path.style.strokeDashoffset = pathLength;

    // Animate offset to 0
    anime({
      targets: path,
      strokeDashoffset: [pathLength, 0], // Animate from full offset to zero
      // OR use anime.setDashoffset helper:
      // strokeDashoffset: [anime.setDashoffset, 0],
      duration: 3000,
      easing: 'easeInOutSine'
    });
    ```

## 4. Animating Along a Path

*   Use SVG `<motionPath>` or libraries like MotionPathPlugin (from GSAP, not anime.js) or calculate positions manually if using only anime.js (more complex). Anime.js doesn't have built-in motion path support as easily as dedicated libraries.

*(SVG animation can be complex. Test thoroughly and consult specific SVG and anime.js documentation.)*