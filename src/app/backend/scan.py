from tkinter import Text, END, messagebox
import os
from loguru import logger

def do_scan(scan_type, usb_path):
    if not os.path.exists(f"{os.environ['HOME']}/.clamav/quarantine"):
        os.makedirs(f"{os.environ['HOME']}/.clamav/quarantine")
    if scan_type == 'complete':
        logger.info(f"Scanning {usb_path} with {scan_type} scan type.")
        complete_scan(usb_path)
    elif scan_type == 'fast':
        logger.info(f"Scanning {usb_path} with {scan_type} scan type.")
        fast_scan(usb_path)
    else:
        logger.error("No scan type selected.")
        messagebox.showerror("Error", "Please select a scan type.")

def fast_scan(usb_path):
    os.system(f'docker run -it --rm --mount type=bind,source={usb_path},target=/scandir --mount type=bind,source=$HOME/.clamav/quarantine/,target=/quarantinedir clamav/clamav:unstable clamscan -r --move /quarantinedir --max-filesize=100M /scandir')
    logger.info(f"Fast scan finished.")

def complete_scan(usb_path):
    os.system(f'docker run -it --rm --mount type=bind,source={usb_path},target=/scandir --mount type=bind,source=$HOME/.clamav/quarantine/,target=/quarantinedir clamav/clamav:unstable clamscan -r --move /quarantinedir /scandir')
    logger.info(f"Complete scan finished.")
