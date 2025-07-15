```
#!/bin/bash

# xAI Artifact: Generated with Grok by xAI
# Made by DeMoD LLC with Grok 4
# Bash CLI for installing and starting the Resistance Storage Project.
# Usage: ./resistance_cli.sh [install|start|help]
# - install: Sets up the project (venv, deps, extract files from README.md).
# - start: Activates venv and runs the TUI (python tui.py).
# - help: Shows this message.
# Assumes Python 3.8+ and README.md with embedded code in the current dir.

set -e  # Exit on error

PROJECT_DIR="$(pwd)/resistance_storage"
VENV_DIR="$PROJECT_DIR/venv"
README_FILE="$(pwd)/docs/README.md"  # Path to README.md

# Function to extract code from README.md using awk
extract_code() {
    local filename=$1
    awk "/### $filename/{getline; while (\$0 !~ /^$/) { if (\$0 ~ /^```(python|bash)/) { getline; while (\$0 !~ /^```/) { print \$0; getline; } } else { getline; } } }" "$README_FILE" > "$filename"
    if [[ "$filename" == *.sh ]]; then
        chmod +x "$filename"
    fi
}

# Check if README.md exists
if [ ! -f "$README_FILE" ]; then
    echo "Error: $README_FILE not found. Please ensure the README.md with embedded code is available."
    exit 1
fi

# CLI logic
case "$1" in
    install)
        echo "Installing Resistance Storage Project..."
        
        # Create project directory if not exists
        mkdir -p "$PROJECT_DIR"
        cd "$PROJECT_DIR"
        
        # Create virtual environment
        python3 -m venv "$VENV_DIR"
        
        # Activate venv
        source "$VENV_DIR/bin/activate"
        
        # Install dependencies
        pip install textual
        
        # Extract Python files
        extract_code "src/binary_parser.py"
        extract_code "src/cipher.py"
        extract_code "src/quality_check.py"
        extract_code "src/tui.py"
        # Extract others if added
        
        # Validate extracted files
        for file in src/binary_parser.py src/cipher.py src/quality_check.py src/tui.py; do
            if [ ! -s "$file" ]; then
                echo "Error: Failed to extract $file from README.md"
                exit 1
            fi
        done
        
        echo "Installation complete! Use './scripts/resistance_cli.sh start' to run the TUI."
        ;;
    
    start)
        if [ ! -d "$VENV_DIR" ]; then
            echo "Error: Project not installed. Run './scripts/resistance_cli.sh install' first."
            exit 1
        fi
        
        cd "$PROJECT_DIR"
        source "$VENV_DIR/bin/activate"
        python src/tui.py
        ;;
    
    help)
        echo "Usage: ./scripts/resistance_cli.sh [install|start|help]"
        echo "  install: Set up the project and dependencies."
        echo "  start: Activate venv and run the TUI."
        echo "  help: Show this message."
        ;;
    
    *)
        echo "Invalid command. Use './scripts/resistance_cli.sh help' for usage."
        exit 1
        ;;
esac
```
