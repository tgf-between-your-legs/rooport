TITLE: Importing and Using Anime.js with Vanilla JavaScript
DESCRIPTION: This code demonstrates how to import Anime.js modules and create animations in vanilla JavaScript. It includes a bounce animation loop, making an element draggable, and animating rotation on click events. The snippet uses utility functions for selecting DOM elements and the animation API.

LANGUAGE: javascript
CODE:
import { animate, utils, createSpring } from 'animejs';

const [ $logo ] = utils.$('.logo.js');
const [ $button ] = utils.$('button');
let rotations = 0;

// Created a bounce animation loop
animate('.logo.js', {
  scale: [
    { to: 1.25, ease: 'inOut(3)', duration: 200 },
    { to: 1, ease: createSpring({ stiffness: 300 }) }
  ],
  loop: true,
  loopDelay: 250,
});

// Make the logo draggable around its center
createDraggable('.logo.js', {
  container: [0, 0, 0, 0],
  releaseEase: createSpring({ stiffness: 200 })
});

// Animate logo rotation on click
const rotateLogo = () => {
  rotations++;
  $button.innerText = `rotations: ${rotations}`;
  animate($logo, {
    rotate: rotations * 360,
    ease: 'out(4)',
    duration: 1500,
  });
}

$button.addEventListener('click', rotateLogo);

----------------------------------------

TITLE: HTML Structure for Animation Targets
DESCRIPTION: HTML markup showing span elements that would be targeted by the animation in the example, arranged in a grid to spell 'HELLO WORLD'.

LANGUAGE: html
CODE:
<h2 class="large grid centered square-grid text-xl">
  <span>H</span>
  <span>E</span>
  <span>L</span>
  <span>L</span>
  <span>O</span>
  <span>&nbsp;</span>
  <span>W</span>
  <span>O</span>
  <span>R</span>
  <span>L</span>
  <span>D</span>
</h2>

----------------------------------------

TITLE: Complex Animation with Keyframes and Property Parameters
DESCRIPTION: A comprehensive example showing animation with keyframes, property-specific parameters, function-based values, easing, loops, and delays.

LANGUAGE: javascript
CODE:
import { animate } from 'animejs';

animate('span', {
  // Property keyframes
  y: [
    { to: '-2.75rem', ease: 'outExpo', duration: 600 },
    { to: 0, ease: 'outBounce', duration: 800, delay: 100 }
  ],
  // Property specific parameters
  rotate: {
    from: '-1turn',
    delay: 0
  },
  delay: (_, i) => i * 50, // Function based value
  ease: 'inOutCirc',
  loopDelay: 1000,
  loop: true
});

----------------------------------------

TITLE: Defining Animatable Properties in AnimateJS
DESCRIPTION: This snippet demonstrates how to define properties that can be animated using the animate() function in AnimateJS. It shows how to set translateX, scale, and opacity along with animation control parameters like duration, delay, easing, and callbacks.

LANGUAGE: javascript
CODE:
animate('.square', {
┌──────────────────┐
│ translateX: 100, │
│ scale: 2,        ├─ Animatable Properties
│ opacity: .5,     │
└──────────────────┘
  duration: 400,
  delay: 250,
  ease: 'out(3)',
  loop: 3,
  alternate: true,
  autoplay: false,
  onBegin: () => {},
  onLoop: () => {},
  onUpdate: () => {},
});

----------------------------------------

TITLE: Defining Animation Values with AnimeJS
DESCRIPTION: Demonstrates how to specify different tween value types in AnimeJS animations. This example shows various ways to define property values including string values with units, function-based values that reference elements, relative values with operators, and object notation for explicit from/to values.

LANGUAGE: javascript
CODE:
animate('.square', {
  x: '6rem', ─────────────────┐
  y: $el => $el.dataset.y, ───┤
  scale: '+=.25', ────────────┼─ Tween Values
  opacity: {                  │
    from: .4, ────────────────┘
  },
});

