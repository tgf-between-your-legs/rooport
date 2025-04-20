# Loading 3D Models (glTF)

Loading `.gltf` and `.glb` (binary glTF) models into a Three.js scene, including handling compression.

## Core Concept: glTF Standard

glTF (GL Transmission Format) is the **recommended standard** for transmitting 3D models efficiently for web and AR/VR applications. It's designed for compact file sizes and fast loading. Three.js provides excellent support for it.

*   `.gltf`: JSON file describing the model structure, referencing external files for geometry (`.bin`), textures (`.jpg`, `.png`), etc.
*   `.glb`: Binary format, packing the JSON, geometry, and sometimes textures into a single file. Often preferred for easier distribution.

## Loaders

*   **`GLTFLoader`:** The main loader for `.gltf` and `.glb` files. Found in `three/addons/loaders/GLTFLoader.js`.
*   **`DRACOLoader`:** Used *in conjunction with* `GLTFLoader` if the glTF model uses Draco mesh compression (significantly reduces geometry file size). Found in `three/addons/loaders/DRACOLoader.js`. Requires separate decoder files.
*   **`KTX2Loader`:** Used *in conjunction with* `GLTFLoader` if the glTF model uses KTX2 texture compression (Basis Universal). Reduces GPU texture memory usage and loading time. Found in `three/addons/loaders/KTX2Loader.js`. Requires separate Basis transcoder files.

## Basic Loading (`.glb`)

```javascript
import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

// Optional: Loading Manager for progress tracking across multiple assets
const loadingManager = new THREE.LoadingManager();
loadingManager.onStart = (url, itemsLoaded, itemsTotal) => console.log(`Started loading: ${url} (${itemsLoaded}/${itemsTotal})`);
loadingManager.onLoad = () => console.log('Loading complete!');
loadingManager.onProgress = (url, itemsLoaded, itemsTotal) => console.log(`Loading ${url}: ${itemsLoaded}/${itemsTotal}`);
loadingManager.onError = (url) => console.error('Error loading:', url);

// 1. Instantiate the loader (pass manager if using)
const gltfLoader = new GLTFLoader(loadingManager);

// 2. Load the model
let loadedModel: THREE.Group | null = null; // Store reference for later disposal/manipulation

gltfLoader.load(
  // Resource URL (path to your .glb or .gltf file)
  '/models/my_model.glb',

  // onLoad callback: Called when load is complete
  (gltf) => {
    console.log('Model loaded:', gltf);
    loadedModel = gltf.scene; // Store the loaded scene graph

    // gltf.scene contains the main Object3D (often a Group)
    // Adjust scale, position, rotation as needed
    loadedModel.scale.set(0.1, 0.1, 0.1);
    loadedModel.position.y = -1;

    // Traverse the loaded model to configure meshes, materials, etc.
    loadedModel.traverse((child) => {
      if (child instanceof THREE.Mesh) {
        // Example: Enable shadows on all meshes
        child.castShadow = true;
        child.receiveShadow = true;

        // Example: Ensure materials are double-sided if needed
        // child.material.side = THREE.DoubleSide;

        // Example: Check for specific material types or names
        // if (child.material.name === 'GlassMaterial') { ... }
      }
    });

    // Add the loaded scene graph to your main scene
    scene.add(loadedModel);

    // Access animations if present (See 08-animation-mixer.md)
    // if (gltf.animations && gltf.animations.length) {
    //   mixer = new THREE.AnimationMixer(loadedModel);
    //   const action = mixer.clipAction(gltf.animations[0]);
    //   action.play();
    // }
  },

  // onProgress callback (provided by LoadingManager if used, or can be defined here)
  (xhr) => {
    if (!loadingManager.onProgress) { // Only log if not using manager's progress
        console.log(`${(xhr.loaded / xhr.total * 100).toFixed(2)}% loaded`);
    }
  },

  // onError callback: Called if loading errors occur
  (error) => {
    console.error('An error happened during model loading:', error);
  }
);

// --- Animation loop ---
// function animate() {
//   requestAnimationFrame(animate);
//   const delta = clock.getDelta();
//   if (mixer) mixer.update(delta);
//   renderer.render(scene, camera);
// }
```

## Loading with Draco Compression

Draco significantly reduces the size of geometry data.

