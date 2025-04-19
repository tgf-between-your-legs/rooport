# Three.js: Interaction with Raycasting

Detecting mouse clicks or hovers on 3D objects using `THREE.Raycaster`.

## Core Concept

Raycasting involves projecting a ray (a straight line) from the camera's position through the mouse cursor's position on the screen into the 3D scene. You can then check which objects in the scene intersect with this ray.

## Implementation Steps

1.  **Store Mouse Coordinates:** Listen for mouse events (e.g., `mousemove`, `click`) on the renderer's DOM element. Convert the screen coordinates (pixels) to normalized device coordinates (NDC), which range from -1 to +1 for both X and Y.
    ```javascript
    const mouse = new THREE.Vector2(); // Reusable vector for NDC

    function onPointerMove( event ) {
        // Calculate pointer position in normalized device coordinates (-1 to +1)
        // event.clientX/clientY are pixel coordinates from top-left
        // renderer.domElement.getBoundingClientRect() helps account for canvas position/size
        const rect = renderer.domElement.getBoundingClientRect();
        mouse.x = ( ( event.clientX - rect.left ) / rect.width ) * 2 - 1;
        mouse.y = - ( ( event.clientY - rect.top ) / rect.height ) * 2 + 1; // Y is inverted
    }
    window.addEventListener( 'pointermove', onPointerMove );
    // Add similar listener for 'click' or 'pointerdown'
    ```

2.  **Create `Raycaster`:** Instantiate `THREE.Raycaster`.
    ```javascript
    const raycaster = new THREE.Raycaster();
    ```

3.  **Update Raycaster:** Inside your event handler (e.g., `onClick`) or animation loop (for hover effects), update the raycaster with the camera and the normalized mouse coordinates.
    ```javascript
    function checkIntersections() {
      // Update the picking ray with the camera and pointer position
      raycaster.setFromCamera( mouse, camera ); // camera is your THREE.Camera

      // Calculate objects intersecting the picking ray
      // scene.children should contain the objects you want to check
      // Set recursive to true if you want to check children of groups
      const intersects = raycaster.intersectObjects( scene.children, true );

      // 'intersects' is an array of objects, sorted by distance (closest first)
      if (intersects.length > 0) {
        // intersects[0].object is the closest intersected object
        console.log('Intersected:', intersects[0].object.name || intersects[0].object.uuid);
        // You can change material, trigger actions, etc.
        // Example: Highlight intersected object
        // if (intersectedObject !== intersects[0].object) {
        //    if (intersectedObject) intersectedObject.material.emissive.setHex(0x000000); // Reset previous
        //    intersectedObject = intersects[0].object;
        //    intersectedObject.material.emissive.setHex(0xff0000); // Highlight current
        // }
      } else {
        // No intersection
        // Example: Reset highlight if mouse moved off
        // if (intersectedObject) intersectedObject.material.emissive.setHex(0x000000);
        // intersectedObject = null;
      }
    }

    // Call checkIntersections() in your click handler or render loop
    // function onClick(event) {
    //    onPointerMove(event); // Update mouse coords first
    //    checkIntersections();
    //    // Perform action based on intersects[0].object if needed
    // }
    // window.addEventListener('click', onClick);

    // Or in animation loop for hover:
    // function animate() {
    //   requestAnimationFrame(animate);
    //   checkIntersections(); // Check on every frame for hover
    //   renderer.render(scene, camera);
    // }
    ```

## Key Components

*   **`THREE.Raycaster`:** The core object for raycasting.
    *   `setFromCamera(coords: Vector2, camera: Camera)`: Updates the ray based on normalized mouse coordinates and the camera.
    *   `intersectObject(object: Object3D, recursive?: boolean)`: Checks intersection with a single object (and optionally its children).
    *   `intersectObjects(objects: Object3D[], recursive?: boolean)`: Checks intersection with an array of objects. Returns an array of intersection objects, sorted by distance.
*   **Intersection Object:** Contains information about an intersection:
    *   `distance`: Distance from the camera's origin to the intersection point.
    *   `point`: `Vector3` representing the intersection point in world space.
    *   `object`: The intersected `Object3D`.
    *   `face`: The intersected face (`Face3` object - less common with `BufferGeometry`).
    *   `faceIndex`: Index of the intersected face.
    *   `uv`: `Vector2` representing the UV coordinates at the intersection point.

## Considerations

*   **Performance:** Calling `intersectObjects` on every frame (for hover) can be expensive if you have many objects or complex geometries.
    *   Limit the array of objects passed to `intersectObjects` to only those that are interactive.
    *   Consider throttling or debouncing hover checks if performance suffers.
*   **Coordinate Conversion:** Correctly converting screen coordinates to NDC (-1 to +1) is crucial and depends on your canvas setup and CSS.
*   **Object Selection:** Ensure the objects you want to interact with are included in the array passed to `intersectObjects`. If objects are nested within `Group`s, set the `recursive` flag to `true`.
*   **Event Listeners:** Attach event listeners to the `renderer.domElement` for better accuracy, especially if the canvas doesn't fill the whole window. Remember to remove listeners on cleanup.
*   **Controls:** If using camera controls like `OrbitControls`, they might interfere with click/drag events. Check the controls' documentation for event handling or disabling options if needed.

*(Refer to the official Three.js Raycaster documentation: https://threejs.org/docs/#api/en/core/Raycaster)*