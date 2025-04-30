+++
# --- Workflow Metadata ---
id = "WF-CREATE-ROO-CMD-BUILD-V1" # (String, Required) Unique identifier
title = "Workflow: Create Roo Commander Build" # (String, Required)
description = """
(String, Required) Defines the steps required to create a new build for Roo Commander.
This workflow orchestrates the necessary actions to compile, package, and prepare a distributable version.
"""
version = "1.0.0" # (String, Required) Semantic version for the workflow definition.
status = "Draft" # (String, Required) Current status: "Draft", "Active", "Deprecated", "Experimental".
tags = ["workflow", "build", "roo-commander", "release"] # (Array of Strings, Optional) Keywords for search/categorization.

# --- Execution Control ---
entry_point = "00_start.md" # (String, Required) Filename of the first step to execute.

# --- Interface ---
inputs = [ # (Array of Strings, Optional) Describe overall inputs needed to start the workflow.
    "build_parameters: Object containing details like version, platform, flags.", # Made more specific
]
outputs = [ # (Array of Strings, Optional) Describe the expected final artifacts or outcomes.
    "build_status: String indicating 'Success' or 'Failure'.", # Made more specific
    "packaged_artifact_path: String path to the final artifact.", # Made more specific
    "log_paths: Array of strings containing paths to relevant logs (build, packaging).", # Made more specific
]

# --- Housekeeping ---
owner = "lead-devops" # (String, Optional) Added owner field
maintainer = "lead-devops" # (String, Optional) Added maintainer field
last_updated = "{{DATE}}" # (String, Required) Date of last modification. Use placeholder.
template_schema_doc = ".ruru/templates/toml-md/23_workflow_readme.md" # (String, Required) Link to this template definition.
related_docs = [] # (Array of Strings, Optional) Links to related rules, KBs, ADRs. # Consider adding links later
+++

# Workflow: Create Roo Commander Build

## Overview

Defines the steps required to create a new build for Roo Commander.
## Workflow Diagram

```mermaid
graph LR
    A[00_start] --> B(01_validate_params);
    B -- Success --> C(02_setup_environment);
    C -- Success --> D(03_run_build);
    D -- Success --> E(04_package_artifacts);
    E -- Success --> F(99_finish);

    A -- Error --> EE_Start(EE_handle_start_error);
    B -- Error --> EE_Val(EE_handle_validation_error);
    C -- Error --> EE_Env(EE_handle_env_error);
    D -- Error --> EE_Build(EE_handle_build_error);
    E -- Error --> EE_Pkg(EE_handle_packaging_error);
    F -- Error --> EE_Fin(EE_handle_finish_error);

    EE_Start --> Z((End Failure));
    EE_Val --> Z;
    EE_Env --> Z;
    EE_Build --> Z;
    EE_Pkg --> Z;
    EE_Fin --> Z;
    F -- Success --> Y((End Success));

    classDef errorNode fill:#f9f,stroke:#333,stroke-width:2px;
    class EE_Start,EE_Val,EE_Env,EE_Build,EE_Pkg,EE_Fin errorNode;
```

---
This workflow orchestrates the necessary actions to compile, package, and prepare a distributable version.

## Usage

This workflow is typically initiated by a coordinator or release manager when a new build of Roo Commander is required. Provide the necessary build parameters as input.

## Inputs

*   **Build Parameters:** Details specifying the desired build, such as target version number, target platform(s), and any specific build flags or configurations.

## Outputs

*   **Build Status:** Confirmation indicating whether the build process completed successfully or encountered errors.
*   **Artifacts/Logs:** Path(s) to the generated build artifacts (e.g., executables, archives) or detailed logs if the build failed.