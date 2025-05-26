"""
Information Synthesizer - Advanced synthesis and validation of retrieved information
Elite Field Service SaaS Platform

Provides intelligent synthesis capabilities:
- Multi-source information fusion
- Fact validation and consistency checking
- Contextual answer generation
- Citation and source attribution
- Confidence assessment
"""

import asyncio
from typing import Dict, List, Any, Optional, Tuple, Set
from datetime import datetime
from enum import Enum
import logging
import json
import re

logger = logging.getLogger(__name__)


class SynthesisStrategy(Enum):
    """Strategies for information synthesis"""
    EXTRACTIVE = "extractive"  # Extract key facts and combine
    ABSTRACTIVE = "abstractive"  # Generate new summary text
    HYBRID = "hybrid"  # Combine extractive and abstractive
    STRUCTURED = "structured"  # Create structured responses
    NARRATIVE = "narrative"  # Create flowing narrative


class FactValidationLevel(Enum):
    """Levels of fact validation"""
    NONE = "none"
    BASIC = "basic"  # Basic consistency checks
    MODERATE = "moderate"  # Cross-reference validation
    STRICT = "strict"  # Comprehensive validation
    EXPERT = "expert"  # Domain-specific validation


class ConfidenceLevel(Enum):
    """Confidence levels for synthesized information"""
    VERY_LOW = "very_low"  # < 0.3
    LOW = "low"  # 0.3 - 0.5
    MODERATE = "moderate"  # 0.5 - 0.7
    HIGH = "high"  # 0.7 - 0.9
    VERY_HIGH = "very_high"  # > 0.9


