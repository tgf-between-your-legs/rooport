"""
Comprehensive Integration Tests for Unified RAG System
Elite Field Service SaaS Platform

Tests the integrated RAG system with:
- ConPort integration
- Semantic search capabilities  
- Multiple retrieval strategies
- Error handling and recovery
- Performance validation
"""

import pytest
import asyncio
from unittest.mock import AsyncMock, MagicMock
from datetime import datetime

from ..engines.agentic_rag import (
    AgenticRAGEngine, AgenticRAGResponse, ConfidenceLevel, RetrievalStrategy
)


class MockConPortClient:
    """Mock ConPort client for testing"""
    
    def __init__(self):
        self.search_decisions_fts = AsyncMock()
        self.search_custom_data_value_fts = AsyncMock()
        self.log_custom_data = AsyncMock()
        
        # Setup default responses
        self.search_decisions_fts.return_value = {
            'decisions': [
                {
                    'id': 1,
                    'summary': 'Test decision about Elite Field Service architecture',
                    'rationale': 'Using microservices for scalability'
                }
            ]
        }
        
        self.search_custom_data_value_fts.return_value = {
            'results': [
                {
                    'id': 1,
                    'category': 'architecture',
                    'key': 'service_pattern',
                    'value': 'Microservices pattern for field service management'
                }
            ]
        }


class MockSemanticEngine:
    """Mock semantic search engine for testing"""
    
    def __init__(self):
        self.semantic_search = AsyncMock()
        
        # Setup default response

class MockVertexMCPClient:
    """Mock Vertex MCP client for batch code analysis"""
    def __init__(self):
        self.batch_code_analysis = AsyncMock()
        # Return a dummy analysis result
        self.batch_code_analysis.return_value = {
            "results": [
                {"snippet": "def foo(): pass", "analysis": "No issues found."}
            ]
        }
        self.semantic_search.return_value = [
            MagicMock(
                content='Semantic search result about field service optimization',
                metadata={'source': 'semantic_db', 'id': 'sem_1'},
                score=0.85
            )
        ]


@pytest.fixture
def mock_conport_client():
    """Fixture for mock ConPort client"""
    return MockConPortClient()


@pytest.fixture
def mock_semantic_engine():
    """Fixture for mock semantic engine"""
    return MockSemanticEngine()


@pytest.fixture
def rag_engine(mock_conport_client, mock_semantic_engine):
    """Fixture for RAG engine with mocked dependencies"""
    # Import the synthesizer and inject the mock MCP client
    from ..synthesizers.information_synthesizer import InformationSynthesizer
    mock_vertex_mcp_client = MockVertexMCPClient()
    synthesizer = InformationSynthesizer(vertex_mcp_client=mock_vertex_mcp_client)
    # The AgenticRAGEngine should be updated to accept a synthesizer instance if not already
    return AgenticRAGEngine(
        conport_client=mock_conport_client,
        semantic_engine=mock_semantic_engine,
        synthesizer=synthesizer
    )


