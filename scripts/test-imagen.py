#!/usr/bin/env python3
import os
import sys
import requests
import base64
from io import BytesIO
from openai import OpenAI

# Get API key from environment
api_key = os.environ.get('GEMINI_API_KEY')

if not api_key:
    print("Error: GEMINI_API_KEY environment variable not set")
    exit(1)

print("Testing Google Imagen image generation...")
try:
    # Initialize the client with Google's API
    client = OpenAI(
        api_key=api_key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )
    
    # Generate an image
    response = client.images.generate(
        model="imagen-3.0-generate-002",
        prompt="A serene lake surrounded by mountains at sunset, photorealistic",
        size="1024x1024",
        n=1,
        response_format="b64_json"  # Google only supports b64_json
    )
    
    # Get the base64 encoded image
    image_data = response.data[0].b64_json
    print("Image generation successful!")
    
    # Decode and save the image
    print("Saving the image...")
    image_bytes = base64.b64decode(image_data)
    with open("imagen-test.png", "wb") as f:
        f.write(image_bytes)
    print("Image saved to imagen-test.png")
        
except Exception as e:
    print(f"Error testing Google Imagen: {e}")
    sys.exit(1)

print("Test complete!") 