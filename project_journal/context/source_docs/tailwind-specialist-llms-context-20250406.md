TITLE: Running Next.js Development Server
DESCRIPTION: Commands to start the Next.js development server using various package managers. This allows developers to run the project locally for development and testing.

LANGUAGE: bash
CODE:
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev

----------------------------------------

TITLE: Advanced Directory Walking with WalkBuilder
DESCRIPTION: Advanced example showing how to customize directory walking behavior using WalkBuilder, specifically demonstrating how to include hidden files in the traversal.

LANGUAGE: rust
CODE:
use ignore::WalkBuilder;

for result in WalkBuilder::new("./").hidden(false).build() {
    println!("{:?}", result);
}

----------------------------------------

TITLE: Basic Directory Walking with Ignore
DESCRIPTION: Basic example of recursively traversing a directory while respecting ignore files like .gitignore and .ignore. Demonstrates error handling for each entry.

LANGUAGE: rust
CODE:
use ignore::Walk;

for result in Walk::new("./") {
    // Each item yielded by the iterator is either a directory entry or an
    // error, so either print the path or the error.
    match result {
        Ok(entry) => println!("{}", entry.path().display()),
        Err(err) => println!("ERROR: {}", err),
    }
}

----------------------------------------

TITLE: HTML Structure for TailwindCSS Project Header
DESCRIPTION: HTML markup for displaying the TailwindCSS project logo with dark/light mode support, project description, and status badges including build status, downloads, version, and license information.

LANGUAGE: HTML
CODE:
<p align="center">
  <a href="https://tailwindcss.com" target="_blank">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/tailwindlabs/tailwindcss/HEAD/.github/logo-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/tailwindlabs/tailwindcss/HEAD/.github/logo-light.svg">
      <img alt="Tailwind CSS" src="https://raw.githubusercontent.com/tailwindlabs/tailwindcss/HEAD/.github/logo-light.svg" width="350" height="70" style="max-width: 100%;">
    </picture>
  </a>
</p>

<p align="center">
  A utility-first CSS framework for rapidly building custom user interfaces.
</p>

<p align="center">
    <a href="https://github.com/tailwindlabs/tailwindcss/actions"><img src="https://img.shields.io/github/actions/workflow/status/tailwindlabs/tailwindcss/ci.yml?branch=next" alt="Build Status"></a>
    <a href="https://www.npmjs.com/package/tailwindcss"><img src="https://img.shields.io/npm/dt/tailwindcss.svg" alt="Total Downloads"></a>
    <a href="https://github.com/tailwindcss/tailwindcss/releases"><img src="https://img.shields.io/npm/v/tailwindcss.svg" alt="Latest Release"></a>
    <a href="https://github.com/tailwindcss/tailwindcss/blob/master/LICENSE"><img src="https://img.shields.io/npm/l/tailwindcss.svg" alt="License"></a>
</p>

----------------------------------------

TITLE: Installing Ignore Crate Dependencies
DESCRIPTION: Cargo dependency configuration for adding the ignore crate to a Rust project.

LANGUAGE: toml
CODE:
[dependencies]
ignore = "0.4"

----------------------------------------

TITLE: Displaying Project Description and Status Badges in HTML
DESCRIPTION: This HTML snippet shows the project description and various status badges for Tailwind CSS. It includes links to GitHub Actions, npm package, releases, and license information.

LANGUAGE: HTML
CODE:
<p align="center">
  A utility-first CSS framework for rapidly building custom user interfaces.
</p>

<p align="center">
    <a href="https://github.com/tailwindlabs/tailwindcss/actions"><img src="https://img.shields.io/github/actions/workflow/status/tailwindlabs/tailwindcss/ci.yml?branch=next" alt="Build Status"></a>
    <a href="https://www.npmjs.com/package/tailwindcss"><img src="https://img.shields.io/npm/dt/tailwindcss.svg" alt="Total Downloads"></a>
    <a href="https://github.com/tailwindcss/tailwindcss/releases"><img src="https://img.shields.io/npm/v/tailwindcss.svg" alt="Latest Release"></a>
    <a href="https://github.com/tailwindcss/tailwindcss/blob/master/LICENSE"><img src="https://img.shields.io/npm/l/tailwindcss.svg" alt="License"></a>
</p>

----------------------------------------

TITLE: Identifying Tailwind CSS Oxide Binary for Apple Silicon
DESCRIPTION: This markdown snippet identifies the specific binary package for Tailwind CSS Oxide that is compatible with ARM64 architecture on Apple's macOS (Darwin) operating system.