@pytest.mark.asyncio
class TestAgenticRAGEngine:
    """Test suite for the Agentic RAG Engine"""
    
    async def test_basic_query_processing(self, rag_engine):
        """Test basic query processing functionality"""
        query = "What is the architecture pattern for Elite Field Service?"
        workspace_id = "test_workspace"
        
        response = await rag_engine.process_query(query, workspace_id)
        
        assert isinstance(response, AgenticRAGResponse)
        assert response.query == query
        assert response.confidence_level in ConfidenceLevel
        assert len(response.retrieved_items) > 0
        assert len(response.reasoning_chain) > 0
        assert response.execution_time > 0
    
    async def test_conport_only_strategy(self, rag_engine):
        """Test ConPort-only retrieval strategy"""
        query = "Show me project decisions"
        workspace_id = "test_workspace"
        
        response = await rag_engine.process_query(
            query, workspace_id, 
            strategy=RetrievalStrategy.CONPORT_ONLY
        )
        
        assert response.retrieval_strategy == RetrievalStrategy.CONPORT_ONLY
        assert any('decision' in item.get('type', '') for item in response.retrieved_items)
        assert len(response.sources_used) > 0
    
    async def test_semantic_only_strategy(self, rag_engine):
        """Test semantic-only retrieval strategy"""
        query = "Find similar field service patterns"
        workspace_id = "test_workspace"
        
        response = await rag_engine.process_query(
            query, workspace_id,
            strategy=RetrievalStrategy.SEMANTIC_ONLY
        )
        
        assert response.retrieval_strategy == RetrievalStrategy.SEMANTIC_ONLY
        assert any('semantic' in item.get('type', '') for item in response.retrieved_items)
    
    async def test_hybrid_strategy(self, rag_engine):
        """Test hybrid retrieval strategy combining ConPort and semantic"""
        query = "Comprehensive analysis of field service architecture"
        workspace_id = "test_workspace"
        
        response = await rag_engine.process_query(
            query, workspace_id,
            strategy=RetrievalStrategy.HYBRID
        )
        
        assert response.retrieval_strategy == RetrievalStrategy.HYBRID
        # Should have items from both sources
        item_types = [item.get('type', '') for item in response.retrieved_items]
        assert len(set(item_types)) > 1  # Multiple types from different sources
    
    async def test_auto_strategy_selection(self, rag_engine):
        """Test automatic strategy selection based on query analysis"""
        # Query that should trigger ConPort strategy
        decision_query = "What decisions were made about the system?"
        response = await rag_engine.process_query(decision_query, "test_workspace")
        
        # Should select ConPort strategy for decision-related queries
        assert response.retrieval_strategy == RetrievalStrategy.CONPORT_ONLY
        
        # Query that should trigger semantic strategy
        semantic_query = "Find similar patterns in the codebase"
        response = await rag_engine.process_query(semantic_query, "test_workspace")
        
        # Should select semantic strategy for similarity queries
        assert response.retrieval_strategy == RetrievalStrategy.SEMANTIC_ONLY
    
    async def test_confidence_calculation(self, rag_engine):
        """Test confidence level calculation based on results"""
        # High confidence scenario (multiple good sources)
        rag_engine.config['min_sources_for_high_confidence'] = 2
        
        query = "Architecture decisions for field service"
        response = await rag_engine.process_query(query, "test_workspace")
        
        # Should have some confidence level assigned
        assert response.confidence_level in ConfidenceLevel
        
        # Test insufficient confidence with no results
        rag_engine.conport_client.search_decisions_fts.return_value = {'decisions': []}
        rag_engine.conport_client.search_custom_data_value_fts.return_value = {'results': []}
        rag_engine.semantic_engine.semantic_search.return_value = []
        
        response = await rag_engine.process_query("empty query", "test_workspace")
        assert response.confidence_level == ConfidenceLevel.INSUFFICIENT
    
    async def test_error_handling(self, rag_engine):
        """Test error handling and recovery"""
        # Simulate ConPort client error
        rag_engine.conport_client.search_decisions_fts.side_effect = Exception("ConPort error")
        
        query = "Test error handling"
        response = await rag_engine.process_query(query, "test_workspace")
        
        # Should return error response
        assert response.confidence_level == ConfidenceLevel.INSUFFICIENT
        assert "Error processing query" in response.final_answer
        assert any("Error occurred" in step for step in response.reasoning_chain)
    
    async def test_performance_metrics_tracking(self, rag_engine):
        """Test performance metrics collection"""
        initial_metrics = rag_engine.get_performance_metrics()
        assert initial_metrics['total_queries'] == 0
        
        # Execute a query
        await rag_engine.process_query("test query", "test_workspace")
        
        updated_metrics = rag_engine.get_performance_metrics()
        assert updated_metrics['total_queries'] == 1
        assert updated_metrics['avg_response_time'] > 0
        assert 0 <= updated_metrics['success_rate'] <= 1
    
    async def test_logging_integration(self, rag_engine):
        """Test ConPort logging integration"""
        query = "Test logging functionality"
        await rag_engine.process_query(query, "test_workspace")
        
        # Verify log_custom_data was called
        rag_engine.conport_client.log_custom_data.assert_called_once()
        
        # Check the logged data structure
        call_args = rag_engine.conport_client.log_custom_data.call_args
        assert call_args[1]['category'] == "AgenticRAGExecution"
        assert 'query' in call_args[1]['value']
        assert 'confidence_level' in call_args[1]['value']
        assert 'execution_time' in call_args[1]['value']
    
    async def test_response_structure_completeness(self, rag_engine):
        """Test that response contains all required fields"""
        query = "Complete response test"
        response = await rag_engine.process_query(query, "test_workspace")
        
        # Verify all required fields are present
        required_fields = [
            'query', 'final_answer', 'confidence_level', 'sources_used',
            'retrieval_strategy', 'retrieved_items', 'relevance_scores',
            'reasoning_chain', 'execution_time', 'metadata', 'timestamp'
        ]
        
        for field in required_fields:
            assert hasattr(response, field), f"Missing required field: {field}"
            assert getattr(response, field) is not None, f"Field {field} is None"
    
    async def test_concurrent_query_processing(self, rag_engine):
        """Test concurrent query processing"""
        queries = [
            "Query 1: Field service architecture",
            "Query 2: Decision patterns",
            "Query 3: System optimization"
        ]
        
        # Execute queries concurrently
        tasks = [
            rag_engine.process_query(query, "test_workspace") 
            for query in queries
        ]
        responses = await asyncio.gather(*tasks)
        
        # Verify all queries completed successfully
        assert len(responses) == 3
        for i, response in enumerate(responses):
            assert response.query == queries[i]
            assert isinstance(response, AgenticRAGResponse)
    
    def test_configuration_management(self, mock_conport_client):
        """Test configuration management and defaults"""
        # Test default configuration
        engine = AgenticRAGEngine(mock_conport_client)
        config = engine.config
        
        assert 'max_retrieval_items' in config
        assert 'confidence_threshold' in config
        assert 'enable_semantic_search' in config
        
        # Test custom configuration
        custom_config = {
            'max_retrieval_items': 15,
            'confidence_threshold': 0.8,
            'timeout_seconds': 45.0
        }
        
        engine_custom = AgenticRAGEngine(mock_conport_client, config=custom_config)
        assert engine_custom.config['max_retrieval_items'] == 15
        assert engine_custom.config['confidence_threshold'] == 0.8


