from .global_imports import *

class KFrame(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)

        self.BG_DARK = "#202020"
        self.FG_DARK = "red"

        self.FG_LIGHT = "black"
        self.BG_LIGHT = "#d6d6d6"

        self.config(width=20, height=10)

        K_MODE_ITEM_LIST.append(self)

    def updateTheme(self, mode_):
        if mode_ == "dark":
            self.bg = self.BG_DARK
            self.fg = self.FG_DARK
        else:
            self.fg = self.FG_LIGHT
            self.bg = self.BG_LIGHT
        self.config(bg=self.bg)