# anime.js Framework Integration Patterns

Examples of integrating anime.js animations within popular frontend frameworks, focusing on lifecycle hooks and cleanup.

## React (`useEffect`, `useRef`)

```jsx
import React, { useRef, useEffect } from 'react';
import anime from 'animejs/lib/anime.es.js';

function AnimatedComponent() {
  const elementRef = useRef(null);
  const animationRef = useRef(null); // Store animation instance

  useEffect(() => {
    if (elementRef.current) {
      // Initialize animation
      animationRef.current = anime({
        targets: elementRef.current,
        translateX: 250,
        rotate: '1turn',
        backgroundColor: '#FFF',
        duration: 800,
        easing: 'easeInOutQuad',
        autoplay: false // Often control playback manually
      });
    }

    // Cleanup function: Stop animation on unmount
    return () => {
      if (animationRef.current) {
        // Remove targets to stop animation and prevent memory leaks
        anime.remove(elementRef.current);
        animationRef.current = null; // Clear ref
      }
    };
  }, []); // Empty dependency array: run only on mount and unmount

  const playAnimation = () => {
    if (animationRef.current) {
      animationRef.current.play();
    }
  };

  return (
    <div>
      <div ref={elementRef} style={{ width: '50px', height: '50px', backgroundColor: '#F00' }}></div>
      <button onClick={playAnimation}>Play</button>
    </div>
  );
}

export default AnimatedComponent;
```

## Vue (`onMounted`, `onUnmounted`, `ref`)

```vue
<template>
  <div>
    <div ref="elementRef" style="width: 50px; height: 50px; background-color: #F00;"></div>
    <button @click="playAnimation">Play</button>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import anime from 'animejs/lib/anime.es.js';

const elementRef = ref(null);
let animationInstance = null; // Store animation instance

onMounted(() => {
  if (elementRef.value) {
    animationInstance = anime({
      targets: elementRef.value,
      translateX: 250,
      rotate: '1turn',
      backgroundColor: '#FFF',
      duration: 800,
      easing: 'easeInOutQuad',
      autoplay: false
    });
  }
});

onUnmounted(() => {
  if (animationInstance && elementRef.value) {
    // Remove targets to stop animation and prevent memory leaks
    anime.remove(elementRef.value);
    animationInstance = null;
  }
});

const playAnimation = () => {
  if (animationInstance) {
    animationInstance.play();
  }
};
</script>
```

## Angular (`ngOnInit`, `ngOnDestroy`, `ElementRef`)

```typescript
import { Component, OnInit, OnDestroy, ElementRef, inject, viewChild } from '@angular/core';
import anime, { AnimeInstance } from 'animejs/lib/anime.es.js'; // Import type if needed

@Component({
  selector: 'app-animated-box',
  standalone: true,
  template: `
    <div #animatedElement style="width: 50px; height: 50px; background-color: #F00;"></div>
    <button (click)="playAnimation()">Play</button>
  `,
})
export class AnimatedBoxComponent implements OnInit, OnDestroy {
  // Use viewChild for safer element access
  animatedElementRef = viewChild.required<ElementRef<HTMLDivElement>>('animatedElement');

  private animationInstance: AnimeInstance | null = null;

  ngOnInit(): void {
    // Access element after view initialization
    this.animationInstance = anime({
      targets: this.animatedElementRef().nativeElement,
      translateX: 250,
      rotate: '1turn',
      backgroundColor: '#FFF',
      duration: 800,
      easing: 'easeInOutQuad',
      autoplay: false
    });
  }

  ngOnDestroy(): void {
    if (this.animationInstance) {
      // Remove targets to stop animation and prevent memory leaks
      anime.remove(this.animatedElementRef().nativeElement);
      this.animationInstance = null;
    }
  }

  playAnimation(): void {
    if (this.animationInstance) {
      this.animationInstance.play();
    }
  }
}
```

**Key Points:**
*   **Target Selection:** Use framework-specific refs (`useRef`, `ref`, `ElementRef`/`viewChild`) to get direct DOM references instead of relying solely on CSS selectors, especially within components.
*   **Lifecycle Hooks:** Initialize animations in mount/init hooks (`useEffect`, `onMounted`, `ngOnInit`/`ngAfterViewInit`).
*   **Cleanup:** **Crucially**, use cleanup hooks (`useEffect` return function, `onUnmounted`, `ngOnDestroy`) to remove the animation targets using `anime.remove(target)` to stop animations and prevent memory leaks when components are destroyed.