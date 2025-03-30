# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed
- Corrected schema issues in several mode templates (`customInstructions` format, invalid `groups`, removed `source` field).
- Updated management modes (`project-manager`, `technical-architect`, `devops-manager`, `roo-chief-executive`) with documentation responsibilities and permissions.
- Added a link to the main README in the Mode Configurator UI (`App.vue`).

### Added
- Added new modes: `discovery-agent` and `project-initializer`.
- Set up GitHub Actions workflow for automated deployment of the Mode Configurator.

### Removed
- Removed unused `mode_collections` directory.

### Added
- **Mode Configurator Tool:** Added a web-based tool (`tools/mode_configurator/`) built with Vue.js and Vite. This tool allows users to select desired mode templates and generates the corresponding JSON configuration array for use in Roo Commander's `cline_custom_modes.json`. It fetches mode definitions dynamically from `tools/mode_configurator/public/mode_templates/`. Includes a `manifest.json` in the templates directory.
- Updated main `README.md` with instructions for using the Mode Configurator tool.

### Changed
- Moved `mode_templates` directory into `tools/mode_configurator/public/` to allow serving via Vite dev server and static hosting.