LANGUAGE: markdown
CODE:
# `@tailwindcss/oxide-darwin-arm64`

This is the **aarch64-apple-darwin** binary for `@tailwindcss/oxide`

----------------------------------------

TITLE: Describing Tailwind CSS Oxide Linux x64 musl Binary in Markdown
DESCRIPTION: This markdown snippet identifies the specific binary distribution for Tailwind CSS Oxide, targeting the x86_64-unknown-linux-musl platform. It provides essential information for users or developers working with this particular build of the Tailwind CSS tooling.

LANGUAGE: markdown
CODE:
# `@tailwindcss/oxide-linux-x64-musl`

This is the **x86_64-unknown-linux-musl** binary for `@tailwindcss/oxide`

----------------------------------------

TITLE: Package Name Definition in Markdown
DESCRIPTION: Defines the package name for the Linux x86_64 GNU binary distribution of Tailwind CSS Oxide.

LANGUAGE: markdown
CODE:
@tailwindcss/oxide-linux-x64-gnu

----------------------------------------

TITLE: Specifying Tailwind CSS Oxide Binary for FreeBSD x64 in Markdown
DESCRIPTION: This snippet defines the package name and describes the specific binary architecture for the Tailwind CSS Oxide package targeting FreeBSD x64 systems.

LANGUAGE: Markdown
CODE:
# `@tailwindcss/oxide-freebsd-x64`

This is the **x86_64-unknown-freebsd** binary for `@tailwindcss/oxide`

----------------------------------------

TITLE: Displaying Project Badges in HTML
DESCRIPTION: This HTML snippet displays various project badges for Tailwind CSS, including build status, total downloads, latest release, and license information. It uses inline SVG images from shields.io to show real-time data.

LANGUAGE: HTML
CODE:
<p align="center">
    <a href="https://github.com/tailwindlabs/tailwindcss/actions"><img src="https://img.shields.io/github/actions/workflow/status/tailwindlabs/tailwindcss/ci.yml?branch=next" alt="Build Status"></a>
    <a href="https://www.npmjs.com/package/tailwindcss"><img src="https://img.shields.io/npm/dt/tailwindcss.svg" alt="Total Downloads"></a>
    <a href="https://github.com/tailwindcss/tailwindcss/releases"><img src="https://img.shields.io/npm/v/tailwindcss.svg" alt="Latest Release"></a>
    <a href="https://github.com/tailwindcss/tailwindcss/blob/master/LICENSE"><img src="https://img.shields.io/npm/l/tailwindcss.svg" alt="License"></a>
</p>

----------------------------------------

TITLE: HTML Repository Header with Logo and Badges
DESCRIPTION: HTML markup for the repository header section including responsive logo display and status badges for build, downloads, version and license.

LANGUAGE: HTML
CODE:
<p align="center">
  <a href="https://tailwindcss.com" target="_blank">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/tailwindlabs/tailwindcss/HEAD/.github/logo-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/tailwindlabs/tailwindcss/HEAD/.github/logo-light.svg">
      <img alt="Tailwind CSS" src="https://raw.githubusercontent.com/tailwindlabs/tailwindcss/HEAD/.github/logo-light.svg" width="350" height="70" style="max-width: 100%;">
    </picture>
  </a>
</p>

<p align="center">
  A utility-first CSS framework for rapidly building custom user interfaces.
</p>

<p align="center">
    <a href="https://github.com/tailwindlabs/tailwindcss/actions"><img src="https://img.shields.io/github/actions/workflow/status/tailwindlabs/tailwindcss/ci.yml?branch=next" alt="Build Status"></a>
    <a href="https://www.npmjs.com/package/tailwindcss"><img src="https://img.shields.io/npm/dt/tailwindcss.svg" alt="Total Downloads"></a>
    <a href="https://github.com/tailwindcss/tailwindcss/releases"><img src="https://img.shields.io/npm/v/tailwindcss.svg" alt="Latest Release"></a>
    <a href="https://github.com/tailwindcss/tailwindcss/blob/master/LICENSE"><img src="https://img.shields.io/npm/l/tailwindcss.svg" alt="License"></a>
</p>

----------------------------------------

TITLE: HTML Logo and Badge Implementation for TailwindCSS
DESCRIPTION: HTML markup for displaying the TailwindCSS logo with dark/light mode support and project status badges. Includes responsive image handling and external links to various project resources.

