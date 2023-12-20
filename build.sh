#!/bin/bash

# BEGIN: Load virtual environment
source env/bin/activate
# END: Load virtual environment

OUTPUT_DIR="./src/test"

# BEGIN: Check if tkdesigner is installed
if ! [ -x "$(command -v tkdesigner)" ]; then
  echo "Error: tkdesigner is not installed." >&2
  exit 1
fi

# BEGIN: Check if .env file exists
if [ ! -f .env ]; then
  echo "Error: .env file not found."
  exit 1
fi
# END: Check if .env file exists

# BEGIN: Load environment variables from .env file
source .env
# END: Load environment variables from .env file

# BEGIN: Build the application
tkdesigner $FIGMA_URL $FIGMA_TOKEN -o $OUTPUT_DIR
# END: Build the application
