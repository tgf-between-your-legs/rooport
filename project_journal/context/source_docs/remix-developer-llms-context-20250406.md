TITLE: Configuring Root Route with Document-Level Components in Remix
DESCRIPTION: This snippet demonstrates how to set up the root route in a Remix application, including the use of document-level components like Links, Meta, and Scripts. It also shows how to include global stylesheets and set up the basic HTML structure.

LANGUAGE: tsx
CODE:
import type { LinksFunction } from "@remix-run/node"; // or cloudflare/deno
import {
  Links,
  LiveReload,
  Meta,
  Outlet,
  Scripts,
  ScrollRestoration,
} from "@remix-run/react";

import globalStylesheetUrl from "./global-styles.css";

export const links: LinksFunction = () => {
  return [{ rel: "stylesheet", href: globalStylesheetUrl }];
};

export default function App() {
  return (
    <html lang="en">
      <head>
        <meta charSet="utf-8" />
        <meta
          name="viewport"
          content="width=device-width, initial-scale=1"
        />

        {/* All `meta` exports on all routes will render here */}
        <Meta />

        {/* All `link` exports on all routes will render here */}
        <Links />
      </head>
      <body>
        {/* Child routes render here */}
        <Outlet />

        {/* Manages scroll position for client-side transitions */}
        {/* If you use a nonce-based content security policy for scripts, you must provide the `nonce` prop. Otherwise, omit the nonce prop as shown here. */}
        <ScrollRestoration />

        {/* Script tags go here */}
        {/* If you use a nonce-based content security policy for scripts, you must provide the `nonce` prop. Otherwise, omit the nonce prop as shown here. */}
        <Scripts />

        {/* Sets up automatic reload when you change code */}
        {/* and only does anything during development */}
        {/* If you use a nonce-based content security policy for scripts, you must provide the `nonce` prop. Otherwise, omit the nonce prop as shown here. */}
        <LiveReload />
      </body>
    </html>
  );
}

----------------------------------------

TITLE: Implementing User Session Validation in Remix
DESCRIPTION: This snippet demonstrates how to create a function that validates user sessions for protecting routes in Remix. It uses cookie-based session storage and redirects to login if no valid session is found.

LANGUAGE: typescript
CODE:
import {
  createCookieSessionStorage,
  redirect,
} from "@remix-run/node"; // or cloudflare/deno

// somewhere you've got a session storage
const { getSession } = createCookieSessionStorage();

export async function requireUserSession(request) {
  // get the session
  const cookie = request.headers.get("cookie");
  const session = await getSession(cookie);

  // validate the session, `userId` is just an example, use whatever value you
  // put in the session when the user authenticated
  if (!session.has("userId")) {
    // if there is no user session, redirect to login
    throw redirect("/login");
  }

  return session;
}

----------------------------------------

TITLE: Defining Route Module Exports in Remix
DESCRIPTION: This snippet shows the basic structure of a Remix route module with loader, component, and action exports. It demonstrates the three main parts of a route file that handle data loading, UI rendering, and data updates.

LANGUAGE: tsx
CODE:
export async function loader() {
  // provides data to the component
}

export default function Component() {
  // renders the UI
}

export async function action() {
  // updates persistent data
}

----------------------------------------

TITLE: Basic Remix Configuration Structure
DESCRIPTION: Basic configuration example showing the main options available in remix.config.js including app directory settings, assets configuration, and custom route definitions.

LANGUAGE: javascript
CODE:
/** @type {import('@remix-run/dev').AppConfig} */
module.exports = {
  appDirectory: "app",
  assetsBuildDirectory: "public/build",
  future: {
    /* any enabled future flags */
  },
  ignoredRouteFiles: ["**/*.css"],
  publicPath: "/build/",
  routes(defineRoutes) {
    return defineRoutes((route) => {
      route("/somewhere/cool/*", "catchall.tsx");
    });
  },
  serverBuildPath: "build/index.js",
};

----------------------------------------

TITLE: Implementing Form Validation Action in Remix TSX
DESCRIPTION: Shows how to implement a server-side action function that handles form validation for email and password fields, with error handling and redirection logic.

LANGUAGE: tsx
CODE:
import type { ActionFunctionArgs } from "@remix-run/node";
import { json, redirect } from "@remix-run/node";
import { Form } from "@remix-run/react";

export default function Signup() {
  // omitted for brevity
}

