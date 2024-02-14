from tkinter import Text, END, messagebox
import os
from loguru import logger

def do_scan(scan_type, usb_path):
    if scan_type == 'complete':
        logger.info(f"Scanning {usb_path} with {scan_type} scan type.")
        complete_scan(usb_path)
    elif scan_type == 'fast':
        logger.info(f"Scanning {usb_path} with {scan_type} scan type.")
        fast_scan(usb_path)
    else:
        logger.error("No scan type selected.")
        messagebox.showerror("Erreur", "Please select a scan type.")

def fast_scan(usb_path):
    os.system(f'clamscan -r --max-filesize=100M {usb_path}')

def complete_scan(usb_path):
    os.system(f'clamscan -r {usb_path}')
