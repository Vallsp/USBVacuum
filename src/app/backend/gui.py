from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Radiobutton, messagebox
from loguru import logger
from backend.USB import list_tree_structure, test_select_USB, return_scan_type, update_scan_type, display_usb_devices, list_quarantine, return_scan_type # Importation des fonctions depuis backend
from backend.scan import do_scan, scan_finished
import threading

window = Tk()
window.geometry("1440x772")
# window.attributes("-fullscreen", True)
window.configure(bg="#202020")

window.title("USBVacuum")
# window.iconbitmap(OUTPUT_PATH / Path(r"./assets/icon.ico"))

current_interface = None

window.resizable(False, False)

OUTPUT_PATH = Path(__file__).parent

def switch_to_interface(interface_name):
        # if current_interface:
        #     current_interface.destroy()  # Détruit l'interface actuelle

        #Ajout de la vérification de l'USB ici
        if interface_name == "gui6" and test_select_USB() == '': 
           logger.error("No storage device selected.")
           messagebox.showerror("Error", "Please select a storage device.")
           return
        
        # if interface_name == "gui5" and scan_type() == '':
        #     logger.error("No scan type selected.")
        #     messagebox.showerror("Error", "Please select a scan type.")
        #     return

        # Appelle la fonction correspondant à l'interface sélectionnée
        interfaces[interface_name]()

def gui():
    canvas = Canvas(
        window,
        bg="#202020",
        height=772,
        width=1440,
        bd=0,
        highlightthickness=0,
        relief="ridge"
        )
    canvas.place(x=0, y=0)

    canvas.delete("all")  # Supprime tous les éléments actuels sur le Canvas
    ASSETS_PATH = OUTPUT_PATH / Path(r"../assets/frame0")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
    
    #------------------------------------------down-code gui-down---------------------------

    image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        1117.0,
        590.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        1118.0,
        314.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        442.0,
        401.0,
        image=image_image_3
    )

    #------------------------------------------up-code gui-up-------------------------------
    

    window.resizable(False, False)
    window.mainloop()

def gui1():
    canvas = Canvas(
        window,
        bg="#202020",
        height=772,
        width=1440,
        bd=0,
        highlightthickness=0,
        relief="ridge"
        )
    canvas.place(x=0, y=0)

    canvas.delete("all")  # Supprime tous les éléments actuels sur le Canvas
    ASSETS_PATH = OUTPUT_PATH / Path(r"../assets/frame1")

    def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)
    #------------------------------------------down-code gui-down---------------------------

    image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        1117.0,
        590.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        1118.0,
        314.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        442.0,
        401.0,
        image=image_image_3
    )

    #------------------------------------------up-code gui-up-------------------------------
    def wait_switch_gui():
            window.after(3000,switch_to_interface, "gui")
    
    thread3 = threading.Thread(target=wait_switch_gui)
    thread3.start()

    window.resizable(False, False)
    window.mainloop()

def gui2():

    canvas = Canvas(
        window,
        bg="#202020",
        height=772,
        width=1440,
        bd=0,
        highlightthickness=0,
        relief="ridge"
        )
    canvas.place(x=0, y=0)

    canvas.delete("all")  # Supprime tous les éléments actuels sur le Canvas
    ASSETS_PATH = OUTPUT_PATH / Path(r"../assets/frame2")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
    
    #------------------------------------------down-code gui-down---------------------------

    image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        1117.0,
        590.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        1118.0,
        314.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        442.0,
        401.0,
        image=image_image_3
    )

    #------------------------------------------up-code gui-up-------------------------------
    

    window.resizable(False, False)
    window.mainloop()

