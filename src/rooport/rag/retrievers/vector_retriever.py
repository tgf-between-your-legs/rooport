"""
Vector Retriever - Semantic search using vector embeddings
Elite Field Service SaaS Platform

Provides semantic similarity search capabilities using:
- ChromaDB vector database
- SentenceTransformer embeddings
- Configurable similarity thresholds
- Multi-modal content support
"""

import asyncio
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime
import logging
import hashlib
import json

logger = logging.getLogger(__name__)


class VectorRetriever:
    """
    Semantic vector search retriever using ChromaDB and SentenceTransformers
    
    Provides similarity search capabilities for:
    - Code semantics and patterns
    - Natural language descriptions
    - Technical documentation
    - Cross-modal content relationships
    """
    
    def __init__(self, semantic_engine=None, config: Optional[Dict[str, Any]] = None):
        """
        Initialize vector retriever
        
        Args:
            semantic_engine: ChromaDB-based semantic search engine
            config: Configuration options for vector retrieval
        """
        self.semantic_engine = semantic_engine
        self.config = {
            'similarity_threshold': 0.7,
            'max_results': 20,
            'embedding_model': 'all-MiniLM-L6-v2',
            'collection_name': 'elite_field_service',
            'enable_reranking': True,
            'diversity_threshold': 0.8,
            'timeout_seconds': 20.0,
            **(config or {})
        }
        
        # Performance tracking
        self.metrics = {
            'total_searches': 0,
            'successful_searches': 0,
            'avg_search_time': 0.0,
            'total_results_returned': 0,
            'avg_similarity_score': 0.0,
            'cache_hits': 0
        }
        
        # Query cache for performance
        self._query_cache = {}
        self._cache_max_size = 100
        
        # Initialize embedding model if semantic engine is available
        self._embedding_model = None
        if self.semantic_engine:
            self._initialize_embedding_model()
    
    def _initialize_embedding_model(self):
        """Initialize the embedding model for query encoding"""
        try:
            # This would typically be initialized through the semantic engine
            # For now, we'll use a placeholder that can be replaced with actual implementation
            self._embedding_model = self.semantic_engine
            logger.info(f"Vector retriever initialized with model: {self.config['embedding_model']}")
        except Exception as e:
            logger.error(f"Failed to initialize embedding model: {e}")
            self._embedding_model = None
    
    async def retrieve_by_similarity(
        self,
        query: str,
        content_types: Optional[List[str]] = None,
        max_results: Optional[int] = None,
        similarity_threshold: Optional[float] = None
    ) -> List[Dict[str, Any]]:
        """
        Retrieve documents by semantic similarity to query
        
        Args:
            query: Natural language query or code snippet
            content_types: Types of content to search ('code', 'docs', 'comments', etc.)
            max_results: Maximum number of results to return
            similarity_threshold: Minimum similarity score (0.0-1.0)
            
        Returns:
            List of similar documents with similarity scores and metadata
        """
        start_time = datetime.now()
        
        try:
            # Check cache first
            cache_key = self._generate_cache_key(query, content_types, max_results, similarity_threshold)
            if cache_key in self._query_cache:
                self.metrics['cache_hits'] += 1
                return self._query_cache[cache_key]
            
            # Set defaults
            max_results = max_results or self.config['max_results']
            similarity_threshold = similarity_threshold or self.config['similarity_threshold']
            
            if not self.semantic_engine:
                logger.warning("No semantic engine available for vector retrieval")
                return []
            
            # Perform semantic search
            search_results = await self._execute_semantic_search(
                query, content_types, max_results, similarity_threshold
            )
            
            # Post-process results
            processed_results = await self._process_search_results(
                search_results, query, similarity_threshold
            )
            
            # Apply re-ranking if enabled
            if self.config['enable_reranking'] and len(processed_results) > 1:
                processed_results = await self._rerank_results(processed_results, query)
            
            # Apply diversity filtering
            final_results = self._apply_diversity_filtering(processed_results)
            
            # Update cache
            self._update_cache(cache_key, final_results)
            
            # Update metrics
            execution_time = (datetime.now() - start_time).total_seconds()
            self._update_metrics(execution_time, len(final_results), final_results)
            
            return final_results
            
        except Exception as e:
            logger.error(f"Vector retrieval failed: {e}")
            execution_time = (datetime.now() - start_time).total_seconds()
            self._update_metrics(execution_time, 0, [], success=False)
            return []
    
    async def retrieve_by_content(
        self,
        content: str,
        content_type: str = 'text',
        exclude_self: bool = True,
        max_results: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """
        Find similar content to a given piece of content
        
        Args:
            content: Content to find similarities for
            content_type: Type of content ('code', 'text', 'documentation')
            exclude_self: Whether to exclude exact matches
            max_results: Maximum number of results
            
        Returns:
            List of similar content items with metadata
        """
        try:
            # Create a search query from the content
            if content_type == 'code':
                # For code, extract meaningful tokens and patterns
                search_query = self._extract_code_concepts(content)
            else:
                # For text, use content directly but limit length
                search_query = content[:500] if len(content) > 500 else content
            
            # Perform similarity search
            results = await self.retrieve_by_similarity(
                search_query,
                content_types=[content_type],
                max_results=max_results
            )
            
            # Filter out exact matches if requested
            if exclude_self:
                content_hash = hashlib.md5(content.encode()).hexdigest()
                results = [
                    r for r in results 
                    if r.get('content_hash') != content_hash
                ]
            
            return results
            
        except Exception as e:
            logger.error(f"Content-based retrieval failed: {e}")
            return []
    
    async def retrieve_multi_modal(
        self,
        queries: Dict[str, str],
        fusion_method: str = 'weighted_average',
        weights: Optional[Dict[str, float]] = None
    ) -> List[Dict[str, Any]]:
        """
        Perform multi-modal retrieval combining different query types
        
        Args:
            queries: Dictionary of query_type -> query_text
            fusion_method: Method for combining results ('weighted_average', 'rrf', 'max')
            weights: Weights for different query types
            
        Returns:
            Fused results from multiple query modalities
        """
        try:
            if not queries:
                return []
            
            # Default weights
            if not weights:
                weights = {query_type: 1.0 for query_type in queries.keys()}
            
            # Execute searches for each query type
            search_tasks = []
            for query_type, query_text in queries.items():
                task = self.retrieve_by_similarity(
                    query_text,
                    content_types=[query_type] if query_type in ['code', 'docs', 'comments'] else None
                )
                search_tasks.append((query_type, task))
            
            # Collect results
            type_results = {}
            for query_type, task in search_tasks:
                try:
                    results = await task
                    type_results[query_type] = results
                except Exception as e:
                    logger.warning(f"Failed to retrieve for {query_type}: {e}")
                    type_results[query_type] = []
            
            # Fuse results based on method
            if fusion_method == 'weighted_average':
                fused_results = self._fuse_weighted_average(type_results, weights)
            elif fusion_method == 'rrf':
                fused_results = self._fuse_reciprocal_rank_fusion(type_results, weights)
            elif fusion_method == 'max':
                fused_results = self._fuse_max_score(type_results, weights)
            else:
                logger.warning(f"Unknown fusion method: {fusion_method}")
                # Fallback to concatenation
                fused_results = []
                for results in type_results.values():
                    fused_results.extend(results)
            
            return fused_results
            
        except Exception as e:
            logger.error(f"Multi-modal retrieval failed: {e}")
            return []
    
    async def _execute_semantic_search(
        self,
        query: str,
        content_types: Optional[List[str]],
        max_results: int,
        similarity_threshold: float
    ) -> List[Dict[str, Any]]:
        """Execute the actual semantic search"""
        try:
            # Use the semantic engine's search functionality
            if hasattr(self.semantic_engine, 'semantic_search'):
                results = await self.semantic_engine.semantic_search(
                    query=query,
                    max_results=max_results,
                    similarity_threshold=similarity_threshold
                )
                return results
            else:
                # Fallback method if semantic_search method is different
                logger.warning("Semantic engine doesn't have expected interface")
                return []
                
        except Exception as e:
            logger.error(f"Semantic search execution failed: {e}")
            return []
    
    async def _process_search_results(
        self,
        raw_results: List[Any],
        query: str,
        similarity_threshold: float
    ) -> List[Dict[str, Any]]:
        """Process and normalize search results"""
        processed_results = []
        
        for result in raw_results:
            try:
                # Normalize result format
                if hasattr(result, 'content'):
                    # ChromaDB result object
                    processed_result = {
                        'content': result.content,
                        'metadata': getattr(result, 'metadata', {}),
                        'similarity_score': getattr(result, 'score', 0.0),
                        'source': 'vector_search'
                    }
                elif isinstance(result, dict):
                    # Dictionary result
                    processed_result = {
                        'content': result.get('content', ''),
                        'metadata': result.get('metadata', {}),
                        'similarity_score': result.get('score', result.get('similarity_score', 0.0)),
                        'source': 'vector_search'
                    }
                else:
                    logger.warning(f"Unexpected result format: {type(result)}")
                    continue
                
                # Apply similarity threshold
                if processed_result['similarity_score'] >= similarity_threshold:
                    # Add retrieval metadata
                    processed_result.update({
                        'retrieved_at': datetime.now().isoformat(),
                        'query': query,
                        'retrieval_method': 'vector_similarity'
                    })
                    
                    processed_results.append(processed_result)
                
            except Exception as e:
                logger.warning(f"Failed to process search result: {e}")
                continue
        
        return processed_results
    
    async def _rerank_results(
        self,
        results: List[Dict[str, Any]],
        query: str
    ) -> List[Dict[str, Any]]:
        """Apply re-ranking to improve result quality"""
        try:
            # Simple re-ranking based on content length and similarity
            # In a full implementation, this could use a dedicated re-ranking model
            
            for result in results:
                content = result.get('content', '')
                original_score = result.get('similarity_score', 0.0)
                
                # Penalize very short or very long content
                length_penalty = 1.0
                if len(content) < 50:
                    length_penalty = 0.8
                elif len(content) > 2000:
                    length_penalty = 0.9
                
                # Boost if content contains query terms
                query_terms = set(query.lower().split())
                content_terms = set(content.lower().split())
                term_overlap = len(query_terms.intersection(content_terms)) / len(query_terms) if query_terms else 0
                term_boost = 1.0 + (term_overlap * 0.2)
                
                # Calculate final score
                reranked_score = original_score * length_penalty * term_boost
                result['similarity_score'] = reranked_score
                result['reranking_applied'] = True
            
            # Sort by reranked scores
            results.sort(key=lambda x: x.get('similarity_score', 0.0), reverse=True)
            return results
            
        except Exception as e:
            logger.error(f"Re-ranking failed: {e}")
            return results
    
    def _apply_diversity_filtering(
        self,
        results: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """Apply diversity filtering to reduce redundant results"""
        if not results or len(results) <= 1:
            return results
        
        try:
            filtered_results = [results[0]]  # Always include top result
            
            for result in results[1:]:
                # Check similarity to already selected results
                should_include = True
                result_content = result.get('content', '').lower()
                
                for selected in filtered_results:
                    selected_content = selected.get('content', '').lower()
                    
                    # Simple content similarity check
                    similarity = self._calculate_content_similarity(result_content, selected_content)
                    
                    if similarity > self.config['diversity_threshold']:
                        should_include = False
                        break
                
                if should_include:
                    filtered_results.append(result)
            
            return filtered_results
            
        except Exception as e:
            logger.error(f"Diversity filtering failed: {e}")
            return results
    
    def _calculate_content_similarity(self, content1: str, content2: str) -> float:
        """Calculate simple content similarity between two texts"""
        if not content1 or not content2:
            return 0.0
        
        # Simple Jaccard similarity
        words1 = set(content1.split())
        words2 = set(content2.split())
        
        if not words1 or not words2:
            return 0.0
        
        intersection = len(words1.intersection(words2))
        union = len(words1.union(words2))
        
        return intersection / union if union > 0 else 0.0
    
    def _extract_code_concepts(self, code: str) -> str:
        """Extract meaningful concepts from code for similarity search"""
        # Simple extraction - in practice, this could use AST parsing
        import re
        
        concepts = []
        
        # Extract function/class names
        function_matches = re.findall(r'def\s+(\w+)', code)
        class_matches = re.findall(r'class\s+(\w+)', code)
        
        concepts.extend(function_matches)
        concepts.extend(class_matches)
        
        # Extract imports
        import_matches = re.findall(r'import\s+([\w.]+)', code)
        from_matches = re.findall(r'from\s+([\w.]+)', code)
        
        concepts.extend(import_matches)
        concepts.extend(from_matches)
        
        # Extract string literals (might contain documentation)
        string_matches = re.findall(r'["\']([^"\']+)["\']', code)
        concepts.extend([s for s in string_matches if len(s) > 10])
        
        return ' '.join(concepts)
    
    def _fuse_weighted_average(
        self,
        type_results: Dict[str, List[Dict[str, Any]]],
        weights: Dict[str, float]
    ) -> List[Dict[str, Any]]:
        """Fuse results using weighted average of scores"""
        document_scores = {}
        
        for query_type, results in type_results.items():
            weight = weights.get(query_type, 1.0)
            
            for result in results:
                doc_id = self._get_document_id(result)
                score = result.get('similarity_score', 0.0) * weight
                
                if doc_id in document_scores:
                    document_scores[doc_id]['score'] += score
                    document_scores[doc_id]['count'] += 1
                else:
                    document_scores[doc_id] = {
                        'result': result,
                        'score': score,
                        'count': 1
                    }
        
        # Calculate final scores and sort
        fused_results = []
        for doc_data in document_scores.values():
            final_score = doc_data['score'] / doc_data['count']
            result = doc_data['result'].copy()
            result['similarity_score'] = final_score
            result['fusion_method'] = 'weighted_average'
            fused_results.append(result)
        
        fused_results.sort(key=lambda x: x['similarity_score'], reverse=True)
        return fused_results
    
    def _fuse_reciprocal_rank_fusion(
        self,
        type_results: Dict[str, List[Dict[str, Any]]],
        weights: Dict[str, float]
    ) -> List[Dict[str, Any]]:
        """Fuse results using Reciprocal Rank Fusion"""
        document_scores = {}
        
        for query_type, results in type_results.items():
            weight = weights.get(query_type, 1.0)
            
            for rank, result in enumerate(results):
                doc_id = self._get_document_id(result)
                rrf_score = weight / (60 + rank)  # RRF with k=60
                
                if doc_id in document_scores:
                    document_scores[doc_id]['score'] += rrf_score
                else:
                    document_scores[doc_id] = {
                        'result': result,
                        'score': rrf_score
                    }
        
        # Sort by RRF scores
        fused_results = []
        for doc_data in document_scores.values():
            result = doc_data['result'].copy()
            result['similarity_score'] = doc_data['score']
            result['fusion_method'] = 'rrf'
            fused_results.append(result)
        
        fused_results.sort(key=lambda x: x['similarity_score'], reverse=True)
        return fused_results
    
    def _fuse_max_score(
        self,
        type_results: Dict[str, List[Dict[str, Any]]],
        weights: Dict[str, float]
    ) -> List[Dict[str, Any]]:
        """Fuse results using maximum score across query types"""
        document_scores = {}
        
        for query_type, results in type_results.items():
            weight = weights.get(query_type, 1.0)
            
            for result in results:
                doc_id = self._get_document_id(result)
                score = result.get('similarity_score', 0.0) * weight
                
                if doc_id not in document_scores or score > document_scores[doc_id]['score']:
                    document_scores[doc_id] = {
                        'result': result,
                        'score': score
                    }
        
        # Sort by max scores
        fused_results = []
        for doc_data in document_scores.values():
            result = doc_data['result'].copy()
            result['similarity_score'] = doc_data['score']
            result['fusion_method'] = 'max_score'
            fused_results.append(result)
        
        fused_results.sort(key=lambda x: x['similarity_score'], reverse=True)
        return fused_results
    
    def _get_document_id(self, result: Dict[str, Any]) -> str:
        """Generate a unique ID for a document"""
        content = result.get('content', '')
        metadata = result.get('metadata', {})
        
        # Try to use an existing ID if available
        if 'id' in metadata:
            return str(metadata['id'])
        
        # Otherwise generate hash of content
        return hashlib.md5(content.encode()).hexdigest()
    
    def _generate_cache_key(self, *args) -> str:
        """Generate cache key from arguments"""
        key_data = json.dumps(args, sort_keys=True, default=str)
        return hashlib.md5(key_data.encode()).hexdigest()
    
    def _update_cache(self, key: str, results: List[Dict[str, Any]]):
        """Update query cache"""
        if len(self._query_cache) >= self._cache_max_size:
            # Remove oldest entry
            oldest_key = next(iter(self._query_cache))
            del self._query_cache[oldest_key]
        
        self._query_cache[key] = results
    
    def _update_metrics(
        self,
        execution_time: float,
        num_results: int,
        results: List[Dict[str, Any]],
        success: bool = True
    ):
        """Update performance metrics"""
        self.metrics['total_searches'] += 1
        
        if success:
            self.metrics['successful_searches'] += 1
            self.metrics['total_results_returned'] += num_results
            
            # Update average search time
            total_time = (
                self.metrics['avg_search_time'] * (self.metrics['total_searches'] - 1) +
                execution_time
            )
            self.metrics['avg_search_time'] = total_time / self.metrics['total_searches']
            
            # Update average similarity score
            if results:
                avg_score = sum(r.get('similarity_score', 0.0) for r in results) / len(results)
                total_score = (
                    self.metrics['avg_similarity_score'] * (self.metrics['successful_searches'] - 1) +
                    avg_score
                )
                self.metrics['avg_similarity_score'] = total_score / self.metrics['successful_searches']
    
    def get_metrics(self) -> Dict[str, Any]:
        """Get current performance metrics"""
        success_rate = (
            self.metrics['successful_searches'] / self.metrics['total_searches']
            if self.metrics['total_searches'] > 0 else 0.0
        )
        
        cache_hit_rate = (
            self.metrics['cache_hits'] / self.metrics['total_searches']
            if self.metrics['total_searches'] > 0 else 0.0
        )
        
        avg_results_per_search = (
            self.metrics['total_results_returned'] / self.metrics['successful_searches']
            if self.metrics['successful_searches'] > 0 else 0.0
        )
        
        return {
            **self.metrics,
            'success_rate': success_rate,
            'cache_hit_rate': cache_hit_rate,
            'avg_results_per_search': avg_results_per_search
        }
    
    def clear_cache(self):
        """Clear the query cache"""
        self._query_cache.clear()
        self.metrics['cache_hits'] = 0