export async function action({
  request,
}: ActionFunctionArgs) {
  const formData = await request.formData();
  const email = String(formData.get("email"));
  const password = String(formData.get("password"));

  const errors = {};

  if (!email.includes("@")) {
    errors.email = "Invalid email address";
  }

  if (password.length < 12) {
    errors.password =
      "Password should be at least 12 characters";
  }

  if (Object.keys(errors).length > 0) {
    return json({ errors });
  }

  // Redirect to dashboard if validation is successful
  return redirect("/dashboard");
}

----------------------------------------

TITLE: Implementing BFF Pattern Loader Function in Remix TypeScript
DESCRIPTION: Demonstrates how to create a loader function that fetches data from an external API, authenticates using environment variables, and transforms the response data before sending to the client. Shows benefits of server-side processing including security, data pruning, and code optimization.

LANGUAGE: typescript
CODE:
import type { LoaderFunctionArgs } from "@remix-run/node"; // or cloudflare/deno
import { json } from "@remix-run/node"; // or cloudflare/deno
import escapeHtml from "escape-html";

export async function loader({
  request,
}: LoaderFunctionArgs) {
  const apiUrl = "http://api.example.com/some-data.json";
  const res = await fetch(apiUrl, {
    headers: {
      Authorization: `Bearer ${process.env.API_TOKEN}`,
    },
  });

  const data = await res.json();

  const prunedData = data.map((record) => {
    return {
      id: record.id,
      title: record.title,
      formattedBody: escapeHtml(record.content),
    };
  });
  return json(prunedData);
}

----------------------------------------

TITLE: Implementing Route Module with Server and Client Code in Remix
DESCRIPTION: Example of a complete route module showing server-side functions (loader, action, headers) and client-side component rendering. Demonstrates typical patterns for handling user data and form submissions in Remix.

LANGUAGE: tsx
CODE:
import type {
  ActionFunctionArgs,
  HeadersFunction,
  LoaderFunctionArgs,
} from "@remix-run/node"; // or cloudflare/deno
import { json } from "@remix-run/node"; // or cloudflare/deno
import { useLoaderData } from "@remix-run/react";

import { getUser, updateUser } from "../user";

export const headers: HeadersFunction = () => ({
  "Cache-Control": "max-age=300, s-maxage=3600",
});

export async function loader({
  request,
}: LoaderFunctionArgs) {
  const user = await getUser(request);
  return json({
    displayName: user.displayName,
    email: user.email,
  });
}

export default function Component() {
  const user = useLoaderData<typeof loader>();
  return (
    <Form action="/account">
      <h1>Settings for {user.displayName}</h1>

      <input
        name="displayName"
        defaultValue={user.displayName}
      />
      <input name="email" defaultValue={user.email} />

      <button type="submit">Save</button>
    </Form>
  );
}

export async function action({
  request,
}: ActionFunctionArgs) {
  const formData = await request.formData();
  const user = await getUser(request);

  await updateUser(user.id, {
    email: formData.get("email"),
    displayValue: formData.get("displayName"),
  });

  return json({ ok: true });
}

----------------------------------------

TITLE: Implementing Navigation Blocking with useBlocker in React Router
DESCRIPTION: This code snippet demonstrates how to use the useBlocker hook to prevent navigation when a form has unsaved changes. It shows how to conditionally render a confirmation dialog and handle proceed/cancel actions.

LANGUAGE: tsx
CODE:
function ImportantForm() {
  const [value, setValue] = React.useState("");

  // Block navigating elsewhere when data has been entered into the input
  const blocker = useBlocker(
    ({ currentLocation, nextLocation }) =>
      value !== "" &&
      currentLocation.pathname !== nextLocation.pathname
  );

  return (
    <Form method="post">
      <label>
        Enter some important data:
        <input
          name="data"
          value={value}
          onChange={(e) => setValue(e.target.value)}
        />
      </label>
      <button type="submit">Save</button>

      {blocker.state === "blocked" ? (
        <div>
          <p>Are you sure you want to leave?</p>
          <button onClick={() => blocker.proceed()}>
            Proceed
          </button>
          <button onClick={() => blocker.reset()}>
            Cancel
          </button>
        </div>
      ) : null}
    </Form>
  );
}

----------------------------------------

TITLE: Using Server and Client Loaders in Remix
DESCRIPTION: This example shows how to use both server and client loaders in a Remix route. The server loader fetches data from a database during SSR, while the client loader fetches data from an API during client-side navigation.