----------------------------------------

TITLE: Defining Animatable Properties in AnimateJS
DESCRIPTION: This snippet demonstrates how to define properties that can be animated using the animate() function in AnimateJS. It shows how to set translateX, scale, and opacity along with animation control parameters like duration, delay, easing, and callbacks.

LANGUAGE: javascript
CODE:
animate('.square', {
┌──────────────────┐
│ translateX: 100, │
│ scale: 2,        ├─ Animatable Properties
│ opacity: .5,     │
└──────────────────┘
  duration: 400,
  delay: 250,
  ease: 'out(3)',
  loop: 3,
  alternate: true,
  autoplay: false,
  onBegin: () => {},
  onLoop: () => {},
  onUpdate: () => {},
});

----------------------------------------

TITLE: Creating Basic Animation with AnimeJS
DESCRIPTION: Shows the fundamental pattern for creating an animation using the animate() method with targets and parameters.

LANGUAGE: javascript
CODE:
const animation = animate(targets, parameters);

----------------------------------------

TITLE: Animating CSS Transforms with AnimeJS using both JavaScript and WAAPI Methods
DESCRIPTION: Shows how to animate CSS transform properties using AnimeJS in two ways: the JavaScript animate() method with individual transform properties and the WAAPI animate() method with the direct transform property. This demonstrates the flexibility of controlling transform animations in AnimeJS.

LANGUAGE: javascript
CODE:
import { animate, waapi } from 'animejs';

animate('.square', {
  x: '15rem', // TranslateX shorthand
  scale: 1.25,
  skew: -45,
  rotate: '1turn',
});

// the WAAPI version is recommanded if you want to animate the transform property directly
waapi.animate('.square', {
  transform: 'translateX(15rem) scale(1.25) skew(-45deg) rotate(1turn)',
});

----------------------------------------

TITLE: Integrating Anime.js with React using Hooks and createScope
DESCRIPTION: A comprehensive React component example that demonstrates how to use Anime.js with React hooks. It shows how to create animation scopes, implement animations with springs, make elements draggable, and properly clean up animations when components unmount.

LANGUAGE: jsx
CODE:
import { animate, createScope, createSpring, createDraggable } from 'animejs';
import { useEffect, useRef, useState } from 'react';
import reactLogo from './assets/react.svg';
import './App.css';

function App() {
  const root = useRef(null);
  const scope = useRef(null);
  const [ rotations, setRotations ] = useState(0);

  useEffect(() => {
  
    scope.current = createScope({ root }).add( scope => {
    
      // Every anime.js instances declared here are now scopped to <div ref={root}>

      // Created a bounce animation loop
      animate('.logo', {
        scale: [
          { to: 1.25, ease: 'inOut(3)', duration: 200 },
          { to: 1, ease: createSpring({ stiffness: 300 }) }
        ],
        loop: true,
        loopDelay: 250,
      });
      
      // Make the logo draggable around its center
      createDraggable('.logo', {
        container: [0, 0, 0, 0],
        releaseEase: createSpring({ stiffness: 200 })
      });

      // Register function methods to be used outside the useEffect
      scope.add('rotateLogo', (i) => {
        animate('.logo', {
          rotate: i * 360,
          ease: 'out(4)',
          duration: 1500,
        });
      });

    });

    // Properly cleanup all anime.js instances declared inside the scope
    return () => scope.current.revert()

  }, []);

  const handleClick = () => {
    const i = rotations + 1;
    setRotations(i);
    // Animate logo rotation on click using the method declared inside the scope
    scope.current.methods.rotateLogo(i);
  };

  return (
    <div ref={root}>
      <div className="large centered row">
        <img src={reactLogo} className="logo react" alt="React logo" />
      </div>
      <div className="medium row">
        <fieldset className="controls">
        <button onClick={handleClick}>rotations: {rotations}</button>
        </fieldset>
      </div>
    </div>
  )
}