class InformationSynthesizer:
    """
    Advanced information synthesizer for RAG systems
    
    Capabilities:
    - Multi-source information fusion
    - Intelligent fact extraction and validation
    - Contextual answer generation with citations
    - Confidence assessment and uncertainty handling
    - Domain-specific synthesis patterns
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None, vertex_mcp_client=None):
        """
        Initialize information synthesizer
        
        Args:
            config: Configuration options for synthesis behavior
            vertex_mcp_client: Optional Vertex MCP client for batch code analysis
        """
        self.config = {
            'default_strategy': SynthesisStrategy.HYBRID,
            'validation_level': FactValidationLevel.MODERATE,
            'max_synthesis_length': 2000,
            'min_source_agreement': 0.6,
            'enable_citations': True,
            'citation_style': 'inline',  # 'inline', 'numbered', 'bracketed'
            'fact_checking': True,
            'consistency_threshold': 0.7,
            'confidence_calculation': 'weighted',
            'domain_adaptations': True,
            **(config or {})
        }
        self.vertex_mcp_client = vertex_mcp_client
        
        # Performance and quality metrics
        self.metrics = {
            'total_syntheses': 0,
            'successful_syntheses': 0,
            'avg_synthesis_time': 0.0,
            'avg_confidence_score': 0.0,
            'fact_validation_rate': 0.0,
            'citation_accuracy': 0.0,
            'strategy_usage': {strategy.value: 0 for strategy in SynthesisStrategy}
        }
        
        # Domain-specific patterns and templates
        self.domain_patterns = {
            'technical': {
                'keywords': ['implementation', 'algorithm', 'architecture', 'code', 'system'],
                'template': "Based on the technical documentation, {synthesis}. Implementation details: {details}.",
                'validation_focus': ['accuracy', 'completeness', 'technical_consistency']
            },
            'decision': {
                'keywords': ['decision', 'choice', 'rationale', 'chosen', 'selected'],
                'template': "The decision was {decision} based on {rationale}. Key factors: {factors}.",
                'validation_focus': ['logical_consistency', 'completeness']
            },
            'progress': {
                'keywords': ['progress', 'status', 'completion', 'milestone', 'task'],
                'template': "Current status: {status}. Progress details: {details}. Next steps: {next_steps}.",
                'validation_focus': ['timeline_consistency', 'status_accuracy']
            },
            'general': {
                'keywords': [],
                'template': "{synthesis}",
                'validation_focus': ['basic_consistency', 'source_agreement']
            }
        }
        
        # Fact extraction patterns
        self.fact_patterns = {
            'dates': r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b|\b\d{4}-\d{2}-\d{2}\b',
            'versions': r'v?\d+\.\d+(?:\.\d+)?',
            'technologies': r'\b(?:React|Angular|Vue|Node\.js|Python|Java|TypeScript|JavaScript|PostgreSQL|MySQL|MongoDB)\b',
            'decisions': r'(?:decided|chosen|selected|opted for|went with)\s+([^.]+)',
            'problems': r'(?:issue|problem|bug|error|challenge):\s*([^.]+)',
            'solutions': r'(?:solution|fix|resolution|approach):\s*([^.]+)'
        }
    
    async def synthesize(
        self,
        retrieved_items: List[Dict[str, Any]],
        query: str,
        context: Optional[Dict[str, Any]] = None,
        strategy: Optional[SynthesisStrategy] = None,
        validation_level: Optional[FactValidationLevel] = None
    ) -> Dict[str, Any]:
        """
        Synthesize information from retrieved items into a coherent response
        
        Args:
            retrieved_items: List of items retrieved from various sources
            query: Original user query
            context: Additional context for synthesis
            strategy: Synthesis strategy to use
            validation_level: Level of fact validation to apply
            
        Returns:
            Synthesis result with answer, confidence, citations, and metadata
        """
        start_time = datetime.now()
        
        try:
            if not retrieved_items:
                return self._create_empty_response(query, "No information available")
            
            # Select synthesis strategy
            strategy = strategy or self._select_synthesis_strategy(query, retrieved_items)
            validation_level = validation_level or self.config['validation_level']
            
            # Pre-process retrieved items
            processed_items = await self._preprocess_items(retrieved_items, query)

            # --- Vertex MCP Batch Code Analysis Integration ---
            code_snippets = []
            for item in processed_items:
                # Detect code snippets by type or content (simple heuristic)
                if item.get('type') == 'code':
                    code_snippets.append(item.get('content', ''))
                else:
                    content = item.get('content', '')
                    # Heuristic: treat as code if contains multiple lines and common code symbols
                    if isinstance(content, str) and (
                        ('def ' in content or 'class ' in content or 'function ' in content or 'import ' in content)
                        and len(content.splitlines()) > 2
                    ):
                        code_snippets.append(content)
            code_analysis_results = None
            if code_snippets and self.vertex_mcp_client:
                try:
                    # The actual method name may differ; adapt as needed
                    code_analysis_results = await self.vertex_mcp_client.batch_code_analysis(code_snippets)
                except Exception as e:
                    logger.error(f"Vertex MCP batch code analysis failed: {e}")
                    code_analysis_results = {'error': str(e)}
            # Attach code analysis results to context for downstream use
            if context is not None:
                context['code_analysis'] = code_analysis_results
            else:
                context = {'code_analysis': code_analysis_results}

            # Extract and validate facts
            facts = await self._extract_facts(processed_items, validation_level)
            
            # Detect domain and select appropriate patterns
            domain = self._detect_domain(query, processed_items)
            
            # Perform synthesis based on strategy
            synthesis_result = await self._execute_synthesis_strategy(
                strategy, facts, query, domain, processed_items
            )
            
            # Post-process and validate synthesis
            final_result = await self._post_process_synthesis(
                synthesis_result, facts, processed_items, validation_level
            )
            
            # Calculate confidence and add metadata
            confidence_info = self._calculate_confidence(final_result, facts, processed_items)
            final_result.update(confidence_info)
            
            # Add citations if enabled
            if self.config['enable_citations']:
                final_result['citations'] = self._generate_citations(
                    processed_items, final_result['answer']
                )
            
            # Update metrics
            execution_time = (datetime.now() - start_time).total_seconds()
            self._update_metrics(execution_time, strategy, confidence_info['confidence_score'])
            
            # Attach code analysis results to the final result
            if code_analysis_results is not None:
                final_result['code_analysis'] = code_analysis_results

            return final_result
            
        except Exception as e:
            logger.error(f"Information synthesis failed: {e}")
            execution_time = (datetime.now() - start_time).total_seconds()
            self._update_metrics(execution_time, strategy, 0.0, success=False)
            return self._create_error_response(query, str(e))
    
    async def synthesize_with_validation(
        self,
        retrieved_items: List[Dict[str, Any]],
        query: str,
        external_validator=None,
        **kwargs
    ) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        """
        Synthesize with external validation and detailed validation report
        
        Returns:
            Tuple of (synthesis_result, validation_report)
        """
        # Perform standard synthesis
        synthesis_result = await self.synthesize(retrieved_items, query, **kwargs)
        
        # Perform additional validation
        validation_report = await self._comprehensive_validation(
            synthesis_result, retrieved_items, external_validator
        )
        
        # Update synthesis result with validation insights
        if validation_report['overall_confidence'] < synthesis_result['confidence_score']:
            synthesis_result['confidence_score'] = validation_report['overall_confidence']
            synthesis_result['confidence_level'] = self._score_to_confidence_level(
                validation_report['overall_confidence']
            )
            synthesis_result['validation_warnings'] = validation_report.get('warnings', [])
        
        return synthesis_result, validation_report
    
    def _select_synthesis_strategy(
        self, 
        query: str, 
        retrieved_items: List[Dict[str, Any]]
    ) -> SynthesisStrategy:
        """Select optimal synthesis strategy based on query and available data"""
        query_lower = query.lower()
        
        # Check for specific strategy indicators
        if any(word in query_lower for word in ['list', 'enumerate', 'what are', 'show me']):
            return SynthesisStrategy.STRUCTURED
        
        elif any(word in query_lower for word in ['explain', 'describe', 'how', 'why']):
            return SynthesisStrategy.NARRATIVE
        
        elif len(retrieved_items) > 10:
            # Many sources - use extractive approach
            return SynthesisStrategy.EXTRACTIVE
        
        elif len(retrieved_items) < 3:
            # Few sources - use abstractive approach
            return SynthesisStrategy.ABSTRACTIVE
        
        else:
            # Default to hybrid approach
            return SynthesisStrategy.HYBRID
    
    async def _preprocess_items(
        self, 
        retrieved_items: List[Dict[str, Any]], 
        query: str
    ) -> List[Dict[str, Any]]:
        """Preprocess retrieved items for synthesis"""
        processed_items = []
        
        for item in retrieved_items:
            try:
                processed_item = {
                    'content': self._extract_content_text(item),
                    'source': item.get('source', 'unknown'),
                    'relevance_score': item.get('relevance_score', item.get('similarity_score', 0.5)),
                    'metadata': item.get('metadata', {}),
                    'source_type': item.get('conport_type', item.get('hybrid_source', 'unknown')),
                    'original_item': item
                }
                
                # Add query-specific relevance
                processed_item['query_relevance'] = self._calculate_query_relevance(
                    processed_item['content'], query
                )
                
                processed_items.append(processed_item)
                
            except Exception as e:
                logger.warning(f"Failed to preprocess item: {e}")
                continue
        
        # Sort by relevance
        processed_items.sort(
            key=lambda x: x.get('query_relevance', 0.0), 
            reverse=True
        )
        
        return processed_items
    
    def _extract_content_text(self, item: Dict[str, Any]) -> str:
        """Extract readable text content from an item"""
        # Try various content fields
        for field in ['content', 'summary', 'description', 'rationale', 'value', 'text']:
            if field in item and item[field]:
                return str(item[field])
        
        # Fallback to string representation
        return str(item)
    
    def _calculate_query_relevance(self, content: str, query: str) -> float:
        """Calculate relevance between content and query"""
        if not content or not query:
            return 0.0
        
        query_terms = set(query.lower().split())
        content_terms = set(content.lower().split())
        
        if not query_terms:
            return 0.0
        
        # Jaccard similarity with term frequency weighting
        intersection = query_terms.intersection(content_terms)
        union = query_terms.union(content_terms)
        
        jaccard = len(intersection) / len(union) if union else 0.0
        
        # Boost for exact phrase matches
        phrase_boost = 1.0
        if query.lower() in content.lower():
            phrase_boost = 1.5
        
        return min(jaccard * phrase_boost, 1.0)
    
    async def _extract_facts(
        self, 
        processed_items: List[Dict[str, Any]], 
        validation_level: FactValidationLevel
    ) -> Dict[str, Any]:
        """Extract structured facts from processed items"""
        facts = {
            'explicit_facts': [],
            'implicit_facts': [],
            'entities': {},
            'relationships': [],
            'temporal_info': [],
            'quantitative_data': []
        }
        
        for item in processed_items:
            content = item['content']
            source = item['source']
            
            # Extract explicit facts using patterns
            for fact_type, pattern in self.fact_patterns.items():
                matches = re.findall(pattern, content, re.IGNORECASE)
                for match in matches:
                    facts['explicit_facts'].append({
                        'type': fact_type,
                        'value': match,
                        'source': source,
                        'confidence': item['relevance_score']
                    })
            
            # Extract entities (simple approach)
            entities = self._extract_entities(content)
            for entity_type, entity_values in entities.items():
                if entity_type not in facts['entities']:
                    facts['entities'][entity_type] = []
                
                for value in entity_values:
                    facts['entities'][entity_type].append({
                        'value': value,
                        'source': source,
                        'confidence': item['relevance_score']
                    })
        
        # Validate facts if required
        if validation_level != FactValidationLevel.NONE:
            facts = await self._validate_facts(facts, validation_level)
        
        return facts
    
    def _extract_entities(self, content: str) -> Dict[str, List[str]]:
        """Extract named entities from content (simplified approach)"""
        entities = {
            'technologies': [],
            'dates': [],
            'versions': [],
            'files': [],
            'functions': []
        }
        
        # Technology entities
        tech_pattern = r'\b(?:React|Angular|Vue|Node\.js|Python|Java|TypeScript|JavaScript|PostgreSQL|MySQL|MongoDB|Docker|Kubernetes|AWS|Azure|GCP)\b'
        entities['technologies'] = re.findall(tech_pattern, content, re.IGNORECASE)
        
        # Date entities
        date_pattern = r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b|\b\d{4}-\d{2}-\d{2}\b'
        entities['dates'] = re.findall(date_pattern, content)
        
        # Version entities
        version_pattern = r'v?\d+\.\d+(?:\.\d+)?'
        entities['versions'] = re.findall(version_pattern, content)
        
        # File entities
        file_pattern = r'\b\w+\.[a-zA-Z]{2,4}\b'
        entities['files'] = re.findall(file_pattern, content)
        
        # Function entities (simple approach)
        function_pattern = r'\b\w+\(\)'
        entities['functions'] = re.findall(function_pattern, content)
        
        return entities
    
    async def _validate_facts(
        self, 
        facts: Dict[str, Any], 
        validation_level: FactValidationLevel
    ) -> Dict[str, Any]:
        """Validate extracted facts for consistency and accuracy"""
        if validation_level == FactValidationLevel.BASIC:
            return self._basic_fact_validation(facts)
        elif validation_level == FactValidationLevel.MODERATE:
            return self._moderate_fact_validation(facts)
        elif validation_level == FactValidationLevel.STRICT:
            return await self._strict_fact_validation(facts)
        else:
            return facts
    
    def _basic_fact_validation(self, facts: Dict[str, Any]) -> Dict[str, Any]:
        """Basic fact validation - remove duplicates and obvious errors"""
        # Remove duplicate facts
        seen_facts = set()
        unique_facts = []
        
        for fact in facts['explicit_facts']:
            fact_key = f"{fact['type']}:{fact['value']}"
            if fact_key not in seen_facts:
                seen_facts.add(fact_key)
                unique_facts.append(fact)
        
        facts['explicit_facts'] = unique_facts
        
        # Basic entity deduplication
        for entity_type in facts['entities']:
            unique_entities = {}
            for entity in facts['entities'][entity_type]:
                value = entity['value'].lower()
                if value not in unique_entities or entity['confidence'] > unique_entities[value]['confidence']:
                    unique_entities[value] = entity
            
            facts['entities'][entity_type] = list(unique_entities.values())
        
        return facts
    
    def _moderate_fact_validation(self, facts: Dict[str, Any]) -> Dict[str, Any]:
        """Moderate fact validation - cross-reference and consistency checks"""
        facts = self._basic_fact_validation(facts)
        
        # Cross-reference facts from multiple sources
        fact_groups = {}
        for fact in facts['explicit_facts']:
            key = f"{fact['type']}:{fact['value']}"
            if key not in fact_groups:
                fact_groups[key] = []
            fact_groups[key].append(fact)
        
        # Mark facts supported by multiple sources
        validated_facts = []
        for key, fact_list in fact_groups.items():
            if len(fact_list) > 1:
                # Multiple sources - higher confidence
                best_fact = max(fact_list, key=lambda x: x['confidence'])
                best_fact['validated'] = True
                best_fact['source_count'] = len(fact_list)
                validated_facts.append(best_fact)
            else:
                # Single source - lower confidence
                fact_list[0]['validated'] = False
                fact_list[0]['source_count'] = 1
                validated_facts.append(fact_list[0])
        
        facts['explicit_facts'] = validated_facts
        return facts
    
    async def _strict_fact_validation(self, facts: Dict[str, Any]) -> Dict[str, Any]:
        """Strict fact validation - comprehensive checks"""
        facts = self._moderate_fact_validation(facts)
        
        # Additional consistency checks
        # Check for contradictory facts
        contradictions = self._detect_contradictions(facts)
        
        # Remove or flag contradictory facts
        if contradictions:
            facts['contradictions'] = contradictions
            facts['explicit_facts'] = [
                f for f in facts['explicit_facts'] 
                if not any(f in c['facts'] for c in contradictions)
            ]
        
        return facts
    
    def _detect_contradictions(self, facts: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Detect contradictory facts"""
        contradictions = []
        
        # Simple contradiction detection for dates and versions
        dates = [f for f in facts['explicit_facts'] if f['type'] == 'dates']
        versions = [f for f in facts['explicit_facts'] if f['type'] == 'versions']
        
        # Check for conflicting dates for the same entity
        # This is a simplified approach - could be more sophisticated
        
        return contradictions
    
    def _detect_domain(
        self, 
        query: str, 
        processed_items: List[Dict[str, Any]]
    ) -> str:
        """Detect the domain context for synthesis"""
        query_words = set(query.lower().split())
        content_words = set()
        
        for item in processed_items:
            content_words.update(item['content'].lower().split())
        
        all_words = query_words.union(content_words)
        
        # Check domain patterns
        for domain, pattern in self.domain_patterns.items():
            if domain == 'general':
                continue
            
            domain_keywords = set(pattern['keywords'])
            overlap = len(all_words.intersection(domain_keywords))
            
            if overlap >= len(domain_keywords) * 0.3:  # 30% keyword overlap
                return domain
        
        return 'general'
    
    async def _execute_synthesis_strategy(
        self,
        strategy: SynthesisStrategy,
        facts: Dict[str, Any],
        query: str,
        domain: str,
        processed_items: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Execute the selected synthesis strategy"""
        self.metrics['strategy_usage'][strategy.value] += 1
        
        if strategy == SynthesisStrategy.EXTRACTIVE:
            return self._extractive_synthesis(facts, query, domain, processed_items)
        
        elif strategy == SynthesisStrategy.ABSTRACTIVE:
            return await self._abstractive_synthesis(facts, query, domain, processed_items)
        
        elif strategy == SynthesisStrategy.HYBRID:
            return await self._hybrid_synthesis(facts, query, domain, processed_items)
        
        elif strategy == SynthesisStrategy.STRUCTURED:
            return self._structured_synthesis(facts, query, domain, processed_items)
        
        elif strategy == SynthesisStrategy.NARRATIVE:
            return await self._narrative_synthesis(facts, query, domain, processed_items)
        
        else:
            # Fallback to extractive
            return self._extractive_synthesis(facts, query, domain, processed_items)
    
    def _extractive_synthesis(
        self,
        facts: Dict[str, Any],
        query: str,
        domain: str,
        processed_items: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Extractive synthesis - combine key facts and excerpts"""
        key_facts = []
        key_excerpts = []
        
        # Extract key facts
        validated_facts = [f for f in facts['explicit_facts'] if f.get('validated', False)]
        if not validated_facts:
            validated_facts = facts['explicit_facts'][:5]  # Top 5 facts
        
        key_facts = validated_facts
        
        # Extract key excerpts from top sources
        for item in processed_items[:3]:  # Top 3 most relevant items
            content = item['content']
            if len(content) > 200:
                # Extract relevant sentences
                sentences = content.split('.')
                relevant_sentences = [
                    s.strip() for s in sentences 
                    if any(term in s.lower() for term in query.lower().split())
                ]
                if relevant_sentences:
                    key_excerpts.append(relevant_sentences[0][:200])
            else:
                key_excerpts.append(content)
        
        # Combine into answer
        answer_parts = []
        
        if key_excerpts:
            answer_parts.extend(key_excerpts)
        
        if key_facts:
            fact_summary = "Key facts: " + "; ".join([
                f"{f['type']}: {f['value']}" for f in key_facts[:3]
            ])
            answer_parts.append(fact_summary)
        
        answer = " ".join(answer_parts)
        
        # Apply domain template
        if domain in self.domain_patterns:
            template = self.domain_patterns[domain]['template']
            try:
                answer = template.format(
                    synthesis=answer,
                    details="See extracted facts above",
                    factors="Multiple sources analyzed"
                )
            except KeyError:
                pass  # Use original answer if template formatting fails
        
        return {
            'answer': answer[:self.config['max_synthesis_length']],
            'strategy': SynthesisStrategy.EXTRACTIVE.value,
            'key_facts': key_facts,
            'sources_used': len(processed_items)
        }
    
    async def _abstractive_synthesis(
        self,
        facts: Dict[str, Any],
        query: str,
        domain: str,
        processed_items: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Abstractive synthesis - generate new summary text"""
        # Collect all content
        all_content = [item['content'] for item in processed_items]
        combined_content = " ".join(all_content)
        
        # Simple abstractive approach - extract key concepts and relationships
        key_concepts = self._extract_key_concepts(combined_content, query)
        relationships = self._extract_relationships(combined_content, key_concepts)
        
        # Generate abstractive summary
        answer = self._generate_abstractive_summary(
            key_concepts, relationships, query, domain
        )
        
        return {
            'answer': answer[:self.config['max_synthesis_length']],
            'strategy': SynthesisStrategy.ABSTRACTIVE.value,
            'key_concepts': key_concepts,
            'relationships': relationships,
            'sources_used': len(processed_items)
        }
    
    async def _hybrid_synthesis(
        self,
        facts: Dict[str, Any],
        query: str,
        domain: str,
        processed_items: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Hybrid synthesis - combine extractive and abstractive approaches"""
        # Get extractive synthesis
        extractive_result = self._extractive_synthesis(facts, query, domain, processed_items)
        
        # Get abstractive synthesis
        abstractive_result = await self._abstractive_synthesis(facts, query, domain, processed_items)
        
        # Combine both approaches
        hybrid_answer = f"{abstractive_result['answer']}\n\n{extractive_result['answer']}"
        
        return {
            'answer': hybrid_answer[:self.config['max_synthesis_length']],
            'strategy': SynthesisStrategy.HYBRID.value,
            'extractive_component': extractive_result,
            'abstractive_component': abstractive_result,
            'sources_used': len(processed_items)
        }
    
    def _structured_synthesis(
        self,
        facts: Dict[str, Any],
        query: str,
        domain: str,
        processed_items: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Structured synthesis - create organized response"""
        structured_sections = {}
        
        # Organize by fact types
        for fact in facts['explicit_facts']:
            fact_type = fact['type']
            if fact_type not in structured_sections:
                structured_sections[fact_type] = []
            structured_sections[fact_type].append(fact['value'])
        
        # Organize by source types
        by_source = {}
        for item in processed_items:
            source_type = item['source_type']
            if source_type not in by_source:
                by_source[source_type] = []
            by_source[source_type].append(item['content'][:100])
        
        # Create structured answer
        answer_parts = []
        
        for section, items in structured_sections.items():
            if items:
                answer_parts.append(f"**{section.title()}**: {', '.join(items[:3])}")
        
        for source_type, contents in by_source.items():
            if contents:
                answer_parts.append(f"**From {source_type}**: {contents[0]}")
        
        answer = "\n".join(answer_parts)
        
        return {
            'answer': answer[:self.config['max_synthesis_length']],
            'strategy': SynthesisStrategy.STRUCTURED.value,
            'structured_sections': structured_sections,
            'source_breakdown': by_source,
            'sources_used': len(processed_items)
        }
    
    async def _narrative_synthesis(
        self,
        facts: Dict[str, Any],
        query: str,
        domain: str,
        processed_items: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Narrative synthesis - create flowing narrative response"""
        # Extract temporal sequence if available
        temporal_facts = [f for f in facts['explicit_facts'] if f['type'] == 'dates']
        temporal_facts.sort(key=lambda x: x['value'])
        
        # Create narrative flow
        narrative_parts = []
        
        # Introduction
        if processed_items:
            narrative_parts.append(f"Based on the available information, {query.lower()}")
        
        # Main content from top sources
        for i, item in enumerate(processed_items[:3]):
            content = item['content'][:150]
            if i == 0:
                narrative_parts.append(f"The primary information indicates that {content}")
            else:
                narrative_parts.append(f"Additionally, {content}")
        
        # Temporal information if available
        if temporal_facts:
            timeline = ", ".join([f['value'] for f in temporal_facts[:3]])
            narrative_parts.append(f"The timeline shows: {timeline}")
        
        # Conclusion
        if facts['explicit_facts']:
            key_fact = facts['explicit_facts'][0]
            narrative_parts.append(f"In summary, {key_fact['value']}")
        
        answer = ". ".join(narrative_parts) + "."
        
        return {
            'answer': answer[:self.config['max_synthesis_length']],
            'strategy': SynthesisStrategy.NARRATIVE.value,
            'narrative_structure': narrative_parts,
            'temporal_sequence': temporal_facts,
            'sources_used': len(processed_items)
        }
    
    def _extract_key_concepts(self, content: str, query: str) -> List[str]:
        """Extract key concepts from content"""
        # Simple approach - could be enhanced with NLP
        query_terms = set(query.lower().split())
        content_words = content.lower().split()
        
        # Find frequently mentioned terms that relate to query
        word_freq = {}
        for word in content_words:
            if len(word) > 3 and word not in {'that', 'this', 'with', 'from', 'they', 'have', 'been'}:
                word_freq[word] = word_freq.get(word, 0) + 1
        
        # Score by frequency and query relevance
        scored_concepts = []
        for word, freq in word_freq.items():
            relevance = 1 if word in query_terms else 0
            score = freq + relevance * 3
            scored_concepts.append((word, score))
        
        # Return top concepts
        scored_concepts.sort(key=lambda x: x[1], reverse=True)
        return [concept[0] for concept in scored_concepts[:10]]
    
    def _extract_relationships(self, content: str, concepts: List[str]) -> List[Dict[str, str]]:
        """Extract relationships between concepts"""
        relationships = []
        
        # Simple pattern-based relationship extraction
        relationship_patterns = [
            (r'(\w+)\s+(?:is|are)\s+(\w+)', 'is_a'),
            (r'(\w+)\s+(?:uses|utilizes)\s+(\w+)', 'uses'),
            (r'(\w+)\s+(?:depends on|requires)\s+(\w+)', 'depends_on'),
            (r'(\w+)\s+(?:implements|provides)\s+(\w+)', 'implements')
        ]
        
        for pattern, rel_type in relationship_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            for match in matches:
                if len(match) == 2 and match[0] in concepts and match[1] in concepts:
                    relationships.append({
                        'subject': match[0],
                        'predicate': rel_type,
                        'object': match[1]
                    })
        
        return relationships[:5]  # Limit to top 5 relationships
    
    def _generate_abstractive_summary(
        self,
        concepts: List[str],
        relationships: List[Dict[str, str]],
        query: str,
        domain: str
    ) -> str:
        """Generate abstractive summary from concepts and relationships"""
        summary_parts = []
        
        # Start with query context
        if concepts:
            main_concepts = concepts[:3]
            summary_parts.append(f"The main concepts involved are {', '.join(main_concepts)}")
        
        # Add relationships
        if relationships:
            rel_descriptions = []
            for rel in relationships[:2]:
                rel_descriptions.append(f"{rel['subject']} {rel['predicate'].replace('_', ' ')} {rel['object']}")
            summary_parts.append(f"Key relationships include: {', '.join(rel_descriptions)}")
        
        # Domain-specific conclusion
        if domain != 'general':
            summary_parts.append(f"From a {domain} perspective, this information provides important insights")
        
        return ". ".join(summary_parts) + "."
    
    async def _post_process_synthesis(
        self,
        synthesis_result: Dict[str, Any],
        facts: Dict[str, Any],
        processed_items: List[Dict[str, Any]],
        validation_level: FactValidationLevel
    ) -> Dict[str, Any]:
        """Post-process synthesis result"""
        # Ensure answer doesn't exceed max length
        if len(synthesis_result['answer']) > self.config['max_synthesis_length']:
            synthesis_result['answer'] = synthesis_result['answer'][:self.config['max_synthesis_length']] + "..."
        
        # Add metadata
        synthesis_result.update({
            'synthesis_timestamp': datetime.now().isoformat(),
            'validation_level': validation_level.value,
            'total_facts_used': len(facts['explicit_facts']),
            'total_sources': len(processed_items)
        })
        
        return synthesis_result
    
    def _calculate_confidence(
        self,
        synthesis_result: Dict[str, Any],
        facts: Dict[str, Any],
        processed_items: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Calculate confidence metrics for synthesis"""
        confidence_factors = {
            'source_count': min(len(processed_items) / 5, 1.0),  # Normalize to 5 sources
            'fact_validation': len([f for f in facts['explicit_facts'] if f.get('validated', False)]) / max(len(facts['explicit_facts']), 1),
            'source_agreement': self._calculate_source_agreement(processed_items),
            'answer_completeness': min(len(synthesis_result['answer']) / 500, 1.0)  # Normalize to 500 chars
        }
        
        # Weighted confidence calculation
        weights = {
            'source_count': 0.3,
            'fact_validation': 0.3,
            'source_agreement': 0.25,
            'answer_completeness': 0.15
        }
        
        confidence_score = sum(
            confidence_factors[factor] * weight 
            for factor, weight in weights.items()
        )
        
        confidence_level = self._score_to_confidence_level(confidence_score)
        
        return {
            'confidence_score': confidence_score,
            'confidence_level': confidence_level.value,
            'confidence_factors': confidence_factors
        }
    
    def _calculate_source_agreement(self, processed_items: List[Dict[str, Any]]) -> float:
        """Calculate agreement level between sources"""
        if len(processed_items) < 2:
            return 1.0
        
        # Simple approach - calculate content similarity between sources
        agreements = []
        
        for i in range(len(processed_items)):
            for j in range(i + 1, len(processed_items)):
                content1 = processed_items[i]['content'].lower()
                content2 = processed_items[j]['content'].lower()
                
                words1 = set(content1.split())
                words2 = set(content2.split())
                
                if words1 and words2:
                    intersection = len(words1.intersection(words2))
                    union = len(words1.union(words2))
                    similarity = intersection / union if union > 0 else 0.0
                    agreements.append(similarity)
        
        return sum(agreements) / len(agreements) if agreements else 0.0
    
    def _score_to_confidence_level(self, score: float) -> ConfidenceLevel:
        """Convert numeric confidence score to confidence level"""
        if score >= 0.9:
            return ConfidenceLevel.VERY_HIGH
        elif score >= 0.7:
            return ConfidenceLevel.HIGH
        elif score >= 0.5:
            return ConfidenceLevel.MODERATE
        elif score >= 0.3:
            return ConfidenceLevel.LOW
        else:
            return ConfidenceLevel.VERY_LOW
    
    def _generate_citations(
        self, 
        processed_items: List[Dict[str, Any]], 
        answer: str
    ) -> List[Dict[str, Any]]:
        """Generate citations for the synthesized answer"""
        citations = []
        
        for i, item in enumerate(processed_items):
            citation = {
                'id': i + 1,
                'source': item['source'],
                'source_type': item['source_type'],
                'relevance_score': item['relevance_score'],
                'used_in_answer': any(
                    word in answer.lower() 
                    for word in item['content'].lower().split()[:10]
                )
            }
            
            # Add source-specific metadata
            if 'metadata' in item and item['metadata']:
                citation['metadata'] = item['metadata']
            
            citations.append(citation)
        
        return citations
    
    async def _comprehensive_validation(
        self,
        synthesis_result: Dict[str, Any],
        retrieved_items: List[Dict[str, Any]],
        external_validator=None
    ) -> Dict[str, Any]:
        """Perform comprehensive validation of synthesis result"""
        validation_report = {
            'overall_confidence': synthesis_result.get('confidence_score', 0.5),
            'validation_checks': {},
            'warnings': [],
            'recommendations': []
        }
        
        # Internal consistency check
        consistency_score = self._check_internal_consistency(synthesis_result['answer'])
        validation_report['validation_checks']['internal_consistency'] = consistency_score
        
        # Source coverage check
        coverage_score = self._check_source_coverage(synthesis_result, retrieved_items)
        validation_report['validation_checks']['source_coverage'] = coverage_score
        
        # External validation if validator provided
        if external_validator:
            try:
                external_score = await external_validator.validate(synthesis_result['answer'])
                validation_report['validation_checks']['external_validation'] = external_score
            except Exception as e:
                logger.warning(f"External validation failed: {e}")
                validation_report['warnings'].append("External validation unavailable")
        
        # Calculate overall confidence
        check_scores = list(validation_report['validation_checks'].values())
        if check_scores:
            validation_report['overall_confidence'] = sum(check_scores) / len(check_scores)
        
        return validation_report
    
    def _check_internal_consistency(self, answer: str) -> float:
        """Check internal consistency of the answer"""
        # Simple consistency checks
        sentences = answer.split('.')
        
        if len(sentences) < 2:
            return 0.8  # Single sentence - assume consistent
        
        # Check for contradictory phrases
        contradictory_pairs = [
            ('is', 'is not'),
            ('true', 'false'),
            ('always', 'never'),
            ('increase', 'decrease')
        ]
        
        contradiction_count = 0
        for sent in sentences:
            sent_lower = sent.lower()
            for pair in contradictory_pairs:
                if pair[0] in sent_lower and pair[1] in sent_lower:
                    contradiction_count += 1
        
        # Simple scoring
        consistency_score = max(0.0, 1.0 - (contradiction_count * 0.2))
        return consistency_score
    
    def _check_source_coverage(
        self, 
        synthesis_result: Dict[str, Any], 
        retrieved_items: List[Dict[str, Any]]
    ) -> float:
        """Check how well the synthesis covers the available sources"""
        answer = synthesis_result['answer'].lower()
        sources_used = synthesis_result.get('sources_used', 0)
        total_sources = len(retrieved_items)
        
        if total_sources == 0:
            return 0.0
        
        # Check content coverage
        content_coverage = 0
        for item in retrieved_items:
            content_words = set(item.get('content', '').lower().split()[:20])  # First 20 words
            answer_words = set(answer.split())
            
            if content_words and answer_words:
                overlap = len(content_words.intersection(answer_words))
                if overlap > 0:
                    content_coverage += 1
        
        coverage_ratio = content_coverage / total_sources
        source_usage_ratio = sources_used / total_sources if sources_used else 0
        
        # Combined coverage score
        coverage_score = (coverage_ratio * 0.6) + (source_usage_ratio * 0.4)
        return min(coverage_score, 1.0)
    
    def _create_empty_response(self, query: str, message: str) -> Dict[str, Any]:
        """Create empty response when no information is available"""
        return {
            'answer': message,
            'strategy': 'none',
            'confidence_score': 0.0,
            'confidence_level': ConfidenceLevel.VERY_LOW.value,
            'sources_used': 0,
            'synthesis_timestamp': datetime.now().isoformat(),
            'citations': []
        }
    
    def _create_error_response(self, query: str, error_message: str) -> Dict[str, Any]:
        """Create error response when synthesis fails"""
        return {
            'answer': f"Error synthesizing information: {error_message}",
            'strategy': 'error',
            'confidence_score': 0.0,
            'confidence_level': ConfidenceLevel.VERY_LOW.value,
            'sources_used': 0,
            'synthesis_timestamp': datetime.now().isoformat(),
            'error': error_message,
            'citations': []
        }
    
    def _update_metrics(
        self,
        execution_time: float,
        strategy: SynthesisStrategy,
        confidence_score: float,
        success: bool = True
    ):
        """Update performance metrics"""
        self.metrics['total_syntheses'] += 1
        
        if success:
            self.metrics['successful_syntheses'] += 1
            
            # Update average synthesis time
            total_time = (
                self.metrics['avg_synthesis_time'] * (self.metrics['total_syntheses'] - 1) +
                execution_time
            )
            self.metrics['avg_synthesis_time'] = total_time / self.metrics['total_syntheses']
            
            # Update average confidence
            total_confidence = (
                self.metrics['avg_confidence_score'] * (self.metrics['successful_syntheses'] - 1) +
                confidence_score
            )
            self.metrics['avg_confidence_score'] = total_confidence / self.metrics['successful_syntheses']
    
    def get_metrics(self) -> Dict[str, Any]:
        """Get current performance metrics"""
        success_rate = (
            self.metrics['successful_syntheses'] / self.metrics['total_syntheses']
            if self.metrics['total_syntheses'] > 0 else 0.0
        )
        
        return {
            **self.metrics,
            'success_rate': success_rate
        }
    
    def reset_metrics(self):
        """Reset performance metrics"""
        for key in self.metrics:
            if isinstance(self.metrics[key], (int, float)):
                self.metrics[key] = 0
            elif isinstance(self.metrics[key], dict):
                for subkey in self.metrics[key]:
                    self.metrics[key][subkey] = 0