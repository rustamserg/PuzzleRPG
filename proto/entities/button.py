import pygame
from core.entity import Entity


class Button(Entity):
    def __init__(self, pos, caption, width=100, height=40):
        Entity.__init__(self)
        self.pos = pos
        self.width = width
        self.height = height
        self.caption = caption
        self.font = pygame.font.SysFont("monospace", 18)

    def on_pos_click(self, pos):
        pass

    def draw(self, world, surface):
        label = self.font.render(self.caption, 1, (255, 255, 0))
        br = pygame.Rect(self.pos[0], self.pos[1], self.width, self.height)
        pygame.draw.rect(surface, pygame.Color(255, 255, 255), br, 1)
        lrx = self.pos[0] + (self.width - label.get_width())/2
        lry = self.pos[1] + (self.height - label.get_height())/2
        surface.blit(label, (lrx, lry))
