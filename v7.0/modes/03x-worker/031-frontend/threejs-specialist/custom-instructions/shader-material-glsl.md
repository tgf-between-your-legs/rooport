# Three.js: Custom Shaders (`ShaderMaterial` & GLSL)

Creating custom visual effects using `ShaderMaterial` and GLSL code.

## Core Concept

While Three.js provides many built-in materials (`MeshStandardMaterial`, etc.), `ShaderMaterial` allows you to define the exact rendering logic for an object using your own **vertex shader** and **fragment shader** written in GLSL (OpenGL Shading Language).

*   **Vertex Shader:** Runs for each vertex of the geometry. Its primary job is to calculate the final position (`gl_Position`) of the vertex in clip space. It can also pass data (varyings) to the fragment shader.
*   **Fragment (Pixel) Shader:** Runs for each pixel (fragment) on the surface of the geometry. Its primary job is to calculate the final color (`gl_FragColor`) of that pixel.

## `ShaderMaterial`

*   **Purpose:** A Three.js material that takes custom GLSL shader code and uniform variables.
*   **Key Properties:**
    *   `vertexShader`: A string containing the GLSL code for the vertex shader.
    *   `fragmentShader`: A string containing the GLSL code for the fragment shader.
    *   `uniforms`: An object defining variables passed from your JavaScript code to the shaders. The values can be updated each frame.
    *   `defines`: An object defining preprocessor constants for the shaders.
    *   `vertexColors`: Boolean, set to `true` if using vertex colors (`vColor` attribute).
    *   `lights`: Boolean, set to `true` if the shader should receive lighting information from Three.js lights (requires including Three.js shader chunks).
    *   `transparent`: Boolean, needed for alpha blending.
    *   `depthWrite`, `depthTest`: Control depth buffer interactions.

```javascript
import * as THREE from 'three';

// 1. Define Uniforms (variables passed from JS to GLSL)
const uniforms = {
  uTime: { value: 0.0 }, // Example: Time for animation
  uColor: { value: new THREE.Color(0xff0000) }, // Example: Base color
  uTexture: { value: myTexture }, // Example: Texture
};

// 2. Define Vertex Shader (GLSL string)
const vertexShader = `
  // Varyings: Data passed from vertex to fragment shader
  varying vec2 vUv;
  varying float vElevation;

  // Uniforms: Variables from JavaScript
  uniform float uTime;

  void main() {
    vUv = uv; // Pass UV coordinates

    vec4 modelPosition = modelMatrix * vec4(position, 1.0);

    // Example: Simple wave animation on Y-axis
    float elevation = sin(modelPosition.x * 5.0 + uTime) * 0.2;
    modelPosition.y += elevation;
    vElevation = elevation; // Pass elevation to fragment shader

    vec4 viewPosition = viewMatrix * modelPosition;
    vec4 projectedPosition = projectionMatrix * viewPosition;

    gl_Position = projectedPosition; // Final vertex position
  }
`;

// 3. Define Fragment Shader (GLSL string)
const fragmentShader = `
  varying vec2 vUv; // Received from vertex shader
  varying float vElevation; // Received from vertex shader

  uniform vec3 uColor; // Received from JavaScript
  uniform sampler2D uTexture; // Received from JavaScript

  void main() {
    // Example: Mix color based on elevation
    float mixStrength = (vElevation + 0.2) / 0.4; // Normalize elevation
    vec3 finalColor = mix(uColor, vec3(0.0, 0.0, 1.0), mixStrength); // Mix red and blue

    // Example: Sample texture
    // vec4 textureColor = texture2D(uTexture, vUv);
    // gl_FragColor = textureColor;

    gl_FragColor = vec4(finalColor, 1.0); // Final pixel color (RGBA)
  }
`;

// 4. Create ShaderMaterial
const shaderMaterial = new THREE.ShaderMaterial({
  vertexShader: vertexShader,
  fragmentShader: fragmentShader,
  uniforms: uniforms,
  // lights: true, // Set to true if using Three.js lighting chunks
  // transparent: true,
});

// 5. Create Mesh and add to scene
const geometry = new THREE.PlaneGeometry(2, 2, 32, 32); // Use segmented geometry for vertex manipulation
const mesh = new THREE.Mesh(geometry, shaderMaterial);
// scene.add(mesh);

// 6. Update Uniforms in Animation Loop
function animate(time) {
  // Convert time to seconds
  const elapsedTime = time * 0.001;
  // Update time uniform
  uniforms.uTime.value = elapsedTime;

  // ... render scene ...
  renderer.render(scene, camera);
  requestAnimationFrame(animate);
}
requestAnimationFrame(animate);

```

## GLSL Basics

*   **Types:** `float`, `int`, `bool`, `vec2`, `vec3`, `vec4` (vectors), `mat2`, `mat3`, `mat4` (matrices), `sampler2D` (texture).
*   **Variables:**
    *   `attribute`: Input data per vertex (e.g., `position`, `normal`, `uv`). Defined by `BufferGeometry`.
    *   `uniform`: Input data constant across all vertices/fragments for a draw call (e.g., `uTime`, `uColor`, matrices like `modelMatrix`, `projectionMatrix`). Set via `ShaderMaterial.uniforms`.
    *   `varying`: Data passed from vertex shader to fragment shader. Interpolated across the face. Must be declared with the same name in both shaders.
*   **Built-in Variables:**
    *   Vertex Shader Output: `gl_Position` (required `vec4`).
    *   Fragment Shader Output: `gl_FragColor` (required `vec4`).
    *   Vertex Shader Input: `position` (`vec3`), `normal` (`vec3`), `uv` (`vec2`).
    *   Matrices (Uniforms provided by Three.js): `modelMatrix`, `viewMatrix`, `projectionMatrix`, `modelViewMatrix`, `normalMatrix`.
*   **Functions:** Standard math functions (`sin`, `cos`, `mix`, `clamp`, `step`, `smoothstep`, `length`, `dot`, `cross`, etc.). Texture sampling (`texture2D`).

## Three.js Shader Chunks

*   **Purpose:** Reusable snippets of GLSL code provided by Three.js for common tasks like lighting calculations, fog, UV transformations, etc.
*   **Usage:** Include them in your custom shaders using `#include <chunk_name>` syntax. Requires setting `lights: true` (or other relevant flags) on `ShaderMaterial`.
    ```glsl
    // Example Fragment Shader using lighting chunks
    varying vec3 vNormal;
    varying vec3 vViewPosition;

    uniform vec3 uColor;

    #include <common> // Includes basic utilities
    #include <lights_pars_begin> // Declares lighting uniforms/varyings

    void main() {
      #include <lights_fragment_begin> // Sets up lighting variables
      // Calculate diffuse color (simplified example)
      vec3 totalDiffuse = vec3(0.0);
      #include <lights_phong_fragment> // Calculates lighting based on Phong model
      // 'totalDiffuse' and 'totalSpecular' are populated by the chunk

      vec3 outgoingLight = totalDiffuse * uColor + totalSpecular; // Combine with material color

      gl_FragColor = vec4(outgoingLight, 1.0);
    }
    ```

## Considerations

*   **Complexity:** Writing custom shaders is significantly more complex than using built-in materials.
*   **Performance:** Shader performance depends heavily on the complexity of calculations, especially in the fragment shader. Profile carefully.
*   **Debugging:** Debugging GLSL can be challenging. Use `discard` for conditional rendering, output intermediate values to `gl_FragColor`, or use browser extensions like Spector.js.

*(Refer to the official Three.js ShaderMaterial documentation, GLSL documentation (e.g., The Book of Shaders), and Three.js shader chunk definitions.)*