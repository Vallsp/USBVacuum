import os, subprocess
from tkinter import Text, END

def get_usb_devices():
    devices = []
    try:
        output = subprocess.check_output(['blkid']).decode('utf-8').splitlines()

        for line in output:
            parts = line.split()
            if parts and parts[0].startswith('/dev/') and 'LABEL=' in line:
                device_path = parts[0]
                label_part = [part for part in parts if 'LABEL=' in part][0]
                volume_name = label_part.split('=')[1].strip('"')
                # Ajout de removable (à adapter si nécessaire)
                removable = 'TYPE="disk"' not in line

                devices.append((device_path, volume_name))

    except Exception as e:
        print(f"Error getting USB devices: {e}")

    return devices


def display_usb_devices(canvas):
    canvas.delete("usb_text")  # Efface les anciens textes pour éviter de les empiler
    usb_devices = get_usb_devices()
    for i, (device_path, device_name) in enumerate(usb_devices):
        x_position = 1082.0  # Choisissez la position x en fonction de votre mise en page
        y_position = 439.0 + i * 50  # Ajustez la position y en fonction de votre mise en page
        text = f"{device_name} ({device_path})"
        canvas.create_text(x_position, y_position, text=text, fill="white", tags="usb_text")


def list_tree_structure(dirname, root):
    text_widget = Text(root, width=50, height=20, bg='gray')  # Set the background color to gray
    text_widget.place(x=100, y=100)  # Place the Text widget at position (100, 100)

    for dirname, dirnames, filenames in os.walk('.'):
        # print path to all subdirectories first.
        for subdirname in dirnames:
            text_widget.insert(END, subdirname + '\n')  # Insert the subdirectory name into the Text widget
        # print path to all filenames.
        for filename in filenames:
            text_widget.insert(END, filename + '\n')  # Insert the filename into the Text widget