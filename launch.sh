#!/bin/bash
# Godmode Launcher Script
# Simple launcher for the Godmode diagnostics tool.

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is required but not installed."
    exit 1
fi

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "🚀 Starting Godmode..."
echo "Location: $SCRIPT_DIR"
echo ""

# Launch the diagnostics tool
python3 "$SCRIPT_DIR/godmode.py" "$@"