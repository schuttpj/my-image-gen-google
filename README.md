# Google Imagen/Gemini Image Generation Tool

This GPTScript tool allows you to generate images using Google's Imagen and Gemini image generation models. It can be used as a standalone tool or integrated with the story-book application.

## Features

- Support for Google's Imagen 3 model (`imagen-3.0-generate-002`)
- Support for Google's Gemini model (`gemini-2.0-flash-exp-image-generation`)
- Configurable image aspect ratio (1:1, 16:9, etc.)
- Adjustable number of images to generate
- Direct integration with the story-book.gpt script

## Prerequisites

- Python 3.8 or higher
- A Google API key with access to Imagen/Gemini models
- Required Python packages (see requirements.txt)

## Installation

1. Clone this repository
2. Install the required dependencies:

```bash
cd my-dalle-tool
pip install -r requirements.txt
```

3. Set your Google API key as an environment variable:

```bash
export GEMINI_API_KEY=your_api_key_here
```

## Usage

### Command Line Interface

Generate an image using the default Gemini model:

```bash
python cli.py --prompt="A serene lake at sunset with mountains in the background"
```

Generate an image using Imagen with specific parameters:

```bash
python cli.py --prompt="A spaceship flying through a nebula" --model="imagen-3.0-generate-002" --size="16:9" --number="2"
```

### Integration with story-book

To use this tool with the story-book application:

1. Make sure the tool is referenced in your `story-book.gpt` file
2. Set the `NUXT_USE_GEMINI` environment variable in your `.env` file:

```
NUXT_USE_GEMINI=true
```

3. Ensure your `GEMINI_API_KEY` is set in the environment

## Testing

You can run the integration test script to verify everything is working:

```bash
cd my-dalle-tool
./scripts/integration-test.sh
```

This will test both Imagen and Gemini models and update the `.env` file to use Google's models.

## Differences from OpenAI's DALL-E

1. Google's API returns base64-encoded images rather than URLs
2. The format for specifying image size is different (aspect ratio vs. dimensions)
3. Different model names and capabilities
4. The story-book application has been modified to handle both formats

## Troubleshooting

- If you encounter "API key not valid" errors, make sure your `GEMINI_API_KEY` is set correctly
- If image generation fails, check that you have access to the Imagen/Gemini models in your Google API account
- For more issues, run the test script in the `scripts` directory to diagnose problems

## License

This project is licensed under the MIT License - see the LICENSE file for details.
