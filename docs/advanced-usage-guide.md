# ROOPORT Advanced Usage Guide

## 🚀 Complete Installation and Configuration

This guide provides step-by-step instructions for setting up ROOPORT with all its dependencies and understanding its real-world functionality.

## ⚠️ Prerequisites

ROOPORT is designed to work specifically with the **RooCode ecosystem**:

- **RooCommander** - The base AI assistant framework
- **ConPort (Context Portal)** - Knowledge management and memory system
- **Vertex AI MCP Server** - Advanced AI capabilities
- **Python 3.8+** - Runtime environment

## 📋 Installation Overview

ROOPORT enhances RooCommander with advanced agentic capabilities. The installation involves:

1. Setting up RooCommander base system
2. Installing and configuring ConPort
3. Setting up Vertex AI MCP server
4. Installing ROOPORT enhancements
5. Configuration and testing

## 🔧 Step 1: RooCommander Installation

### 1.1 Clone RooCommander Repository

```bash
# Clone the official RooCommander repository
git clone https://github.com/RooVeterinaryInc/roo-commander.git
cd roo-commander

# Install dependencies
npm install
# or
yarn install
```

### 1.2 Basic RooCommander Setup

Follow the RooCommander documentation for initial setup:

```bash
# Configure VS Code extension
# Install the RooCommander VS Code extension from the marketplace
# Configure your AI provider (Claude, OpenAI, etc.)
```

## 🗄️ Step 2: ConPort (Context Portal) Installation

ConPort provides persistent memory and knowledge management for ROOPORT.

### 2.1 Install ConPort

```bash
# Clone ConPort repository
git clone https://github.com/context-portal/context-portal.git
cd context-portal

# Create Python virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install ConPort
pip install -e .
```

### 2.2 Configure ConPort MCP Server

Create or update your MCP configuration:

```json
{
  "mcpServers": {
    "conport": {
      "command": "/path/to/context-portal/.venv/Scripts/python.exe",
      "args": [
        "/path/to/context-portal/src/context_portal_mcp/main.py",
        "--mode", "stdio",
        "--workspace_id", "${workspaceFolder}",
        "--log-file", "/logs/conport.log",
        "--log-level", "INFO"
      ],
      "alwaysAllow": [
        "get_product_context",
        "update_product_context",
        "get_active_context",
        "update_active_context",
        "log_decision",
        "get_decisions",
        "search_decisions_fts",
        "log_progress",
        "get_progress",
        "log_system_pattern",
        "get_system_patterns",
        "log_custom_data",
        "get_custom_data",
        "search_custom_data_value_fts",
        "link_conport_items",
        "get_linked_items",
        "get_recent_activity_summary"
      ]
    }
  }
}
```

### 2.3 Initialize ConPort Database

```bash
# Navigate to your project workspace
cd /path/to/your/project

# Initialize ConPort database
mkdir -p context_portal
cd context_portal

# ConPort will create context.db automatically on first use
```

## 🤖 Step 3: Vertex AI MCP Server Installation

### 3.1 Install Vertex AI MCP Server

```bash
# Clone Vertex AI MCP server repository
git clone https://github.com/vertex-ai-mcp-server/vertex-ai-mcp-server.git
cd vertex-ai-mcp-server

# Install dependencies
npm install
# or
yarn install

# Build the server
npm run build
# or
yarn build
```

### 3.2 Configure Google Cloud Credentials

```bash
# Set up Google Cloud authentication
gcloud auth login
gcloud config set project YOUR_PROJECT_ID

# Or set up service account key
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account-key.json"
```

### 3.3 Configure Vertex AI MCP Server

Add to your MCP configuration:

```json
{
  "mcpServers": {
    "vertex-ai-mcp-server": {
      "type": "stdio",
      "command": "bun",
      "args": ["/path/to/vertex-ai-mcp-server/build/index.js"],
      "env": {
        "GOOGLE_CLOUD_PROJECT": "your-project-id",
        "GOOGLE_CLOUD_LOCATION": "us-central1",
        "VERTEX_MODEL_ID": "gemini-2.5-pro-preview-05-06",
        "VERTEX_AI_TEMPERATURE": "0.0",
        "VERTEX_AI_USE_STREAMING": "true",
        "VERTEX_AI_MAX_OUTPUT_TOKENS": "65535",
        "VERTEX_AI_MAX_RETRIES": "3"
      }
    }
  }
}
```

## 🎯 Step 4: ROOPORT Installation

### 4.1 Install ROOPORT Package

```bash
# Clone ROOPORT repository
git clone https://github.com/tgf-between-your-legs/rooport.git
cd rooport

# Install ROOPORT
pip install -e .

# Or install from PyPI (when available)
pip install rooport
```

### 4.2 Configure Environment Variables

Copy and configure the environment template:

```bash
# Copy environment template
cp .env.template .env

# Edit .env with your actual values
```

Required environment variables:

