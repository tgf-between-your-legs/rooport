"""
CONVEX (ConPort + Vertex AI) Integration Module

This module provides the CONVEX system - an intelligent query routing and processing
system that combines ConPort's project memory with Vertex AI's research capabilities.

Key Components:
- ConvexOrchestrator: Main orchestrator for intelligent query routing
- Ultimate Agentic Orchestrator: High-level coordination and suggestion system
- Continuous Learning System: Adaptive learning from user feedback
- Proactive Orchestration Engine: Proactive suggestions and optimizations

The CONVEX system provides:
1. Intelligent query intent analysis
2. Optimal routing between ConPort and Vertex AI
3. Continuous learning and improvement
4. Proactive suggestions and optimizations
"""

from .convex_orchestrator import ConvexOrchestrator, QueryIntent, ConfidenceLevel
from .ultimate_agentic_orchestrator import UltimateAgenticOrchestrator # Corrected below to ultimate-agentic-orchestrator
from .continuous_learning_system import ContinuousLearningSystem
from .proactive_orchestration_engine import ProactiveOrchestrationEngine

__all__ = [
    'ConvexOrchestrator',
    'QueryIntent', 
    'ConfidenceLevel',
    'UltimateAgenticOrchestrator' # Corrected below to ultimate-agentic-orchestrator
    'ContinuousLearningSystem',
    'ProactiveOrchestrationEngine'
]

__version__ = '1.0.0'