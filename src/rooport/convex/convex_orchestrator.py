#!/usr/bin/env python3
"""
CONVEX (ConPort + Vertex AI unified system) Orchestrator
Implements intelligent dual-brain architecture for ROOPORT
"""

import asyncio
import logging
import re
from datetime import datetime
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from enum import Enum

class QueryIntent(Enum):
    """Types of query intents for routing decisions"""
    PROJECT_SPECIFIC = "project_specific"  # ConPort primary
    RESEARCH_NEEDED = "research_needed"    # Vertex AI primary
    HYBRID_ANALYSIS = "hybrid_analysis"    # Both systems
    DECISION_SUPPORT = "decision_support"  # Both with feedback loop
    LEARNING_UPDATE = "learning_update"    # Results feed back to ConPort

class ConfidenceLevel(Enum):
    """Confidence levels for routing decisions"""
    HIGH = "high"
    MEDIUM = "medium" 
    LOW = "low"
    INSUFFICIENT = "insufficient"

@dataclass
class QueryAnalysis:
    """Result of query intent analysis"""
    intent: QueryIntent
    confidence: ConfidenceLevel
    conport_relevance: float  # 0.0 to 1.0
    vertex_relevance: float   # 0.0 to 1.0
    keywords: List[str]
    reasoning: str

@dataclass
class ConvexResponse:
    """Unified response from CONVEX system"""
    user_query: str
    primary_response: str
    conport_insights: Dict[str, Any]
    vertex_insights: Dict[str, Any]
    routing_decision: str
    confidence_score: float
    sources_used: List[str]
    execution_time: float
    feedback_applied: bool
    next_actions: List[str]

