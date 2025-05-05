#!/bin/bash

echo "Installing dependencies for Google Imagen/Gemini image generation tool..."

# Ensure pip is available
which pip3 > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "pip3 not found. Please install Python 3 and pip first."
    exit 1
fi

# Install requirements
pip3 install -r requirements.txt

echo "Installation complete!"
echo "To use this tool, make sure to set the GEMINI_API_KEY environment variable."
echo "Example: export GEMINI_API_KEY=your_api_key_here" 