"""
ROOPORT: The Ultimate Agentic Coding Tool

A revolutionary AI-enhanced development assistant with autonomous operation,
continuous learning, and proactive orchestration capabilities.
"""

__version__ = "1.0.0"
__author__ = "ROOPORT Development Team"

from .core.orchestrator import UltimateAgenticOrchestrator
from .core.rag_engine import AgenticRAGEngine
from .core.learning_system import ContinuousLearningSystem
from .core.proactive_engine import ProactiveOrchestrationEngine

__all__ = [
    "UltimateAgenticOrchestrator",
    "AgenticRAGEngine", 
    "ContinuousLearningSystem",
    "ProactiveOrchestrationEngine",
]