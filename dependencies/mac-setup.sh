#!/bin/bash

# Changing to root directory
cd ..

# Instantiating virtual enviornment
python -m venv tfod

# Activating virtual enviornment
source tfod/bin/activate

# Installing the required Python dependencies from PyPi
pip install -r dependencies/pip-requirements.txt