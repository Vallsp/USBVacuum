import os
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

window = Tk()

canvas = Canvas(
    window,
    bg = "#202020",
    height = 772,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

def list_tree_structure(directory):
    for root, dirs, files in os.walk(directory):
        level = root.replace(directory, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        sub_indent = ' ' * 4 * (level + 1)
        for file in files:
            canvas.create_text(395.0, 276.0, text=file)

