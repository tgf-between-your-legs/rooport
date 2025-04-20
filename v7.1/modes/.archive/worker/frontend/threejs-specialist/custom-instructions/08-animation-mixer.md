# Animation Mixer

Playing animations embedded within 3D models (like glTF).

## Core Concept: Playing Predefined Animations

Many 3D models, especially those in glTF format, come with embedded animation data (e.g., skeletal animations for characters, transform animations for objects). Three.js provides the `AnimationMixer` system to play, blend, and control these animations.

**Key Components:**

*   **`gltf.animations`:** When a glTF model is loaded using `GLTFLoader`, the `gltf` object contains an `animations` array holding `THREE.AnimationClip` objects. Each `AnimationClip` represents a distinct animation sequence (e.g., "walk", "run", "idle").
*   **`THREE.AnimationMixer`:** The central player for animations on a specific object. You create one mixer instance per animated object (usually the root `gltf.scene` or a specific skeleton/mesh).
*   **`THREE.AnimationClip`:** Contains the keyframe data for an animation (times, values for properties like position, rotation, scale, or morph targets).
*   **`THREE.AnimationAction`:** Represents an active, scheduled animation created from an `AnimationClip` via the mixer. You control playback (`play()`, `stop()`, `reset()`), looping (`setLoop()`), time scale (`setEffectiveTimeScale()`), weight (`setEffectiveWeight()`), etc., through the action.
*   **`THREE.Clock`:** A helper object to track time elapsed, essential for updating the `AnimationMixer` in the render loop.

## Implementation Steps

1.  **Load Model with Animations:** Load your glTF model using `GLTFLoader`. Ensure the model actually contains animations (check `gltf.animations` array after loading).

2.  **Create Clock and Mixer:** Instantiate `THREE.Clock` and `THREE.AnimationMixer`, associating the mixer with the object you want to animate (usually `gltf.scene`). Store the mixer and actions in accessible variables.

    ```javascript
    import * as THREE from 'three';
    import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

    const clock = new THREE.Clock();
    let mixer: THREE.AnimationMixer | null = null; // Variable to hold the mixer
    const actions: { [name: string]: THREE.AnimationAction } = {}; // Store actions by name

    const gltfLoader = new GLTFLoader();
    gltfLoader.load('/models/animated-character.glb', (gltf) => {
        const model = gltf.scene;
        scene.add(model);

        // Check if animations exist
        if (gltf.animations && gltf.animations.length) {
            // Create a mixer for the model's scene graph
            mixer = new THREE.AnimationMixer(model);
            console.log('Animations found:', gltf.animations.map(clip => clip.name));

            // --- Step 3: Create Actions ---
            gltf.animations.forEach((clip) => {
                const action = mixer.clipAction(clip);
                actions[clip.name] = action; // Store action by name

                // Optional: Configure default settings (e.g., prevent clampWhenFinished)
                // action.clampWhenFinished = false;
                // action.setLoop(THREE.LoopRepeat);
            });

            // --- Step 4: Play Initial Action ---
            // Example: Play the 'Idle' animation if it exists
            if (actions['Idle']) {
                actions['Idle'].play();
            } else if (gltf.animations.length > 0) {
                // Fallback: play the first animation found
                mixer.clipAction(gltf.animations[0]).play();
            }

        } else {
            console.log('No animations found in the model.');
        }
    });
    ```

3.  **Create Animation Actions:** Use `mixer.clipAction(animationClip)` to create an `AnimationAction` for each animation you want to control. Store these actions (e.g., in an object keyed by animation name) for easy access later.

4.  **Control Actions:** Use methods on the `AnimationAction` instance to manage playback:
    *   `.play()`: Starts the animation (resumes if paused).
    *   `.stop()`: Stops the animation and resets its time to the beginning.
    *   `.reset()`: Resets the action state (stops, removes fading, sets time to 0).
    *   `.fadeIn(duration)`: Smoothly increases the action's weight to 1 over `duration` seconds and plays it.
    *   `.fadeOut(duration)`: Smoothly decreases the action's weight to 0 over `duration` seconds. Often paired with `.stop()` in a timeout or via the mixer's `finished` event if you want it to stop completely after fading.
    *   `.crossFadeTo(otherAction, duration, warp)`: Smoothly fades this action out while fading `otherAction` in over `duration` seconds. `warp` (boolean) synchronizes the animations if true.
    *   `.setLoop(loopMode, repetitions)`: Control looping (`THREE.LoopOnce`, `THREE.LoopRepeat` (default), `THREE.LoopPingPong`). `repetitions` is the number of repeats (Infinity for `LoopRepeat`).
    *   `.setEffectiveTimeScale(scale)`: Control playback speed (1 = normal, 0.5 = half speed, -1 = reverse).
    *   `.setEffectiveWeight(weight)`: Control the influence of this animation when blending multiple actions (0 = no influence, 1 = full influence). Used for manual blending.
    *   `.paused`: Boolean property to pause/resume without resetting time.
    *   `.time`: Current playback time of the action.
    *   `.clampWhenFinished`: Boolean. If true, the animation state stays at the last frame when finished (useful for `LoopOnce`). Default is `false`.

5.  **Update Mixer in Render Loop:** In your `animate` function (render loop), get the time delta from the `THREE.Clock` and update the mixer using `mixer.update(deltaTime)`. This advances the animations based on the elapsed time.

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

**Example: Switching Animations with Crossfade**

```javascript
function playAnimation(name: string) {
    const newAction = actions[name];
    if (!newAction) {
        console.warn(`Animation "${name}" not found.`);
        return;
    }

    // Find currently active action (simplified - assumes only one active)
    let oldAction: THREE.AnimationAction | null = null;
    for (const actionName in actions) {
        if (actions[actionName].isRunning()) {
            oldAction = actions[actionName];
            break;
        }
    }

    if (oldAction === newAction) return; // Already playing

    newAction.reset(); // Reset the new action
    if (oldAction) {
        newAction.crossFadeFrom(oldAction, 0.3, true); // Fade from old to new in 0.3s
    }
    newAction.play();
}

// Call this function when you want to switch, e.g., on button click
// playAnimation('Walk');
// playAnimation('Run');
```

The `AnimationMixer` system is the standard way to handle pre-defined animations within Three.js. Remember to create a mixer, get clips from `gltf.animations`, create actions using `mixer.clipAction()`, control playback via the action methods (especially `crossFadeFrom` or `fadeIn`/`fadeOut` for smooth transitions), and crucially, update the mixer in your render loop with the time delta.