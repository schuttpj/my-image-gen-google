# Custom Google Image Generation Tool for GPTScript

This tool provides a simple interface for generating images using OpenAI's DALL-E models through GPTScript. It allows you to easily integrate image generation capabilities into your GPTScript workflows.

## Features

* Supports both DALL-E 3 and DALL-E 2 models
* Configurable image size, quality, and quantity
* Easy integration with GPTScript
* Simple API key management

## Prerequisites

* Python 3.x
* OpenAI API key
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
| model | Model to use ("dall-e-3" or "dall-e-2") | "dall-e-3" |
| size | Image size (e.g., "1024x1024") | "1024x1024" |
| quality | Image quality ("standard" or "hd") | "standard" |
| number | Number of images to generate | 1 |

Example usage in a GPTScript:

```
tools: github.com/schuttpj/my-image-gen-google

Generate an image of a serene mountain landscape with a lake reflecting the sunset.
Use the dall-e-3 model with high quality.

Parameters:
- model: dall-e-3
- quality: hd
- size: 1024x1024
```

## Authentication

An OpenAI API key is required. When running with GPTScript, the credential tool will prompt you to provide a key if not already set. You can also set it as an environment variable:

```
export OPENAI_API_KEY="your-api-key-here"
```

## Direct CLI Usage

You can also use the tool directly from the command line:

```
python cli.py --api-key YOUR_API_KEY --prompt "Your text prompt here" --model dall-e-3 --size 1024x1024 --quality hd --number 1
```

## Example Images

See the examples directory for sample usage and resulting images.

## License

This project is based on the GPTScript dalle-image-generation tool and is provided under the same license.

## Acknowledgments

This tool is a customized fork of the [gptscript-ai/dalle-image-generation](https://github.com/gptscript-ai/dalle-image-generation) repository.
