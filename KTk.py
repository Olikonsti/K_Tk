from .global_imports import *

class KTk(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.BG_DARK = "#202020"
        self.FG_DARK = "red"

        self.FG_LIGHT = "black"
        self.BG_LIGHT = "#d6d6d6"


        self.geometry("700x500")
        self.title("APP:VERSION")
        self.resizable(False, False)

        K_MODE_ITEM_LIST.append(self)

    def updateTheme(self, mode_):
        if mode_ == "dark":
            self.bg = self.BG_DARK
            self.fg = self.FG_DARK
        else:
            self.fg = self.FG_LIGHT
            self.bg = self.BG_LIGHT
        self.config(bg=self.bg)
