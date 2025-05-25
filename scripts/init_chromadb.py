#!/usr/bin/env python3
"""
ChromaDB Initialization Script for RooPort CONVEX v2.0

Sets up ChromaDB collections and prepares the vector database for semantic search.
"""

import os
import sys
import asyncio
import logging
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from rooport.core.semantic_engine import SemanticContextEngine
from config.chromadb_config import get_chromadb_config, COLLECTION_CONFIGS

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def initialize_chromadb():
    """Initialize ChromaDB with collections and configuration"""
    
    logger.info("🚀 Initializing ChromaDB for RooPort CONVEX v2.0")
    
    try:
        # Get configuration
        config = get_chromadb_config()
        persist_dir = config['persist_directory']
        
        # Create data directory if it doesn't exist
        os.makedirs(persist_dir, exist_ok=True)
        logger.info(f"📁 Data directory: {persist_dir}")
        
        # Initialize semantic engine
        semantic_engine = SemanticContextEngine(persist_directory=persist_dir)
        logger.info("✅ Semantic engine initialized")
        
        # Verify collections
        stats = semantic_engine.get_collection_stats()
        logger.info("📊 Collection statistics:")
        for collection_name, count in stats.items():
            config_info = COLLECTION_CONFIGS.get(collection_name, {})
            description = config_info.get('description', 'No description')
            logger.info(f"  - {collection_name}: {count} documents ({description})")
        
        logger.info("🎯 ChromaDB initialization completed successfully!")
        
        return semantic_engine
        
    except Exception as e:
        logger.error(f"❌ ChromaDB initialization failed: {e}")
        raise


async def test_semantic_search(semantic_engine):
    """Test semantic search functionality"""
    
    logger.info("🧪 Testing semantic search functionality")
    
    try:
        # Test queries
        test_queries = [
            "project architecture decisions",
            "error handling patterns",
            "database integration",
            "user authentication"
        ]
        
        for query in test_queries:
            logger.info(f"🔍 Testing query: '{query}'")
            
            # Test multi-collection search
            results = await semantic_engine.multi_collection_search(
                query=query,
                limit_per_collection=2
            )
            
            total_results = sum(len(results_list) for results_list in results.values())
            logger.info(f"  Found {total_results} results across {len(results)} collections")
            
            # Show sample results
            for collection_type, search_results in results.items():
                if search_results:
                    best_result = search_results[0]
                    logger.info(f"  Best match in {collection_type}: "
                              f"similarity={best_result.similarity_score:.3f}")
        
        logger.info("✅ Semantic search tests completed")
        
    except Exception as e:
        logger.error(f"❌ Semantic search test failed: {e}")


async def add_sample_data(semantic_engine):
    """Add sample data for testing"""
    
    logger.info("📝 Adding sample data for testing")
    
    try:
        # Sample decisions
        sample_decisions = [
            {
                'id': 'sample_decision_1',
                'content': 'We decided to use React for the frontend framework due to its component-based architecture and large ecosystem.',
                'metadata': {
                    'workspace_id': 'sample_workspace',
                    'item_type': 'decision',
                    'tags': 'frontend,react,architecture'
                }
            },
            {
                'id': 'sample_decision_2', 
                'content': 'PostgreSQL was chosen as the primary database for its ACID compliance and JSON support.',
                'metadata': {
                    'workspace_id': 'sample_workspace',
                    'item_type': 'decision',
                    'tags': 'database,postgresql,backend'
                }
            }
        ]
        
        # Sample patterns
        sample_patterns = [
            {
                'id': 'sample_pattern_1',
                'content': 'Repository pattern implementation for data access layer abstraction and testability.',
                'metadata': {
                    'workspace_id': 'sample_workspace',
                    'item_type': 'pattern',
                    'tags': 'design-pattern,repository,data-access'
                }
            }
        ]
        
        # Add sample data
        for decision in sample_decisions:
            await semantic_engine.add_document(
                collection_type='decisions',
                document_id=decision['id'],
                content=decision['content'],
                metadata=decision['metadata']
            )
        
        for pattern in sample_patterns:
            await semantic_engine.add_document(
                collection_type='patterns',
                document_id=pattern['id'],
                content=pattern['content'],
                metadata=pattern['metadata']
            )
        
        logger.info("✅ Sample data added successfully")
        
    except Exception as e:
        logger.error(f"❌ Failed to add sample data: {e}")


async def main():
    """Main initialization function"""
    
    print("=" * 60)
    print("🚀 RooPort CONVEX v2.0 - ChromaDB Initialization")
    print("=" * 60)
    
    try:
        # Initialize ChromaDB
        semantic_engine = await initialize_chromadb()
        
        # Add sample data
        await add_sample_data(semantic_engine)
        
        # Test functionality
        await test_semantic_search(semantic_engine)
        
        print("\n" + "=" * 60)
        print("✅ ChromaDB initialization completed successfully!")
        print("🎯 Ready for RooPort CONVEX v2.0 development")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ Initialization failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())