def gui3():

    canvas = Canvas(
        window,
        bg="#202020",
        height=772,
        width=1440,
        bd=0,
        highlightthickness=0,
        relief="ridge"
        )
    canvas.place(x=0, y=0)

    canvas.delete("all")  # Supprime tous les éléments actuels sur le Canvas
    ASSETS_PATH = OUTPUT_PATH / Path(r"../assets/frame3")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
    
    #------------------------------------------down-code gui-down---------------------------

    image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        720.0,
        81.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        1348.0,
        81.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        116.0,
        81.0,
        image=image_image_3
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=946.0,
        y=33.0,
        width=335.0,
        height=114.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=580.0,
        y=24.0,
        width=335.0,
        height=114.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=241.0,
        y=24.0,
        width=335.0,
        height=114.0
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        724.0,
        429.0,
        image=image_image_4
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switch_to_interface("gui1"),
        relief="flat"
    )
    button_4.place(
        x=594.0,
        y=660.0,
        width=251.0,
        height=62.0
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        718.0,
        340.0,
        image=image_image_5
    )

    #------------------------------------------up-code gui-up-------------------------------
    list_quarantine()

    window.resizable(False, False)
    window.mainloop()
    
def gui4():
    canvas = Canvas(
        window,
        bg="#202020",
        height=772,
        width=1440,
        bd=0,
        highlightthickness=0,
        relief="ridge"
        )
    canvas.place(x=0, y=0)

    canvas.delete("all")  # Supprime tous les éléments actuels sur le Canvas
    ASSETS_PATH = OUTPUT_PATH / Path(r"../assets/frame4")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
    #------------------------------------------down-code gui-down---------------------------

    image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        720.0,
        81.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        1348.0,
        81.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        116.0,
        81.0,
        image=image_image_3
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=946.0,
        y=33.0,
        width=335.0,
        height=114.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=580.0,
        y=24.0,
        width=335.0,
        height=114.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=241.0,
        y=24.0,
        width=335.0,
        height=114.0
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        1082.0,
        439.0,
        image=image_image_4
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=990.8837890625,
        y=663.6064453125,
        width=181.2318878173828,
        height=69.78723907470703
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        1083.0,
        199.0,
        image=image_image_5
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        383.0,
        472.0,
        image=image_image_6
    )

    #------------------------------------------up-code gui-up-------------------------------

    window.resizable(False, False)
    window.mainloop()
    
def gui5():
    canvas = Canvas(
        window,
        bg="#202020",
        height=772,
        width=1440,
        bd=0,
        highlightthickness=0,
        relief="ridge"
        )
    canvas.place(x=0, y=0)
    canvas.delete("all")  # Supprime tous les éléments actuels sur le Canvas
    ASSETS_PATH = OUTPUT_PATH / Path(r"../assets/frame5")

    def relative_to_assets(path: str) -> Path:
          return ASSETS_PATH / Path(path)
    #------------------------------------------down-code gui-down---------------------------

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        720.0,
        311.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        735.0,
        618.0,
        image=image_image_2
    )

    #------------------------------------------up-code-gui-up------------------------------
    def wait_switch_gui3():
            scan_finished.wait()
            window.after(0,switch_to_interface, "gui3")
    
    thread2 = threading.Thread(target=wait_switch_gui3)
    thread2.start()


    window.mainloop()   
    window.resizable(False, False)


def gui6():
        canvas = Canvas(
        window,
        bg="#202020",
        height=772,
        width=1440,
        bd=0,
        highlightthickness=0,
        relief="ridge"
        )
        canvas.place(x=0, y=0)

        canvas.delete("all")  # Supprime tous les éléments actuels sur le Canvas
        ASSETS_PATH = OUTPUT_PATH / Path(r"../assets/frame6")

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)
        
        global scan_type
