#!/usr/bin/env python3
"""
Continuous Learning System for ROOPORT Agents
Implements feedback collection, performance analysis, and self-optimization
"""

import json
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, asdict
from enum import Enum
import statistics
import re

class FeedbackSource(Enum):
    USER_EXPLICIT = "user_explicit"
    USER_IMPLICIT_INFERRED = "user_implicit_inferred" 
    AGENT_OBSERVED = "agent_observed"
    SYSTEM_METRICS = "system_metrics"

class FeedbackCategory(Enum):
    ACCURACY = "accuracy"
    TOOL_ERROR = "tool_error"
    RESPONSE_QUALITY = "response_quality"
    TASK_COMPLETION = "task_completion"
    USER_SATISFACTION = "user_satisfaction"
    PERFORMANCE = "performance"

class ReviewStatus(Enum):
    PENDING_REVIEW = "pending_review"
    REVIEWED_ACTION_TAKEN = "reviewed_action_taken"
    REVIEWED_NO_ACTION = "reviewed_no_action"
    ARCHIVED = "archived"

@dataclass
class AgentFeedback:
    """Structured feedback about agent performance"""
    feedback_id: str
    timestamp: datetime
    source_of_feedback: FeedbackSource
    agent_slug_target: str
    agent_slug_reporter: str
    mdtm_task_id_context: Optional[str] = None
    session_id_context: Optional[str] = None
    interaction_summary_context: str = ""
    user_rating: Optional[int] = None
    feedback_categories: List[FeedbackCategory] = None
    feedback_text_positive: str = ""
    feedback_text_negative: str = ""
    suggested_correction_action: str = ""
    raw_user_input_triggering_feedback: str = ""
    status_of_feedback_review: ReviewStatus = ReviewStatus.PENDING_REVIEW
    review_notes: str = ""

@dataclass
class PerformanceMetrics:
    """Agent performance metrics over time"""
    agent_slug: str
    time_period: timedelta
    task_completion_rate: float
    average_user_rating: float
    error_frequency: float
    response_time_avg: float
    feedback_count: int
    improvement_trend: float

@dataclass
class RefinementProposal:
    """Proposal for agent improvement"""
    proposal_id: str
    timestamp_proposed: datetime
    source_analysis_ids: List[str]
    target_component_type: str  # KB, rule, prompt
    target_component_identifier: str
    problem_summary: str
    proposed_change_description: str
    expected_impact_benefit: str
    priority: str
    status: str
    review_notes: str = ""
    implementation_mdtm_task_id: Optional[str] = None

