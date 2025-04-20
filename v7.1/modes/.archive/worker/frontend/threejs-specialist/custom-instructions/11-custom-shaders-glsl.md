# Custom Shaders (GLSL &amp; ShaderMaterial)

Creating unique visual effects by writing custom vertex and fragment shaders using GLSL.

## Core Concept: Programmable Rendering Pipeline

While Three.js's built-in materials cover many common use cases, **`ShaderMaterial`** (and `RawShaderMaterial`) allows you to take full control of the GPU rendering pipeline by providing your own **vertex shader** and **fragment shader** code written in **GLSL** (OpenGL Shading Language).

*   **Vertex Shader:** Runs once for each vertex in your geometry. Its primary job is to calculate the final `gl_Position` (the vertex's position in 2D screen space) based on the object's position, camera view, and projection. It can also pass data (**varyings**) to the fragment shader.
*   **Fragment (Pixel) Shader:** Runs once for every pixel (fragment) on the screen that the geometry covers. Its primary job is to calculate the final `gl_FragColor` (the pixel's RGBA color). It receives data (**varyings**) interpolated from the vertex shader.
*   **GLSL:** A C-like language specifically for programming GPUs. It includes vector types (`vec2`, `vec3`, `vec4`), matrix types (`mat3`, `mat4`), texture samplers (`sampler2D`), and built-in functions (`mix`, `smoothstep`, `sin`, `cos`, `texture2D`, etc.).
*   **`ShaderMaterial`:** A Three.js material that takes GLSL shader code strings and uniform definitions. It automatically adds common Three.js uniforms (like `modelViewMatrix`, `projectionMatrix`) and attributes (`position`, `normal`, `uv`). **Generally preferred.**
*   **`RawShaderMaterial`:** Similar to `ShaderMaterial`, but *does not* automatically add Three.js uniforms/attributes. You must declare and manage them all manually. Used for highly specific cases or when porting shaders from other environments.

## Implementation Steps

1.  **Write GLSL Shaders:** Create strings containing your vertex and fragment shader code.
    *   **Vertex Shader (`vertexShader` string):**
        *   Must output `gl_Position` (a `vec4`). Typically calculated as `projectionMatrix * viewMatrix * modelMatrix * vec4(position, 1.0);`.
        *   Receives attributes like `vec3 position`, `vec3 normal`, `vec2 uv` (if defined in geometry and used by shader).
        *   Receives uniforms like `mat4 modelMatrix`, `mat4 viewMatrix`, `mat4 projectionMatrix`, `mat3 normalMatrix`.
        *   Can define `varying` variables (e.g., `varying vec2 vUv;`) to pass interpolated data to the fragment shader. Declare the same varying in the fragment shader.
    *   **Fragment Shader (`fragmentShader` string):**
        *   Must output `gl_FragColor` (a `vec4` representing RGBA color).
        *   Receives `varying` variables interpolated from the vertex shader.
        *   Receives uniforms like textures (`sampler2D`), colors (`vec3`), floats (`float`), time (`float`), etc.

2.  **Define Uniforms:** Create a `uniforms` object in JavaScript. This object defines the data you want to pass from your JavaScript code into your shaders.
    *   Keys are the uniform names used in GLSL (e.g., `uTime`, `uColor`, `uTexture`).
    *   Values are objects with a `value` property holding the initial value (e.g., `0.0`, `new THREE.Color(0xff0000)`, `myTexture`).
    *   Uniform values can be updated from your JavaScript animation loop (e.g., `myShaderMaterial.uniforms.uTime.value = elapsedTime;`).

3.  **Create `ShaderMaterial`:** Instantiate `ShaderMaterial`, passing the `uniforms`, `vertexShader`, and `fragmentShader` strings. Configure other material properties as needed (`transparent`, `side`, `lights`, etc.).

4.  **Apply Material:** Use the `ShaderMaterial` on a `Mesh`.

## Example: Animated Wave Shader

```glsl
// --- Vertex Shader ---
varying vec2 vUv;
varying float vElevation;

uniform float uTime;
uniform float uFrequency; // Control wave frequency from JS

void main() {
  vUv = uv; // Pass UV to fragment shader

  vec4 modelPosition = modelMatrix * vec4(position, 1.0);

  // Simple wave animation on Y-axis based on X position and time
  float elevation = sin(modelPosition.x * uFrequency + uTime * 2.0) * 0.1; // Wave height 0.1
  modelPosition.y += elevation;
  vElevation = elevation; // Pass elevation to fragment shader

  vec4 viewPosition = viewMatrix * modelPosition;
  vec4 projectedPosition = projectionMatrix * viewPosition;

  gl_Position = projectedPosition; // Final vertex position
}
```

```glsl
// --- Fragment Shader ---
varying vec2 vUv; // Received from vertex shader
varying float vElevation; // Received from vertex shader

uniform vec3 uColor; // Base color from JS
uniform sampler2D uTexture; // Texture from JS

void main() {
  // Example 1: Mix color based on elevation
  // float mixStrength = (vElevation + 0.1) / 0.2; // Normalize elevation to 0-1 range
  // vec3 finalColor = mix(uColor, vec3(0.0, 0.0, 1.0), mixStrength); // Mix base color with blue

  // Example 2: Sample texture and modify color based on elevation
  vec4 textureColor = texture2D(uTexture, vUv);
  textureColor.rgb *= (vElevation * 2.0 + 0.8); // Make higher parts brighter

  gl_FragColor = textureColor; // Final pixel color (RGBA)
  // gl_FragColor = vec4(finalColor, 1.0); // Use if using Example 1
}
```

```javascript
// --- JavaScript ---
import * as THREE from 'three';

// Assume textureLoader is created and myTexture is loaded
// const myTexture = textureLoader.load('/textures/water.jpg');
// myTexture.wrapS = myTexture.wrapT = THREE.RepeatWrapping;

// Define uniforms
const uniforms = {
    uTime: { value: 0.0 },
    uFrequency: { value: 10.0 }, // Example frequency control
    uColor: { value: new THREE.Color(0x0055aa) },
    uTexture: { value: myTexture },
};

// Create the ShaderMaterial
const waveMaterial = new THREE.ShaderMaterial({
    uniforms: uniforms,
    vertexShader: `/* Paste Vertex Shader GLSL here */`,
    fragmentShader: `/* Paste Fragment Shader GLSL here */`,
    side: THREE.DoubleSide,
    // transparent: true, // If using alpha
});

// Use segmented geometry for vertex manipulation
const geometry = new THREE.PlaneGeometry(2, 2, 64, 64);
const mesh = new THREE.Mesh(geometry, waveMaterial);
// scene.add(mesh);

// --- Update Uniforms in Render Loop ---
const clock = new THREE.Clock();
function animate() {
    const elapsedTime = clock.getElapsedTime();
    waveMaterial.uniforms.uTime.value = elapsedTime; // Update time uniform

    // Optional: Animate frequency or other uniforms
    // waveMaterial.uniforms.uFrequency.value = Math.sin(elapsedTime * 0.5) * 5 + 10;

    renderer.render(scene, camera);
    requestAnimationFrame(animate);
}
animate();
```

## GLSL Basics Recap

*   **Types:** `float`, `int`, `bool`, `vec2`, `vec3`, `vec4`, `mat2`, `mat3`, `mat4`, `sampler2D`.
*   **Qualifiers:**
    *   `attribute`: Per-vertex input (from `BufferGeometry`). Vertex shader only.
    *   `uniform`: Constant input per draw call (from JS `uniforms`). Both shaders.
    *   `varying`: Passed from vertex to fragment shader (interpolated).
*   **Built-ins (Examples):**
    *   Vertex In: `position`, `normal`, `uv`.
    *   Vertex Out: `gl_Position` (required).
    *   Fragment Out: `gl_FragColor` (required).
    *   Fragment In: `gl_FragCoord` (pixel coords), `gl_FrontFacing` (bool).
    *   Matrices (Uniforms): `modelMatrix`, `viewMatrix`, `projectionMatrix`, `modelViewMatrix`, `normalMatrix`.
*   **Functions:** `sin`, `cos`, `mix`, `clamp`, `step`, `smoothstep`, `length`, `dot`, `cross`, `texture2D`, etc.

## Three.js Shader Chunks

*   **Purpose:** Reusable snippets of GLSL code provided by Three.js for common tasks (lighting, fog, UV transforms).
*   **Usage:** Include using `#include <chunk_name>` (e.g., `#include <common>`, `#include <lights_pars_fragment>`, `#include <fog_fragment>`). Requires setting relevant flags on `ShaderMaterial` (e.g., `lights: true`, `fog: true`). Consult Three.js source or examples for available chunks and usage.

Custom shaders offer immense creative possibilities but require understanding GLSL and the graphics pipeline. Start simple, leverage `ShaderMaterial`'s automatic uniforms/attributes, and debug iteratively.