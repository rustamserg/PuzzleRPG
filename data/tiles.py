import os
import pygame


class Tiles:
    def __init__(self, folder):
        self.images = {}
        for entry in os.listdir(folder):
            name, ext = os.path.splitext(entry)
            if ext.lower().endswith('.png'):
                self.images[name] = pygame.image.load(os.path.join(folder, entry)).convert_alpha()
