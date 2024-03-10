#!/bin/bash

# It actually does not update definitions, but instead pulling the latest docker image available
# It also checks if the user is a member of the docker group

if ping -q -c 1 -W 1 google.com >/dev/null; then
    if groups | grep -q docker; then
        echo "Internet connection detected"
        docker pull clamav/clamav:unstable
    else
        echo "User is not a member of the docker group, have you run the install_dependencies.sh script?"
    fi
else
    echo "No internet connection"
fi
