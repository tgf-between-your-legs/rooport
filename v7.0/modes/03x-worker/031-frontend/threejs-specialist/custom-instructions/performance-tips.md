# Three.js Performance Optimization Tips

Strategies for improving the performance of Three.js applications.

## 1. Reduce Draw Calls

*   **Problem:** Each `Mesh` (or `Points`, `Line`) often results in at least one draw call to the GPU. Too many draw calls can bottleneck the CPU.
*   **Solutions:**
    *   **Merge Geometries:** Combine multiple static geometries with the *same material* into a single `BufferGeometry` using `BufferGeometryUtils.mergeGeometries()`. This creates one larger mesh, reducing draw calls significantly. Best for static scenery.
    *   **Instanced Rendering (`InstancedMesh`):** Render many identical (or similar) geometries with slight variations (position, rotation, scale, color) using a single draw call. Ideal for things like forests, crowds, particle systems where the base geometry is the same. You provide transformation matrices (and optionally colors) for each instance.
    *   **Use Sprites/Points:** For large numbers of small, billboarded objects (like particles), use `THREE.Points` with `PointsMaterial` instead of many small meshes.

## 2. Optimize Geometry

*   **Problem:** High polygon counts increase GPU load for vertex processing and memory usage.
*   **Solutions:**
    *   **Lower Poly Counts:** Use lower-polygon models where possible, especially for objects far from the camera or less detailed elements.
    *   **Level of Detail (`LOD`):** Use the `THREE.LOD` object to automatically switch between different versions of a model (high-poly, medium-poly, low-poly) based on its distance from the camera.
    *   **Share Geometries:** If multiple meshes use the exact same geometry, create the geometry once and reuse it for each mesh instance.

## 3. Optimize Materials & Textures

*   **Problem:** Complex materials and large textures consume significant GPU memory and bandwidth.
*   **Solutions:**
    *   **Share Materials:** Reuse the same material instance for multiple meshes if they look identical.
    *   **Texture Atlases:** Combine multiple small textures into a single larger texture sheet (atlas). Adjust UV coordinates accordingly. Reduces texture switching overhead.
    *   **Texture Compression:** Use compressed texture formats like KTX2 (with Basis Universal) or DDS. Requires `KTX2Loader` or `DDSLoader`. Significantly reduces GPU memory usage and loading times.
    *   **Texture Dimensions:** Use power-of-two (POT) dimensions (e.g., 256x256, 512x512, 1024x1024) for textures where possible, especially if using mipmapping or certain compression formats/wrapping modes. Keep texture sizes reasonable for the object's screen size.
    *   **Mipmapping:** Enabled by default for POT textures. Helps reduce aliasing and improve performance when textures are viewed from a distance.
    *   **Material Choice:** Use the simplest material possible for the desired effect (`MeshBasicMaterial` is fastest, `MeshStandardMaterial` is generally preferred over older Phong/Lambert).

## 4. Optimize Lighting & Shadows

*   **Problem:** Real-time lighting and shadows are computationally expensive.
*   **Solutions:**
    *   **Limit Lights:** Use fewer dynamic lights. Consider baking lighting into textures (lightmaps) for static scenes.
    *   **Light Types:** `AmbientLight` and `HemisphereLight` are cheap. `DirectionalLight` is cheaper than `PointLight` or `SpotLight`.
    *   **Shadows:**
        *   Limit the number of lights casting shadows (`light.castShadow = true`).
        *   Limit the number of objects casting/receiving shadows (`mesh.castShadow = true`, `mesh.receiveShadow = true`).
        *   Optimize shadow map resolution (`light.shadow.mapSize.width/height`). Lower values are faster but lower quality. Use POT values.
        *   Adjust the shadow camera frustum (`light.shadow.camera.near/far/left/right/top/bottom`) to be as tight as possible around the shadow-casting area.
        *   Disable shadows for objects far from the camera.

## 5. Optimize Shaders (GLSL)

*   **Problem:** Complex calculations in custom shaders, especially the fragment shader, directly impact GPU performance.
*   **Solutions:**
    *   Move calculations from the fragment shader to the vertex shader whenever possible (calculations run per-vertex instead of per-pixel).
    *   Avoid branching (`if`/`else`) based on uniform values in shaders if possible.
    *   Use lower precision (`mediump` or `lowp`) for floats/vectors if full `highp` isn't necessary (especially on mobile).
    *   Minimize texture lookups in the fragment shader.

## 6. General JavaScript & Rendering Loop

*   **Avoid Work in Render Loop:** Minimize calculations, object creation, or complex logic within the `requestAnimationFrame` loop. Do setup work outside the loop.
*   **Conditional Rendering:** Only render the scene (`renderer.render(scene, camera)`) when necessary (e.g., if the camera moved, an animation updated, or user interacted). For static scenes, you might only need to render once or on demand.
*   **`onDemand` Rendering:** If using controls like `OrbitControls`, listen for the `change` event and trigger a render, instead of rendering continuously.
*   **Memory Management (`dispose()`):** Explicitly call `.dispose()` on geometries, materials, textures, render targets, etc., when they are removed from the scene and no longer needed to free up GPU memory.

## 7. Profiling

*   **Browser DevTools:** Use the performance profiler to identify CPU bottlenecks in your JavaScript code.
*   **`stats.js`:** A common library to display FPS and memory usage in the corner of the screen.
*   **Spector.js:** A browser extension for detailed WebGL frame debugging, showing draw calls, shader code, textures, and state. Invaluable for diagnosing GPU-related issues.

*(Performance optimization is often iterative. Profile first, identify bottlenecks, then apply targeted optimizations.)*