class ConvexOrchestrator:
    """Master orchestrator for ConPort + Vertex AI unified system"""
    
    def __init__(self, conport_client, vertex_ai_client=None):
        self.conport = conport_client
        self.vertex_ai = vertex_ai_client
        self.logger = logging.getLogger(__name__)
        
        # Performance tracking
        self.routing_metrics = []
        self.feedback_loops = []
        
        # Query analysis patterns
        self.project_patterns = [
            r'\b(our project|this codebase|current implementation|existing system)\b',
            r'\b(previous decision|past choice|earlier implementation)\b',
            r'\b(project history|development timeline|our approach)\b',
            r'\b(team decision|architecture choice|design pattern)\b',
            r'\b(ConPort|context|memory|decision record)\b'
        ]
        
        self.research_patterns = [
            r'\b(best practice|industry standard|latest trend)\b',
            r'\b(how to|what is|explain|compare|alternatives)\b',
            r'\b(benchmark|performance comparison|security analysis)\b',
            r'\b(external|third-party|library|framework)\b',
            r'\b(research|investigate|analyze|evaluate)\b'
        ]
        
        self.hybrid_patterns = [
            r'\b(should we|recommend|suggest|advise)\b',
            r'\b(decision|choice|selection|evaluation)\b',
            r'\b(architecture|design|strategy|approach)\b',
            r'\b(implement|adopt|integrate|migrate)\b'
        ]

    async def process_convex_query(self, user_query: str, workspace_id: str, 
                                 context: Dict[str, Any] = None) -> ConvexResponse:
        """Process query through CONVEX dual-brain system"""
        start_time = datetime.now()
        
        try:
            self.logger.info(f"Processing CONVEX query: {user_query}")
            
            # Phase 1: Analyze query intent and determine routing
            query_analysis = await self._analyze_query_intent(user_query, workspace_id)
            self.logger.info(f"Query analysis: {query_analysis.intent.value} (confidence: {query_analysis.confidence.value})")
            
            # Phase 2: Execute based on routing decision
            if query_analysis.intent == QueryIntent.PROJECT_SPECIFIC:
                response = await self._execute_conport_primary(user_query, workspace_id, query_analysis)
            elif query_analysis.intent == QueryIntent.RESEARCH_NEEDED:
                response = await self._execute_vertex_primary(user_query, workspace_id, query_analysis)
            elif query_analysis.intent == QueryIntent.HYBRID_ANALYSIS:
                response = await self._execute_hybrid_parallel(user_query, workspace_id, query_analysis)
            elif query_analysis.intent == QueryIntent.DECISION_SUPPORT:
                response = await self._execute_decision_support(user_query, workspace_id, query_analysis)
            else:  # LEARNING_UPDATE
                response = await self._execute_learning_update(user_query, workspace_id, query_analysis)
            
            # Phase 3: Apply feedback loops
            feedback_applied = await self._apply_feedback_loops(response, workspace_id)
            response.feedback_applied = feedback_applied
            
            # Phase 4: Log execution metrics
            execution_time = (datetime.now() - start_time).total_seconds()
            response.execution_time = execution_time
            await self._log_convex_execution(workspace_id, user_query, query_analysis, response)
            
            return response
            
        except Exception as e:
            self.logger.error(f"CONVEX processing failed: {e}")
            return self._error_response(user_query, str(e))

    async def _analyze_query_intent(self, query: str, workspace_id: str) -> QueryAnalysis:
        """Analyze query to determine intent and routing strategy"""
        query_lower = query.lower()
        
        # Calculate pattern matches
        project_score = self._calculate_pattern_score(query_lower, self.project_patterns)
        research_score = self._calculate_pattern_score(query_lower, self.research_patterns)
        hybrid_score = self._calculate_pattern_score(query_lower, self.hybrid_patterns)
        
        # Check ConPort relevance by looking for existing context
        conport_relevance = await self._assess_conport_relevance(query, workspace_id)
        
        # Determine intent based on scores
        scores = {
            QueryIntent.PROJECT_SPECIFIC: project_score + (conport_relevance * 0.3),
            QueryIntent.RESEARCH_NEEDED: research_score,
            QueryIntent.HYBRID_ANALYSIS: hybrid_score,
            QueryIntent.DECISION_SUPPORT: (hybrid_score + project_score) * 0.7,
            QueryIntent.LEARNING_UPDATE: 0.1  # Default low
        }
        
        # Special case: if asking about implementing/adopting something external
        if any(word in query_lower for word in ['implement', 'adopt', 'integrate', 'should we use']):
            scores[QueryIntent.DECISION_SUPPORT] += 0.4
        
        # Determine primary intent
        primary_intent = max(scores, key=scores.get)
        max_score = scores[primary_intent]
        
        # Determine confidence
        if max_score > 0.7:
            confidence = ConfidenceLevel.HIGH
        elif max_score > 0.4:
            confidence = ConfidenceLevel.MEDIUM
        elif max_score > 0.2:
            confidence = ConfidenceLevel.LOW
        else:
            confidence = ConfidenceLevel.INSUFFICIENT
            primary_intent = QueryIntent.HYBRID_ANALYSIS  # Default to hybrid for low confidence
        
        # Calculate vertex relevance
        vertex_relevance = research_score + (0.3 if any(word in query_lower for word in 
                                           ['best practice', 'how to', 'what is', 'compare']) else 0)
        
        # Extract keywords
        keywords = self._extract_keywords(query)
        
        reasoning = f"Project patterns: {project_score:.2f}, Research patterns: {research_score:.2f}, " \
                   f"Hybrid patterns: {hybrid_score:.2f}, ConPort relevance: {conport_relevance:.2f}"
        
        return QueryAnalysis(
            intent=primary_intent,
            confidence=confidence,
            conport_relevance=conport_relevance,
            vertex_relevance=vertex_relevance,
            keywords=keywords,
            reasoning=reasoning
        )

    def _calculate_pattern_score(self, query: str, patterns: List[str]) -> float:
        """Calculate pattern match score for query"""
        matches = 0
        total_patterns = len(patterns)
        
        for pattern in patterns:
            if re.search(pattern, query, re.IGNORECASE):
                matches += 1
        
        return matches / total_patterns if total_patterns > 0 else 0.0

    async def _assess_conport_relevance(self, query: str, workspace_id: str) -> float:
        """Assess how relevant ConPort data is to the query"""
        try:
            # Quick search for relevant ConPort content
            keywords = self._extract_keywords(query)
            relevance_score = 0.0
            
            # Search decisions
            if keywords:
                search_query = ' '.join(keywords[:3])  # Use top 3 keywords
                decisions = await self.conport.search_decisions_fts(
                    workspace_id=workspace_id,
                    query_term=search_query,
                    limit=3
                )
                if decisions and len(decisions) > 0:
                    relevance_score += 0.4
            
            # Check for project context
            product_context = await self.conport.get_product_context(workspace_id=workspace_id)
            if product_context and any(keyword in str(product_context).lower() 
                                     for keyword in keywords):
                relevance_score += 0.3
            
            # Check for active context
            active_context = await self.conport.get_active_context(workspace_id=workspace_id)
            if active_context and any(keyword in str(active_context).lower() 
                                    for keyword in keywords):
                relevance_score += 0.3
            
            return min(relevance_score, 1.0)
            
        except Exception as e:
            self.logger.warning(f"ConPort relevance assessment failed: {e}")
            return 0.2  # Default low relevance

    def _extract_keywords(self, query: str) -> List[str]:
        """Extract relevant keywords from query"""
        # Remove common words and extract meaningful terms
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 
                     'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
                     'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could',
                     'should', 'may', 'might', 'can', 'what', 'how', 'when', 'where', 'why'}
        
        words = re.findall(r'\b\w+\b', query.lower())
        keywords = [word for word in words if len(word) > 2 and word not in stop_words]
        
        return keywords[:10]  # Limit to top 10 keywords
    async def _execute_conport_primary(self, query: str, workspace_id: str,
                                         analysis: QueryAnalysis) -> ConvexResponse:
        """Execute with ConPort as primary source"""
        try:
            # Search ConPort for relevant information
            conport_results = await self._comprehensive_conport_search(query, workspace_id, analysis.keywords)
            
            # Generate response based on ConPort data
            primary_response = self._synthesize_conport_response(query, conport_results)
            
            # Optionally enhance with minimal Vertex AI context if available
            vertex_insights = {}
            if self.vertex_ai and analysis.vertex_relevance > 0.3:
                vertex_insights = await self._get_minimal_vertex_context(query, analysis.keywords)
            
            return ConvexResponse(
                user_query=query,
                primary_response=primary_response,
                conport_insights=conport_results,
                vertex_insights=vertex_insights,
                routing_decision="ConPort Primary",
                confidence_score=0.8 if analysis.confidence == ConfidenceLevel.HIGH else 0.6,
                sources_used=self._extract_conport_sources(conport_results),
                execution_time=0.0,  # Will be set later
                feedback_applied=False,
                next_actions=self._generate_conport_actions(conport_results)
            )
            
        except Exception as e:
            self.logger.error(f"ConPort primary execution failed: {e}")
            return self._error_response(query, str(e))

    async def _execute_vertex_primary(self, query: str, workspace_id: str,
                                     analysis: QueryAnalysis) -> ConvexResponse:
        """Execute with Vertex AI as primary source"""
        try:
            if not self.vertex_ai:
                return self._error_response(query, "Vertex AI not available for research query")
            
            # Use Vertex AI for research
            vertex_results = await self._comprehensive_vertex_research(query, analysis.keywords)
            
            # Generate response based on Vertex AI research
            primary_response = self._synthesize_vertex_response(query, vertex_results)
            
            # Get minimal ConPort context for grounding
            conport_context = await self._get_minimal_conport_context(query, workspace_id, analysis.keywords)
            
            return ConvexResponse(
                user_query=query,
                primary_response=primary_response,
                conport_insights=conport_context,
                vertex_insights=vertex_results,
                routing_decision="Vertex AI Primary",
                confidence_score=0.7 if analysis.confidence == ConfidenceLevel.HIGH else 0.5,
                sources_used=self._extract_vertex_sources(vertex_results),
                execution_time=0.0,
                feedback_applied=False,
                next_actions=self._generate_vertex_actions(vertex_results)
            )
            
        except Exception as e:
            self.logger.error(f"Vertex AI primary execution failed: {e}")
            return self._error_response(query, str(e))

    async def _execute_hybrid_parallel(self, query: str, workspace_id: str,
                                     analysis: QueryAnalysis) -> ConvexResponse:
        """Execute with both systems in parallel"""
        try:
            # Execute both systems in parallel
            conport_task = self._comprehensive_conport_search(query, workspace_id, analysis.keywords)
            vertex_task = self._comprehensive_vertex_research(query, analysis.keywords) if self.vertex_ai else None
            
            # Wait for both to complete
            if vertex_task:
                conport_results, vertex_results = await asyncio.gather(
                    conport_task, vertex_task, return_exceptions=True
                )
            else:
                conport_results = await conport_task
                vertex_results = {}
            
            # Synthesize hybrid response
            primary_response = self._synthesize_hybrid_response(query, conport_results, vertex_results)
            
            return ConvexResponse(
                user_query=query,
                primary_response=primary_response,
                conport_insights=conport_results if not isinstance(conport_results, Exception) else {},
                vertex_insights=vertex_results if not isinstance(vertex_results, Exception) else {},
                routing_decision="Hybrid Parallel",
                confidence_score=0.8,
                sources_used=self._extract_hybrid_sources(conport_results, vertex_results),
                execution_time=0.0,
                feedback_applied=False,
                next_actions=self._generate_hybrid_actions(conport_results, vertex_results)
            )
            
        except Exception as e:
            self.logger.error(f"Hybrid parallel execution failed: {e}")
            return self._error_response(query, str(e))

    async def _execute_decision_support(self, query: str, workspace_id: str,
                                      analysis: QueryAnalysis) -> ConvexResponse:
        """Execute decision support workflow with feedback loops"""
        try:
            # Phase 1: Gather ConPort context
            conport_context = await self._comprehensive_conport_search(query, workspace_id, analysis.keywords)
            
            # Phase 2: Research external options if Vertex AI available
            vertex_research = {}
            if self.vertex_ai:
                vertex_research = await self._comprehensive_vertex_research(query, analysis.keywords)
            
            # Phase 3: Generate decision framework
            decision_framework = self._generate_decision_framework(query, conport_context, vertex_research)
            
            # Phase 4: Synthesize recommendation
            primary_response = self._synthesize_decision_response(query, decision_framework)
            
            return ConvexResponse(
                user_query=query,
                primary_response=primary_response,
                conport_insights=conport_context,
                vertex_insights=vertex_research,
                routing_decision="Decision Support",
                confidence_score=0.75,
                sources_used=self._extract_hybrid_sources(conport_context, vertex_research),
                execution_time=0.0,
                feedback_applied=False,
                next_actions=self._generate_decision_actions(decision_framework)
            )
            
        except Exception as e:
            self.logger.error(f"Decision support execution failed: {e}")
            return self._error_response(query, str(e))

    async def _execute_learning_update(self, query: str, workspace_id: str,
                                     analysis: QueryAnalysis) -> ConvexResponse:
        """Execute learning update workflow"""
        try:
            # This would typically be used for updating ConPort with external research
            # For now, implement as hybrid with emphasis on feedback
            
            response = await self._execute_hybrid_parallel(query, workspace_id, analysis)
            response.routing_decision = "Learning Update"
            
            # Mark for feedback application
            response.feedback_applied = True
            
            return response
            
        except Exception as e:
            self.logger.error(f"Learning update execution failed: {e}")
            return self._error_response(query, str(e))

    async def _comprehensive_conport_search(self, query: str, workspace_id: str, 
                                          keywords: List[str]) -> Dict[str, Any]:
        """Comprehensive search of ConPort data"""
        results = {}
        
        try:
            # Search decisions
            if keywords:
                search_term = ' '.join(keywords[:3])
                decisions = await self.conport.search_decisions_fts(
                    workspace_id=workspace_id,
                    query_term=search_term,
                    limit=5
                )
                results['decisions'] = decisions or []
            
            # Get product context
            product_context = await self.conport.get_product_context(workspace_id=workspace_id)
            results['product_context'] = product_context or {}
            
            # Get active context
            active_context = await self.conport.get_active_context(workspace_id=workspace_id)
            results['active_context'] = active_context or {}
            
            # Search custom data
            if keywords:
                custom_data = await self.conport.search_custom_data_value_fts(
                    workspace_id=workspace_id,
                    query_term=search_term,
                    limit=5
                )
                results['custom_data'] = custom_data or []
            
            # Get system patterns
            patterns = await self.conport.get_system_patterns(workspace_id=workspace_id)
            results['system_patterns'] = patterns or []
            
        except Exception as e:
            self.logger.error(f"ConPort search failed: {e}")
            results['error'] = str(e)
        
        return results

    async def _comprehensive_vertex_research(self, query: str, keywords: List[str]) -> Dict[str, Any]:
        """Comprehensive research using Vertex AI"""
        if not self.vertex_ai:
            return {}
        
        results = {}
        
        try:
            # Use answer_query_websearch for research
            research_response = await self.vertex_ai.answer_query_websearch(
                query=query
            )
            results['research_response'] = research_response
            
            # If keywords suggest technical topics, get documentation snippets
            if any(keyword in ['implement', 'how', 'best', 'practice'] for keyword in keywords):
                if len(keywords) > 0:
                    topic = keywords[0]  # Use first keyword as topic
                    doc_snippets = await self.vertex_ai.get_doc_snippets(
                        topic=topic,
                        query=query
                    )
                    results['doc_snippets'] = doc_snippets
            
        except Exception as e:
            self.logger.error(f"Vertex AI research failed: {e}")
            results['error'] = str(e)
        
        return results

    async def _get_minimal_vertex_context(self, query: str, keywords: List[str]) -> Dict[str, Any]:
        """Get minimal Vertex AI context for ConPort-primary queries"""
        if not self.vertex_ai or not keywords:
            return {}
        
        try:
            # Quick research for context
            topic = keywords[0] if keywords else "general"
            context = await self.vertex_ai.answer_query_direct(
                query=f"Brief context about {topic} for {query}"
            )
            return {'context': context}
        except Exception as e:
            self.logger.warning(f"Minimal Vertex AI context failed: {e}")
            return {}

    async def _get_minimal_conport_context(self, query: str, workspace_id: str, 
                                         keywords: List[str]) -> Dict[str, Any]:
        """Get minimal ConPort context for Vertex-primary queries"""
        try:
            # Get just product context for grounding
            product_context = await self.conport.get_product_context(workspace_id=workspace_id)
            return {'product_context': product_context or {}}
        except Exception as e:
            self.logger.warning(f"Minimal ConPort context failed: {e}")
            return {}
    def _synthesize_conport_response(self, query: str, conport_results: Dict[str, Any]) -> str:
        """Synthesize response from ConPort data"""
        if conport_results.get('error'):
            return f"I encountered an issue accessing project memory: {conport_results['error']}"
        
        response_parts = []
        
        # Check product context
        product_context = conport_results.get('product_context', {})
        if product_context:
            response_parts.append("Based on our project context:")
        
        # Check decisions
        decisions = conport_results.get('decisions', [])
        if decisions:
            response_parts.append(f"Found {len(decisions)} relevant project decisions:")
            for i, decision in enumerate(decisions[:3], 1):
                if isinstance(decision, dict):
                    summary = decision.get('summary', 'Decision')
                    response_parts.append(f"{i}. {summary}")
        
        # Check active context
        active_context = conport_results.get('active_context', {})
        if active_context:
            response_parts.append("Current project focus aligns with your query.")
        
        if not response_parts:
            response_parts.append("I found limited project-specific information for your query.")
        
        return "\n".join(response_parts)

    def _synthesize_vertex_response(self, query: str, vertex_results: Dict[str, Any]) -> str:
        """Synthesize response from Vertex AI research"""
        if vertex_results.get('error'):
            return f"I encountered an issue with external research: {vertex_results['error']}"
        
        response_parts = []
        
        # Use research response
        research = vertex_results.get('research_response')
        if research:
            response_parts.append("Based on external research:")
            response_parts.append(str(research))
        
        # Use doc snippets
        snippets = vertex_results.get('doc_snippets')
        if snippets:
            response_parts.append("\nRelevant documentation:")
            response_parts.append(str(snippets))
        
        if not response_parts:
            response_parts.append("External research provided limited insights for your query.")
        
        return "\n".join(response_parts)

    def _synthesize_hybrid_response(self, query: str, conport_results: Dict[str, Any], 
                                  vertex_results: Dict[str, Any]) -> str:
        """Synthesize response from both ConPort and Vertex AI"""
        response_parts = []
        
        # Start with ConPort context
        if conport_results and not isinstance(conport_results, Exception):
            decisions = conport_results.get('decisions', [])
            if decisions:
                response_parts.append("From our project history:")
                for decision in decisions[:2]:
                    if isinstance(decision, dict):
                        summary = decision.get('summary', 'Decision')
                        response_parts.append(f"• {summary}")
        
        # Add Vertex AI research
        if vertex_results and not isinstance(vertex_results, Exception):
            research = vertex_results.get('research_response')
            if research:
                response_parts.append("\nExternal research insights:")
                response_parts.append(str(research)[:500] + "..." if len(str(research)) > 500 else str(research))
        
        if not response_parts:
            response_parts.append("I've analyzed both project context and external sources for your query.")
        
        return "\n".join(response_parts)

    def _generate_decision_framework(self, query: str, conport_context: Dict[str, Any],
                                   vertex_research: Dict[str, Any]) -> Dict[str, Any]:
        """Generate decision framework from both sources"""
        framework = {
            'query': query,
            'project_factors': [],
            'external_factors': [],
            'recommendations': []
        }
        
        # Extract project factors from ConPort
        decisions = conport_context.get('decisions', [])
        for decision in decisions[:3]:
            if isinstance(decision, dict):
                framework['project_factors'].append(decision.get('summary', 'Previous decision'))
        
        # Extract external factors from Vertex AI
        if vertex_research.get('research_response'):
            framework['external_factors'].append("Industry best practices")
        
        if vertex_research.get('doc_snippets'):
            framework['external_factors'].append("Technical documentation")
        
        return framework

    def _synthesize_decision_response(self, query: str, framework: Dict[str, Any]) -> str:
        """Synthesize decision support response"""
        response_parts = [f"Decision analysis for: {query}"]
        
        if framework['project_factors']:
            response_parts.append("\nProject considerations:")
            for factor in framework['project_factors']:
                response_parts.append(f"• {factor}")
        
        if framework['external_factors']:
            response_parts.append("\nExternal considerations:")
            for factor in framework['external_factors']:
                response_parts.append(f"• {factor}")
        
        response_parts.append("\nRecommendation: Consider both project history and industry practices when making this decision.")
        
        return "\n".join(response_parts)

    def _extract_conport_sources(self, conport_results: Dict[str, Any]) -> List[str]:
        """Extract source information from ConPort results"""
        sources = []
        
        if conport_results.get('decisions'):
            sources.append(f"Project decisions ({len(conport_results['decisions'])})")
        
        if conport_results.get('product_context'):
            sources.append("Product context")
        
        if conport_results.get('active_context'):
            sources.append("Active context")
        
        if conport_results.get('custom_data'):
            sources.append(f"Custom data ({len(conport_results['custom_data'])})")
        
        return sources

    def _extract_vertex_sources(self, vertex_results: Dict[str, Any]) -> List[str]:
        """Extract source information from Vertex AI results"""
        sources = []
        
        if vertex_results.get('research_response'):
            sources.append("Web research")
        
        if vertex_results.get('doc_snippets'):
            sources.append("Technical documentation")
        
        return sources

    def _extract_hybrid_sources(self, conport_results: Dict[str, Any], 
                               vertex_results: Dict[str, Any]) -> List[str]:
        """Extract source information from both systems"""
        sources = []
        if not isinstance(conport_results, Exception):
            sources.extend(self._extract_conport_sources(conport_results))
        if not isinstance(vertex_results, Exception):
            sources.extend(self._extract_vertex_sources(vertex_results))
        return sources

    def _generate_conport_actions(self, conport_results: Dict[str, Any]) -> List[str]:
        """Generate next actions based on ConPort data"""
        actions = ["Review project context", "Check related decisions"]
        
        if conport_results.get('decisions'):
            actions.append("Analyze decision patterns")
        
        return actions

    def _generate_vertex_actions(self, vertex_results: Dict[str, Any]) -> List[str]:
        """Generate next actions based on Vertex AI research"""
        actions = ["Review research findings", "Validate against project needs"]
        
        if vertex_results.get('doc_snippets'):
            actions.append("Study technical documentation")
        
        return actions

    def _generate_hybrid_actions(self, conport_results: Dict[str, Any], 
                                vertex_results: Dict[str, Any]) -> List[str]:
        """Generate next actions for hybrid responses"""
        actions = []
        if not isinstance(conport_results, Exception):
            actions.extend(self._generate_conport_actions(conport_results)[:2])
        if not isinstance(vertex_results, Exception):
            actions.extend(self._generate_vertex_actions(vertex_results)[:2])
        actions.append("Synthesize project and external insights")
        return actions

    def _generate_decision_actions(self, framework: Dict[str, Any]) -> List[str]:
        """Generate next actions for decision support"""
        return [
            "Evaluate project constraints",
            "Research implementation options", 
            "Consult with team",
            "Document decision rationale",
            "Plan implementation approach"
        ]

    async def _apply_feedback_loops(self, response: ConvexResponse, workspace_id: str) -> bool:
        """Apply feedback loops to update ConPort with insights"""
        try:
            # If Vertex AI provided valuable insights, consider storing them
            if (response.vertex_insights and 
                response.routing_decision in ["Vertex AI Primary", "Decision Support"]):
                
                # Store valuable research findings
                research_response = response.vertex_insights.get('research_response')
                if research_response and len(str(research_response)) > 100:
                    
                    # Create a custom data entry for the research
                    research_id = f"RESEARCH-{datetime.now().strftime('%Y%m%d%H%M%S')}"
                    
                    await self.conport.log_custom_data(
                        workspace_id=workspace_id,
                        category="VertexResearch",
                        key=research_id,
                        value={
                            "query": response.user_query,
                            "research_findings": str(research_response)[:1000],  # Truncate if too long
                            "timestamp": datetime.now().isoformat(),
                            "routing_decision": response.routing_decision
                        }
                    )
                    
                    self.logger.info(f"Applied feedback loop: stored research findings as {research_id}")
                    return True
                    
        except Exception as e:
            self.logger.error(f"Feedback loop application failed: {e}")
        
        return False

    async def _log_convex_execution(self, workspace_id: str, query: str, 
                                  analysis: QueryAnalysis, response: ConvexResponse):
        """Log CONVEX execution to ConPort"""
        try:
            execution_id = f"CONVEX-{datetime.now().strftime('%Y%m%d%H%M%S')}"
            
            await self.conport.log_custom_data(
                workspace_id=workspace_id,
                category="ConvexExecution",
                key=execution_id,
                value={
                    "query": query,
                    "intent": analysis.intent.value,
                    "confidence": analysis.confidence.value,
                    "routing_decision": response.routing_decision,
                    "confidence_score": response.confidence_score,
                    "execution_time": response.execution_time,
                    "sources_used": response.sources_used,
                    "feedback_applied": response.feedback_applied,
                    "timestamp": datetime.now().isoformat()
                }
            )
            
            # Update routing metrics
            self.routing_metrics.append({
                'timestamp': datetime.now(),
                'intent': analysis.intent.value,
                'confidence': analysis.confidence.value,
                'execution_time': response.execution_time,
                'success': True
            })
            
            # Keep only recent metrics
            if len(self.routing_metrics) > 100:
                self.routing_metrics = self.routing_metrics[-100:]
                
        except Exception as e:
            self.logger.error(f"Failed to log CONVEX execution: {e}")

    def _error_response(self, user_query: str, error_msg: str) -> ConvexResponse:
        """Return error response"""
        return ConvexResponse(
            user_query=user_query,
            primary_response=f"I encountered an issue processing your request: {error_msg}",
            conport_insights={},
            vertex_insights={},
            routing_decision="Error",
            confidence_score=0.0,
            sources_used=[],
            execution_time=0.0,
            feedback_applied=False,
            next_actions=["Retry request", "Check system status"]
        )

    async def get_routing_analytics(self, workspace_id: str) -> Dict[str, Any]:
        """Get analytics on routing decisions and performance"""
        try:
            if not self.routing_metrics:
                return {'status': 'no_data'}
            
            recent_metrics = self.routing_metrics[-50:]  # Last 50 executions
            
            # Intent distribution
            intent_counts = {}
            for metric in recent_metrics:
                intent = metric['intent']
                intent_counts[intent] = intent_counts.get(intent, 0) + 1
            
            # Average execution times by intent
            intent_times = {}
            for intent in intent_counts:
                times = [m['execution_time'] for m in recent_metrics if m['intent'] == intent]
                intent_times[intent] = sum(times) / len(times) if times else 0
            
            # Success rate
            success_rate = sum(1 for m in recent_metrics if m['success']) / len(recent_metrics)
            
            return {
                'status': 'analyzed',
                'sample_size': len(recent_metrics),
                'intent_distribution': intent_counts,
                'avg_execution_times': intent_times,
                'success_rate': success_rate,
                'total_executions': len(self.routing_metrics)
            }
            
        except Exception as e:
            self.logger.error(f"Routing analytics failed: {e}")
            return {'status': 'error', 'error': str(e)}

# Main integration functions
async def integrate_convex_system(workspace_id: str, user_query: str, 
                                conport_client, vertex_ai_client=None) -> ConvexResponse:
    """Main integration point for the CONVEX system"""
    orchestrator = ConvexOrchestrator(conport_client, vertex_ai_client)
    response = await orchestrator.process_convex_query(user_query, workspace_id)
    return response

async def get_convex_analytics(workspace_id: str, conport_client) -> Dict[str, Any]:
    """Get CONVEX system analytics"""
    orchestrator = ConvexOrchestrator(conport_client)
    return await orchestrator.get_routing_analytics(workspace_id)