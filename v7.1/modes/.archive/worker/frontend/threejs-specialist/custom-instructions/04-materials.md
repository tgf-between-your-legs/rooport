# Materials

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
    *   **Use Cases:** Debugging, simple unlit objects, UI elements in 3D space, wireframes.
    *   **Key Props:** `color`, `map`, `wireframe`, `opacity`, `transparent`, `side`.

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
        *   `metalnessMap`: Texture controlling metalness (usually packed in RGB channels with roughness or AO).
        *   `roughnessMap`: Texture controlling roughness.
        *   `normalMap`: Texture simulating fine surface detail/bumps.
        *   `normalScale`: `Vector2` controlling the strength of the normal map.
        *   `aoMap` (Ambient Occlusion): Texture simulating shadows in crevices. Requires `uv2` attribute on geometry.
        *   `aoMapIntensity`: Strength of the AO map.
        *   `envMap`: Texture for environment reflections (`CubeTexture` or equirectangular).
        *   `envMapIntensity`: Strength of environment map reflections.
        *   `emissive`, `emissiveMap`, `emissiveIntensity`: Make parts of the material glow.
        *   `transparent`, `opacity`, `alphaMap`: Control transparency.
        *   `side`: `THREE.FrontSide`, `THREE.BackSide`, `THREE.DoubleSide`.

    ```javascript
    const standardMaterial = new THREE.MeshStandardMaterial({
      color: 0xffffff,
      map: colorTexture, // Assign a loaded THREE.Texture
      roughness: 0.2,
      metalness: 0.8,
      normalMap: normalTexture,
      normalScale: new THREE.Vector2(1, 1),
      aoMap: aoTexture,
      aoMapIntensity: 1,
      envMap: environmentMapTexture, // Assign a loaded CubeTexture or equirectangular texture
      envMapIntensity: 1.0,
    });
    ```

3.  **`MeshPhysicalMaterial`:**
    *   **Appearance:** An extension of `MeshStandardMaterial` adding more advanced PBR properties for complex surfaces.
    *   **Use Cases:** Simulating glass, clear coats (car paint), subsurface scattering (skin, wax), thin films (bubbles), fabric sheen.
    *   **Key Props (in addition to Standard):**
        *   `transmission`: Amount of light passing through (0 to 1). For glass/water effects. Requires careful scene setup (multiple renders or buffer techniques).
        *   `ior` (Index of Refraction): Controls how much light bends when passing through transmissive material (e.g., ~1.5 for glass).
        *   `thickness`: Thickness of the transmissive volume (affects refraction). Requires `thicknessMap` if varying.
        *   `clearcoat`: Adds a thin, reflective layer on top (0 to 1).
        *   `clearcoatRoughness`: Roughness of the clearcoat layer.
        *   `sheen`: Simulates light scattering on microfibers (for fabrics like velvet).
        *   `sheenColor`, `sheenRoughness`.
        *   `specularIntensity`, `specularColor`: Control non-metallic reflection intensity and color.

    ```javascript
    const glassMaterial = new THREE.MeshPhysicalMaterial({
      color: 0xffffff,
      metalness: 0.0,
      roughness: 0.0,
      transmission: 1.0, // Make it transparent like glass
      ior: 1.5,
      // thickness: 0.1, // Optional: For refraction depth
      // clearcoat: 1.0, // Optional: Add a clear coat
      // clearcoatRoughness: 0.1,
    });
    ```

4.  **`MeshLambertMaterial`:**
    *   **Appearance:** Simple diffuse lighting model (calculates light per vertex). Less realistic than Standard/Physical, but computationally cheaper. Can look faceted on low-poly models.
    *   **Use Cases:** Simple shaded objects where performance is critical and high realism isn't needed.

5.  **`MeshPhongMaterial`:**
    *   **Appearance:** Calculates lighting per pixel, includes specular highlights (shininess). More realistic than Lambert, less realistic but often cheaper than Standard/Physical.
    *   **Use Cases:** Shiny non-metallic surfaces when PBR isn't required or performance is a concern. Key props: `specular` (color), `shininess` (float).

6.  **`ShaderMaterial` / `RawShaderMaterial`:**
    *   **Appearance:** Completely custom appearance defined by vertex and fragment shaders written in GLSL.
    *   **Use Cases:** Advanced visual effects, non-photorealistic rendering, unique material behaviors. Requires knowledge of GLSL. (See `11-custom-shaders-glsl.md`).

7.  **Other Materials:** `PointsMaterial` (for `THREE.Points`), `LineBasicMaterial`/`LineDashedMaterial` (for `THREE.Line`), `SpriteMaterial` (for `THREE.Sprite`), `MeshDepthMaterial` (renders depth), `MeshNormalMaterial` (renders normals as colors).

## Common Material Properties

*   `color`: Base color (`THREE.Color` object or hex value).
*   `map`: Texture map (`THREE.Texture` object).
*   `side`: Which side(s) to render (`THREE.FrontSide`, `THREE.BackSide`, `THREE.DoubleSide`). Default is `FrontSide`. Use `DoubleSide` carefully as it disables some GPU optimizations.
*   `transparent`: Boolean indicating if the material allows transparency. Necessary for `opacity < 1` or `alphaMap`.
*   `opacity`: Float between 0 (fully transparent) and 1 (fully opaque). Requires `transparent: true`.
*   `alphaMap`: Grayscale texture controlling opacity per pixel. Requires `transparent: true`. White = opaque, black = transparent.
*   `alphaTest`: Float (0-1). Fragments with alpha below this threshold are discarded. Useful for hard-edged transparency without blending issues (like leaves).
*   `depthWrite`: Boolean. Whether this material writes to the depth buffer. Set to `false` for transparent objects that should not obscure objects behind them (render transparent objects last).
*   `depthTest`: Boolean. Whether this material should be depth-tested against the depth buffer.
*   `wireframe`: Boolean to render as wireframe.
*   `visible`: Boolean to toggle visibility.

Choose the material that best suits the desired visual appearance and performance requirements. `MeshStandardMaterial` is the modern default for realistic, lit objects. Remember to dispose of materials when no longer needed (`material.dispose()`).