"""
Enhanced Context Intelligence Engine for RooPort CONVEX v2.0

Provides advanced context synthesis with relevance scoring, parallel retrieval,
and intelligent context prioritization.
"""

import asyncio
import logging
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass
from enum import Enum

import numpy as np
from sentence_transformers import SentenceTransformer

logger = logging.getLogger(__name__)


class ContextType(Enum):
    """Types of context sources"""
    CONPORT_FTS = "conport_fts"
    CONPORT_SEMANTIC = "conport_semantic" 
    CONPORT_GRAPH = "conport_graph"
    CHROMADB_SEMANTIC = "chromadb_semantic"
    AI_PROVIDER = "ai_provider"


@dataclass
class ContextItem:
    """Represents a single context item with metadata"""
    content: str
    source_type: ContextType
    confidence_score: float
    relevance_score: float
    metadata: Dict[str, Any]
    item_id: Optional[str] = None
    relationships: List[str] = None


@dataclass
class ContextSynthesis:
    """Result of context synthesis with scoring"""
    synthesized_context: str
    primary_sources: List[ContextItem]
    confidence_score: float
    relevance_breakdown: Dict[str, float]
    query_analysis: Dict[str, Any]


class ContextIntelligenceEngine:
    """Advanced context synthesis with relevance scoring and ML optimization"""
    
    def __init__(self, conport_client=None, chromadb_client=None):
        self.conport_client = conport_client
        self.chromadb_client = chromadb_client
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        self.confidence_threshold = 0.7
        self.max_context_items = 10
        
        # Context scoring weights
        self.scoring_weights = {
            'semantic_similarity': 0.3,
            'temporal_relevance': 0.2,
            'source_authority': 0.2,
            'cross_reference_strength': 0.15,
            'user_preference_alignment': 0.15
        }
    
    async def enhanced_context_retrieval(
        self, 
        query: str, 
        workspace_id: str,
        context_types: Optional[List[ContextType]] = None
    ) -> ContextSynthesis:
        """
        Enhanced context retrieval with multi-strategy approach and intelligent scoring
        
        Args:
            query: User query or task description
            workspace_id: Target workspace identifier
            context_types: Specific context types to retrieve (optional)
            
        Returns:
            ContextSynthesis with scored and ranked context items
        """
        try:
            # Analyze query to understand intent and requirements
            query_analysis = await self._analyze_query_intent(query)
            
            # Parallel retrieval from multiple sources
            context_items = await self._parallel_context_retrieval(
                query, workspace_id, context_types, query_analysis
            )
            
            # Apply advanced relevance scoring
            scored_items = await self._apply_relevance_scoring(
                context_items, query, query_analysis
            )
            
            # Synthesize optimal context
            synthesis = await self._synthesize_optimal_context(
                scored_items, query, query_analysis
            )
            
            logger.info(f"Context retrieval completed: {len(scored_items)} items, "
                       f"confidence: {synthesis.confidence_score:.3f}")
            
            return synthesis
            
        except Exception as e:
            logger.error(f"Enhanced context retrieval failed: {e}")
            return await self._fallback_context_retrieval(query, workspace_id)
    
    async def _analyze_query_intent(self, query: str) -> Dict[str, Any]:
        """Analyze query to understand intent, entities, and context requirements"""
        
        # Extract query embedding for semantic analysis
        query_embedding = self.embedding_model.encode([query])[0]
        
        # Intent classification (simplified - could use ML model)
        intent_indicators = {
            'code_analysis': ['analyze', 'review', 'check', 'debug', 'fix'],
            'architecture': ['design', 'structure', 'pattern', 'architecture'],
            'implementation': ['implement', 'create', 'build', 'develop'],
            'documentation': ['document', 'explain', 'describe', 'guide'],
            'decision_making': ['decide', 'choose', 'select', 'recommend'],
            'troubleshooting': ['error', 'issue', 'problem', 'bug', 'fix']
        }
        
        detected_intents = []
        query_lower = query.lower()
        
        for intent, indicators in intent_indicators.items():
            if any(indicator in query_lower for indicator in indicators):
                detected_intents.append(intent)
        
        # Entity extraction (simplified)
        entities = self._extract_entities(query)
        
        # Complexity assessment
        complexity_score = min(len(query.split()) / 20.0, 1.0)  # Normalize by word count
        
        return {
            'query_embedding': query_embedding,
            'detected_intents': detected_intents,
            'entities': entities,
            'complexity_score': complexity_score,
            'query_length': len(query),
            'technical_terms': self._extract_technical_terms(query)
        }
    
    async def _parallel_context_retrieval(
        self,
        query: str,
        workspace_id: str,
        context_types: Optional[List[ContextType]],
        query_analysis: Dict[str, Any]
    ) -> List[ContextItem]:
        """Retrieve context from multiple sources in parallel"""
        
        if context_types is None:
            context_types = [
                ContextType.CONPORT_FTS,
                ContextType.CONPORT_SEMANTIC,
                ContextType.CHROMADB_SEMANTIC,
                ContextType.CONPORT_GRAPH
            ]
        
        # Create retrieval tasks
        tasks = []
        
        if ContextType.CONPORT_FTS in context_types and self.conport_client:
            tasks.append(self._retrieve_conport_fts(query, workspace_id))
        
        if ContextType.CHROMADB_SEMANTIC in context_types and self.chromadb_client:
            tasks.append(self._retrieve_chromadb_semantic(query, query_analysis))
        
        if ContextType.CONPORT_GRAPH in context_types and self.conport_client:
            tasks.append(self._retrieve_conport_graph(query, workspace_id))
        
        # Execute retrieval tasks in parallel
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Combine results and filter exceptions
        all_context_items = []
        for result in results:
            if isinstance(result, Exception):
                logger.warning(f"Context retrieval task failed: {result}")
            elif isinstance(result, list):
                all_context_items.extend(result)
        
        return all_context_items
    
    async def _apply_relevance_scoring(
        self,
        context_items: List[ContextItem],
        query: str,
        query_analysis: Dict[str, Any]
    ) -> List[ContextItem]:
        """Apply advanced relevance scoring to context items"""
        
        query_embedding = query_analysis['query_embedding']
        
        for item in context_items:
            # Calculate semantic similarity
            item_embedding = self.embedding_model.encode([item.content])[0]
            semantic_sim = np.dot(query_embedding, item_embedding) / (
                np.linalg.norm(query_embedding) * np.linalg.norm(item_embedding)
            )
            
            # Calculate temporal relevance (more recent = more relevant)
            temporal_score = self._calculate_temporal_relevance(item.metadata)
            
            # Calculate source authority (some sources are more authoritative)
            authority_score = self._calculate_source_authority(item.source_type)
            
            # Calculate cross-reference strength
            cross_ref_score = self._calculate_cross_reference_strength(item)
            
            # Calculate user preference alignment (placeholder)
            preference_score = 0.5  # Would be learned from user behavior
            
            # Weighted relevance score
            relevance_score = (
                semantic_sim * self.scoring_weights['semantic_similarity'] +
                temporal_score * self.scoring_weights['temporal_relevance'] +
                authority_score * self.scoring_weights['source_authority'] +
                cross_ref_score * self.scoring_weights['cross_reference_strength'] +
                preference_score * self.scoring_weights['user_preference_alignment']
            )
            
            item.relevance_score = relevance_score
        
        # Sort by relevance score and limit results
        sorted_items = sorted(context_items, key=lambda x: x.relevance_score, reverse=True)
        return sorted_items[:self.max_context_items]
    
    async def _synthesize_optimal_context(
        self,
        scored_items: List[ContextItem],
        query: str,
        query_analysis: Dict[str, Any]
    ) -> ContextSynthesis:
        """Synthesize optimal context from scored items"""
        
        if not scored_items:
            return ContextSynthesis(
                synthesized_context="No relevant context found.",
                primary_sources=[],
                confidence_score=0.0,
                relevance_breakdown={},
                query_analysis=query_analysis
            )
        
        # Filter items above confidence threshold
        high_confidence_items = [
            item for item in scored_items 
            if item.relevance_score >= self.confidence_threshold
        ]
        
        if not high_confidence_items:
            high_confidence_items = scored_items[:3]  # Take top 3 if none above threshold
        
        # Create synthesized context
        context_parts = []
        for i, item in enumerate(high_confidence_items):
            source_label = f"[Source {i+1}]"
            context_parts.append(f"{source_label} {item.content}")
        
        synthesized_context = "\n\n".join(context_parts)
        
        # Calculate overall confidence
        confidence_score = np.mean([item.relevance_score for item in high_confidence_items])
        
        # Create relevance breakdown
        relevance_breakdown = {
            f"source_{i+1}": item.relevance_score 
            for i, item in enumerate(high_confidence_items)
        }
        
        return ContextSynthesis(
            synthesized_context=synthesized_context,
            primary_sources=high_confidence_items,
            confidence_score=confidence_score,
            relevance_breakdown=relevance_breakdown,
            query_analysis=query_analysis
        )
    
    # Helper methods for retrieval and scoring
    
    async def _retrieve_conport_fts(self, query: str, workspace_id: str) -> List[ContextItem]:
        """Retrieve context using ConPort full-text search"""
        # Implementation would use ConPort FTS APIs
        return []
    
    async def _retrieve_chromadb_semantic(self, query: str, query_analysis: Dict) -> List[ContextItem]:
        """Retrieve context using ChromaDB semantic search"""
        # Implementation would use ChromaDB vector search
        return []
    
    async def _retrieve_conport_graph(self, query: str, workspace_id: str) -> List[ContextItem]:
        """Retrieve context using ConPort graph traversal"""
        # Implementation would use ConPort relationship APIs
        return []
    
    def _extract_entities(self, query: str) -> List[str]:
        """Extract entities from query (simplified implementation)"""
        # Would use NER model in production
        return []
    
    def _extract_technical_terms(self, query: str) -> List[str]:
        """Extract technical terms from query"""
        # Would use technical vocabulary matching
        return []
    
    def _calculate_temporal_relevance(self, metadata: Dict) -> float:
        """Calculate temporal relevance score"""
        # Would consider creation/update timestamps
        return 0.5
    
    def _calculate_source_authority(self, source_type: ContextType) -> float:
        """Calculate source authority score"""
        authority_scores = {
            ContextType.CONPORT_FTS: 0.9,
            ContextType.CONPORT_SEMANTIC: 0.8,
            ContextType.CHROMADB_SEMANTIC: 0.7,
            ContextType.CONPORT_GRAPH: 0.8,
            ContextType.AI_PROVIDER: 0.6
        }
        return authority_scores.get(source_type, 0.5)
    
    def _calculate_cross_reference_strength(self, item: ContextItem) -> float:
        """Calculate cross-reference strength score"""
        # Would analyze relationships and references
        return 0.5
    
    async def _fallback_context_retrieval(self, query: str, workspace_id: str) -> ContextSynthesis:
        """Fallback context retrieval when main system fails"""
        return ContextSynthesis(
            synthesized_context=f"Fallback context for query: {query}",
            primary_sources=[],
            confidence_score=0.3,
            relevance_breakdown={},
            query_analysis={'fallback': True}
        )