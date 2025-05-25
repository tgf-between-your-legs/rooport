#!/bin/bash
# RooPort CONVEX - One-Line Installer
# Usage: curl -sSL https://raw.githubusercontent.com/tgf-between-your-legs/rooport/master/install.sh | bash

set -e

echo "🚀 Installing RooPort CONVEX - Ultimate Agentic Coding Tool"

# Check prerequisites
command -v python3 >/dev/null 2>&1 || { echo "❌ Python 3.9+ required but not installed. Aborting." >&2; exit 1; }
command -v git >/dev/null 2>&1 || { echo "❌ Git required but not installed. Aborting." >&2; exit 1; }

# Install RooPort CONVEX
echo "📦 Installing RooPort CONVEX..."
pip install git+https://github.com/tgf-between-your-legs/rooport.git

# Verify installation
if command -v rooport >/dev/null 2>&1; then
    echo "✅ RooPort CONVEX installed successfully!"
    echo ""
    echo "🎯 Quick Start:"
    echo "   rooport --convex    # Launch with CONVEX capabilities"
    echo "   rooport --help      # Show all options"
    echo ""
    echo "📚 Documentation: https://github.com/tgf-between-your-legs/rooport"
else
    echo "❌ Installation failed. Please check the error messages above."
    exit 1
fi