LANGUAGE: tsx
CODE:
export async function loader() {
  // During SSR, we talk to the DB directly
  const data = getServerDataFromDb();
  return json(data);
}

export async function clientLoader() {
  // During client-side navigations, we hit our exposed API endpoints directly
  const data = await fetchDataFromApi();
  return data;
}

export default function Component() {
  const data = useLoaderData<typeof loader>();
  return <>...</>;
}

----------------------------------------

TITLE: Implementing a Route Loader in Remix
DESCRIPTION: This code demonstrates how to create a loader function in a Remix route. It fetches user data and returns it as JSON, which will be available to the route component.

LANGUAGE: tsx
CODE:
import type { LoaderFunctionArgs } from "@remix-run/node"; // or cloudflare/deno
import { json } from "@remix-run/node"; // or cloudflare/deno

export async function loader({
  request,
}: LoaderFunctionArgs) {
  const user = await getUser(request);
  return json({
    displayName: user.displayName,
    email: user.email,
  });
}

export default function Component() {
  // ...
}

export async function action() {
  // ...
}

----------------------------------------

TITLE: Remix Route Module with Loader, Action, and Component
DESCRIPTION: This snippet showcases a complete Remix route module. It includes a loader for data fetching, an action for form handling, and a default export for the React component. It demonstrates how Remix combines server-side and client-side functionality in a single file.

LANGUAGE: tsx
CODE:
// Loaders only run on the server and provide data
// to your component on GET requests
export async function loader() {
  return json(await db.projects.findAll());
}

// The default export is the component that will be
// rendered when a route matches the URL. This runs
// both on the server and the client
export default function Projects() {
  const projects = useLoaderData<typeof loader>();
  const actionData = useActionData<typeof action>();

  return (
    <div>
      {projects.map((project) => (
        <Link key={project.slug} to={project.slug}>
          {project.title}
        </Link>
      ))}

      <Form method="post">
        <input name="title" />
        <button type="submit">Create New Project</button>
      </Form>
      {actionData?.errors ? (
        <ErrorMessages errors={actionData.errors} />
      ) : null}

      {/* outlets render the nested child routes
          that match the URL deeper than this route,
          allowing each layout to co-locate the UI and
          controller code in the same file */}
      <Outlet />
    </div>
  );
}

// Actions only run on the server and handle POST
// PUT, PATCH, and DELETE. They can also provide data
// to the component
export async function action({
  request,
}: ActionFunctionArgs) {
  const form = await request.formData();
  const errors = validate(form);
  if (errors) {
    return json({ errors });
  }
  await createProject({ title: form.get("title") });
  return json({ ok: true });
}

----------------------------------------

TITLE: Creating Custom Database Session Storage in Remix
DESCRIPTION: This example shows how to create a custom session storage using a database in Remix. It implements the required CRUD operations for managing session data.

LANGUAGE: typescript
CODE:
import { createSessionStorage } from "@remix-run/node"; // or cloudflare/deno

function createDatabaseSessionStorage({
  cookie,
  host,
  port,
}) {
  // Configure your database client...
  const db = createDatabaseClient(host, port);

  return createSessionStorage({
    cookie,
    async createData(data, expires) {
      // `expires` is a Date after which the data should be considered
      // invalid. You could use it to invalidate the data somehow or
      // automatically purge this record from your database.
      const id = await db.insert(data);
      return id;
    },
    async readData(id) {
      return (await db.select(id)) || null;
    },
    async updateData(id, data, expires) {
      await db.update(id, data);
    },
    async deleteData(id) {
      await db.delete(id);
    },
  });
}

const { getSession, commitSession, destroySession } =
  createDatabaseSessionStorage({
    host: "localhost",
    port: 1234,
    cookie: {
      name: "__session",
      sameSite: "lax",
    },
  });

----------------------------------------

TITLE: Creating a Progressive Search Box in Remix (TSX)
DESCRIPTION: This snippet shows how to create a search box component in Remix that works without JavaScript and can be progressively enhanced. It demonstrates using the URL as the source of truth and adding pending UI without changing the fundamental design.

LANGUAGE: tsx
CODE:
export function SearchBox() {
  return (
    <Form method="get" action="/search">
      <input type="search" name="query" />
      <SearchIcon />
    </Form>
  );
}

LANGUAGE: tsx
CODE:
import { useNavigation } from "@remix-run/react";

