#!/bin/bash

# Define the path to the virtual environment
VENV_PATH="env"

# Check if the virtual environment exists
if [ ! -d "$VENV_PATH" ] || [ ! -f "$VENV_PATH/bin/activate" ]; then
    echo "Initializing Virtual Python Environment..."
    python3 -m venv env
    source $VENV_PATH/bin/activate
    pip install -r requirements.txt || rm -rf "$VENV_PATH"
    echo "Setup Complete"
else
    source $VENV_PATH/bin/activate
fi

# Run Wild-Storage
python cli_app.py
