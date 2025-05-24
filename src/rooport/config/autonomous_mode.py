"""
Autonomous Mode Configuration for ROOPORT
Handles user-controllable automation levels and safety mechanisms
"""

import json
import os
from pathlib import Path
from typing import Tuple, Dict, Any
from enum import Enum

class AutomationLevel(Enum):
    """Automation levels for ROOPORT"""
    OFF = "off"
    MINIMAL = "minimal" 
    STANDARD = "standard"
    FULL = "full"

class AutonomousModeConfig:
    """Manages autonomous mode configuration"""
    
    def __init__(self, config_path: str = None):
        if config_path is None:
            config_path = os.path.join(os.getcwd(), "config", "autonomous-mode.json")
        self.config_path = Path(config_path)
        self.config_path.parent.mkdir(parents=True, exist_ok=True)
        
    def get_default_config(self) -> Dict[str, Any]:
        """Get default configuration"""
        return {
            "enabled": False,
            "level": "standard",
            "user_preferences": {
                "auto_approve_types": [],
                "never_auto_types": [],
                "confidence_thresholds": {
                    "suggestions": 0.8,
                    "optimizations": 0.7,
                    "learning_updates": 0.9
                }
            },
            "last_updated": None,
            "version": "1.0"
        }
    
    def load_config(self) -> Dict[str, Any]:
        """Load configuration from file"""
        try:
            if self.config_path.exists():
                with open(self.config_path, 'r') as f:
                    config = json.load(f)
                # Validate config structure
                default_config = self.get_default_config()
                for key in default_config:
                    if key not in config:
                        config[key] = default_config[key]
                return config
            else:
                return self.get_default_config()
        except Exception:
            return self.get_default_config()
    
    def save_config(self, config: Dict[str, Any]) -> None:
        """Save configuration to file"""
        try:
            with open(self.config_path, 'w') as f:
                json.dump(config, f, indent=2)
        except Exception as e:
            raise RuntimeError(f"Failed to save autonomous mode config: {e}")
    
    def get_mode(self) -> Tuple[bool, str]:
        """Get current autonomous mode status"""
        config = self.load_config()
        return config.get('enabled', False), config.get('level', 'standard')
    
    def set_mode(self, enabled: bool = None, level: str = None) -> None:
        """Set autonomous mode status"""
        config = self.load_config()
        
        if enabled is not None:
            config['enabled'] = enabled
        
        if level is not None:
            if level not in [l.value for l in AutomationLevel]:
                raise ValueError(f"Invalid automation level: {level}")
            config['level'] = level
        
        config['last_updated'] = self._get_timestamp()
        self.save_config(config)
    
    def should_execute_autonomous_action(self, confidence_score: float, action_type: str) -> bool:
        """Determine if action should be executed autonomously"""
        enabled, level = self.get_mode()
        
        if not enabled:
            return False
        
        config = self.load_config()
        user_prefs = config.get('user_preferences', {})
        
        # Check user preferences
        if action_type in user_prefs.get('never_auto_types', []):
            return False
        
        if action_type in user_prefs.get('auto_approve_types', []):
            return True
        
        # Check confidence thresholds based on level
        thresholds = user_prefs.get('confidence_thresholds', {})
        
        if level == AutomationLevel.MINIMAL.value:
            return False  # Always ask in minimal mode
        elif level == AutomationLevel.STANDARD.value:
            threshold = thresholds.get('suggestions', 0.8)
            return confidence_score > threshold
        elif level == AutomationLevel.FULL.value:
            return confidence_score > 0.3  # Low threshold for full automation
        
        return False
    
    def update_user_preference(self, action_type: str, preference: str) -> None:
        """Update user preference for specific action type"""
        config = self.load_config()
        user_prefs = config.setdefault('user_preferences', {})
        
        if preference == "auto_approve":
            auto_types = user_prefs.setdefault('auto_approve_types', [])
            if action_type not in auto_types:
                auto_types.append(action_type)
            
            # Remove from never_auto if present
            never_types = user_prefs.get('never_auto_types', [])
            if action_type in never_types:
                never_types.remove(action_type)
        
        elif preference == "never_auto":
            never_types = user_prefs.setdefault('never_auto_types', [])
            if action_type not in never_types:
                never_types.append(action_type)
            
            # Remove from auto_approve if present
            auto_types = user_prefs.get('auto_approve_types', [])
            if action_type in auto_types:
                auto_types.remove(action_type)
        
        config['last_updated'] = self._get_timestamp()
        self.save_config(config)
    
    def get_status_display(self) -> str:
        """Get status display string"""
        enabled, level = self.get_mode()
        
        if not enabled:
            return "[AUTONOMOUS: OFF]"
        else:
            return f"[AUTONOMOUS: {level.upper()}]"
    
    def _get_timestamp(self) -> str:
        """Get current timestamp"""
        from datetime import datetime
        return datetime.now().isoformat()

# Global instance
_config_instance = None

def get_config_instance() -> AutonomousModeConfig:
    """Get global configuration instance"""
    global _config_instance
    if _config_instance is None:
        _config_instance = AutonomousModeConfig()
    return _config_instance

def get_autonomous_mode() -> Tuple[bool, str]:
    """Get current autonomous mode"""
    return get_config_instance().get_mode()

def set_autonomous_mode(level: str) -> None:
    """Set autonomous mode level"""
    config = get_config_instance()
    
    if level == "off":
        config.set_mode(enabled=False)
    else:
        config.set_mode(enabled=True, level=level)

def should_execute_autonomous_action(confidence_score: float, action_type: str) -> bool:
    """Check if action should be executed autonomously"""
    return get_config_instance().should_execute_autonomous_action(confidence_score, action_type)

def get_status_display() -> str:
    """Get autonomous mode status for display"""
    return get_config_instance().get_status_display()

def update_user_preference(action_type: str, preference: str) -> None:
    """Update user preference for action type"""
    get_config_instance().update_user_preference(action_type, preference)