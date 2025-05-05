import os
import sys
import argparse
import base64
import json
from io import BytesIO
from PIL import Image
import google.generativeai as genai
from google.generativeai import types

# Set up defaults and get API key from environment variable
defaults = {
    "api_key": os.getenv('GEMINI_API_KEY'),
    "model": "gemini-2.0-flash-exp-image-generation",
    "size": "1:1",  # Aspect ratio format for Google's API
    "quality": "standard",
    "number": "1",
}

# Function to validate and parse arguments
def validate_and_parse_args(parser):
    args = parser.parse_args()

    for key, value in vars(args).items():
        if not value:
            args.__dict__[key] = parser.get_default(key)

    if not args.api_key:
        parser.error('The --api-key argument is required if GEMINI_API_KEY environment variable is not set.')
    if not args.prompt:
        parser.error('The --prompt argument is required.')
    if not args.number.isdigit():
        parser.error('The --number argument must be a number.')
    args.number = int(args.number)

    return args

def main():
    # Parse the command line arguments
    parser = argparse.ArgumentParser(description="CLI for image generation prompt using Google's Imagen/Gemini model.")
    parser.add_argument('-k', '--api-key', type=str, default=defaults["api_key"],
                        help='Google Gemini API key. Can also be set with GEMINI_API_KEY environment variable.')
    parser.add_argument('-p', '--prompt', type=str, required=True, help='Prompt for image generation.')
    parser.add_argument('-m', '--model', type=str, default=defaults["model"],
                        help=f'Model to use for image generation. Default is "{defaults["model"]}".')
    parser.add_argument('-s', '--size', type=str, default=defaults["size"],
                        help=f'Aspect ratio of the image to generate (e.g. "1:1", "16:9"). Default is {defaults["size"]}.')
    parser.add_argument('-q', '--quality', type=str, default=defaults["quality"],
                        help=f'Quality of the generated image. Allowed values are "standard" or "hd". Default is "{defaults["quality"]}"')
    parser.add_argument('-n', '--number', type=str, default=defaults["number"],
                        help='Number of images to generate. Default is 1.')
    args = validate_and_parse_args(parser)

    # Initialize Google genai client
    try:
        genai.configure(api_key=args.api_key)
        client = genai.Client()

        image_urls = []

        # For Gemini model (text-to-image generation)
        if "gemini" in args.model:
            response = client.models.generate_content(
                model=args.model,
                contents=args.prompt,
                config=types.GenerateContentConfig(
                    response_modalities=['TEXT', 'IMAGE']
                )
            )
            
            # Extract images from response
            for i, part in enumerate(response.candidates[0].content.parts):
                if part.inline_data is not None:
                    # Create a unique identifier for the image
                    image_data = {
                        "b64_json": base64.b64encode(part.inline_data.data).decode(),
                        "index": i
                    }
                    # Create a JSON string that looks like a URL but contains the base64 data
                    image_urls.append(f"data:image/b64json;{base64.b64encode(json.dumps(image_data).encode()).decode()}")
        
        # For Imagen model (dedicated image generation)
        else:
            # Convert size from "width:height" format to Google's aspect ratio format
            aspect_ratio = args.size  # Google already uses the 1:1, 16:9 format
            
            response = client.models.generate_images(
                model="imagen-3.0-generate-002",  # Use specific Imagen model
                prompt=args.prompt,
                config=types.GenerateImagesConfig(
                    number_of_images=args.number,
                    aspect_ratio=aspect_ratio
                )
            )
            
            # Extract images from response
            for i, generated_image in enumerate(response.generated_images):
                # Create a unique identifier for the image
                image_data = {
                    "b64_json": base64.b64encode(generated_image.image.image_bytes).decode(),
                    "index": i
                }
                # Create a JSON string that looks like a URL but contains the base64 data
                image_urls.append(f"data:image/b64json;{base64.b64encode(json.dumps(image_data).encode()).decode()}")
        
        print(image_urls)
        
    except Exception as e:
        print(f"Received an error while generating images: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
