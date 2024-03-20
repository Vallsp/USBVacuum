from loguru import logger
from backend.gui import gui7
import subprocess
import sys
import os

__version__ = "Alpha 0.1"

def is_docker_installed():
    try:
        subprocess.check_output(["docker", "--version"])
        return True
    except subprocess.CalledProcessError:
        return False

def pull_docker_image():
    try:
        # Check internet connection
        response = os.system("ping -c 1 google.com")
        if response == 0:
            # Pull docker image
            os.system("docker pull clamav/clamav:unstable")
            logger.info("Docker image pulled successfully")
        else:
            logger.warning("No internet connection detected")
    except Exception as e:
        logger.error(f"An error occurred while checking internet connection: {e}")


if not is_docker_installed():
    logger.error("Docker is not installed. Please run install_dependencies.sh")
    sys.exit(1)

pull_docker_image()
gui7()
logger.info(f"Starting USBVacuum version {__version__}")