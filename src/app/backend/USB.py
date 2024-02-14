import os,psutil
from tkinter import Text, END, messagebox
from pathlib import Path

selected_usb_mount_path = ""
scan_type_var = 0
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
        print(f"Error getting USB devices: {e}")


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
    selected_usb_mount_path = mount_path
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

# Fonction pour mettre à jour la variable scan_type en fonction de l'état des radioButton
def update_scan_type():
        global scan_type
        if scan_type_var == 1:
            scan_type = "fast"
            print(scan_type)
        elif scan_type_var == 2:
            scan_type = "complete"
            print(scan_type)
        else:
            scan_type = None