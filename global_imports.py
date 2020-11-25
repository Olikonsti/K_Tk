from tkinter import *
import tkinter.ttk as ttk
import pygame

pygame.init()
pygame.mixer.init(44100)

K_MODE_ITEM_LIST = []


mode = "dark"
debug_mode = False

def debug(text):
    if debug_mode:
        print("Debug: " + text)


def KDarkMode():
    debug("Toggled dark theme")
    global mode
    mode = "dark"
    for i in K_MODE_ITEM_LIST:
        try:
            i.updateTheme(mode)
        except Exception as e:
            print("KTK THEME ERROR: KDarkMode():\n" + str(e))

def KLightMode():
    debug("Toggled light theme")
    global mode
    mode = "light"
    for i in K_MODE_ITEM_LIST:
        try:
            i.updateTheme(mode)
        except Exception as e:
            print("KTK THEME ERROR: KDarkMode():\n" + str(e))

def KToggleMode():
    global mode
    debug("Toggled theme change " + mode)
    if mode == "dark":
        KLightMode()
    else:
        KDarkMode()
    debug("mode " + mode)