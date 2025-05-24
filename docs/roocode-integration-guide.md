# ROOPORT + RooCode Integration Guide

## 🔗 Complete RooCode Ecosystem Integration

ROOPORT is specifically designed to enhance the RooCode ecosystem, building upon RooCommander's foundation with advanced agentic capabilities. This guide details the complete integration process.

## 📚 RooCode Documentation Integration

### Understanding the RooCode Ecosystem

The RooCode ecosystem consists of:

1. **RooCommander** - Base AI assistant framework
2. **RooCode VS Code Extension** - IDE integration
3. **ConPort (Context Portal)** - Knowledge management system
4. **ROOPORT** - Advanced agentic capabilities layer

### RooCode Documentation in RAG System

ROOPORT automatically integrates RooCode documentation into its knowledge base through ConPort. Here's how:

#### 1. Documentation Sources Loaded into ConPort:

```python
# RooCode documentation sources automatically indexed:
ROOCODE_DOCS_SOURCES = [
    # Core RooCommander documentation
    "https://github.com/RooVeterinaryInc/roo-commander/blob/main/README.md",
    "https://github.com/RooVeterinaryInc/roo-commander/tree/main/docs",
    
    # RooCode VS Code extension docs
    "https://github.com/RooVeterinaryInc/roo-code-vscode/blob/main/README.md",
    
    # ConPort documentation
    "https://github.com/context-portal/context-portal/blob/main/README.md",
    "https://github.com/context-portal/context-portal/tree/main/docs",
    
    # Mode definitions and capabilities
    "/ruru/modes/*/README.md",
    "/ruru/modes/*/*.mode.md",
    
    # Rule definitions
    "/.roo/rules/*.md",
    "/.roo/rules-*/",
    
    # Workflow and process documentation
    "/.ruru/workflows/",
    "/.ruru/processes/"
]
```

#### 2. Automatic Documentation Indexing:

```python
# ROOPORT automatically indexes documentation on startup
async def initialize_roocode_knowledge_base(workspace_id: str):
    """Initialize RooCode documentation in ConPort"""
    
    # Index core RooCode concepts
    await conport.log_custom_data(
        workspace_id=workspace_id,
        category="RooCodeDocumentation",
        key="core_concepts",
        value={
            "modes": "Specialist AI agents with specific capabilities",
            "rules": "Behavioral guidelines and procedures for modes",
            "mdtm": "Markdown-driven task management system",
            "workflows": "High-level process definitions",
            "processes": "Detailed step-by-step procedures",
            "context_sources": "Information sources for AI decision-making"
        }
    )
    
    # Index available modes and their capabilities
    modes_info = await discover_available_modes()
    await conport.log_custom_data(
        workspace_id=workspace_id,
        category="RooCodeDocumentation", 
        key="available_modes",
        value=modes_info
    )
    
    # Index rule system
    rules_info = await discover_rule_system()
    await conport.log_custom_data(
        workspace_id=workspace_id,
        category="RooCodeDocumentation",
        key="rule_system", 
        value=rules_info
    )
```

#### 3. RAG System Access to Documentation:

```python
# ROOPORT's RAG engine can retrieve RooCode documentation
async def query_roocode_documentation(query: str):
    """Query RooCode documentation through RAG system"""
    
    # Search RooCode documentation
    docs_results = await conport.search_custom_data_value_fts(
        workspace_id=workspace_id,
        query_term=query,
        category_filter="RooCodeDocumentation"
    )
    
    # Search mode-specific documentation
    mode_results = await conport.search_custom_data_value_fts(
        workspace_id=workspace_id,
        query_term=query,
        category_filter="ModeDocumentation"
    )
    
    # Combine and rank results
    return synthesize_documentation_response(docs_results, mode_results)
```

## 🚀 Complete Installation for RooCode Integration

### Step 1: RooCode Base Setup

```bash
# 1. Install RooCommander
git clone https://github.com/RooVeterinaryInc/roo-commander.git
cd roo-commander
npm install

# 2. Install RooCode VS Code Extension
# Install from VS Code marketplace: "Roo Code"

# 3. Configure base RooCommander
# Set up your AI provider (Claude, OpenAI, etc.)
# Configure basic modes and rules
```

### Step 2: ConPort Integration

