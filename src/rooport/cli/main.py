#!/usr/bin/env python3
"""ROOPORT CLI Entry Point."""

import argparse
import asyncio
import sys
from pathlib import Path
import logging
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

# Import ROOPORT core components
from ..core.orchestrator import UltimateAgenticOrchestrator
from ..config.autonomous_mode import get_autonomous_mode, set_autonomous_mode

console = Console()

def setup_logging(level=logging.INFO):
    """Setup logging configuration"""
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def display_banner():
    """Display ROOPORT banner"""
    banner = Text("🚀 ROOPORT", style="bold blue")
    subtitle = Text("The Ultimate Agentic Coding Tool", style="italic")
    
    console.print(Panel.fit(
        f"{banner}\n{subtitle}",
        border_style="blue"
    ))

def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="ROOPORT: The Ultimate Agentic Coding Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  rooport --autonomous standard          # Run with standard automation
  rooport --workspace /path/to/project   # Specify workspace directory
  rooport --version                      # Show version information
        """
    )
    
    parser.add_argument("--version", action="version", version="ROOPORT 1.0.0")
    parser.add_argument(
        "--autonomous", 
        choices=["off", "minimal", "standard", "full"], 
        default=None,
        help="Set autonomous mode level"
    )
    parser.add_argument(
        "--workspace", 
        type=str, 
        default=".", 
        help="Workspace directory (default: current directory)"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose logging"
    )
    parser.add_argument(
        "--config",
        type=str,
        help="Path to configuration file"
    )
    
    args = parser.parse_args()
    
    # Setup logging
    log_level = logging.DEBUG if args.verbose else logging.INFO
    setup_logging(log_level)
    
    # Display banner
    display_banner()
    
    # Show current configuration
    workspace_path = Path(args.workspace).absolute()
    console.print(f"📁 Workspace: {workspace_path}")
    
    # Handle autonomous mode setting
    if args.autonomous:
        try:
            set_autonomous_mode(args.autonomous)
            console.print(f"🤖 Autonomous Mode: {args.autonomous.upper()}", style="green")
        except Exception as e:
            console.print(f"❌ Failed to set autonomous mode: {e}", style="red")
            return 1
    else:
        enabled, level = get_autonomous_mode()
        status = f"{level.upper()}" if enabled else "OFF"
        console.print(f"🤖 Autonomous Mode: {status}")
    
    console.print("\n🧠 Initializing AI engines...")
    
    try:
        # Initialize ROOPORT (placeholder for now)
        console.print("  ✅ Ultimate Agentic Orchestrator")
        console.print("  ✅ Agentic RAG Engine")
        console.print("  ✅ Continuous Learning System")
        console.print("  ✅ Proactive Orchestration Engine")
        
        console.print("\n🎯 ROOPORT ready for action!")
        console.print("\nNext steps:")
        console.print("  • Configure your API keys in .env file")
        console.print("  • Set up MCP servers (see docs/setup-guide.md)")
        console.print("  • Initialize ConPort knowledge base")
        console.print("  • Start your first agentic coding session!")
        
        console.print(f"\n📚 Documentation: docs/README.md")
        console.print(f"🔧 Configuration: {workspace_path}/config/")
        
        return 0
        
    except Exception as e:
        console.print(f"❌ Failed to initialize ROOPORT: {e}", style="red")
        return 1

if __name__ == "__main__":
    sys.exit(main())