1.  **Copy Draco Decoder Files:** Obtain the Draco decoder files (`draco_decoder.js`, `draco_decoder.wasm`, `draco_wasm_wrapper.js`) usually found within the `three/examples/jsm/libs/draco/gltf/` directory of the Three.js installation/repository. Place them in a publicly accessible folder in your project (e.g., `/draco/`).
2.  **Configure `DRACOLoader`:** Instantiate `DRACOLoader`, set the path to the decoder files using `setDecoderPath()`, and provide the `DRACOLoader` instance to `GLTFLoader` using `setDRACOLoader()`.

```javascript
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { DRACOLoader } from 'three/addons/loaders/DRACOLoader.js';

const gltfLoader = new GLTFLoader(); // Or use LoadingManager

// 1. Instantiate DRACOLoader
const dracoLoader = new DRACOLoader();
// 2. Specify path to the Draco decoder files (relative to your public folder)
dracoLoader.setDecoderPath('/draco/'); // **Adjust this path**
// dracoLoader.setDecoderConfig({ type: 'js' }); // Optional: Use 'js' or 'wasm' (wasm is generally preferred)
dracoLoader.preload(); // Optional: Start loading decoder files early

// 3. Provide DRACOLoader instance to GLTFLoader
gltfLoader.setDRACOLoader(dracoLoader);

// 4. Load the Draco-compressed model (same .load() method)
gltfLoader.load('/models/my_draco_model.glb', (gltf) => {
  scene.add(gltf.scene);
  // ... rest of setup ...
}, undefined, (error) => {
  console.error('Error loading Draco model:', error);
});

// Remember to dispose dracoLoader when done if necessary
// dracoLoader.dispose();
```

## Loading with KTX2 Texture Compression

KTX2 (using Basis Universal) significantly reduces GPU texture memory usage and loading times.

1.  **Copy Basis Transcoder Files:** Obtain the Basis Universal transcoder files (e.g., `basis_transcoder.js`, `basis_transcoder.wasm`) usually found within `three/examples/jsm/libs/basis/`. Place them in a publicly accessible folder (e.g., `/basis/`).
2.  **Configure `KTX2Loader`:** Instantiate `KTX2Loader`, set the path to the transcoder files using `setTranscoderPath()`, call `detectSupport(renderer)` to determine optimal GPU formats, and provide the `KTX2Loader` instance to `GLTFLoader` using `setKTX2Loader()`. Requires the `WebGLRenderer` instance.

```javascript
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { KTX2Loader } from 'three/addons/loaders/KTX2Loader.js';

// Assume 'renderer' is your THREE.WebGLRenderer instance
const ktx2Loader = new KTX2Loader()
  .setTranscoderPath('/basis/') // **Adjust this path**
  .detectSupport(renderer); // Detect supported texture formats using the renderer

const gltfLoader = new GLTFLoader(); // Or use LoadingManager
gltfLoader.setKTX2Loader(ktx2Loader);

// Optional: Dispose KTX2Loader worker after all KTX2 textures are loaded
// loadingManager.onLoad = () => {
//    console.log('Loading complete!');
//    ktx2Loader.dispose(); // Dispose worker when all loading is done
// };

gltfLoader.load('/models/my_ktx2_model.glb', (gltf) => {
  scene.add(gltf.scene);
  // ... rest of setup ...
}, undefined, (error) => {
  console.error('Error loading KTX2 model:', error);
});

// If not using LoadingManager, dispose manually when appropriate
// ktx2Loader.dispose();
```

## Considerations

*   **File Paths:** Ensure paths to models and decoder/transcoder files are correct relative to your project's structure and how static assets are served.
*   **Async/Await:** Loaders return Promises, so you can use `async/await` for cleaner asynchronous code.
*   **Error Handling:** Implement `onError` callbacks or `.catch()` with Promises. Provide informative error messages.
*   **Model Structure:** The loaded `gltf.scene` might be a `THREE.Group`. Traverse it (`gltf.scene.traverse(...)`) to find specific meshes, apply materials, enable shadows, configure animations, etc.
*   **Disposal:** Remember to dispose of geometries, materials, and textures loaded with the model when they are no longer needed (see `13-performance-disposal.md`). Also dispose of Draco and KTX2 loaders if they are no longer needed to free up web workers.
*   **Compression Tools:** Models need to be exported/processed with Draco and/or Basis Universal compression enabled using tools like Blender glTF exporter, gltfpack, or Gestaltor.