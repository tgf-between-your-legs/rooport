# Camera Controls

Adding interactive camera controls like orbit, trackball, and fly controls to a Three.js scene.

## Core Concept: User Camera Manipulation

To allow users to navigate and view your 3D scene from different angles, you typically use pre-built camera control libraries provided by Three.js. These libraries listen to mouse, touch, and keyboard events and update the camera's position and orientation accordingly.

**Key Points:**

*   **Separate Modules:** Controls are located in the `three/addons/controls/` directory and need to be imported separately.
*   **Instantiation:** Create an instance of a control class, passing the `camera` object and the renderer's `domElement` (for event listeners).
*   **Update in Render Loop:** Most controls (especially those with damping/inertia or time-based movement like `FlyControls`) require their `.update()` method to be called within the animation loop to function correctly.

## Common Control Types

1.  **`OrbitControls`:**
    *   **Behavior:** Allows orbiting around a target point (defaulting to scene origin), dollying (zooming), and panning. Very common for model viewers and general scene exploration.
    *   **Import:** `import { OrbitControls } from 'three/addons/controls/OrbitControls.js';`
    *   **Key Options:**
        *   `enableDamping`: Creates a smoother, more natural movement inertia (requires calling `controls.update()` in loop).
        *   `dampingFactor`: Controls the amount of damping.
        *   `autoRotate`, `autoRotateSpeed`: Automatically orbit the camera. Requires `controls.update()` in loop.
        *   `enableZoom`, `enablePan`, `enableRotate`: Toggle specific interactions.
        *   `minDistance`, `maxDistance`: Limit zooming.
        *   `minPolarAngle`, `maxPolarAngle`: Limit vertical orbiting angle (radians).
        *   `minAzimuthAngle`, `maxAzimuthAngle`: Limit horizontal orbiting angle (radians).
        *   `target`: The `Vector3` point the camera orbits around. `controls.target.set(x, y, z);`.

    ```javascript
    import * as THREE from 'three';
    import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

    // Assuming camera and renderer are already created
    const controls = new OrbitControls(camera, renderer.domElement);

    // Optional configuration
    controls.enableDamping = true; // Requires controls.update() in animation loop
    controls.dampingFactor = 0.05;
    controls.screenSpacePanning = false; // Keep panning parallel to ground plane unless true
    controls.minDistance = 2;
    controls.maxDistance = 50;
    controls.maxPolarAngle = Math.PI / 2 - 0.05; // Prevent orbiting slightly below ground
    // controls.target.set(0, 1, 0); // Orbit around a point 1 unit up

    // --- In the animation loop ---
    function animate() {
        requestAnimationFrame(animate);
        controls.update(); // Update controls (needed for damping/autoRotate)
        renderer.render(scene, camera);
    }
    animate();
    ```

2.  **`TrackballControls`:**
    *   **Behavior:** Similar to OrbitControls but allows "rolling" the camera and doesn't have a fixed vertical axis, offering more free-form rotation. Can feel less intuitive for simple orbiting.
    *   **Import:** `import { TrackballControls } from 'three/addons/controls/TrackballControls.js';`
    *   **Key Options:** `noZoom`, `noPan`, `noRotate`, `rotateSpeed`, `zoomSpeed`, `panSpeed`, `dynamicDampingFactor`, `staticMoving`.
    *   **Requires:** Calling `controls.update()` in the animation loop.

3.  **`FlyControls`:**
    *   **Behavior:** Allows flying through the scene using mouse look and keyboard movement (W, A, S, D, R, F), similar to first-person games or flight simulators.
    *   **Import:** `import { FlyControls } from 'three/addons/controls/FlyControls.js';`
    *   **Key Options:** `movementSpeed`, `rollSpeed`, `dragToLook`, `autoForward`.
    *   **Requires:** Calling `controls.update(deltaTime)` in the animation loop, passing the time delta obtained from `THREE.Clock`.

    ```javascript
    // import { FlyControls } from 'three/addons/controls/FlyControls.js';
    // const clock = new THREE.Clock();
    // const flyControls = new FlyControls(camera, renderer.domElement);
    // flyControls.movementSpeed = 10;
    // flyControls.rollSpeed = Math.PI / 12;
    // --- In animation loop ---
    // const delta = clock.getDelta();
    // flyControls.update(delta);
    ```

4.  **`FirstPersonControls`:**
    *   **Behavior:** Similar to FlyControls but constrained movement, often better suited for ground-level first-person perspectives where the camera doesn't roll.
    *   **Import:** `import { FirstPersonControls } from 'three/addons/controls/FirstPersonControls.js';`
    *   **Requires:** Calling `controls.update(deltaTime)` in the animation loop.

5.  **`PointerLockControls`:**
    *   **Behavior:** Implements first-person shooter style controls where the mouse cursor is locked, and movement directly controls the camera view. Requires user interaction (click) to activate pointer lock and manual handling of keyboard events for movement.
    *   **Import:** `import { PointerLockControls } from 'three/addons/controls/PointerLockControls.js';`
    *   **Requires:** Adding event listeners for `lock`/`unlock`, handling keyboard input to call `controls.moveForward()` and `controls.moveRight()`, and updating within the animation loop. More complex setup.

## Choosing Controls

*   **`OrbitControls`:** Best for general object viewing and scene exploration where the user orbits a central point. Most common and intuitive for many applications.
*   **`TrackballControls`:** For free-form rotation without a fixed up-axis, useful in specific scientific or modeling contexts.
*   **`FlyControls` / `FirstPersonControls`:** For navigating *through* a large scene or environment from a first-person perspective.
*   **`PointerLockControls`:** For immersive FPS-style experiences requiring direct mouse look.

Remember to import the specific control module, instantiate it with the camera and DOM element, configure its options, and call `controls.update()` (potentially with `deltaTime`) in your animation loop if required by the control type or its configuration (like `enableDamping`). Dispose of controls (`controls.dispose()`) when they are no longer needed, especially in SPA frameworks, to remove event listeners.