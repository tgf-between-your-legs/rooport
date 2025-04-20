# Three.js: Camera Controls

Adding interactive camera controls like orbit, trackball, and fly controls to a Three.js scene.

## Core Concept: User Camera Manipulation

To allow users to navigate and view your 3D scene from different angles, you typically use pre-built camera control libraries provided by Three.js or the community. These libraries listen to mouse and keyboard events and update the camera's position and orientation accordingly.

**Key Points:**

*   **Separate Modules:** Controls are usually located in the `three/addons/controls/` directory and need to be imported separately.
*   **Instantiation:** You create an instance of a control class, passing the `camera` object and the renderer's `domElement` (for event listeners).
*   **Update in Render Loop:** Most controls (especially those with damping/inertia) require their `.update()` method to be called within the animation loop to function correctly.

## Common Control Types

1.  **`OrbitControls`:**
    *   **Behavior:** Allows orbiting around a target point (defaulting to scene origin), dollying (zooming), and panning. Very common for model viewers and general scene exploration.
    *   **Import:** `import { OrbitControls } from 'three/addons/controls/OrbitControls.js';`
    *   **Key Options:**
        *   `enableDamping`: Creates a smoother, more natural movement inertia (requires calling `controls.update()` in loop).
        *   `dampingFactor`: Controls the amount of damping.
        *   `enableZoom`, `enablePan`, `enableRotate`: Toggle specific interactions.
        *   `minDistance`, `maxDistance`: Limit zooming.
        *   `minPolarAngle`, `maxPolarAngle`: Limit vertical orbiting angle.
        *   `target`: The `Vector3` point the camera orbits around.

    ```javascript
    import * as THREE from 'three';
    import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

    // Assuming camera and renderer are already created
    // const camera = new THREE.PerspectiveCamera(...);
    // const renderer = new THREE.WebGLRenderer(...);
    // document.body.appendChild(renderer.domElement);

    const controls = new OrbitControls(camera, renderer.domElement);

    // Optional configuration
    controls.enableDamping = true; // an animation loop is required when either damping or auto-rotation are enabled
    controls.dampingFactor = 0.05;
    controls.screenSpacePanning = false; // Keep panning parallel to ground plane
    controls.minDistance = 2;
    controls.maxDistance = 10;
    controls.maxPolarAngle = Math.PI / 2; // Prevent orbiting below ground

    // --- In the animation loop ---
    function animate() {
        requestAnimationFrame(animate);

        controls.update(); // only required if controls.enableDamping = true, or if controls.autoRotate = true

        renderer.render(scene, camera);
    }
    animate();
    ```

2.  **`TrackballControls`:**
    *   **Behavior:** Similar to OrbitControls but allows "rolling" the camera and doesn't have a fixed vertical axis, offering more free-form rotation. Can feel less intuitive for simple orbiting.
    *   **Import:** `import { TrackballControls } from 'three/addons/controls/TrackballControls.js';`
    *   **Key Options:** `noZoom`, `noPan`, `noRotate`, `rotateSpeed`, `zoomSpeed`, `panSpeed`, `dynamicDampingFactor`.
    *   **Requires:** Calling `controls.update()` in the animation loop.

3.  **`FlyControls`:**
    *   **Behavior:** Allows flying through the scene using mouse look and keyboard movement (W, A, S, D, R, F), similar to first-person games.
    *   **Import:** `import { FlyControls } from 'three/addons/controls/FlyControls.js';`
    *   **Key Options:** `movementSpeed`, `rollSpeed`, `dragToLook`.
    *   **Requires:** Calling `controls.update(deltaTime)` in the animation loop, passing the time delta.

4.  **`FirstPersonControls`:**
    *   **Behavior:** Similar to FlyControls but constrained movement, often better suited for ground-level first-person perspectives.
    *   **Import:** `import { FirstPersonControls } from 'three/addons/controls/FirstPersonControls.js';`
    *   **Requires:** Calling `controls.update(deltaTime)` in the animation loop.

5.  **`PointerLockControls`:**
    *   **Behavior:** Implements first-person shooter style controls where the mouse cursor is locked, and movement directly controls the camera view. Requires user interaction (click) to activate pointer lock.
    *   **Import:** `import { PointerLockControls } from 'three/addons/controls/PointerLockControls.js';`
    *   **Requires:** Manual handling of keyboard events to move the camera (`controls.moveForward()`, `controls.moveRight()`) and updating within the animation loop.

## Choosing Controls

*   **`OrbitControls`:** Best for general object viewing and scene exploration where the user orbits a central point.
*   **`TrackballControls`:** For free-form rotation without a fixed up-axis.
*   **`FlyControls` / `FirstPersonControls`:** For navigating *through* a scene from a first-person perspective.
*   **`PointerLockControls`:** For immersive FPS-style experiences.

Remember to import the specific control module, instantiate it with the camera and DOM element, and call `controls.update()` in your animation loop if required by the control type (especially if damping is enabled).

*(Refer to the official Three.js documentation under Examples > Controls for specific control types.)*