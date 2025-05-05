# Custom Google Imagen Generation Tool for GPTScript

This tool provides a simple interface for generating images using Google's Imagen model through GPTScript. It allows you to easily integrate high-quality image generation capabilities into your GPTScript workflows.

## Features

* Uses Google's advanced Imagen image generation model
* Configurable image size and quantity
* Easy integration with GPTScript
* Simple API key management

## Prerequisites

* Python 3.x
* Google Gemini API key (for access to Imagen)
* GPTScript installed

## Installation

1. Clone this repository:
```
git clone https://github.com/schuttpj/my-image-gen-google.git
cd my-image-gen-google
```

2. Install the required Python packages:
```
pip install -r requirements.txt
```

## Usage with GPTScript

You can use this tool in your GPTScript files by referencing it:

```
tools: github.com/schuttpj/my-image-gen-google

You are an expert in image generation. Generate an image of a futuristic city with flying cars.
```

### Customizing Image Generation

The tool supports several parameters:

| Parameter | Description | Default |
|-----------|-------------|---------|
| prompt | The text prompt for image generation | (Required) |
| model | Model to use (default: "imagen-3.0-generate-002") | "imagen-3.0-generate-002" |
| size | Image size (e.g., "1024x1024") | "1024x1024" |
| number | Number of images to generate | 1 |

Example usage in a GPTScript:

```
tools: github.com/schuttpj/my-image-gen-google

Generate an image of a serene mountain landscape with a lake reflecting the sunset.
Use high quality settings.

Parameters:
- model: imagen-3.0-generate-002
- size: 1024x1024
```

## Authentication

A Google Gemini API key is required. When running with GPTScript, the credential tool will prompt you to provide a key if not already set. You can also set it as an environment variable:

```
export GEMINI_API_KEY="your_gemini_api_key_here"
```

## Direct CLI Usage

You can also use the tool directly from the command line:

```
python cli.py --api-key YOUR_GEMINI_API_KEY --prompt "Your text prompt here" --model imagen-3.0-generate-002 --size 1024x1024 --number 1
```

## Testing

To test the Google Imagen integration:

```
# Set your API key
export GEMINI_API_KEY="your_gemini_api_key_here"

# Run the test script
python scripts/test-imagen.py
```

## Acknowledgments

This tool is based on the GPTScript dalle-image-generation tool and has been modified to use Google's Imagen model.
