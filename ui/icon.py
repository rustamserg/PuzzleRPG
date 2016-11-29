import pygame
from core.entity import Entity
from data import tiles_data


class Icon(Entity):
    def __init__(self, pos, tile, width=32, height=32):
        Entity.__init__(self)
        self.pos = pos
        self.width = width
        self.height = height
        self.tile = tile
        self.icon_rect = pygame.Rect(self.pos[0], self.pos[1], self.width, self.height)
        self.on_click = None

    def on_pos_click(self, game, pos):
        if self.icon_rect.collidepoint(pos):
            if self.on_click:
                self.on_click(game)

    def draw(self, game, surface):
        pygame.draw.rect(surface, pygame.Color(255, 100, 0), self.icon_rect)
        surface.blit(game.tiles, (self.pos[0], self.pos[1]), tiles_data.TILES[self.tile])
