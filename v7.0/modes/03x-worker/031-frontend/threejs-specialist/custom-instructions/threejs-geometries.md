# Three.js: Geometries

Defining the shape and structure of 3D objects in Three.js.

## Core Concept: Geometry Defines Shape

In Three.js, **Geometry** defines the shape of a 3D object. It essentially holds data about the object's vertices (points in 3D space) and how they connect to form faces (triangles).

**Key Classes:**

*   **Built-in Geometries:** Three.js provides constructors for common shapes:
    *   `THREE.BoxGeometry(width, height, depth, ...)`
    *   `THREE.SphereGeometry(radius, widthSegments, heightSegments, ...)`
    *   `THREE.PlaneGeometry(width, height, ...)`
    *   `THREE.CylinderGeometry(...)`
    *   `THREE.ConeGeometry(...)`
    *   `THREE.TorusGeometry(...)`
    *   `THREE.TorusKnotGeometry(...)`
    *   ...and many others. These are convenient for basic shapes.
*   **`THREE.BufferGeometry`:**
    *   The **modern and preferred** way to represent geometry. All built-in geometries are ultimately converted to `BufferGeometry`.
    *   Stores geometry data (vertex positions, normals, UVs, colors, etc.) efficiently in typed arrays (`Float32Array`, `Uint16Array`, etc.) called **BufferAttributes**.
    *   **Use Cases:** Creating custom shapes, loading complex models (glTF loaders produce BufferGeometry), optimizing performance.

## Using Built-in Geometries

Instantiate the desired geometry class and pass it to a `Mesh` along with a `Material`.

```javascript
import * as THREE from 'three';

// Create a standard material
const material = new THREE.MeshStandardMaterial({ color: 0xff0000, roughness: 0.5 });

// --- Box ---
const boxGeometry = new THREE.BoxGeometry(1, 1, 1); // Width, Height, Depth
const cube = new THREE.Mesh(boxGeometry, material);
cube.position.x = -2;
// scene.add(cube);

// --- Sphere ---
// SphereGeometry(radius, widthSegments, heightSegments)
const sphereGeometry = new THREE.SphereGeometry(0.7, 32, 16);
const sphere = new THREE.Mesh(sphereGeometry, material);
sphere.position.x = 0;
// scene.add(sphere);

// --- Plane ---
const planeGeometry = new THREE.PlaneGeometry(10, 10);
const planeMaterial = new THREE.MeshStandardMaterial({ color: 0xcccccc, side: THREE.DoubleSide }); // Use DoubleSide for planes
const plane = new THREE.Mesh(planeGeometry, planeMaterial);
plane.rotation.x = -Math.PI / 2; // Rotate to be horizontal
plane.position.y = -1;
plane.receiveShadow = true; // Allow plane to receive shadows
// scene.add(plane);
```

## Using `BufferGeometry` (Custom Triangle)

Creating custom geometry involves defining `BufferAttribute`s for vertex positions and potentially other data like normals (for lighting) and UVs (for textures).

```javascript
import * as THREE from 'three';

// 1. Create an empty BufferGeometry
const customGeometry = new THREE.BufferGeometry();

// 2. Define vertices (x, y, z for each vertex)
const vertices = new Float32Array([
	-1.0, -1.0,  0.0, // Vertex 0 (bottom left)
	 1.0, -1.0,  0.0, // Vertex 1 (bottom right)
	 1.0,  1.0,  0.0, // Vertex 2 (top right)

    // Add another triangle if needed (e.g., for a quad)
    // -1.0, -1.0,  0.0, // Vertex 0
    //  1.0,  1.0,  0.0, // Vertex 2
    // -1.0,  1.0,  0.0  // Vertex 3 (top left)
]);

// 3. Create a BufferAttribute and add it to the geometry
// 'position' is the standard attribute name for vertex positions
// 3 indicates each vertex position is composed of 3 values (x, y, z)
customGeometry.setAttribute('position', new THREE.BufferAttribute(vertices, 3));

// Optional: Define UV coordinates (for textures)
// const uvs = new Float32Array([
//    0.0, 0.0, // UV for Vertex 0
//    1.0, 0.0, // UV for Vertex 1
//    1.0, 1.0, // UV for Vertex 2
// ]);
// customGeometry.setAttribute('uv', new THREE.BufferAttribute(uvs, 2)); // 2 values per UV (u, v)

// Optional: Define vertex normals (for lighting)
// If not provided, Three.js can compute flat normals
// customGeometry.computeVertexNormals(); // Calculate normals automatically

// Optional: Define indices (if reusing vertices)
// const indices = [ 0, 1, 2 ]; // Defines one triangle using vertices 0, 1, 2
// customGeometry.setIndex(indices);

// 4. Create a Mesh
const customMaterial = new THREE.MeshBasicMaterial({ color: 0x0000ff, side: THREE.DoubleSide });
const customMesh = new THREE.Mesh(customGeometry, customMaterial);
customMesh.position.x = 2;
// scene.add(customMesh);
```

**Key `BufferGeometry` Attributes:**

*   `position`: (Required) `Float32Array` of vertex coordinates (x, y, z). Item size is 3.
*   `normal`: `Float32Array` of vertex normal vectors (x, y, z) for lighting calculations. Item size is 3. Can be computed via `computeVertexNormals()`.
*   `uv`: `Float32Array` of UV texture coordinates (u, v). Item size is 2. Used for mapping textures.
*   `color`: `Float32Array` of vertex colors (r, g, b). Item size is 3. Requires `vertexColors: true` on the material.
*   `index`: (Optional) `Uint16Array` or `Uint32Array` defining the order in which vertices are used to form triangles. Allows reusing vertices for efficiency.

Geometries define the structure, while Materials define the appearance. Use built-in geometries for common shapes and `BufferGeometry` for custom shapes or loaded models. Remember to dispose of geometries when they are no longer needed (`geometry.dispose()`).

*(Refer to the official Three.js documentation on Geometries and BufferGeometry.)*