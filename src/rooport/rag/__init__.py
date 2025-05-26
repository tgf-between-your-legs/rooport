"""
Unified RAG (Retrieval-Augmented Generation) Module for RooPort
Elite Field Service SaaS Platform

This module provides a consolidated, production-ready RAG system that combines:
- ConPort project memory integration
- Semantic search with ChromaDB
- Multiple retrieval strategies
- Information synthesis and validation
- Performance optimization

Key Components:
- AgenticRAGEngine: Main orchestrator for RAG operations
- ConPortRetriever: Retrieval from ConPort project memory
- VectorRetriever: Semantic search using ChromaDB
- HybridRetriever: Combined retrieval strategies
- InformationSynthesizer: Content synthesis and validation
"""

from .engines.agentic_rag import AgenticRAGEngine, AgenticRAGResponse, ConfidenceLevel
from .retrievers.conport_retriever import ConPortRetriever
from .retrievers.vector_retriever import VectorRetriever
from .retrievers.hybrid_retriever import HybridRetriever
from .synthesizers.information_synthesizer import InformationSynthesizer

__version__ = "2.0.0"
__author__ = "RooPort Development Team"

__all__ = [
    "AgenticRAGEngine",
    "AgenticRAGResponse", 
    "ConfidenceLevel",
    "ConPortRetriever",
    "VectorRetriever",
    "HybridRetriever",
    "InformationSynthesizer"
]

# Integration function for backwards compatibility
async def integrate_agentic_rag(workspace_id: str, query: str, conport_client) -> AgenticRAGResponse:
    """
    Main integration point for agentic RAG in Roo Commander
    
    Args:
        workspace_id: The workspace identifier
        query: User query to process
        conport_client: ConPort MCP client instance
        
    Returns:
        AgenticRAGResponse with processed results
    """
    rag_engine = AgenticRAGEngine(conport_client)
    response = await rag_engine.process_query(query, workspace_id)
    return response