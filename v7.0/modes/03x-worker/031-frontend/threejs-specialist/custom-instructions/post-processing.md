# Three.js: Post-Processing (`EffectComposer`)

Applying visual effects to the entire rendered scene after it's drawn.

## Core Concept

Post-processing involves rendering your main scene to an off-screen buffer (render target) instead of directly to the screen. Then, one or more "passes" are applied to this buffer, modifying the image (e.g., adding blur, bloom, color correction) before finally rendering the result to the screen.

Three.js uses the `EffectComposer` to manage this process.

## Setup

1.  **Import necessary modules:**
    ```javascript
    import * as THREE from 'three';
    import { EffectComposer } from 'three/examples/jsm/postprocessing/EffectComposer.js';
    import { RenderPass } from 'three/examples/jsm/postprocessing/RenderPass.js';
    // Import specific effect passes
    import { UnrealBloomPass } from 'three/examples/jsm/postprocessing/UnrealBloomPass.js';
    import { OutputPass } from 'three/examples/jsm/postprocessing/OutputPass.js';
    // ... import other passes like GlitchPass, FilmPass, SMAAPass, etc.
    ```

2.  **Create `EffectComposer`:** Instantiate it, passing in the `WebGLRenderer`.
    ```javascript
    // Assume 'renderer', 'scene', 'camera' are already set up
    const composer = new EffectComposer(renderer);
    ```

3.  **Add Passes:** Add passes sequentially to the composer.
    *   **`RenderPass` (Usually First):** Renders the main scene into the composer's buffer.
    *   **Effect Passes:** Apply visual effects (e.g., `UnrealBloomPass`, `GlitchPass`).
    *   **`OutputPass` (Usually Last):** Handles output encoding (e.g., converting from linear to sRGB) and renders the final result to the screen. Important for correct colors.

    ```javascript
    // 1. Render the scene
    const renderPass = new RenderPass(scene, camera);
    composer.addPass(renderPass);

    // 2. Add Bloom effect
    const bloomPass = new UnrealBloomPass(
      new THREE.Vector2(window.innerWidth, window.innerHeight), // resolution
      1.5, // strength
      0.4, // radius
      0.85 // threshold
    );
    // bloomPass.renderToScreen = true; // Set to true if this is the LAST pass and you don't need OutputPass
    composer.addPass(bloomPass);

    // 3. Add Output pass for color correction (recommended if not rendering bloom directly to screen)
    const outputPass = new OutputPass();
    composer.addPass(outputPass);

    // Example: Adding Anti-aliasing (SMAAPass) - often placed after effects
    // import { SMAAPass } from 'three/examples/jsm/postprocessing/SMAAPass.js';
    // const smaaPass = new SMAAPass( window.innerWidth * renderer.getPixelRatio(), window.innerHeight * renderer.getPixelRatio() );
    // composer.addPass(smaaPass); // Place before or after OutputPass depending on desired effect
    ```

## Rendering Loop

*   Instead of calling `renderer.render(scene, camera)`, call `composer.render()` inside your animation loop.
*   Pass the `deltaTime` to the composer's render method for time-dependent effects.

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

*   When the window resizes, you need to update both the renderer's size **and** the composer's size (and potentially the aspect ratio of passes like bloom).

```javascript
function onWindowResize() {
  const width = window.innerWidth;
  const height = window.innerHeight;

  camera.aspect = width / height;
  camera.updateProjectionMatrix();

  renderer.setSize(width, height);
  composer.setSize(width, height); // Update composer size

  // Update resolution uniforms/aspect for passes if needed
  // bloomPass.resolution.set(width, height);
}
window.addEventListener('resize', onWindowResize);
```

## Common Passes

*   `RenderPass`: Renders the input scene.
*   `UnrealBloomPass`: Creates a bloom (glow) effect for bright areas.
*   `GlitchPass`: Adds digital glitch effects.
*   `FilmPass`: Simulates film grain, scanlines, etc.
*   `DotScreenPass`: Renders the scene as dots.
*   `BokehPass`: Simulates depth-of-field blur.
*   `SMAAPass` / `SSAARenderPass`: Anti-aliasing techniques.
*   `ShaderPass`: Apply a custom shader (GLSL) as a post-processing step.
*   `OutputPass`: Handles color space conversion (Linear-to-sRGB).

## Considerations

*   **Performance:** Each pass adds overhead. More passes mean lower performance. Profile your application.
*   **Order Matters:** The order in which passes are added to the composer determines how effects are layered.
*   **Render Target:** The composer uses internal render targets (off-screen buffers). Be mindful of memory usage, especially with high resolutions.
*   **Color Space:** Ensure correct color space handling, especially when using `OutputPass` and configuring the renderer's output encoding (`renderer.outputEncoding = THREE.sRGBEncoding;`).

*(Refer to the official Three.js Post-processing documentation and examples: https://threejs.org/docs/#manual/en/introduction/How-to-use-post-processing)*