#------------------------------------------down-code gui-down---------------------------
        image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            720.0,
            81.0,
            image=image_image_1
            )

        image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = canvas.create_image(
            116.0,
            81.0,
            image=image_image_2
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        image_3 = canvas.create_image(
            720.0,
            429.0,
            image=image_image_3
        )

        image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        image_4 = canvas.create_image(
            1348.0,
            81.0,
            image=image_image_4
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: makeScan(),
            relief="flat"
        )
        button_1.place(
            x=629.0,
            y=677.0,
            width=183.0,
            height=62.0
        )

        image_image_5 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        image_5 = canvas.create_image(
            1110.0,
            81.0,
            image=image_image_5
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        button_2.place(
            x=586.0,
            y=37.0,
            width=335.0,
            height=89.0
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: switch_to_interface("gui7"),
            relief="flat"
        )
        button_3.place(
            x=233.0,
            y=19.0,
            width=335.0,
            height=114.0
        )

        image_image_6 = PhotoImage(
            file=relative_to_assets("image_6.png"))
        image_6 = canvas.create_image(
            960.0,
            276.0,
            image=image_image_6
        )

        image_image_7 = PhotoImage(
            file=relative_to_assets("image_7.png"))
        image_7 = canvas.create_image(
            960.0,
            354.0,
            image=image_image_7
        )

        image_image_8 = PhotoImage(
            file=relative_to_assets("image_8.png"))
        image_8 = canvas.create_image(
            960.0,
            561.0,
            image=image_image_8
        )

        image_image_9 = PhotoImage(
            file=relative_to_assets("image_9.png"))
        image_9 = canvas.create_image(
            395.0,
            276.0,
            image=image_image_9
        )
#------------------------------------------up-code gui-up---------------------------
        scan_type_var = None
        list_tree_structure()

        # Définition des Radiobuttons
        fast_scan_radio = Radiobutton(window, variable=scan_type_var, value=1, command=lambda: update_scan_type("1"))
        fast_scan_radio.place(x=1050, y=320)

        complete_scan_radio = Radiobutton(window, variable=scan_type_var, value=2, command=lambda: update_scan_type("2"))
        complete_scan_radio.place(x=1050, y=370)

        
        def makeScan():
            if return_scan_type() == 'complete' or return_scan_type() == 'fast':
                global terminate_thread
                terminate_thread = False
                thread1 = threading.Thread(target=do_scan, args=(return_scan_type(), test_select_USB()))
                thread1.start()
                switch_to_interface("gui5")
                
            else:
                logger.error("No scan type selected.")
                messagebox.showerror("Error", "Please select a scan type.")
                return


        window.resizable(False, False)
        window.mainloop()
    
def gui7():
        canvas = Canvas(
        window,
        bg="#202020",
        height=772,
        width=1440,
        bd=0,
        highlightthickness=0,
        relief="ridge"
        )
        canvas.place(x=0, y=0)

        canvas.delete("all")  # Supprime tous les éléments actuels sur le Canvas
        ASSETS_PATH = OUTPUT_PATH / Path(r"../assets/frame7")

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)
#------------------------------------------down-code gui-down---------------------------
        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            720.0,
            81.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = canvas.create_image(
            116.0,
            81.0,
            image=image_image_2
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        image_3 = canvas.create_image(
            1082.0,
            439.0,
            image=image_image_3
        )

        image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        image_4 = canvas.create_image(
            1348.0,
            81.0,
            image=image_image_4
        )

        image_image_5 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        image_5 = canvas.create_image(
            757.0,
            89.0,
            image=image_image_5
        )

        image_image_6 = PhotoImage(
            file=relative_to_assets("image_6.png"))
        image_6 = canvas.create_image(
            1102.0,
            89.0,
            image=image_image_6
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: switch_to_interface("gui6"),
            relief="flat"
        )
        button_1.place(
            x=990.884033203125,
            y=663.6063842773438,
            width=181.2318878173828,
            height=69.78723907470703
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: gui3(),
            relief="flat"
        )
        button_2.place(
            x=233.0,
            y=45.0,
            width=316.0,
            height=89.0
        )

        image_image_7 = PhotoImage(
            file=relative_to_assets("image_7.png"))
        image_7 = canvas.create_image(
            383.0,
            472.0,
            image=image_image_7
        )

        image_image_8 = PhotoImage(
            file=relative_to_assets("image_8.png"))
        image_8 = canvas.create_image(
            1081.0,
            201.0,
            image=image_image_8
        )
    
#------------------------------------------up-code gui-up---------------------------

        
        # Fonction pour mettre à jour l'affichage toutes les secondes
        def update_display():
            display_usb_devices(canvas)
            window.after(1000, update_display)  # Planifie la prochaine mise à jour après 1000 millisecondes (1 seconde)

        # Appel de la fonction pour mettre à jour l'affichage toutes les secondes
        update_display()

        window.resizable(False, False)
        window.mainloop()


interfaces = {
    "gui": gui,
    "gui1": gui1,
    "gui2": gui2,
    "gui3": gui3,
    "gui4": gui4,
    "gui5": gui5,
    "gui6": gui6,
    "gui7": gui7,
    }