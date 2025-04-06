## Three.js vUnknown - Condensed Context Index

### Overall Purpose
Three.js (Version Unknown) is a JavaScript library for creating and displaying animated 3D computer graphics in a web browser using WebGL. It provides APIs for scenes, cameras, lighting, materials, geometries, and loaders. This index summarizes core setup, asset loading, editor commands, testing, and documentation patterns based on provided context snippets.

### Core Concepts & Capabilities
*   **Scene Graph:** Building 3D scenes using `THREE.Scene`, adding objects like `THREE.Mesh` (composed of `THREE.Geometry` and `THREE.Material`).
*   **Rendering:** Using `THREE.WebGLRenderer` to display the scene via a `THREE.Camera` (e.g., `THREE.PerspectiveCamera`), often within an animation loop (`renderer.setAnimationLoop`).
*   **Asset Loading:** Importing complex geometries and textures using loaders like `DRACOLoader` (for Draco compressed meshes) and `KTX2Loader` (for KTX2 textures). Requires setting decoder/transcoder paths.
*   **Editor Framework:** Extending the Three.js editor with custom actions using a `Command` pattern supporting `execute`, `undo`, `toJSON`, `fromJSON`, and optional `update`.
*   **Testing & Development:** Standard practices include unit tests (`npm run test-unit`), E2E tests (`npm run test-e2e`), dependency management (`npm install`), and version control (`git clone`).
*   **Documentation:** Specific Markdown/HTML syntax for linking classes (`[page:...]`), members (`[page:ClassName.memberName]`), methods (`[method:...]`), properties (`[property:...]`), and examples (`[example:...]`).

### Key APIs / Components / Configuration / Patterns
*   `import * as THREE from 'three';`: Standard ES6 module import.
*   `new THREE.Scene()`: Creates the root container for 3D objects.
*   `new THREE.PerspectiveCamera(fov, aspect, near, far)`: Defines a camera for viewing the scene.
*   `new THREE.BoxGeometry(width, height, depth)`: Creates a basic cube geometry.
*   `new THREE.MeshNormalMaterial()`: A material that maps normal vectors to RGB colors.
*   `new THREE.Mesh(geometry, material)`: Represents an object in the scene.
*   `scene.add(mesh)`: Adds an object to the scene graph.
*   `new THREE.WebGLRenderer({ antialias: true })`: Initializes the renderer.
*   `renderer.setSize(width, height)`: Sets the output canvas size.
*   `renderer.setAnimationLoop(callback)`: Sets a function to be called every frame for animation.
*   `renderer.render(scene, camera)`: Renders a frame.
*   `new DRACOLoader()`: Loader for Draco compressed geometry. Requires `setDecoderPath()`.
*   `new KTX2Loader()`: Loader for KTX2 compressed textures. Requires `setTranscoderPath()` and `detectSupport()`.
*   `Command` Pattern (Editor): Base class/pattern for undoable actions (`execute`, `undo`, `toJSON`, `fromJSON`). Requires matching `type` property.
*   `editor.execute(new Command(...))`: Executes a command and adds it to the undo stack.
*   `npm install`: Installs project dependencies.
*   `npm run test-unit`: Runs unit tests (Node.js).
*   `npm run test-e2e [example_name]`: Runs end-to-end tests (browser).
*   `npx servez -p 8080 --ssl`: Starts a local server for browser tests.
*   `git clone --depth=1 ...`: Clones the repository efficiently.
*   `debugger;`: Pauses execution for browser debugging.

### Common Patterns & Best Practices / Pitfalls
*   **Loader Configuration:** Loaders like `DRACOLoader` and `KTX2Loader` require setting paths (`setDecoderPath`, `setTranscoderPath`) to their respective decoder/transcoder libraries.
*   **Editor Command Structure:** Custom editor commands must inherit from `Command`, implement `execute` and `undo`, and define `type` and `name`. `toJSON`/`fromJSON` are needed for serialization.
*   **Testing Setup:** Unit tests often require initializing an `Editor` instance and adding objects (`AddObjectCommand`). E2E tests use `npm run test-e2e`.
*   **Documentation Linking:** Use specific `[page:...]`, `[method:...]`, `[property:...]`, `[example:...]` syntax for internal documentation links.
*   **Debugging:** Use the `debugger;` statement to pause execution in browser tests.

This index summarizes the core concepts, APIs, and patterns for Three.js (Version Unknown) based on the provided snippets. Consult the full source documentation (project_journal/context/source_docs/threejs-specialist-llms-context-20250406.md) for exhaustive details.