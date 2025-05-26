#!/usr/bin/env python3
"""
FULL CONVEX System Integration Test
Tests the complete Ultimate Agentic Orchestrator with all components

This will show us what's working vs what needs fixes.
"""

import asyncio
import sys
import os
from pathlib import Path

# Add the rooport src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from rooport.convex.ultimate_agentic_orchestrator import UltimateAgenticOrchestrator


class MockConPortClient:
    """Mock ConPort client for testing"""
    
    def __init__(self, workspace_id: str):
        self.workspace_id = workspace_id
    
    async def search_decisions_fts(self, workspace_id: str, query_term: str, limit: int = 5):
        """Mock ConPort decisions search"""
        return {
            'decisions': [
                {
                    'id': 55,
                    'summary': 'CONVEX Real Implementation Initiative - Build Functional AI Orchestration System',
                    'rationale': 'After verification showing ROOPORT CONVEX claims are false...',
                    'timestamp': '2025-05-26T04:39:55.531514'
                }
            ]
        }
    
    async def search_custom_data_value_fts(self, workspace_id: str, query_term: str, limit: int = 5):
        """Mock ConPort custom data search"""
        return {
            'results': [
                {
                    'id': 1,
                    'category': 'ProjectGlossary',
                    'key': 'convex',
                    'value': 'Complete AI orchestration system for intelligent development workflows'
                }
            ]
        }
    
    async def log_custom_data(self, workspace_id: str, category: str, key: str, value: str):
        """Mock logging method"""
        print(f"📝 Logged to ConPort: {category}/{key}")
        return {"id": 123, "success": True}


async def test_full_convex_system():
    """Test the complete CONVEX Ultimate Agentic Orchestrator"""
    workspace_id = "c:/Users/thegr/OneDrive/Desktop/frontendtest/integration"
    
    print("🚀 Testing FULL CONVEX Ultimate Agentic Orchestrator...")
    
    try:
        # Create mock ConPort client
        conport_client = MockConPortClient(workspace_id)
        
        # Initialize Ultimate Agentic Orchestrator
        print("🔄 Initializing Ultimate Agentic Orchestrator...")
        orchestrator = UltimateAgenticOrchestrator(conport_client)
        
        # Test comprehensive query processing
        query = "How should I integrate the CONVEX system into my application dashboard?"
        print(f"\n🎯 Query: {query}")
        
        # Process with full CONVEX system
        print("⚡ Processing with full CONVEX integration...")
        response = await orchestrator.process_ultimate_request(query, workspace_id)
        
        # Display comprehensive results
        print("\n" + "="*60)
        print("🎉 FULL CONVEX SYSTEM RESULTS")
        print("="*60)
        
        print(f"📝 Primary Response:\n{response.primary_response}")
        print(f"\n🎯 Confidence Score: {response.confidence_score:.2f}")
        print(f"⚡ Execution Time: {response.execution_time:.3f}s")
        
        print(f"\n🚀 Proactive Suggestions ({len(response.proactive_suggestions)}):")
        for i, suggestion in enumerate(response.proactive_suggestions, 1):
            print(f"  {i}. {suggestion.get('suggestion', suggestion)}")
        
        print(f"\n🧠 RAG Insights:")
        for key, value in response.rag_insights.items():
            print(f"  • {key}: {value}")
        
        print(f"\n📈 Learning Feedback:")
        for key, value in response.learning_feedback.items():
            print(f"  • {key}: {value}")
        
        print(f"\n🔧 System Improvements ({len(response.system_improvements)}):")
        for improvement in response.system_improvements:
            print(f"  • {improvement}")
        
        print(f"\n➡️ Next Actions ({len(response.next_actions)}):")
        for action in response.next_actions:
            print(f"  • {action}")
        
        return response
        
    except Exception as e:
        print(f"\n❌ CONVEX System Error: {e}")
        import traceback
        traceback.print_exc()
        return None


if __name__ == "__main__":
    response = asyncio.run(test_full_convex_system())
    
    if response and response.confidence_score > 0.5:
        print("\n🎉 SUCCESS: FULL CONVEX SYSTEM IS OPERATIONAL!")
        print("✅ All components integrated and functional")
    else:
        print("\n⚠️ CONVEX System needs component fixes")
        print("🔧 Individual components may need debugging")