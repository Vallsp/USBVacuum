#!/bin/bash
source ./venv/bin/activate
source .env
#Set environnement display
export DISPLAY=$DISPLAY
python3 ./src/app/app.py
