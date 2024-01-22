#!/bin/bash

# Replace these variables with your project-specific values

VENV_DIR="./env"


# Create a virtual environment
python3 -m venv $VENV_DIR
source $VENV_DIR/bin/activate

# Install project dependencies and configure Django settings
# cd $PROJECT_DIR
# pip install -r requirements.txt

# Start Django development server
python manage.py runserver 