```bash
# Google Cloud Configuration
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1

# API Keys (if using additional services)
BRAVE_API_KEY=your-brave-api-key
PERPLEXITY_API_KEY=your-perplexity-api-key
SUPABASE_ACCESS_TOKEN=your-supabase-token

# File Paths
VERTEX_AI_SERVER_PATH=./vertex-ai-mcp-server/build/index.js
CONPORT_PYTHON_PATH=./context-portal/.venv/Scripts/python.exe
CONPORT_MAIN_PATH=./context-portal/src/context_portal_mcp/main.py
```

### 4.3 Install ROOPORT Rules and Modes

Copy ROOPORT enhancements to your RooCommander installation:

```bash
# Copy ROOPORT AI engines to RooCommander
cp -r src/rooport/core/* /path/to/roo-commander/.ruru/modes/roo-commander/

# Copy ROOPORT rules
cp -r .roo/rules/* /path/to/roo-commander/.roo/rules/

# Copy ROOPORT mode-specific rules
cp -r .roo/rules-roo-commander/* /path/to/roo-commander/.roo/rules-roo-commander/
```

## 🧪 Step 5: Testing Your Installation

### 5.1 Test ConPort Connection

```python
# Test ConPort MCP connection
import asyncio
from rooport.integrations.conport import ConPortClient

async def test_conport():
    client = ConPortClient(workspace_id="/path/to/your/workspace")
    
    # Test basic connection
    result = await client.get_product_context()
    print(f"ConPort connection: {'✅ Success' if result else '❌ Failed'}")
    
    # Test logging
    await client.log_custom_data(
        category="test",
        key="installation_test",
        value={"status": "testing", "timestamp": "2025-05-24"}
    )
    print("✅ ConPort logging test successful")

# Run test
asyncio.run(test_conport())
```

### 5.2 Test ROOPORT CLI

```bash
# Test ROOPORT CLI installation
rooport --version

# Test with verbose output
rooport --verbose --workspace /path/to/your/project

# Test autonomous mode configuration
rooport --autonomous standard
```

### 5.3 Test AI Engines

```python
# Test the Ultimate Agentic Orchestrator
import asyncio
from rooport.core.orchestrator import UltimateAgenticOrchestrator

async def test_orchestrator():
    # Mock ConPort client for testing
    class MockConPortClient:
        async def log_custom_data(self, **kwargs):
            return {"status": "success"}
    
    orchestrator = UltimateAgenticOrchestrator(MockConPortClient())
    
    # Test basic query processing
    response = await orchestrator.process_ultimate_request(
        user_query="What is the current project status?",
        workspace_id="/path/to/your/workspace"
    )
    
    print(f"Primary Response: {response.primary_response}")
    print(f"Confidence Score: {response.confidence_score}")
    print(f"Execution Time: {response.execution_time}s")

# Run test
asyncio.run(test_orchestrator())
```

## 🔍 Understanding ROOPORT's Real Functionality

### 📊 What Actually Works vs. Theoretical

#### ✅ Fully Implemented and Functional:

1. **Autonomous Mode Control**
   - Configuration system with 4 levels (OFF/MINIMAL/STANDARD/FULL)
   - User preference learning and persistence
   - Safety mechanisms and emergency controls

2. **ConPort Integration**
   - All ConPort MCP tools are functional
   - Real-time logging of decisions, progress, and custom data
   - Knowledge graph building with relationship linking
   - Session management and artifact tracking

3. **Configuration Management**
   - Environment variable handling
   - MCP server configuration templates
   - Security-first credential management

#### 🚧 Partially Implemented (Core Structure Ready):

1. **Agentic RAG Engine**
   - **Structure**: Complete with query decomposition, retrieval strategies, confidence assessment
   - **Integration**: ConPort integration points defined
   - **Status**: Requires ConPort data population and query processing implementation
   - **Real Usage**: Can retrieve from ConPort but needs content to be meaningful

2. **Continuous Learning System**
   - **Structure**: Complete feedback collection, performance analysis, agent improvement proposals
   - **Data Models**: Full feedback categorization and review workflows
   - **Status**: Requires integration with actual agent performance metrics
   - **Real Usage**: Can collect feedback but needs historical data for meaningful analysis

3. **Proactive Orchestration Engine**
   - **Structure**: Complete project state analysis, opportunity identification, suggestion generation
   - **Integration**: ConPort integration for project state retrieval
   - **Status**: Requires project data in ConPort to generate meaningful suggestions
   - **Real Usage**: Will work once ConPort contains project information

#### 🎯 Ultimate Agentic Orchestrator (Fully Functional):
- Coordinates all engines in parallel
- Handles errors gracefully with fallbacks
- Provides unified response synthesis
- Real performance tracking and optimization cycles

### 🔄 ConPort Logging Frequency and Behavior

