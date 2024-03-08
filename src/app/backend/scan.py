from tkinter import END, messagebox
import os
from loguru import logger
from datetime import datetime

def do_scan(scan_type, usb_path, gui5, gui3):
    if not os.path.exists(f"{os.environ['HOME']}/.clamav/quarantine"):
        os.makedirs(f"{os.environ['HOME']}/.clamav/quarantine")
    if scan_type == 'complete':
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y_%m_%d_%H_%M_%S")
        if not os.path.exists(f"{os.environ['HOME']}/.clamav/quarantine/{usb_path}"):
            os.makedirs(f"{os.environ['HOME']}/.clamav/quarantine/{usb_path}")
        logger.info(f"Scanning {usb_path} with {scan_type} scan type.")
        complete_scan(usb_path, gui3)
    elif scan_type == 'fast':
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y_%m_%d_%H_%M_%S")
        if not os.path.exists(f"{os.environ['HOME']}/.clamav/quarantine/{usb_path}"):
            os.makedirs(f"{os.environ['HOME']}/.clamav/quarantine/{usb_path}")
        logger.info(f"Scanning {usb_path} with {scan_type} scan type.")
        fast_scan(usb_path, gui3)
    else:
        logger.error("No scan type selected.")
        messagebox.showerror("Error", "Please select a scan type.")

def fast_scan(usb_path, gui3):
    os.system(f'docker run -it --rm --mount type=bind,source={usb_path},target=/scandir --mount type=bind,source=$HOME/.clamav/quarantine/,target=/quarantinedir clamav/clamav:unstable clamscan -r --move /quarantinedir --max-filesize=100M /scandir')
    logger.info(f"Fast scan finished.")
    gui3()

def complete_scan(usb_path, gui3):
    os.system(f'docker run -it --rm --mount type=bind,source={usb_path},target=/scandir --mount type=bind,source=$HOME/.clamav/quarantine/,target=/quarantinedir clamav/clamav:unstable clamscan -r --move /quarantinedir /scandir')
    logger.info(f"Complete scan finished.")
    gui3()
 
