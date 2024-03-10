import os,psutil
from tkinter import Text, END, messagebox
from pathlib import Path
from loguru import logger

selected_usb_mount_path = ""
selected_usb_device_name = ""
scan_type = ""

def is_usb_device(partition):
    # Vérifie si la partition est probablement une clé USB plutôt qu'une partition système
    # Critère 1: Point de montage
    if '/media/' in partition.mountpoint:
        return True
    
    return False

def get_usb_devices():
    devices = []

    try:
        partitions = psutil.disk_partitions(all=True)
        username = Path.home().name

        for partition in partitions:
            if is_usb_device(partition):
                volume_name = os.path.basename(partition.mountpoint)
                devices.append((partition.device, volume_name, partition.mountpoint))

    except Exception as e:
        logger.error(f"Error getting USB devices: {e}")


    return devices


def display_usb_devices(canvas):
    canvas.delete("usb_text")  # Efface les anciens textes pour éviter de les empiler
    usb_devices = get_usb_devices()

    for i, (device_path, device_name, mount_path) in enumerate(usb_devices):
        x_position = 1082.0  # Choisissez la position x en fonction de votre mise en page
        y_position = 439.0 + i * 50  # Ajustez la position y en fonction de votre mise en page
        text = f"{device_name} ({mount_path})"
        # Créez le texte pour le périphérique USB avec un tag unique pour identifier l'événement de clic
        canvas.create_text(x_position, y_position, text=text, fill="white", tags=f"usb_text")
        # Liez un événement de clic à ce texte
        canvas.tag_bind(f"usb_text", "<Button-1>", lambda event, mount_path=mount_path: on_usb_device_click(mount_path, device_name))

def on_usb_device_click(mount_path, device_name):
    global selected_usb_mount_path
    global selected_usb_device_name
    selected_usb_mount_path = mount_path
    selected_device_name = device_name
    logger.info(f"USB device selected: {selected_usb_device_name}")
    logger.info(f"USB device mount path: {selected_usb_mount_path}")
    messagebox.showinfo("Info", f"USB device selected: {device_name}")

def test_select_USB():
    return selected_usb_mount_path

def list_tree_structure():
    text_widget = Text(width=50, height=17, bg='gray')  # Set the background color to gray
    text_widget.place(x=320, y=300)  # Place the Text widget at position (100, 100)

    for dirname,dirnames, filenames in os.walk(selected_usb_mount_path):
        # print path to all subdirectories first.
        for subdirname in dirnames:
            text_widget.insert(END, subdirname + '\n')  # Insert the subdirectory name into the Text widget
        # print path to all filenames.
        for filename in filenames:
            text_widget.insert(END, filename + '\n')  # Insert the filename into the Text widget

# Fonction pour mettre à jour la variable en fonction de l'état des radioButton
def update_scan_type(value):
    global scan_type
    if value == "1":
        scan_type = "fast"
    elif value == "2":
        scan_type = "complete"
    else:
        scan_type = None

def return_scan_type():
    return scan_type

def list_quarantine():
    text_widget = Text(width=50, height=17, bg='gray')  # Set the background color to gray
    text_widget.place(x=525, y=300)  # Place the Text widget at position (100, 100)

    for dirname,dirnames, filenames in os.walk(f"{os.environ['HOME']}/.clamav/quarantine/{selected_usb_device_name}"):
        # print path to all subdirectories first.
        for subdirname in dirnames:
            text_widget.insert(END, subdirname + '\n')  # Insert the subdirectory name into the Text widget
        # print path to all filenames.
        for filename in filenames:
            text_widget.insert(END, filename + '\n')  # Insert the filename into the Text widget


