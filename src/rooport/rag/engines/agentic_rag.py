"""
Enhanced Agentic RAG Engine for Elite Field Service SaaS Platform

Combines the best features from all discovered RAG implementations:
- Minimal working RAG engine (stable foundation)
- Semantic search capabilities from context-portal
- CONVEX orchestration intelligence
- Multiple retrieval strategies

Key Features:
- Async query processing with multiple retrieval strategies
- ConPort integration for project memory
- Semantic search with ChromaDB
- Information synthesis and validation
- Performance monitoring and optimization
- Error handling and recovery
"""

import logging
import asyncio
from datetime import datetime
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from enum import Enum

logger = logging.getLogger(__name__)


class ConfidenceLevel(Enum):
    """Confidence levels for RAG responses"""
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INSUFFICIENT = "insufficient"


class RetrievalStrategy(Enum):
    """Available retrieval strategies"""
    CONPORT_ONLY = "conport_only"
    SEMANTIC_ONLY = "semantic_only"
    HYBRID = "hybrid"
    AUTO_SELECT = "auto_select"


@dataclass
class AgenticRAGResponse:
    """Response from the Agentic RAG Engine"""
    query: str
    final_answer: str
    confidence_level: ConfidenceLevel
    sources_used: List[str]
    retrieval_strategy: RetrievalStrategy
    retrieved_items: List[Dict[str, Any]]
    relevance_scores: List[float]
    reasoning_chain: List[str]
    execution_time: float
    metadata: Dict[str, Any]
    timestamp: datetime


