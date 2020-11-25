from .global_imports import *


class KSound():
    def __init__(self, file):
        self.file = file

    def play(self):
        debug("Played sound: " + self.file)
        pygame.mixer.music.load(self.file)
        pygame.mixer.music.play()