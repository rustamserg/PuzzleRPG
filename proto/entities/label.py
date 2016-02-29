import pygame
from core.entity import Entity


class Label(Entity):
    def __init__(self, pos, text):
        Entity.__init__(self)
        self.pos = pos
        self.text = text
        self.font = pygame.font.SysFont("monospace", 18)

    def draw(self, world, surface):
        label = self.font.render(self.text, 1, (255, 255, 0))
        surface.blit(label, self.pos)
