# anime.js: Framework Integration (React, Vue, Angular)

Patterns for using anime.js within popular JavaScript frameworks/libraries.

## Core Concept: Lifecycle Hooks & Refs

Integrating anime.js typically involves:

1.  **Getting References:** Obtaining a reference to the DOM element(s) you want to animate using the framework's mechanism (e.g., `useRef` in React, `ref` in Vue, `ElementRef` or template reference variables in Angular).
2.  **Initializing Animation:** Creating the `anime()` instance or timeline within an appropriate lifecycle hook that runs *after* the target DOM elements have been rendered (e.g., `useEffect` in React, `onMounted` in Vue, `ngAfterViewInit` in Angular).
3.  **Cleanup:** Destroying or pausing animations when the component unmounts or is destroyed to prevent memory leaks or errors (e.g., in the `useEffect` cleanup function, `onUnmounted`, `ngOnDestroy`).

## 1. React Integration (`useEffect`, `useRef`)

```jsx
import React, { useRef, useEffect } from 'react';
import anime from 'animejs/lib/anime.es.js';

function AnimatedBox() {
  const boxRef = useRef(null); // Create a ref to hold the DOM element
  const animationRef = useRef(null); // Ref to hold the anime instance for cleanup

  useEffect(() => {
    // Animation setup runs after component mounts
    if (boxRef.current) {
      animationRef.current = anime({
        targets: boxRef.current, // Use the ref's current value
        translateX: 250,
        rotate: '1turn',
        backgroundColor: '#FFF',
        duration: 800,
        loop: true,
        direction: 'alternate',
        easing: 'easeInOutQuad'
        // autoplay: false // Consider controlling playback manually
      });
    }

    // Cleanup function: runs when component unmounts
    return () => {
      if (animationRef.current) {
        // Option 1: Remove targets (if animation might be reused elsewhere)
        // anime.remove(boxRef.current);

        // Option 2: Pause the animation instance (safer if instance is specific to this component)
        animationRef.current.pause();
        animationRef.current = null; // Clear the ref
        console.log('Animation paused and cleaned up');
      }
    };
  }, []); // Empty dependency array ensures this runs only once on mount/unmount

  return <div className="box" ref={boxRef}></div>;
}

export default AnimatedBox;
```

## 2. Vue Integration (`onMounted`, `onUnmounted`, `ref`)

```vue
<template>
  <div class="box" ref="boxElement"></div> <!-- Template ref -->
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import anime from 'animejs/lib/anime.es.js';

const boxElement = ref(null); // Create a template ref
let animationInstance = null; // Variable to hold the anime instance

onMounted(() => {
  // Code runs after component is mounted and element is available
  if (boxElement.value) {
    animationInstance = anime({
      targets: boxElement.value, // Access element via .value
      translateX: 250,
      rotate: '1turn',
      backgroundColor: '#FFF',
      duration: 800,
      loop: true,
      direction: 'alternate',
      easing: 'easeInOutQuad'
    });
  }
});

onUnmounted(() => {
  // Cleanup when component is destroyed
  if (animationInstance) {
    // anime.remove(boxElement.value); // Option 1
    animationInstance.pause(); // Option 2
    animationInstance = null;
    console.log('Animation paused and cleaned up');
  }
});
</script>

<style scoped>
.box { /* Basic styling */
  width: 50px;
  height: 50px;
  background-color: blue;
}
</style>
```

## 3. Angular Integration (`AfterViewInit`, `OnDestroy`, `ElementRef`, `ViewChild`)

```typescript
import { Component, ElementRef, ViewChild, AfterViewInit, OnDestroy, inject } from '@angular/core';
import anime, { AnimeInstance } from 'animejs/lib/anime.es.js'; // Import AnimeInstance type if needed

@Component({
  selector: 'app-animated-div',
  standalone: true,
  template: `<div class="box" #animatedBox></div>`, // Template reference variable #animatedBox
  styles: [`.box { width: 50px; height: 50px; background-color: green; }`]
})
export class AnimatedDivComponent implements AfterViewInit, OnDestroy {
  // Access element using @ViewChild with the template reference variable
  @ViewChild('animatedBox') boxRef!: ElementRef<HTMLDivElement>;

  private animationInstance: AnimeInstance | null = null;

  ngAfterViewInit(): void {
    // ElementRef is available here
    if (this.boxRef?.nativeElement) {
      this.animationInstance = anime({
        targets: this.boxRef.nativeElement, // Access DOM node via .nativeElement
        translateX: 250,
        rotate: '1turn',
        backgroundColor: '#FFF',
        duration: 800,
        loop: true,
        direction: 'alternate',
        easing: 'easeInOutQuad'
      });
    }
  }

  ngOnDestroy(): void {
    // Cleanup when component is destroyed
    if (this.animationInstance) {
      // anime.remove(this.boxRef.nativeElement); // Option 1
      this.animationInstance.pause(); // Option 2
      this.animationInstance = null;
      console.log('Animation paused and cleaned up');
    }
  }
}
```

## Key Considerations for Frameworks

*   **Lifecycle Hooks:** Always initialize animations *after* the target elements are rendered (e.g., `useEffect`, `onMounted`, `ngAfterViewInit`).
*   **Element References:** Use the framework's specific mechanism (`useRef`, `ref`, `ElementRef`/`@ViewChild`) to get a stable reference to the DOM element. Avoid direct DOM manipulation (`document.querySelector`) within components if possible.
*   **Cleanup:** Crucially, clean up animations when the component is destroyed (`useEffect` return function, `onUnmounted`, `ngOnDestroy`). This usually involves pausing the animation (`.pause()`) or removing the targets (`anime.remove()`) to prevent memory leaks and errors if the component tries to animate elements that no longer exist.
*   **State Management:** For animations driven by component state, ensure state updates correctly trigger animation changes or restarts as needed.
*   **Change Detection (Angular):** Be aware that anime.js animations run outside Angular's zone. If an animation callback (`update`, `complete`) needs to update component properties that affect the template, you might need to re-enter the zone using `NgZone.run()` or trigger change detection manually (`ChangeDetectorRef.detectChanges()` or `markForCheck()`). Using Signals often simplifies this.

Integrating anime.js requires understanding both the animation library's API and the framework's lifecycle and DOM referencing mechanisms.