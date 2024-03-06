#!/bin/bash

# Check if the script is run with internet connection
if ping -q -c 1 -W 1 google.com >/dev/null; then
    echo "Internet connection detected"
else
    echo "No internet connection detected"
    exit
fi

# Check if script is run as root
if [ "$EUID" -eq 0 ]
    then echo "Please do not run as root"
    exit
fi

#Install packages
sudo apt install python3 python3-tk python3-venv python3-pip docker.io -y

#Add user to docker group
sudo usermod -aG docker $USER

#Pull the clamav docker image
sudo docker pull clamav/clamav:unstable

# Create a Python virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

echo "Dependencies installed"
echo "Please reboot your system to apply changes"