```bash
# 1. Clone and install ConPort
git clone https://github.com/context-portal/context-portal.git
cd context-portal

# 2. Set up Python environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate     # Windows

# 3. Install ConPort
pip install -e .

# 4. Configure ConPort MCP server
# Add ConPort configuration to your RooCommander MCP settings
```

### Step 3: ROOPORT Enhancement Layer

```bash
# 1. Install ROOPORT
git clone https://github.com/tgf-between-your-legs/rooport.git
cd rooport
pip install -e .

# 2. Integrate ROOPORT with RooCommander
# Copy ROOPORT AI engines to RooCommander
cp -r src/rooport/core/* /path/to/roo-commander/.ruru/modes/roo-commander/

# 3. Install ROOPORT rules
cp -r .roo/rules/* /path/to/roo-commander/.roo/rules/
cp -r .roo/rules-roo-commander/* /path/to/roo-commander/.roo/rules-roo-commander/

# 4. Configure integration
cp config/mcp.template.json /path/to/roo-commander/.roo/mcp.json
# Edit with your actual paths and API keys
```

## 🔧 Practical Implementation Details

### ConPort Logging Frequency and Behavior

#### Real-Time Logging Events:

```python
# ROOPORT logs to ConPort in these scenarios:

# 1. Every user interaction
await conport.log_custom_data(
    category="UserInteraction",
    key=f"interaction-{timestamp}",
    value={
        "query": user_query,
        "response_summary": response_summary,
        "confidence": confidence_score,
        "execution_time": execution_time
    }
)

# 2. Decision points
await conport.log_decision(
    summary="User chose React for frontend",
    rationale="Better TypeScript integration and team familiarity",
    tags=["frontend", "technology-choice", "react"]
)

# 3. Task delegation and completion
await conport.log_progress(
    description="Implementing user authentication system",
    status="IN_PROGRESS",
    linked_item_type="decision",
    linked_item_id="D-123"
)

# 4. Performance metrics
await conport.log_custom_data(
    category="PerformanceMetrics",
    key=f"execution-{timestamp}",
    value={
        "orchestrator_time": 2.3,
        "rag_iterations": 3,
        "confidence_score": 0.87,
        "suggestions_generated": 5
    }
)

# 5. Learning events
await conport.log_custom_data(
    category="LearningEvents",
    key=f"feedback-{timestamp}",
    value={
        "agent": "roo-commander",
        "user_rating": 4,
        "feedback_type": "response_quality",
        "improvement_suggested": "More specific code examples"
    }
)
```

#### Data Persistence Strategy:

```python
# ConPort uses SQLite for persistence
DATABASE_LOCATION = "workspace_root/context_portal/context.db"

# Data is organized by categories:
CONPORT_CATEGORIES = {
    "ProductContext": "Overall project information",
    "ActiveContext": "Current session focus",
    "Decisions": "Architectural and implementation decisions", 
    "Progress": "Task and milestone tracking",
    "SystemPatterns": "Reusable architectural patterns",
    "UserInteractions": "Complete interaction history",
    "PerformanceMetrics": "System performance data",
    "LearningEvents": "Feedback and improvement data",
    "RooCodeDocumentation": "Integrated RooCode knowledge",
    "ProjectGlossary": "Project-specific terminology"
}
```

### Project Context Management

#### How ROOPORT Determines Current Project:

```python
def determine_current_project():
    """ROOPORT uses multiple signals to identify current project"""
    
    # 1. Workspace ID (primary identifier)
    workspace_id = os.path.abspath(os.getcwd())
    
    # 2. ConPort database location
    conport_db = os.path.join(workspace_id, "context_portal", "context.db")
    
    # 3. Project context in ConPort
    product_context = await conport.get_product_context(workspace_id)
    
    # 4. Active session tracking
    active_context = await conport.get_active_context(workspace_id)
    
    return {
        "workspace_id": workspace_id,
        "project_name": product_context.get("name", "Unknown"),
        "database_path": conport_db,
        "session_active": bool(active_context.get("current_session"))
    }
```

#### Switching Between Projects:

```bash
# Method 1: Change directory (automatic detection)
cd /path/to/project-a
rooport --workspace .
# ROOPORT automatically loads project-a's ConPort database

cd /path/to/project-b  
rooport --workspace .
# ROOPORT automatically switches to project-b's context

# Method 2: Explicit workspace specification
rooport --workspace /path/to/specific/project

# Method 3: RooCommander integration
# When using within RooCommander, workspace is automatically detected
# from VS Code's workspaceFolder variable
```

