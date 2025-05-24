# ROOPORT Troubleshooting & FAQ

## 🛠️ Common Issues and Solutions

### Installation Issues

#### Q: "ModuleNotFoundError: No module named 'rooport'"
**Solution:**
```bash
# Ensure you're in the correct directory and have activated your virtual environment
cd rooport
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate     # Windows

# Install in development mode
pip install -e .

# Verify installation
python -c "import rooport; print('ROOPORT installed successfully')"
```

#### Q: "ConPort MCP server not found"
**Solution:**
```bash
# 1. Verify ConPort installation
python -c "import context_portal; print('ConPort installed')"

# 2. Check MCP configuration
cat .roo/mcp.json  # Should include ConPort server configuration

# 3. Verify server executable path
which context-portal-server  # Should return path to executable

# 4. Test server manually
context-portal-server --version
```

#### Q: "Vertex AI authentication failed"
**Solution:**
```bash
# 1. Check environment variables
echo $GOOGLE_APPLICATION_CREDENTIALS
echo $GOOGLE_CLOUD_PROJECT

# 2. Verify credentials file exists
ls -la $GOOGLE_APPLICATION_CREDENTIALS

# 3. Test authentication
python -c "
from google.cloud import aiplatform
aiplatform.init(project='your-project-id')
print('Vertex AI authentication successful')
"

# 4. Alternative: Use gcloud authentication
gcloud auth application-default login
```

### Configuration Issues

#### Q: "ROOPORT can't find workspace"
**Solution:**
```python
# Check workspace detection
import os
print("Current working directory:", os.getcwd())
print("Expected ConPort database:", os.path.join(os.getcwd(), "context_portal", "context.db"))

# Manual workspace specification
from rooport.core.orchestrator import UltimateAgenticOrchestrator
orchestrator = UltimateAgenticOrchestrator(workspace_id="/absolute/path/to/workspace")
```

#### Q: "Autonomous mode not working"
**Solution:**
```bash
# 1. Check autonomous mode configuration
cat .roo/config/autonomous-mode.json

# 2. Verify configuration is valid JSON
python -c "import json; print(json.load(open('.roo/config/autonomous-mode.json')))"

# 3. Reset to default configuration
mkdir -p .roo/config
echo '{"enabled": false, "level": "standard"}' > .roo/config/autonomous-mode.json

# 4. Test mode toggle
python -c "
from rooport.config.autonomous_mode import get_autonomous_mode, set_autonomous_mode
print('Current mode:', get_autonomous_mode())
set_autonomous_mode(True, 'standard')
print('Updated mode:', get_autonomous_mode())
"
```

### Runtime Issues

#### Q: "ConPort database locked"
**Solution:**
```bash
# 1. Check for zombie processes
ps aux | grep context-portal

# 2. Kill any hanging processes
pkill -f context-portal

# 3. Remove lock file if exists
rm -f context_portal/context.db-wal
rm -f context_portal/context.db-shm

# 4. Restart with fresh database connection
python -c "
from context_portal import ConPortClient
client = ConPortClient('.')
print('Database connection restored')
"
```

#### Q: "High memory usage"
**Solution:**
```python
# Monitor memory usage
import psutil
import os

process = psutil.Process(os.getpid())
print(f"Memory usage: {process.memory_info().rss / 1024 / 1024:.2f} MB")

# Enable memory optimization
from rooport.core.orchestrator import UltimateAgenticOrchestrator

# Use memory-efficient settings
orchestrator = UltimateAgenticOrchestrator(
    conport_client=client,
    max_context_size=50000,  # Limit context size
    enable_caching=True,     # Enable response caching
    memory_limit_mb=512      # Set memory limit
)
```

#### Q: "Slow response times"
**Solution:**
```python
# Enable performance monitoring
import time
from rooport.core.orchestrator import UltimateAgenticOrchestrator

async def test_performance():
    start_time = time.time()
    
    response = await orchestrator.process_ultimate_request(
        user_query="Test query",
        workspace_id="."
    )
    
    execution_time = time.time() - start_time
    print(f"Response time: {execution_time:.2f}s")
    
    # Performance optimization suggestions
    if execution_time > 5.0:
        print("Performance tips:")
        print("- Reduce context size")
        print("- Enable caching")
        print("- Use faster AI model")
        print("- Optimize ConPort queries")

# Run performance test
import asyncio
asyncio.run(test_performance())
```