class FeedbackCollector:
    """Collects and structures feedback from various sources"""
    
    def __init__(self, conport_client):
        self.conport = conport_client
        self.logger = logging.getLogger(__name__)
    
    async def log_agent_feedback(self, workspace_id: str, feedback: AgentFeedback) -> bool:
        """Log feedback to ConPort"""
        try:
            feedback_data = asdict(feedback)
            # Convert enums to strings for storage
            feedback_data['source_of_feedback'] = feedback.source_of_feedback.value
            feedback_data['feedback_categories'] = [cat.value for cat in (feedback.feedback_categories or [])]
            feedback_data['status_of_feedback_review'] = feedback.status_of_feedback_review.value
            feedback_data['timestamp'] = feedback.timestamp.isoformat()
            
            await self.conport.log_custom_data(
                workspace_id=workspace_id,
                category="AgentInteractionFeedback",
                key=feedback.feedback_id,
                value=feedback_data
            )
            
            self.logger.info(f"Logged feedback {feedback.feedback_id} for agent {feedback.agent_slug_target}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to log feedback: {e}")
            return False
    
    def create_feedback_from_user_interaction(self, 
                                            agent_target: str,
                                            user_input: str,
                                            rating: Optional[int] = None,
                                            positive_text: str = "",
                                            negative_text: str = "",
                                            context_task_id: str = "",
                                            context_session_id: str = "") -> AgentFeedback:
        """Create feedback object from user interaction"""
        
        feedback_id = f"FDBK-{datetime.now().strftime('%Y%m%d%H%M%S')}-{agent_target}"
        
        # Infer categories from feedback text
        categories = self._infer_feedback_categories(positive_text + " " + negative_text)
        
        return AgentFeedback(
            feedback_id=feedback_id,
            timestamp=datetime.now(),
            source_of_feedback=FeedbackSource.USER_EXPLICIT,
            agent_slug_target=agent_target,
            agent_slug_reporter="roo-commander",
            mdtm_task_id_context=context_task_id,
            session_id_context=context_session_id,
            interaction_summary_context=user_input[:200],
            user_rating=rating,
            feedback_categories=categories,
            feedback_text_positive=positive_text,
            feedback_text_negative=negative_text,
            raw_user_input_triggering_feedback=user_input
        )
    
    def create_agent_observed_feedback(self,
                                     observer_agent: str,
                                     target_agent: str,
                                     observation: str,
                                     suggested_improvement: str = "",
                                     context_task_id: str = "") -> AgentFeedback:
        """Create feedback from agent self-observation"""
        
        feedback_id = f"FDBK-{datetime.now().strftime('%Y%m%d%H%M%S')}-{target_agent}-OBS"
        
        return AgentFeedback(
            feedback_id=feedback_id,
            timestamp=datetime.now(),
            source_of_feedback=FeedbackSource.AGENT_OBSERVED,
            agent_slug_target=target_agent,
            agent_slug_reporter=observer_agent,
            mdtm_task_id_context=context_task_id,
            interaction_summary_context=observation[:200],
            feedback_text_negative=observation,
            suggested_correction_action=suggested_improvement,
            feedback_categories=[FeedbackCategory.PERFORMANCE]
        )
    
    def _infer_feedback_categories(self, feedback_text: str) -> List[FeedbackCategory]:
        """Infer feedback categories from text content"""
        categories = []
        text_lower = feedback_text.lower()
        
        if any(word in text_lower for word in ['accurate', 'correct', 'right', 'wrong', 'incorrect']):
            categories.append(FeedbackCategory.ACCURACY)
        
        if any(word in text_lower for word in ['error', 'failed', 'broken', 'crash']):
            categories.append(FeedbackCategory.TOOL_ERROR)
        
        if any(word in text_lower for word in ['quality', 'helpful', 'clear', 'confusing']):
            categories.append(FeedbackCategory.RESPONSE_QUALITY)
        
        if any(word in text_lower for word in ['complete', 'finished', 'done', 'incomplete']):
            categories.append(FeedbackCategory.TASK_COMPLETION)
        
        if any(word in text_lower for word in ['satisfied', 'happy', 'frustrated', 'annoyed']):
            categories.append(FeedbackCategory.USER_SATISFACTION)
        
        return categories if categories else [FeedbackCategory.RESPONSE_QUALITY]

