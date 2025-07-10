#!/bin/bash

set -e  # Stop the script if an error occurs
set -x  # Print commands before execution

# Ensure Python and pip are installed
if ! command -v python3.9 &> /dev/null
then
    echo "Python 3.9 not found. Ensure Vercel is using the correct runtime."
    exit 1
fi

# Upgrade pip and install dependencies
python3.12 -m ensurepip --default-pip
python3.12 -m pip install --upgrade pip setuptools wheel

# Install 

python3.12 -m pip install -r requirements.txt || exit 1

# Collect static files
python3.12 manage.py collectstatic --noinput --clear || exit 1

echo "Build completed successfully."