## ❓ Frequently Asked Questions

### General Questions

#### Q: What's the difference between ROOPORT and RooCommander?
**A:** ROOPORT is an advanced enhancement layer that adds agentic capabilities to RooCommander:

- **RooCommander**: Base AI assistant framework with mode system
- **ROOPORT**: Adds RAG, learning, proactive orchestration, and autonomous operation

Think of ROOPORT as "RooCommander Pro" with advanced AI capabilities.

#### Q: Do I need RooCommander to use ROOPORT?
**A:** ROOPORT is designed to integrate with RooCommander, but core components can work standalone:

- **Full Integration**: Best experience with RooCommander + ConPort + ROOPORT
- **Standalone**: Core AI engines can work independently
- **Partial Integration**: Some features work with just ConPort

#### Q: How much does ROOPORT cost to run?
**A:** ROOPORT itself is free and open source. Costs come from AI services:

- **Vertex AI**: ~$0.01-0.05 per query (depending on model)
- **OpenAI**: ~$0.002-0.02 per query 
- **Claude**: ~$0.008-0.024 per query
- **ConPort**: Free (local SQLite database)

Typical usage: $5-20/month for active development.

### Technical Questions

#### Q: How does ROOPORT handle sensitive code?
**A:** ROOPORT includes several privacy protections:

```python
# 1. Local-first architecture
# - ConPort database stays on your machine
# - No code uploaded to external servers (except AI API calls)

# 2. Configurable privacy levels
PRIVACY_SETTINGS = {
    "share_code_snippets": False,     # Don't send code to AI
    "share_file_names": True,         # OK to share file names
    "share_project_structure": True,  # OK to share folder structure
    "local_processing_only": False    # Use only local AI models
}

# 3. Data sanitization
# - Automatically removes API keys, passwords, secrets
# - Configurable filtering for sensitive patterns
# - Option to review before sending to AI
```

#### Q: Can I use ROOPORT with different AI providers?
**A:** Yes, ROOPORT supports multiple AI providers:

```python
# Vertex AI (Google)
ai_config = {
    "provider": "vertex",
    "model": "gemini-pro",
    "project_id": "your-project"
}

# OpenAI
ai_config = {
    "provider": "openai", 
    "model": "gpt-4",
    "api_key": "your-key"
}

# Claude (Anthropic)
ai_config = {
    "provider": "anthropic",
    "model": "claude-3-sonnet",
    "api_key": "your-key"
}

# Local models (Ollama)
ai_config = {
    "provider": "ollama",
    "model": "llama2",
    "base_url": "http://localhost:11434"
}
```

#### Q: How does the learning system work?
**A:** ROOPORT's Continuous Learning System:

1. **Feedback Collection**: Captures user ratings, corrections, preferences
2. **Pattern Analysis**: Identifies what works well vs. what doesn't
3. **Model Adaptation**: Adjusts responses based on learned patterns
4. **Performance Tracking**: Monitors improvement over time

```python
# Example learning cycle
user_feedback = {
    "query": "Implement user authentication",
    "response_rating": 4,  # 1-5 scale
    "corrections": "Needed more security considerations",
    "preferred_approach": "OAuth 2.0 with JWT tokens"
}

# System learns:
# - User prefers OAuth 2.0 for auth
# - Security considerations are important
# - Response quality was good (4/5) but could improve
```

### Integration Questions

#### Q: How do I migrate from plain RooCommander to ROOPORT?
**A:** Migration is designed to be seamless:

```bash
# 1. Install ROOPORT alongside existing RooCommander
cd your-roocommander-project
git clone https://github.com/your-username/rooport.git
cd rooport
pip install -e .

# 2. Copy ROOPORT enhancements to RooCommander
cp -r src/rooport/core/* ../.ruru/modes/roo-commander/
cp -r .roo/rules/* ../.roo/rules/

# 3. Update configuration
cp config/mcp.template.json ../.roo/mcp.json
# Edit with your settings

# 4. Initialize ConPort (preserves existing data)
# ConPort will create database if it doesn't exist
# Existing RooCommander data remains untouched

# 5. Test integration
# Your existing modes, rules, and workflows continue working
# ROOPORT adds new capabilities without breaking existing functionality
```

