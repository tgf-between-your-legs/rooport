#!/usr/bin/env python3
"""
ROOPORT CONVEX System Demonstration
Shows the full capabilities of the Ultimate Agentic Orchestrator
"""

import asyncio
import sys
import os
from datetime import datetime

# Add rooport to path for demo
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

async def demo_convex_system():
    """Demonstrate CONVEX system capabilities"""
    print("🚀 ROOPORT CONVEX System Demo")
    print("=" * 50)
    
    try:
        from rooport.convex.ultimate_agentic_orchestrator import UltimateAgenticOrchestrator
        from unittest.mock import Mock
        
        # Create mock ConPort client for demo
        mock_conport = Mock()
        mock_conport.log_custom_data = lambda **kwargs: print(f"📝 Logged to ConPort: {kwargs.get('category', 'Unknown')}")
        mock_conport.get_product_context = lambda **kwargs: {"project": "ROOPORT Development"}
        
        # Initialize CONVEX orchestrator
        print("🔄 Initializing Ultimate Agentic Orchestrator...")
        orchestrator = UltimateAgenticOrchestrator(conport_client=mock_conport)
        print("✅ CONVEX System initialized successfully!")
        
        # Demo queries showcasing different capabilities
        demo_queries = [
            "How can I optimize my Python code for better performance?",
            "Suggest architectural improvements for a web application",
            "Help me understand best practices for API design",
            "What are the latest trends in AI-powered development tools?"
        ]
        
        workspace_id = os.path.abspath(".")
        
        for i, query in enumerate(demo_queries, 1):
            print(f"\n🎯 Demo Query {i}: {query}")
            print("-" * 40)
            
            try:
                # Process query with CONVEX
                response = await orchestrator.process_ultimate_request(query, workspace_id)
                
                # Display results
                print(f"📝 Primary Response: {response.primary_response}")
                print(f"🎯 Confidence Score: {response.confidence_score:.2f}")
                print(f"⚡ Execution Time: {response.execution_time:.3f}s")
                
                if response.proactive_suggestions:
                    print(f"🚀 Proactive Suggestions ({len(response.proactive_suggestions)}):")
                    for j, suggestion in enumerate(response.proactive_suggestions[:3]):
                        print(f"  {j+1}. {suggestion}")
                
                if response.system_improvements:
                    print(f"🔧 System Improvements ({len(response.system_improvements)}):")
                    for improvement in response.system_improvements[:2]:
                        print(f"  • {improvement}")
                
                print(f"🧠 RAG Status: {response.rag_insights.get('status', 'Unknown')}")
                print(f"📈 Learning Status: {response.learning_feedback.get('status', 'Unknown')}")
                
            except Exception as e:
                print(f"❌ Query processing failed: {e}")
                
        print(f"\n🎉 CONVEX Demo Complete!")
        print("🏆 ROOPORT - The Ultimate Agentic Coding Tool")
        
    except ImportError as e:
        print(f"❌ Failed to import CONVEX components: {e}")
        print("💡 Make sure ROOPORT is properly installed: pip install -e .")
        
    except Exception as e:
        print(f"❌ Demo failed: {e}")
        import traceback
        traceback.print_exc()

def demo_individual_components():
    """Demonstrate individual CONVEX components"""
    print("\n🔍 Individual Component Demo")
    print("=" * 30)
    
    try:
        from rooport.rag.engines.agentic_rag import AgenticRAGEngine
        from rooport.convex.proactive_orchestration_engine import ProactiveOrchestrationEngine
        from rooport.convex.continuous_learning_system import ContinuousLearningSystem
        from unittest.mock import Mock
        
        mock_conport = Mock()
        workspace_id = os.path.abspath(".")
        
        print("✅ AgenticRAGEngine available")
        print("✅ ProactiveOrchestrationEngine available") 
        print("✅ ContinuousLearningSystem available")
        print("✅ All CONVEX components ready!")
        
    except ImportError as e:
        print(f"⚠️ Some components not available: {e}")

if __name__ == "__main__":
    print("🚀 Starting ROOPORT CONVEX System Demo...")
    print(f"📅 Demo Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🐍 Python Version: {sys.version}")
    print()
    
    # Run the main demo
    asyncio.run(demo_convex_system())
    
    # Show component availability
    demo_individual_components()
    
    print(f"\n📖 For more information, visit: https://github.com/tgf-between-your-legs/rooport")
    print("🔗 Documentation: https://github.com/tgf-between-your-legs/rooport/tree/main/docs")