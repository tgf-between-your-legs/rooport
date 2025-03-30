# Mode Collections (`mode_templates/mode_collections/`)

This directory contains JSON files, each representing a curated collection or set of mode definitions.

The mode definitions within each JSON file are copies of the individual mode templates found in the parent `mode_templates/` directory. These collections are organized by theme (e.g., web specialists, backend specialists, management roles) to provide convenient groupings for users.

The primary purpose of these collection files is to allow users to easily enable a specific set of modes. You can copy the *entire content* of a desired collection file (e.g., `custom_modes_specialists_web.json`) and paste it directly into your active runtime configuration file. This could be your project-specific `context/cline_custom_modes.json` or a global settings file used by your Cline setup.

**Important Note:** The JSON files within this `mode_collections/` directory are **not** directly loaded or processed by the system. They exist purely as a way to organize mode templates into convenient, copy-pasteable sets for manual configuration.