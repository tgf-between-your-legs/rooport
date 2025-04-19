# Three.js: Performance Optimization Techniques

Strategies for improving the rendering speed and efficiency of Three.js scenes.

## Core Concept: Reducing GPU & CPU Load

Three.js performance depends on both the GPU (drawing pixels, running shaders) and the CPU (managing the scene graph, calculating animations, sending instructions to the GPU). Optimization involves reducing the workload on both.

**Key Areas for Optimization:**

1.  **Draw Calls:** Each separate object/material combination often results in a draw call. The GPU can handle a limited number per frame. Reducing draw calls is often the most significant optimization.
2.  **Geometry Complexity:** High polygon counts increase the data sent to the GPU and the work needed per vertex.
3.  **Texture Size & Format:** Large, uncompressed textures consume significant GPU memory and bandwidth.
4.  **Lighting & Shadows:** Complex lighting setups and high-resolution shadow maps are very GPU-intensive.
5.  **Shaders:** Complex fragment shaders run for every pixel and can heavily impact GPU performance.
6.  **JavaScript Logic:** Complex calculations, frequent scene graph manipulations, or inefficient code in the render loop increase CPU load.
7.  **Memory Management:** Failing to dispose of unused geometries, materials, and textures leads to memory leaks.

## Common Optimization Techniques

1.  **Reduce Draw Calls:**
    *   **Instancing (`THREE.InstancedMesh`):** Draw many identical (or similar) objects with slight variations (position, rotation, color) in a single draw call. Ideal for things like trees, grass, particles.
    *   **Merge Geometries (`BufferGeometryUtils.mergeGeometries`):** Combine multiple static geometries (with the *same* material) into a single `BufferGeometry`. Reduces draw calls but makes individual objects harder to manipulate later.
    *   **Use Texture Atlases:** Combine multiple small textures into a single larger texture sheet. Allows multiple objects to share the same material, reducing draw calls if they can be merged or instanced.

2.  **Simplify Geometry:**
    *   **Lower Polygon Count:** Use lower-poly models where possible, especially for objects far from the camera or in large numbers.
    *   **Level of Detail (`THREE.LOD`):** Automatically switch between high-detail and low-detail versions of a model based on its distance from the camera.

3.  **Optimize Textures:**
    *   **Resize Textures:** Use the smallest texture dimensions necessary for the desired visual quality. Avoid unnecessarily large textures.
    *   **Use Compressed Formats:** Use `.ktx2` textures with Basis Universal compression (loaded via `KTX2Loader`). This significantly reduces file size and GPU memory usage compared to JPG/PNG.
    *   **Mipmapping:** Ensure mipmaps are generated (`texture.generateMipmaps = true`, default) for textures viewed at various distances (requires power-of-two dimensions for best results/compatibility).

4.  **Optimize Lighting & Shadows:**
    *   **Limit Shadow Casters:** Only enable `castShadow` on necessary lights and objects.
    *   **Optimize Shadow Map Size (`light.shadow.mapSize`):** Reduce resolution (e.g., 512x512 instead of 2048x2048) if high detail isn't needed. Powers of 2 are required.
    *   **Optimize Shadow Camera Frustum:** Make the `light.shadow.camera` frustum (near, far, left, right, top, bottom) as tight as possible around the area where shadows are needed. Use `CameraHelper` to visualize.
    *   **Avoid Excessive Lights:** Fewer lights generally mean better performance. Consider baking lighting into textures for static scenes.

5.  **Optimize Shaders:**
    *   **Prefer Built-in Materials:** Use `MeshStandardMaterial` or `MeshBasicMaterial` over `ShaderMaterial` unless custom effects are essential.
    *   **Simplify GLSL:** If using custom shaders, keep calculations minimal, especially in the fragment shader. Move calculations to the vertex shader if possible (runs per vertex instead of per pixel). Use lower precision (`mediump`, `lowp`) if acceptable.

6.  **Optimize JavaScript:**
    *   **Minimize Work in Render Loop:** Perform calculations outside the `animate` function whenever possible. Avoid creating new objects (`new THREE.Vector3()`) inside the loop; reuse objects instead.
    *   **Throttle Expensive Operations:** Debounce or throttle raycasting or other calculations tied to frequent events like `mousemove`.

7.  **Manage Memory:**
    *   **Dispose Resources:** Explicitly call `.dispose()` on geometries, materials, and textures when they are removed from the scene and no longer needed to free up GPU memory.

## Profiling

*   **Browser DevTools (Performance Tab):** Profile JavaScript execution time to find CPU bottlenecks in your render loop or event handlers.
*   **`renderer.info`:** Log `renderer.info.render.calls` and `renderer.info.render.triangles` to monitor draw calls and polygon counts.
*   **Stats.js:** A simple library to display FPS and other performance metrics on screen.
*   **Spector.js:** A browser extension for detailed WebGL frame debugging, showing individual draw calls, shader code, and state changes. Essential for deep dives into GPU bottlenecks.

Performance optimization is an iterative process. Profile your scene to identify bottlenecks, then apply appropriate techniques focusing on reducing draw calls, simplifying geometry/textures, and optimizing lighting/shaders. Always test the impact of optimizations.

*(Refer to the official Three.js documentation on Performance and specific optimization techniques like InstancedMesh, LOD, BufferGeometryUtils.)*