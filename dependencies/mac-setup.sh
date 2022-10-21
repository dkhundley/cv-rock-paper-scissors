#!/bin/bash

# Changing to root directory
cd ..

# Instantiating virtual environment
python3 -m venv venv

# Activating virtual environment
source venv/bin/activate

# Installing the required Python dependencies from PyPi
pip install -r dependencies/pip-requirements.txt