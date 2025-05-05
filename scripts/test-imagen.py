#!/usr/bin/env python3
import os
import sys
import base64
from io import BytesIO
from PIL import Image
import google.generativeai as genai
from google.generativeai import types

# Get API key from environment
api_key = os.environ.get('GEMINI_API_KEY')

if not api_key:
    print("Error: GEMINI_API_KEY environment variable not set")
    exit(1)

print("Testing Google Imagen image generation...")
try:
    # Configure the genai client
    genai.configure(api_key=api_key)
    client = genai.Client()
    
    # Method 1: Using generate_images (for Imagen 3 model)
    print("Testing Imagen model...")
    response = client.models.generate_images(
        model="imagen-3.0-generate-002",
        prompt="A serene lake surrounded by mountains at sunset, photorealistic",
        config=types.GenerateImagesConfig(
            number_of_images=1,
            aspect_ratio="1:1"  # 1:1 aspect ratio (square)
        )
    )
    
    # Save the image from the response
    if response.generated_images:
        print("Image generation successful!")
        print("Saving the Imagen generated image...")
        
        # Get the image bytes from the first generated image
        image_bytes = response.generated_images[0].image.image_bytes
        
        # Save the image
        with open("imagen-test.png", "wb") as f:
            f.write(image_bytes)
        print("Image saved to imagen-test.png")
    
    # Method 2: Using generate_content (for Gemini model)
    print("\nTesting Gemini model...")
    response = client.models.generate_content(
        model="gemini-2.0-flash-exp-image-generation",
        contents="A colorful tropical fish swimming in a coral reef, photorealistic",
        config=types.GenerateContentConfig(
            response_modalities=['TEXT', 'IMAGE']
        )
    )
    
    # Process the response for parts that contain images
    for i, part in enumerate(response.candidates[0].content.parts):
        if part.text:
            print(f"Text from Gemini: {part.text}")
        elif part.inline_data is not None:
            print(f"Image generation successful!")
            print(f"Saving the Gemini generated image...")
            
            # Get the image data
            image_data = part.inline_data.data
            
            # Save the image
            with open(f"gemini-test-{i}.png", "wb") as f:
                f.write(image_data)
            print(f"Image saved to gemini-test-{i}.png")
        
except Exception as e:
    print(f"Error testing Google image generation: {e}")
    sys.exit(1)

print("Test complete!") 