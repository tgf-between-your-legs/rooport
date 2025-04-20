# anime.js: Core API Basics

Fundamental concepts for creating animations with the `anime()` function.

## Core Concept: `anime(parameters)`

The main function `anime()` creates an animation instance. It takes a single object containing parameters that define the animation's targets, properties, timing, and behavior.

```javascript
import anime from 'animejs/lib/anime.es.js'; // Import ES module

// Basic animation
anime({
  targets: '.css-selector', // Target element(s)
  translateX: 250, // Property to animate (CSS transform)
  rotate: '1turn', // Another property
  backgroundColor: '#FFF', // CSS background color
  duration: 800, // Duration in milliseconds
  easing: 'easeInOutQuad', // Easing function
  loop: true, // Loop the animation
  direction: 'alternate' // Alternate direction on each loop
});
```

## 1. Targets

Specifies the element(s) or object(s) to animate.

*   **CSS Selectors:** (Most common for DOM)
    *   `targets: '.my-class'`
    *   `targets: '#element-id'`
    *   `targets: 'div, .box, #specific'` (Multiple selectors)
*   **DOM Node / NodeList:**
    *   `targets: document.querySelector('.my-element')`
    *   `targets: document.querySelectorAll('.multiple-elements')`
*   **JavaScript Object:** Animate properties of a plain JS object. Useful for driving other logic or custom rendering (e.g., Canvas).
    *   `let myObj = { progress: 0, value: 10 };`
    *   `anime({ targets: myObj, progress: 100, value: 50, update: () => console.log(myObj.progress) });`
*   **Array:** An array of DOM nodes or JS objects.
    *   `targets: [el1, el2, document.querySelector('#el3')]`

## 2. Properties

Specifies the CSS properties, transforms, SVG attributes, or Object properties to animate.

*   **CSS Properties:** (Use camelCase) `backgroundColor`, `opacity`, `color`, `fontSize`, `borderRadius`, etc.
    *   `opacity: 0.5`
    *   `backgroundColor: '#FF0000'`
*   **CSS Transforms:** `translateX`, `translateY`, `rotate`, `scale`, `scaleX`, `scaleY`, `skewX`, `skewY`.
    *   `translateX: 250` (Defaults to `px`, can use other units: `'50%'`, `'3em'`)
    *   `rotate: '1turn'` (Units: `deg`, `rad`, `turn`)
    *   `scale: 1.5`
*   **SVG Attributes:** Animate attributes of SVG elements (`<circle>`, `<path>`, etc.).
    *   `targets: 'circle', r: 50, fill: '#F00'`
    *   `targets: 'path', d: [{ value: 'M...'}, { value: 'M...' }]` (For path morphing - see `animejs-svg-morphing.md`)
*   **Object Properties:** Animate numeric properties of plain JS objects.
    *   `targets: myObj, value: 100`

## 3. Property Parameters (Defining Values)

How to specify the start, end, and intermediate values for properties.

*   **Specific End Value:** The animation starts from the element's current value and animates *to* the specified value.
    *   `translateX: 250`
*   **From/To Values:** Specify both start and end values using an array `[startValue, endValue]`.
    *   `translateX: [0, 250]` (Start at 0, end at 250)
    *   `opacity: [1, 0]` (Fade out)
*   **Relative Values:** Animate *relative* to the current value.
    *   `translateX: '+=250'` (Move 250px further from current position)
    *   `rotate: '-=15deg'` (Rotate 15 degrees less)
*   **Function-Based Values:** Calculate the value dynamically per target element. The function receives `(targetElement, index, totalTargets)` as arguments.
    *   `translateX: (el, i) => 50 + (i * 100)` (Position elements based on their index)
    *   `delay: anime.stagger(100)` (See Staggering)
*   **Keyframes:** Define multiple steps within a single animation property.
    *   ```javascript
        translateX: [
          { value: 100, duration: 500, easing: 'easeOutSine' },
          { value: 0, duration: 800, delay: 200, easing: 'easeInOutQuad' }
        ]
        ```

## 4. Animation Parameters (Controlling Behavior)

*   **`duration`:** Duration in milliseconds (e.g., `1000`). Can be function-based.
*   **`delay`:** Delay before the animation starts in milliseconds (e.g., `500`). Can be function-based or use `anime.stagger()`.
*   **`endDelay`:** Delay *after* the animation finishes before completing (useful in timelines).
*   **`easing`:** Specifies the acceleration curve. Many built-in options (`'linear'`, `'easeInQuad'`, `'easeInOutExpo'`, `'spring(1, 80, 10, 0)'`, etc.). See anime.js easing visualizer.
*   **`round`:** Round animated values to a specific decimal place (e.g., `1` for 1 decimal place).
*   **`direction`:** `'normal'` (default), `'reverse'`, `'alternate'`.
*   **`loop`:** `true` (infinite), a number (loop count), `false` (default).
*   **`autoplay`:** `true` (default) or `false`. If false, need to use animation controls (`.play()`).

## 5. Callbacks & Controls

*   **Callbacks:** Functions executed at different points in the animation lifecycle.
    *   `update(anim)`: Called on every frame while the animation is running. `anim` contains animation instance details.
    *   `begin(anim)`: Called when the animation begins.
    *   `complete(anim)`: Called when the animation completes.
    *   `loopBegin(anim)`, `loopComplete(anim)`: Called at the start/end of each loop iteration.
    *   `change(anim)`: Called at the start of `autoplay` or `.play()`.
    *   `changeBegin(anim)`, `changeComplete(anim)`: Called when `autoplay` starts or `.play()`/`.pause()`/etc. are called.
*   **Controls:** Methods on the animation instance returned by `anime()`.
    *   `play()`: Starts playback.
    *   `pause()`: Pauses playback.
    *   `restart()`: Restarts the animation from the beginning.
    *   `reverse()`: Reverses the animation direction.
    *   `seek(time)`: Jump to a specific time (in ms) or percentage.
    *   `remove(targets)`: Remove specific targets from the animation.

```javascript
const animation = anime({
  targets: '.box',
  translateX: 200,
  autoplay: false, // Don't start immediately
  duration: 1000,
  update: (anim) => {
    console.log('Progress:', anim.progress); // Log progress (0-100)
  },
  complete: () => {
    console.log('Animation finished!');
  }
});

document.querySelector('#playButton').onclick = animation.play;
document.querySelector('#pauseButton').onclick = animation.pause;
```

This covers the fundamentals of creating single animations. Use timelines (`anime.timeline()`) for sequencing multiple animations.

*(Refer to the official anime.js documentation for Targets, Properties, Parameters, etc.)*