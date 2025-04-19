# Three.js: Materials

Defining the surface appearance of 3D objects using Three.js materials.

## Core Concept: Material Defines Appearance

While Geometry defines the shape, **Material** defines how the surface of that shape looks. It determines properties like color, texture, shininess, transparency, and how the object interacts with light.

**Key Points:**

*   Every `Mesh` object requires both a `Geometry` and a `Material`.
*   Materials are created by instantiating specific material classes provided by Three.js.
*   Different materials have different properties and performance characteristics, suited for different visual effects and rendering needs.
*   Materials interact with lights in the scene (except for basic materials like `MeshBasicMaterial`).

## Common Material Types

1.  **`MeshBasicMaterial`:**
    *   **Appearance:** Simple, flat shading. Not affected by lights.
    *   **Use Cases:** Debugging, simple unlit objects, UI elements in 3D space.
    *   **Key Props:** `color` (color value, e.g., `0xff0000`), `map` (texture), `wireframe` (boolean), `opacity`, `transparent`.

    ```javascript
    const basicMaterial = new THREE.MeshBasicMaterial({
      color: 0x00ff00, // Green
      wireframe: true,
    });
    ```

2.  **`MeshStandardMaterial`:**
    *   **Appearance:** Physically Based Rendering (PBR) material. Aims for realistic appearance by simulating real-world light interaction. **Most common material for realistic rendering.**
    *   **Use Cases:** Realistic objects, standard rendering pipeline. Requires lights in the scene.
    *   **Key Props:**
        *   `color`: Base color (albedo).
        *   `map`: Color texture (albedo map).
        *   `metalness`: How metallic the surface is (0 = dielectric, 1 = metal).
        *   `roughness`: How rough the surface is (0 = smooth/shiny, 1 = rough/diffuse).
        *   `metalnessMap`: Texture controlling metalness.
        *   `roughnessMap`: Texture controlling roughness.
        *   `normalMap`: Texture simulating fine surface detail/bumps.
        *   `aoMap` (Ambient Occlusion): Texture simulating shadows in crevices.
        *   `envMap`: Texture for environment reflections.
        *   `emissive`, `emissiveMap`, `emissiveIntensity`: Make parts of the material glow.
        *   `transparent`, `opacity`, `alphaMap`: Control transparency.

    ```javascript
    const standardMaterial = new THREE.MeshStandardMaterial({
      color: 0xffffff,
      map: colorTexture, // Assign a loaded THREE.Texture
      roughness: 0.2,
      metalness: 0.8,
      normalMap: normalTexture,
      aoMap: aoTexture,
      // aoMapIntensity: 1,
    });
    ```

3.  **`MeshPhysicalMaterial`:**
    *   **Appearance:** An extension of `MeshStandardMaterial` adding more advanced PBR properties.
    *   **Use Cases:** Simulating complex surfaces like glass, clear coats, subsurface scattering.
    *   **Key Props (in addition to Standard):** `transmission` (light passing through, for glass), `ior` (index of refraction), `thickness`, `clearcoat`, `clearcoatRoughness`, `sheen`, `specularIntensity`, `specularColor`.

    ```javascript
    const physicalMaterial = new THREE.MeshPhysicalMaterial({
      color: 0xffffff,
      metalness: 0.1,
      roughness: 0.05,
      transmission: 1.0, // Make it transparent like glass
      ior: 1.5, // Index of refraction for glass
      thickness: 0.5, // Thickness affects refraction
    });
    ```

4.  **`MeshLambertMaterial`:**
    *   **Appearance:** Simple diffuse lighting model (calculates light per vertex). Less realistic than Standard/Physical, but computationally cheaper.
    *   **Use Cases:** Simple shaded objects where performance is critical and high realism isn't needed.

5.  **`MeshPhongMaterial`:**
    *   **Appearance:** Calculates lighting per pixel, includes specular highlights (shininess). More realistic than Lambert, less realistic but often cheaper than Standard/Physical.
    *   **Use Cases:** Shiny non-metallic surfaces when PBR isn't required.

6.  **`ShaderMaterial` / `RawShaderMaterial`:**
    *   **Appearance:** Completely custom appearance defined by vertex and fragment shaders written in GLSL.
    *   **Use Cases:** Advanced visual effects, non-photorealistic rendering, unique material behaviors. Requires knowledge of GLSL. (See `threejs-custom-shaders-glsl.md`).

    ```javascript
    const shaderMaterial = new THREE.ShaderMaterial({
      uniforms: { /* ... uniforms ... */ },
      vertexShader: /* ... GLSL vertex shader code ... */,
      fragmentShader: /* ... GLSL fragment shader code ... */,
      // side: THREE.DoubleSide,
      // transparent: true,
    });
    ```

7.  **Other Materials:** `PointsMaterial` (for `THREE.Points`), `LineBasicMaterial`/`LineDashedMaterial` (for `THREE.Line`), `SpriteMaterial` (for `THREE.Sprite`), `MeshDepthMaterial`, `MeshNormalMaterial`.

## Common Material Properties

*   `color`: Base color (`THREE.Color` object or hex value).
*   `map`: Texture map (`THREE.Texture` object).
*   `side`: Which side(s) to render (`THREE.FrontSide`, `THREE.BackSide`, `THREE.DoubleSide`). Default is `FrontSide`.
*   `transparent`: Boolean indicating if the material allows transparency.
*   `opacity`: Float between 0 (fully transparent) and 1 (fully opaque). Requires `transparent: true`.
*   `alphaMap`: Grayscale texture controlling opacity per pixel. Requires `transparent: true`.
*   `wireframe`: Boolean to render as wireframe.
*   `visible`: Boolean to toggle visibility.

Choose the material that best suits the desired visual appearance and performance requirements. `MeshStandardMaterial` is the modern default for realistic, lit objects. Remember to dispose of materials when no longer needed (`material.dispose()`).

*(Refer to the official Three.js documentation on Materials.)*