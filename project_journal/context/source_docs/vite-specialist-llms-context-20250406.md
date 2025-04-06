TITLE: Installing Vite with Package Managers
DESCRIPTION: Commands for installing Vite using different package managers including npm, Yarn, pnpm, and Bun.

LANGUAGE: bash
CODE:
$ npm create vite@latest
$ yarn create vite
$ pnpm create vite
$ bun create vite

----------------------------------------

TITLE: Creating Vue Project with Vite
DESCRIPTION: Commands to scaffold a Vue.js project using Vite with different package managers.

LANGUAGE: bash
CODE:
# npm 7+, extra double-dash is needed:
$ npm create vite@latest my-vue-app -- --template vue
$ yarn create vite my-vue-app --template vue
$ pnpm create vite my-vue-app --template vue
$ bun create vite my-vue-app --template vue

----------------------------------------

TITLE: Basic Vite Configuration Structure
DESCRIPTION: The most basic Vite configuration file structure using ES modules syntax.

LANGUAGE: javascript
CODE:
export default {
  // config options
}

----------------------------------------

TITLE: Glob Importing in Vite
DESCRIPTION: Vite provides a special import.meta.glob function for importing multiple modules from the file system.

LANGUAGE: javascript
CODE:
const modules = import.meta.glob('./dir/*.js')

----------------------------------------

TITLE: Configuring Vite Plugins in JavaScript
DESCRIPTION: Example showing how to configure Vite and Rollup plugins in a vite.config.js file, including support for plugin presets.

LANGUAGE: javascript
CODE:
import vitePlugin from 'vite-plugin-feature'
import rollupPlugin from 'rollup-plugin-feature'

export default defineConfig({
  plugins: [vitePlugin(), rollupPlugin()],
})

----------------------------------------

TITLE: Virtual Modules Plugin Example
DESCRIPTION: Plugin implementation showing how to create virtual modules in Vite for passing build time information through ESM imports.

LANGUAGE: javascript
CODE:
export default function myPlugin() {
  const virtualModuleId = 'virtual:my-module'
  const resolvedVirtualModuleId = '\0' + virtualModuleId

  return {
    name: 'my-plugin',
    resolveId(id) {
      if (id === virtualModuleId) {
        return resolvedVirtualModuleId
      }
    },
    load(id) {
      if (id === resolvedVirtualModuleId) {
        return `export const msg = "from virtual module"`
      }
    },
  }
}

----------------------------------------

TITLE: Vite NPM Scripts Configuration
DESCRIPTION: Standard npm scripts configuration for a Vite project including development, build, and preview commands.

LANGUAGE: json
CODE:
{
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  }
}

----------------------------------------

TITLE: Setting up SSR dev server with Express and Vite
DESCRIPTION: This snippet demonstrates how to set up a development server for SSR using Express and Vite in middleware mode. It creates a Vite server instance and uses it as middleware in an Express application.

LANGUAGE: javascript
CODE:
import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import express from 'express'
import { createServer as createViteServer } from 'vite'

const __dirname = path.dirname(fileURLToPath(import.meta.url))

async function createServer() {
  const app = express()

  // Create Vite server in middleware mode and configure the app type as
  // 'custom', disabling Vite's own HTML serving logic so parent server
  // can take control
  const vite = await createViteServer({
    server: { middlewareMode: true },
    appType: 'custom'
  })

  // Use vite's connect instance as middleware. If you use your own
  // express router (express.Router()), you should use router.use
  // When the server restarts (for example after the user modifies
  // vite.config.js), `vite.middlewares` is still going to be the same
  // reference (with a new internal stack of Vite and plugin-injected
  // middlewares). The following is valid even after restarts.
  app.use(vite.middlewares)

  app.use('*', async (req, res) => {
    // serve index.html - we will tackle this next
  })

  app.listen(5173)
}

createServer()

----------------------------------------

TITLE: Accessing Environment Variables in JavaScript
DESCRIPTION: Demonstrates how Vite exposes environment variables with VITE_ prefix to client code while protecting sensitive variables.

