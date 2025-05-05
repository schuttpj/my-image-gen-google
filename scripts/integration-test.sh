#!/bin/bash

echo "Running integration test for Google Imagen/Gemini image generation"

# Make sure GEMINI_API_KEY is set
if [ -z "${GEMINI_API_KEY}" ]; then
    echo "Error: GEMINI_API_KEY environment variable not set"
    echo "Please set it using: export GEMINI_API_KEY=your_api_key_here"
    exit 1
fi

# Test directory
TEST_DIR="integration-test-output"
mkdir -p $TEST_DIR

echo "1. Testing Imagen model..."
python3 cli.py --prompt="A friendly cartoon robot helping a child with homework" \
    --model="imagen-3.0-generate-002" \
    --size="1:1" \
    --number="1" > "$TEST_DIR/imagen-response.txt"

# Extract the URL from the response and save it to a file
URL=$(cat "$TEST_DIR/imagen-response.txt" | tr -d '[]"')
echo "$URL" > "$TEST_DIR/imagen-test.png"
echo "Saved Imagen test output to $TEST_DIR/imagen-test.png"

echo "2. Testing Gemini model..."
python3 cli.py --prompt="A magical forest with glowing mushrooms and fairies" \
    --model="gemini-2.0-flash-exp-image-generation" \
    --size="1:1" \
    --number="1" > "$TEST_DIR/gemini-response.txt"

# Extract the URL from the response and save it to a file
URL=$(cat "$TEST_DIR/gemini-response.txt" | tr -d '[]"')
echo "$URL" > "$TEST_DIR/gemini-test.png"
echo "Saved Gemini test output to $TEST_DIR/gemini-test.png"

echo "3. Testing story-book.gpt integration..."
# Update the .env file with NUXT_USE_GEMINI=true
if [ -f "../.env" ]; then
    # Check if NUXT_USE_GEMINI is already in the .env file
    if grep -q "NUXT_USE_GEMINI" "../.env"; then
        # Update the existing value
        sed -i '' 's/NUXT_USE_GEMINI=.*/NUXT_USE_GEMINI=true/' "../.env"
    else
        # Add the variable
        echo "NUXT_USE_GEMINI=true" >> "../.env"
    fi
else
    # Create a new .env file
    echo "NUXT_USE_GEMINI=true" > "../.env"
fi

echo "Updated .env file with NUXT_USE_GEMINI=true"
echo "Integration test complete!"
echo ""
echo "Next steps:"
echo "1. Restart the Nuxt application to apply the changes"
echo "2. Create a new story to test the integration with Google's Imagen/Gemini"
echo ""
echo "You can toggle between Google and OpenAI by changing NUXT_USE_GEMINI in the .env file" 