class PerformanceAnalyzer:
    """Analyzes agent performance based on feedback and metrics"""
    
    def __init__(self, conport_client):
        self.conport = conport_client
        self.logger = logging.getLogger(__name__)
    
    async def analyze_agent_performance(self, workspace_id: str, agent_slug: str, 
                                      days_back: int = 30) -> PerformanceMetrics:
        """Analyze performance for specific agent over time period"""
        try:
            # Get feedback data for the agent
            feedback_data = await self._get_agent_feedback(workspace_id, agent_slug, days_back)
            
            # Calculate metrics
            metrics = self._calculate_performance_metrics(agent_slug, feedback_data, days_back)
            
            # Store analysis results
            await self._store_performance_analysis(workspace_id, metrics)
            
            return metrics
            
        except Exception as e:
            self.logger.error(f"Performance analysis failed for {agent_slug}: {e}")
            return self._empty_metrics(agent_slug, days_back)
    
    async def _get_agent_feedback(self, workspace_id: str, agent_slug: str, days_back: int) -> List[Dict]:
        """Retrieve feedback data for agent from ConPort"""
        try:
            # Search for feedback in AgentInteractionFeedback category
            # This would use ConPort search functionality
            feedback_data = []
            
            # Implementation would query ConPort custom_data with category filter
            # and parse results to find feedback for the specific agent
            
            return feedback_data
        except Exception as e:
            self.logger.error(f"Failed to retrieve feedback for {agent_slug}: {e}")
            return []
    
    def _calculate_performance_metrics(self, agent_slug: str, feedback_data: List[Dict], 
                                     days_back: int) -> PerformanceMetrics:
        """Calculate performance metrics from feedback data"""
        if not feedback_data:
            return self._empty_metrics(agent_slug, days_back)
        
        # Extract ratings
        ratings = [fb.get('user_rating') for fb in feedback_data if fb.get('user_rating')]
        avg_rating = statistics.mean(ratings) if ratings else 0.0
        
        # Count errors
        error_feedback = [fb for fb in feedback_data 
                         if 'tool_error' in fb.get('feedback_categories', [])]
        error_rate = len(error_feedback) / len(feedback_data) if feedback_data else 0.0
        
        # Calculate completion rate (simplified)
        completion_feedback = [fb for fb in feedback_data 
                             if 'task_completion' in fb.get('feedback_categories', [])]
        completion_rate = 1.0 - (len(completion_feedback) / len(feedback_data)) if feedback_data else 1.0
        
        # Response time would need to be tracked separately
        response_time_avg = 2.5  # Placeholder
        
        # Calculate improvement trend (simplified)
        improvement_trend = self._calculate_trend(feedback_data)
        
        return PerformanceMetrics(
            agent_slug=agent_slug,
            time_period=timedelta(days=days_back),
            task_completion_rate=completion_rate,
            average_user_rating=avg_rating,
            error_frequency=error_rate,
            response_time_avg=response_time_avg,
            feedback_count=len(feedback_data),
            improvement_trend=improvement_trend
        )
    
    def _calculate_trend(self, feedback_data: List[Dict]) -> float:
        """Calculate improvement trend from feedback over time"""
        if len(feedback_data) < 2:
            return 0.0
        
        # Sort by timestamp and compare early vs late ratings
        sorted_data = sorted(feedback_data, key=lambda x: x.get('timestamp', ''))
        
        early_ratings = [fb.get('user_rating', 3) for fb in sorted_data[:len(sorted_data)//2]]
        late_ratings = [fb.get('user_rating', 3) for fb in sorted_data[len(sorted_data)//2:]]
        
        early_avg = statistics.mean(early_ratings) if early_ratings else 3.0
        late_avg = statistics.mean(late_ratings) if late_ratings else 3.0
        
        return late_avg - early_avg
    
    def _empty_metrics(self, agent_slug: str, days_back: int) -> PerformanceMetrics:
        """Return empty metrics for error cases"""
        return PerformanceMetrics(
            agent_slug=agent_slug,
            time_period=timedelta(days=days_back),
            task_completion_rate=1.0,
            average_user_rating=3.0,
            error_frequency=0.0,
            response_time_avg=2.5,
            feedback_count=0,
            improvement_trend=0.0
        )
    
    async def _store_performance_analysis(self, workspace_id: str, metrics: PerformanceMetrics):
        """Store performance analysis results in ConPort"""
        try:
            analysis_id = f"PERF-ANALYSIS-{metrics.agent_slug}-{datetime.now().strftime('%Y%m%d')}"
            
            await self.conport.log_custom_data(
                workspace_id=workspace_id,
                category="PerformanceAnalysisReport",
                key=analysis_id,
                value=asdict(metrics)
            )
        except Exception as e:
            self.logger.error(f"Failed to store performance analysis: {e}")

class ImprovementStrategist:
    """Generates improvement proposals based on performance analysis"""
    
    def __init__(self, conport_client):
        self.conport = conport_client
        self.logger = logging.getLogger(__name__)
    
    async def generate_improvement_proposals(self, workspace_id: str, 
                                           metrics: PerformanceMetrics) -> List[RefinementProposal]:
        """Generate improvement proposals based on performance metrics"""
        proposals = []
        
        try:
            # Analyze metrics and generate targeted proposals
            if metrics.error_frequency > 0.1:  # More than 10% error rate
                proposals.append(self._create_error_reduction_proposal(metrics))
            
            if metrics.average_user_rating < 3.5:  # Below average rating
                proposals.append(self._create_quality_improvement_proposal(metrics))
            
            if metrics.task_completion_rate < 0.8:  # Less than 80% completion
                proposals.append(self._create_completion_improvement_proposal(metrics))
            
            if metrics.improvement_trend < -0.5:  # Declining performance
                proposals.append(self._create_trend_reversal_proposal(metrics))
            
            # Store proposals in ConPort
            for proposal in proposals:
                await self._store_proposal(workspace_id, proposal)
            
            return proposals
            
        except Exception as e:
            self.logger.error(f"Failed to generate improvement proposals: {e}")
            return []
    
    def _create_error_reduction_proposal(self, metrics: PerformanceMetrics) -> RefinementProposal:
        """Create proposal to reduce error frequency"""
        proposal_id = f"PROP-ERR-{metrics.agent_slug}-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        return RefinementProposal(
            proposal_id=proposal_id,
            timestamp_proposed=datetime.now(),
            source_analysis_ids=[f"PERF-ANALYSIS-{metrics.agent_slug}"],
            target_component_type="rule",
            target_component_identifier=f"{metrics.agent_slug}-error-handling",
            problem_summary=f"High error frequency ({metrics.error_frequency:.1%}) for {metrics.agent_slug}",
            proposed_change_description="Add enhanced error handling and validation rules",
            expected_impact_benefit="Reduce error rate by 50% and improve user experience",
            priority="high",
            status="pending_review"
        )
    
    def _create_quality_improvement_proposal(self, metrics: PerformanceMetrics) -> RefinementProposal:
        """Create proposal to improve response quality"""
        proposal_id = f"PROP-QUAL-{metrics.agent_slug}-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        return RefinementProposal(
            proposal_id=proposal_id,
            timestamp_proposed=datetime.now(),
            source_analysis_ids=[f"PERF-ANALYSIS-{metrics.agent_slug}"],
            target_component_type="prompt",
            target_component_identifier=f"{metrics.agent_slug}-main-prompt",
            problem_summary=f"Low user satisfaction rating ({metrics.average_user_rating:.1f}/5) for {metrics.agent_slug}",
            proposed_change_description="Refine prompts to improve response clarity and helpfulness",
            expected_impact_benefit="Increase average rating to 4.0+ and improve user satisfaction",
            priority="medium",
            status="pending_review"
        )
    
    def _create_completion_improvement_proposal(self, metrics: PerformanceMetrics) -> RefinementProposal:
        """Create proposal to improve task completion rate"""
        proposal_id = f"PROP-COMP-{metrics.agent_slug}-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        return RefinementProposal(
            proposal_id=proposal_id,
            timestamp_proposed=datetime.now(),
            source_analysis_ids=[f"PERF-ANALYSIS-{metrics.agent_slug}"],
            target_component_type="KB",
            target_component_identifier=f"{metrics.agent_slug}-task-procedures",
            problem_summary=f"Low task completion rate ({metrics.task_completion_rate:.1%}) for {metrics.agent_slug}",
            proposed_change_description="Add detailed task completion procedures and checkpoints",
            expected_impact_benefit="Increase completion rate to 95%+ and reduce incomplete tasks",
            priority="high",
            status="pending_review"
        )
    
    def _create_trend_reversal_proposal(self, metrics: PerformanceMetrics) -> RefinementProposal:
        """Create proposal to reverse declining performance trend"""
        proposal_id = f"PROP-TREND-{metrics.agent_slug}-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        return RefinementProposal(
            proposal_id=proposal_id,
            timestamp_proposed=datetime.now(),
            source_analysis_ids=[f"PERF-ANALYSIS-{metrics.agent_slug}"],
            target_component_type="rule",
            target_component_identifier=f"{metrics.agent_slug}-performance-monitoring",
            problem_summary=f"Declining performance trend ({metrics.improvement_trend:.2f}) for {metrics.agent_slug}",
            proposed_change_description="Implement performance monitoring and adaptive behavior rules",
            expected_impact_benefit="Reverse declining trend and establish positive improvement trajectory",
            priority="critical",
            status="pending_review"
        )
    
    async def _store_proposal(self, workspace_id: str, proposal: RefinementProposal):
        """Store improvement proposal in ConPort"""
        try:
            proposal_data = asdict(proposal)
            proposal_data['timestamp_proposed'] = proposal.timestamp_proposed.isoformat()
            
            await self.conport.log_custom_data(
                workspace_id=workspace_id,
                category="AgentRefinementProposal",
                key=proposal.proposal_id,
                value=proposal_data
            )
        except Exception as e:
            self.logger.error(f"Failed to store proposal {proposal.proposal_id}: {e}")