export default App;

----------------------------------------

TITLE: Importing Anime.js as ES6 Module after NPM Installation
DESCRIPTION: Example showing how to import the animate method from Anime.js as an ES6 module after installing via NPM.

LANGUAGE: javascript
CODE:
import { animate } from 'animejs';

----------------------------------------

TITLE: Animating Elements with Tween Values Array in Anime.js
DESCRIPTION: This example demonstrates how to animate an element by specifying an array of values for x and y properties. The animation will transition through each value over the total duration.

LANGUAGE: javascript
CODE:
animate('.square', {
  x: [0, 100, 200],
  y: [0, 100, 200],
  duration: 3000,
}

----------------------------------------

TITLE: Synchronizing Multiple Timelines in AnimeJS
DESCRIPTION: This example demonstrates how to use the sync() method to synchronize different timelines and animations in AnimeJS. It shows creating and synchronizing multiple timelines with different animations, including position offsets.

LANGUAGE: javascript
CODE:
import { createTimeline, animate } from 'animejs';

const circleAnimation = animate('.circle', {
  x: '15rem'
});

const tlA = createTimeline()
.sync(circleAnimation)
.add('.triangle', {
  x: '15rem',
  duration: 2000,
})
.add('.square', {
  x: '15rem',
});

const tlB = createTimeline({ defaults: { duration: 2000 } })
.add(['.triangle', '.square'], {
  rotate: 360,
}, 0)
.add('.circle', {
  scale: [1, 1.5, 1],
}, 0);

const tlMain = createTimeline()
.sync(tlA)
.sync(tlB, '-=2000');

----------------------------------------

TITLE: Importing and Using AnimeJS to Animate CSS Properties
DESCRIPTION: This snippet demonstrates how to use AnimeJS to animate various CSS properties including positioning, border radius, background color, and filter effects. Properties with dashes are converted to camel case or written as strings.

LANGUAGE: javascript
CODE:
import { animate } from 'animejs';

animate('.square', {
  left: 'calc(7.75rem * 2)',
  borderRadius: 64,
  'background-color': '#F9F640',
  filter: 'blur(5px)',
});

----------------------------------------

TITLE: Installing Anime.js via NPM
DESCRIPTION: Command to install Anime.js using NPM package manager for projects using bundlers like Vite or esbuild.

LANGUAGE: bash
CODE:
npm install animejs

----------------------------------------

TITLE: Importing AnimeJS Animation Module
DESCRIPTION: Basic import statement for the animate function from the animejs library.

LANGUAGE: javascript
CODE:
import { animate } from 'animejs';

----------------------------------------

TITLE: Animating JavaScript Object Properties with AnimeJS
DESCRIPTION: This snippet demonstrates how to animate a JavaScript object's properties using AnimeJS. It creates a 2D vector object and animates its x and y coordinates from 0 to 100 and 150 respectively, with the current state displayed in a code element. The animation uses the round modifier to ensure integer values and an onUpdate callback to display the changing values.

LANGUAGE: javascript
CODE:
import { animate, utils } from 'animejs';

const [ $log ] = utils.$('code');

const vector2D = { x: 0, y: 0 };

animate(vector2D, {
  x: 100,
  y: 150,
  modifier: utils.round(0),
  onUpdate: () => $log.textContent = JSON.stringify(vector2D),
});

LANGUAGE: html
CODE:
<pre class="row large centered">
  <code>{"x":0,"y":0}</code>
</pre>

----------------------------------------

TITLE: Implementing Complete Animation with Keyframes in Anime.js
DESCRIPTION: A complete example showing how to use the animate function from Anime.js with keyframes. Demonstrates sequencing multiple animation states with individual timing and easing parameters while also applying global animation settings.

LANGUAGE: javascript
CODE:
import { animate } from 'animejs';

animate('.square', {
  keyframes: [
    { y: '-2.5rem', ease: 'out', duration: 400 },
    { x: '17rem', scale: .5, duration: 800 },
    { y: '2.5rem' }, // The duration here is 3000 / 5 = 600ms
    { x: 0, scale: 1, duration: 800 },
    { y: 0, ease: 'in', duration: 400 }
  ],
  rotate: { to: 360, ease: 'linear' },
  duration: 3000,
  ease: 'inOut', // ease applied between each keyframes if no ease defined
  playbackEase: 'ouIn(5)', // ease applied accross all keyframes
  loop: true,
});

----------------------------------------

TITLE: Implementing Resume, Pause, and Alternate Controls with AnimeJS in JavaScript
DESCRIPTION: This code demonstrates how to create animation controls using AnimeJS. It sets up an animation that moves squares horizontally with staggered delays and implements pause, alternate, and resume functionality through button click handlers.

LANGUAGE: javascript
CODE:
import { animate, utils, stagger } from 'animejs';

const [ $pauseButton, $alternateButton, $resumeButton ] = utils.$('.button');

const animation = animate('.square', {
  x: '17rem',
  ease: 'inOutSine',
  loop: true,
  delay: stagger(100),
});

const pauseAnimation = () => animation.pause();
const alternateAnimation = () => animation.alternate();
const resumeAnimation = () => animation.resume();

$pauseButton.addEventListener('click', pauseAnimation);
$alternateButton.addEventListener('click', alternateAnimation);
$resumeButton.addEventListener('click', resumeAnimation);

----------------------------------------

TITLE: Importing createScope from Anime.js
DESCRIPTION: Basic syntax for importing and creating a new animation scope with parameters in Anime.js.

LANGUAGE: javascript
CODE:
import { createScope } from 'animejs';

const scope = createScope(parameters);

----------------------------------------

TITLE: Configuring Animation Playback Settings with AnimeJS in JavaScript
DESCRIPTION: This snippet demonstrates how to configure animation playback settings in AnimeJS. It shows how to animate a square element with various properties including transformation, opacity, duration, delay, easing function, and playback settings such as looping, alternating direction, and autoplay control.

LANGUAGE: javascript
CODE:
animate('.square', {
  translateX: 100,
  scale: 2,
  opacity: .5,
  duration: 400,
  delay: 250,
  ease: 'out(3)',
  loop: 3,
  alternate: true,
  autoplay: false,
  onBegin: () => {},
  onLoop: () => {},
  onUpdate: () => {},
});

----------------------------------------

TITLE: Creating an Animation Object in AnimeJS
DESCRIPTION: This snippet demonstrates how to create an animation object in AnimeJS by calling the animate function with targets and parameters. The animation object provides access to various properties for controlling and monitoring the animation.

LANGUAGE: javascript
CODE:
const animation = animate(targets, parameters);

----------------------------------------

TITLE: Creating WAAPI-powered Animation
DESCRIPTION: Shows how to create an animation using the lightweight WAAPI version of AnimeJS.

LANGUAGE: javascript
CODE:
const animation = waapi.animate(targets, parameters);

----------------------------------------

TITLE: Importing and Using AnimeJS with DOM Element Targets
DESCRIPTION: Demonstrates how to import the animate function from AnimeJS and use it to target DOM elements. The example shows animating both a single element and a collection of elements with different properties.

LANGUAGE: javascript
CODE:
import { animate } from 'animejs';

const $demo = document.querySelector('#selector-demo');
const $squares = $demo.querySelectorAll('.square');

animate($demo, { scale: .75 });
animate($squares, { x: '23rem' });

----------------------------------------

TITLE: Complete Timeline Example with add() and sync() in Anime.js
DESCRIPTION: A comprehensive example showing how to import Anime.js functions, create an animation, then add it to a timeline using sync(). Also demonstrates adding additional animations directly with add() and chaining timeline methods.

LANGUAGE: javascript
CODE:
import { createTimeline, animate } from 'animejs';

const circleAnimation = animate('.circle', {
  x: '15rem'
});

const tl = createTimeline()
.sync(circleAnimation)
.add('.triangle', {
  x: '15rem',
  rotate: '1turn',
  duration: 500,
  alternate: true,
  loop: 2,
})
.add('.square', {
  x: '15rem',
});

----------------------------------------

TITLE: Importing and Creating a Timeline in AnimeJS
DESCRIPTION: Basic syntax for importing the createTimeline function from AnimeJS and creating a new timeline instance. The timeline can be configured with optional parameters for playback settings and callbacks.

LANGUAGE: javascript
CODE:
import { createTimeline } from 'animejs';

const timeline = createTimeline(parameters);

----------------------------------------

TITLE: Animating Elements with Different Color Formats in AnimeJS
DESCRIPTION: This snippet demonstrates how to animate background colors of elements using various color formats in AnimeJS. It imports the animate function and applies different color formats (HEX, RGB, HSL, HEXA, RGBA, HSLA) to target elements with corresponding class names.

LANGUAGE: javascript
CODE:
import { animate } from 'animejs';

animate('.hex',  {
  background: '#FF4B4B',
});

animate('.rgb',  {
  background: 'rgb(255, 168, 40)',
});

animate('.hsl',  {
  background: 'hsl(44, 100%, 59%)',
});

animate('.hexa', {
  background: '#FF4B4B33',
});

animate('.rgba', {
  background: 'rgba(255, 168, 40, .2)',
});

animate('.hsla', {
  background: 'hsla(44, 100%, 59%, .2)',
});

----------------------------------------

TITLE: Creating a Responsive Animation Scope with Media Queries
DESCRIPTION: Example of creating a scope with media queries to adjust animations based on screen size and user preferences. The animation adapts by changing its behavior, direction, and duration when viewed on smaller screens or when reduced motion is preferred.

LANGUAGE: javascript
CODE:
import { animate, utils, createScope } from 'animejs';

createScope({
  mediaQueries: {
    isSmall: '(max-width: 200px)',
    reduceMotion: '(prefers-reduced-motion)',
  }
})
.add(self => {

  const { isSmall, reduceMotion } = self.matches;
  
  if (isSmall) {
    utils.set('.square', { scale: .5 });
  }
    
  animate('.square', {
    x: isSmall ? 0 : ['-35vw', '35vw'],
    y: isSmall ? ['-40vh', '40vh'] : 0,
    loop: true,
    alternate: true,
    duration: reduceMotion ? 0 : isSmall ? 750 : 1250
  });

});

----------------------------------------

TITLE: Interactive Animation with Mouse Tracking in anime.js
DESCRIPTION: A complete example demonstrating how to create an interactive animation that responds to mouse movement. The code creates an animatable circle element and updates its position and background color based on cursor coordinates.

LANGUAGE: javascript
CODE:
import { createAnimatable, utils } from 'animejs';

const $demos = document.querySelector('#docs-demos');
const $demo = $demos.querySelector('.docs-demo.is-active');
let bounds = $demo.getBoundingClientRect();
const refreshBounds = () => bounds = $demo.getBoundingClientRect();

const circle = createAnimatable('.circle', {
  x: 0,
  y: 0,
  backgroundColor: 0,
  ease: 'outExpo',
});

const rgb = [164, 255, 79];

// Sets new durations and easings
circle.x(0, 500, 'out(2)');
circle.y(0, 500, 'out(3)');
circle.backgroundColor(rgb, 250);

const onMouseMove = e => {
  const { width, height, left, top } = bounds;
  const hw = width / 2;
  const hh = height / 2;
  const x = utils.clamp(e.clientX - left - hw, -hw, hw);
  const y = utils.clamp(e.clientY - top - hh, -hh, hh);
  rgb[0] = utils.mapRange(x, -hw, hw, 0, 164);
  rgb[2] = utils.mapRange(x, -hw, hw, 79, 255);
  circle.x(x).y(y).backgroundColor(rgb); // Update values
}

window.addEventListener('mousemove', onMouseMove);
$demos.addEventListener('scroll', refreshBounds);

----------------------------------------

TITLE: Creating Duration-Based Keyframe Animation in Anime.js
DESCRIPTION: This snippet demonstrates how to create a duration-based keyframe animation that affects multiple properties per keyframe. Each object in the keyframes array represents a state in the animation sequence.

LANGUAGE: javascript
CODE:
animate('.square', {
  keyframes: [
    { x: 100, y: 100 },
    { x: 200, y: 200 },
  ],
  duration: 3000,
}

----------------------------------------

TITLE: Implementing Staggered Animation with AnimeJS in JavaScript
DESCRIPTION: This snippet demonstrates how to use the stagger function in AnimeJS to create staggered animations. The code animates multiple '.square' elements with staggered y-position and rotation values, creating a sequential effect across targets. The animation is set to loop and alternate direction.

LANGUAGE: javascript
CODE:
import { animate, stagger } from 'animejs';

const animation = animate('.square', {
  y: stagger(['-2.75rem', '2.75rem']),
  rotate: { from: stagger('-.125turn') },
  loop: true,
  alternate: true
});

----------------------------------------

TITLE: Creating an Animation Instance in AnimeJS
DESCRIPTION: Shows how to create an animation instance object that provides access to animation control methods like play(), pause(), and restart().

LANGUAGE: javascript
CODE:
const animation = animate(target, parameters);

----------------------------------------

TITLE: Creating and Using Timeline with Labels and Relative Positioning in AnimeJS
DESCRIPTION: Example of creating a timeline with default settings, adding animations with label references and relative time positions. This demonstrates animation sequencing and timing control.

LANGUAGE: javascript
CODE:
import { createTimeline } from 'animejs';

const tl = createTimeline({ defaults: { duration: 750 } });

tl.label('start')
  .add('.square', { x: '15rem' }, 500)
  .add('.circle', { x: '15rem' }, 'start')
  .add('.triangle', { x: '15rem', rotate: '1turn' }, '<-=500');

----------------------------------------

TITLE: Using onLeave Callback with AnimeJS ScrollObserver in JavaScript
DESCRIPTION: This code demonstrates how to set up scroll-based animation with AnimeJS that tracks when an element leaves the viewport. It imports the necessary functions, selects DOM elements, and creates an animation with a ScrollObserver that increments a counter each time the element exits the viewport.

LANGUAGE: javascript
CODE:
import { animate, onScroll, utils } from 'animejs';

const [ $value ] = utils.$('.value');

let exits = 0;

animate('.square', {
  x: '15rem',
  rotate: '1turn',
  ease: 'linear',
  autoplay: onScroll({
    container: '.scroll-container',
    enter: 'bottom-=50 top',
    leave: 'top+=60 bottom',
    sync: true,
    debug: true,
    onLeave: () => $value.textContent = ++exits,
  })
});

----------------------------------------

TITLE: Basic Timeline Control Methods in Anime.js
DESCRIPTION: Examples of basic timeline control methods in Anime.js, including pause(), play(), and restart(). These methods allow for controlling the execution state of animation timelines.

LANGUAGE: javascript
CODE:
timeline.pause()
timeline.play()
timeline.restart()

----------------------------------------

TITLE: Timer Implementation Example with Callbacks in AnimJS
DESCRIPTION: Shows a complete example of creating a timer with various settings including duration, loop, frameRate, and callback functions. This example updates DOM elements with the current time and loop count.

LANGUAGE: javascript
CODE:
import { animate } from 'animejs';

const [ $time, $count ] = utils.$('.value');

createTimer({
  duration: 1000,
  loop: true,
  frameRate: 30,
  onUpdate: self => $time.innerHTML = self.currentTime,
  onLoop: self => $count.innerHTML = self._currentIteration
});