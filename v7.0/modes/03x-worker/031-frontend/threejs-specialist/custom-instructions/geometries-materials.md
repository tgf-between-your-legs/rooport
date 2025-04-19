# Three.js: Geometries & Materials

Defining the shape and appearance of objects in a 3D scene.

## Core Concept: `Mesh`

Most visible objects in Three.js are `Mesh` objects. A `Mesh` requires two things:

1.  **Geometry:** Defines the shape or structure of the object (vertices, faces, UVs, normals).
2.  **Material:** Defines how the surface of the object looks (color, texture, shininess, transparency, how it reacts to light).

```javascript
import * as THREE from 'three';

// 1. Create Geometry
const geometry = new THREE.BoxGeometry(1, 1, 1); // A simple 1x1x1 cube

// 2. Create Material
const material = new THREE.MeshStandardMaterial({
  color: 0x00ff00, // Green
  roughness: 0.5,
  metalness: 0.5
});

// 3. Create Mesh
const cube = new THREE.Mesh(geometry, material);

// 4. Add to Scene
// scene.add(cube);
```

## Geometries (`THREE.*Geometry`)

*   **Built-in Geometries:** Three.js provides constructors for common shapes:
    *   `BoxGeometry(width, height, depth, ...)`
    *   `SphereGeometry(radius, widthSegments, heightSegments, ...)`
    *   `PlaneGeometry(width, height, ...)`
    *   `CylinderGeometry(...)`
    *   `ConeGeometry(...)`
    *   `TorusGeometry(...)`
    *   `TorusKnotGeometry(...)`
    *   ... and more.
*   **`BufferGeometry`:** The base class for all geometries. Represents geometry data efficiently using `BufferAttribute` objects (typed arrays) for positions, normals, UVs, colors, etc.
    *   You can create custom geometries by defining your own `BufferAttribute`s and adding them to a `BufferGeometry`.
    *   Loaders (like `GLTFLoader`) typically return `BufferGeometry`.
    ```javascript
    // Example: Custom triangle geometry
    const geometry = new THREE.BufferGeometry();
    const vertices = new Float32Array([
      -1.0, -1.0,  1.0, // v0
       1.0, -1.0,  1.0, // v1
       1.0,  1.0,  1.0, // v2
    ]);
    // Item size = 3 because each vertex has 3 values (x, y, z)
    geometry.setAttribute('position', new THREE.BufferAttribute(vertices, 3));
    geometry.computeVertexNormals(); // Calculate normals for lighting
    ```
*   **Disposal:** Call `geometry.dispose()` when a geometry is no longer needed to free up GPU memory.

## Materials (`THREE.*Material`)

Define the surface appearance.

*   **Common Properties:**
    *   `color`: Base color (often takes a hex number like `0xff0000` or a `THREE.Color` object).
    *   `map`: Texture map (requires a `THREE.Texture` object, usually loaded with `TextureLoader`).
    *   `transparent`: Boolean, whether the material is transparent.
    *   `opacity`: Number (0-1), how transparent the material is (requires `transparent: true`).
    *   `wireframe`: Boolean, render as wireframe.
    *   `side`: `THREE.FrontSide` (default), `THREE.BackSide`, `THREE.DoubleSide`.
*   **Common Material Types:**
    *   `MeshBasicMaterial`: Simple material, not affected by lights. Good for unlit scenes or simple colors/textures.
        ```javascript
        const basicMat = new THREE.MeshBasicMaterial({ color: 0xff0000, map: texture });
        ```
    *   `MeshStandardMaterial`: Physically Based Rendering (PBR) material. Standard for realistic rendering. Reacts to lights. Uses properties like:
        *   `roughness`: How rough the surface is (0=smooth mirror, 1=fully diffuse).
        *   `metalness`: How metallic the surface is (0=dielectric/non-metal, 1=fully metallic).
        *   `normalMap`: Texture for simulating surface detail.
        *   `aoMap` (Ambient Occlusion), `emissiveMap`, `metalnessMap`, `roughnessMap`, etc.
        ```javascript
        const standardMat = new THREE.MeshStandardMaterial({
          color: 0xffffff,
          map: colorTexture,
          normalMap: normalTexture,
          roughness: 0.2,
          metalness: 0.8
        });
        ```
    *   `MeshPhysicalMaterial`: Extends `MeshStandardMaterial` with more advanced PBR properties like `clearcoat`, `transmission`, `thickness`, `ior`.
    *   `MeshPhongMaterial` / `MeshLambertMaterial`: Older, less physically accurate lighting models. Still useful sometimes but `MeshStandardMaterial` is generally preferred.
    *   `PointsMaterial`: For rendering particles (`THREE.Points`).
    *   `LineBasicMaterial` / `LineDashedMaterial`: For rendering lines (`THREE.Line`, `THREE.LineSegments`).
    *   `ShaderMaterial`: For using custom vertex and fragment shaders written in GLSL. Provides complete control over rendering. (See `shader-material-glsl.md`)
        ```javascript
        const shaderMat = new THREE.ShaderMaterial({
          uniforms: { /* ... */ },
          vertexShader: /* GLSL string */,
          fragmentShader: /* GLSL string */
        });
        ```
*   **Disposal:** Call `material.dispose()` when a material is no longer needed. If it uses textures, dispose of those too (`texture.dispose()`).

*(Refer to the official Three.js documentation for specific Geometry and Material types and their properties.)*