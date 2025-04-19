# Textures

Applying images to the surface of 3D objects using textures.

## Core Concept: Mapping Images to Surfaces

Textures allow you to wrap a 2D image onto the surface of a 3D geometry, defining its color, bumpiness, roughness, and other visual details based on the image data.

**Key Components:**

*   **Image File:** The source image (e.g., `.jpg`, `.png`, `.ktx2`). For optimal performance and quality:
    *   Use power-of-two dimensions (e.g., 512x512, 1024x1024, 2048x1024) where possible, especially if using mipmapping or `RepeatWrapping`.
    *   Consider compressed formats like KTX2 (`.ktx2`) using Basis Universal compression, loaded via `KTX2Loader`, for significantly smaller file sizes and faster GPU uploads, especially on mobile.
*   **Loaders:**
    *   `THREE.TextureLoader`: For standard image files (`.jpg`, `.png`).
    *   `THREE.CubeTextureLoader`: For loading 6 images that form a cube map (for environment maps).
    *   `THREE.KTX2Loader`: For loading `.ktx2` compressed textures (requires Basis Universal transcoder files). Used with `GLTFLoader` or standalone.
*   **`THREE.Texture`:** An object representing the loaded image data, ready to be used by materials.
*   **UV Coordinates:** 2D coordinates (ranging from 0.0 to 1.0) stored in the geometry's `uv` attribute. These tell Three.js how to map points on the 2D texture image to points (vertices) on the 3D geometry's surface. Built-in geometries usually have default UVs; custom geometries or loaded models need them defined. Some textures (like `aoMap`) may require a second set (`uv2`).
*   **Material Properties:** Materials have properties (like `.map`, `.normalMap`, `.roughnessMap`) where you assign `THREE.Texture` objects.

## Loading and Applying Textures (`TextureLoader`)

1.  **Instantiate Loader:** Create an instance of `TextureLoader`. Reuse a single loader instance for efficiency.
    ```javascript
    import * as THREE from 'three';

    const textureLoader = new THREE.TextureLoader();
    // Optional: Use a LoadingManager for progress tracking across multiple loads
    // const loadingManager = new THREE.LoadingManager();
    // const textureLoader = new THREE.TextureLoader(loadingManager);
    ```
2.  **Load Texture:** Use the loader's `.load()` method, providing the image path and optional callback functions.
    ```javascript
    const colorTexture = textureLoader.load(
        '/textures/checkerboard.png', // Path relative to public/static folder
        // onLoad callback (optional)
        (texture) => {
            console.log('Texture loaded:', texture);
            // Configure texture properties here if needed *after* load
            texture.colorSpace = THREE.SRGBColorSpace; // Crucial for color textures
            texture.wrapS = THREE.RepeatWrapping;
            texture.wrapT = THREE.RepeatWrapping;
            texture.repeat.set(4, 4);
            // texture.needsUpdate = true; // Often not needed if configured in onLoad
        },
        // onProgress callback (rarely used for single textures)
        undefined,
        // onError callback (optional)
        (error) => {
            console.error('Error loading texture:', error);
        }
    );
    ```
3.  **Configure Texture Properties (Can be set before or after load):**
    *   **`colorSpace`:** **Crucial.** For color textures (`.map`, `.emissiveMap`), set to `THREE.SRGBColorSpace`. For data textures (normal, roughness, metalness, AO, height maps), leave as the default `THREE.LinearSRGBColorSpace`. Mismatched color spaces lead to incorrect rendering.
    *   **`wrapS`, `wrapT`:** Controls wrapping on U (horizontal) and V (vertical) axes. Options: `THREE.RepeatWrapping`, `THREE.MirroredRepeatWrapping`, `THREE.ClampToEdgeWrapping` (default).
    *   **`repeat`:** `Vector2` specifying how many times the texture repeats when using `RepeatWrapping` or `MirroredRepeatWrapping`. `texture.repeat.set(horizRepeat, vertRepeat);`.
    *   **`offset`:** `Vector2` specifying UV offset. `texture.offset.set(uOffset, vOffset);`.
    *   **`rotation`:** Rotation angle in radians around the center. `texture.rotation = Math.PI / 4;`.
    *   **`center`:** `Vector2` specifying the center point for rotation. `texture.center.set(0.5, 0.5);`.
    *   **Filtering:** Controls appearance when scaled.
        *   `magFilter`: Magnification (texture bigger than surface area). `THREE.LinearFilter` (smooth, default) or `THREE.NearestFilter` (pixelated).
        *   `minFilter`: Minification (texture smaller than surface area). Options include `THREE.LinearFilter`, `THREE.NearestFilter`, and mipmap filters (`THREE.LinearMipmapLinearFilter` - best quality, `THREE.LinearMipmapNearestFilter`, `THREE.NearestMipmapLinearFilter`, `THREE.NearestMipmapNearestFilter`). Mipmapping improves performance and quality for distant textures but requires power-of-two dimensions and uses more memory.
    *   **`generateMipmaps`:** Boolean (default `true`). Set to `false` if you don't need mipmaps (e.g., for UI elements, or non-power-of-two textures where mipmaps aren't supported by default).
    *   **`anisotropy`:** Number. Improves texture quality when viewed at steep angles. Requires renderer capabilities check. `texture.anisotropy = renderer.capabilities.getMaxAnisotropy();`.

4.  **Assign Texture to Material:** Set the appropriate property on your material instance.
    ```javascript
    const material = new THREE.MeshStandardMaterial({
        map: colorTexture,         // Base color texture
        // alphaMap: alphaTexture, // Grayscale texture for opacity
        // transparent: true,      // Required if using alphaMap or opacity < 1
        // aoMap: aoTexture,       // Requires uv2 attribute
        // normalMap: normalTexture, // Data texture (LinearSRGBColorSpace)
        // roughnessMap: roughnessTexture, // Data texture
        // metalnessMap: metalnessTexture, // Data texture
    });

    const geometry = new THREE.PlaneGeometry(1, 1); // Plane geometry has UVs by default
    const mesh = new THREE.Mesh(geometry, material);
    // scene.add(mesh);
    ```

## Texture Types & Usage in Materials

*   **`map`:** Base color (albedo). Use `SRGBColorSpace`.
*   **`alphaMap`:** Controls opacity (requires `transparent: true`). White = opaque, black = transparent. Use `LinearSRGBColorSpace`.
*   **`aoMap` (Ambient Occlusion):** Adds fake shadows in crevices. Requires a second set of UV coordinates (`uv2`) in the geometry. Use `LinearSRGBColorSpace`.
*   **`normalMap`:** Simulates surface details/bumps without adding geometry. Affects lighting. Use `LinearSRGBColorSpace`.
*   **`roughnessMap` / `metalnessMap`:** Control PBR properties per pixel. Often packed together. Use `LinearSRGBColorSpace`.
*   **`envMap` (Environment Map):** Adds reflections. Often a `CubeTexture` or an equirectangular texture loaded via `TextureLoader`. Color space depends on source (e.g., `.hdr` needs special handling).
*   **`displacementMap` / `bumpMap`:** Modify vertex positions or normals. Can be performance-intensive. Use `LinearSRGBColorSpace`.
*   **`emissiveMap`:** Defines areas that emit light. Use `SRGBColorSpace`.

Textures are fundamental for creating visually interesting materials. Use appropriate loaders, **pay close attention to `colorSpace`**, configure wrapping and filtering, and assign them to the correct material slots. Consider compressed formats like KTX2 for better performance. Remember to dispose of textures (`texture.dispose()`).