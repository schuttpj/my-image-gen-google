#!/usr/bin/env python3
import os
import sys
import google.generativeai as genai

# Test if we can initialize the client
try:
    print("Testing Google GenAI client initialization...")
    api_key = os.environ.get('GEMINI_API_KEY')
    if not api_key or api_key == "your_api_key_here":
        print("⚠️ Warning: Using a placeholder API key. This will fail.")
        print("Please set a real GEMINI_API_KEY environment variable.")
    
    # Just initialize the client (will validate API key format but not connect)
    genai.configure(api_key=api_key)
    print("✓ Client initialization successful")
    
    # List available models (this will test the API connection)
    print("\nTesting API connection by listing available models...")
    try:
        models = genai.list_models()
        print("✓ API connection successful")
        print("\nAvailable models:")
        for model in models:
            if "image" in model.supported_generation_methods:
                print(f"- {model.name} (Supports image generation)")
    except Exception as e:
        print(f"✗ API connection failed: {e}")
        
except Exception as e:
    print(f"✗ Client initialization failed: {e}")
    sys.exit(1)

print("\nTest complete!") 