LANGUAGE: HTML
CODE:
<p align="center">
  <a href="https://tailwindcss.com" target="_blank">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/tailwindlabs/tailwindcss/HEAD/.github/logo-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/tailwindlabs/tailwindcss/HEAD/.github/logo-light.svg">
      <img alt="Tailwind CSS" src="https://raw.githubusercontent.com/tailwindlabs/tailwindcss/HEAD/.github/logo-light.svg" width="350" height="70" style="max-width: 100%;">
    </picture>
  </a>
</p>

<p align="center">
  A utility-first CSS framework for rapidly building custom user interfaces.
</p>

<p align="center">
    <a href="https://github.com/tailwindlabs/tailwindcss/actions"><img src="https://img.shields.io/github/actions/workflow/status/tailwindlabs/tailwindcss/ci.yml?branch=next" alt="Build Status"></a>
    <a href="https://www.npmjs.com/package/tailwindcss"><img src="https://img.shields.io/npm/dt/tailwindcss.svg" alt="Total Downloads"></a>
    <a href="https://github.com/tailwindcss/tailwindcss/releases"><img src="https://img.shields.io/npm/v/tailwindcss.svg" alt="Latest Release"></a>
    <a href="https://github.com/tailwindcss/tailwindcss/blob/master/LICENSE"><img src="https://img.shields.io/npm/l/tailwindcss.svg" alt="License"></a>
</p>

----------------------------------------

TITLE: Displaying Project Status Badges
DESCRIPTION: HTML markup for displaying project status badges including build status, download count, version, and license information.

LANGUAGE: html
CODE:
<p align="center">
    <a href="https://github.com/tailwindlabs/tailwindcss/actions"><img src="https://img.shields.io/github/actions/workflow/status/tailwindlabs/tailwindcss/ci.yml?branch=next" alt="Build Status"></a>
    <a href="https://www.npmjs.com/package/tailwindcss"><img src="https://img.shields.io/npm/dt/tailwindcss.svg" alt="Total Downloads"></a>
    <a href="https://github.com/tailwindcss/tailwindcss/releases"><img src="https://img.shields.io/npm/v/tailwindcss.svg" alt="Latest Release"></a>
    <a href="https://github.com/tailwindcss/tailwindcss/blob/master/LICENSE"><img src="https://img.shields.io/npm/l/tailwindcss.svg" alt="License"></a>
</p>

----------------------------------------

TITLE: Displaying Project Status Badges in HTML
DESCRIPTION: This HTML snippet shows a set of status badges for the Tailwind CSS project, including build status, total downloads, latest release version, and license information. Each badge is linked to its respective source.

LANGUAGE: HTML
CODE:
<p align="center">
    <a href="https://github.com/tailwindlabs/tailwindcss/actions"><img src="https://img.shields.io/github/actions/workflow/status/tailwindlabs/tailwindcss/ci.yml?branch=next" alt="Build Status"></a>
    <a href="https://www.npmjs.com/package/tailwindcss"><img src="https://img.shields.io/npm/dt/tailwindcss.svg" alt="Total Downloads"></a>
    <a href="https://github.com/tailwindcss/tailwindcss/releases"><img src="https://img.shields.io/npm/v/tailwindcss.svg" alt="Latest Release"></a>
    <a href="https://github.com/tailwindcss/tailwindcss/blob/master/LICENSE"><img src="https://img.shields.io/npm/l/tailwindcss.svg" alt="License"></a>
</p>

----------------------------------------

TITLE: Rendering TailwindCSS Project Logo with Dark/Light Mode Support
DESCRIPTION: HTML markup for displaying the TailwindCSS logo with responsive dark/light mode support using the picture element and multiple sources.

LANGUAGE: HTML
CODE:
<p align="center">
  <a href="https://tailwindcss.com" target="_blank">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/tailwindlabs/tailwindcss/HEAD/.github/logo-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/tailwindlabs/tailwindcss/HEAD/.github/logo-light.svg">
      <img alt="Tailwind CSS" src="https://raw.githubusercontent.com/tailwindlabs/tailwindcss/HEAD/.github/logo-light.svg" width="350" height="70" style="max-width: 100%;">
    </picture>
  </a>
</p>

----------------------------------------

TITLE: Displaying Tailwind CSS Logo with Dark/Light Mode Support in HTML
DESCRIPTION: This HTML snippet displays the Tailwind CSS logo with support for dark and light color schemes. It uses the <picture> element to provide different logo versions based on the user's color scheme preference.

