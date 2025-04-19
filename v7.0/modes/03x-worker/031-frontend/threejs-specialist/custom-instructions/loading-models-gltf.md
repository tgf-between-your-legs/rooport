# Three.js: Loading 3D Models (glTF)

Loading `.gltf` and `.glb` (binary glTF) models into a Three.js scene.

## Core Concept

glTF (GL Transmission Format) is the recommended standard for transmitting 3D models efficiently for web and AR/VR applications. Three.js provides loaders specifically for this format.

## Loaders

*   **`GLTFLoader`:** The main loader for `.gltf` and `.glb` files. Found in `three/examples/jsm/loaders/GLTFLoader.js`.
*   **`DRACOLoader`:** Used *in conjunction with* `GLTFLoader` if the glTF model uses Draco mesh compression (significantly reduces file size). Found in `three/examples/jsm/loaders/DRACOLoader.js`. Requires decoder files.
*   **`KTX2Loader`:** Used *in conjunction with* `GLTFLoader` if the glTF model uses KTX2 texture compression (reduces texture memory usage and loading time). Found in `three/examples/jsm/loaders/KTX2Loader.js`. Requires Basis Universal decoder files.

## Basic Loading (`.glb`)

```javascript
import * as THREE from 'three';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';

const scene = new THREE.Scene();
// ... setup camera, renderer ...

// 1. Instantiate the loader
const loader = new GLTFLoader();

// Optional: Loading Manager for progress tracking
const loadingManager = new THREE.LoadingManager();
loadingManager.onStart = (url, itemsLoaded, itemsTotal) => console.log('Started loading:', url);
loadingManager.onLoad = () => console.log('Loading complete!');
loadingManager.onProgress = (url, itemsLoaded, itemsTotal) => console.log(`Loading ${url}: ${itemsLoaded}/${itemsTotal}`);
loadingManager.onError = (url) => console.error('Error loading:', url);
// const loader = new GLTFLoader(loadingManager); // Pass manager to loader

// 2. Load the model
loader.load(
  // Resource URL (path to your .glb file)
  '/models/my_model.glb',
  // onLoad callback: Called when load is complete
  function (gltf) {
    console.log('Model loaded:', gltf);
    // gltf.scene contains the main Object3D (often a Group)
    // You might need to traverse it to find specific meshes or adjust properties
    gltf.scene.traverse(function (child) {
      if ((child as THREE.Mesh).isMesh) {
        // Example: Enable shadows on meshes
        child.castShadow = true;
        child.receiveShadow = true;
      }
    });

    // Optional: Scale or position the model
    // gltf.scene.scale.set(0.1, 0.1, 0.1);
    // gltf.scene.position.y = -1;

    // Add the loaded scene graph to your main scene
    scene.add(gltf.scene);

    // Access animations if present
    // mixer = new THREE.AnimationMixer(gltf.scene);
    // gltf.animations.forEach((clip) => {
    //   mixer.clipAction(clip).play();
    // });

  },
  // onProgress callback (optional): Called while loading is progressing
  function (xhr) {
    console.log((xhr.loaded / xhr.total * 100) + '% loaded');
  },
  // onError callback (optional): Called if loading errors occur
  function (error) {
    console.error('An error happened during loading:', error);
  }
);

// ... animation loop ...
```

## Loading with Draco Compression

1.  **Copy Draco Decoder Files:** Obtain the Draco decoder files (`draco_decoder.js`, `draco_decoder.wasm`, `draco_wasm_wrapper.js`) usually found within the `three/examples/jsm/libs/draco/gltf/` directory of the Three.js installation or repository. Place them in your `public` or static assets folder.
2.  **Configure `DRACOLoader`:** Instantiate `DRACOLoader`, set the decoder path, and provide it to `GLTFLoader`.

```javascript
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
import { DRACOLoader } from 'three/examples/jsm/loaders/DRACOLoader.js';

const gltfLoader = new GLTFLoader();

// 1. Instantiate DRACOLoader
const dracoLoader = new DRACOLoader();
// 2. Specify path to the Draco decoder files relative to your public folder
dracoLoader.setDecoderPath('/draco/gltf/'); // Adjust path as needed
dracoLoader.setDecoderConfig({ type: 'js' }); // Optional: Use 'js' or 'wasm'

// 3. Provide DRACOLoader instance to GLTFLoader
gltfLoader.setDRACOLoader(dracoLoader);

// 4. Load the Draco-compressed model
gltfLoader.load('/models/my_draco_model.glb', (gltf) => {
  scene.add(gltf.scene);
}, undefined, (error) => {
  console.error(error);
});
```

## Loading with KTX2 Texture Compression

1.  **Copy Basis Universal Decoder Files:** Obtain the Basis Universal decoder files (e.g., `basis_transcoder.js`, `basis_transcoder.wasm`) usually found within `three/examples/jsm/libs/basis/`. Place them in your `public` or static assets folder.
2.  **Configure `KTX2Loader`:** Instantiate `KTX2Loader`, set the transcoder path, detect GPU capabilities, and provide it to `GLTFLoader`. Requires the renderer instance.

```javascript
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
import { KTX2Loader } from 'three/examples/jsm/loaders/KTX2Loader.js';

// Assume 'renderer' is your THREE.WebGLRenderer instance
const ktx2Loader = new KTX2Loader()
  .setTranscoderPath('/basis/') // Adjust path to basis decoder files
  .detectSupport(renderer); // Detect supported texture formats

const gltfLoader = new GLTFLoader();
gltfLoader.setKTX2Loader(ktx2Loader);
// Optional: Dispose of KTX2Loader worker after use if needed
// gltfLoader.setDisposeCallback(() => ktx2Loader.dispose());

gltfLoader.load('/models/my_ktx2_model.glb', (gltf) => {
  scene.add(gltf.scene);
  // Remember to dispose KTX2Loader if you used setDisposeCallback
  // ktx2Loader.dispose(); // Or handle disposal elsewhere
}, undefined, (error) => {
  console.error(error);
});
```

## Considerations

*   **File Paths:** Ensure the paths to models and decoder files are correct relative to your project's structure and how static assets are served.
*   **Async/Await:** Loaders return Promises, so you can use `async/await` for cleaner code.
*   **Error Handling:** Implement `onError` callbacks or `.catch()` with Promises.
*   **Model Structure:** The loaded `gltf.scene` might be a `THREE.Group`. You may need to traverse it (`gltf.scene.traverse(...)`) to find specific meshes, apply materials, enable shadows, etc.
*   **Disposal:** Remember to dispose of geometries, materials, and textures loaded with the model when they are no longer needed.

*(Refer to the official Three.js documentation for `GLTFLoader`, `DRACOLoader`, and `KTX2Loader`.)*