LANGUAGE: javascript
CODE:
console.log(import.meta.env.VITE_SOME_KEY) // "123"
console.log(import.meta.env.DB_PASSWORD) // undefined

----------------------------------------

TITLE: Creating Vite Dev Server in TypeScript
DESCRIPTION: Example of creating and configuring a Vite dev server programmatically with TypeScript. Shows basic server setup with port configuration and CLI shortcuts.

LANGUAGE: typescript
CODE:
import { fileURLToPath } from 'node:url'
import { createServer } from 'vite'

const __dirname = fileURLToPath(new URL('.', import.meta.url))

const server = await createServer({
  configFile: false,
  root: __dirname,
  server: {
    port: 1337,
  },
})
await server.listen()

server.printUrls()
server.bindCLIShortcuts({ print: true })

----------------------------------------

TITLE: Configuring Rollup Build Options in Vite
DESCRIPTION: Example of customizing Vite's build configuration by adjusting Rollup options in the vite.config.js file.

LANGUAGE: javascript
CODE:
export default defineConfig({
  build: {
    rollupOptions: {
      // https://rollupjs.org/configuration-options/
    },
  },
})

----------------------------------------

TITLE: Multi-Page App Configuration in Vite
DESCRIPTION: Configuration for building a multi-page application with multiple HTML entry points using Vite.

LANGUAGE: javascript
CODE:
import { dirname, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'
import { defineConfig } from 'vite'

const __dirname = dirname(fileURLToPath(import.meta.url))

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        nested: resolve(__dirname, 'nested/index.html'),
      },
    },
  },
})

----------------------------------------

TITLE: Configuring SPA/MPA Environment in Vite
DESCRIPTION: Example configuration for a single-page or multi-page application in Vite. This configuration applies to the default 'client' environment.

LANGUAGE: javascript
CODE:
export default defineConfig({
  build: {
    sourcemap: false,
  },
  optimizeDeps: {
    include: ['lib'],
  },
})

----------------------------------------

TITLE: Configuring npm scripts for Vite build and preview
DESCRIPTION: Defines npm scripts for building and previewing a Vite project. The 'build' script runs the Vite build process, while 'preview' starts a local server to preview the built files.

LANGUAGE: json
CODE:
{
  "scripts": {
    "build": "vite build",
    "preview": "vite preview"
  }
}

----------------------------------------

TITLE: Self-accepting Module with HMR in JavaScript
DESCRIPTION: Demonstrates how to create a self-accepting module using `import.meta.hot.accept()`. The callback receives the updated module, allowing for handling of the hot update.

LANGUAGE: javascript
CODE:
export const count = 1

if (import.meta.hot) {
  import.meta.hot.accept((newModule) => {
    if (newModule) {
      // newModule is undefined when SyntaxError happened
      console.log('updated: count is now ', newModule.count)
    }
  })
}

----------------------------------------

TITLE: Resolving Bare Module Imports in JavaScript
DESCRIPTION: Vite detects and resolves bare module imports in source files, converting them to valid URLs that the browser can import.

LANGUAGE: javascript
CODE:
import { someMethod } from 'my-dep'

----------------------------------------

TITLE: Configuring Vite Warmup for Performance
DESCRIPTION: Shows how to configure Vite's server warmup feature to pre-transform frequently used files and improve loading performance.

LANGUAGE: javascript
CODE:
export default defineConfig({
  server: {
    warmup: {
      clientFiles: [
        './src/components/BigComponent.vue',
        './src/utils/big-utils.js',
      ],
    },
  },
})

----------------------------------------

TITLE: Creating a Workerd Environment Factory in TypeScript
DESCRIPTION: Demonstrates how to create an environment factory for Workerd, setting up default options and merging with user configurations. This factory can be used to create environments for both development and build phases.