#### Automatic Logging Triggers:
1. **Every user interaction** - Query and response logged
2. **Decision points** - When user makes choices or confirmations
3. **Task delegation** - When work is assigned to specialist modes
4. **Completion events** - When tasks finish (success/failure)
5. **Error occurrences** - When issues are encountered
6. **Performance metrics** - Execution times and confidence scores
7. **Learning events** - When feedback is collected or improvements identified

#### Manual Logging Opportunities:
- User can explicitly log decisions via commands
- Proactive suggestions from the system
- Session summaries and milestone documentation
- Custom project information and glossary terms

#### Data Persistence:
- ConPort uses SQLite database (`context.db`)
- All data persists across sessions
- Workspace-specific isolation
- Full export/import capabilities

### 🗂️ Project Management and Context Switching

#### Current Project Detection:
```python
# ROOPORT determines current project by:
1. Workspace ID (absolute path to current directory)
2. ConPort database location (workspace/context_portal/context.db)
3. Active session tracking in ConPort
4. Product context configuration
```

#### Switching Between Projects:
```bash
# Method 1: Change workspace directory
cd /path/to/different/project
rooport --workspace .

# Method 2: Explicit workspace specification
rooport --workspace /path/to/specific/project

# Method 3: ConPort workspace switching (future)
# Each workspace maintains its own ConPort database
```

#### Project State Restoration:
- ConPort automatically loads project context when workspace changes
- Recent activity summary provides quick catch-up
- Session logs maintain detailed interaction history
- Knowledge graph preserves relationships and decisions

### 🧪 Testing a ROOPORT Installation

#### Level 1: Basic Installation Test
```bash
# 1. Verify CLI works
rooport --version
rooport --help

# 2. Test configuration
rooport --workspace /test/project --verbose

# 3. Check autonomous mode
rooport --autonomous minimal
```

#### Level 2: ConPort Integration Test
```python
# Test ConPort connectivity and basic operations
import asyncio
from rooport.integrations.conport import ConPortClient

async def integration_test():
    client = ConPortClient(workspace_id="/test/project")
    
    # Test basic CRUD operations
    await client.update_product_context({
        "name": "Test Project",
        "description": "ROOPORT installation test"
    })
    
    context = await client.get_product_context()
    assert context["name"] == "Test Project"
    
    # Test logging
    await client.log_decision(
        summary="Test decision",
        rationale="Installation verification"
    )
    
    decisions = await client.get_decisions(limit=1)
    assert len(decisions) > 0
    
    print("✅ ConPort integration test passed")

asyncio.run(integration_test())
```

#### Level 3: AI Engine Test
```python
# Test the orchestrator with real ConPort data
async def full_system_test():
    from rooport.core.orchestrator import UltimateAgenticOrchestrator
    from rooport.integrations.conport import ConPortClient
    
    conport = ConPortClient(workspace_id="/test/project")
    orchestrator = UltimateAgenticOrchestrator(conport)
    
    # Populate some test data
    await conport.update_product_context({
        "name": "ROOPORT Test Project",
        "tech_stack": ["Python", "AI", "ConPort"],
        "goals": ["Test AI capabilities", "Verify integration"]
    })
    
    await conport.log_progress(
        description="Setting up test environment",
        status="IN_PROGRESS"
    )
    
    # Test orchestrator
    response = await orchestrator.process_ultimate_request(
        user_query="What is the current status of this project?",
        workspace_id="/test/project"
    )
    
    print(f"Response: {response.primary_response}")
    print(f"Suggestions: {len(response.proactive_suggestions)}")
    print(f"Confidence: {response.confidence_score}")
    
    assert response.confidence_score > 0.0
    assert len(response.primary_response) > 0
    
    print("✅ Full system test passed")

asyncio.run(full_system_test())
```

#### Level 4: Real-World Usage Test
```bash
# 1. Start a real project session
cd /your/actual/project
rooport --autonomous standard

# 2. Initialize project in ConPort
# Ask: "Initialize this project in ConPort with basic information"

# 3. Test decision logging
# Ask: "I've decided to use React for the frontend. Please log this decision."

# 4. Test progress tracking
# Ask: "I'm starting work on user authentication. Track this as a new task."

# 5. Test knowledge retrieval
# Ask: "What decisions have we made about the frontend?"

# 6. Test proactive suggestions
# Ask: "What should I work on next?"

# 7. Test learning system
# Rate responses and provide feedback
```

## 🎯 Real-World ROOPORT Workflow

### Daily Usage Pattern:
1. **Session Start**: ROOPORT loads project context from ConPort
2. **Continuous Logging**: Every interaction updates ConPort knowledge base
3. **Proactive Assistance**: System suggests next actions based on project state
4. **Learning Integration**: Performance feedback improves future responses
5. **Session End**: Summary logged for future reference

### Knowledge Accumulation:
- Each conversation builds project knowledge
- Decisions create permanent project memory
- Relationships between concepts are automatically detected
- Historical context improves suggestion quality over time

ROOPORT transforms from a simple AI assistant into an intelligent project companion that learns, remembers, and proactively helps drive your development forward.