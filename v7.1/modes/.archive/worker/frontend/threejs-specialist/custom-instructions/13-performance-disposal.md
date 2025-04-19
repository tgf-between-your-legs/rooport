# Performance Optimization &amp; Resource Disposal

Strategies for improving the performance of Three.js applications and managing memory effectively.

## A. Performance Optimization

Performance is critical for smooth user experiences in WebGL. Focus on minimizing both CPU and GPU bottlenecks.

**1. Reduce Draw Calls (CPU Bound)**

*   **Problem:** Each `Mesh`, `Line`, `Points` object often results in at least one draw call. Too many draw calls overwhelm the CPU preparing data for the GPU.
*   **Solutions:**
    *   **Merge Geometries:** Combine multiple static geometries *that share the same material* into a single `BufferGeometry` using `BufferGeometryUtils.mergeGeometries()` or `BufferGeometryUtils.mergeBufferGeometries()`. Best for static scenery.
    *   **Instanced Rendering (`InstancedMesh`):** Render many copies of the *same geometry* with potentially different transformations (position, rotation, scale) and colors using a single draw call. Ideal for forests, crowds, particle systems. You provide transformation matrices and optionally colors per instance.
    *   **Use `Points`:** For large numbers of small, billboarded objects (particles), use `THREE.Points` with `PointsMaterial` instead of many small meshes.

**2. Optimize Geometry (GPU Vertex Bound)**

*   **Problem:** High polygon counts increase GPU load for vertex processing and consume more memory.
*   **Solutions:**
    *   **Lower Poly Counts:** Use models with fewer vertices/faces where possible, especially for distant or less important objects. Work with modelers to optimize assets.
    *   **Level of Detail (`LOD`):** Use the `THREE.LOD` object to automatically switch between different versions of a model (high-poly, medium-poly, low-poly) based on its distance from the camera. Requires creating multiple versions of the geometry.
    *   **Share Geometries:** If multiple meshes use the exact same geometry, create the geometry *once* and reuse the instance for each mesh.

**3. Optimize Materials &amp; Textures (GPU Fragment Bound &amp; Memory)**

*   **Problem:** Complex materials and large/many textures consume significant GPU memory (VRAM) and bandwidth. Fragment shader complexity increases GPU load per pixel.
*   **Solutions:**
    *   **Share Materials:** Reuse the same material instance for multiple meshes if they have identical appearance.
    *   **Texture Atlases:** Combine multiple small textures into a single larger texture sheet (atlas). Adjust UV coordinates accordingly. Reduces texture switching overhead.
    *   **Texture Compression:** **Highly Recommended.** Use compressed formats like KTX2 (Basis Universal) loaded via `KTX2Loader`. Significantly reduces GPU memory usage and loading times compared to JPG/PNG.
    *   **Texture Dimensions:** Use power-of-two (POT) dimensions (e.g., 512x512, 1024x1024) where possible, especially for mipmapping or repeating textures. Keep texture sizes appropriate for the object's on-screen size. Avoid unnecessarily large textures.
    *   **Mipmapping:** Generally keep enabled (`texture.generateMipmaps = true`, default) for POT textures. Improves quality and performance for textures viewed at a distance.
    *   **Material Choice:** Use the simplest material possible (`MeshBasicMaterial` is fastest, `MeshStandardMaterial` is generally preferred for lit scenes over older Phong/Lambert). Avoid `MeshPhysicalMaterial` features unless necessary.
    *   **Shader Optimization:** If using `ShaderMaterial`, optimize GLSL code (see `11-custom-shaders-glsl.md`).

**4. Optimize Lighting &amp; Shadows (GPU Bound)**

