# Three.js: Resource Disposal & Memory Management

Manually freeing up GPU memory by disposing of unused Three.js objects.

## Core Concept: Manual GPU Memory Management

When you create Three.js objects like geometries, materials, and textures, they consume memory not only in JavaScript (CPU RAM) but also on the GPU (VRAM). The JavaScript garbage collector automatically cleans up CPU memory when objects are no longer referenced, but it **does not manage GPU memory**.

If you remove an object (like a `Mesh`) from the scene, the associated geometry, material, and textures might still reside in GPU memory. Failing to explicitly release these resources can lead to memory leaks, eventually crashing the browser tab or degrading performance significantly.

**Key Principle:** You must manually call the `.dispose()` method on geometries, materials, and textures when you are certain they will no longer be used anywhere in your scene.

## When to Dispose

*   **Dynamically Removing Objects:** If you remove a `Mesh` or `Group` from the scene and won't be adding it back later.
*   **Replacing Materials/Geometries:** If you assign a new material or geometry to a mesh, the old one might need disposal if it's not used elsewhere.
*   **Changing Textures:** If you load a new texture and apply it to a material, the old texture might need disposal if it's not used by other materials.
*   **Component Unmount (Frameworks):** In frameworks like React, Vue, or Svelte, the cleanup function of `useEffect` or the component's unmount lifecycle method is the ideal place to dispose of resources created by that component.

## How to Dispose

Call the `.dispose()` method on the specific object:

*   **Geometry:** `geometry.dispose()`
*   **Material:** `material.dispose()`
    *   Note: If a material is shared by multiple meshes, only dispose of it when *all* meshes using it are removed.
*   **Texture:** `texture.dispose()`
    *   Note: Similar to materials, only dispose if the texture isn't used by other materials.

**Traversing Scene Graph for Disposal:**

When removing a complex object (like a loaded model `gltf.scene` which is often a `Group`), you need to traverse its children to dispose of all unique geometries and materials.

```javascript
import * as THREE from 'three';

function disposeNode(node) {
    if (node instanceof THREE.Mesh) {
        // Dispose geometry
        if (node.geometry) {
            node.geometry.dispose();
            // console.log("Disposed geometry:", node.geometry.uuid);
        }

        // Dispose material(s)
        // Check if material is an array (multiple materials)
        if (Array.isArray(node.material)) {
            node.material.forEach(material => {
                disposeMaterial(material);
            });
        } else if (node.material) {
            disposeMaterial(node.material);
        }
    }
}

function disposeMaterial(material) {
    // console.log("Disposing material:", material.uuid);
    material.dispose(); // Dispose the material itself

    // Dispose textures used by the material
    for (const key in material) {
        const value = material[key];
        // Check if property is a texture and has a dispose method
        if (value instanceof THREE.Texture && typeof value.dispose === 'function') {
            // console.log("Disposing texture:", value.uuid);
            value.dispose();
        }
    }
}

// --- Example Usage ---
// Assuming 'modelToRemove' is a THREE.Group or THREE.Mesh loaded earlier
if (modelToRemove) {
    console.log("Removing and disposing model:", modelToRemove.uuid);

    // Traverse the object and its children
    modelToRemove.traverse(disposeNode);

    // Remove the object from the scene
    scene.remove(modelToRemove);

    console.log("Model removed and resources disposed.");
}

// --- Example in React ---
// useEffect(() => {
//   // ... setup Three.js scene, load model ...
//   const model = gltf.scene;
//   scene.add(model);
//
//   // Cleanup function
//   return () => {
//     console.log("React component unmounting, disposing Three.js resources...");
//     model.traverse(disposeNode);
//     scene.remove(model);
//     // Dispose renderer, controls, etc. if necessary
//     // renderer.dispose();
//   };
// }, []); // Empty dependency array means run on mount/unmount
```

**Important Notes:**

*   **Render Targets:** If using `EffectComposer` or manual render targets (`WebGLRenderTarget`), dispose of them too: `renderTarget.dispose()`.
*   **Renderer Context:** While less common for typical leaks, in extreme cases or single-page apps where the WebGL context might persist longer than needed, you might call `renderer.dispose()` when the entire application/canvas is destroyed.
*   **Double Check:** Be careful not to dispose of resources still in use elsewhere in your scene.

Proper resource disposal is crucial for stable, long-running Three.js applications. Always call `.dispose()` on geometries, materials, and textures when they are permanently removed from the scene. Use traversal for complex objects and leverage framework cleanup functions.

*(Refer to the official Three.js documentation on How to dispose of objects.)*