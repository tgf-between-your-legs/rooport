# jQuery: Effects & Animations

Using jQuery's built-in methods for common visual effects and custom animations.

## Core Concept

jQuery provides simple methods to add visual effects like showing, hiding, fading, and sliding elements, as well as a `.animate()` method for creating custom animations on CSS properties.

## Basic Effects

These methods change the `display` property (or `opacity` for fades) and often involve animation.

*   **`.show([duration], [easing], [completeCallback])`:** Displays the selected element(s). Restores the original `display` value (e.g., `block`, `inline`).
*   **`.hide([duration], [easing], [completeCallback])`:** Hides the selected element(s) (`display: none`).
*   **`.toggle([duration], [easing], [completeCallback])`:** Toggles between showing and hiding.
*   **`.fadeIn([duration], [easing], [completeCallback])`:** Fades in the element(s) by animating opacity from 0 to 1.
*   **`.fadeOut([duration], [easing], [completeCallback])`:** Fades out the element(s) by animating opacity from 1 to 0, then sets `display: none`.
*   **`.fadeToggle([duration], [easing], [completeCallback])`:** Toggles between fading in and out.
*   **`.fadeTo(duration, opacity, [easing], [completeCallback])`:** Fades to a specific `opacity` value (0 to 1). Does *not* change `display`.
*   **`.slideDown([duration], [easing], [completeCallback])`:** Slides the element(s) down into view by animating height.
*   **`.slideUp([duration], [easing], [completeCallback])`:** Slides the element(s) up out of view by animating height, then sets `display: none`.
*   **`.slideToggle([duration], [easing], [completeCallback])`:** Toggles between sliding up and down.

**Parameters:**

*   `duration` (Optional): Animation speed in milliseconds (e.g., `400`) or keywords (`'slow'`, `'fast'`). Defaults to `400`.
*   `easing` (Optional): Specifies the animation's acceleration curve. Defaults to `'swing'`. `'linear'` is also built-in. Requires jQuery UI or plugins for more easing options.
*   `completeCallback` (Optional): A function to execute once the animation completes for each element.

```javascript
$(function() {
  $('#showBtn').on('click', function() {
    $('#myElement').show('fast'); // Show quickly
  });

  $('#hideBtn').on('click', function() {
    $('#myElement').hide(1000); // Hide over 1 second
  });

  $('#toggleBtn').on('click', function() {
    $('#myElement').slideToggle('slow', function() {
      // Callback after animation completes
      console.log('Slide toggle finished!');
    });
  });

  $('#fadeBtn').on('click', function() {
    $('#anotherElement').fadeToggle();
  });
});
```

## Custom Animations (`.animate()`)

*   **Purpose:** Create custom animations by animating specific numeric CSS properties.
*   **Syntax:** `.animate(properties, [duration], [easing], [completeCallback])`
*   **`properties`:** An object containing the target CSS properties and their final numeric values.
    *   Use camelCase for CSS properties (e.g., `marginLeft`, `fontSize`).
    *   Values should generally be numeric (or use `+=`/`-=` for relative changes). Non-numeric properties (like `color`) usually require jQuery UI or plugins.
    *   Can animate properties like `opacity`, `height`, `width`, `top`, `left`, `fontSize`, `margin*`, `padding*`.

```javascript
$(function() {
  $('#animateBtn').on('click', function() {
    $('#box')
      .animate({
        opacity: 0.5,       // Target opacity
        marginLeft: '+=50px', // Move right by 50px
        height: 'toggle'    // Special value: animates height to/from 0
      }, 1000, 'linear', function() {
        // Animation complete
        console.log('Box animation finished.');
      })
      .animate({ // Chain another animation
        width: '50px'
      }, 'fast');
  });
});
```

## Animation Queue & Control

*   jQuery maintains an animation queue (`fx`) for each element. Animations chained on the same element run sequentially by default.
*   **`.stop([clearQueue], [jumpToEnd])`:** Stops the currently running animation on the selected elements.
    *   `clearQueue` (boolean, default `false`): If `true`, removes remaining animations from the queue.
    *   `jumpToEnd` (boolean, default `false`): If `true`, immediately completes the current animation to its end state.
*   **`.delay(duration)`:** Adds a delay (in milliseconds) to the animation queue.

```javascript
$('#myElement')
  .slideUp(500)
  .delay(200) // Wait 200ms
  .slideDown(500);

$('#stopBtn').on('click', function() {
  $('#myElement').stop(true, true); // Clear queue and jump to end of current animation
});
```

jQuery effects provide a simple way to add basic animations. While CSS transitions and animations are often preferred for performance today, jQuery's `.animate()` and effects methods remain useful, especially in older codebases or for complex chained animations controlled via JavaScript logic.