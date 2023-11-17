from tkinter import Tk, Canvas, Button, PhotoImage, Listbox, Scrollbar, messagebox
from pathlib import Path
from backend import USBBackend

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("/home/vallsp/Bureau/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class USBApp:
    def __init__(self, root, backend):
        self.root = root
        self.backend = backend

        self.root.geometry("1409x735")
        self.root.configure(bg="#9C9BC0")
        self.root.resizable(False, False)

        window_width = self.root.winfo_reqwidth()
        window_height = self.root.winfo_reqheight()
        position_x = (self.root.winfo_screenwidth() - window_width) // 2
        position_y = (self.root.winfo_screenheight() - window_height) // 2
        self.root.geometry(f"+{position_x}+{position_y}")

        self.canvas = Canvas(
            self.root,
            bg="#9C9BC0",
            height=735,
            width=1409,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            1.94097900390625,
            0.0660400390625,
            1408.2139282226562,
            157.73916625976562,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_text(
            57.0,
            17.0,
            anchor="nw",
            text="USBVaccum",
            fill="#000000",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
            587.0,
            82.0,
            anchor="nw",
            text="2 - Scanning",
            fill="#000000",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
            963.0,
            82.0,
            anchor="nw",
            text="3 - Reporting",
            fill="#000000",
            font=("Inter", 24 * -1)
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            self.canvas,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.perform_action,
            relief="flat"
        )
        self.button_1.place(
            x=211.0,
            y=79.0,
            width=220.0,
            height=38.0
        )

        self.canvas.create_text(
            703.5,
            211.0,
            anchor="n",
            text="Select your device :",
            fill="#000000",
            font=("Inter", 24 * -1)
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            self.canvas,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.execute_selected_device_action,
            relief="flat"
        )
        self.button_2.place(
            x=683.5,
            y=621.0,
            width=217.0,
            height=50.0
        )

        self.listbox = Listbox(self.root, selectmode="single")
        self.listbox.place(x=663.5, y=250.0, width=400.0, height=300.0)

        scrollbar = Scrollbar(self.root, command=self.listbox.yview)
        scrollbar.place(x=1063.5, y=250.0, height=300.0)
        self.listbox.config(yscrollcommand=scrollbar.set)

        self.update_usb_devices()

    def update_usb_devices(self):
        appareils_usb = self.backend.detect_usb_devices()
        self.listbox.delete(0, "end")
        for appareil in appareils_usb:
            self.listbox.insert("end", appareil)
        self.root.after(1000, self.update_usb_devices)

    def execute_selected_device_action(self):
        selected_index = self.listbox.curselection()
        if not selected_index:
            messagebox.showinfo("Information", "Veuillez sélectionner un appareil.")
            return

        selected_device = self.listbox.get(selected_index)
        # Remplacez cette action factice par l'action réelle que vous souhaitez effectuer
        messagebox.showinfo("Action sur l'appareil", f"Action effectuée sur l'appareil : {selected_device}")

    def perform_action(self):
        # Cette méthode peut être utilisée pour une action différente sur le bouton_1 si nécessaire
        print("button_1 clicked")


if __name__ == "__main__":
    backend = USBBackend()
    root = Tk()
    app = USBApp(root, backend)
    root.mainloop()