#### Q: Can I disable ROOPORT features selectively?
**A:** Yes, ROOPORT is modular:

```python
# Disable specific engines
ROOPORT_CONFIG = {
    "agentic_rag_enabled": True,      # Keep RAG
    "proactive_engine_enabled": False, # Disable proactive suggestions
    "learning_system_enabled": True,   # Keep learning
    "autonomous_mode_enabled": False   # Disable autonomous operation
}

# Use only specific components
from rooport.core.rag_engine import AgenticRAGEngine
# Use just the RAG engine without other components
```

### Performance Questions

#### Q: How can I optimize ROOPORT performance?
**A:** Several optimization strategies:

```python
# 1. Enable caching
CACHE_CONFIG = {
    "enable_response_cache": True,
    "cache_ttl_seconds": 3600,
    "max_cache_size_mb": 100
}

# 2. Optimize ConPort queries
# Use specific searches instead of broad queries
await conport.search_decisions_fts("authentication", limit=5)
# Instead of getting all decisions

# 3. Tune AI model selection
# Use faster models for simple queries, advanced models for complex ones
MODEL_SELECTION = {
    "simple_queries": "gemini-flash",    # Fast, cheap
    "complex_queries": "gemini-pro",     # Slower, more capable
    "code_generation": "claude-sonnet"   # Best for code
}

# 4. Batch operations
# Process multiple queries together when possible
queries = ["query1", "query2", "query3"]
responses = await orchestrator.process_batch_requests(queries)
```

#### Q: What are the system requirements?
**A:** Minimum and recommended requirements:

```
Minimum:
- Python 3.8+
- 4GB RAM
- 1GB disk space
- Internet connection (for AI APIs)

Recommended:
- Python 3.10+
- 8GB RAM
- 5GB disk space (for caching and databases)
- SSD storage
- Stable internet (low latency to AI providers)

For heavy usage:
- 16GB+ RAM
- Fast SSD
- Multiple CPU cores
- Dedicated GPU (for local AI models)
```

## 🔧 Debug Mode and Diagnostics

### Enable Debug Logging

```python
import logging

# Enable debug logging for ROOPORT
logging.basicConfig(level=logging.DEBUG)

# Specific component logging
logging.getLogger('rooport.core.orchestrator').setLevel(logging.DEBUG)
logging.getLogger('rooport.core.rag_engine').setLevel(logging.DEBUG)
logging.getLogger('context_portal').setLevel(logging.DEBUG)
```

### Diagnostic Commands

```bash
# System health check
python -c "
import rooport.diagnostics as diag
diag.run_health_check()
"

# Performance profiling
python -c "
import rooport.diagnostics as diag
diag.profile_performance()
"

# Configuration validation
python -c "
import rooport.diagnostics as diag
diag.validate_configuration()
"
```

### Getting Help

#### Community Support
- **GitHub Issues**: https://github.com/your-username/rooport/issues
- **Discussions**: https://github.com/your-username/rooport/discussions
- **RooCode Community**: Join the RooCode Discord/Slack

#### Reporting Bugs
When reporting issues, include:

1. **Environment Details**:
   ```bash
   python --version
   pip list | grep -E "(rooport|context-portal|google-cloud)"
   uname -a  # Linux/Mac
   # or
   systeminfo  # Windows
   ```

2. **Error Logs**:
   ```bash
   # Enable debug logging and capture output
   python your_script.py 2>&1 | tee debug.log
   ```

3. **Configuration** (sanitized):
   ```bash
   # Remove sensitive information before sharing
   cat .roo/mcp.json | sed 's/"api_key": ".*"/"api_key": "REDACTED"/g'
   ```

4. **Minimal Reproduction Case**:
   ```python
   # Provide minimal code that reproduces the issue
   from rooport.core.orchestrator import UltimateAgenticOrchestrator
   
   # Steps to reproduce...
   ```

This troubleshooting guide should help resolve most common issues and provide clear guidance for getting help when needed.