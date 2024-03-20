from tkinter import END, messagebox, Tk
import os, threading
from loguru import logger
from backend.USB import test_select_name
#from datetime import 

scan_finished = threading.Event()

def do_scan(scan_type, usb_path):
    device_name = test_select_name()
    if not os.path.exists(f"{os.environ['HOME']}/.clamav/quarantine"):
        os.makedirs(f"{os.environ['HOME']}/.clamav/quarantine")
    if scan_type == 'complete':
        if not os.path.exists(f"{os.environ['HOME']}/.clamav/quarantine/{device_name}"):
            os.makedirs(f"{os.environ['HOME']}/.clamav/quarantine/{device_name}")
        logger.info(f"Scanning {usb_path} with {scan_type} scan type.")
        complete_scan(usb_path)
    elif scan_type == 'fast':
        if not os.path.exists(f"{os.environ['HOME']}/.clamav/quarantine/{device_name}"):
            os.makedirs(f"{os.environ['HOME']}/.clamav/quarantine/{device_name}")
        logger.info(f"Scanning {usb_path} with {scan_type} scan type.")
        fast_scan(usb_path)
    else:
        logger.error("No scan type selected.")
        messagebox.showerror("Error", "Please select a scan type.")
        return

    

def fast_scan(usb_path):
    device_name = test_select_name()
    try:
        os.system(f'docker run -it --rm --mount type=bind,source={usb_path},target=/scandir --mount type=bind,source=$HOME/.clamav/quarantine/{device_name},target=/quarantinedir clamav/clamav:unstable clamscan -r --move /quarantinedir --max-filesize=100M /scandir')
        logger.info(f"Fast scan finished.")
        scan_finished.set()
    except Exception as e:
        logger.error(f"Error in fast scan: {e}")
        


def complete_scan(usb_path):
    device_name = test_select_name()
    try:
        os.system(f'docker run -it --rm --mount type=bind,source={usb_path},target=/scandir --mount type=bind,source=$HOME/.clamav/quarantine/{device_name},target=/quarantinedir clamav/clamav:unstable clamscan -r --move /quarantinedir /scandir')
        logger.info(f"Complete scan finished.")
    except Exception as e:
        logger.error(f"Error in complete scan: {e}")
    finally:
        # Définir l'Event pour signaler la fin de la numérisation
        scan_finished.set()