class ContinuousLearningSystem:
    """Main orchestrator for continuous learning and self-optimization"""
    
    def __init__(self, conport_client):
        self.conport = conport_client
        self.feedback_collector = FeedbackCollector(conport_client)
        self.performance_analyzer = PerformanceAnalyzer(conport_client)
        self.improvement_strategist = ImprovementStrategist(conport_client)
        self.logger = logging.getLogger(__name__)
    
    async def run_learning_cycle(self, workspace_id: str, target_agents: List[str] = None) -> Dict[str, Any]:
        """Execute a complete learning cycle for specified agents"""
        results = {
            'cycle_timestamp': datetime.now().isoformat(),
            'agents_analyzed': [],
            'proposals_generated': [],
            'errors': []
        }
        
        try:
            # Default to analyzing all known agents if none specified
            if not target_agents:
                target_agents = ['roo-commander', 'prime-coordinator', 'core-architect']
            
            for agent_slug in target_agents:
                try:
                    self.logger.info(f"Analyzing performance for {agent_slug}")
                    
                    # Analyze agent performance
                    metrics = await self.performance_analyzer.analyze_agent_performance(
                        workspace_id, agent_slug
                    )
                    
                    results['agents_analyzed'].append({
                        'agent': agent_slug,
                        'metrics': asdict(metrics)
                    })
                    
                    # Generate improvement proposals if needed
                    proposals = await self.improvement_strategist.generate_improvement_proposals(
                        workspace_id, metrics
                    )
                    
                    for proposal in proposals:
                        results['proposals_generated'].append(asdict(proposal))
                    
                    self.logger.info(f"Generated {len(proposals)} proposals for {agent_slug}")
                    
                except Exception as e:
                    error_msg = f"Failed to analyze {agent_slug}: {e}"
                    self.logger.error(error_msg)
                    results['errors'].append(error_msg)
            
            # Log learning cycle completion
            await self._log_learning_cycle(workspace_id, results)
            
            return results
            
        except Exception as e:
            self.logger.error(f"Learning cycle failed: {e}")
            results['errors'].append(str(e))
            return results
    
    async def _log_learning_cycle(self, workspace_id: str, results: Dict[str, Any]):
        """Log learning cycle results to ConPort"""
        try:
            cycle_id = f"LEARNING-CYCLE-{datetime.now().strftime('%Y%m%d%H%M%S')}"
            
            await self.conport.log_custom_data(
                workspace_id=workspace_id,
                category="ContinuousLearningCycle",
                key=cycle_id,
                value=results
            )
        except Exception as e:
            self.logger.error(f"Failed to log learning cycle: {e}")

# Integration point for Roo Commander
async def integrate_continuous_learning(workspace_id: str, conport_client) -> Dict[str, Any]:
    """Integration point for continuous learning in Roo Commander"""
    learning_system = ContinuousLearningSystem(conport_client)
    
    # Run learning cycle for key agents
    results = await learning_system.run_learning_cycle(
        workspace_id, 
        target_agents=['roo-commander', 'prime-coordinator', 'core-architect']
    )
    
    return results
