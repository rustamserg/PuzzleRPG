import pygame
import globals
from core.entity import Entity


class InventoryCell(Entity):
    def __init__(self, pos):
        Entity.__init__(self)
        self.item = None
        self.selected = False
        self.pos = pos
        self.width = globals.INVENTORY_CELL_SIZE
        self.height = globals.INVENTORY_CELL_SIZE
        self.button_rect = pygame.Rect(self.pos[0], self.pos[1], self.width, self.height)
        self.font = pygame.font.SysFont("monospace", 18)

    def on_pos_click(self, world, pos):
        if self.button_rect.collidepoint(pos):
            if self.item:
                self.selected = not self.selected

    def draw(self, world, surface):
        self.button_rect = pygame.Rect(self.pos[0], self.pos[1], self.width, self.height)
        pygame.draw.rect(surface, pygame.Color(255, 255, 255), self.button_rect, 1)
        if self.selected:
            pygame.draw.rect(surface, pygame.Color(255, 100, 0), self.button_rect)
