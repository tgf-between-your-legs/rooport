# Interaction with Raycasting

Detecting mouse clicks, hovers, or other pointer interactions on 3D objects using `THREE.Raycaster`.

## Core Concept

Raycasting involves projecting an invisible ray (a straight line) from the camera's position through the pointer's position on the screen into the 3D scene. You then check which objects in the scene intersect with this ray, allowing you to identify what the user is pointing at or clicking on.

## Implementation Steps

1.  **Store Pointer Coordinates (Normalized Device Coordinates - NDC):**
    *   Listen for pointer events (e.g., `pointermove`, `click`, `pointerdown`) on the renderer's DOM element (`renderer.domElement`).
    *   Convert the screen coordinates (pixels, `event.clientX`, `event.clientY`) to Normalized Device Coordinates (NDC). NDC range from -1 to +1 for both X and Y, with (0,0) being the center of the canvas.
    *   Account for the canvas's position and size on the page using `getBoundingClientRect()`.

    ```javascript
    import * as THREE from 'three';

    const pointer = new THREE.Vector2(); // Reusable vector for NDC coordinates

    function onPointerMove( event ) {
        // Calculate pointer position in normalized device coordinates (-1 to +1)
        const rect = renderer.domElement.getBoundingClientRect();
        pointer.x = ( ( event.clientX - rect.left ) / rect.width ) * 2 - 1;
        pointer.y = - ( ( event.clientY - rect.top ) / rect.height ) * 2 + 1; // Y is inverted (origin bottom-left in NDC)
    }

    // Listen on the canvas element for better accuracy
    renderer.domElement.addEventListener( 'pointermove', onPointerMove );
    // Add similar listeners for 'click' or 'pointerdown' as needed
    // renderer.domElement.addEventListener( 'click', onClick );
    ```

2.  **Create `Raycaster`:** Instantiate `THREE.Raycaster`. You typically only need one instance.

    ```javascript
    const raycaster = new THREE.Raycaster();
    ```

3.  **Update Raycaster and Check Intersections:**
    *   Inside your event handler (`onClick`) or animation loop (for hover effects), update the raycaster with the current camera and the normalized pointer coordinates using `raycaster.setFromCamera()`.
    *   Call `raycaster.intersectObjects()` passing an array of the `Object3D` instances you want to check against. Set the second argument (`recursive`) to `true` if you want to check children of groups or loaded models.
    *   The method returns an array of intersection objects, sorted by distance from the camera (closest first).

    ```javascript
    let intersectedObject: THREE.Object3D | null = null; // Keep track of the currently hovered object

    function checkIntersections() {
      // Update the picking ray with the camera and pointer position
      raycaster.setFromCamera( pointer, camera ); // camera is your THREE.Camera

      // Calculate objects intersecting the picking ray
      // Pass the array of objects you want to test (e.g., interactive meshes, scene children)
      const objectsToTest = scene.children; // Or a specific group: myInteractiveGroup.children
      const intersects = raycaster.intersectObjects( objectsToTest, true ); // `true` for recursive check

      if (intersects.length > 0) {
        // intersects[0] is the closest intersected object
        const closestIntersect = intersects[0];
        // console.log('Intersected:', closestIntersect.object.name || closestIntersect.object.uuid);
        // console.log('Intersection Point:', closestIntersect.point);
        // console.log('Distance:', closestIntersect.distance);
        // console.log('UV Coords:', closestIntersect.uv);

        // --- Handle Hover Effect ---
        if (intersectedObject !== closestIntersect.object) {
            // Mouse moved onto a new object
            if (intersectedObject) {
                // Reset previous hovered object's appearance (example)
                // intersectedObject.material.emissive?.setHex(0x000000);
            }
            intersectedObject = closestIntersect.object;
            // Highlight current hovered object (example)
            // if (intersectedObject.material.emissive) {
            //    intersectedObject.material.emissive.setHex(0xff0000);
            // }
            // Change cursor style
            document.body.style.cursor = 'pointer';
        }
      } else {
        // --- Handle Mouse Out ---
        if (intersectedObject) {
            // Reset previous hovered object's appearance (example)
            // intersectedObject.material.emissive?.setHex(0x000000);
        }
        intersectedObject = null;
        // Restore default cursor style
        document.body.style.cursor = 'default';
      }
    }

    // --- How to Trigger checkIntersections ---

    // Option A: Check on every frame (for hover effects) in the animation loop
    // function animate() {
    //   requestAnimationFrame(animate);
    //   checkIntersections(); // Check hover state continuously
    //   renderer.render(scene, camera);
    // }
    // animate();

    // Option B: Check only on click
    // function onClick(event) {
    //    // Update pointer coordinates based on click event (optional, if not using pointermove)
    //    // onPointerMove(event);
    //    checkIntersections(); // Check intersections at the click moment
    //    if (intersectedObject) {
    //        console.log(`Clicked on ${intersectedObject.name || intersectedObject.uuid}!`);
    //        // Perform action based on the clicked object
    //    }
    // }
    // renderer.domElement.addEventListener('click', onClick);
    ```

## Key Components

*   **`THREE.Raycaster`:**
    *   `setFromCamera(coords: Vector2, camera: Camera)`: Updates the ray.
    *   `intersectObject(object: Object3D, recursive?: boolean)`: Checks a single object.
    *   `intersectObjects(objects: Object3D[], recursive?: boolean)`: Checks an array of objects. Returns sorted array of intersections.
    *   `layers`: Can be used to filter intersections based on object layers. `raycaster.layers.set(layerNumber);`. Objects must also be assigned to layers: `object.layers.enable(layerNumber);`.
    *   `far`: Maximum distance for intersections.
*   **Intersection Object:** Contains info about an intersection:
    *   `distance`: Distance from the ray's origin to the intersection point.
    *   `point`: `Vector3` of the intersection point in world space.
    *   `object`: The intersected `Object3D`.
    *   `face`: Intersected face (`Face3` object - less common with `BufferGeometry`).
    *   `faceIndex`: Index of the intersected face in the geometry.
    *   `uv`: `Vector2` UV coordinates at the intersection point (if geometry has UVs).
    *   `instanceId`: If intersecting an `InstancedMesh`, the ID of the specific instance hit.

## Considerations

*   **Performance:** Calling `intersectObjects` on every frame (for hover) can be expensive if checking many objects or complex geometries.
    *   **Limit Target Objects:** Pass only potentially interactive objects to `intersectObjects`, not the entire scene if possible. Maintain a separate array or group for interactive elements.
    *   **Throttling/Debouncing:** For hover effects, consider checking intersections less frequently (e.g., using `setTimeout` or a throttling library) if performance suffers.
*   **Coordinate Conversion:** Correctly converting screen coordinates to NDC (-1 to +1) is crucial. Use `getBoundingClientRect()` for accuracy.
*   **Event Listeners:** Attach listeners to `renderer.domElement`. Remember to remove listeners on cleanup (`removeEventListener`).
*   **Controls Interference:** Camera controls like `OrbitControls` might interfere with click/drag events needed for raycasting interactions. Check controls documentation for event handling or methods like `.enabled = false` to temporarily disable them if needed.
*   **InstancedMesh:** Raycasting works with `InstancedMesh`, returning the `instanceId` in the intersection object, allowing interaction with individual instances.
*   **Visibility:** Raycaster respects the `.visible` property of objects. Invisible objects are ignored.