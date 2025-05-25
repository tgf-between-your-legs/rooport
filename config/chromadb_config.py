"""
ChromaDB Configuration for RooPort CONVEX v2.0

Defines configuration settings for ChromaDB vector database integration.
"""

import os
from typing import Dict, Any

# ChromaDB Configuration
CHROMADB_CONFIG = {
    # Persistence settings
    'persist_directory': os.getenv('CHROMADB_PERSIST_DIR', './data/chromadb'),
    
    # Embedding model configuration
    'embedding_function': 'sentence-transformers/all-MiniLM-L6-v2',
    'embedding_model_cache_dir': './data/models/sentence-transformers',
    
    # Search and similarity settings
    'distance_metric': 'cosine',  # Options: cosine, l2, ip
    'max_batch_size': 1000,
    'similarity_threshold': 0.7,
    
    # Collection settings
    'auto_embed': True,
    'auto_sync_interval': 300,  # seconds
    'max_collection_size': 100000,
    
    # Performance settings
    'query_cache_size': 1000,
    'embedding_cache_size': 5000,
    'parallel_queries': True,
    'max_concurrent_queries': 10,
    
    # Logging and monitoring
    'enable_telemetry': False,
    'log_level': 'INFO',
    'performance_monitoring': True
}

# Collection-specific configurations
COLLECTION_CONFIGS = {
    'decisions': {
        'name': 'project_decisions',
        'description': 'Project decisions and architectural choices',
        'embedding_fields': ['summary', 'rationale', 'details'],
        'metadata_fields': ['timestamp', 'tags', 'confidence_score', 'workspace_id'],
        'auto_sync': True,
        'retention_days': 365
    },
    'patterns': {
        'name': 'system_patterns',
        'description': 'Architectural and design patterns',
        'embedding_fields': ['name', 'description', 'implementation'],
        'metadata_fields': ['timestamp', 'tags', 'pattern_type', 'workspace_id'],
        'auto_sync': True,
        'retention_days': 365
    },
    'progress': {
        'name': 'project_progress',
        'description': 'Project progress and task tracking',
        'embedding_fields': ['description', 'status', 'notes'],
        'metadata_fields': ['timestamp', 'status', 'priority', 'workspace_id'],
        'auto_sync': True,
        'retention_days': 180
    },
    'custom_data': {
        'name': 'custom_project_data',
        'description': 'Custom project data and documentation',
        'embedding_fields': ['value', 'description'],
        'metadata_fields': ['timestamp', 'category', 'key', 'workspace_id'],
        'auto_sync': True,
        'retention_days': 365
    },
    'code_snippets': {
        'name': 'code_patterns',
        'description': 'Code snippets and programming patterns',
        'embedding_fields': ['code', 'description', 'comments'],
        'metadata_fields': ['timestamp', 'language', 'framework', 'workspace_id'],
        'auto_sync': True,
        'retention_days': 365
    },
    'error_solutions': {
        'name': 'error_solutions',
        'description': 'Error patterns and their solutions',
        'embedding_fields': ['error_description', 'solution', 'context'],
        'metadata_fields': ['timestamp', 'error_type', 'success_rate', 'workspace_id'],
        'auto_sync': True,
        'retention_days': 730  # Keep error solutions longer
    }
}

# Embedding model configurations
EMBEDDING_MODELS = {
    'default': {
        'model_name': 'sentence-transformers/all-MiniLM-L6-v2',
        'dimensions': 384,
        'max_seq_length': 256,
        'use_cache': True
    },
    'code': {
        'model_name': 'microsoft/codebert-base',
        'dimensions': 768,
        'max_seq_length': 512,
        'use_cache': True
    },
    'multilingual': {
        'model_name': 'sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2',
        'dimensions': 384,
        'max_seq_length': 128,
        'use_cache': True
    }
}

def get_chromadb_config() -> Dict[str, Any]:
    """Get ChromaDB configuration with environment overrides"""
    config = CHROMADB_CONFIG.copy()
    
    # Override with environment variables if present
    config.update({
        key: os.getenv(f'CHROMADB_{key.upper()}', value)
        for key, value in config.items()
        if isinstance(value, (str, int, float, bool))
    })
    
    return config

def get_collection_config(collection_type: str) -> Dict[str, Any]:
    """Get configuration for a specific collection type"""
    return COLLECTION_CONFIGS.get(collection_type, {})

def get_embedding_model_config(model_type: str = 'default') -> Dict[str, Any]:
    """Get embedding model configuration"""
    return EMBEDDING_MODELS.get(model_type, EMBEDDING_MODELS['default'])