LANGUAGE: typescript
CODE:
function createWorkerdEnvironment(
  userConfig: EnvironmentOptions,
): EnvironmentOptions {
  return mergeConfig(
    {
      resolve: {
        conditions: [
          /*...*/
        ],
      },
      dev: {
        createEnvironment(name, config) {
          return createWorkerdDevEnvironment(name, config, {
            hot: true,
            transport: customHotChannel(),
          })
        },
      },
      build: {
        createEnvironment(name, config) {
          return createWorkerdBuildEnvironment(name, config)
        },
      },
    },
    userConfig,
  )
}

----------------------------------------

TITLE: Importing CSS Modules in Vite
DESCRIPTION: Vite supports CSS Modules for files ending with .module.css, allowing import of CSS classes as objects.

LANGUAGE: javascript
CODE:
import classes from './example.module.css'
document.getElementById('foo').className = classes.red

----------------------------------------

TITLE: Configuring Global Constants in Vite
DESCRIPTION: Example of using defineConfig to set global constants that will be defined during dev and statically replaced during build using esbuild defines.

LANGUAGE: javascript
CODE:
export default defineConfig({
  define: {
    __APP_VERSION__: JSON.stringify('v1.0.0'),
    __API_URL__: 'window.__backend_api_url',
  },
})

----------------------------------------

TITLE: Dev Server Configuration Plugin
DESCRIPTION: Example showing how to configure the Vite dev server using the configureServer hook to add custom middleware.

LANGUAGE: javascript
CODE:
const myPlugin = () => ({
  name: 'configure-server',
  configureServer(server) {
    server.middlewares.use((req, res, next) => {
      // custom handle request...
    })
  },
})

----------------------------------------

TITLE: Importing Asset as URL in JavaScript
DESCRIPTION: Demonstrates how to import a static asset as a URL in JavaScript using Vite. The resolved public URL is returned when the asset is served.

LANGUAGE: javascript
CODE:
import imgUrl from './img.png'
document.getElementById('hero-img').src = imgUrl

----------------------------------------

TITLE: Configuring Legacy Browser Support Plugin in Vite
DESCRIPTION: This code demonstrates how to configure the @vitejs/plugin-legacy plugin in the vite.config.js file. It sets up legacy browser support targeting default browsers except IE 11.

LANGUAGE: javascript
CODE:
import legacy from '@vitejs/plugin-legacy'
import { defineConfig } from 'vite'

export default defineConfig({
  plugins: [
    legacy({
      targets: ['defaults', 'not IE 11'],
    }),
  ],
})

----------------------------------------

TITLE: Implementing server-rendered HTML handler
DESCRIPTION: This code snippet shows how to implement a catch-all route handler that serves server-rendered HTML. It reads the index.html template, applies Vite transformations, loads the server entry module, renders the app, and sends the final HTML to the client.

LANGUAGE: javascript
CODE:
app.use('*', async (req, res, next) => {
  const url = req.originalUrl

  try {
    // 1. Read index.html
    let template = fs.readFileSync(
      path.resolve(__dirname, 'index.html'),
      'utf-8',
    )

    // 2. Apply Vite HTML transforms. This injects the Vite HMR client,
    //    and also applies HTML transforms from Vite plugins, e.g. global
    //    preambles from @vitejs/plugin-react
    template = await vite.transformIndexHtml(url, template)

    // 3. Load the server entry. ssrLoadModule automatically transforms
    //    ESM source code to be usable in Node.js! There is no bundling
    //    required, and provides efficient invalidation similar to HMR.
    const { render } = await vite.ssrLoadModule('/src/entry-server.js')

    // 4. render the app HTML. This assumes entry-server.js's exported
    //     `render` function calls appropriate framework SSR APIs,
    //    e.g. ReactDOMServer.renderToString()
    const appHtml = await render(url)

    // 5. Inject the app-rendered HTML into the template.
    const html = template.replace(`<!--ssr-outlet-->`, () => appHtml)

    // 6. Send the rendered HTML back.
    res.status(200).set({ 'Content-Type': 'text/html' }).end(html)
  } catch (e) {
    // If an error is caught, let Vite fix the stack trace so it maps back
    // to your actual source code.
    vite.ssrFixStacktrace(e)
    next(e)
  }
})

