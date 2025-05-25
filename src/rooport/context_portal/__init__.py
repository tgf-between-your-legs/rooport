"""
ConPort - Context Portal Integration Module

This module provides the ConPort (Context Portal) system for persistent project memory,
decision tracking, and knowledge management. ConPort serves as the "memory brain" of
the ultimate agentic tool, storing and retrieving project-specific context.

Key Features:
- Decision tracking and retrieval
- Progress monitoring
- System pattern documentation  
- Custom data storage
- Full-text search capabilities
- Vector-based semantic search
- Knowledge graph relationships

This integration includes the latest bug fixes for:
- Proper timestamp handling in vector metadata (line 91 fix)
- Safe timestamp creation for custom data (line 486 fix)
"""

# Re-export the main MCP handlers for easy access
from .context_portal_mcp.main import main
from .context_portal_mcp.handlers.mcp_handlers import *

__all__ = [
    'main'
]

__version__ = '1.0.0'