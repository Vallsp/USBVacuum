from tkinter import END, messagebox, Tk
import os
from loguru import logger
from backend.USB import selected_usb_device_name
#from datetime import datetime

def do_scan(scan_type, usb_path, gui3):

    if not os.path.exists(f"{os.environ['HOME']}/.clamav/quarantine"):
        os.makedirs(f"{os.environ['HOME']}/.clamav/quarantine")
    if scan_type == 'complete':
        #current_datetime = datetime.now()
        #formatted_datetime = current_datetime.strftime("%Y_%m_%d_%H_%M_%S")
        if not os.path.exists(f"{os.environ['HOME']}/.clamav/quarantine/{selected_usb_device_name}"):
            os.makedirs(f"{os.environ['HOME']}/.clamav/quarantine/{selected_usb_device_name}")
        logger.info(f"Scanning {usb_path} with {scan_type} scan type.")
        complete_scan(usb_path)
    elif scan_type == 'fast':
        #current_datetime = datetime.now()
        #formatted_datetime = current_datetime.strftime("%Y_%m_%d_%H_%M_%S")
        if not os.path.exists(f"{os.environ['HOME']}/.clamav/quarantine/{selected_usb_device_name}"):
            os.makedirs(f"{os.environ['HOME']}/.clamav/quarantine/{selected_usb_device_name}")
        logger.info(f"Scanning {usb_path} with {scan_type} scan type.")
        fast_scan(usb_path)
    else:
        logger.error("No scan type selected.")
        messagebox.showerror("Error", "Please select a scan type.")
        return

    

def fast_scan(usb_path):
    try:
        os.system(f'docker run -it --rm --mount type=bind,source={usb_path},target=/scandir --mount type=bind,source=$HOME/.clamav/quarantine/,target=/quarantinedir clamav/clamav:unstable clamscan -r --move /quarantinedir --max-filesize=100M /scandir')
        logger.info(f"Fast scan finished.")
    except Exception as e:
        logger.error(f"Error in fast scan: {e}")


def complete_scan(usb_path):
    try:
        os.system(f'docker run -it --rm --mount type=bind,source={usb_path},target=/scandir --mount type=bind,source=$HOME/.clamav/quarantine/,target=/quarantinedir clamav/clamav:unstable clamscan -r --move /quarantinedir /scandir')
        logger.info(f"Complete scan finished.")
    except Exception as e:
        logger.error(f"Error in complete scan: {e}")
