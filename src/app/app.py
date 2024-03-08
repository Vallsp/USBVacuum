from loguru import logger
from backend.gui import gui7

__version__ = "Alpha 0.1"

logger.info(f"Starting USBVacuum version {__version__}")

if __name__ == "__main__":
    gui7()