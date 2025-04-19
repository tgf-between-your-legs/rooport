# Three.js: Interaction with Raycasting

Detecting mouse clicks or hovers on 3D objects using `THREE.Raycaster`.

## Core Concept: Raycasting

Raycasting is the process of shooting an invisible ray from a point (usually the camera) in a specific direction (usually towards the mouse cursor's position in 3D space) and determining which objects in the scene intersect with that ray. This is the primary method for detecting mouse interactions with 3D objects in Three.js.

**Key Components:**

*   **`THREE.Raycaster`:** The main class for performing raycasting.
*   **Origin:** The starting point of the ray (typically `camera.position`).
*   **Direction:** A normalized `THREE.Vector3` indicating the direction the ray travels. For mouse interaction, this vector points from the camera through the mouse cursor's projected position in the 3D scene.
*   **Mouse Coordinates:** Need to convert the 2D mouse coordinates (from `event.clientX`, `event.clientY`) into normalized device coordinates (NDC), which range from -1 to +1 for both X and Y.
*   **`raycaster.setFromCamera(coords, camera)`:** Helper method to set the raycaster's origin and direction based on normalized mouse coordinates and the camera.
*   **`raycaster.intersectObjects(objects, recursive?)`:** Checks for intersections between the ray and an array of `THREE.Object3D` instances (or their children if `recursive` is true). Returns an array of intersection objects, sorted by distance (closest first).
*   **Intersection Object:** Contains information about an intersection:
    *   `distance`: Distance from the ray's origin to the intersection point.
    *   `point`: `THREE.Vector3` representing the intersection point in world space.
    *   `object`: The specific `THREE.Object3D` that was intersected.
    *   `face`, `faceIndex`: Information about the specific face intersected (if available).
    *   `uv`: UV coordinates at the intersection point.

## Implementation Steps

1.  **Store Mouse Coordinates:** Add event listeners (e.g., `mousemove`, `click`) to the renderer's DOM element (canvas) to capture mouse coordinates. Store the normalized device coordinates (-1 to +1 range).

    ```javascript
    const mouse = new THREE.Vector2(); // Store normalized coordinates (-1 to +1)

    function onPointerMove( event ) {
        // Calculate pointer position in normalized device coordinates
        // (-1 to +1) for both components
        mouse.x = ( event.clientX / window.innerWidth ) * 2 - 1;
        mouse.y = - ( event.clientY / window.innerHeight ) * 2 + 1;
    }

    window.addEventListener( 'pointermove', onPointerMove );
    ```

2.  **Instantiate Raycaster:** Create a `THREE.Raycaster` instance.

    ```javascript
    const raycaster = new THREE.Raycaster();
    ```

3.  **Perform Raycasting (in Render Loop or Event Handler):**
    *   **Update Ray:** Call `raycaster.setFromCamera(mouse, camera)` to update the ray's origin and direction based on the current mouse position and camera view.
    *   **Check Intersections:** Call `raycaster.intersectObjects(scene.children, true)` (or pass a specific array of interactive objects) to get intersections.
    *   **Process Intersections:** Check if the returned array is non-empty. The first element (`intersects[0]`) is usually the closest intersected object. Use `intersects[0].object` to identify which object was hit.

    ```javascript
    // Example: Checking intersections on every frame (for hover effects)
    let intersectedObject = null; // Keep track of hovered object

    function render() { // Inside your render loop
        // Update the picking ray with the camera and pointer position
        raycaster.setFromCamera(mouse, camera);

        // Calculate objects intersecting the picking ray
        const intersects = raycaster.intersectObjects(scene.children, true); // Check recursively

        // Reset previous intersected object's state (if any)
        if (intersectedObject) {
            // Example: Reset material color
            // intersectedObject.material.color.set(intersectedObject.userData.originalColor);
            intersectedObject = null;
        }

        if (intersects.length > 0) {
            // Get the closest intersected object
            intersectedObject = intersects[0].object;

            // Apply hover effect
            // Example: Change material color and store original
            // if (!intersectedObject.userData.originalColor) {
            //     intersectedObject.userData.originalColor = intersectedObject.material.color.getHex();
            // }
            // intersectedObject.material.color.set(0xff0000); // Set to red on hover

            // console.log('Hovering over:', intersectedObject.name || intersectedObject.uuid);
        }

        renderer.render(scene, camera);
    }

    // Example: Checking intersections on click
    function onClick(event) {
        // Update mouse coords (might be slightly different from move event)
        mouse.x = ( event.clientX / window.innerWidth ) * 2 - 1;
        mouse.y = - ( event.clientY / window.innerHeight ) * 2 + 1;

        raycaster.setFromCamera(mouse, camera);
        const intersects = raycaster.intersectObjects(scene.children, true);

        if (intersects.length > 0) {
            const clickedObject = intersects[0].object;
            console.log('Clicked on:', clickedObject.name || clickedObject.uuid);
            // Trigger actions based on the clicked object
            // e.g., open a modal, navigate, change state
        }
    }
    window.addEventListener('click', onClick);
    ```

## Considerations

*   **Performance:** Raycasting on every frame (`mousemove`) can be performance-intensive, especially with complex scenes. Consider:
    *   Raycasting only on specific events like `click`.
    *   Limiting the array of objects passed to `intersectObjects` to only those that are interactive.
    *   Debouncing or throttling `mousemove` events if necessary.
*   **Recursive Flag:** Setting the second argument of `intersectObjects` to `true` checks children of the objects in the array. This is often needed for loaded models (`gltf.scene` is usually a `Group`).
*   **Coordinate Conversion:** Ensure mouse coordinates are correctly converted to the -1 to +1 NDC range.
*   **Object Identification:** Use `object.name`, `object.uuid`, or `object.userData` to identify which object was intersected and trigger appropriate actions.

Raycasting is the standard technique for bridging 2D mouse input with your 3D scene in Three.js, enabling clicks, hovers, and other interactions with objects.

*(Refer to the official Three.js documentation on Raycaster.)*