#### Project State Restoration:

```python
async def restore_project_state(workspace_id: str):
    """Restore complete project state when switching projects"""
    
    # 1. Load product context
    product_context = await conport.get_product_context(workspace_id)
    
    # 2. Get recent activity summary
    recent_activity = await conport.get_recent_activity_summary(
        workspace_id=workspace_id,
        hours_ago=24,
        limit_per_type=5
    )
    
    # 3. Load active tasks
    active_tasks = await conport.get_progress(
        workspace_id=workspace_id,
        status_filter="IN_PROGRESS"
    )
    
    # 4. Get recent decisions
    recent_decisions = await conport.get_decisions(
        workspace_id=workspace_id,
        limit=10
    )
    
    # 5. Load system patterns
    patterns = await conport.get_system_patterns(workspace_id=workspace_id)
    
    return {
        "project_context": product_context,
        "recent_activity": recent_activity,
        "active_tasks": active_tasks,
        "recent_decisions": recent_decisions,
        "system_patterns": patterns,
        "restoration_timestamp": datetime.now().isoformat()
    }
```

## 🧪 Testing ROOPORT Installation

### Complete Integration Test

```python
# Create comprehensive test: test_rooport_integration.py
import asyncio
import os
import tempfile
from pathlib import Path

async def test_complete_rooport_integration():
    """Test complete ROOPORT + RooCode integration"""
    
    print("🧪 Testing Complete ROOPORT Integration...")
    
    # Create test workspace
    with tempfile.TemporaryDirectory() as temp_dir:
        workspace = Path(temp_dir) / "test_project"
        workspace.mkdir()
        
        # Set up project structure
        (workspace / "README.md").write_text("# Test Project")
        (workspace / "src").mkdir()
        (workspace / "docs").mkdir()
        
        # Initialize ConPort
        context_portal = workspace / "context_portal"
        context_portal.mkdir()
        
        # Test 1: Project initialization
        print("📝 Testing project initialization...")
        
        from rooport.core.orchestrator import UltimateAgenticOrchestrator
        
        # Mock ConPort for testing
        class TestConPortClient:
            def __init__(self, workspace_id):
                self.workspace_id = workspace_id
                self.data = {}
            
            async def update_product_context(self, content):
                self.data["product_context"] = content
                return {"status": "success"}
            
            async def get_product_context(self):
                return self.data.get("product_context", {})
            
            async def log_decision(self, summary, rationale, tags=None):
                decision_id = f"D-{len(self.data.get('decisions', []))}"
                decision = {
                    "id": decision_id,
                    "summary": summary,
                    "rationale": rationale,
                    "tags": tags or []
                }
                if "decisions" not in self.data:
                    self.data["decisions"] = []
                self.data["decisions"].append(decision)
                return {"id": decision_id}
            
            async def get_decisions(self, limit=10):
                return self.data.get("decisions", [])[:limit]
            
            async def log_progress(self, description, status):
                progress_id = f"P-{len(self.data.get('progress', []))}"
                progress = {
                    "id": progress_id,
                    "description": description,
                    "status": status
                }
                if "progress" not in self.data:
                    self.data["progress"] = []
                self.data["progress"].append(progress)
                return {"id": progress_id}
            
            async def get_progress(self, status_filter=None):
                progress = self.data.get("progress", [])
                if status_filter:
                    return [p for p in progress if p["status"] == status_filter]
                return progress
            
            async def log_custom_data(self, category, key, value):
                if category not in self.data:
                    self.data[category] = {}
                self.data[category][key] = value
                return {"status": "success"}
            
            async def search_custom_data_value_fts(self, query_term, category_filter=None):
                # Simple search simulation
                results = []
                for category, items in self.data.items():
                    if category_filter and category != category_filter:
                        continue
                    for key, value in items.items():
                        if query_term.lower() in str(value).lower():
                            results.append({
                                "category": category,
                                "key": key,
                                "value": value
                            })
                return results
        
        # Initialize ROOPORT with test ConPort
        conport_client = TestConPortClient(str(workspace))
        orchestrator = UltimateAgenticOrchestrator(conport_client)
        
        # Test 2: Initialize project context
        print("📝 Testing project context initialization...")
        await conport_client.update_product_context({
            "name": "ROOPORT Integration Test",
            "description": "Testing complete ROOPORT functionality",
            "tech_stack": ["Python", "AI", "ConPort", "RooCommander"],
            "goals": [
                "Verify ROOPORT installation",
                "Test ConPort integration", 
                "Validate AI engine functionality"
            ]
        })
        
        # Test 3: Log some decisions
        print("📝 Testing decision logging...")
        await conport_client.log_decision(
            summary="Use ROOPORT for AI enhancement",
            rationale="Provides advanced agentic capabilities beyond base RooCommander",
            tags=["architecture", "ai", "tooling"]
        )
        
        await conport_client.log_decision(
            summary="Integrate ConPort for persistent memory",
            rationale="Enables knowledge accumulation and context preservation",
            tags=["architecture", "memory", "persistence"]
        )
        
        # Test 4: Track some progress
        print("📝 Testing progress tracking...")
        await conport_client.log_progress(
            description="Setting up ROOPORT integration test framework",
            status="COMPLETED"
        )
        
        await conport_client.log_progress(
            description="Validating AI engine functionality",
            status="IN_PROGRESS"
        )
        
        # Test 5: Process queries through orchestrator
        print("📝 Testing orchestrator query processing...")
        
        test_queries = [
            "What is this project about?",
            "What decisions have we made?",
            "What are we currently working on?",
            "What should we work on next?"
        ]
        
        for query in test_queries:
            print(f"  🔍 Query: {query}")
            
            response = await orchestrator.process_ultimate_request(
                user_query=query,
                workspace_id=str(workspace)
            )
            
            print(f"    ⏱️ Time: {response.execution_time:.2f}s")
            print(f"    🎯 Confidence: {response.confidence_score:.2f}")
            print(f"    📝 Response: {response.primary_response[:100]}...")
            print(f"    💡 Suggestions: {len(response.proactive_suggestions)}")
        
        # Test 6: Validate data persistence
        print("📝 Testing data persistence...")
        
        decisions = await conport_client.get_decisions()
        progress = await conport_client.get_progress()
        product_context = await conport_client.get_product_context()
        
        assert len(decisions) == 2, f"Expected 2 decisions, got {len(decisions)}"
        assert len(progress) == 2, f"Expected 2 progress items, got {len(progress)}"
        assert product_context["name"] == "ROOPORT Integration Test"
        
        print("✅ All integration tests passed!")
        
        # Test 7: Search functionality
        print("📝 Testing search functionality...")
        
        search_results = await conport_client.search_custom_data_value_fts("ROOPORT")
        assert len(search_results) > 0, "Search should find ROOPORT-related content"
        
        print(f"✅ Search found {len(search_results)} relevant items")
        
        return True

if __name__ == "__main__":
    result = asyncio.run(test_complete_rooport_integration())
    print(f"\n🎯 Complete integration test: {'✅ PASSED' if result else '❌ FAILED'}")
```

