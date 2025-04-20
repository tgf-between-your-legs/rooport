# Three.js: Animation Mixer

Playing animations embedded within 3D models (like glTF).

## Core Concept: Playing Predefined Animations

Many 3D models, especially those in glTF format, come with embedded animation data (e.g., skeletal animations for characters, transform animations for objects). Three.js provides the `AnimationMixer` system to play, blend, and control these animations.

**Key Components:**

*   **`gltf.animations`:** When a glTF model is loaded using `GLTFLoader`, the `gltf` object contains an `animations` array holding `THREE.AnimationClip` objects. Each `AnimationClip` represents a distinct animation sequence (e.g., "walk", "run", "idle").
*   **`THREE.AnimationMixer`:** The central player for animations on a specific object. You create one mixer instance per animated object (usually the root `gltf.scene` or a specific skeleton).
*   **`THREE.AnimationClip`:** Contains the keyframe data for an animation (times, values for properties like position, rotation, scale, or morph targets).
*   **`THREE.AnimationAction`:** Represents an active, scheduled animation created from an `AnimationClip` via the mixer. You control playback (`play()`, `stop()`, `reset()`), looping (`setLoop()`), time scale (`setEffectiveTimeScale()`), weight (`setEffectiveWeight()`), etc., through the action.
*   **`THREE.Clock`:** A helper object to track time elapsed, essential for updating the `AnimationMixer` in the render loop.

## Implementation Steps

1.  **Load Model with Animations:** Load your glTF model using `GLTFLoader`. Ensure the model actually contains animations (check `gltf.animations` array).

2.  **Create Clock and Mixer:** Instantiate `THREE.Clock` and `THREE.AnimationMixer`, associating the mixer with the object you want to animate (usually `gltf.scene`).

    ```javascript
    import * as THREE from 'three';
    import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

    const clock = new THREE.Clock();
    let mixer: THREE.AnimationMixer | null = null; // Variable to hold the mixer

    const gltfLoader = new GLTFLoader();
    gltfLoader.load('/models/animated-character.glb', (gltf) => {
        const model = gltf.scene;
        scene.add(model);

        // Check if animations exist
        if (gltf.animations && gltf.animations.length) {
            // Create a mixer for the model's scene graph
            mixer = new THREE.AnimationMixer(model);
            console.log('Animations found:', gltf.animations);

            // --- Step 3: Create and Play Actions ---
            // Example: Play the first animation found
            const action = mixer.clipAction(gltf.animations[0]);
            action.play();

            // Example: Find and play a specific animation by name
            // const walkClip = THREE.AnimationClip.findByName(gltf.animations, 'Walk');
            // if (walkClip) {
            //     const walkAction = mixer.clipAction(walkClip);
            //     walkAction.play();
            // }

            // Example: Play all animations (might look weird without blending)
            // gltf.animations.forEach((clip) => {
            //     mixer?.clipAction(clip).play();
            // });
        } else {
            console.log('No animations found in the model.');
        }
    });
    ```

3.  **Create Animation Actions:** Use `mixer.clipAction(animationClip)` to create an `AnimationAction` for each animation you want to control.

4.  **Control Actions:** Use methods on the `AnimationAction` instance:
    *   `.play()`: Starts the animation.
    *   `.stop()`: Stops the animation, preserving its current state.
    *   `.reset()`: Resets the animation to its initial state.
    *   `.fadeIn(duration)` / `.fadeOut(duration)`: Smoothly blend animations in or out.
    *   `.crossFadeTo(otherAction, duration, warp)`: Smoothly transition from this action to another.
    *   `.setLoop(loopMode, repetitions)`: Control looping (`THREE.LoopOnce`, `THREE.LoopRepeat`, `THREE.LoopPingPong`).
    *   `.setEffectiveTimeScale(scale)`: Control playback speed (1 = normal, 0.5 = half speed, -1 = reverse).
    *   `.setEffectiveWeight(weight)`: Control the influence of this animation when blending multiple actions (0 = no influence, 1 = full influence).
    *   `.paused`: Boolean property to pause/resume.

5.  **Update Mixer in Render Loop:** In your `animate` function (render loop), get the time delta from the `THREE.Clock` and update the mixer using `mixer.update(deltaTime)`. This advances the animations.

    ```javascript
    // --- Render Loop ---
    function animate() {
        const deltaTime = clock.getDelta(); // Get time elapsed since last frame

        // Update the mixer if it exists
        if (mixer) {
            mixer.update(deltaTime);
        }

        // ... update controls, other logic ...

        renderer.render(scene, camera);
        requestAnimationFrame(animate);
    }

    animate(); // Start loop
    ```

The `AnimationMixer` system is the standard way to handle pre-defined animations within Three.js, especially those loaded from glTF files. Remember to create a mixer, get clips from the loaded `gltf.animations`, create actions using `mixer.clipAction()`, control playback via the action methods, and crucially, update the mixer in your render loop with the time delta.

*(Refer to the official Three.js documentation on Animation System / AnimationMixer, AnimationClip, AnimationAction.)*