# Three.js: Model Loading (glTF, Draco, KTX2)

Loading 3D models, particularly the glTF format, into a Three.js scene.

## Core Concept: glTF - The JPEG of 3D

**glTF (GL Transmission Format)** is the industry standard file format for efficiently transmitting and loading 3D scenes and models. It's often referred to as the "JPEG of 3D" due to its focus on runtime delivery.

**Key Features:**

*   **JSON Structure:** `.gltf` files use JSON to describe the scene graph, materials, animations, etc.
*   **Binary Data:** Geometry, textures, and animation data are often stored in separate binary files (`.bin`) or embedded directly in a binary glTF (`.glb`) file.
*   **PBR Materials:** Natively supports Physically Based Rendering materials.
*   **Animation:** Can include skeletal animations.
*   **Extensibility:** Supports extensions for features like mesh compression (Draco) and texture compression (KTX2/Basis Universal).

**File Types:**

*   `.gltf` + `.bin` + textures: JSON structure with separate binary data and image files.
*   `.glb`: Binary format that embeds JSON, binary data, and textures into a single file. Often preferred for easier distribution.

## Loading glTF Models

1.  **Import Loaders:**
    *   `GLTFLoader`: The main loader for `.gltf` and `.glb` files.
    *   `DRACOLoader` (Optional): For loading models compressed with Google's Draco algorithm (significantly smaller geometry data). Requires Draco decoder files.
    *   `KTX2Loader` (Optional): For loading textures compressed with Basis Universal (`.ktx2` format). Requires Basis Universal decoder files.

    ```javascript
    import * as THREE from 'three';
    import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
    import { DRACOLoader } from 'three/addons/loaders/DRACOLoader.js';
    import { KTX2Loader } from 'three/addons/loaders/KTX2Loader.js';
    ```

2.  **Instantiate Loaders & Configure Decoders (if needed):**
    *   Create instances of the loaders.
    *   If using Draco or KTX2, create instances of their respective loaders and point the `GLTFLoader` to them. You need to host the decoder files (`draco/` and `basis/` folders, usually copied from `node_modules/three/examples/jsm/libs/`) and provide the path.

    ```javascript
    const gltfLoader = new GLTFLoader();

    // --- Optional: Draco ---
    const dracoLoader = new DRACOLoader();
    // Specify path to the Draco decoder files (relative to your public folder)
    dracoLoader.setDecoderPath('/libs/draco/gltf/');
    gltfLoader.setDRACOLoader(dracoLoader); // Associate with GLTFLoader

    // --- Optional: KTX2 ---
    const ktx2Loader = new KTX2Loader();
    // Specify path to the Basis Universal decoder files
    ktx2Loader.setTranscoderPath('/libs/basis/');
    // Detect supported features (important for KTX2Loader)
    ktx2Loader.detectSupport(renderer); // Pass your WebGLRenderer instance
    gltfLoader.setKTX2Loader(ktx2Loader); // Associate with GLTFLoader
    ```

3.  **Load the Model:**
    *   Use `gltfLoader.load()`, providing the path to the `.gltf` or `.glb` file and callback functions.

    ```javascript
    gltfLoader.load(
        '/models/myModel/myModel.glb', // Path to your model file

        // --- onLoad callback ---
        (gltf) => {
            console.log('Model loaded successfully:', gltf);

            // gltf.scene contains the loaded scene graph (usually a THREE.Group)
            const model = gltf.scene;

            // Optional: Adjust model position, scale, rotation
            model.scale.set(0.1, 0.1, 0.1);
            model.position.y = -1;

            // Optional: Enable shadows for all meshes in the model
            model.traverse((child) => {
                if (child instanceof THREE.Mesh) {
                    child.castShadow = true;
                    child.receiveShadow = true;
                }
            });

            // Add the loaded model to your main scene
            scene.add(model);

            // Optional: Handle animations (see threejs-animation-mixer.md)
            // if (gltf.animations && gltf.animations.length) {
            //     mixer = new THREE.AnimationMixer(model);
            //     const action = mixer.clipAction(gltf.animations[0]);
            //     action.play();
            // }
        },

        // --- onProgress callback ---
        (xhr) => {
            const percentLoaded = (xhr.loaded / xhr.total) * 100;
            console.log(`Model loading progress: ${percentLoaded.toFixed(2)}%`);
            // Update loading bar UI here
        },

        // --- onError callback ---
        (error) => {
            console.error('Error loading model:', error);
        }
    );
    ```

## Important Considerations

*   **File Paths:** Ensure paths to models and decoder libraries (`draco/`, `basis/`) are correct relative to your web server's public directory.
*   **Compression:** Use Draco for geometry and KTX2/Basis Universal for textures whenever possible to significantly reduce file sizes and loading times. These often need to be applied during the model export process (e.g., in Blender).
*   **Renderer Configuration:** Ensure your `WebGLRenderer` is configured correctly, especially regarding color spaces (`renderer.outputColorSpace = THREE.SRGBColorSpace;`) if your model uses PBR materials and textures.
*   **Lighting:** glTF models using PBR materials (`MeshStandardMaterial`) require appropriate lighting in your Three.js scene to look correct.
*   **Animations:** Load animations via `gltf.animations` and play them using `AnimationMixer`.
*   **Disposal:** While the loader handles some cleanup, if you remove models dynamically, ensure you traverse the model and dispose of its geometries and materials properly.

Loading glTF models is a core part of building complex Three.js scenes. Use `GLTFLoader` and configure `DRACOLoader` and `KTX2Loader` when using compressed assets for optimal performance.

*(Refer to the official Three.js documentation on Loading 3D models, `GLTFLoader`, `DRACOLoader`, and `KTX2Loader`.)*