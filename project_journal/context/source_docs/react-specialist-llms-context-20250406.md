TITLE: Declaring a State Variable with useState
DESCRIPTION: Call useState at the top level of your component to declare a state variable. It returns an array with the current state and a function to update it.

LANGUAGE: javascript
CODE:
const [state, setState] = useState(initialState)

----------------------------------------

TITLE: Using useState Hook in React
DESCRIPTION: Demonstrates how to use the useState Hook to add state to a React component. The example shows declaring a state variable 'index' and its setter function 'setIndex' for an ImageGallery component.

LANGUAGE: javascript
CODE:
function ImageGallery() {
  const [index, setIndex] = useState(0);
  // ...


----------------------------------------

TITLE: Creating React Components with JSX
DESCRIPTION: Demonstrates how to create and nest React components using JSX syntax. The Gallery component renders multiple Profile components.

LANGUAGE: jsx
CODE:
function Profile() {
  return (
    <img
      src="https://i.imgur.com/MK3eW3As.jpg"
      alt="Katherine Johnson"
    />
  );
}

export default function Gallery() {
  return (
    <section>
      <h1>Amazing scientists</h1>
      <Profile />
      <Profile />
      <Profile />
    </section>
  );
}

----------------------------------------

TITLE: Creating Basic React Component
DESCRIPTION: Demonstrates how to create a simple React button component using a function that returns JSX markup.

LANGUAGE: JavaScript
CODE:
function MyButton() {
  return (
    <button>I'm a button</button>
  );
}

----------------------------------------

TITLE: Reading context in a component
DESCRIPTION: Call useContext at the top level of your component to read and subscribe to context.

LANGUAGE: javascript
CODE:
const value = useContext(SomeContext)

----------------------------------------

TITLE: Rendering Lists in React
DESCRIPTION: Demonstrates how to render a list of components from an array of data using map(). Each list item requires a unique key prop for React to track items efficiently.

LANGUAGE: jsx
CODE:
export default function List() {
  const listItems = people.map(person =>
    <li key={person.id}>
      <img
        src={getImageUrl(person)}
        alt={person.name}
      />
      <p>
        <b>{person.name}:</b>
        {' ' + person.profession + ' '}
        known for {person.accomplishment}
      </p>
    </li>
  );
  return (
    <article>
      <h1>Scientists</h1>
      <ul>{listItems}</ul>
    </article>
  );
}

----------------------------------------

TITLE: Optimizing re-renders with objects and functions
DESCRIPTION: Use useMemo and useCallback to optimize re-renders when passing objects and functions via context.

LANGUAGE: javascript
CODE:
function MyApp() {
  const [currentUser, setCurrentUser] = useState(null);

  const login = useCallback((response) => {
    storeCredentials(response.credentials);
    setCurrentUser(response.user);
  }, []);

  const contextValue = useMemo(() => ({
    currentUser,
    login
  }), [currentUser, login]);

  return (
    <AuthContext.Provider value={contextValue}>
      <Page />
    </AuthContext.Provider>
  );
}

----------------------------------------

TITLE: Updating State in a React Event Handler
DESCRIPTION: Shows how to update a state variable using its setter function inside an event handler. The 'handleClick' function increments the 'index' state variable.

LANGUAGE: JavaScript
CODE:
function handleClick() {
  setIndex(index + 1);
}

----------------------------------------

TITLE: Initializing State with useState in React
DESCRIPTION: Demonstrates how to initialize a state variable using the useState Hook in a React component. The state variable 'index' is created with an initial value of 0 and a setter function 'setIndex'.

LANGUAGE: JavaScript
CODE:
const [index, setIndex] = useState(0);

----------------------------------------

TITLE: Creating a TasksProvider Component
DESCRIPTION: Encapsulate the reducer and context logic in a separate provider component for cleaner organization.

LANGUAGE: JSX
CODE:
export function TasksProvider({ children }) {
  const [tasks, dispatch] = useReducer(tasksReducer, initialTasks);
  return (
    <TasksContext.Provider value={tasks}>
      <TasksDispatchContext.Provider value={dispatch}>
        {children}
      </TasksDispatchContext.Provider>
    </TasksContext.Provider>
  );
}

----------------------------------------

TITLE: Modern Context Usage with useContext
DESCRIPTION: Demonstrates the recommended way to read context values using the useContext hook.

LANGUAGE: javascript
CODE:
function Button() {
  const theme = useContext(ThemeContext);
  return <button className={theme} />;
}

----------------------------------------

TITLE: Forwarding Props with JSX Spread Syntax in React
DESCRIPTION: Demonstrates how to forward all props to a child component using the spread syntax. This can be useful when a component doesn't use props directly but passes them to its children.

LANGUAGE: jsx
CODE:
function Profile(props) {
  return (
    <div className="card">
      <Avatar {...props} />
    </div>
  );
}

----------------------------------------

TITLE: Server Components Build-Time Rendering
DESCRIPTION: Shows how Server Components can render content at build time, eliminating the need for client-side libraries and improving initial load performance.

LANGUAGE: javascript
CODE:
import marked from 'marked'; // Not included in bundle
import sanitizeHtml from 'sanitize-html'; // Not included in bundle

async function Page({page}) {
  // NOTE: loads *during* render, when the app is built.
  const content = await file.readFile(`${page}.md`);
  
  return <div>{sanitizeHtml(marked(content))}</div>;
}

----------------------------------------

TITLE: Interface-based React Component Props
DESCRIPTION: Example demonstrating how to use TypeScript interfaces to define component props with documentation and multiple properties.

LANGUAGE: tsx
CODE:
interface MyButtonProps {
  /** The text to display inside the button */
  title: string;
  /** Whether the button can be interacted with */
  disabled: boolean;
}

function MyButton({ title, disabled }: MyButtonProps) {
  return (
    <button disabled={disabled}>{title}</button>
  );
}

----------------------------------------

TITLE: Implementing a Form with State in React
DESCRIPTION: This snippet demonstrates a React component that uses state to manage a form submission. It shows how setting state triggers a re-render and updates the UI.

LANGUAGE: JavaScript
CODE:
import { useState } from 'react';

export default function Form() {
  const [isSent, setIsSent] = useState(false);
  const [message, setMessage] = useState('Hi!');
  if (isSent) {
    return <h1>Your message is on its way!</h1>
  }
  return (
    <form onSubmit={(e) => {
      e.preventDefault();
      setIsSent(true);
      sendMessage(message);
    }}>
      <textarea
        placeholder="Message"
        value={message}
        onChange={e => setMessage(e.target.value)}
      />
      <button type="submit">Send</button>
    </form>
  );
}

function sendMessage(message) {
  // ...
}

----------------------------------------

TITLE: Basic useRef Hook Usage - React
DESCRIPTION: Basic example of declaring and using a ref with useRef hook. Returns an object with a mutable current property that persists across renders.

LANGUAGE: javascript
CODE:
const ref = useRef(initialValue)

----------------------------------------

TITLE: Sharing State Between Components in React
DESCRIPTION: Illustrates how to lift state up to a common parent component to share it between child components.

LANGUAGE: jsx
CODE:
import { useState } from 'react';

export default function Accordion() {
  const [activeIndex, setActiveIndex] = useState(0);
  return (
    <>
      <h2>Almaty, Kazakhstan</h2>
      <Panel
        title="About"
        isActive={activeIndex === 0}
        onShow={() => setActiveIndex(0)}
      >
        With a population of about 2 million, Almaty is Kazakhstan's largest city. From 1929 to 1997, it was its capital city.
      </Panel>
      <Panel
        title="Etymology"
        isActive={activeIndex === 1}
        onShow={() => setActiveIndex(1)}
      >
        The name comes from <span lang="kk-KZ">алма</span>, the Kazakh word for "apple" and is often translated as "full of apples". In fact, the region surrounding Almaty is thought to be the ancestral home of the apple, and the wild <i lang="la">Malus sieversii</i> is considered a likely candidate for the ancestor of the modern domestic apple.
      </Panel>
    </>
  );
}

function Panel({
  title,
  children,
  isActive,
  onShow
}) {
  return (
    <section className="panel">
      <h3>{title}</h3>
      {isActive ? (
        <p>{children}</p>
      ) : (
        <button onClick={onShow}>
          Show
        </button>
      )}
    </section>
  );
}

----------------------------------------

TITLE: Implementing Lazy Loading with Suspense in a React Component
DESCRIPTION: A complete example showing how to implement lazy loading in a React component. It includes state management, conditional rendering, and error handling with Suspense.

LANGUAGE: javascript
CODE:
import { useState, Suspense, lazy } from 'react';
import Loading from './Loading.js';

const MarkdownPreview = lazy(() => delayForDemo(import('./MarkdownPreview.js')));

export default function MarkdownEditor() {
  const [showPreview, setShowPreview] = useState(false);
  const [markdown, setMarkdown] = useState('Hello, **world**!');
  return (
    <>
      <textarea value={markdown} onChange={e => setMarkdown(e.target.value)} />
      <label>
        <input type="checkbox" checked={showPreview} onChange={e => setShowPreview(e.target.checked)} />
        Show preview
      </label>
      <hr />
      {showPreview && (
        <Suspense fallback={<Loading />}>
          <h2>Preview</h2>
          <MarkdownPreview markdown={markdown} />
        </Suspense>
      )}
    </>
  );
}

// Add a fixed delay so you can see the loading state
function delayForDemo(promise) {
  return new Promise(resolve => {
    setTimeout(resolve, 2000);
  }).then(() => promise);
}

----------------------------------------

TITLE: Choosing State Structure in React
DESCRIPTION: Shows how to simplify state by removing redundant variables and calculating derived values during rendering.

LANGUAGE: jsx
CODE:
import { useState } from 'react';

export default function Form() {
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');

  const fullName = firstName + ' ' + lastName;

  function handleFirstNameChange(e) {
    setFirstName(e.target.value);
  }

  function handleLastNameChange(e) {
    setLastName(e.target.value);
  }

  return (
    <>
      <h2>Let's check you in</h2>
      <label>
        First name:{' '}
        <input
          value={firstName}
          onChange={handleFirstNameChange}
        />
      </label>
      <label>
        Last name:{' '}
        <input
          value={lastName}
          onChange={handleLastNameChange}
        />
      </label>
      <p>
        Your ticket will be issued to: <b>{fullName}</b>
      </p>
    </>
  );
}

----------------------------------------

TITLE: Managing State with useState Hook in React
DESCRIPTION: Shows how to use the useState Hook to add state to a component, update it, and render based on state changes.

LANGUAGE: jsx
CODE:
import { useState } from 'react';
import { sculptureList } from './data.js';

export default function Gallery() {
  const [index, setIndex] = useState(0);
  const [showMore, setShowMore] = useState(false);
  const hasNext = index < sculptureList.length - 1;

  function handleNextClick() {
    if (hasNext) {
      setIndex(index + 1);
    } else {
      setIndex(0);
    }
  }

  function handleMoreClick() {
    setShowMore(!showMore);
  }

  let sculpture = sculptureList[index];
  return (
    // Component JSX
  );
}

----------------------------------------

TITLE: Converting HTML to JSX in React
DESCRIPTION: This snippet demonstrates the process of converting HTML markup to JSX syntax for use in a React component. It shows the original HTML and the resulting JSX, highlighting the differences and necessary adjustments.

LANGUAGE: html
CODE:
<h1>Hedy Lamarr's Todos</h1>
<img 
  src="https://i.imgur.com/yXOvdOSs.jpg" 
  alt="Hedy Lamarr" 
  class="photo"
>
<ul>
    <li>Invent new traffic lights
    <li>Rehearse a movie scene
    <li>Improve the spectrum technology
</ul>

LANGUAGE: jsx
CODE:
export default function TodoList() {
  return (
    <>
      <h1>Hedy Lamarr's Todos</h1>
      <img 
        src="https://i.imgur.com/yXOvdOSs.jpg" 
        alt="Hedy Lamarr" 
        className="photo" 
      />
      <ul>
        <li>Invent new traffic lights</li>
        <li>Rehearse a movie scene</li>
        <li>Improve the spectrum technology</li>
      </ul>
    </>
  );
}

----------------------------------------

TITLE: Demonstrating State Snapshots in React
DESCRIPTION: This snippet shows how React uses state snapshots. It demonstrates that the state value accessed in an asynchronous callback reflects the value at the time the callback was created, not the current state.

LANGUAGE: JavaScript
CODE:
import { useState } from 'react';

export default function Counter() {
  const [number, setNumber] = useState(0);

  return (
    <>
      <h1>{number}</h1>
      <button onClick={() => {
        setNumber(number + 5);
        setTimeout(() => {
          alert(number);
        }, 3000);
      }}>+5</button>
    </>
  )
}

----------------------------------------

TITLE: Using useMemo Hook in React
DESCRIPTION: Shows how to use the useMemo Hook to optimize performance by caching expensive calculations. The example demonstrates memoizing filtered todos based on the 'todos' and 'tab' dependencies.

LANGUAGE: javascript
CODE:
function TodoList({ todos, tab, theme }) {
  const visibleTodos = useMemo(() => filterTodos(todos, tab), [todos, tab]);
  // ...
}

----------------------------------------

TITLE: Adding Cleanup to an Effect in React
DESCRIPTION: This snippet shows how to add a cleanup function to an Effect. The cleanup function is returned from the Effect and runs before the Effect runs again or when the component unmounts.

LANGUAGE: JavaScript
CODE:
useEffect(() => {
  const connection = createConnection();
  connection.connect();
  return () => {
    connection.disconnect();
  };
}, []);

----------------------------------------

TITLE: Updating State Based on Previous State
DESCRIPTION: Example of using an updater function to set state based on the previous state value, which is useful for avoiding race conditions.

LANGUAGE: javascript
CODE:
function handleClick() {
  setAge(a => a + 1); // setAge(42 => 43)
  setAge(a => a + 1); // setAge(43 => 44)
  setAge(a => a + 1); // setAge(44 => 45)
}

----------------------------------------

TITLE: Importing createRoot from react-dom/client in React
DESCRIPTION: Shows how to import the createRoot function from the react-dom/client package. This function is used to create a root for rendering React components in a browser DOM node.

LANGUAGE: jsx
CODE:
import { createRoot } from 'react-dom/client';

----------------------------------------

TITLE: Updating State with useState Setter Function
DESCRIPTION: Example of using the setter function returned by useState to update state in response to an event.

LANGUAGE: javascript
CODE:
function handleClick() {
  setName('Robin');
}

----------------------------------------

TITLE: Providing context to a component tree
DESCRIPTION: Wrap a component or part of the tree with a context provider to make the context value available to all components inside it.

LANGUAGE: jsx
CODE:
function MyPage() {
  return (
    <ThemeContext.Provider value="dark">
      <Form />
    </ThemeContext.Provider>
  );
}

----------------------------------------

TITLE: useContext with TypeScript
DESCRIPTION: Implementation of React Context using TypeScript with proper typing for theme values and context creation.

LANGUAGE: tsx
CODE:
type Theme = "light" | "dark" | "system";
const ThemeContext = createContext<Theme>("system");

const useGetTheme = () => useContext(ThemeContext);

----------------------------------------

TITLE: Importing and Exporting React Components
DESCRIPTION: Shows how to split React components into separate files and import/export them. The Gallery component imports and renders the Profile component.

LANGUAGE: jsx
CODE:
import Profile from './Profile.js';

export default function Gallery() {
  return (
    <section>
      <h1>Amazing scientists</h1>
      <Profile />
      <Profile />
      <Profile />
    </section>
  );
}

----------------------------------------

TITLE: Preventing Default Behavior in React Events
DESCRIPTION: This example shows how to prevent the default behavior of a form submission event in React using e.preventDefault(). It allows for custom handling of form submissions without page reloads.

LANGUAGE: jsx
CODE:
export default function Signup() {
  return (
    <form onSubmit={e => {
      e.preventDefault();
      alert('Submitting!');
    }}>
      <input />
      <button>Send</button>
    </form>
  );
}

----------------------------------------

TITLE: Interactive React Product Table with State
DESCRIPTION: Final implementation with state management and two-way data binding for search and filtering functionality.

LANGUAGE: jsx
CODE:
function FilterableProductTable({ products }) {
  const [filterText, setFilterText] = useState('');
  const [inStockOnly, setInStockOnly] = useState(false);

  return (
    <div>
      <SearchBar 
        filterText={filterText} 
        inStockOnly={inStockOnly}
        onFilterTextChange={setFilterText}
        onInStockOnlyChange={setInStockOnly} />
      <ProductTable 
        products={products}
        filterText={filterText}
        inStockOnly={inStockOnly} />
    </div>
  );
}

----------------------------------------

TITLE: Using Server Functions with Actions in Client Components
DESCRIPTION: Illustrates how to use Server Functions within Actions in Client Components, including state management and error handling.

LANGUAGE: jsx
CODE:
"use client";

import {updateName} from './actions';

function UpdateName() {
  const [name, setName] = useState('');
  const [error, setError] = useState(null);

  const [isPending, startTransition] = useTransition();

  const submitAction = async () => {
    startTransition(async () => {
      const {error} = await updateName(name);
      if (error) {
        setError(error);
      } else {
        setName('');
      }
    })
  }
  
  return (
    <form action={submitAction}>
      <input type="text" name="name" disabled={isPending}/>
      {error && <span>Failed: {error}</span>}
    </form>
  )
}

----------------------------------------

TITLE: useReducer with TypeScript
DESCRIPTION: Complete example of implementing useReducer with proper TypeScript types for state and actions.

LANGUAGE: tsx
CODE:
interface State {
   count: number 
};

type CounterAction =
  | { type: "reset" }
  | { type: "setCount"; value: State["count"] }

const initialState: State = { count: 0 };

function stateReducer(state: State, action: CounterAction): State {
  switch (action.type) {
    case "reset":
      return initialState;
    case "setCount":
      return { ...state, count: action.value };
    default:
      throw new Error("Unknown action");
  }
}

----------------------------------------

TITLE: Consuming Context with useContext Hook
DESCRIPTION: Example of reading context values in a component using the useContext Hook

LANGUAGE: javascript
CODE:
import { useContext } from 'react';
import { LevelContext } from './LevelContext.js';

export default function Heading({ children }) {
  const level = useContext(LevelContext);
  switch (level) {
    case 1:
      return <h1>{children}</h1>;
    case 2:
      return <h2>{children}</h2>;
    // ... additional cases
  }
}

----------------------------------------

TITLE: Conditional Rendering with Ternary Operator in React
DESCRIPTION: This example shows how to use the ternary operator (? :) to conditionally render JSX inline within a component's return statement.

LANGUAGE: jsx
CODE:
function Item({ name, isPacked }) {
  return (
    <li className="item">
      {isPacked ? (
        <del>
          {name + ' ✅'}
        </del>
      ) : (
        name
      )}
    </li>
  );
}

----------------------------------------

TITLE: Creating Chat Room Connection Hook in React
DESCRIPTION: Illustrates a custom useChatRoom Hook that manages chat room connections with proper cleanup.

LANGUAGE: javascript
CODE:
function useChatRoom({ serverUrl, roomId }) {
  useEffect(() => {
    const options = {
      serverUrl: serverUrl,
      roomId: roomId
    };
    const connection = createConnection(options);
    connection.connect();
    connection.on('message', (msg) => {
      showNotification('New message: ' + msg);
    });
    return () => connection.disconnect();
  }, [roomId, serverUrl]);
}

----------------------------------------

TITLE: Basic createRoot Usage in JavaScript
DESCRIPTION: Basic example of creating a React root and rendering a component into a DOM node

LANGUAGE: javascript
CODE:
import { createRoot } from 'react-dom/client';

const domNode = document.getElementById('root');
const root = createRoot(domNode);
root.render(<App />);

----------------------------------------

TITLE: Managing Form State with Status Enumeration
DESCRIPTION: Shows how to avoid contradictory state by using a single status variable with enumerated values instead of multiple boolean flags.

LANGUAGE: jsx
CODE:
const [status, setStatus] = useState('typing');

async function handleSubmit(e) {
  e.preventDefault();
  setStatus('sending');
  await sendMessage(text);
  setStatus('sent');
}

const isSending = status === 'sending';
const isSent = status === 'sent';

----------------------------------------

TITLE: Basic useReducer Hook Usage
DESCRIPTION: Shows the basic syntax for using useReducer Hook to manage component state with a reducer function.

LANGUAGE: javascript
CODE:
const [state, dispatch] = useReducer(reducer, initialArg, init?)

----------------------------------------

TITLE: Passing JSX as Children Props in React
DESCRIPTION: Shows how to pass JSX content as children to a component. The Card component receives and renders its children prop, allowing flexible content nesting.

LANGUAGE: jsx
CODE:
function Card({ children }) {
  return (
    <div className="card">
      {children}
    </div>
  );
}

export default function Profile() {
  return (
    <Card>
      <Avatar
        size={100}
        person={{ 
          name: 'Katsuko Saruhashi',
          imageId: 'YfeOqp2'
        }}
      />
    </Card>
  );
}

----------------------------------------

TITLE: Comparing useLayoutEffect and useEffect in React
DESCRIPTION: Demonstrates the difference between useLayoutEffect and useEffect in terms of when they execute relative to browser painting.

LANGUAGE: javascript
CODE:
// useLayoutEffect blocks the browser from repainting
useLayoutEffect(() => {
  const { height } = ref.current.getBoundingClientRect();
  setTooltipHeight(height);
}, []);

// useEffect does not block the browser
useEffect(() => {
  const { height } = ref.current.getBoundingClientRect();
  setTooltipHeight(height);
}, []);

----------------------------------------

TITLE: Forwarding Ref Through Multiple Components in React
DESCRIPTION: Example of forwarding a ref through multiple levels of components. FormField forwards its received ref to MyInput, which then forwards it to the input element.

LANGUAGE: javascript
CODE:
const FormField = forwardRef(function FormField(props, ref) {
  // ...
  return (
    <>
      <MyInput ref={ref} />
      ...
    </>
  );
});

----------------------------------------

TITLE: Caching Expensive Calculations with useMemo
DESCRIPTION: Demonstrates using useMemo to cache expensive calculations instead of using Effects.

LANGUAGE: jsx
CODE:
function TodoList({ todos, filter }) {
  const [newTodo, setNewTodo] = useState('');
  const visibleTodos = useMemo(() => {
    // ✅ Does not re-run unless todos or filter change
    return getFilteredTodos(todos, filter);
  }, [todos, filter]);
  // ...
}

----------------------------------------

TITLE: Nesting React Components
DESCRIPTION: Shows how to compose React components by nesting them within other components using JSX syntax.

LANGUAGE: JavaScript
CODE:
export default function MyApp() {
  return (
    <div>
      <h1>Welcome to my app</h1>
      <MyButton />
    </div>
  );
}

----------------------------------------

TITLE: Importing and Declaring Lazy Components in React
DESCRIPTION: Shows how to import the lazy function from React and use it to declare a lazy-loaded component. This enables code splitting and on-demand loading of the component.

LANGUAGE: javascript
CODE:
import { lazy } from 'react';

const MarkdownPreview = lazy(() => import('./MarkdownPreview.js'));

----------------------------------------

TITLE: Streaming Data from Server to Client
DESCRIPTION: Example demonstrating how to stream data from a Server Component to a Client Component using the use API.

LANGUAGE: jsx
CODE:
export default function App() {
  const messagePromise = fetchMessage();
  return (
    <Suspense fallback={<p>waiting for message...</p>}>
      <Message messagePromise={messagePromise} />
    </Suspense>
  );
}

----------------------------------------

TITLE: Using useContext Hook in React
DESCRIPTION: Shows how to use the useContext Hook to access context in a React component. The example demonstrates reading a 'theme' value from ThemeContext in a Button component.

LANGUAGE: javascript
CODE:
function Button() {
  const theme = useContext(ThemeContext);
  // ...


----------------------------------------

TITLE: Updating Nested Arrays in React State with Immer
DESCRIPTION: Example of using Immer to update nested arrays in state more concisely by allowing "mutating" operations on a draft state.

LANGUAGE: JavaScript
CODE:
updateMyTodos(draft => {
  const artwork = draft.find(a => a.id === artworkId);
  artwork.seen = nextSeen;
});