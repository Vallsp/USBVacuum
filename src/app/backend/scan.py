from tkinter import Text, END, messagebox
import os

def do_scan(scan_type, usb_path):
    if scan_type == 'complete':
        complete_scan(usb_path)
    elif scan_type == 'fast':
        fast_scan(usb_path)
    else:
        messagebox.showerror("Erreur", "Please select a scan type.")

def fast_scan(usb_path):
    os.system(f'clamscan -r --max-filesize=100M {usb_path}')

def complete_scan(usb_path):
    os.system(f'clamscan -r {usb_path}')