----------------------------------------

TITLE: Library Build Configuration in Vite
DESCRIPTION: Configuration for building a library with single or multiple entry points and external dependencies.

LANGUAGE: javascript
CODE:
import { dirname, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'
import { defineConfig } from 'vite'

const __dirname = dirname(fileURLToPath(import.meta.url))

export default defineConfig({
  build: {
    lib: {
      entry: resolve(__dirname, 'lib/main.js'),
      name: 'MyLib',
      fileName: 'my-lib',
    },
    rollupOptions: {
      external: ['vue'],
      output: {
        globals: {
          vue: 'Vue',
        },
      },
    },
  },
})

----------------------------------------

TITLE: Accessing Vite Server Environments in JavaScript
DESCRIPTION: Demonstrates how to access and interact with environments in a Vite dev server, including transforming requests and accessing the module graph.

LANGUAGE: javascript
CODE:
// create the server, or get it from the configureServer hook
const server = await createServer(/* options */)

const environment = server.environments.client
environment.transformRequest(url)
console.log(server.environments.ssr.moduleGraph)

----------------------------------------

TITLE: Building Vite Project Programmatically
DESCRIPTION: Example of using Vite's build API to programmatically build a project with custom configuration.

LANGUAGE: typescript
CODE:
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { build } from 'vite'

const __dirname = fileURLToPath(new URL('.', import.meta.url))

await build({
  root: path.resolve(__dirname, './project'),
  base: '/foo/',
  build: {
    rollupOptions: {
      // ...
    },
  },
})

----------------------------------------

TITLE: Configuring Multiple Environments in Vite
DESCRIPTION: Example configuration for an application with multiple environments (client, server, and edge) in Vite. This demonstrates how to use the new 'environments' config option.

LANGUAGE: javascript
CODE:
export default {
  build: {
    sourcemap: false,
  },
  optimizeDeps: {
    include: ['lib'],
  },
  environments: {
    server: {},
    edge: {
      resolve: {
        noExternal: true,
      },
    },
  },
}

----------------------------------------

TITLE: Configuring Library Build Settings in Vite
DESCRIPTION: Demonstrates how to configure library build settings, including entry points, file naming, and CSS output in the Vite configuration.

LANGUAGE: javascript
CODE:
import { defineConfig } from 'vite'

export default defineConfig({
  build: {
    lib: {
      entry: ['src/main.js'],
      fileName: (format, entryName) => `my-lib-${entryName}.${format}.js`,
      cssFileName: 'my-lib-style',
    },
  },
})

----------------------------------------

TITLE: Using Environment Factory in Vite Configuration
DESCRIPTION: Shows how to use a custom environment factory in a Vite configuration file. This example sets up two environments (SSR and RSC) using the Workerd environment factory.

LANGUAGE: javascript
CODE:
import { createWorkerdEnvironment } from 'vite-environment-workerd'

export default {
  environments: {
    ssr: createWorkerdEnvironment({
      build: {
        outDir: '/dist/ssr',
      },
    }),
    rsc: createWorkerdEnvironment({
      build: {
        outDir: '/dist/rsc',
      },
    }),
  },
}

----------------------------------------

TITLE: Starting Vite Dev Server
DESCRIPTION: Command to start the Vite development server in the current directory. Supports various options for configuration including host, port, CORS, and other development settings.

LANGUAGE: bash
CODE:
vite [root]

----------------------------------------

TITLE: Configuring preview port for Vite app
DESCRIPTION: Shows how to set a custom port for the Vite preview server by modifying the npm script. This allows you to specify the port on which the preview server will run.

LANGUAGE: json
CODE:
{
  "scripts": {
    "preview": "vite preview --port 8080"
  }
}

----------------------------------------

TITLE: Configuring Server Proxy in Vite (JavaScript)
DESCRIPTION: Shows various examples of configuring proxy rules for the Vite development server, including string shortcuts, options with rewrite rules, RegExp patterns, and websocket proxying.

LANGUAGE: javascript
CODE:
export default defineConfig({
  server: {
    proxy: {
      // string shorthand:
      '/foo': 'http://localhost:4567',
      // with options:
      '/api': {
        target: 'http://jsonplaceholder.typicode.com',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ''),
      },
      // with RegExp:
      '^/fallback/.*': {
        target: 'http://jsonplaceholder.typicode.com',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/fallback/, ''),
      },
      // Using the proxy instance
      '/api': {
        target: 'http://jsonplaceholder.typicode.com',
        changeOrigin: true,
        configure: (proxy, options) => {
          // proxy will be an instance of 'http-proxy'
        },
      },
      // Proxying websockets or socket.io:
      '/socket.io': {
        target: 'ws://localhost:5174',
        ws: true,
        rewriteWsOrigin: true,
      },
    },
  },
})

