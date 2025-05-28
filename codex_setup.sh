#!/usr/bin/env bash
# Setup script for OpenAI Codex environments
# Installs dependencies before network access is disabled
set -e

python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -e .