class AgenticRAGEngine:
    """
    Enhanced Agentic RAG Engine for SaaS orchestration
    
    Provides intelligent query processing with multiple retrieval strategies,
    information synthesis, and performance optimization.
    """
    
    def __init__(self, conport_client, semantic_engine=None, config=None, synthesizer=None):
        """
        Initialize the Agentic RAG Engine
        
        Args:
            conport_client: ConPort MCP client for project memory
            semantic_engine: ChromaDB semantic search engine (optional)
            config: Configuration dictionary (optional)
            synthesizer: Optional InformationSynthesizer instance (for testability/injection)
        """
        self.conport_client = conport_client
        self.semantic_engine = semantic_engine
        self.config = config or self._default_config()
        self.logger = logging.getLogger(__name__)

        # Synthesis engine (for answer generation and validation)
        if synthesizer is not None:
            self.synthesizer = synthesizer
        else:
            from ..synthesizers.information_synthesizer import InformationSynthesizer
            self.synthesizer = InformationSynthesizer()

        # Performance tracking
        self.query_history = []
        self.performance_metrics = {
            'total_queries': 0,
            'avg_response_time': 0.0,
            'success_rate': 0.0
        }
    
    def _default_config(self) -> Dict[str, Any]:
        """Default configuration for the RAG engine"""
        return {
            'max_retrieval_items': 10,
            'confidence_threshold': 0.7,
            'enable_semantic_search': True,
            'enable_query_caching': False,
            'timeout_seconds': 30.0,
            'min_sources_for_high_confidence': 3
        }
    
    async def process_query(self, query: str, workspace_id: str, 
                          strategy: RetrievalStrategy = RetrievalStrategy.AUTO_SELECT,
                          context: Optional[Dict[str, Any]] = None) -> AgenticRAGResponse:
        """
        Process a query using the agentic RAG approach
        
        Args:
            query: User query to process
            workspace_id: Workspace identifier
            strategy: Retrieval strategy to use
            context: Additional context for query processing
            
        Returns:
            AgenticRAGResponse with processed results
        """
        start_time = datetime.now()
        reasoning_chain = []
        
        try:
            self.logger.info(f"Processing RAG query: {query[:50]}...")
            reasoning_chain.append(f"Starting RAG processing for query: {query[:50]}...")
            
            # Step 1: Analyze query and select strategy
            if strategy == RetrievalStrategy.AUTO_SELECT:
                strategy = await self._analyze_and_select_strategy(query, workspace_id)
                reasoning_chain.append(f"Auto-selected strategy: {strategy.value}")
            
            # Step 2: Retrieve information
            retrieved_items, relevance_scores = await self._retrieve_information(
                query, workspace_id, strategy, context
            )
            reasoning_chain.append(f"Retrieved {len(retrieved_items)} items using {strategy.value}")
            
            # Step 3: Synthesize information
            final_answer, confidence = await self._synthesize_information(
                query, retrieved_items, relevance_scores
            )
            reasoning_chain.append(f"Synthesized answer with {confidence.value} confidence")
            
            # Step 4: Extract sources
            sources_used = self._extract_sources(retrieved_items)
            
            # Step 5: Calculate execution time and update metrics
            execution_time = (datetime.now() - start_time).total_seconds()
            await self._update_performance_metrics(True, execution_time)
            
            # Step 6: Create response
            response = AgenticRAGResponse(
                query=query,
                final_answer=final_answer,
                confidence_level=confidence,
                sources_used=sources_used,
                retrieval_strategy=strategy,
                retrieved_items=retrieved_items,
                relevance_scores=relevance_scores,
                reasoning_chain=reasoning_chain,
                execution_time=execution_time,
                metadata={
                    'workspace_id': workspace_id,
                    'items_processed': len(retrieved_items),
                    'strategy_used': strategy.value
                },
                timestamp=start_time
            )
            
            # Step 7: Log successful execution
            await self._log_execution(workspace_id, response)
            
            return response
            
        except Exception as e:
            self.logger.error(f"RAG processing failed: {e}")
            await self._update_performance_metrics(False, 0.0)
            return self._create_error_response(query, str(e), reasoning_chain)
    
    async def _analyze_and_select_strategy(self, query: str, workspace_id: str) -> RetrievalStrategy:
        """
        Analyze query and automatically select optimal retrieval strategy
        
        Args:
            query: User query
            workspace_id: Workspace identifier
            
        Returns:
            Selected RetrievalStrategy
        """
        query_lower = query.lower()
        
        # Simple heuristics for strategy selection
        if any(keyword in query_lower for keyword in ['decision', 'pattern', 'progress', 'custom']):
            return RetrievalStrategy.CONPORT_ONLY
        elif any(keyword in query_lower for keyword in ['semantic', 'similar', 'related', 'like']):
            return RetrievalStrategy.SEMANTIC_ONLY
        else:
            return RetrievalStrategy.HYBRID
    
    async def _retrieve_information(self, query: str, workspace_id: str, 
                                  strategy: RetrievalStrategy,
                                  context: Optional[Dict[str, Any]]) -> tuple[List[Dict], List[float]]:
        """
        Retrieve information using the specified strategy
        
        Args:
            query: User query
            workspace_id: Workspace identifier
            strategy: Retrieval strategy to use
            context: Additional context
            
        Returns:
            Tuple of (retrieved_items, relevance_scores)
        """
        retrieved_items = []
        relevance_scores = []
        
        try:
            if strategy == RetrievalStrategy.CONPORT_ONLY:
                items, scores = await self._retrieve_from_conport(query, workspace_id)
                retrieved_items.extend(items)
                relevance_scores.extend(scores)
                
            elif strategy == RetrievalStrategy.SEMANTIC_ONLY and self.semantic_engine:
                items, scores = await self._retrieve_from_semantic(query, workspace_id)
                retrieved_items.extend(items)
                relevance_scores.extend(scores)
                
            elif strategy == RetrievalStrategy.HYBRID:
                # Parallel retrieval from both sources
                conport_task = self._retrieve_from_conport(query, workspace_id)
                semantic_task = (self._retrieve_from_semantic(query, workspace_id) 
                               if self.semantic_engine else None)
                
                if semantic_task:
                    conport_results, semantic_results = await asyncio.gather(
                        conport_task, semantic_task, return_exceptions=True
                    )
                    
                    if isinstance(conport_results, tuple):
                        retrieved_items.extend(conport_results[0])
                        relevance_scores.extend(conport_results[1])
                    
                    if isinstance(semantic_results, tuple):
                        retrieved_items.extend(semantic_results[0])
                        relevance_scores.extend(semantic_results[1])
                else:
                    items, scores = await conport_task
                    retrieved_items.extend(items)
                    relevance_scores.extend(scores)
            
            # Limit results and deduplicate
            max_items = self.config['max_retrieval_items']
            if len(retrieved_items) > max_items:
                # Sort by relevance and take top items
                sorted_items = sorted(zip(retrieved_items, relevance_scores), 
                                    key=lambda x: x[1], reverse=True)
                retrieved_items = [item for item, _ in sorted_items[:max_items]]
                relevance_scores = [score for _, score in sorted_items[:max_items]]
            
            return retrieved_items, relevance_scores
            
        except Exception as e:
            self.logger.error(f"Information retrieval failed: {e}")
            return [], []
    
    async def _retrieve_from_conport(self, query: str, workspace_id: str) -> tuple[List[Dict], List[float]]:
        """Retrieve information from ConPort"""
        try:
            items = []
            scores = []
            
            # Search decisions
            decision_results = await self.conport_client.search_decisions_fts(
                workspace_id=workspace_id,
                query_term=query,
                limit=5
            )
            if decision_results and 'decisions' in decision_results:
                for decision in decision_results['decisions']:
                    items.append({
                        'type': 'decision',
                        'content': decision.get('summary', ''),
                        'metadata': decision
                    })
                    scores.append(0.8)  # Default score for FTS results
            
            # Search custom data
            custom_results = await self.conport_client.search_custom_data_value_fts(
                workspace_id=workspace_id,
                query_term=query,
                limit=5
            )
            if custom_results and 'results' in custom_results:
                for result in custom_results['results']:
                    items.append({
                        'type': 'custom_data',
                        'content': str(result.get('value', '')),
                        'metadata': result
                    })
                    scores.append(0.7)  # Slightly lower score for custom data
            
            return items, scores
            
        except Exception as e:
            self.logger.error(f"ConPort retrieval failed: {e}")
            return [], []
    
    async def _retrieve_from_semantic(self, query: str, workspace_id: str) -> tuple[List[Dict], List[float]]:
        """Retrieve information using semantic search"""
        try:
            if not self.semantic_engine:
                return [], []
            
            # Perform semantic search
            results = await self.semantic_engine.semantic_search(
                query=query,
                collection_type='decisions',  # Default collection
                limit=5,
                workspace_filter=workspace_id
            )
            
            items = []
            scores = []
            
            for result in results:
                items.append({
                    'type': 'semantic',
                    'content': result.content,
                    'metadata': result.metadata
                })
                scores.append(result.score)
            
            return items, scores
            
        except Exception as e:
            self.logger.error(f"Semantic retrieval failed: {e}")
            return [], []
    
    async def _synthesize_information(self, query: str, items: List[Dict], 
                                    scores: List[float]) -> tuple[str, ConfidenceLevel]:
        """
        Synthesize retrieved information into a coherent answer
        
        Args:
            query: Original query
            items: Retrieved items
            scores: Relevance scores
            
        Returns:
            Tuple of (synthesized_answer, confidence_level)
        """
        if not items:
            return f"No relevant information found for: {query}", ConfidenceLevel.INSUFFICIENT
        
        # Simple synthesis approach
        synthesis_parts = [f"Based on available information regarding '{query}':"]
        
        # Add top items
        for i, item in enumerate(items[:5]):
            content = item.get('content', '')
            if content:
                synthesis_parts.append(f"{i+1}. {content}")
        
        if len(items) > 5:
            synthesis_parts.append(f"Additional information available from {len(items) - 5} more sources.")
        
        synthesized_content = '\n\n'.join(synthesis_parts)
        
        # Calculate confidence
        if not scores:
            confidence = ConfidenceLevel.LOW
        else:
            avg_score = sum(scores) / len(scores)
            source_count = len(items)
            
            if (avg_score >= 0.8 and 
                source_count >= self.config['min_sources_for_high_confidence']):
                confidence = ConfidenceLevel.HIGH
            elif avg_score >= 0.6 and source_count >= 2:
                confidence = ConfidenceLevel.MEDIUM
            elif avg_score >= 0.4:
                confidence = ConfidenceLevel.LOW
            else:
                confidence = ConfidenceLevel.INSUFFICIENT
        
        return synthesized_content, confidence
    
    def _extract_sources(self, items: List[Dict]) -> List[str]:
        """Extract source identifiers from retrieved items"""
        sources = []
        for item in items:
            metadata = item.get('metadata', {})
            if 'id' in metadata:
                source_id = f"{item.get('type', 'unknown')}-{metadata['id']}"
                sources.append(source_id)
            else:
                sources.append(f"{item.get('type', 'unknown')}-{hash(str(item))}")
        return sources
    
    async def _update_performance_metrics(self, success: bool, execution_time: float):
        """Update engine performance metrics"""
        self.performance_metrics['total_queries'] += 1
        
        if success:
            current_avg = self.performance_metrics['avg_response_time']
            total_queries = self.performance_metrics['total_queries']
            self.performance_metrics['avg_response_time'] = (
                (current_avg * (total_queries - 1) + execution_time) / total_queries
            )
        
        # Calculate success rate
        successful_queries = sum(1 for entry in self.query_history if entry.get('success', False))
        if success:
            successful_queries += 1
        
        self.performance_metrics['success_rate'] = successful_queries / self.performance_metrics['total_queries']
    
    async def _log_execution(self, workspace_id: str, response: AgenticRAGResponse):
        """Log successful RAG execution to ConPort"""
        try:
            execution_id = f"RAG-EXEC-{datetime.now().strftime('%Y%m%d%H%M%S')}"
            
            await self.conport_client.log_custom_data(
                workspace_id=workspace_id,
                category="AgenticRAGExecution",
                key=execution_id,
                value={
                    "query": response.query,
                    "confidence_level": response.confidence_level.value,
                    "sources_count": len(response.sources_used),
                    "strategy_used": response.retrieval_strategy.value,
                    "execution_time": response.execution_time,
                    "timestamp": response.timestamp.isoformat()
                }
            )
        except Exception as e:
            self.logger.error(f"Failed to log RAG execution: {e}")
    
    def _create_error_response(self, query: str, error_msg: str, 
                             reasoning_chain: List[str]) -> AgenticRAGResponse:
        """Create error response for failed queries"""
        return AgenticRAGResponse(
            query=query,
            final_answer=f"Error processing query: {error_msg}",
            confidence_level=ConfidenceLevel.INSUFFICIENT,
            sources_used=[],
            retrieval_strategy=RetrievalStrategy.AUTO_SELECT,
            retrieved_items=[],
            relevance_scores=[],
            reasoning_chain=reasoning_chain + [f"Error occurred: {error_msg}"],
            execution_time=0.0,
            metadata={'error': error_msg},
            timestamp=datetime.now()
        )
    
    def get_performance_metrics(self) -> Dict[str, Any]:
        """Get current performance metrics"""
# Integration function for CONVEX system
async def integrate_agentic_rag(conport_client, semantic_engine=None, config=None):
    """
    Integration function for CONVEX Ultimate Agentic Orchestrator
    
    Args:
        conport_client: ConPort client for project memory
        semantic_engine: Optional semantic search engine
        config: Optional configuration dictionary
        
    Returns:
        Configured AgenticRAGEngine instance
    """
    return AgenticRAGEngine(
        conport_client=conport_client,
        semantic_engine=semantic_engine,
        config=config or {}
    )