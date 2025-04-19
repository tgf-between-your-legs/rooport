# Technology Stack Indicators

This document lists common files, keywords, and patterns that indicate the presence of specific technologies. Use this as a reference during the automated context analysis phase.

## Package Managers & Manifests

*   **Node.js/JavaScript:**
    *   `package.json`: Dependencies (`dependencies`, `devDependencies`), scripts (`scripts`).
    *   `package-lock.json` / `yarn.lock` / `pnpm-lock.yaml`: Lock files.
    *   Keywords: `require(...)`, `import ... from ...`, `module.exports`, `export default`.
*   **Python:**
    *   `requirements.txt`: List of pip packages.
    *   `Pipfile` / `Pipfile.lock`: Pipenv files.
    *   `pyproject.toml`: Poetry or modern pip configuration.
    *   Keywords: `import ...`, `from ... import ...`.
*   **PHP:**
    *   `composer.json`: Dependencies (`require`, `require-dev`), scripts.
    *   `composer.lock`: Lock file.
    *   Keywords: `require`, `include`, `use ...`, `namespace ...`.
*   **Java:**
    *   `pom.xml`: Maven project file (look for `<dependencies>`).
    *   `build.gradle` / `build.gradle.kts`: Gradle build file (look for `dependencies { ... }`).
    *   Keywords: `import ...`, `package ...`.
*   **Go:**
    *   `go.mod`: Module dependencies.
    *   `go.sum`: Checksums.
    *   Keywords: `import (...)`, `package main`.
*   **Ruby:**
    *   `Gemfile` / `Gemfile.lock`: Bundler dependencies.
    *   Keywords: `require ...`.
*   **Rust:**
    *   `Cargo.toml`: Dependencies (`[dependencies]`).
    *   `Cargo.lock`: Lock file.
    *   Keywords: `use ...`, `mod ...`, `extern crate ...`.

## Frameworks & Libraries (Examples)

*   **React:** `import React`, `import ReactDOM`, `useState`, `useEffect`, JSX syntax (`<Component />`), `package.json` deps (`react`, `react-dom`).
*   **Vue.js:** `import Vue`, `new Vue({...})`, `.vue` files (Single File Components), `<template>`, `<script>`, `<style>`, `package.json` deps (`vue`).
*   **Angular:** `import { Component } from '@angular/core'`, `@Component({...})`, `*.component.ts`, `*.module.ts`, `angular.json`, `package.json` deps (`@angular/core`).
*   **Next.js:** `import Head from 'next/head'`, `getServerSideProps`, `getStaticProps`, `pages/` directory structure, `next.config.js`, `package.json` deps (`next`).
*   **Nuxt.js:** `asyncData`, `fetch`, `plugins/`, `middleware/`, `pages/` directory structure, `nuxt.config.js`, `package.json` deps (`nuxt`).
*   **Svelte/SvelteKit:** `.svelte` files, `export let prop`, `<script context="module">`, `+page.svelte`, `+layout.svelte`, `svelte.config.js`, `package.json` deps (`svelte`, `@sveltejs/kit`).
*   **Astro:** `.astro` files, `---` frontmatter fences, `Astro.*` APIs, `astro.config.mjs`, `package.json` deps (`astro`).
*   **Tailwind CSS:** `tailwind.config.js`, `@tailwind` directives in CSS, utility classes (`class="text-red-500"`), `package.json` deps (`tailwindcss`).
*   **Bootstrap:** `class="container"`, `class="row"`, `class="col-"`, `class="btn"`, `package.json` deps (`bootstrap`).
*   **Django:** `manage.py`, `settings.py`, `urls.py`, `views.py`, `models.py`, `apps.py`, `requirements.txt` deps (`django`).
*   **Flask:** `from flask import Flask`, `app = Flask(...)`, `@app.route(...)`, `requirements.txt` deps (`flask`).
*   **FastAPI:** `from fastapi import FastAPI`, `app = FastAPI(...)`, `@app.get(...)`, `requirements.txt` deps (`fastapi`, `uvicorn`).
*   **Laravel:** `artisan` file, `composer.json` deps (`laravel/framework`), `routes/web.php`, `app/Http/Controllers`, `.env` file structure.
*   **Express.js:** `require('express')`, `const app = express()`, `app.get(...)`, `app.listen(...)`, `package.json` deps (`express`).

## Databases & ORMs

*   **SQLAlchemy (Python):** `import sqlalchemy`, `create_engine`, `declarative_base`, `sessionmaker`.
*   **Django ORM (Python):** `from django.db import models`, `Model.objects.all()`.
*   **Prisma (Node.js/TS):** `schema.prisma`, `prisma generate`, `prisma migrate`, `package.json` deps (`@prisma/client`).
*   **TypeORM (Node.js/TS):** `@Entity()`, `@Column()`, `DataSource`, `getRepository`.
*   **Mongoose (Node.js):** `require('mongoose')`, `new Schema({...})`, `mongoose.model(...)`.

## Build Tools & CI/CD

*   **Webpack:** `webpack.config.js`.
*   **Vite:** `vite.config.js` / `vite.config.ts`.
*   **Docker:** `Dockerfile`, `docker-compose.yml`.
*   **GitHub Actions:** `.github/workflows/*.yml`.
*   **GitLab CI:** `.gitlab-ci.yml`.
*   **Jenkins:** `Jenkinsfile`.

*(This list is not exhaustive. Add more indicators based on common technologies encountered.)*