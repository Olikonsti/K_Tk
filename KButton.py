from .global_imports import *


class KButton(Frame):
    def __init__(self, parent, command=lambda: print("UNDEFINED BUTTON COMMAND"), text="UNDEFINED", *args, **kwargs):
        Frame.__init__(self, parent, highlightthickness=1, *args, **kwargs)
        self.command = command

        self.text = Label(self, text=text)
        self.text.pack(padx=2, pady=2)

        self.BG_DARK = "#202020"
        self.FG_DARK = "#34856c"

        self.FG_LIGHT = "black"
        self.BG_LIGHT = "#d6d6d6"

        # hover
        self.BG_DARK_HOVER = "#2B2B2B"
        self.BG_LIGHT_HOVER = "grey"

        self.BORDER_DARK = "#2B2B2B"
        self.BORDER_LIGHT = "grey"

        self.BORDER_DARK_HOVER = "#34856c"
        self.BORDER_LIGHT_HOVER = "#34856c"

        K_MODE_ITEM_LIST.append(self)

        self.bind('<Enter>', self.hover)
        self.text.bind('<Enter>', self.hover)
        self.bind('<Leave>', self.leave)
        self.bind('<Button-1>', self.click)
        self.text.bind('<Button-1>', self.click)

        self.after(100, self.leave)

    def hover(self, event=None):
        if self.mode == "dark":
            self.config(bg=self.BG_DARK_HOVER, highlightbackground=self.BORDER_DARK_HOVER)
            self.text.config(bg=self.BG_DARK_HOVER)
        else:
            self.config(bg=self.BG_LIGHT_HOVER, highlightbackground=self.BORDER_LIGHT_HOVER)
            self.text.config(bg=self.BG_LIGHT_HOVER)

        self.text.pack(padx=2, pady=2)

    def leave(self, event=None):
        if self.mode == "dark":
            self.config(bg=self.BG_DARK, highlightbackground=self.BORDER_DARK)
            self.text.config(bg=self.BG_DARK)
        else:
            self.config(bg=self.BG_LIGHT, highlightbackground=self.BORDER_LIGHT)
            self.text.config(bg=self.BG_LIGHT)

        self.text.pack(padx=2, pady=2)

    def click(self, event=None):
        self.command()
        self.text.pack(padx=2, pady=2)

    def updateTheme(self, mode_):
        self.mode = mode_
        if mode_ == "dark":
            self.bg = self.BG_DARK
            self.fg = self.FG_DARK
            self.bd = self.BORDER_DARK
        else:
            self.fg = self.FG_LIGHT
            self.bg = self.BG_LIGHT
            self.bd = self.BORDER_LIGHT
        self.config(bg=self.bg)
        self.text.config(bg=self.bg, fg=self.fg, highlightbackground=self.bd)
        self.text.pack(padx=2, pady=2)
        self.leave()