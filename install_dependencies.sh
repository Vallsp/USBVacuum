#!/bin/bash

# Check if script is run as root
if [ "$EUID" -eq 0 ]
    then echo "Please do not run as root"
    exit
fi

#Install packages
sudo apt install python3 python3-tk python3-venv python3-pip clamav -y

# Create a Python virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

#Install packages
sudo apt install python3 python3-tk python3-venv python3-pip clamav -y

# Create a Python virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install requirements
pip install -r requirements.txt
