#!/usr/bin/env python3
"""
Ultimate Agentic Orchestrator for ROOPORT
Integrates all AI enrichment components into a unified intelligent system
"""

import asyncio
import logging
from datetime import datetime
from typing import Dict, List, Optional, Any
from dataclasses import dataclass

# Import all core components
from .proactive_engine import ProactiveOrchestrationEngine
from .learning_system import ContinuousLearningSystem
from .rag_engine import AgenticRAGEngine

@dataclass
class UltimateAgenticResponse:
    """Response from the ultimate agentic system"""
    user_query: str
    primary_response: str
    proactive_suggestions: List[Dict]
    rag_insights: Dict[str, Any]
    learning_feedback: Dict[str, Any]
    confidence_score: float
    execution_time: float
    system_improvements: List[str]
    next_actions: List[str]

class UltimateAgenticOrchestrator:
    """Master orchestrator for all AI enrichment capabilities"""
    
    def __init__(self, conport_client, vertex_ai_client=None):
        self.conport = conport_client
        self.vertex_ai = vertex_ai_client
        self.logger = logging.getLogger(__name__)
        
        # Initialize core engines
        self.poe = ProactiveOrchestrationEngine(conport_client)
        self.cls = ContinuousLearningSystem(conport_client)
        self.rag = AgenticRAGEngine(conport_client)
        
        # Performance tracking
        self.execution_metrics = []
        
    async def process_ultimate_request(self, user_query: str, workspace_id: str, 
                                     context: Dict[str, Any] = None) -> UltimateAgenticResponse:
        """Process user request with full agentic capabilities"""
        start_time = datetime.now()
        
        try:
            self.logger.info(f"Processing ultimate agentic request: {user_query}")
            
            # Phase 1: Parallel execution of core engines
            rag_task = self._execute_agentic_rag(user_query, workspace_id)
            poe_task = self._execute_proactive_orchestration(workspace_id)
            learning_task = self._execute_continuous_learning(workspace_id)
            
            # Execute in parallel for maximum efficiency
            rag_response, poe_suggestions, learning_feedback = await asyncio.gather(
                rag_task, poe_task, learning_task, return_exceptions=True
            )
            
            # Phase 2: Synthesize results
            primary_response = self._synthesize_primary_response(rag_response, user_query)
            proactive_suggestions = self._process_proactive_suggestions(poe_suggestions)
            learning_insights = self._process_learning_feedback(learning_feedback)
            
            # Phase 3: Meta-analysis and improvement identification
            confidence_score = self._calculate_overall_confidence(rag_response, poe_suggestions)
            system_improvements = self._identify_system_improvements(rag_response, poe_suggestions, learning_feedback)
            next_actions = self._determine_next_actions(proactive_suggestions, system_improvements)
            
            # Phase 4: Log execution and update metrics
            execution_time = (datetime.now() - start_time).total_seconds()
            await self._log_ultimate_execution(workspace_id, user_query, execution_time, confidence_score)
            
            return UltimateAgenticResponse(
                user_query=user_query,
                primary_response=primary_response,
                proactive_suggestions=proactive_suggestions,
                rag_insights=self._extract_rag_insights(rag_response),
                learning_feedback=learning_insights,
                confidence_score=confidence_score,
                execution_time=execution_time,
                system_improvements=system_improvements,
                next_actions=next_actions
            )
            
        except Exception as e:
            self.logger.error(f"Ultimate agentic processing failed: {e}")
            return self._error_response(user_query, str(e))
    
    async def _execute_agentic_rag(self, query: str, workspace_id: str):
        """Execute agentic RAG with error handling"""
        try:
            return await self.rag.process_query(query, workspace_id)
        except Exception as e:
            self.logger.error(f"Agentic RAG execution failed: {e}")
            return None
    
    async def _execute_proactive_orchestration(self, workspace_id: str):
        """Execute proactive orchestration with error handling"""
        try:
            return await self.poe.generate_suggestions(workspace_id)
        except Exception as e:
            self.logger.error(f"Proactive orchestration failed: {e}")
            return []
    
    async def _execute_continuous_learning(self, workspace_id: str):
        """Execute continuous learning with error handling"""
        try:
            return await self.cls.run_learning_cycle(workspace_id)
        except Exception as e:
            self.logger.error(f"Continuous learning failed: {e}")
            return {}
    
    def _synthesize_primary_response(self, rag_response, user_query: str) -> str:
        """Synthesize primary response from RAG results"""
        if rag_response and hasattr(rag_response, 'final_answer'):
            base_response = rag_response.final_answer
            
            # Enhance with confidence and source information
            if hasattr(rag_response, 'confidence_level') and rag_response.confidence_level.value != 'high':
                base_response += f"\n\n*Note: Response confidence is {rag_response.confidence_level.value}*"
            
            if hasattr(rag_response, 'sources_used') and rag_response.sources_used:
                base_response += f"\n\n*Based on {len(rag_response.sources_used)} sources*"
            
            return base_response
        else:
            return f"I understand you're asking about: {user_query}. Let me help you with that based on available information."
    
    def _process_proactive_suggestions(self, poe_suggestions) -> List[Dict]:
        """Process proactive orchestration suggestions"""
        if not poe_suggestions or not isinstance(poe_suggestions, list):
            return []
        
        processed_suggestions = []
        for suggestion in poe_suggestions[:5]:  # Limit to top 5
            if hasattr(suggestion, '__dict__'):
                processed_suggestions.append({
                    'title': getattr(suggestion, 'title', 'Suggestion'),
                    'description': getattr(suggestion, 'description', ''),
                    'priority': getattr(suggestion, 'priority', 'medium'),
                    'actions': getattr(suggestion, 'suggested_actions', []),
                    'confidence': getattr(suggestion, 'confidence_score', 0.5)
                })
        
        return processed_suggestions
    
    def _process_learning_feedback(self, learning_feedback) -> Dict[str, Any]:
        """Process continuous learning feedback"""
        if not learning_feedback or not isinstance(learning_feedback, dict):
            return {'status': 'no_feedback', 'insights': []}
        
        return {
            'status': 'active',
            'agents_analyzed': len(learning_feedback.get('agents_analyzed', [])),
            'proposals_generated': len(learning_feedback.get('proposals_generated', [])),
            'insights': self._extract_learning_insights(learning_feedback),
            'errors': learning_feedback.get('errors', [])
        }
    
    def _extract_learning_insights(self, learning_feedback: Dict) -> List[str]:
        """Extract key insights from learning feedback"""
        insights = []
        
        agents_analyzed = learning_feedback.get('agents_analyzed', [])
        for agent_data in agents_analyzed:
            agent = agent_data.get('agent', 'unknown')
            metrics = agent_data.get('metrics', {})
            
            completion_rate = metrics.get('task_completion_rate', 1.0)
            error_frequency = metrics.get('error_frequency', 0.0)
            user_rating = metrics.get('average_user_rating', 3.0)
            
            if completion_rate < 0.8:
                insights.append(f"{agent}: Low completion rate ({completion_rate:.1%})")
            
            if error_frequency > 0.1:
                insights.append(f"{agent}: High error rate ({error_frequency:.1%})")
            
            if user_rating < 3.5:
                insights.append(f"{agent}: Below average user rating ({user_rating:.1f}/5)")
        
        return insights
    
    def _calculate_overall_confidence(self, rag_response, poe_suggestions) -> float:
        """Calculate overall system confidence"""
        confidence_factors = []
        
        # RAG confidence
        if rag_response and hasattr(rag_response, 'confidence_level'):
            confidence_values = {'high': 1.0, 'medium': 0.7, 'low': 0.4, 'insufficient': 0.1}
            rag_confidence = confidence_values.get(rag_response.confidence_level.value, 0.5)
            confidence_factors.append(rag_confidence * 0.6)  # 60% weight
        
        # POE confidence (based on suggestion quality)
        if poe_suggestions and isinstance(poe_suggestions, list):
            avg_poe_confidence = sum(getattr(s, 'confidence_score', 0.5) for s in poe_suggestions) / len(poe_suggestions)
            confidence_factors.append(avg_poe_confidence * 0.3)  # 30% weight
        
        # System health (simplified)
        confidence_factors.append(0.8 * 0.1)  # 10% weight - baseline system health
        
        return sum(confidence_factors) if confidence_factors else 0.5
    
    def _identify_system_improvements(self, rag_response, poe_suggestions, learning_feedback) -> List[str]:
        """Identify potential system improvements"""
        improvements = []
        
        # RAG-based improvements
        if rag_response and hasattr(rag_response, 'improvement_suggestions'):
            improvements.extend(rag_response.improvement_suggestions)
        
        # Learning-based improvements
        if isinstance(learning_feedback, dict):
            proposals = learning_feedback.get('proposals_generated', [])
            for proposal in proposals[:3]:  # Top 3 proposals
                if isinstance(proposal, dict):
                    improvements.append(proposal.get('proposed_change_description', 'System optimization'))
        
        # Performance-based improvements
        if rag_response and hasattr(rag_response, 'execution_time'):
            if rag_response.execution_time > 10.0:  # Slow response
                improvements.append("Optimize RAG response time - consider caching strategies")
        
        return improvements[:5]  # Limit to top 5
    
    def _determine_next_actions(self, proactive_suggestions: List[Dict], 
                              system_improvements: List[str]) -> List[str]:
        """Determine recommended next actions"""
        actions = []
        
        # Add high-priority proactive suggestions
        for suggestion in proactive_suggestions:
            if suggestion.get('priority') in ['high', 'critical']:
                actions.extend(suggestion.get('actions', [])[:2])  # Top 2 actions per suggestion
        
        # Add system improvements as actions
        for improvement in system_improvements[:2]:  # Top 2 improvements
            actions.append(f"Implement: {improvement}")
        
        # Add default actions if none found
        if not actions:
            actions = [
                "Continue current task execution",
                "Monitor system performance",
                "Gather user feedback"
            ]
        
        return actions[:5]  # Limit to 5 actions
    
    def _extract_rag_insights(self, rag_response) -> Dict[str, Any]:
        """Extract insights from RAG response"""
        if not rag_response or not hasattr(rag_response, '__dict__'):
            return {'status': 'no_insights'}
        
        return {
            'status': 'active',
            'retrieval_iterations': getattr(rag_response, 'retrieval_iterations', 0),
            'sources_count': len(getattr(rag_response, 'sources_used', [])),
            'reasoning_steps': len(getattr(rag_response, 'reasoning_chain', [])),
            'validation_checks': len(getattr(rag_response, 'validation_checks', [])),
            'execution_time': getattr(rag_response, 'execution_time', 0)
        }
    
    async def _log_ultimate_execution(self, workspace_id: str, query: str, 
                                    execution_time: float, confidence_score: float):
        """Log ultimate agentic execution to ConPort"""
        try:
            execution_id = f"ULTIMATE-EXEC-{datetime.now().strftime('%Y%m%d%H%M%S')}"
            
            await self.conport.log_custom_data(
                workspace_id=workspace_id,
                category="UltimateAgenticExecution",
                key=execution_id,
                value={
                    "query": query,
                    "confidence_score": confidence_score,
                    "execution_time": execution_time,
                    "timestamp": datetime.now().isoformat(),
                    "components_used": ["RAG", "POE", "CLS"]
                }
            )
            
            # Update execution metrics
            self.execution_metrics.append({
                'timestamp': datetime.now(),
                'execution_time': execution_time,
                'confidence_score': confidence_score
            })
            
            # Keep only recent metrics
            if len(self.execution_metrics) > 100:
                self.execution_metrics = self.execution_metrics[-100:]
                
        except Exception as e:
            self.logger.error(f"Failed to log ultimate execution: {e}")
    
    def _error_response(self, user_query: str, error_msg: str) -> UltimateAgenticResponse:
        """Return error response"""
        return UltimateAgenticResponse(
            user_query=user_query,
            primary_response=f"I encountered an issue processing your request: {error_msg}",
            proactive_suggestions=[],
            rag_insights={'status': 'error'},
            learning_feedback={'status': 'error'},
            confidence_score=0.0,
            execution_time=0.0,
            system_improvements=["Debug and fix system error"],
            next_actions=["Retry request", "Report issue to system administrator"]
        )
    
    async def run_system_optimization_cycle(self, workspace_id: str) -> Dict[str, Any]:
        """Run a complete system optimization cycle"""
        try:
            self.logger.info("Running system optimization cycle")
            
            # Run continuous learning cycle
            learning_results = await self.cls.run_learning_cycle(workspace_id)
            
            # Generate proactive suggestions for system state
            poe_suggestions = await self.poe.generate_suggestions(workspace_id)
            
            # Analyze recent execution metrics
            performance_analysis = self._analyze_performance_metrics()
            
            # Generate optimization recommendations
            optimizations = self._generate_optimization_recommendations(
                learning_results, poe_suggestions, performance_analysis
            )
            
            # Log optimization cycle
            await self._log_optimization_cycle(workspace_id, optimizations)
            
            return {
                'status': 'completed',
                'learning_results': learning_results,
                'poe_suggestions_count': len(poe_suggestions),
                'performance_analysis': performance_analysis,
                'optimizations': optimizations,
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            self.logger.error(f"System optimization cycle failed: {e}")
            return {'status': 'failed', 'error': str(e)}
    
    def _analyze_performance_metrics(self) -> Dict[str, Any]:
        """Analyze recent performance metrics"""
        if not self.execution_metrics:
            return {'status': 'no_data'}
        
        recent_metrics = self.execution_metrics[-20:]  # Last 20 executions
        
        avg_execution_time = sum(m['execution_time'] for m in recent_metrics) / len(recent_metrics)
        avg_confidence = sum(m['confidence_score'] for m in recent_metrics) / len(recent_metrics)
        
        return {
            'status': 'analyzed',
            'sample_size': len(recent_metrics),
            'avg_execution_time': avg_execution_time,
            'avg_confidence_score': avg_confidence,
            'performance_trend': self._calculate_performance_trend(recent_metrics)
        }
    
    def _calculate_performance_trend(self, metrics: List[Dict]) -> str:
        """Calculate performance trend"""
        if len(metrics) < 5:
            return 'insufficient_data'
        
        early_avg = sum(m['confidence_score'] for m in metrics[:len(metrics)//2]) / (len(metrics)//2)
        late_avg = sum(m['confidence_score'] for m in metrics[len(metrics)//2:]) / (len(metrics) - len(metrics)//2)
        
        if late_avg > early_avg + 0.1:
            return 'improving'
        elif late_avg < early_avg - 0.1:
            return 'declining'
        else:
            return 'stable'
    
    def _generate_optimization_recommendations(self, learning_results: Dict, 
                                             poe_suggestions: List, 
                                             performance_analysis: Dict) -> List[str]:
        """Generate system optimization recommendations"""
        recommendations = []
        
        # Performance-based recommendations
        if performance_analysis.get('avg_execution_time', 0) > 5.0:
            recommendations.append("Optimize execution pipeline for faster response times")
        
        if performance_analysis.get('avg_confidence_score', 0) < 0.7:
            recommendations.append("Improve information retrieval quality and source diversity")
        
        if performance_analysis.get('performance_trend') == 'declining':
            recommendations.append("Investigate and address performance degradation causes")
        
        # Learning-based recommendations
        if learning_results.get('proposals_generated'):
            recommendations.append("Review and implement agent improvement proposals")
        
        # POE-based recommendations
        if len(poe_suggestions) < 3:
            recommendations.append("Enhance proactive suggestion generation capabilities")
        
        return recommendations[:5]
    
    async def _log_optimization_cycle(self, workspace_id: str, optimizations: List[str]):
        """Log optimization cycle to ConPort"""
        try:
            cycle_id = f"OPT-CYCLE-{datetime.now().strftime('%Y%m%d%H%M%S')}"
            
            await self.conport.log_custom_data(
                workspace_id=workspace_id,
                category="SystemOptimizationCycle",
                key=cycle_id,
                value={
                    "optimizations": optimizations,
                    "timestamp": datetime.now().isoformat(),
                    "cycle_type": "automated"
                }
            )
        except Exception as e:
            self.logger.error(f"Failed to log optimization cycle: {e}")

# Main integration function for ROOPORT
async def integrate_ultimate_agentic_system(workspace_id: str, user_query: str, 
                                          conport_client, vertex_ai_client=None) -> UltimateAgenticResponse:
    """Main integration point for the ultimate agentic system"""
    orchestrator = UltimateAgenticOrchestrator(conport_client, vertex_ai_client)
    response = await orchestrator.process_ultimate_request(user_query, workspace_id)
    return response

# System optimization function
async def run_ultimate_system_optimization(workspace_id: str, conport_client) -> Dict[str, Any]:
    """Run complete system optimization"""
    orchestrator = UltimateAgenticOrchestrator(conport_client)
    return await orchestrator.run_system_optimization_cycle(workspace_id)