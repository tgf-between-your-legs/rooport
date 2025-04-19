# Three.js: Textures

Applying images to the surface of 3D objects using textures.

## Core Concept: Mapping Images to Surfaces

Textures allow you to wrap a 2D image onto the surface of a 3D geometry, defining its color, bumpiness, roughness, and other visual details.

**Key Components:**

*   **Image File:** The source image (e.g., `.jpg`, `.png`). For optimal performance and quality:
    *   Use power-of-two dimensions (e.g., 512x512, 1024x1024, 2048x1024). Not strictly required anymore, but often helps with mipmapping and compatibility.
    *   Consider compressed formats like KTX2 (`.ktx2`) using Basis Universal compression, loaded via `KTX2Loader`, for significantly smaller file sizes and faster GPU uploads, especially on mobile.
*   **`THREE.TextureLoader`:** A class used to load standard image files (`.jpg`, `.png`).
*   **`THREE.Texture`:** An object representing the loaded image data, ready to be used by materials.
*   **UV Coordinates:** 2D coordinates (ranging from 0.0 to 1.0) stored in the geometry's `uv` attribute. These tell Three.js how to map points on the 2D texture image to points (vertices) on the 3D geometry's surface. Built-in geometries usually have default UVs; custom geometries or loaded models need them defined.
*   **Material Properties:** Materials have properties (like `.map`, `.normalMap`, `.roughnessMap`) where you assign `THREE.Texture` objects.

## Loading and Applying Textures

1.  **Instantiate Loader:** Create an instance of `TextureLoader`. It's often good practice to reuse a single loader instance.
    ```javascript
    import * as THREE from 'three';

    const textureLoader = new THREE.TextureLoader();
    ```
2.  **Load Texture:** Use the loader's `.load()` method, providing the image path and optional callback functions.
    ```javascript
    // Basic loading
    const colorTexture = textureLoader.load('/textures/door/color.jpg');

    // Loading with callbacks
    const alphaTexture = textureLoader.load(
        '/textures/door/alpha.jpg',
        // onLoad callback
        (texture) => {
            console.log('Alpha texture loaded successfully');
        },
        // onProgress callback (not typically used for single images)
        undefined,
        // onError callback
        (error) => {
            console.error('Error loading alpha texture:', error);
        }
    );
    ```
3.  **Configure Texture Properties (Optional but Important):**
    *   **Color Space:** For color textures (`.map`, `.emissiveMap`), ensure the correct color space is set, especially when using `WebGLRenderer` with physically correct lighting. Use `THREE.SRGBColorSpace` for most color images. Data textures (like normal, roughness, metalness maps) should typically use `THREE.LinearSRGBColorSpace` (the default).
        ```javascript
        colorTexture.colorSpace = THREE.SRGBColorSpace;
        ```
    *   **Wrapping:** Controls how the texture repeats or clamps when UV coordinates go outside the 0.0-1.0 range (`texture.wrapS`, `texture.wrapT`). Options: `THREE.RepeatWrapping`, `THREE.MirroredRepeatWrapping`, `THREE.ClampToEdgeWrapping`.
        ```javascript
        // Repeat the texture
        colorTexture.wrapS = THREE.RepeatWrapping;
        colorTexture.wrapT = THREE.RepeatWrapping;
        colorTexture.repeat.set(2, 3); // Repeat 2 times horizontally, 3 times vertically
        ```
    *   **Filtering:** Controls how the texture looks when magnified (`magFilter`) or minified (`minFilter`). `THREE.LinearFilter` (default) provides smooth results. `THREE.NearestFilter` gives a pixelated look. Mipmapping (`minFilter` options like `THREE.LinearMipmapLinearFilter`) improves quality and performance for textures viewed from a distance but requires power-of-two dimensions.
        ```javascript
        // Use mipmapping for minification if texture has power-of-two dimensions
        // colorTexture.generateMipmaps = true; // Default is true
        // colorTexture.minFilter = THREE.LinearMipmapLinearFilter;
        // Use nearest filter for pixelated look
        // colorTexture.magFilter = THREE.NearestFilter;
        ```
    *   **Other:** `offset`, `rotation`, `center`.
4.  **Assign Texture to Material:** Set the appropriate property on your material instance.
    ```javascript
    const material = new THREE.MeshStandardMaterial({
        map: colorTexture,         // Base color texture
        // alphaMap: alphaTexture, // Grayscale texture for opacity
        // transparent: true,      // Required if using alphaMap or opacity < 1
        // aoMap: aoTexture,
        // displacementMap: heightTexture,
        // displacementScale: 0.05,
        // metalnessMap: metalnessTexture,
        // roughnessMap: roughnessTexture,
        // normalMap: normalTexture,
        // normalScale: new THREE.Vector2(0.5, 0.5),
        // envMap: environmentMapTexture,
        // emissiveMap: emissiveTexture,
    });

    const geometry = new THREE.PlaneGeometry(1, 1); // Plane geometry has UVs by default
    const mesh = new THREE.Mesh(geometry, material);
    // scene.add(mesh);
    ```

## Texture Types & Usage

*   **`map`:** Base color (albedo).
*   **`alphaMap`:** Controls opacity (requires `transparent: true`). White = opaque, black = transparent.
*   **`aoMap` (Ambient Occlusion):** Adds fake shadows in crevices. Requires a second set of UV coordinates (`uv2`) in the geometry.
*   **`normalMap`:** Simulates surface details/bumps without adding geometry. Affects lighting.
*   **`roughnessMap` / `metalnessMap`:** Control PBR properties per pixel.
*   **`envMap` (Environment Map):** Adds reflections of the surroundings. Often a `CubeTexture`.
*   **`displacementMap` / `bumpMap`:** Modify vertex positions or normals based on texture values (can be performance-intensive).
*   **`emissiveMap`:** Defines areas that emit light (unaffected by scene lighting).

Textures are fundamental for creating visually interesting materials. Use `TextureLoader` for basic images, configure properties like `colorSpace` and `wrapS`/`wrapT`, and assign them to the corresponding material slots. Consider compressed formats like KTX2 for better performance. Remember to dispose of textures (`texture.dispose()`).

*(Refer to the official Three.js documentation on Textures and specific loaders like `TextureLoader`.)*