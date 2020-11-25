from .global_imports import *
from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk

class KIcon():
    def __init__(self, canvas, image, resx, resy):
        self.img = self.Sprite(image, resx, resy)

    def Sprite(self, picture, res1, res2):
        im = Image.open(picture).convert("RGBA").resize((res1, res2), Image.BOX)
        pic = ImageTk.PhotoImage(im)
        cor = Image.open(picture)
        return pic
