# Custom Instructions for 🧊 Three.js Specialist

This directory contains specific instructions and guidelines for the `threejs-specialist` mode, supplementing the core role definition.

## Instruction Files

1.  **`01-core-workflow-principles.md`**: General operational guidelines, standard workflow steps, and communication protocols.
2.  **`02-scene-setup.md`**: Setting up the core `Scene`, `Camera`, `WebGLRenderer`, and render loop.
3.  **`03-geometries.md`**: Using built-in geometries and creating custom `BufferGeometry`.
4.  **`04-materials.md`**: Overview of common material types (`MeshBasicMaterial`, `MeshStandardMaterial`, `MeshPhysicalMaterial`, etc.) and their properties.
5.  **`05-textures.md`**: Loading (`TextureLoader`), configuring (`colorSpace`, wrapping, filtering), and applying textures to materials.
6.  **`06-lights-shadows.md`**: Implementing various light types (`Ambient`, `Directional`, `Point`, `Spot`, `Hemisphere`) and configuring shadow mapping.
7.  **`07-camera-controls.md`**: Using standard camera controls like `OrbitControls`, `TrackballControls`, `FlyControls`.
8.  **`08-animation-mixer.md`**: Playing pre-defined animations embedded in models (e.g., glTF) using `AnimationMixer`.
9.  **`09-model-loading-gltf.md`**: Loading glTF models (`.glb`, `.gltf`) using `GLTFLoader`, including Draco (`DRACOLoader`) and KTX2 (`KTX2Loader`) compression.
10. **`10-interaction-raycasting.md`**: Detecting pointer interactions (clicks, hovers) on 3D objects using `Raycaster`.
11. **`11-custom-shaders-glsl.md`**: Creating custom visual effects using `ShaderMaterial` and GLSL vertex/fragment shaders.
12. **`12-post-processing.md`**: Applying full-screen effects like bloom, anti-aliasing using `EffectComposer` and passes.
13. **`13-performance-disposal.md`**: Key performance optimization techniques (draw calls, geometry, textures, shadows) and crucial manual resource disposal (`.dispose()`) for memory management.
14. **`14-collaboration-escalation.md`**: Guidelines for collaborating with other specialist modes and escalating issues beyond core expertise.