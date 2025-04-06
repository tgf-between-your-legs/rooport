TITLE: Loading Page Data in SvelteKit
DESCRIPTION: Defines a load function in +page.js to fetch data for a page component. The data is then available to the page via the data prop.

LANGUAGE: javascript
CODE:
/// file: src/routes/blog/[slug]/+page.js
/** @type {import('./$types').PageLoad} */
export function load({ params }) {
	return {
		post: {
			title: `Title for ${params.slug} goes here`,
			content: `Content for ${params.slug} goes here`
		}
	};
}

LANGUAGE: svelte
CODE:
<!--- file: src/routes/blog/[slug]/+page.svelte --->
<script>
	/** @type {import('./$types').PageProps} */
	let { data } = $props();
</script>

<h1>{data.post.title}</h1>
<div>{@html data.post.content}</div>

----------------------------------------

TITLE: Implementing Form Action Logic in SvelteKit
DESCRIPTION: Demonstrates a complete implementation of form actions including form data processing, database interaction, and returning action results.

LANGUAGE: javascript
CODE:
/// file: src/routes/login/+page.server.js
import * as db from '$lib/server/db';

/** @type {import('./$types').PageServerLoad} */
export async function load({ cookies }) {
	const user = await db.getUserFromSession(cookies.get('sessionid'));
	return { user };
}

/** @satisfies {import('./$types').Actions} */
export const actions = {
	login: async ({ cookies, request }) => {
		const data = await request.formData();
		const email = data.get('email');
		const password = data.get('password');

		const user = await db.getUser(email);
		cookies.set('sessionid', await db.createSession(user), { path: '/' });

		return { success: true };
	},
	register: async (event) => {
		// TODO register the user
	}
};

----------------------------------------

TITLE: Basic Page Component Implementation in Svelte
DESCRIPTION: Demonstrates creating basic page components using +page.svelte files for home and about pages with navigation links between them.

LANGUAGE: svelte
CODE:
<!--- file: src/routes/+page.svelte --->
<h1>Hello and welcome to my site!</h1>
<a href="/about">About my site</a>

LANGUAGE: svelte
CODE:
<!--- file: src/routes/about/+page.svelte --->
<h1>About this site</h1>
<p>TODO...</p>
<a href="/">Home</a>

----------------------------------------

TITLE: Implementing Server-Side Handle Hook in SvelteKit
DESCRIPTION: This snippet demonstrates how to implement the 'handle' hook in SvelteKit for server-side request handling. It shows how to customize responses or bypass SvelteKit for specific routes.

LANGUAGE: javascript
CODE:
/// file: src/hooks.server.js
/** @type {import('@sveltejs/kit').Handle} */
export async function handle({ event, resolve }) {
	if (event.url.pathname.startsWith('/custom')) {
		return new Response('custom response');
	}

	const response = await resolve(event);
	return response;
}

----------------------------------------

TITLE: Initializing SvelteKit Project via CLI
DESCRIPTION: Commands to create a new SvelteKit project, install dependencies, and start the development server. The server will run on localhost:5173 after setup.

LANGUAGE: bash
CODE:
npx sv create my-app
cd my-app
npm install
npm run dev

----------------------------------------

TITLE: Configuring SvelteKit with Adapter in JavaScript
DESCRIPTION: Demonstrates the basic structure of a svelte.config.js file, showing how to import and configure an adapter for SvelteKit. The configuration includes TypeScript type declarations and the main configuration object with adapter setup.

LANGUAGE: javascript
CODE:
/// file: svelte.config.js
// @filename: ambient.d.ts
declare module '@sveltejs/adapter-auto' {
	const plugin: () => import('@sveltejs/kit').Adapter;
	export default plugin;
}

// @filename: index.js
// ---cut---
import adapter from '@sveltejs/adapter-auto';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	kit: {
		adapter: adapter()
	}
};

export default config;

----------------------------------------

TITLE: Implementing Form Validation in SvelteKit Actions
DESCRIPTION: Demonstrates how to implement form validation in SvelteKit actions using the fail function to return validation errors and previously submitted form values.