@pytest.mark.asyncio
class TestIntegrationScenarios:
    """Integration test scenarios for real-world usage"""
    
    async def test_elite_field_service_query_scenario(self, rag_engine):
        """Test a realistic Elite Field Service query scenario"""
        query = """
        What are the recommended architecture patterns for implementing 
        real-time field technician tracking in our SaaS platform?
        """
        
        response = await rag_engine.process_query(query, "elite_field_service")
        
        # Verify realistic response characteristics
        assert len(response.final_answer) > 100  # Substantial answer
        assert response.confidence_level != ConfidenceLevel.INSUFFICIENT
        assert len(response.retrieved_items) > 0
        assert response.execution_time < 30.0  # Reasonable performance
    
    async def test_empty_workspace_scenario(self, rag_engine):
        """Test handling of empty workspace with no data"""
        # Configure mocks to return empty results
        rag_engine.conport_client.search_decisions_fts.return_value = {'decisions': []}
        rag_engine.conport_client.search_custom_data_value_fts.return_value = {'results': []}
        rag_engine.semantic_engine.semantic_search.return_value = []
        
        query = "Find information about anything"
        response = await rag_engine.process_query(query, "empty_workspace")
        
        assert "No relevant information found" in response.final_answer
        assert response.confidence_level == ConfidenceLevel.INSUFFICIENT
        assert len(response.retrieved_items) == 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])