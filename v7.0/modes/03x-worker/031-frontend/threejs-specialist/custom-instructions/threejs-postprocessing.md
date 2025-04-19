# Three.js: Post-Processing Effects

Applying full-screen visual effects after the main scene rendering using `EffectComposer`.

## Core Concept: Processing the Rendered Image

Post-processing involves taking the rendered image of your scene and applying one or more visual effects (like bloom, depth of field, vignette, custom shader effects) to the entire image before displaying it on the screen.

Three.js provides the `EffectComposer` to manage this process. It works by rendering the scene into an off-screen buffer (render target) and then passing this buffer through a series of **Passes**. Each pass can read the result of the previous pass, apply an effect (often using shaders), and write to the next buffer.

**Key Components:**

*   **`EffectComposer`:** Manages the chain of post-processing passes. You render your scene *through* the composer instead of directly with the renderer.
*   **Render Target (`WebGLRenderTarget`):** An off-screen buffer where the scene or intermediate pass results are drawn. The composer manages these internally.
*   **Passes:** Individual units that perform an operation in the post-processing chain.
    *   **`RenderPass`:** (Required first pass) Renders the main scene into the composer's buffer.
    *   **Effect Passes:** Apply specific visual effects (e.g., `UnrealBloomPass`, `BokehPass`, `SSAOPass`, `FilmPass`). Many are available in `three/addons/postprocessing/`.
    *   **`ShaderPass`:** Applies a custom full-screen shader effect using your own GLSL code. Receives the previous pass's texture as a uniform (`tDiffuse`).
    *   **`OutputPass`:** (Required last pass, usually) Renders the final result to the screen, handling color space conversions correctly.

## Implementation Steps

1.  **Import Composer and Passes:** Import `EffectComposer` and the specific passes you need from `three/addons/postprocessing/`.

    ```javascript
    import * as THREE from 'three';
    import { EffectComposer } from 'three/addons/postprocessing/EffectComposer.js';
    import { RenderPass } from 'three/addons/postprocessing/RenderPass.js';
    import { OutputPass } from 'three/addons/postprocessing/OutputPass.js';
    import { UnrealBloomPass } from 'three/addons/postprocessing/UnrealBloomPass.js';
    // import { ShaderPass } from 'three/addons/postprocessing/ShaderPass.js';
    // import { MyCustomShader } from './MyCustomShader.js'; // Example custom shader pass
    ```

2.  **Create `EffectComposer`:** Instantiate the composer, passing the `WebGLRenderer` instance.

    ```javascript
    // Assuming renderer, scene, camera are already created
    const composer = new EffectComposer(renderer);
    // Optional: Set size (usually matches renderer)
    composer.setSize(window.innerWidth, window.innerHeight);
    // Optional: Adjust pixel ratio
    composer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    ```

3.  **Add Passes:** Add passes to the composer in the order they should be applied.
    *   Start with `RenderPass` to render the main scene.
    *   Add desired effect passes.
    *   End with `OutputPass` to render to the screen correctly.

    ```javascript
    // 1. Render the main scene
    const renderPass = new RenderPass(scene, camera);
    composer.addPass(renderPass);

    // 2. Add Bloom effect
    const bloomPass = new UnrealBloomPass(
        new THREE.Vector2(window.innerWidth, window.innerHeight), // resolution
        1.5, // strength
        0.4, // radius
        0.85 // threshold
    );
    // bloomPass.threshold = 0.1;
    // bloomPass.strength = 0.5;
    // bloomPass.radius = 0.2;
    composer.addPass(bloomPass);

    // 3. Add a custom shader pass (optional)
    // const customPass = new ShaderPass(MyCustomShader);
    // composer.addPass(customPass);

    // 4. Add OutputPass (handles color space conversion) - usually last
    const outputPass = new OutputPass();
    composer.addPass(outputPass);
    ```

4.  **Render via Composer:** In your animation loop, call `composer.render(deltaTime)` **instead of** `renderer.render(scene, camera)`. Pass the time delta if any passes require it for animation.

    ```javascript
    const clock = new THREE.Clock();

    function animate() {
        const deltaTime = clock.getDelta();

        // ... update scene, controls, etc. ...

        // Render using the composer
        composer.render(deltaTime);

        requestAnimationFrame(animate);
    }
    animate();
    ```

5.  **Handle Resize:** Update the composer's size and pixel ratio when the window resizes, similar to the renderer and camera. Also update the resolution uniform for passes that require it (like `UnrealBloomPass`).

    ```javascript
    function onWindowResize() {
        // ... update camera aspect and projection matrix ...
        // ... update renderer size and pixel ratio ...

        // Update composer size and pixel ratio
        composer.setSize(window.innerWidth, window.innerHeight);
        composer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

        // Update resolution for passes that need it
        bloomPass.resolution.set(window.innerWidth, window.innerHeight);
    }
    window.addEventListener('resize', onWindowResize);
    ```

Post-processing allows adding complex full-screen effects efficiently. Use `EffectComposer`, start with `RenderPass`, add effect passes like `UnrealBloomPass` or custom `ShaderPass`, end with `OutputPass`, and render using `composer.render()` in your animation loop. Remember to update sizes on resize.

*(Refer to the official Three.js documentation on Post-processing and `EffectComposer`.)*