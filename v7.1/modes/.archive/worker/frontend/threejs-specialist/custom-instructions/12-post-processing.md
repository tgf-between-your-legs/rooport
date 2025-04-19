# Post-Processing (`EffectComposer`)

Applying visual effects to the entire rendered scene after it's drawn, using `EffectComposer`.

## Core Concept

Post-processing involves rendering your main scene to an off-screen buffer (render target) instead of directly to the screen. Then, one or more "passes" are applied sequentially to this buffer, modifying the image (e.g., adding blur, bloom, color correction, anti-aliasing) before finally rendering the result to the screen.

Three.js uses the `EffectComposer` to manage this chain of passes.

## Setup

1.  **Import necessary modules:**
    ```javascript
    import * as THREE from 'three';
    import { EffectComposer } from 'three/addons/postprocessing/EffectComposer.js';
    import { RenderPass } from 'three/addons/postprocessing/RenderPass.js';
    // Import specific effect passes you need
    import { UnrealBloomPass } from 'three/addons/postprocessing/UnrealBloomPass.js';
    import { OutputPass } from 'three/addons/postprocessing/OutputPass.js'; // Important for color space
    import { SMAAPass } from 'three/addons/postprocessing/SMAAPass.js'; // Example: Anti-aliasing
    // import { GlitchPass } from 'three/addons/postprocessing/GlitchPass.js';
    // import { FilmPass } from 'three/addons/postprocessing/FilmPass.js';
    // import { ShaderPass } from 'three/addons/postprocessing/ShaderPass.js'; // For custom shader effects
    ```

2.  **Create `EffectComposer`:** Instantiate it, passing in the `WebGLRenderer` and optionally a `WebGLRenderTarget` if you need specific configurations (like multisampling). Usually, the composer creates its own render targets.
    ```javascript
    // Assume 'renderer', 'scene', 'camera' are already set up
    const composer = new EffectComposer(renderer);
    // Optional: Set size initially (will also be updated on resize)
    composer.setSize(window.innerWidth, window.innerHeight);
    composer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    ```

3.  **Add Passes:** Add passes sequentially using `composer.addPass()`. The order matters!
    *   **`RenderPass` (Usually First):** Renders the main scene into the composer's buffer.
    *   **Effect Passes:** Apply visual effects (e.g., `UnrealBloomPass`, `GlitchPass`). Configure parameters for each pass.
    *   **Anti-Aliasing Pass (Optional, often near end):** Passes like `SMAAPass` can apply anti-aliasing to the processed image.
    *   **`OutputPass` (Usually Last):** Handles output encoding (e.g., converting from linear to sRGB if your renderer's `outputColorSpace` is `sRGBColorSpace`) and renders the final result to the screen. **Crucial for correct colors when using a standard sRGB workflow.**

    ```javascript
    // 1. Render the scene
    const renderPass = new RenderPass(scene, camera);
    composer.addPass(renderPass);

    // 2. Add Bloom effect (Example)
    const bloomPass = new UnrealBloomPass(
      new THREE.Vector2(window.innerWidth, window.innerHeight), // resolution
      1.2, // strength
      0.6, // radius
      0.8  // threshold (pixels brighter than this contribute to bloom)
    );
    composer.addPass(bloomPass);

    // 3. Add Anti-aliasing (Example - SMAA)
    // SMAAPass requires width/height considering pixel ratio
    // const smaaPass = new SMAAPass(
    //    window.innerWidth * renderer.getPixelRatio(),
    //    window.innerHeight * renderer.getPixelRatio()
    // );
    // composer.addPass(smaaPass);

    // 4. Add Output pass for color space correction (IMPORTANT!)
    const outputPass = new OutputPass();
    composer.addPass(outputPass);
    ```
    *   **Note:** Some older examples might set `renderToScreen = true` on the *last* effect pass. This is generally discouraged now; using `OutputPass` is the standard way to handle final output and color space conversion correctly.

## Rendering Loop

*   Instead of calling `renderer.render(scene, camera)`, call `composer.render()` inside your animation loop.
*   Pass the `deltaTime` (from `THREE.Clock`) to the composer's render method, as some passes might be time-dependent.

```javascript
const clock = new THREE.Clock();

function animate() {
  const deltaTime = clock.getDelta();

  // Update animations, controls, etc.
  // mixer?.update(deltaTime);
  // controls?.update();

  // Render using the composer
  composer.render(deltaTime);

  requestAnimationFrame(animate);
}

requestAnimationFrame(animate);
```

## Handling Resize

*   When the window resizes, update the renderer's size and pixel ratio, **and also the composer's size and pixel ratio**.
*   Some passes (like `UnrealBloomPass`) might have resolution-dependent uniforms that also need updating.

```javascript
function onWindowResize() {
  const width = window.innerWidth;
  const height = window.innerHeight;
  const pixelRatio = Math.min(window.devicePixelRatio, 2);

  camera.aspect = width / height;
  camera.updateProjectionMatrix();

  renderer.setSize(width, height);
  renderer.setPixelRatio(pixelRatio);

  composer.setSize(width, height); // Update composer size
  composer.setPixelRatio(pixelRatio); // Update composer pixel ratio

  // Update resolution uniforms for passes if needed
  // bloomPass.resolution.set(width, height); // Example for bloom pass if needed
  // smaaPass.setSize(width * pixelRatio, height * pixelRatio); // Example for SMAAPass
}
window.addEventListener('resize', onWindowResize);
```

## Common Passes

*   `RenderPass`: Renders the input scene.
*   `UnrealBloomPass`: Creates a bloom (glow) effect for bright areas.
*   `GlitchPass`: Adds digital glitch effects.
*   `FilmPass`: Simulates film grain, scanlines, etc.
*   `DotScreenPass`: Renders the scene as dots.
*   `BokehPass`: Simulates depth-of-field blur (can be complex to set up).
*   `SMAAPass` / `SSAARenderPass`: Anti-aliasing techniques (SMAA is generally faster).
*   `ShaderPass`: Apply a custom shader (GLSL) as a post-processing step. Takes a shader object (with uniforms, vertex/fragment shaders) as input.
*   `OutputPass`: Handles color space conversion (Linear-to-sRGB).

## Considerations

*   **Performance:** Each pass adds overhead (rendering a full-screen quad). More passes = lower performance. Profile your application. Disable passes or reduce their quality settings if needed.
*   **Order Matters:** The sequence of passes determines how effects are layered. Experiment to achieve the desired look.
*   **Render Targets:** The composer uses internal `WebGLRenderTarget`s. Be mindful of memory usage, especially with high resolutions or many passes. Dispose of the composer (`composer.dispose()`) if it's removed to free these targets.
*   **Color Space:** Ensure correct color space handling throughout your pipeline (renderer `outputColorSpace`, texture `colorSpace`, `OutputPass`). Using `renderer.outputColorSpace = THREE.SRGBColorSpace` and `OutputPass` is the standard approach for displaying correctly on sRGB monitors.