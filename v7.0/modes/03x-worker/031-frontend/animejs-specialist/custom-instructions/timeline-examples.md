# anime.js Timeline Examples

Illustrative examples of using `anime.timeline()` for sequencing animations.

## 1. Simple Sequence

Animates box1, then box2, then box3 one after another.

```javascript
anime.timeline({
  easing: 'easeOutExpo',
  duration: 750
})
.add({
  targets: '.box1',
  translateX: 250
})
.add({
  targets: '.box2',
  translateY: 100
})
.add({
  targets: '.box3',
  rotate: 360
});
```

## 2. Overlapping Animations with Relative Offset

Box2 starts 300ms before Box1 finishes. Box3 starts exactly when Box2 starts.

```javascript
anime.timeline({
  easing: 'easeInOutSine',
  duration: 1000
})
.add({
  targets: '.box1',
  scale: 1.5
})
.add({
  targets: '.box2',
  translateX: 200,
  offset: '-=300' // Relative offset from the END of the previous animation
})
.add({
  targets: '.box3',
  translateY: 50,
  offset: '-=700' // Relative offset from the END of the *first* animation (1000ms - 300ms = 700ms)
  // OR use absolute offset: offset: 700
});
```

## 3. Absolute Offsets

Position animations precisely on the timeline.

```javascript
anime.timeline({
  easing: 'linear',
})
.add({
  targets: '.el1',
  opacity: [0, 1],
  duration: 500,
  offset: 0 // Starts immediately
})
.add({
  targets: '.el2',
  translateX: 100,
  duration: 800,
  offset: 200 // Starts at 200ms
})
.add({
  targets: '.el3',
  scale: [1, 1.2],
  duration: 600,
  offset: 500 // Starts at 500ms
});
```

## 4. Combining Timelines and Staggering

Stagger multiple elements within a timeline step.

```javascript
anime.timeline({
  duration: 600,
  easing: 'easeOutCubic'
})
.add({
  targets: '.intro-text',
  opacity: [0, 1],
  translateY: [20, 0]
})
.add({
  targets: '.card',
  scale: [0.8, 1],
  opacity: [0, 1],
  delay: anime.stagger(150), // Stagger cards after intro text
  offset: '-=300' // Overlap slightly with intro text fade-in
});
```

*(Remember to adjust targets, properties, durations, offsets, and easing functions based on the specific animation requirements.)*