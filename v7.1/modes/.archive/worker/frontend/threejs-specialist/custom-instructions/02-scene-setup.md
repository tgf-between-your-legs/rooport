# Basic Scene Setup

Creating the fundamental components for a Three.js scene: Scene, Camera, Renderer, and Render Loop.

## Core Concept: The Rendering Pipeline

To display anything with Three.js, you need these core components working together:

1.  **Scene (`THREE.Scene`):** A container that holds all your objects, lights, and cameras. Think of it as the stage.
2.  **Camera (`THREE.PerspectiveCamera` or `THREE.OrthographicCamera`):** Defines the viewpoint from which the scene is rendered. Determines what is visible and how it appears (perspective or orthographic projection).
3.  **Renderer (`THREE.WebGLRenderer`):** Takes the scene and camera information and draws the result onto an HTML `<canvas>` element using WebGL.
4.  **Objects (`THREE.Mesh`, `THREE.Group`, etc.):** The visible things in your scene, composed of Geometry (shape) and Material (appearance). (See `03-geometries.md`, `04-materials.md`).
5.  **Render Loop (`requestAnimationFrame` or `renderer.setAnimationLoop`):** A function that runs repeatedly (ideally 60 times per second) to update animations and tell the renderer to draw the scene from the camera's perspective for each frame.

## Implementation Steps

```javascript
import * as THREE from 'three';
// Optional: Import controls if needed
// import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

// --- 1. Scene ---
const scene = new THREE.Scene();
// Optional: Set background color
scene.background = new THREE.Color(0xeeeeee);
// Optional: Add fog
// scene.fog = new THREE.Fog(0xcccccc, 10, 50); // color, near, far

// --- 2. Camera ---
// PerspectiveCamera(fov, aspect, near, far)
// fov: Field of view (degrees) - how wide the view is
// aspect: Width / Height of the renderer output
// near: Near clipping plane - objects closer than this won't be rendered
// far: Far clipping plane - objects further than this won't be rendered
const camera = new THREE.PerspectiveCamera(
  75, // fov
  window.innerWidth / window.innerHeight, // aspect ratio
  0.1, // near plane
  1000 // far plane
);
// Position the camera
camera.position.z = 5; // Move camera back along Z-axis
camera.position.y = 2;
// camera.lookAt(scene.position); // Look at the center by default

// --- 3. Renderer ---
const renderer = new THREE.WebGLRenderer({
  antialias: true, // Smooths jagged edges (can impact performance)
  // alpha: true, // Make canvas background transparent (if needed)
});
// Set the size of the renderer output (usually canvas size)
renderer.setSize(window.innerWidth, window.innerHeight);
// Optional: Improve color accuracy (Important for PBR)
renderer.outputColorSpace = THREE.SRGBColorSpace;
// Optional: Enable shadow map rendering (See 06-lights-shadows.md)
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap; // Optional softer shadows

// Append the renderer's canvas element to the DOM
document.body.appendChild(renderer.domElement);

// --- Optional: Camera Controls ---
// (See 07-camera-controls.md)
// const controls = new OrbitControls(camera, renderer.domElement);
// controls.enableDamping = true;
// controls.update(); // Required in loop if enableDamping is true

// --- Add Objects to Scene (Example) ---
// (See 03-geometries.md, 04-materials.md, 06-lights-shadows.md)
const geometry = new THREE.BoxGeometry(1, 1, 1);
const material = new THREE.MeshStandardMaterial({ color: 0x00ff00 }); // Use Standard for lights
const cube = new THREE.Mesh(geometry, material);
cube.castShadow = true; // Allow cube to cast shadows
scene.add(cube); // Add the cube to the scene

const planeGeometry = new THREE.PlaneGeometry(10, 10);
const planeMaterial = new THREE.MeshStandardMaterial({ color: 0xcccccc, side: THREE.DoubleSide });
const plane = new THREE.Mesh(planeGeometry, planeMaterial);
plane.rotation.x = -Math.PI / 2;
plane.position.y = -0.5;
plane.receiveShadow = true; // Allow plane to receive shadows
scene.add(plane);

const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
scene.add(ambientLight);

const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
directionalLight.position.set(5, 10, 7);
directionalLight.castShadow = true;
scene.add(directionalLight);

// --- 4. Render Loop ---
function animate() {
  // Request the next frame *first*
  requestAnimationFrame(animate);

  // Update animations or objects
  cube.rotation.x += 0.01;
  cube.rotation.y += 0.01;

  // Update controls if damping is enabled
  // controls.update();

  // Render the scene from the camera's perspective
  renderer.render(scene, camera);
}

// Alternative using renderer.setAnimationLoop (handles WebXR sessions automatically)
// renderer.setAnimationLoop( function () {
//   cube.rotation.x += 0.01;
//   cube.rotation.y += 0.01;
//   // controls.update();
//	 renderer.render( scene, camera );
// });

// Start the animation loop
animate();

// --- Handle Window Resize ---
window.addEventListener('resize', onWindowResize, false);

function onWindowResize() {
    // Update camera aspect ratio
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();

    // Update renderer size
    renderer.setSize(window.innerWidth, window.innerHeight);
    // Optional: Adjust pixel ratio for high-DPI displays (consider performance)
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
}

// Call initially in case of high-DPI display
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

```

This basic setup creates a scene with a light, camera, renderer, a rotating cube casting shadows onto a plane, and starts the animation loop. Remember to handle window resizing.