----------------------------------------

TITLE: Advanced Base URL Configuration in Vite
DESCRIPTION: Implementation of advanced base URL handling for assets and public files during build.

LANGUAGE: typescript
CODE:
experimental: {
  renderBuiltUrl(filename, { hostType }) {
    if (hostType === 'js') {
      return { runtime: `window.__toCdnUrl(${JSON.stringify(filename)})` }
    } else {
      return { relative: true }
    }
  },
}

----------------------------------------

TITLE: Importing Script as Web Worker in JavaScript
DESCRIPTION: Shows various ways to import scripts as web workers using ?worker, ?sharedworker, and ?worker&inline suffixes in Vite.

LANGUAGE: javascript
CODE:
// Separate chunk in the production build
import Worker from './shader.js?worker'
const worker = new Worker()

// sharedworker
import SharedWorker from './shader.js?sharedworker'
const sharedWorker = new SharedWorker()

// Inlined as base64 strings
import InlineWorker from './shader.js?worker&inline'

----------------------------------------

TITLE: Conditional Guard for HMR API Usage in JavaScript
DESCRIPTION: Example of using a conditional guard to ensure HMR API code is only executed in development and can be tree-shaken in production.

LANGUAGE: javascript
CODE:
if (import.meta.hot) {
  // HMR code
}

----------------------------------------

TITLE: Implementing a Virtual Module Plugin for Runtime-Agnostic SSR in TypeScript
DESCRIPTION: This plugin creates a virtual module to handle index.html transformation in a runtime-agnostic manner. It demonstrates how to use Vite's plugin API to create and load virtual modules for SSR scenarios.

LANGUAGE: typescript
CODE:
function vitePluginVirtualIndexHtml(): Plugin {
  let server: ViteDevServer | undefined
  return {
    name: vitePluginVirtualIndexHtml.name,
    configureServer(server_) {
      server = server_
    },
    resolveId(source) {
      return source === 'virtual:index-html' ? '\0' + source : undefined
    },
    async load(id) {
      if (id === '\0' + 'virtual:index-html') {
        let html: string
        if (server) {
          this.addWatchFile('index.html')
          html = fs.readFileSync('index.html', 'utf-8')
          html = await server.transformIndexHtml('/', html)
        } else {
          html = fs.readFileSync('dist/client/index.html', 'utf-8')
        }
        return `export default ${JSON.stringify(html)}`
      }
      return
    },
  }
}

----------------------------------------

TITLE: Configuring Vite for Linked Dependencies
DESCRIPTION: Configuration example showing how to handle linked dependencies in a monorepo setup by including them in optimization and CommonJS options.

LANGUAGE: javascript
CODE:
export default defineConfig({
  optimizeDeps: {
    include: ['linked-dep'],
  },
  build: {
    commonjsOptions: {
      include: [/linked-dep/, /node_modules/],
    },
  },
})

----------------------------------------