export function SearchBox() {
  const navigation = useNavigation();
  const isSearching =
    navigation.location.pathname === "/search";

  return (
    <Form method="get" action="/search">
      <input type="search" name="query" />
      {isSearching ? <Spinner /> : <SearchIcon />}
    </Form>
  );
}

----------------------------------------

TITLE: Implementing Add to Cart Functionality in Remix (TSX)
DESCRIPTION: This snippet demonstrates a simple Add to Cart button implementation using Remix's Form component. It shows how the feature works without JavaScript and then how it can be enhanced with client-side behavior using useFetcher.

LANGUAGE: tsx
CODE:
export function AddToCart({ id }) {
  return (
    <Form method="post" action="/add-to-cart">
      <input type="hidden" name="id" value={id} />
      <button type="submit">Add To Cart</button>
    </Form>
  );
}

LANGUAGE: tsx
CODE:
import { useFetcher } from "@remix-run/react";

export function AddToCart({ id }) {
  const fetcher = useFetcher();

  return (
    <fetcher.Form method="post" action="/add-to-cart">
      <input name="id" value={id} />
      <button type="submit">
        {fetcher.state === "submitting"
          ? "Adding..."
          : "Add To Cart"}
      </button>
    </fetcher.Form>
  );
}

----------------------------------------

TITLE: Loader Function with Database Query in Remix (TypeScript)
DESCRIPTION: Illustrates a loader function that queries a database using Prisma ORM. It fetches user data and returns it as JSON, demonstrating how server-only code is excluded from the browser bundle.

LANGUAGE: tsx
CODE:
import { useLoaderData } from "@remix-run/react";

import { prisma } from "../db";

export async function loader() {
  return json(await prisma.user.findMany());
}

