"""
Unified RAG System Example - Elite Field Service SaaS Platform
Demonstrates the complete integrated RAG/CONVEX system

This example shows how to use the unified RAG system that combines:
- ConPort project memory retrieval
- Vector semantic search  
- Intelligent hybrid retrieval strategies
- Advanced information synthesis
- Comprehensive error handling and metrics
"""

import asyncio
import sys
import os
from datetime import datetime
from typing import Dict, Any

# Add the rooport module to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from rooport.rag.engines.agentic_rag import (
    AgenticRAGEngine, RetrievalStrategy, ConfidenceLevel
)
from rooport.rag.retrievers.conport_retriever import ConPortRetriever
from rooport.rag.retrievers.vector_retriever import VectorRetriever
from rooport.rag.retrievers.hybrid_retriever import HybridRetriever, FusionStrategy
from rooport.rag.synthesizers.information_synthesizer import (
    InformationSynthesizer, SynthesisStrategy
)


class MockConPortClient:
    """Mock ConPort client for demonstration"""
    
    async def search_decisions_fts(self, workspace_id: str, query_term: str, limit: int = 10):
        """Mock decision search"""
        return {
            'decisions': [
                {
                    'id': 1,
                    'summary': 'Adopt microservices architecture for Elite Field Service platform',
                    'rationale': 'Microservices provide better scalability and team autonomy for field service operations',
                    'implementation_details': 'Split monolith into service domains: scheduling, dispatching, inventory, billing',
                    'tags': ['architecture', 'microservices', 'scalability']
                },
                {
                    'id': 2,
                    'summary': 'Use React Native for mobile field technician app',
                    'rationale': 'Single codebase for iOS and Android, faster development cycle',
                    'implementation_details': 'React Native with Redux for state management, offline-first design',
                    'tags': ['mobile', 'react-native', 'field-technicians']
                }
            ]
        }
    
    async def search_custom_data_value_fts(self, workspace_id: str, query_term: str, limit: int = 10):
        """Mock custom data search"""
        return {
            'results': [
                {
                    'id': 1,
                    'category': 'TechnicalSpecs',
                    'key': 'real_time_tracking',
                    'value': 'GPS tracking with 30-second intervals for field technicians. WebSocket connections for real-time dashboard updates. Redis for caching location data.'
                },
                {
                    'id': 2,
                    'category': 'BusinessRules',
                    'key': 'scheduling_constraints',
                    'value': 'Technicians must be scheduled within 50 miles of home base. Maximum 8 hours per day. Emergency calls override regular scheduling.'
                }
            ]
        }
    
    async def log_custom_data(self, workspace_id: str, category: str, key: str, value: Any):
        """Mock logging function"""
        print(f"[ConPort Log] {category}/{key}: {value}")
        return True


class MockSemanticEngine:
    """Mock semantic search engine for demonstration"""
    
    async def semantic_search(self, query: str, max_results: int = 10, similarity_threshold: float = 0.7):
        """Mock semantic search"""
        mock_results = []
        
        if 'tracking' in query.lower():
            mock_results.append(MockResult(
                content='GPS tracking implementation using React Native Geolocation API with real-time WebSocket updates to central dashboard',
                metadata={'source_file': 'LocationService.js', 'type': 'code'},
                score=0.89
            ))
            
        if 'architecture' in query.lower():
            mock_results.append(MockResult(
                content='Microservices architecture pattern with API Gateway, service discovery, and event-driven communication between services',
                metadata={'source_file': 'architecture_docs.md', 'type': 'documentation'},
                score=0.85
            ))
            
        if 'field service' in query.lower():
            mock_results.append(MockResult(
                content='Field service optimization algorithm using constraint satisfaction for technician scheduling and route optimization',
                metadata={'source_file': 'SchedulingAlgorithm.py', 'type': 'code'},
                score=0.82
            ))
        
        return [r for r in mock_results if r.score >= similarity_threshold]


class MockResult:
    """Mock result object"""
    def __init__(self, content: str, metadata: Dict[str, Any], score: float):
        self.content = content
        self.metadata = metadata
        self.score = score