TITLE: ModuleRunnerTransport Interface Definition in TypeScript
DESCRIPTION: Defines the interface for transport mechanisms used by ModuleRunner to communicate with the Vite server. It includes methods for connecting, disconnecting, sending data, and invoking remote procedures.

LANGUAGE: typescript
CODE:
interface ModuleRunnerTransport {
  connect?(handlers: ModuleRunnerTransportHandlers): Promise<void> | void
  disconnect?(): Promise<void> | void
  send?(data: HotPayload): Promise<void> | void
  invoke?(data: HotPayload): Promise<{ result: any } | { error: any }>
  timeout?: number
}

----------------------------------------

TITLE: Using hot.data for Persistent Data in HMR
DESCRIPTION: Demonstrates how to use `import.meta.hot.data` to persist data across different instances of the same updated module during hot module replacement.

LANGUAGE: javascript
CODE:
// ok
import.meta.hot.data.someValue = 'hello'

// not supported
import.meta.hot.data = { someValue: 'hello' }

----------------------------------------

TITLE: Applying Plugins Conditionally in Vite
DESCRIPTION: This code shows how to conditionally apply a plugin only during the build process in Vite. It uses the rollup-plugin-typescript2 as an example and sets it to apply only during 'build' using the 'apply' property.

LANGUAGE: javascript
CODE:
import typescript2 from 'rollup-plugin-typescript2'
import { defineConfig } from 'vite'

export default defineConfig({
  plugins: [
    {
      ...typescript2(),
      apply: 'build',
    },
  ],
})

----------------------------------------

TITLE: Creating a Custom Dev Environment for Workerd in TypeScript
DESCRIPTION: Illustrates how to create a custom development environment for Workerd. This example sets up a connection and transport mechanism for hot module replacement (HMR).

LANGUAGE: typescript
CODE:
import { DevEnvironment, HotChannel } from 'vite'

function createWorkerdDevEnvironment(
  name: string,
  config: ResolvedConfig,
  context: DevEnvironmentContext
) {
  const connection = /* ... */
  const transport: HotChannel = {
    on: (listener) => { connection.on('message', listener) },
    send: (data) => connection.send(data),
  }

  const workerdDevEnvironment = new DevEnvironment(name, config, {
    options: {
      resolve: { conditions: ['custom'] },
      ...context.options,
    },
    hot: true,
    transport,
  })
  return workerdDevEnvironment
}

----------------------------------------

TITLE: Accepting Updates from Dependencies in JavaScript
DESCRIPTION: Shows how a module can accept updates from its direct dependencies without reloading itself, using `import.meta.hot.accept()` with specified dependency paths.

LANGUAGE: javascript
CODE:
import { foo } from './foo.js'

foo()

if (import.meta.hot) {
  import.meta.hot.accept('./foo.js', (newFoo) => {
    // the callback receives the updated './foo.js' module
    newFoo?.foo()
  })

  // Can also accept an array of dep modules:
  import.meta.hot.accept(
    ['./foo.js', './bar.js'],
    ([newFooModule, newBarModule]) => {
      // The callback receives an array where only the updated module is
      // non null. If the update was not successful (syntax error for ex.),
      // the array is empty
    },
  )
}

----------------------------------------

TITLE: Defining RunnableDevEnvironment and ModuleRunner in TypeScript
DESCRIPTION: This snippet defines the RunnableDevEnvironment class and ModuleRunner interface, which are used for running modules in the same runtime as the Vite server. It includes methods for importing modules and checking environment compatibility.

LANGUAGE: typescript
CODE:
export class RunnableDevEnvironment extends DevEnvironment {
  public readonly runner: ModuleRunner
}

class ModuleRunner {
  /**
   * URL to execute.
   * Accepts file path, server path, or id relative to the root.
   * Returns an instantiated module (same as in ssrLoadModule)
   */
  public async import(url: string): Promise<Record<string, any>>
  /**
   * Other ModuleRunner methods...
   */
}

if (isRunnableDevEnvironment(server.environments.ssr)) {
  await server.environments.ssr.runner.import('/entry-point.js')
}