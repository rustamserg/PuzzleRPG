import pygame
import globals
from core.layer import Layer
from entities.button import Button


class UILayer(Layer):
    def __init__(self):
        Layer.__init__(self)

    def fill_ui(self):
        self.entities.append(Button((globals.VIEW_OFFSET[0], globals.WINDOW_HEIGHT - 100), 'end turn'))