*   **Problem:** Real-time lighting and especially shadows are computationally expensive.
*   **Solutions:**
    *   **Limit Lights:** Use fewer dynamic lights. Prefer `AmbientLight`, `HemisphereLight`, `DirectionalLight` over `PointLight` and `SpotLight` where possible.
    *   **Bake Lighting:** For static scenes, bake lighting information into textures (lightmaps) using external tools (e.g., Blender). This drastically reduces real-time lighting cost. Apply lightmaps to `material.lightMap`. Requires `uv2` attribute.
    *   **Shadows:**
        *   Minimize lights casting shadows (`light.castShadow = true`).
        *   Minimize objects casting/receiving shadows (`mesh.castShadow = true`, `mesh.receiveShadow = true`).
        *   **Optimize Shadow Map Resolution:** (`light.shadow.mapSize.width/height`). Use the lowest acceptable power-of-two value (e.g., 512, 1024). Higher values drastically increase cost.
        *   **Tighten Shadow Camera Frustum:** Adjust the shadow camera (`light.shadow.camera.near/far/left/right/top/bottom`) to fit *only* the area where shadows are needed. Use helpers (`CameraHelper`) to visualize.
        *   Adjust `light.shadow.bias` and `light.shadow.normalBias` carefully to prevent shadow acne and peter-panning.
        *   Consider disabling shadows for objects far from the camera.

**5. Optimize Rendering Loop &amp; JavaScript (CPU Bound)**

*   **Avoid Work in Render Loop:** Minimize calculations, object creation (`new`), or complex logic inside `requestAnimationFrame`. Perform setup outside the loop. Cache values where possible.
*   **Conditional Rendering:** Only render the scene (`renderer.render(scene, camera)`) when necessary (e.g., camera moved, animation updated, user interacted). For static scenes, render only once or on demand.
*   **`onDemand` Rendering with Controls:** If using controls like `OrbitControls`, listen for the `change` event and trigger a render, instead of rendering continuously in the loop (unless `enableDamping` or `autoRotate` is true).

**6. Profiling Tools**

*   **Browser DevTools:** Use the Performance tab to identify CPU bottlenecks in JavaScript. Use memory snapshots to track JS heap size.
*   **`stats.js`:** Simple library to display FPS and memory usage overlay.
*   **Spector.js:** Browser extension for detailed WebGL frame debugging (draw calls, shaders, textures, state). Invaluable for GPU diagnosis.
*   **Three.js DevTools:** Browser extension for inspecting scene graph, materials, textures, etc.

## B. Resource Disposal (Memory Management)

**Problem:** JavaScript's garbage collector handles CPU memory, but **not GPU memory**. Geometries, materials, textures, and render targets uploaded to the GPU must be manually disposed of when no longer needed to prevent memory leaks.

**When to Dispose:**

*   Dynamically removing objects/models from the scene permanently.
*   Replacing materials/geometries/textures on existing objects if the old ones aren't used elsewhere.
*   In component cleanup functions (e.g., React `useEffect` return function, Vue `unmounted`, Svelte `onDestroy`).

**How to Dispose:**

*   **Geometry:** `geometry.dispose()`
*   **Material:** `material.dispose()`
*   **Texture:** `texture.dispose()`
*   **Render Target:** `renderTarget.dispose()`
*   **Renderer:** `renderer.dispose()` (When the entire canvas/app is destroyed)
*   **Controls:** `controls.dispose()` (Removes event listeners)

**Traversal for Complex Objects:** When removing a group or loaded model, traverse its children to dispose of all unique geometries, materials, and textures.

```javascript
function disposeNode(node) {
    if (node instanceof THREE.Mesh) {
        if (node.geometry) {
            node.geometry.dispose();
        }
        // Dispose material(s) - handle arrays and check for shared materials if necessary
        if (Array.isArray(node.material)) {
            node.material.forEach(disposeMaterial);
        } else if (node.material) {
            disposeMaterial(node.material);
        }
    }
}

function disposeMaterial(material) {
    material.dispose(); // Dispose the material itself
    // Dispose textures used by the material
    for (const key of Object.keys(material)) {
        const value = material[key];
        if (value instanceof THREE.Texture && typeof value.dispose === 'function') {
            value.dispose();
        }
    }
}

// --- Usage ---
// Assuming 'modelToRemove' is a THREE.Group or THREE.Mesh
if (modelToRemove) {
    modelToRemove.traverse(disposeNode); // Dispose resources within the model
    scene.remove(modelToRemove); // Remove from scene
}
```

**Key Takeaway:** Performance optimization is iterative: profile, identify bottlenecks, apply targeted fixes. **Always dispose of GPU resources (geometries, materials, textures) manually using `.dispose()` when they are no longer needed.**