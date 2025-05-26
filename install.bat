@echo off
REM RooPort CONVEX - One-Line Installer for Windows
REM Usage: Download and run this file, or use: powershell -c "iwr https://raw.githubusercontent.com/tgf-between-your-legs/rooport/master/install.bat -o install.bat; .\install.bat"

echo 🚀 Installing RooPort CONVEX - Ultimate Agentic Coding Tool

REM Check prerequisites
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python 3.9+ required but not installed. Please install Python first.
    pause
    exit /b 1
)

git --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Git required but not installed. Please install Git first.
    pause
    exit /b 1
)

REM Install RooPort CONVEX
echo 📦 Installing RooPort CONVEX...
pip install git+https://github.com/tgf-between-your-legs/rooport.git

REM Verify installation
rooport --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Installation failed. Please check the error messages above.
    pause
    exit /b 1
) else (
    echo ✅ RooPort CONVEX installed successfully!
    echo.
    echo 🎯 Quick Start:
    echo    rooport --autonomous standard    # Launch with CONVEX capabilities
    echo    rooport --help      # Show all options
    echo.
    echo 📚 Documentation: https://github.com/tgf-between-your-legs/rooport
    pause
)