LANGUAGE: HTML
CODE:
<p align="center">
  <a href="https://tailwindcss.com" target="_blank">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/tailwindlabs/tailwindcss/HEAD/.github/logo-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/tailwindlabs/tailwindcss/HEAD/.github/logo-light.svg">
      <img alt="Tailwind CSS" src="https://raw.githubusercontent.com/tailwindlabs/tailwindcss/HEAD/.github/logo-light.svg" width="350" height="70" style="max-width: 100%;">
    </picture>
  </a>
</p>

----------------------------------------

TITLE: Displaying Tailwind CSS Oxide Android ARM EABI Binary Information in Markdown
DESCRIPTION: This snippet uses Markdown syntax to display the name of the binary package and provide a brief description of its target architecture and platform.

LANGUAGE: Markdown
CODE:
# `@tailwindcss/oxide-android-arm-eabi`

This is the **armv7-linux-android-eabi** binary for `@tailwindcss/oxide`

----------------------------------------

TITLE: Rendering Project Status Badges
DESCRIPTION: HTML markup for displaying project status badges including build status, download count, version, and license information.

LANGUAGE: HTML
CODE:
<p align="center">
    <a href="https://github.com/tailwindlabs/tailwindcss/actions"><img src="https://img.shields.io/github/actions/workflow/status/tailwindlabs/tailwindcss/ci.yml?branch=next" alt="Build Status"></a>
    <a href="https://www.npmjs.com/package/tailwindcss"><img src="https://img.shields.io/npm/dt/tailwindcss.svg" alt="Total Downloads"></a>
    <a href="https://github.com/tailwindcss/tailwindcss/releases"><img src="https://img.shields.io/npm/v/tailwindcss.svg" alt="Latest Release"></a>
    <a href="https://github.com/tailwindcss/tailwindcss/blob/master/LICENSE"><img src="https://img.shields.io/npm/l/tailwindcss.svg" alt="License"></a>
</p>

----------------------------------------

TITLE: Displaying Tailwind CSS Logo with Dark/Light Mode Support in HTML
DESCRIPTION: This HTML snippet displays the Tailwind CSS logo with support for dark and light color schemes. It uses the <picture> element to provide different logo versions based on the user's color scheme preference.

LANGUAGE: HTML
CODE:
<p align="center">
  <a href="https://tailwindcss.com" target="_blank">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/tailwindlabs/tailwindcss/HEAD/.github/logo-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/tailwindlabs/tailwindcss/HEAD/.github/logo-light.svg">
      <img alt="Tailwind CSS" src="https://raw.githubusercontent.com/tailwindlabs/tailwindcss/HEAD/.github/logo-light.svg" width="350" height="70" style="max-width: 100%;">
    </picture>
  </a>
</p>

----------------------------------------

TITLE: Displaying TailwindCSS Logo with Dark/Light Mode Support
DESCRIPTION: HTML markup for rendering the TailwindCSS logo with responsive dark/light mode support using the picture element and multiple sources.

LANGUAGE: html
CODE:
<p align="center">
  <a href="https://tailwindcss.com" target="_blank">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/tailwindlabs/tailwindcss/HEAD/.github/logo-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/tailwindlabs/tailwindcss/HEAD/.github/logo-light.svg">
      <img alt="Tailwind CSS" src="https://raw.githubusercontent.com/tailwindlabs/tailwindcss/HEAD/.github/logo-light.svg" width="350" height="70" style="max-width: 100%;">
    </picture>
  </a>
</p>

----------------------------------------

TITLE: Displaying Tailwind CSS Logo with Dark/Light Mode Support in HTML
DESCRIPTION: This HTML snippet showcases the Tailwind CSS logo with support for dark and light color schemes. It uses the <picture> element to provide different logo versions based on the user's preferred color scheme.

LANGUAGE: HTML
CODE:
<p align="center">
  <a href="https://tailwindcss.com" target="_blank">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/tailwindlabs/tailwindcss/HEAD/.github/logo-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/tailwindlabs/tailwindcss/HEAD/.github/logo-light.svg">
      <img alt="Tailwind CSS" src="https://raw.githubusercontent.com/tailwindlabs/tailwindcss/HEAD/.github/logo-light.svg" width="350" height="70" style="max-width: 100%;">
    </picture>
  </a>
</p>