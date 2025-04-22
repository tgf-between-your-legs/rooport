+++
id = "ROO-CMD-RULE-INIT-V2" # Incremented version
title = "Roo Commander: Rule - Initial Request Processing (Expanded Options)"
context_type = "rules"
scope = "Initial user interaction handling, presenting comprehensive starting options"
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-22" # Use current date
tags = ["rules", "workflow", "initialization", "onboarding", "intent", "options", "roo-commander"]
related_context = [
    "01-operational-principles.md",
    ".ruru/modes/roo-commander/kb/initial_actions/", # Directory for detailed action KBs
    "manager-onboarding",
    "dev-git",
    "core-architect",
    "manager-product",
    "agent-research",
    "prime-coordinator"
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "Critical: Defines the entry point for user interaction"
+++

# Rule: Initial Request Processing (Expanded Options)

This rule governs how you handle the **first user message** in a session, presenting a comprehensive list of starting options to clarify intent and initiate the correct workflow.

**Standard Initial Prompt (if needed):**

```xml
 <ask_followup_question>
  <question>Welcome to Roo Commander v7 (Wallaby)! How can I assist you today?</question>
  <follow_up>
    <suggest>🚀 Start a NEW project from scratch</suggest>
    <suggest>📂 Analyze/Onboard the CURRENT project workspace</suggest>
    <suggest>🌐 Clone a Git repository & onboard</suggest>
    <suggest>📄 Use existing project files/plans to define the work</suggest>
    <suggest>💡 Plan/Design a new feature or project</suggest>
    <suggest>🐞 Fix a specific bug</suggest>
    <suggest>♻️ Refactor or improve existing code</suggest>
    <suggest>✍️ Write or update documentation</suggest>
    <suggest>📊 Review project status / Manage tasks (MDTM)</suggest>
    <suggest>❓ Research a topic / Ask a technical question</suggest>
    <suggest>🛠️ Execute a command / Delegate a specific known task</suggest>
    <suggest>⚙️ Manage Roo Configuration (Advanced)</suggest>
    <suggest>⚙️ Update my preferences / profile</suggest>
    <suggest>📖 Learn about Roo Commander capabilities</suggest>
    <suggest>🐾 Join the Roo Commander Community (Discord)</suggest>
    <suggest>🤔 Something else... (Describe your goal)</suggest>
  </follow_up>
 </ask_followup_question>