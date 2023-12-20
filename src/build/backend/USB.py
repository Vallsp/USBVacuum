from pathlib import Path
import psutil , platform, ctypes
import platform
from tkinter import Canvas, Tk

def get_usb_devices():
    devices = []
    for device in psutil.disk_partitions():
        if 'removable' in device.opts:
            device_info = psutil.disk_usage(device.device)
            volume_name = get_volume_name(device.device)
            devices.append((device.device, volume_name))
    return devices

# Fonction pour obtenir le nom du volume sur Windows
def get_volume_name(device_path):
    if platform.system() == 'Windows':
        try:
            volume_name_buffer = ctypes.create_unicode_buffer(1024)
            ctypes.windll.kernel32.GetVolumeInformationW(
                device_path + '\\',
                volume_name_buffer,
                ctypes.sizeof(volume_name_buffer),
                None,
                None,
                None,
                None,
                0
            )
            return volume_name_buffer.value
        except Exception as e:
            print(f"Error getting volume name: {e}")
            return "Unknown"
    else:
        return "Unknown"


def display_usb_devices(canvas):
    canvas.delete("usb_text")  # Efface les anciens textes pour éviter de les empiler
    usb_devices = get_usb_devices()
    for i, (device_path, device_name) in enumerate(usb_devices):
        x_position = 1082.0  # Choisissez la position x en fonction de votre mise en page
        y_position = 439.0 + i * 50  # Ajustez la position y en fonction de votre mise en page
        text = f"{device_name} ({device_path})"
        canvas.create_text(x_position, y_position, text=text, fill="white", tags="usb_text")