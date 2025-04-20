# Common Animation Patterns with anime.js

Examples of frequently used animation effects.

## 1. Fade In / Fade Out

```javascript
// Fade In
anime({
  targets: '.element-to-fade-in',
  opacity: [0, 1],
  duration: 1000,
  easing: 'easeOutExpo'
});

// Fade Out
anime({
  targets: '.element-to-fade-out',
  opacity: [1, 0],
  duration: 800,
  easing: 'easeInExpo',
  // Optional: Hide element after fade out
  complete: (anim) => {
    anim.animatables.forEach(a => a.target.style.display = 'none');
  }
});
```

## 2. Slide In / Slide Out

```javascript
// Slide In from Left
anime({
  targets: '.element-to-slide-in',
  translateX: ['-100%', 0], // Start off-screen left
  opacity: [0, 1], // Optional fade-in
  duration: 900,
  easing: 'easeOutCubic'
});

// Slide Out to Right
anime({
  targets: '.element-to-slide-out',
  translateX: [0, '100%'], // End off-screen right
  opacity: [1, 0], // Optional fade-out
  duration: 700,
  easing: 'easeInCubic'
});
```

## 3. Staggered List Animation (Fade & Slide Up)

```javascript
anime({
  targets: '.list-item',
  translateY: [50, 0], // Start 50px down
  opacity: [0, 1],
  duration: 800,
  delay: anime.stagger(100), // 100ms delay between each item
  easing: 'easeOutExpo'
});
```

## 4. Simple Hover Effect (Scale)

```javascript
const element = document.querySelector('.hover-target');

element.addEventListener('mouseenter', () => {
  anime({
    targets: element,
    scale: 1.1,
    duration: 300,
    easing: 'easeOutQuad'
  });
});

element.addEventListener('mouseleave', () => {
  anime({
    targets: element,
    scale: 1.0,
    duration: 400,
    easing: 'easeOutQuad'
  });
});
```

## 5. Basic Timeline Sequence

```javascript
const tl = anime.timeline({
  easing: 'easeInOutSine',
  duration: 500
});

tl
  .add({
    targets: '.box1',
    translateX: 200,
  })
  .add({
    targets: '.box2',
    translateY: 100,
    offset: '-=300' // Start 300ms before box1 finishes
  })
  .add({
    targets: '.box3',
    scale: 1.2,
    rotate: '1turn'
  });
```

*(These are basic examples. Combine properties, timings, easings, and timelines for more complex effects.)*