"""
Hybrid Retriever - Combines ConPort and Vector retrieval strategies
Elite Field Service SaaS Platform

Provides intelligent fusion of:
- ConPort project memory (decisions, patterns, progress)
- Vector semantic search (code, documentation, comments)
- Adaptive strategy selection based on query analysis
- Multi-modal result fusion and ranking
"""

import asyncio
from typing import Dict, List, Any, Optional, Tuple, Union
from datetime import datetime
import logging
from enum import Enum

from .conport_retriever import ConPortRetriever
from .vector_retriever import VectorRetriever

logger = logging.getLogger(__name__)


class FusionStrategy(Enum):
    """Strategies for combining ConPort and vector search results"""
    WEIGHTED_AVERAGE = "weighted_average"
    RECIPROCAL_RANK_FUSION = "rrf"
    CONFIDENCE_BASED = "confidence_based" 
    ADAPTIVE = "adaptive"
    SEQUENTIAL = "sequential"


class QueryType(Enum):
    """Detected query types for adaptive retrieval"""
    DECISION_FOCUSED = "decision"
    TECHNICAL_CODE = "code"
    ARCHITECTURAL = "architecture"
    PROGRESS_STATUS = "progress"
    GENERAL_SEARCH = "general"
    MIXED = "mixed"


class HybridRetriever:
    """
    Intelligent hybrid retrieval combining ConPort memory and vector search
    
    Features:
    - Automatic query type detection
    - Adaptive strategy selection
    - Multi-modal result fusion
    - Performance optimization
    - Relevance scoring and ranking
    """
    
    def __init__(
        self,
        conport_retriever: ConPortRetriever,
        vector_retriever: VectorRetriever,
        config: Optional[Dict[str, Any]] = None
    ):
        """
        Initialize hybrid retriever
        
        Args:
            conport_retriever: ConPort memory retriever instance
            vector_retriever: Vector semantic search retriever instance
            config: Configuration options for hybrid retrieval
        """
        self.conport_retriever = conport_retriever
        self.vector_retriever = vector_retriever
        
        self.config = {
            'default_fusion_strategy': FusionStrategy.ADAPTIVE,
            'conport_weight': 0.6,
            'vector_weight': 0.4,
            'max_total_results': 25,
            'confidence_threshold': 0.5,
            'enable_query_expansion': True,
            'enable_result_deduplication': True,
            'parallel_execution': True,
            'timeout_seconds': 30.0,
            'adaptive_weights': True,
            **(config or {})
        }
        
        # Performance and analytics
        self.metrics = {
            'total_queries': 0,
            'conport_queries': 0,
            'vector_queries': 0,
            'hybrid_queries': 0,
            'avg_response_time': 0.0,
            'fusion_strategy_usage': {strategy.value: 0 for strategy in FusionStrategy},
            'query_type_distribution': {qtype.value: 0 for qtype in QueryType},
            'avg_relevance_score': 0.0
        }
        
        # Query analysis cache
        self._query_analysis_cache = {}
        self._analysis_cache_max_size = 200
    
    async def retrieve(
        self,
        query: str,
        workspace_id: str,
        fusion_strategy: Optional[FusionStrategy] = None,
        max_results: Optional[int] = None,
        custom_weights: Optional[Dict[str, float]] = None,
        retrieval_hints: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """
        Perform hybrid retrieval combining ConPort and vector search
        
        Args:
            query: Natural language query
            workspace_id: ConPort workspace identifier
            fusion_strategy: Strategy for combining results
            max_results: Maximum number of results to return
            custom_weights: Custom weights for ConPort vs vector results
            retrieval_hints: Additional hints for retrieval strategy
            
        Returns:
            Fused and ranked list of results from both sources
        """
        start_time = datetime.now()
        
        try:
            # Analyze query to determine optimal strategy
            query_analysis = await self._analyze_query(query, retrieval_hints)
            
            # Select fusion strategy
            strategy = fusion_strategy or self._select_fusion_strategy(query_analysis)
            
            # Determine retrieval weights
            weights = self._calculate_retrieval_weights(
                query_analysis, custom_weights
            )
            
            # Execute retrieval strategy
            results = await self._execute_retrieval_strategy(
                query, workspace_id, strategy, weights, query_analysis, max_results
            )
            
            # Post-process results
            final_results = await self._post_process_results(
                results, query, query_analysis
            )
            
            # Update metrics
            execution_time = (datetime.now() - start_time).total_seconds()
            self._update_metrics(execution_time, strategy, query_analysis, len(final_results))
            
            return final_results
            
        except Exception as e:
            logger.error(f"Hybrid retrieval failed: {e}")
            execution_time = (datetime.now() - start_time).total_seconds()
            self._update_metrics(execution_time, strategy, query_analysis, 0, success=False)
            return []
    
    async def retrieve_with_explanation(
        self,
        query: str,
        workspace_id: str,
        **kwargs
    ) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
        """
        Perform retrieval with detailed explanation of strategy and results
        
        Returns:
            Tuple of (results, explanation_metadata)
        """
        start_time = datetime.now()
        
        # Analyze query
        query_analysis = await self._analyze_query(query, kwargs.get('retrieval_hints'))
        
        # Track decision process
        explanation = {
            'query_analysis': query_analysis,
            'strategy_selection': {},
            'retrieval_execution': {},
            'fusion_details': {},
            'performance_metrics': {}
        }
        
        # Select strategy with explanation
        strategy = kwargs.get('fusion_strategy') or self._select_fusion_strategy(query_analysis)
        explanation['strategy_selection'] = {
            'selected_strategy': strategy.value,
            'reasoning': self._explain_strategy_selection(query_analysis, strategy)
        }
        
        # Execute retrieval
        results = await self.retrieve(query, workspace_id, **kwargs)
        
        # Add execution details
        explanation['retrieval_execution'] = {
            'total_results': len(results),
            'execution_time': (datetime.now() - start_time).total_seconds(),
            'sources_used': list(set(r.get('source', 'unknown') for r in results))
        }
        
        return results, explanation
    
    async def _analyze_query(
        self, 
        query: str, 
        hints: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Analyze query to determine optimal retrieval strategy
        
        Returns:
            Analysis including query type, confidence, and retrieval recommendations
        """
        # Check cache first
        cache_key = f"{query}:{str(hints)}"
        if cache_key in self._query_analysis_cache:
            return self._query_analysis_cache[cache_key]
        
        analysis = {
            'query': query,
            'query_type': self._detect_query_type(query),
            'confidence': 0.0,
            'keywords': self._extract_keywords(query),
            'conport_relevance': 0.0,
            'vector_relevance': 0.0,
            'complexity_score': self._calculate_complexity_score(query),
            'recommendations': {}
        }
        
        # Apply hints if provided
        if hints:
            analysis.update(hints)
        
        # Calculate relevance scores for each retrieval type
        analysis['conport_relevance'] = self._calculate_conport_relevance(query, analysis)
        analysis['vector_relevance'] = self._calculate_vector_relevance(query, analysis)
        
        # Generate recommendations
        analysis['recommendations'] = self._generate_retrieval_recommendations(analysis)
        
        # Cache the analysis
        self._cache_query_analysis(cache_key, analysis)
        
        return analysis
    
    def _detect_query_type(self, query: str) -> QueryType:
        """Detect the primary type of the query"""
        query_lower = query.lower()
        
        # Decision-focused queries
        if any(word in query_lower for word in [
            'decision', 'decide', 'choice', 'rationale', 'why', 'because', 'chosen'
        ]):
            return QueryType.DECISION_FOCUSED
        
        # Technical/code queries
        elif any(word in query_lower for word in [
            'function', 'class', 'method', 'code', 'implementation', 'algorithm',
            'bug', 'error', 'exception', 'debug', 'refactor'
        ]):
            return QueryType.TECHNICAL_CODE
        
        # Architectural queries
        elif any(word in query_lower for word in [
            'architecture', 'design', 'pattern', 'structure', 'system',
            'component', 'module', 'service', 'api'
        ]):
            return QueryType.ARCHITECTURAL
        
        # Progress/status queries
        elif any(word in query_lower for word in [
            'progress', 'status', 'task', 'todo', 'completion', 'done',
            'milestone', 'deadline', 'schedule'
        ]):
            return QueryType.PROGRESS_STATUS
        
        # Mixed indicators
        elif len([word for word in query_lower.split() if word in [
            'decision', 'code', 'architecture', 'progress'
        ]]) > 1:
            return QueryType.MIXED
        
        else:
            return QueryType.GENERAL_SEARCH
    
    def _extract_keywords(self, query: str) -> List[str]:
        """Extract important keywords from query"""
        # Simple keyword extraction - could be enhanced with NLP
        import re
        
        # Remove common stop words
        stop_words = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
            'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'have',
            'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should'
        }
        
        # Extract words (alphanumeric + underscores)
        words = re.findall(r'\b\w+\b', query.lower())
        keywords = [word for word in words if word not in stop_words and len(word) > 2]
        
        return keywords[:10]  # Limit to top 10 keywords
    
    def _calculate_complexity_score(self, query: str) -> float:
        """Calculate query complexity score (0.0 to 1.0)"""
        factors = {
            'length': min(len(query) / 200, 1.0),  # Normalize to 200 chars
            'word_count': min(len(query.split()) / 20, 1.0),  # Normalize to 20 words
            'question_words': len([w for w in query.lower().split() if w in [
                'what', 'how', 'why', 'when', 'where', 'which', 'who'
            ]]) / len(query.split()),
            'technical_terms': len([w for w in query.lower().split() if w in [
                'architecture', 'implementation', 'algorithm', 'optimization',
                'integration', 'deployment', 'scalability', 'performance'
            ]]) / len(query.split())
        }
        
        # Weighted combination
        complexity = (
            factors['length'] * 0.2 +
            factors['word_count'] * 0.3 +
            factors['question_words'] * 0.3 +
            factors['technical_terms'] * 0.2
        )
        
        return min(complexity, 1.0)
    
    def _calculate_conport_relevance(self, query: str, analysis: Dict[str, Any]) -> float:
        """Calculate how relevant ConPort retrieval is for this query"""
        query_type = analysis['query_type']
        
        # Base relevance by query type
        type_relevance = {
            QueryType.DECISION_FOCUSED: 0.9,
            QueryType.PROGRESS_STATUS: 0.8,
            QueryType.ARCHITECTURAL: 0.7,
            QueryType.MIXED: 0.6,
            QueryType.GENERAL_SEARCH: 0.5,
            QueryType.TECHNICAL_CODE: 0.3
        }
        
        base_score = type_relevance.get(query_type, 0.5)
        
        # Adjust based on keywords
        conport_keywords = {
            'decision', 'pattern', 'progress', 'task', 'rationale',
            'choice', 'milestone', 'completion', 'architecture'
        }
        
        keyword_boost = len(set(analysis['keywords']).intersection(conport_keywords)) / len(analysis['keywords']) if analysis['keywords'] else 0
        
        return min(base_score + (keyword_boost * 0.3), 1.0)
    
    def _calculate_vector_relevance(self, query: str, analysis: Dict[str, Any]) -> float:
        """Calculate how relevant vector search is for this query"""
        query_type = analysis['query_type']
        
        # Base relevance by query type
        type_relevance = {
            QueryType.TECHNICAL_CODE: 0.9,
            QueryType.GENERAL_SEARCH: 0.8,
            QueryType.ARCHITECTURAL: 0.7,
            QueryType.MIXED: 0.6,
            QueryType.DECISION_FOCUSED: 0.4,
            QueryType.PROGRESS_STATUS: 0.3
        }
        
        base_score = type_relevance.get(query_type, 0.5)
        
        # Adjust based on keywords
        vector_keywords = {
            'code', 'function', 'class', 'method', 'implementation',
            'algorithm', 'similar', 'like', 'example', 'documentation'
        }
        
        keyword_boost = len(set(analysis['keywords']).intersection(vector_keywords)) / len(analysis['keywords']) if analysis['keywords'] else 0
        
        return min(base_score + (keyword_boost * 0.3), 1.0)
    
    def _generate_retrieval_recommendations(self, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Generate recommendations for retrieval strategy"""
        conport_rel = analysis['conport_relevance']
        vector_rel = analysis['vector_relevance']
        
        recommendations = {
            'primary_source': 'conport' if conport_rel > vector_rel else 'vector',
            'use_both': abs(conport_rel - vector_rel) < 0.3,
            'suggested_weights': {
                'conport': conport_rel / (conport_rel + vector_rel),
                'vector': vector_rel / (conport_rel + vector_rel)
            },
            'confidence': max(conport_rel, vector_rel)
        }
        
        return recommendations
    
    def _select_fusion_strategy(self, query_analysis: Dict[str, Any]) -> FusionStrategy:
        """Select optimal fusion strategy based on query analysis"""
        if self.config['default_fusion_strategy'] != FusionStrategy.ADAPTIVE:
            return self.config['default_fusion_strategy']
        
        query_type = query_analysis['query_type']
        complexity = query_analysis['complexity_score']
        confidence = query_analysis['recommendations']['confidence']
        
        # Strategy selection logic
        if query_type == QueryType.MIXED or complexity > 0.7:
            return FusionStrategy.RECIPROCAL_RANK_FUSION
        elif confidence > 0.8:
            return FusionStrategy.CONFIDENCE_BASED
        elif query_type in [QueryType.DECISION_FOCUSED, QueryType.PROGRESS_STATUS]:
            return FusionStrategy.SEQUENTIAL  # ConPort first, then vector
        else:
            return FusionStrategy.WEIGHTED_AVERAGE
    
    def _calculate_retrieval_weights(
        self,
        query_analysis: Dict[str, Any],
        custom_weights: Optional[Dict[str, float]] = None
    ) -> Dict[str, float]:
        """Calculate optimal weights for ConPort vs vector retrieval"""
        if custom_weights:
            return custom_weights
        
        if not self.config['adaptive_weights']:
            return {
                'conport': self.config['conport_weight'],
                'vector': self.config['vector_weight']
            }
        
        # Use analysis-based weights
        suggested_weights = query_analysis['recommendations']['suggested_weights']
        
        return {
            'conport': suggested_weights['conport'],
            'vector': suggested_weights['vector']
        }
    
    async def _execute_retrieval_strategy(
        self,
        query: str,
        workspace_id: str,
        strategy: FusionStrategy,
        weights: Dict[str, float],
        query_analysis: Dict[str, Any],
        max_results: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """Execute the selected retrieval strategy"""
        max_results = max_results or self.config['max_total_results']
        
        if strategy == FusionStrategy.SEQUENTIAL:
            return await self._execute_sequential_retrieval(
                query, workspace_id, weights, query_analysis, max_results
            )
        
        else:
            # For other strategies, retrieve from both sources in parallel
            conport_results, vector_results = await self._retrieve_from_both_sources(
                query, workspace_id, query_analysis, max_results
            )
            
            # Apply fusion strategy
            if strategy == FusionStrategy.WEIGHTED_AVERAGE:
                return self._fuse_weighted_average(conport_results, vector_results, weights)
            
            elif strategy == FusionStrategy.RECIPROCAL_RANK_FUSION:
                return self._fuse_reciprocal_rank_fusion(conport_results, vector_results, weights)
            
            elif strategy == FusionStrategy.CONFIDENCE_BASED:
                return self._fuse_confidence_based(conport_results, vector_results, query_analysis)
            
            else:
                # Default fallback
                return self._fuse_weighted_average(conport_results, vector_results, weights)
    
    async def _retrieve_from_both_sources(
        self,
        query: str,
        workspace_id: str,
        query_analysis: Dict[str, Any],
        max_results: int
    ) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
        """Retrieve from both ConPort and vector sources in parallel"""
        try:
            if self.config['parallel_execution']:
                # Execute both retrievals concurrently
                conport_task = self._retrieve_from_conport(
                    query, workspace_id, query_analysis, max_results // 2
                )
                vector_task = self._retrieve_from_vector(
                    query, query_analysis, max_results // 2
                )
                
                conport_results, vector_results = await asyncio.gather(
                    conport_task, vector_task, return_exceptions=True
                )
                
                # Handle exceptions
                if isinstance(conport_results, Exception):
                    logger.error(f"ConPort retrieval failed: {conport_results}")
                    conport_results = []
                
                if isinstance(vector_results, Exception):
                    logger.error(f"Vector retrieval failed: {vector_results}")
                    vector_results = []
            
            else:
                # Execute sequentially
                conport_results = await self._retrieve_from_conport(
                    query, workspace_id, query_analysis, max_results // 2
                )
                vector_results = await self._retrieve_from_vector(
                    query, query_analysis, max_results // 2
                )
            
            return conport_results, vector_results
            
        except Exception as e:
            logger.error(f"Dual source retrieval failed: {e}")
            return [], []
    
    async def _retrieve_from_conport(
        self,
        query: str,
        workspace_id: str,
        query_analysis: Dict[str, Any],
        max_results: int
    ) -> List[Dict[str, Any]]:
        """Retrieve from ConPort with query-specific optimization"""
        try:
            # Determine retrieval types based on query analysis
            query_type = query_analysis['query_type']
            
            if query_type == QueryType.DECISION_FOCUSED:
                retrieval_types = ['decisions', 'custom_data']
            elif query_type == QueryType.PROGRESS_STATUS:
                retrieval_types = ['progress', 'decisions']
            elif query_type == QueryType.ARCHITECTURAL:
                retrieval_types = ['patterns', 'decisions', 'custom_data']
            else:
                retrieval_types = None  # Let ConPort retriever decide
            
            results = await self.conport_retriever.retrieve_by_query(
                query=query,
                workspace_id=workspace_id,
                retrieval_types=retrieval_types,
                max_items=max_results
            )
            
            # Add source metadata
            for result in results:
                result['hybrid_source'] = 'conport'
            
            return results
            
        except Exception as e:
            logger.error(f"ConPort retrieval in hybrid mode failed: {e}")
            return []
    
    async def _retrieve_from_vector(
        self,
        query: str,
        query_analysis: Dict[str, Any],
        max_results: int
    ) -> List[Dict[str, Any]]:
        """Retrieve from vector search with query-specific optimization"""
        try:
            # Determine content types based on query analysis
            query_type = query_analysis['query_type']
            
            if query_type == QueryType.TECHNICAL_CODE:
                content_types = ['code', 'comments']
            elif query_type in [QueryType.ARCHITECTURAL, QueryType.GENERAL_SEARCH]:
                content_types = ['docs', 'code', 'comments']
            else:
                content_types = None  # Let vector retriever decide
            
            results = await self.vector_retriever.retrieve_by_similarity(
                query=query,
                content_types=content_types,
                max_results=max_results
            )
            
            # Add source metadata
            for result in results:
                result['hybrid_source'] = 'vector'
            
            return results
            
        except Exception as e:
            logger.error(f"Vector retrieval in hybrid mode failed: {e}")
            return []
    
    async def _execute_sequential_retrieval(
        self,
        query: str,
        workspace_id: str,
        weights: Dict[str, float],
        query_analysis: Dict[str, Any],
        max_results: int
    ) -> List[Dict[str, Any]]:
        """Execute sequential retrieval (primary source first, then secondary)"""
        primary_source = query_analysis['recommendations']['primary_source']
        
        if primary_source == 'conport':
            # ConPort first, then vector to supplement
            primary_results = await self._retrieve_from_conport(
                query, workspace_id, query_analysis, int(max_results * 0.7)
            )
            
            # Only use vector if ConPort results are insufficient
            if len(primary_results) < max_results * 0.5:
                secondary_results = await self._retrieve_from_vector(
                    query, query_analysis, max_results - len(primary_results)
                )
                return primary_results + secondary_results
            else:
                return primary_results[:max_results]
        
        else:
            # Vector first, then ConPort to supplement
            primary_results = await self._retrieve_from_vector(
                query, query_analysis, int(max_results * 0.7)
            )
            
            # Only use ConPort if vector results are insufficient
            if len(primary_results) < max_results * 0.5:
                secondary_results = await self._retrieve_from_conport(
                    query, workspace_id, query_analysis, max_results - len(primary_results)
                )
                return primary_results + secondary_results
            else:
                return primary_results[:max_results]
    
    def _fuse_weighted_average(
        self,
        conport_results: List[Dict[str, Any]],
        vector_results: List[Dict[str, Any]],
        weights: Dict[str, float]
    ) -> List[Dict[str, Any]]:
        """Fuse results using weighted average of relevance scores"""
        all_results = []
        
        # Weight ConPort results
        for result in conport_results:
            weighted_result = result.copy()
            original_score = result.get('relevance_score', result.get('similarity_score', 0.5))
            weighted_result['fusion_score'] = original_score * weights['conport']
            weighted_result['fusion_method'] = 'weighted_average'
            all_results.append(weighted_result)
        
        # Weight vector results
        for result in vector_results:
            weighted_result = result.copy()
            original_score = result.get('similarity_score', result.get('relevance_score', 0.5))
            weighted_result['fusion_score'] = original_score * weights['vector']
            weighted_result['fusion_method'] = 'weighted_average'
            all_results.append(weighted_result)
        
        # Sort by fusion score
        all_results.sort(key=lambda x: x.get('fusion_score', 0.0), reverse=True)
        
        return all_results
    
    def _fuse_reciprocal_rank_fusion(
        self,
        conport_results: List[Dict[str, Any]],
        vector_results: List[Dict[str, Any]],
        weights: Dict[str, float]
    ) -> List[Dict[str, Any]]:
        """Fuse results using Reciprocal Rank Fusion"""
        document_scores = {}
        
        # Process ConPort results
        for rank, result in enumerate(conport_results):
            doc_id = self._get_result_id(result)
            rrf_score = weights['conport'] / (60 + rank)
            
            if doc_id in document_scores:
                document_scores[doc_id]['score'] += rrf_score
            else:
                document_scores[doc_id] = {
                    'result': result,
                    'score': rrf_score
                }
        
        # Process vector results
        for rank, result in enumerate(vector_results):
            doc_id = self._get_result_id(result)
            rrf_score = weights['vector'] / (60 + rank)
            
            if doc_id in document_scores:
                document_scores[doc_id]['score'] += rrf_score
            else:
                document_scores[doc_id] = {
                    'result': result,
                    'score': rrf_score
                }
        
        # Create final results
        fused_results = []
        for doc_data in document_scores.values():
            result = doc_data['result'].copy()
            result['fusion_score'] = doc_data['score']
            result['fusion_method'] = 'rrf'
            fused_results.append(result)
        
        # Sort by RRF score
        fused_results.sort(key=lambda x: x['fusion_score'], reverse=True)
        
        return fused_results
    
    def _fuse_confidence_based(
        self,
        conport_results: List[Dict[str, Any]],
        vector_results: List[Dict[str, Any]],
        query_analysis: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Fuse results based on confidence in each source for this query"""
        conport_confidence = query_analysis['conport_relevance']
        vector_confidence = query_analysis['vector_relevance']
        
        all_results = []
        
        # Apply confidence-based scoring
        for result in conport_results:
            confident_result = result.copy()
            original_score = result.get('relevance_score', result.get('similarity_score', 0.5))
            confident_result['fusion_score'] = original_score * conport_confidence
            confident_result['fusion_method'] = 'confidence_based'
            all_results.append(confident_result)
        
        for result in vector_results:
            confident_result = result.copy()
            original_score = result.get('similarity_score', result.get('relevance_score', 0.5))
            confident_result['fusion_score'] = original_score * vector_confidence
            confident_result['fusion_method'] = 'confidence_based'
            all_results.append(confident_result)
        
        # Sort by confidence-adjusted score
        all_results.sort(key=lambda x: x.get('fusion_score', 0.0), reverse=True)
        
        return all_results
    
    async def _post_process_results(
        self,
        results: List[Dict[str, Any]],
        query: str,
        query_analysis: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Post-process fused results"""
        if not results:
            return results
        
        # Apply deduplication if enabled
        if self.config['enable_result_deduplication']:
            results = self._deduplicate_results(results)
        
        # Apply confidence threshold
        results = [
            r for r in results 
            if r.get('fusion_score', 0.0) >= self.config['confidence_threshold']
        ]
        
        # Limit to max results
        max_results = self.config['max_total_results']
        results = results[:max_results]
        
        # Add final metadata
        for result in results:
            result.update({
                'hybrid_retrieval': True,
                'processed_at': datetime.now().isoformat(),
                'query_type': query_analysis['query_type'].value
            })
        
        return results
    
    def _deduplicate_results(self, results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Remove duplicate results based on content similarity"""
        if len(results) <= 1:
            return results
        
        deduplicated = [results[0]]  # Always keep first result
        
        for result in results[1:]:
            is_duplicate = False
            result_content = str(result.get('content', ''))
            
            for existing in deduplicated:
                existing_content = str(existing.get('content', ''))
                
                # Simple content similarity check
                if self._calculate_content_similarity(result_content, existing_content) > 0.8:
                    is_duplicate = True
                    break
            
            if not is_duplicate:
                deduplicated.append(result)
        
        return deduplicated
    
    def _calculate_content_similarity(self, content1: str, content2: str) -> float:
        """Calculate simple content similarity"""
        if not content1 or not content2:
            return 0.0
        
        words1 = set(content1.lower().split())
        words2 = set(content2.lower().split())
        
        if not words1 or not words2:
            return 0.0
        
        intersection = len(words1.intersection(words2))
        union = len(words1.union(words2))
        
        return intersection / union if union > 0 else 0.0
    
    def _get_result_id(self, result: Dict[str, Any]) -> str:
        """Generate unique ID for a result"""
        # Try various ID fields
        for id_field in ['id', 'doc_id', 'document_id']:
            if id_field in result:
                return str(result[id_field])
        
        # Fallback to content hash
        content = str(result.get('content', ''))
        return str(hash(content))
    
    def _explain_strategy_selection(
        self, 
        query_analysis: Dict[str, Any], 
        strategy: FusionStrategy
    ) -> str:
        """Generate human-readable explanation for strategy selection"""
        query_type = query_analysis['query_type'].value
        conport_rel = query_analysis['conport_relevance']
        vector_rel = query_analysis['vector_relevance']
        
        explanations = {
            FusionStrategy.WEIGHTED_AVERAGE: f"Balanced approach chosen for {query_type} query with ConPort relevance {conport_rel:.2f} and vector relevance {vector_rel:.2f}",
            FusionStrategy.RECIPROCAL_RANK_FUSION: f"RRF selected for complex {query_type} query to handle multiple relevant sources",
            FusionStrategy.CONFIDENCE_BASED: f"Confidence-based fusion for high-confidence {query_type} query",
            FusionStrategy.SEQUENTIAL: f"Sequential retrieval prioritizing {'ConPort' if conport_rel > vector_rel else 'vector'} for {query_type} query",
            FusionStrategy.ADAPTIVE: "Adaptive strategy selection based on query analysis"
        }
        
        return explanations.get(strategy, f"Strategy {strategy.value} selected for {query_type} query")
    
    def _cache_query_analysis(self, key: str, analysis: Dict[str, Any]):
        """Cache query analysis results"""
        if len(self._query_analysis_cache) >= self._analysis_cache_max_size:
            # Remove oldest entry
            oldest_key = next(iter(self._query_analysis_cache))
            del self._query_analysis_cache[oldest_key]
        
        self._query_analysis_cache[key] = analysis
    
    def _update_metrics(
        self,
        execution_time: float,
        strategy: FusionStrategy,
        query_analysis: Dict[str, Any],
        num_results: int,
        success: bool = True
    ):
        """Update performance metrics"""
        self.metrics['total_queries'] += 1
        self.metrics['fusion_strategy_usage'][strategy.value] += 1
        self.metrics['query_type_distribution'][query_analysis['query_type'].value] += 1
        
        if success:
            # Update average response time
            total_time = (
                self.metrics['avg_response_time'] * (self.metrics['total_queries'] - 1) +
                execution_time
            )
            self.metrics['avg_response_time'] = total_time / self.metrics['total_queries']
    
    def get_metrics(self) -> Dict[str, Any]:
        """Get current performance metrics"""
        return {
            **self.metrics,
            'conport_retriever_metrics': self.conport_retriever.get_metrics(),
            'vector_retriever_metrics': self.vector_retriever.get_metrics()
        }
    
    def clear_cache(self):
        """Clear all caches"""
        self._query_analysis_cache.clear()
        self.conport_retriever.clear_cache()
        self.vector_retriever.clear_cache()