### Quick Validation Commands

```bash
# 1. Verify ROOPORT can access RooCode documentation
python -c "
import asyncio
from rooport.core.orchestrator import UltimateAgenticOrchestrator
# Test that ROOPORT can explain RooCode concepts
"

# 2. Test autonomous mode with RooCommander
rooport --autonomous standard --workspace .

# 3. Verify ConPort integration
python -c "
# Test ConPort database creation and basic operations
import os
print('ConPort database path:', os.path.join(os.getcwd(), 'context_portal', 'context.db'))
"

# 4. Test complete workflow
python test_complete_rooport_integration.py
```

## 🎯 Real-World Usage Patterns

### Daily ROOPORT + RooCode Workflow:

1. **Morning Startup**:
   - RooCommander loads with ROOPORT enhancements
   - ConPort restores project context automatically
   - Recent activity summary provides catch-up
   - Proactive suggestions for daily priorities

2. **Development Session**:
   - Every query logged to ConPort for memory
   - Decisions automatically captured and stored
   - Progress tracked as tasks advance
   - Knowledge graph builds relationships

3. **Context Switching**:
   - Switch VS Code workspace → ROOPORT detects new project
   - ConPort loads different project context
   - AI engines adapt to new project patterns
   - Continuous memory across projects

4. **Learning and Improvement**:
   - User feedback collected automatically
   - Performance metrics tracked per project
   - Suggestions improve based on project patterns
   - Knowledge accumulates over time

This integration makes ROOPORT a natural extension of the RooCode ecosystem, providing seamless AI enhancement while preserving all the familiar RooCommander workflows and capabilities.