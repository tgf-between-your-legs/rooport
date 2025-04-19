# Three.js: Custom Shaders (GLSL & ShaderMaterial)

Creating unique visual effects by writing custom vertex and fragment shaders using GLSL.

## Core Concept: Programmable Rendering Pipeline

While Three.js's built-in materials cover many common use cases, **ShaderMaterial** (and `RawShaderMaterial`) allows you to take full control of the GPU rendering pipeline by providing your own **vertex shader** and **fragment shader** code written in **GLSL** (OpenGL Shading Language).

*   **Vertex Shader:** Runs once for each vertex in your geometry. Its primary job is to calculate the final `gl_Position` (the vertex's position in 2D screen space) based on the object's position, camera view, and projection. It can also pass data (varyings) to the fragment shader.
*   **Fragment (Pixel) Shader:** Runs once for every pixel (fragment) on the screen that the geometry covers. Its primary job is to calculate the final `gl_FragColor` (the pixel's color). It receives data (varyings) interpolated from the vertex shader.
*   **GLSL:** A C-like language specifically for programming GPUs. It includes vector types (`vec2`, `vec3`, `vec4`), matrix types (`mat3`, `mat4`), texture samplers (`sampler2D`), and built-in functions (`mix`, `smoothstep`, `sin`, `cos`, etc.).
*   **`ShaderMaterial`:** A Three.js material that takes GLSL shader code strings and uniform definitions. It automatically adds common Three.js uniforms (like `modelViewMatrix`, `projectionMatrix`) and attributes (`position`, `normal`, `uv`).
*   **`RawShaderMaterial`:** Similar to `ShaderMaterial`, but *does not* automatically add Three.js uniforms/attributes. You must declare and manage them all manually. Used for highly specific cases or when porting shaders from other environments.

## Implementation Steps

1.  **Write GLSL Shaders:** Create strings containing your vertex and fragment shader code.
    *   **Vertex Shader (`vertexShader`):**
        *   Must output `gl_Position` (a `vec4`). Typically calculated as `projectionMatrix * modelViewMatrix * vec4(position, 1.0);`.
        *   Receives attributes like `vec3 position`, `vec3 normal`, `vec2 uv` (if defined in geometry and used by shader).
        *   Receives uniforms like `mat4 modelViewMatrix`, `mat4 projectionMatrix`.
        *   Can define `varying` variables to pass interpolated data (like UVs or world position) to the fragment shader.
    *   **Fragment Shader (`fragmentShader`):**
        *   Must output `gl_FragColor` (a `vec4` representing RGBA color).
        *   Receives `varying` variables interpolated from the vertex shader.
        *   Receives uniforms like textures (`sampler2D`), colors (`vec3`), floats (`float`), etc.

2.  **Define Uniforms:** Create a `uniforms` object in JavaScript. This object defines the data you want to pass from your JavaScript code into your shaders.
    *   Keys are the uniform names used in GLSL.
    *   Values are objects with a `value` property holding the initial value (e.g., `new THREE.Color(0xff0000)`, `myTexture`, `0.5`).
    *   Uniform values can be updated from your JavaScript animation loop.

3.  **Create `ShaderMaterial`:** Instantiate `ShaderMaterial`, passing the `uniforms`, `vertexShader`, and `fragmentShader` strings.

4.  **Apply Material:** Use the `ShaderMaterial` on a `Mesh`.

## Example: Simple UV Color Shader

```glsl
// --- Vertex Shader ---
// Varying to pass UV coordinates to fragment shader
varying vec2 vUv;

void main() {
  // Pass the UV attribute to the varying
  vUv = uv;

  // Calculate final screen position (standard calculation)
  gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
}
```

```glsl
// --- Fragment Shader ---
// Receive interpolated UV coordinates
varying vec2 vUv;

// Optional: Uniform for a base color
uniform vec3 uColor;

void main() {
  // Output color based on UV coordinates (Red = U, Green = V)
  // gl_FragColor = vec4(vUv.x, vUv.y, 0.0, 1.0);

  // Or output color based on uniform
   gl_FragColor = vec4(uColor, 1.0);

  // Or combine UVs and color
  // gl_FragColor = vec4(uColor * vec3(vUv.x, vUv.y, 1.0), 1.0);
}
```

```javascript
// --- JavaScript ---
import * as THREE from 'three';

// Define uniforms
const uniforms = {
    // Define a color uniform, accessible as 'uColor' in GLSL
    uColor: { value: new THREE.Color(0x00ffff) } // Cyan
    // uTime: { value: 0.0 } // Example time uniform for animation
    // uTexture: { value: myTexture } // Example texture uniform
};

// Create the ShaderMaterial
const customMaterial = new THREE.ShaderMaterial({
    uniforms: uniforms,
    vertexShader: `
        varying vec2 vUv;
        void main() {
            vUv = uv;
            gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
        }
    `,
    fragmentShader: `
        varying vec2 vUv;
        uniform vec3 uColor;
        void main() {
            // Use UVs to create a pattern and mix with uniform color
            float pattern = (sin(vUv.x * 20.0) + sin(vUv.y * 20.0)) * 0.5 + 0.5;
            gl_FragColor = vec4(uColor * pattern, 1.0);
        }
    `,
    // wireframe: true,
    // side: THREE.DoubleSide,
});

const geometry = new THREE.PlaneGeometry(2, 2); // Plane has UVs
const mesh = new THREE.Mesh(geometry, customMaterial);
// scene.add(mesh);

// --- Update Uniforms in Render Loop (Example) ---
// const clock = new THREE.Clock();
// function animate() {
//     const elapsedTime = clock.getElapsedTime();
//     customMaterial.uniforms.uTime.value = elapsedTime; // Update time uniform
//     renderer.render(scene, camera);
//     requestAnimationFrame(animate);
// }
```

Custom shaders offer immense creative possibilities but require understanding GLSL and the graphics pipeline. Start simple, use built-in uniforms/attributes provided by `ShaderMaterial`, and debug using `console.log` (in JS) and by outputting intermediate values as colors in the fragment shader.

*(Refer to the official Three.js documentation on ShaderMaterial, RawShaderMaterial, and GLSL concepts. Resources like "The Book of Shaders" are excellent for learning GLSL.)*