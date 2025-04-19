# Lights &amp; Shadows

Illuminating scenes and casting shadows with various light types in Three.js.

## Core Concept: Simulating Light

Most materials in Three.js (like `MeshStandardMaterial`, `MeshPhysicalMaterial`) react to light sources added to the scene. Without lights, these materials will typically appear black. Different light types simulate different kinds of real-world light sources.

Shadows add realism by simulating how objects block light, but they can be computationally expensive.

## Common Light Types

1.  **`AmbientLight`:**
    *   **Effect:** Illuminates all objects globally and equally from all directions. Does not cast shadows.
    *   **Use Case:** Provides basic fill light to prevent areas from being completely black. Often used in combination with other lights.
    *   **Props:** `color`, `intensity`.

    ```javascript
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.5); // White light, half intensity
    scene.add(ambientLight);
    ```

2.  **`DirectionalLight`:**
    *   **Effect:** Emits light in a specific direction, as if from an infinitely distant source (like the sun). Light rays are parallel. **Can cast shadows.**
    *   **Use Case:** Simulating sunlight or strong directional light sources.
    *   **Props:** `color`, `intensity`, `position` (determines direction - light shines *from* position *towards* target), `target` (object the light points at, defaults to scene origin).
    *   **Shadows:** Requires setting `castShadow = true` and configuring `shadow` properties.

    ```javascript
    const directionalLight = new THREE.DirectionalLight(0xffffff, 1.0);
    directionalLight.position.set(5, 10, 7); // Position determines direction
    directionalLight.castShadow = true; // Enable shadow casting
    // Configure shadow camera properties (adjust frustum to fit scene tightly)
    directionalLight.shadow.camera.near = 1;
    directionalLight.shadow.camera.far = 25;
    directionalLight.shadow.camera.left = -10;
    directionalLight.shadow.camera.right = 10;
    directionalLight.shadow.camera.top = 10;
    directionalLight.shadow.camera.bottom = -10;
    // Configure shadow map resolution (power of 2, higher = better quality but slower)
    directionalLight.shadow.mapSize.width = 1024; // Start lower (e.g., 512) and increase if needed
    directionalLight.shadow.mapSize.height = 1024;
    // Optional: Adjust shadow bias to prevent shadow acne/artifacts
    directionalLight.shadow.bias = -0.001;
    // Optional: Soften shadow edges (requires PCFSoftShadowMap on renderer)
    // directionalLight.shadow.radius = 4;
    scene.add(directionalLight);
    // Optional: Add a helper to visualize the light direction and shadow frustum
    // const dirLightHelper = new THREE.DirectionalLightHelper(directionalLight, 1);
    // scene.add(dirLightHelper);
    // const shadowCamHelper = new THREE.CameraHelper(directionalLight.shadow.camera);
    // scene.add(shadowCamHelper);
    ```

3.  **`PointLight`:**
    *   **Effect:** Emits light equally in all directions from a single point. Intensity diminishes with distance. **Can cast shadows** (omnidirectional, expensive).
    *   **Use Case:** Simulating light bulbs, candles, explosions.
    *   **Props:** `color`, `intensity`, `distance` (where light intensity becomes 0), `decay` (how intensity diminishes, 2 is physically correct), `position`.
    *   **Shadows:** Requires `castShadow = true`. Point light shadows are rendered using a cube map (6 renders), which is performance-intensive. Use sparingly.

    ```javascript
    const pointLight = new THREE.PointLight(0xffaa00, 1.5, 10, 2); // Color, Intensity, Distance, Decay
    pointLight.position.set(2, 3, 1);
    pointLight.castShadow = true; // Enable shadows (can be expensive!)
    // Configure shadow properties (near, far, bias)
    pointLight.shadow.mapSize.width = 512; // Keep resolution lower for point lights if possible
    pointLight.shadow.mapSize.height = 512;
    pointLight.shadow.camera.near = 0.5;
    pointLight.shadow.camera.far = 20;
    pointLight.shadow.bias = -0.005; // Bias might need more tweaking for point lights
    scene.add(pointLight);
    // Optional: Helper
    // const pointLightHelper = new THREE.PointLightHelper(pointLight, 0.5);
    // scene.add(pointLightHelper);
    ```