LANGUAGE: javascript
CODE:
/// file: src/routes/login/+page.server.js
import { fail } from '@sveltejs/kit';
import * as db from '$lib/server/db';

/** @satisfies {import('./$types').Actions} */
export const actions = {
	login: async ({ cookies, request }) => {
		const data = await request.formData();
		const email = data.get('email');
		const password = data.get('password');

		if (!email) {
			return fail(400, { email, missing: true });
		}

		const user = await db.getUser(email);

		if (!user || user.password !== db.hash(password)) {
			return fail(400, { email, incorrect: true });
		}

		cookies.set('sessionid', await db.createSession(user), { path: '/' });

		return { success: true };
	},
	register: async (event) => {
		// TODO register the user
	}
};

----------------------------------------

TITLE: Server-side Page Data Loading in SvelteKit
DESCRIPTION: Demonstrates a server-side load function in +page.server.js that fetches data from a database. This function only runs on the server and can access private resources.

LANGUAGE: javascript
CODE:
/// file: src/routes/blog/[slug]/+page.server.js
import * as db from '$lib/server/database';

/** @type {import('./$types').PageServerLoad} */
export async function load({ params }) {
	return {
		post: await db.getPost(params.slug)
	};
}

----------------------------------------

TITLE: Displaying Validation Errors in Svelte Form
DESCRIPTION: Shows how to display validation errors returned from a form action in a Svelte component, including error messages and preserving form values.