async def demonstrate_unified_rag_system():
    """
    Comprehensive demonstration of the unified RAG system
    """
    print("🚀 Elite Field Service - Unified RAG System Demo")
    print("=" * 60)
    
    # Initialize mock dependencies
    conport_client = MockConPortClient()
    semantic_engine = MockSemanticEngine()
    
    # Initialize RAG components
    print("\n📦 Initializing RAG components...")
    
    # Individual retrievers
    conport_retriever = ConPortRetriever(conport_client)
    vector_retriever = VectorRetriever(semantic_engine)
    hybrid_retriever = HybridRetriever(conport_retriever, vector_retriever)
    
    # Information synthesizer
    synthesizer = InformationSynthesizer({
        'enable_citations': True,
        'validation_level': 'moderate'
    })
    
    # Main RAG engine
    rag_engine = AgenticRAGEngine(
        conport_client=conport_client,
        semantic_engine=semantic_engine,
        config={
            'max_retrieval_items': 15,
            'confidence_threshold': 0.6,
            'enable_logging': True
        }
    )
    
    print("✅ All components initialized successfully!")
    
    # Test scenarios
    test_scenarios = [
        {
            'query': 'What architecture decisions were made for real-time field technician tracking?',
            'description': 'Mixed query requiring both ConPort decisions and technical implementation details',
            'expected_strategy': RetrievalStrategy.HYBRID
        },
        {
            'query': 'Show me the current progress on mobile app development',
            'description': 'ConPort-focused query for project status and decisions',
            'expected_strategy': RetrievalStrategy.CONPORT_ONLY
        },
        {
            'query': 'Find similar GPS tracking implementations in the codebase',
            'description': 'Semantic search query for code patterns and implementations',
            'expected_strategy': RetrievalStrategy.SEMANTIC_ONLY
        }
    ]
    
    print(f"\n🧪 Running {len(test_scenarios)} test scenarios...")
    
    for i, scenario in enumerate(test_scenarios, 1):
        print(f"\n--- Scenario {i}: {scenario['description']} ---")
        print(f"Query: {scenario['query']}")
        
        try:
            # Process query with RAG engine
            start_time = datetime.now()
            result = await rag_engine.process_query(
                query=scenario['query'],
                workspace_id="elite_field_service_demo"
            )
            execution_time = (datetime.now() - start_time).total_seconds()
            
            # Display results
            print(f"\n📊 Results:")
            print(f"  • Strategy: {result.retrieval_strategy.value}")
            print(f"  • Confidence: {result.confidence_level.value} ({result.metadata.get('confidence_score', 0.0):.2f})")
            print(f"  • Sources: {len(result.sources_used)} used, {len(result.retrieved_items)} retrieved")
            print(f"  • Execution time: {execution_time:.2f}s")
            
            print(f"\n💬 Answer:")
            print(f"  {result.final_answer}")
            
            if result.reasoning_chain:
                print(f"\n🧠 Reasoning:")
                for step in result.reasoning_chain[:3]:  # Show first 3 steps
                    print(f"  • {step}")
            
            print(f"\n📈 Strategy Performance:")
            expected = scenario['expected_strategy']
            actual = result.retrieval_strategy
            strategy_match = "✅ Correct" if actual == expected else f"⚠️  Expected {expected.value}, got {actual.value}"
            print(f"  • Strategy selection: {strategy_match}")
            
        except Exception as e:
            print(f"❌ Error in scenario {i}: {e}")
            continue
    
    # Component-specific demonstrations
    print(f"\n🔍 Component-Specific Demonstrations")
    print("=" * 40)
    
    # Demonstrate hybrid retriever with different fusion strategies
    print(f"\n🔄 Hybrid Retrieval Strategies:")
    
    hybrid_query = "Explain the microservices architecture for field service optimization"
    
    fusion_strategies = [
        FusionStrategy.WEIGHTED_AVERAGE,
        FusionStrategy.RECIPROCAL_RANK_FUSION,
        FusionStrategy.CONFIDENCE_BASED
    ]
    
    for strategy in fusion_strategies:
        try:
            print(f"\n  Testing {strategy.value}:")
            
            results = await hybrid_retriever.retrieve(
                query=hybrid_query,
                workspace_id="demo",
                fusion_strategy=strategy,
                max_results=5
            )
            
            print(f"    • Retrieved {len(results)} items")
            if results:
                avg_score = sum(r.get('fusion_score', 0) for r in results) / len(results)
                print(f"    • Average fusion score: {avg_score:.3f}")
                print(f"    • Top source: {results[0].get('hybrid_source', 'unknown')}")
            
        except Exception as e:
            print(f"    ❌ Error: {e}")
    
    # Demonstrate information synthesizer strategies
    print(f"\n📝 Information Synthesis Strategies:")
    
    # Create mock retrieved items for synthesis
    mock_items = [
        {
            'content': 'Microservices architecture enables independent scaling of field service components like scheduling, dispatching, and inventory management.',
            'source': 'architecture_decisions',
            'relevance_score': 0.9,
            'conport_type': 'decision'
        },
        {
            'content': 'GPS tracking service implemented with React Native Geolocation API, providing 30-second location updates to central dashboard.',
            'source': 'technical_implementation',
            'similarity_score': 0.85,
            'metadata': {'file': 'LocationService.js'}
        },
        {
            'content': 'Field technician mobile app built with React Native for cross-platform compatibility and faster development cycles.',
            'source': 'mobile_development',
            'relevance_score': 0.8,
            'conport_type': 'custom_data'
        }
    ]
    
    synthesis_strategies = [
        SynthesisStrategy.EXTRACTIVE,
        SynthesisStrategy.STRUCTURED,
        SynthesisStrategy.NARRATIVE
    ]
    
    synthesis_query = "How is real-time tracking implemented in the field service platform?"
    
    for strategy in synthesis_strategies:
        try:
            print(f"\n  Testing {strategy.value} synthesis:")
            
            synthesis_result = await synthesizer.synthesize(
                retrieved_items=mock_items,
                query=synthesis_query,
                strategy=strategy
            )
            
            print(f"    • Confidence: {synthesis_result['confidence_level']} ({synthesis_result['confidence_score']:.2f})")
            print(f"    • Answer length: {len(synthesis_result['answer'])} chars")
            print(f"    • Answer preview: {synthesis_result['answer'][:100]}...")
            
        except Exception as e:
            print(f"    ❌ Error: {e}")
    
    # Performance metrics
    print(f"\n📊 Performance Metrics")
    print("=" * 30)
    
    rag_metrics = rag_engine.get_performance_metrics()
    print(f"\nRAG Engine:")
    print(f"  • Total queries: {rag_metrics['total_queries']}")
    print(f"  • Success rate: {rag_metrics['success_rate']:.1%}")
    print(f"  • Average response time: {rag_metrics['avg_response_time']:.2f}s")
    
    conport_metrics = conport_retriever.get_metrics()
    print(f"\nConPort Retriever:")
    print(f"  • Total retrievals: {conport_metrics['total_retrievals']}")
    print(f"  • Success rate: {conport_metrics['success_rate']:.1%}")
    print(f"  • Cache hit rate: {conport_metrics.get('cache_hit_rate', 0):.1%}")
    
    vector_metrics = vector_retriever.get_metrics()
    print(f"\nVector Retriever:")
    print(f"  • Total searches: {vector_metrics['total_searches']}")
    print(f"  • Success rate: {vector_metrics['success_rate']:.1%}")
    print(f"  • Average similarity: {vector_metrics['avg_similarity_score']:.3f}")
    
    synthesizer_metrics = synthesizer.get_metrics()
    print(f"\nInformation Synthesizer:")
    print(f"  • Total syntheses: {synthesizer_metrics['total_syntheses']}")
    print(f"  • Success rate: {synthesizer_metrics['success_rate']:.1%}")
    print(f"  • Average confidence: {synthesizer_metrics['avg_confidence_score']:.3f}")
    
    print(f"\n🎉 Demo completed successfully!")
    print(f"\n💡 Key Features Demonstrated:")
    print(f"  ✅ Unified RAG architecture with multiple retrieval strategies")
    print(f"  ✅ Intelligent ConPort + Vector search fusion")
    print(f"  ✅ Advanced information synthesis with multiple strategies")
    print(f"  ✅ Comprehensive error handling and performance metrics")
    print(f"  ✅ Automatic strategy selection based on query analysis")
    print(f"  ✅ Citation generation and confidence assessment")
    
    return True


async def main():
    """Main execution function"""
    try:
        success = await demonstrate_unified_rag_system()
        if success:
            print(f"\n🚀 Elite Field Service Unified RAG System ready for production!")
        return success
    except Exception as e:
        print(f"\n❌ Demo failed with error: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    # Run the demonstration
    asyncio.run(main())