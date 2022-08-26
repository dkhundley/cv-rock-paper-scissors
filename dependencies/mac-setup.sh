#!/bin/bash

# Changing to root directory
cd ..

# Instantiating virtual environment
python -m venv tfod

# Activating virtual environment
source tfod/bin/activate

# Installing the required Python dependencies from PyPi
pip install -r dependencies/pip-requirements.txt