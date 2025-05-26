"""
ConPort Retriever - Specialized retrieval from ConPort memory system
Elite Field Service SaaS Platform

Provides structured access to project context, decisions, patterns, and custom data
stored in the ConPort knowledge management system.
"""

import asyncio
from typing import Dict, List, Any, Optional, Union
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class ConPortRetriever:
    """
    Specialized retriever for ConPort memory system
    
    Provides structured access to:
    - Project decisions and rationale
    - System patterns and architecture
    - Custom data and glossary terms
    - Progress tracking and task history
    - Linked relationships between items
    """
    
    def __init__(self, conport_client, config: Optional[Dict[str, Any]] = None):
        """
        Initialize ConPort retriever
        
        Args:
            conport_client: ConPort MCP client instance
            config: Configuration options for retrieval behavior
        """
        self.conport_client = conport_client
        self.config = {
            'max_items_per_type': 10,
            'include_metadata': True,
            'follow_relationships': True,
            'max_relationship_depth': 2,
            'timeout_seconds': 15.0,
            'relevance_threshold': 0.1,
            **(config or {})
        }
        
        # Performance tracking
        self.metrics = {
            'total_retrievals': 0,
            'successful_retrievals': 0,
            'avg_retrieval_time': 0.0,
            'cache_hits': 0,
            'relationship_expansions': 0
        }
        
        # Simple LRU cache for recent queries
        self._cache = {}
        self._cache_max_size = 50
    
    async def retrieve_by_query(
        self, 
        query: str, 
        workspace_id: str,
        retrieval_types: Optional[List[str]] = None,
        max_items: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """
        Retrieve ConPort items based on a natural language query
        
        Args:
            query: Natural language query
            workspace_id: ConPort workspace identifier
            retrieval_types: Types to search ('decisions', 'patterns', 'custom_data', 'progress')
            max_items: Maximum items to return per type
            
        Returns:
            List of retrieved items with metadata
        """
        start_time = datetime.now()
        cache_key = f"{query}:{workspace_id}:{':'.join(retrieval_types or [])}"
        
        try:
            # Check cache first
            if cache_key in self._cache:
                self.metrics['cache_hits'] += 1
                return self._cache[cache_key]
            
            # Default retrieval types if not specified
            if not retrieval_types:
                retrieval_types = self._determine_retrieval_types(query)
            
            max_items = max_items or self.config['max_items_per_type']
            
            # Execute parallel retrievals for different types
            retrieval_tasks = []
            
            if 'decisions' in retrieval_types:
                retrieval_tasks.append(
                    self._retrieve_decisions(query, workspace_id, max_items)
                )
            
            if 'patterns' in retrieval_types:
                retrieval_tasks.append(
                    self._retrieve_system_patterns(query, workspace_id, max_items)
                )
            
            if 'custom_data' in retrieval_types:
                retrieval_tasks.append(
                    self._retrieve_custom_data(query, workspace_id, max_items)
                )
            
            if 'progress' in retrieval_types:
                retrieval_tasks.append(
                    self._retrieve_progress(query, workspace_id, max_items)
                )
            
            # Execute all retrievals concurrently
            results = await asyncio.gather(*retrieval_tasks, return_exceptions=True)
            
            # Combine and process results
            combined_items = []
            for result in results:
                if isinstance(result, Exception):
                    logger.warning(f"ConPort retrieval error: {result}")
                    continue
                
                if isinstance(result, list):
                    combined_items.extend(result)
            
            # Expand with relationships if enabled
            if self.config['follow_relationships'] and combined_items:
                expanded_items = await self._expand_with_relationships(
                    combined_items, workspace_id
                )
                combined_items.extend(expanded_items)
            
            # Sort by relevance and limit total results
            sorted_items = self._sort_by_relevance(combined_items, query)
            final_items = sorted_items[:max_items * len(retrieval_types)]
            
            # Cache the results
            self._update_cache(cache_key, final_items)
            
            # Update metrics
            execution_time = (datetime.now() - start_time).total_seconds()
            self._update_metrics(execution_time, success=True)
            
            return final_items
            
        except Exception as e:
            logger.error(f"ConPort retrieval failed: {e}")
            execution_time = (datetime.now() - start_time).total_seconds()
            self._update_metrics(execution_time, success=False)
            raise
    
    async def retrieve_by_id(
        self, 
        item_type: str, 
        item_id: Union[str, int], 
        workspace_id: str,
        include_relationships: bool = True
    ) -> Optional[Dict[str, Any]]:
        """
        Retrieve specific ConPort item by ID
        
        Args:
            item_type: Type of item ('decision', 'pattern', 'custom_data', 'progress')
            item_id: Unique identifier for the item
            workspace_id: ConPort workspace identifier
            include_relationships: Whether to include related items
            
        Returns:
            Retrieved item with metadata, or None if not found
        """
        try:
            # Route to appropriate retrieval method
            if item_type == 'decision':
                items = await self.conport_client.get_decisions(
                    workspace_id=workspace_id,
                    limit=1
                )
                decisions = items.get('decisions', [])
                item = next((d for d in decisions if d.get('id') == item_id), None)
                
            elif item_type == 'pattern':
                patterns = await self.conport_client.get_system_patterns(
                    workspace_id=workspace_id
                )
                item = next((p for p in patterns if p.get('id') == item_id), None)
                
            elif item_type == 'custom_data':
                # For custom data, we need category and key
                if isinstance(item_id, dict) and 'category' in item_id and 'key' in item_id:
                    result = await self.conport_client.get_custom_data(
                        workspace_id=workspace_id,
                        category=item_id['category'],
                        key=item_id['key']
                    )
                    item = result if result else None
                else:
                    return None
                    
            elif item_type == 'progress':
                progress_items = await self.conport_client.get_progress(
                    workspace_id=workspace_id,
                    limit=100  # Need to search through items
                )
                item = next((p for p in progress_items if p.get('id') == item_id), None)
                
            else:
                logger.warning(f"Unknown item type: {item_type}")
                return None
            
            if not item:
                return None
            
            # Add metadata
            enriched_item = {
                **item,
                'conport_type': item_type,
                'retrieved_at': datetime.now().isoformat(),
                'retrieval_method': 'by_id'
            }
            
            # Include relationships if requested
            if include_relationships:
                relationships = await self._get_item_relationships(
                    item_type, str(item_id), workspace_id
                )
                enriched_item['relationships'] = relationships
            
            return enriched_item
            
        except Exception as e:
            logger.error(f"Failed to retrieve {item_type} {item_id}: {e}")
            return None
    
    async def _retrieve_decisions(
        self, 
        query: str, 
        workspace_id: str, 
        max_items: int
    ) -> List[Dict[str, Any]]:
        """Retrieve decisions using full-text search"""
        try:
            result = await self.conport_client.search_decisions_fts(
                workspace_id=workspace_id,
                query_term=query,
                limit=max_items
            )
            
            decisions = result.get('decisions', [])
            return [
                {
                    **decision,
                    'conport_type': 'decision',
                    'retrieved_at': datetime.now().isoformat(),
                    'relevance_score': self._calculate_text_relevance(query, decision)
                }
                for decision in decisions
            ]
            
        except Exception as e:
            logger.error(f"Decision retrieval failed: {e}")
            return []
    
    async def _retrieve_system_patterns(
        self, 
        query: str, 
        workspace_id: str, 
        max_items: int
    ) -> List[Dict[str, Any]]:
        """Retrieve system patterns with keyword matching"""
        try:
            patterns = await self.conport_client.get_system_patterns(
                workspace_id=workspace_id
            )
            
            # Filter patterns by relevance to query
            relevant_patterns = []
            for pattern in patterns:
                relevance = self._calculate_text_relevance(query, pattern)
                if relevance >= self.config['relevance_threshold']:
                    relevant_patterns.append({
                        **pattern,
                        'conport_type': 'pattern',
                        'retrieved_at': datetime.now().isoformat(),
                        'relevance_score': relevance
                    })
            
            # Sort by relevance and limit
            relevant_patterns.sort(key=lambda x: x['relevance_score'], reverse=True)
            return relevant_patterns[:max_items]
            
        except Exception as e:
            logger.error(f"Pattern retrieval failed: {e}")
            return []
    
    async def _retrieve_custom_data(
        self, 
        query: str, 
        workspace_id: str, 
        max_items: int
    ) -> List[Dict[str, Any]]:
        """Retrieve custom data using full-text search"""
        try:
            result = await self.conport_client.search_custom_data_value_fts(
                workspace_id=workspace_id,
                query_term=query,
                limit=max_items
            )
            
            custom_items = result.get('results', [])
            return [
                {
                    **item,
                    'conport_type': 'custom_data',
                    'retrieved_at': datetime.now().isoformat(),
                    'relevance_score': self._calculate_text_relevance(query, item)
                }
                for item in custom_items
            ]
            
        except Exception as e:
            logger.error(f"Custom data retrieval failed: {e}")
            return []
    
    async def _retrieve_progress(
        self, 
        query: str, 
        workspace_id: str, 
        max_items: int
    ) -> List[Dict[str, Any]]:
        """Retrieve progress items with keyword matching"""
        try:
            progress_items = await self.conport_client.get_progress(
                workspace_id=workspace_id,
                limit=max_items * 2  # Get more to filter
            )
            
            # Filter by relevance to query
            relevant_items = []
            for item in progress_items:
                relevance = self._calculate_text_relevance(query, item)
                if relevance >= self.config['relevance_threshold']:
                    relevant_items.append({
                        **item,
                        'conport_type': 'progress',
                        'retrieved_at': datetime.now().isoformat(),
                        'relevance_score': relevance
                    })
            
            # Sort by relevance and limit
            relevant_items.sort(key=lambda x: x['relevance_score'], reverse=True)
            return relevant_items[:max_items]
            
        except Exception as e:
            logger.error(f"Progress retrieval failed: {e}")
            return []
    
    async def _expand_with_relationships(
        self, 
        items: List[Dict[str, Any]], 
        workspace_id: str
    ) -> List[Dict[str, Any]]:
        """Expand items with their relationships"""
        expanded_items = []
        
        try:
            for item in items:
                item_type = item.get('conport_type')
                item_id = str(item.get('id', ''))
                
                if item_type and item_id:
                    relationships = await self._get_item_relationships(
                        item_type, item_id, workspace_id
                    )
                    
                    # Add related items to expansion set
                    for rel in relationships:
                        related_item = await self.retrieve_by_id(
                            rel.get('target_item_type'),
                            rel.get('target_item_id'),
                            workspace_id,
                            include_relationships=False  # Avoid infinite recursion
                        )
                        if related_item:
                            related_item['relationship_context'] = {
                                'type': rel.get('relationship_type'),
                                'description': rel.get('description'),
                                'source_item': f"{item_type}:{item_id}"
                            }
                            expanded_items.append(related_item)
            
            self.metrics['relationship_expansions'] += len(expanded_items)
            return expanded_items
            
        except Exception as e:
            logger.error(f"Relationship expansion failed: {e}")
            return []
    
    async def _get_item_relationships(
        self, 
        item_type: str, 
        item_id: str, 
        workspace_id: str
    ) -> List[Dict[str, Any]]:
        """Get relationships for a specific item"""
        try:
            result = await self.conport_client.get_linked_items(
                workspace_id=workspace_id,
                item_type=item_type,
                item_id=item_id,
                limit=self.config['max_items_per_type']
            )
            return result.get('links', [])
            
        except Exception as e:
            logger.error(f"Failed to get relationships for {item_type}:{item_id}: {e}")
            return []
    
    def _determine_retrieval_types(self, query: str) -> List[str]:
        """Determine which ConPort types to search based on query content"""
        query_lower = query.lower()
        types = []
        
        # Decision keywords
        if any(word in query_lower for word in [
            'decision', 'decide', 'choice', 'rationale', 'why', 'because'
        ]):
            types.append('decisions')
        
        # Pattern keywords  
        if any(word in query_lower for word in [
            'pattern', 'architecture', 'design', 'structure', 'system'
        ]):
            types.append('patterns')
        
        # Progress keywords
        if any(word in query_lower for word in [
            'progress', 'task', 'todo', 'status', 'completion', 'done'
        ]):
            types.append('progress')
        
        # Custom data is default if no specific types detected
        if not types or any(word in query_lower for word in [
            'data', 'information', 'glossary', 'term', 'definition'
        ]):
            types.append('custom_data')
        
        # If no specific indicators, search all types
        if not types:
            types = ['decisions', 'patterns', 'custom_data', 'progress']
        
        return types
    
    def _calculate_text_relevance(self, query: str, item: Dict[str, Any]) -> float:
        """Calculate text-based relevance score between query and item"""
        query_terms = set(query.lower().split())
        
        # Combine relevant text fields from the item
        text_fields = []
        for field in ['summary', 'description', 'rationale', 'name', 'key', 'value']:
            if field in item and item[field]:
                text_fields.append(str(item[field]).lower())
        
        combined_text = ' '.join(text_fields)
        item_terms = set(combined_text.split())
        
        if not query_terms or not item_terms:
            return 0.0
        
        # Calculate Jaccard similarity
        intersection = len(query_terms.intersection(item_terms))
        union = len(query_terms.union(item_terms))
        
        return intersection / union if union > 0 else 0.0
    
    def _sort_by_relevance(
        self, 
        items: List[Dict[str, Any]], 
        query: str
    ) -> List[Dict[str, Any]]:
        """Sort items by relevance to query"""
        return sorted(
            items, 
            key=lambda x: x.get('relevance_score', 0.0), 
            reverse=True
        )
    
    def _update_cache(self, key: str, items: List[Dict[str, Any]]):
        """Update LRU cache with new results"""
        if len(self._cache) >= self._cache_max_size:
            # Remove oldest item
            oldest_key = next(iter(self._cache))
            del self._cache[oldest_key]
        
        self._cache[key] = items
    
    def _update_metrics(self, execution_time: float, success: bool):
        """Update performance metrics"""
        self.metrics['total_retrievals'] += 1
        if success:
            self.metrics['successful_retrievals'] += 1
        
        # Update average execution time
        total_time = (
            self.metrics['avg_retrieval_time'] * (self.metrics['total_retrievals'] - 1) +
            execution_time
        )
        self.metrics['avg_retrieval_time'] = total_time / self.metrics['total_retrievals']
    
    def get_metrics(self) -> Dict[str, Any]:
        """Get current performance metrics"""
        success_rate = (
            self.metrics['successful_retrievals'] / self.metrics['total_retrievals']
            if self.metrics['total_retrievals'] > 0 else 0.0
        )
        
        return {
            **self.metrics,
            'success_rate': success_rate,
            'cache_hit_rate': (
                self.metrics['cache_hits'] / self.metrics['total_retrievals']
                if self.metrics['total_retrievals'] > 0 else 0.0
            )
        }
    
    def clear_cache(self):
        """Clear the retrieval cache"""
        self._cache.clear()
        self.metrics['cache_hits'] = 0