4.  **`SpotLight`:**
    *   **Effect:** Emits light in a cone shape from a point in a specific direction. Intensity diminishes with distance and angle. **Can cast shadows** (directional, like `DirectionalLight`).
    *   **Use Case:** Simulating flashlights, stage spotlights, focused lighting.
    *   **Props:** `color`, `intensity`, `distance`, `decay`, `angle` (cone angle), `penumbra` (softness of cone edge, 0-1), `position`, `target`.
    *   **Shadows:** Requires `castShadow = true`. Shadow configuration is similar to `DirectionalLight`.

    ```javascript
    const spotLight = new THREE.SpotLight(0xffffff, 3.0, 20, Math.PI * 0.15, 0.2, 1); // Color, Intensity, Distance, Angle, Penumbra, Decay
    spotLight.position.set(0, 10, 5);
    spotLight.target.position.set(0, 0, 0); // Point towards origin
    spotLight.castShadow = true;
    // Configure shadows (mapSize, camera near/far, bias)
    spotLight.shadow.mapSize.width = 1024;
    spotLight.shadow.mapSize.height = 1024;
    spotLight.shadow.camera.near = 1;
    spotLight.shadow.camera.far = 25;
    spotLight.shadow.bias = -0.002;
    // spotLight.shadow.focus = 1; // Optional focus adjustment (less common now)
    scene.add(spotLight);
    scene.add(spotLight.target); // Target needs to be added to scene too
    // Optional: Helper
    // const spotLightHelper = new THREE.SpotLightHelper(spotLight);
    // scene.add(spotLightHelper);
    // window.requestAnimationFrame(() => spotLightHelper.update()); // Update helper if target moves
    ```

5.  **`HemisphereLight`:**
    *   **Effect:** Simulates light coming from the sky (top color) and reflected from the ground (bottom color). Does not cast shadows.
    *   **Use Case:** Providing soft, natural-looking ambient light, often more realistic than `AmbientLight`.
    *   **Props:** `skyColor`, `groundColor`, `intensity`.

    ```javascript
    const hemisphereLight = new THREE.HemisphereLight(0x87ceeb, 0x444444, 0.8); // Sky blue, ground gray, intensity
    scene.add(hemisphereLight);
    ```

6.  **`RectAreaLight`:**
    *   **Effect:** Emits light uniformly from a rectangular plane. Only works with `MeshStandardMaterial` and `MeshPhysicalMaterial`. Does not cast shadows by default (requires helpers/extensions).
    *   **Use Case:** Simulating window lighting, rectangular light panels, photo studio lights.
    *   **Props:** `color`, `intensity`, `width`, `height`, `position`, `lookAt`.
    *   **Note:** Requires importing `RectAreaLightUniformsLib` and calling `init()`. Can be performance-intensive.

    ```javascript
    // import { RectAreaLightUniformsLib } from 'three/addons/lights/RectAreaLightUniformsLib.js';
    // RectAreaLightUniformsLib.init(); // Call once
    // const rectLight = new THREE.RectAreaLight(0xffffff, 5, 2, 3); // Color, Intensity, Width, Height
    // rectLight.position.set(0, 5, 5);
    // rectLight.lookAt(0, 0, 0);
    // scene.add(rectLight);
    ```

## Enabling Shadows

Shadows require setup on three components:

1.  **Renderer:** Enable shadow maps and optionally set the type.
    ```javascript
    renderer.shadowMap.enabled = true;
    // Optional: Choose shadow map type (PCFSoftShadowMap is smoother but slower)
    renderer.shadowMap.type = THREE.PCFSoftShadowMap;
    ```
2.  **Lights:** Set `castShadow = true` on lights that should cast shadows (`DirectionalLight`, `PointLight`, `SpotLight`). Carefully configure the light's `shadow` properties (camera frustum, map size, bias, radius). **Tuning the shadow camera frustum is critical for quality and performance.**
3.  **Objects (Meshes):**
    *   Set `castShadow = true` on objects that should cast shadows.
    *   Set `receiveShadow = true` on objects (like floors or walls) that should have shadows cast onto them.

```javascript
// Light casts shadow
directionalLight.castShadow = true;

// Cube casts shadow
cube.castShadow = true;

// Plane receives shadow
plane.receiveShadow = true;
```

Choose appropriate light types based on the desired effect. Use `AmbientLight` or `HemisphereLight` for basic illumination. Use `DirectionalLight`, `PointLight`, or `SpotLight` for more defined lighting and shadows. Remember that shadows significantly impact performance; use them judiciously, keep shadow map resolutions as low as acceptable, and tightly fit shadow camera frustums.