export default function Users() {
  const data = useLoaderData<typeof loader>();
  return (
    <ul>
      {data.map((user) => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
}

----------------------------------------

TITLE: Configuring Server Bundles with Vite Plugin in Remix
DESCRIPTION: Demonstrates how to configure the Remix Vite plugin to create separate server bundles for authenticated and unauthenticated routes. The serverBundles function analyzes the route branch to determine bundle assignment based on route path patterns.

LANGUAGE: typescript
CODE:
import { vitePlugin as remix } from "@remix-run/dev";
import { defineConfig } from "vite";

export default defineConfig({
  plugins: [
    remix({
      serverBundles: ({ branch }) => {
        const isAuthenticatedRoute = branch.some((route) =>
          route.id.split("/").includes("_authenticated")
        );

        return isAuthenticatedRoute
          ? "authenticated"
          : "unauthenticated";
      },
    }),
  ],
});

----------------------------------------

TITLE: Implementing Logout Functionality with Sessions in Remix
DESCRIPTION: This snippet demonstrates how to implement a logout route in Remix using sessions. It includes the action function to destroy the session and a simple logout form component.

LANGUAGE: tsx
CODE:
import { getSession, destroySession } from "../sessions";

export const action = async ({
  request,
}: ActionFunctionArgs) => {
  const session = await getSession(
    request.headers.get("Cookie")
  );
  return redirect("/login", {
    headers: {
      "Set-Cookie": await destroySession(session),
    },
  });
};

export default function LogoutRoute() {
  return (
    <>
      <p>Are you sure you want to log out?</p>
      <Form method="post">
        <button>Logout</button>
      </Form>
      <Link to="/">Never mind</Link>
    </>
  );
}

----------------------------------------

TITLE: Implementing Root Error Boundary in Remix
DESCRIPTION: Example showing how to create a root error boundary component in Remix. This component handles uncaught errors at the application root level and ensures proper rendering of Meta, Links, and Scripts components.

LANGUAGE: tsx
CODE:
export function ErrorBoundary() {
  const error = useRouteError();
  console.error(error);
  return (
    <html>
      <head>
        <title>Oh no!</title>
        <Meta />
        <Links />
      </head>
      <body>
        {/* add the UI you want your users to see */}
        <Scripts />
      </body>
    </html>
  );
}

----------------------------------------

TITLE: Canonical Link Meta Implementation
DESCRIPTION: Example demonstrating how to add canonical URL links using the meta function.

LANGUAGE: tsx
CODE:
export const meta: MetaFunction = () => {
  return [
    {
      tagName: "link",
      rel: "canonical",
      href: "https://remix.run",
    },
  ];
};

----------------------------------------

TITLE: Handling Multiple Forms in Remix Route
DESCRIPTION: This snippet demonstrates how to handle multiple forms in a single Remix route using the 'intent' field. It includes both the action function that processes different form submissions and the component rendering multiple forms.

LANGUAGE: typescript
CODE:
export async function action({
  request,
}: ActionFunctionArgs) {
  const formData = await request.formData();
  const intent = formData.get("intent");
  switch (intent) {
    case "update": {
      // do your update
      return updateProjectName(formData.get("name"));
    }
    case "delete": {
      // do your delete
      return deleteStuff(formData);
    }
    default: {
      throw new Error("Unexpected action");
    }
  }
}

export default function Projects() {
  const project = useLoaderData<typeof loader>();
  return (
    <>
      <h2>Update Project</h2>
      <Form method="post">
        <label>
          Project name:{" "}
          <input
            type="text"
            name="name"
            defaultValue={project.name}
          />
        </label>
        <button type="submit" name="intent" value="update">
          Update
        </button>
      </Form>

      <Form method="post">
        <button type="submit" name="intent" value="delete">
          Delete
        </button>
      </Form>
    </>
  );
}

----------------------------------------

TITLE: Defining Root Layout in Remix
DESCRIPTION: This code snippet demonstrates how to create a root layout component in Remix. It includes essential Remix components for handling links, meta tags, scripts, and rendering child routes.

LANGUAGE: tsx
CODE:
import {
  Links,
  Meta,
  Outlet,
  Scripts,
  ScrollRestoration,
} from "@remix-run/react";

export default function Root() {
  return (
    <html lang="en">
      <head>
        <Links />
        <Meta />
      </head>
      <body>
        <Outlet />
        <ScrollRestoration />
        <Scripts />
      </body>
    </html>
  );
}

----------------------------------------

TITLE: Accessing Request Object in Remix Loader (TypeScript)
DESCRIPTION: Shows how to use the request object in a loader to read headers and URL search parameters. This is useful for accessing cookies and query string data.

LANGUAGE: tsx
CODE:
export async function loader({
  request,
}: LoaderFunctionArgs) {
  // read a cookie
  const cookie = request.headers.get("Cookie");

  // parse the search params for `?q=`
  const url = new URL(request.url);
  const query = url.searchParams.get("q");
}

----------------------------------------

TITLE: Extended Remix Vite Plugin Configuration
DESCRIPTION: Comprehensive example showing various configuration options for the Remix Vite plugin, including basename, build directory, future flags, route ignoring, and custom routing.

LANGUAGE: javascript
CODE:
import { vitePlugin as remix } from "@remix-run/dev";
import { defineConfig } from "vite";

export default defineConfig({
  plugins: [
    remix({
      basename: "/",
      buildDirectory: "build",
      future: {
        /* any enabled future flags */
      },
      ignoredRouteFiles: ["**/*.css"],
      routes(defineRoutes) {
        return defineRoutes((route) => {
          route("/somewhere/cool/*", "catchall.tsx");
        });
      },
      serverBuildFile: "index.js",
    }),
  ],
});

----------------------------------------

TITLE: Implementing City Search Combobox with Remix
DESCRIPTION: Example implementation of a city search combobox component using Remix's useFetcher hook for handling network requests. Demonstrates automatic network management for rapid, consecutive search queries.

LANGUAGE: tsx
CODE:
import type { LoaderFunctionArgs } from "@remix-run/node"; // or cloudflare/deno
import { json } from "@remix-run/node"; // or cloudflare/deno

export async function loader({
  request,
}: LoaderFunctionArgs) {
  const { searchParams } = new URL(request.url);
  const cities = await searchCities(searchParams.get("q"));
  return json(cities);
}

export function CitySearchCombobox() {
  const fetcher = useFetcher<typeof loader>();

  return (
    <fetcher.Form action="/city-search">
      <Combobox aria-label="Cities">
        <ComboboxInput
          name="q"
          onChange={(event) =>
            // submit the form onChange to get the list of cities
            fetcher.submit(event.target.form)
          }
        />

        {/* render with the loader's data */}
        {fetcher.data ? (
          <ComboboxPopover className="shadow-popup">
            {fetcher.data.length > 0 ? (
              <ComboboxList>
                {fetcher.data.map((city) => (
                  <ComboboxOption
                    key={city.id}
                    value={city.name}
                  />
                ))}
              </ComboboxList>
            ) : (
              <span>No results found</span>
            )}
          </ComboboxPopover>
        ) : null}
      </Combobox>
    </fetcher.Form>
  );
}