"""
Semantic Context Engine for RooPort CONVEX v2.0

ChromaDB integration for semantic search and vector embeddings.
Provides semantic similarity search capabilities for enhanced context retrieval.
"""

import asyncio
import logging
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
import json
from datetime import datetime

import chromadb
from chromadb.config import Settings
import numpy as np

logger = logging.getLogger(__name__)


@dataclass
class SemanticSearchResult:
    """Result from semantic search with metadata"""
    content: str
    similarity_score: float
    metadata: Dict[str, Any]
    document_id: str
    collection_name: str


class SemanticContextEngine:
    """ChromaDB integration for semantic search and context management"""
    
    def __init__(self, persist_directory: str = "./data/chromadb"):
        """
        Initialize ChromaDB client and collections
        
        Args:
            persist_directory: Directory to persist ChromaDB data
        """
        self.persist_directory = persist_directory
        
        # Initialize ChromaDB client
        self.client = chromadb.PersistentClient(
            path=persist_directory,
            settings=Settings(
                anonymized_telemetry=False,
                allow_reset=True
            )
        )
        
        # Collection configurations
        self.collection_configs = {
            'decisions': {
                'name': 'project_decisions',
                'metadata': {'description': 'Project decisions and rationale'}
            },
            'patterns': {
                'name': 'system_patterns', 
                'metadata': {'description': 'Architectural and design patterns'}
            },
            'progress': {
                'name': 'project_progress',
                'metadata': {'description': 'Project progress and task tracking'}
            },
            'custom_data': {
                'name': 'custom_project_data',
                'metadata': {'description': 'Custom project data and documentation'}
            },
            'code_snippets': {
                'name': 'code_patterns',
                'metadata': {'description': 'Code snippets and patterns'}
            },
            'error_solutions': {
                'name': 'error_solutions',
                'metadata': {'description': 'Error patterns and solutions'}
            }
        }
        
        # Initialize collections
        self.collections = {}
        self._initialize_collections()
    
    def _initialize_collections(self):
        """Initialize or get existing ChromaDB collections"""
        try:
            for key, config in self.collection_configs.items():
                try:
                    # Try to get existing collection
                    collection = self.client.get_collection(
                        name=config['name']
                    )
                    logger.info(f"Retrieved existing collection: {config['name']}")
                except Exception:
                    # Create new collection if it doesn't exist
                    collection = self.client.create_collection(
                        name=config['name'],
                        metadata=config['metadata']
                    )
                    logger.info(f"Created new collection: {config['name']}")
                
                self.collections[key] = collection
                
        except Exception as e:
            logger.error(f"Failed to initialize ChromaDB collections: {e}")
            raise
    
    async def embed_conport_data(self, workspace_id: str, conport_client) -> Dict[str, int]:
        """
        Embed ConPort data into ChromaDB collections
        
        Args:
            workspace_id: Workspace identifier
            conport_client: ConPort client instance
            
        Returns:
            Dictionary with collection names and count of embedded items
        """
        embed_counts = {}
        
        try:
            # Embed decisions
            decisions = await conport_client.get_decisions(workspace_id, limit=1000)
            if decisions:
                count = await self._embed_decisions(decisions, workspace_id)
                embed_counts['decisions'] = count
            
            # Embed system patterns
            patterns = await conport_client.get_system_patterns(workspace_id, limit=1000)
            if patterns:
                count = await self._embed_patterns(patterns, workspace_id)
                embed_counts['patterns'] = count
            
            # Embed progress items
            progress = await conport_client.get_progress(workspace_id, limit=1000)
            if progress:
                count = await self._embed_progress(progress, workspace_id)
                embed_counts['progress'] = count
            
            # Embed custom data
            # Note: This would need to iterate through categories
            # For now, we'll embed a sample of custom data
            custom_data = await self._get_sample_custom_data(conport_client, workspace_id)
            if custom_data:
                count = await self._embed_custom_data(custom_data, workspace_id)
                embed_counts['custom_data'] = count
            
            logger.info(f"Embedded ConPort data: {embed_counts}")
            return embed_counts
            
        except Exception as e:
            logger.error(f"Failed to embed ConPort data: {e}")
            return embed_counts
    
    async def semantic_search(
        self, 
        query: str, 
        collection_type: str = 'decisions',
        limit: int = 5,
        workspace_filter: Optional[str] = None
    ) -> List[SemanticSearchResult]:
        """
        Perform semantic search across specified collection
        
        Args:
            query: Search query
            collection_type: Type of collection to search
            limit: Maximum number of results
            workspace_filter: Filter by workspace ID
            
        Returns:
            List of semantic search results
        """
        try:
            if collection_type not in self.collections:
                logger.warning(f"Collection type '{collection_type}' not found")
                return []
            
            collection = self.collections[collection_type]
            
            # Prepare where clause for workspace filtering
            where_clause = None
            if workspace_filter:
                where_clause = {"workspace_id": workspace_filter}
            
            # Perform semantic search
            results = collection.query(
                query_texts=[query],
                n_results=limit,
                where=where_clause,
                include=['documents', 'metadatas', 'distances']
            )
            
            # Format results
            search_results = []
            if results['documents'] and results['documents'][0]:
                for i, doc in enumerate(results['documents'][0]):
                    similarity_score = 1.0 - results['distances'][0][i]  # Convert distance to similarity
                    metadata = results['metadatas'][0][i] if results['metadatas'][0] else {}
                    
                    search_results.append(SemanticSearchResult(
                        content=doc,
                        similarity_score=similarity_score,
                        metadata=metadata,
                        document_id=results['ids'][0][i] if results['ids'] else f"doc_{i}",
                        collection_name=collection_type
                    ))
            
            logger.info(f"Semantic search returned {len(search_results)} results for query: {query[:50]}...")
            return search_results
            
        except Exception as e:
            logger.error(f"Semantic search failed: {e}")
            return []
    
    async def multi_collection_search(
        self,
        query: str,
        collection_types: List[str] = None,
        limit_per_collection: int = 3,
        workspace_filter: Optional[str] = None
    ) -> Dict[str, List[SemanticSearchResult]]:
        """
        Search across multiple collections simultaneously
        
        Args:
            query: Search query
            collection_types: List of collection types to search
            limit_per_collection: Max results per collection
            workspace_filter: Filter by workspace ID
            
        Returns:
            Dictionary mapping collection types to search results
        """
        if collection_types is None:
            collection_types = ['decisions', 'patterns', 'progress', 'custom_data']
        
        # Create search tasks for each collection
        search_tasks = []
        for collection_type in collection_types:
            if collection_type in self.collections:
                task = self.semantic_search(
                    query, collection_type, limit_per_collection, workspace_filter
                )
                search_tasks.append((collection_type, task))
        
        # Execute searches in parallel
        results = {}
        if search_tasks:
            task_results = await asyncio.gather(
                *[task for _, task in search_tasks],
                return_exceptions=True
            )
            
            for i, (collection_type, _) in enumerate(search_tasks):
                result = task_results[i]
                if isinstance(result, Exception):
                    logger.warning(f"Search failed for {collection_type}: {result}")
                    results[collection_type] = []
                else:
                    results[collection_type] = result
        
        return results
    
    async def add_document(
        self,
        collection_type: str,
        document_id: str,
        content: str,
        metadata: Dict[str, Any]
    ) -> bool:
        """
        Add a document to a specific collection
        
        Args:
            collection_type: Type of collection
            document_id: Unique document identifier
            content: Document content
            metadata: Document metadata
            
        Returns:
            Success status
        """
        try:
            if collection_type not in self.collections:
                logger.error(f"Collection type '{collection_type}' not found")
                return False
            
            collection = self.collections[collection_type]
            
            # Add timestamp if not present
            if 'timestamp' not in metadata:
                metadata['timestamp'] = datetime.now().isoformat()
            
            collection.add(
                documents=[content],
                ids=[document_id],
                metadatas=[metadata]
            )
            
            logger.info(f"Added document {document_id} to {collection_type}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to add document: {e}")
            return False
    
    # Helper methods for embedding ConPort data
    
    async def _embed_decisions(self, decisions: List[Dict], workspace_id: str) -> int:
        """Embed ConPort decisions into ChromaDB"""
        collection = self.collections['decisions']
        count = 0
        
        for decision in decisions:
            try:
                doc_id = f"decision_{decision.get('id', count)}"
                content = f"{decision.get('summary', '')} {decision.get('rationale', '')}"
                
                metadata = {
                    'workspace_id': workspace_id,
                    'item_type': 'decision',
                    'decision_id': decision.get('id'),
                    'tags': json.dumps(decision.get('tags', [])),
                    'timestamp': decision.get('timestamp', datetime.now().isoformat())
                }
                
                collection.add(
                    documents=[content],
                    ids=[doc_id],
                    metadatas=[metadata]
                )
                count += 1
                
            except Exception as e:
                logger.warning(f"Failed to embed decision {decision.get('id')}: {e}")
        
        return count
    
    async def _embed_patterns(self, patterns: List[Dict], workspace_id: str) -> int:
        """Embed ConPort system patterns into ChromaDB"""
        collection = self.collections['patterns']
        count = 0
        
        for pattern in patterns:
            try:
                doc_id = f"pattern_{pattern.get('id', count)}"
                content = f"{pattern.get('name', '')} {pattern.get('description', '')}"
                
                metadata = {
                    'workspace_id': workspace_id,
                    'item_type': 'pattern',
                    'pattern_id': pattern.get('id'),
                    'tags': json.dumps(pattern.get('tags', [])),
                    'timestamp': pattern.get('timestamp', datetime.now().isoformat())
                }
                
                collection.add(
                    documents=[content],
                    ids=[doc_id],
                    metadatas=[metadata]
                )
                count += 1
                
            except Exception as e:
                logger.warning(f"Failed to embed pattern {pattern.get('id')}: {e}")
        
        return count
    
    async def _embed_progress(self, progress_items: List[Dict], workspace_id: str) -> int:
        """Embed ConPort progress items into ChromaDB"""
        collection = self.collections['progress']
        count = 0
        
        for item in progress_items:
            try:
                doc_id = f"progress_{item.get('id', count)}"
                content = f"{item.get('description', '')} {item.get('status', '')}"
                
                metadata = {
                    'workspace_id': workspace_id,
                    'item_type': 'progress',
                    'progress_id': item.get('id'),
                    'status': item.get('status'),
                    'timestamp': item.get('timestamp', datetime.now().isoformat())
                }
                
                collection.add(
                    documents=[content],
                    ids=[doc_id],
                    metadatas=[metadata]
                )
                count += 1
                
            except Exception as e:
                logger.warning(f"Failed to embed progress {item.get('id')}: {e}")
        
        return count
    
    async def _embed_custom_data(self, custom_data: List[Dict], workspace_id: str) -> int:
        """Embed ConPort custom data into ChromaDB"""
        collection = self.collections['custom_data']
        count = 0
        
        for item in custom_data:
            try:
                doc_id = f"custom_{item.get('category', 'unknown')}_{count}"
                content = str(item.get('value', ''))
                
                metadata = {
                    'workspace_id': workspace_id,
                    'item_type': 'custom_data',
                    'category': item.get('category'),
                    'key': item.get('key'),
                    'timestamp': item.get('timestamp', datetime.now().isoformat())
                }
                
                collection.add(
                    documents=[content],
                    ids=[doc_id],
                    metadatas=[metadata]
                )
                count += 1
                
            except Exception as e:
                logger.warning(f"Failed to embed custom data {item.get('key')}: {e}")
        
        return count
    
    async def _get_sample_custom_data(self, conport_client, workspace_id: str) -> List[Dict]:
        """Get sample custom data from ConPort (placeholder implementation)"""
        # In a real implementation, this would iterate through categories
        # and retrieve custom data items
        return []
    
    def get_collection_stats(self) -> Dict[str, int]:
        """Get statistics for all collections"""
        stats = {}
        for name, collection in self.collections.items():
            try:
                count = collection.count()
                stats[name] = count
            except Exception as e:
                logger.warning(f"Failed to get stats for {name}: {e}")
                stats[name] = 0
        
        return stats
    
    def reset_collections(self):
        """Reset all collections (for development/testing)"""
        try:
            for config in self.collection_configs.values():
                try:
                    self.client.delete_collection(name=config['name'])
                except Exception:
                    pass  # Collection might not exist
            
            self._initialize_collections()
            logger.info("All collections reset successfully")
            
        except Exception as e:
            logger.error(f"Failed to reset collections: {e}")