LANGUAGE: svelte
CODE:
/// file: src/routes/login/+page.svelte
<form method="POST" action="?/login">
	{#if form?.missing}<p class="error">The email field is required</p>{/if}
	{#if form?.incorrect}<p class="error">Invalid credentials!</p>{/if}
	<label>
		Email
		<input name="email" type="email" value={form?.email ?? ''}>
	</label>
	<label>
		Password
		<input name="password" type="password">
	</label>
	<button>Log in</button>
	<button formaction="?/register">Register</button>
</form>

----------------------------------------

TITLE: Defining Default Form Action in SvelteKit
DESCRIPTION: Shows how to define a default form action in a +page.server.js file. This action will handle POST requests from forms without a specific action attribute.

LANGUAGE: javascript
CODE:
/// file: src/routes/login/+page.server.js
/** @satisfies {import('./$types').Actions} */
export const actions = {
	default: async (event) => {
		// TODO log the user in
	}
};

----------------------------------------

TITLE: Using Progressive Enhancement with use:enhance in Svelte
DESCRIPTION: Shows how to use the use:enhance directive in Svelte to progressively enhance form submissions without full page reloads.

LANGUAGE: svelte
CODE:
/// file: src/routes/login/+page.svelte
<script>
	import { enhance } from '$app/forms';

	/** @type {import('./$types').PageProps} */
	let { form } = $props();
</script>

<form method="POST" use:enhance>
	<!-- form content -->
</form>

----------------------------------------

TITLE: Correct Load Function Implementation
DESCRIPTION: Demonstrates the proper way to handle data in a load function by returning it instead of setting global state.

LANGUAGE: javascript
CODE:
/** @type {import('./$types').PageServerLoad} */
export async function load({ fetch }) {
	const response = await fetch('/api/user');

	return {
		user: await response.json()
	};
}

----------------------------------------

TITLE: Implementing Custom SvelteKit Adapter in JavaScript
DESCRIPTION: This code snippet demonstrates the structure and required methods for creating a custom SvelteKit adapter. It includes the main adapter function, the 'adapt' method for building, an optional 'emulate' method for development and preview, and a 'supports' object for handling file system operations.

LANGUAGE: javascript
CODE:
/** @param {AdapterSpecificOptions} options */
export default function (options) {
	/** @type {import('@sveltejs/kit').Adapter} */
	const adapter = {
		name: 'adapter-package-name',
		async adapt(builder) {
			// adapter implementation
		},
		async emulate() {
			return {
				async platform({ config, prerender }) {
					// the returned object becomes `event.platform` during dev, build and
					// preview. Its shape is that of `App.Platform`
				}
			}
		},
		supports: {
			read: ({ config, route }) => {
				// Return `true` if the route with the given `config` can use `read`
				// from `$app/server` in production, return `false` if it can't.
				// Or throw a descriptive error describing how to configure the deployment
			}
		}
	};

	return adapter;
}

----------------------------------------

TITLE: Layout Data Loading in SvelteKit
DESCRIPTION: Shows how to load data for a layout component using +layout.server.js. The loaded data is available to child components.

LANGUAGE: javascript
CODE:
/// file: src/routes/blog/[slug]/+layout.server.js
import * as db from '$lib/server/database';

/** @type {import('./$types').LayoutServerLoad} */
export async function load() {
	return {
		posts: await db.getPostSummaries()
	};
}

LANGUAGE: svelte
CODE:
<!--- file: src/routes/blog/[slug]/+layout.svelte --->
<script>
	/** @type {import('./$types').LayoutProps} */
	let { data, children } = $props();
</script>

<main>
	<!-- +page.svelte is `@render`ed here -->
	{@render children()}
</main>

<aside>
	<h2>More posts</h2>
	<ul>
		{#each data.posts as post}
			<li>
				<a href="/blog/{post.slug}">
					{post.title}
				</a>
			</li>
		{/each}
	</ul>
</aside>

----------------------------------------

TITLE: Setting Page Title in Svelte Component
DESCRIPTION: Demonstrates how to set a unique, descriptive title for each page in a SvelteKit application using the <svelte:head> element. This is important for route announcements and SEO.

LANGUAGE: svelte
CODE:
<svelte:head>
	<title>Todo List</title>
</svelte:head>

----------------------------------------

TITLE: Configuring SvelteKit Adapter in JavaScript
DESCRIPTION: Demonstrates how to configure a SvelteKit adapter in the svelte.config.js file. The code shows the basic structure for importing and configuring an adapter with custom options. This configuration is essential for preparing the app for deployment to specific platforms.

LANGUAGE: javascript
CODE:
import adapter from 'svelte-adapter-foo';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	kit: {
		adapter: adapter({
			// adapter options go here
		})
	}
};

export default config;

----------------------------------------

TITLE: Implementing handleFetch Hook for Server-Side Fetch Requests in SvelteKit
DESCRIPTION: This snippet demonstrates the implementation of the 'handleFetch' hook in SvelteKit, allowing modification of fetch requests made inside server-side load or action functions.

LANGUAGE: javascript
CODE:
/// file: src/hooks.server.js
/** @type {import('@sveltejs/kit').HandleFetch} */
export async function handleFetch({ request, fetch }) {
	if (request.url.startsWith('https://api.yourapp.com/')) {
		request = new Request(
			request.url.replace('https://api.yourapp.com/', 'http://localhost:9999/'),
			request
		);
	}

	return fetch(request);
}

----------------------------------------

TITLE: Error Handling in SvelteKit Load Functions
DESCRIPTION: Shows how to handle errors in load functions using the error helper from @sveltejs/kit.

LANGUAGE: javascript
CODE:
/// file: src/routes/admin/+layout.server.js
import { error } from '@sveltejs/kit';

/** @type {import('./$types').LayoutServerLoad} */
export function load({ locals }) {
	if (!locals.user) {
		error(401, 'not logged in');
	}

	if (!locals.user.isAdmin) {
		error(403, 'not an admin');
	}
}

----------------------------------------

TITLE: Implementing handleError Hook for Error Handling in SvelteKit
DESCRIPTION: This example shows how to implement the 'handleError' hook in SvelteKit for custom error handling and logging, including integration with error tracking services like Sentry.

LANGUAGE: javascript
CODE:
/// file: src/hooks.server.js
import * as Sentry from '@sentry/sveltekit';

Sentry.init({/*...*/})

/** @type {import('@sveltejs/kit').HandleServerError} */
export async function handleError({ error, event, status, message }) {
	const errorId = crypto.randomUUID();

	Sentry.captureException(error, {
		extra: { event, errorId, status }
	});

	return {
		message: 'Whoops!',
		errorId
	};
}

----------------------------------------

TITLE: Throwing Expected Errors in SvelteKit Page Load Function
DESCRIPTION: This snippet demonstrates how to throw an expected error using the 'error' helper from '@sveltejs/kit' in a page server load function. It checks if a post exists and throws a 404 error if not found.

LANGUAGE: javascript
CODE:
import { error } from '@sveltejs/kit';
import * as db from '$lib/server/database';

/** @type {import('./$types').PageServerLoad} */
export async function load({ params }) {
	const post = await db.getPost(params.slug);

	if (!post) {
		error(404, {
			message: 'Not found'
		});
	}

	return { post };
}

----------------------------------------

TITLE: Configuring Prerender Option in SvelteKit
DESCRIPTION: Enables or disables prerendering for routes. Can be set to true, false, or 'auto'. When true, the route will be prerendered at build time.

LANGUAGE: javascript
CODE:
export const prerender = true;

----------------------------------------

TITLE: Dynamic Page Loading with Parameters
DESCRIPTION: Shows how to implement dynamic page loading using +page.js for blog posts with error handling

LANGUAGE: javascript
CODE:
/// file: src/routes/blog/[slug]/+page.js
import { error } from '@sveltejs/kit';

/** @type {import('./$types').PageLoad} */
export function load({ params }) {
	if (params.slug === 'hello-world') {
		return {
			title: 'Hello world!',
			content: 'Welcome to our blog. Lorem ipsum dolor sit amet...'
		};
	}

	error(404, 'Not found');
}

----------------------------------------

TITLE: Custom Express Server Integration
DESCRIPTION: Example of creating a custom server using Express with SvelteKit's handler, including a separate healthcheck endpoint.

LANGUAGE: javascript
CODE:
import { handler } from './build/handler.js';
import express from 'express';

const app = express();

// add a route that lives separately from the SvelteKit app
app.get('/healthcheck', (req, res) => {
	res.end('ok');
});

// let SvelteKit handle everything else, including serving prerendered pages and static assets
app.use(handler);

app.listen(3000, () => {
	console.log('listening on port 3000');
});

----------------------------------------

TITLE: Adding Custom Data to Request with Locals in SvelteKit
DESCRIPTION: This example shows how to use the 'locals' object in SvelteKit to add custom data to the request, which can be accessed in handlers and server-side load functions.

LANGUAGE: javascript
CODE:
/// file: src/hooks.server.js
/** @type {import('@sveltejs/kit').Handle} */
export async function handle({ event, resolve }) {
	event.locals.user = await getUserInformation(event.cookies.get('sessionid'));

	const response = await resolve(event);

	response.headers.set('x-custom-header', 'potato');

	return response;
}

----------------------------------------

TITLE: Handling Headers with Fetch API in SvelteKit Server Route
DESCRIPTION: Demonstrates how to work with request and response headers in a SvelteKit server route. Shows logging request headers and creating a JSON response with custom headers using the user-agent information.

LANGUAGE: javascript
CODE:
import { json } from '@sveltejs/kit';

/** @type {import('./$types').RequestHandler} */
export function GET({ request }) {
	// log all headers
	console.log(...request.headers);

	// create a JSON Response using a header we received
	return json({
		// retrieve a specific header
		userAgent: request.headers.get('user-agent')
	}, {
		// set a header on the response
		headers: { 'x-custom-header': 'potato' }
	});
}

----------------------------------------

TITLE: Making Fetch Requests in SvelteKit Load Functions
DESCRIPTION: Shows how to use the provided fetch function to make API requests within a load function.

LANGUAGE: javascript
CODE:
/// file: src/routes/items/[id]/+page.js
/** @type {import('./$types').PageLoad} */
export async function load({ fetch, params }) {
	const res = await fetch(`/api/items/${params.id}`);
	const item = await res.json();

	return { item };
}

----------------------------------------

TITLE: Implementing Redirects in SvelteKit Form Actions
DESCRIPTION: Demonstrates how to implement redirects in SvelteKit form actions using the redirect function from @sveltejs/kit.

LANGUAGE: javascript
CODE:
// @errors: 2345
/// file: src/routes/login/+page.server.js
import { fail, redirect } from '@sveltejs/kit';
import * as db from '$lib/server/db';

/** @satisfies {import('./$types').Actions} */
export const actions = {
	login: async ({ cookies, request, url }) => {
		const data = await request.formData();
		const email = data.get('email');
		const password = data.get('password');

		const user = await db.getUser(email);
		if (!user) {
			return fail(400, { email, missing: true });
		}

		if (user.password !== db.hash(password)) {
			return fail(400, { email, incorrect: true });
		}

		cookies.set('sessionid', await db.createSession(user), { path: '/' });

		if (url.searchParams.has('redirectTo')) {
			redirect(303, url.searchParams.get('redirectTo'));
		}

		return { success: true };
	},
	register: async (event) => {
		// TODO register the user
	}
};

----------------------------------------

TITLE: Implementing Offline-Capable Service Worker
DESCRIPTION: Complete implementation of a service worker that caches built app assets and static files eagerly, while caching other requests as they occur. Enables offline functionality for previously visited pages.

LANGUAGE: javascript
CODE:
// @errors: 2339
/// <reference types="@sveltejs/kit" />
import { build, files, version } from '$service-worker';

const CACHE = `cache-${version}`;

const ASSETS = [
	...build,
	...files
];

self.addEventListener('install', (event) => {
	async function addFilesToCache() {
		const cache = await caches.open(CACHE);
		await cache.addAll(ASSETS);
	}

	event.waitUntil(addFilesToCache());
});

self.addEventListener('activate', (event) => {
	async function deleteOldCaches() {
		for (const key of await caches.keys()) {
			if (key !== CACHE) await caches.delete(key);
		}
	}

	event.waitUntil(deleteOldCaches());
});

self.addEventListener('fetch', (event) => {
	if (event.request.method !== 'GET') return;

	async function respond() {
		const url = new URL(event.request.url);
		const cache = await caches.open(CACHE);

		if (ASSETS.includes(url.pathname)) {
			const response = await cache.match(url.pathname);

			if (response) {
				return response;
			}
		}

		try {
			const response = await fetch(event.request);

			if (!(response instanceof Response)) {
				throw new Error('invalid response from fetch');
			}

			if (response.status === 200) {
				cache.put(event.request, response.clone());
			}

			return response;
		} catch (err) {
			const response = await cache.match(event.request);

			if (response) {
				return response;
			}

			throw err;
		}
	}

	event.respondWith(respond());
});

----------------------------------------

TITLE: Redirects in SvelteKit Load Functions
DESCRIPTION: Demonstrates how to perform redirects in load functions using the redirect helper from @sveltejs/kit.

LANGUAGE: javascript
CODE:
/// file: src/routes/user/+layout.server.js
import { redirect } from '@sveltejs/kit';

/** @type {import('./$types').LayoutServerLoad} */
export function load({ locals }) {
	if (!locals.user) {
		redirect(307, '/login');
	}
}

----------------------------------------

TITLE: Defining Named Form Actions in SvelteKit
DESCRIPTION: Illustrates how to define multiple named actions in a +page.server.js file. This allows for different actions to be triggered based on the form's action attribute.

LANGUAGE: javascript
CODE:
/// file: src/routes/login/+page.server.js
/** @satisfies {import('./$types').Actions} */
export const actions = {
	login: async (event) => {
		// TODO log the user in
	},
	register: async (event) => {
		// TODO register the user
	}
};

----------------------------------------

TITLE: Configuring SvelteKit for Cloudflare Pages Deployment
DESCRIPTION: This snippet shows how to configure the svelte.config.js file to use the Cloudflare adapter. It includes options for customizing routes and platform proxy settings.

LANGUAGE: javascript
CODE:
// @errors: 2307
/// file: svelte.config.js
import adapter from '@sveltejs/adapter-cloudflare';

export default {
	kit: {
		adapter: adapter({
			// See below for an explanation of these options
			routes: {
				include: ['/*'],
				exclude: ['<all>']
			},
			platformProxy: {
				configPath: undefined,
				environment: undefined,
				persist: undefined
			}
		})
	}
};

----------------------------------------

TITLE: Context-Based State Management in SvelteKit Layout
DESCRIPTION: Shows how to properly manage state using Svelte's context API in a layout component.

LANGUAGE: svelte
CODE:
<script>
	import { setContext } from 'svelte';

	/** @type {import('./$types').LayoutProps} */
	let { data } = $props();

	// Pass a function referencing our state
	// to the context for child components to access
	setContext('user', () => data.user);
</script>

----------------------------------------

TITLE: Configuring SvelteKit Node Adapter
DESCRIPTION: Basic configuration for setting up adapter-node in a SvelteKit project's svelte.config.js file.

LANGUAGE: javascript
CODE:
import adapter from '@sveltejs/adapter-node';

export default {
	kit: {
		adapter: adapter()
	}
};

----------------------------------------

TITLE: Configuring SvelteKit Vercel Adapter
DESCRIPTION: Basic setup for adapter-vercel in svelte.config.js file. Shows how to initialize and configure the Vercel adapter with optional settings.

LANGUAGE: javascript
CODE:
import adapter from '@sveltejs/adapter-vercel';

export default {
	kit: {
		adapter: adapter({
			// see below for options that can be set here
		})
	}
};

----------------------------------------

TITLE: Configuring adapter-static in SvelteKit
DESCRIPTION: Basic configuration setup for adapter-static in svelte.config.js showing default options including pages, assets, fallback, precompress and strict settings.

LANGUAGE: javascript
CODE:
import adapter from '@sveltejs/adapter-static';

export default {
	kit: {
		adapter: adapter({
			// default options are shown. On some platforms
			// these options are set automatically — see below
			pages: 'build',
			assets: 'build',
			fallback: undefined,
			precompress: false,
			strict: true
		})
	}
};

----------------------------------------

TITLE: Accessing Parent Data in SvelteKit Load Functions
DESCRIPTION: Demonstrates how to access data from a parent load function using await parent().

LANGUAGE: javascript
CODE:
/// file: src/routes/+layout.js
/** @type {import('./$types').LayoutLoad} */
export function load() {
	return { a: 1 };
}

LANGUAGE: javascript
CODE:
/// file: src/routes/abc/+layout.js
/** @type {import('./$types').LayoutLoad} */
export async function load({ parent }) {
	const { a } = await parent();
	return { b: a + 1 };
}

LANGUAGE: javascript
CODE:
/// file: src/routes/abc/+page.js
/** @type {import('./$types').PageLoad} */
export async function load({ parent }) {
	const { a, b } = await parent();
	return { c: a + b };
}

LANGUAGE: svelte
CODE:
<!--- file: src/routes/abc/+page.svelte --->
<script>
	/** @type {import('./$types').PageProps} */
	let { data } = $props();
</script>

<!-- renders `1 + 2 = 3` -->
<p>{data.a} + {data.b} = {data.c}</p>

----------------------------------------

TITLE: Displaying SvelteKit Project Structure in Bash
DESCRIPTION: This snippet shows the typical directory and file structure of a SvelteKit project, including the src directory, configuration files, and other common project files.

LANGUAGE: bash
CODE:
my-project/
├ src/
│ ├ lib/
│ │ ├ server/
│ │ │ └ [your server-only lib files]
│ │ └ [your lib files]
│ ├ params/
│ │ └ [your param matchers]
│ ├ routes/
│ │ └ [your routes]
│ ├ app.html
│ ├ error.html
│ ├ hooks.client.js
│ ├ hooks.server.js
│ └ service-worker.js
├ static/
│ └ [your static assets]
├ tests/
│ └ [your tests]
├ package.json
├ svelte.config.js
├ tsconfig.json
└ vite.config.js

----------------------------------------

TITLE: Defining RequestHandler Type for Route Parameters in SvelteKit (JavaScript)
DESCRIPTION: Demonstrates how to manually define types for route parameters in a SvelteKit RequestHandler. This approach is cumbersome and less portable.

LANGUAGE: javascript
CODE:
/** @type {import('@sveltejs/kit').RequestHandler<{
    foo: string;
    bar: string;
    baz: string
  }>} */
export async function GET({ params }) {
	// ...
}