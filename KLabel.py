from .global_imports import *


class KLabel(Label):
    def __init__(self, parent, *args, **kwargs):
        Label.__init__(self, parent, font="Calibri 11", justify=LEFT, *args, **kwargs)

        self.BG_DARK = "#202020"
        self.FG_DARK = "#45c49d"

        self.FG_LIGHT = "black"
        self.BG_LIGHT = "#d6d6d6"

        K_MODE_ITEM_LIST.append(self)

    def updateTheme(self, mode_):
        if mode_ == "dark":
            self.bg = self.BG_DARK
            self.fg = self.FG_DARK
        else:
            self.fg = self.FG_LIGHT
            self.bg = self.BG_LIGHT
        self.config(bg=self.bg, fg=self.fg)