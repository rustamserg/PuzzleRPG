import pygame
from core.entity import Entity
from data import tiles_data


class Icon(Entity):
    def __init__(self, pos, tile=None, tile_back=pygame.Color(0, 0, 0), data=None, width=32, height=32):
        Entity.__init__(self)
        self.pos = pos
        self.width = width
        self.height = height
        self.tile = tile
        self.tile_back = tile_back
        self.selected = False
        self.data = data
        self.icon_rect = pygame.Rect(self.pos[0], self.pos[1], self.width, self.height)
        self.on_click = None

    def on_pos_click(self, game, pos):
        if self.icon_rect.collidepoint(pos):
            if self.on_click and not self.selected:
                self.on_click(self, game)

    def draw(self, game, surface):
        pygame.draw.rect(surface, self.tile_back, self.icon_rect)
        if self.tile:
            surface.blit(game.tiles, (self.pos[0], self.pos[1]), tiles_data.TILES[self.tile])
        if self.selected:
            pygame.draw.rect(surface, pygame.Color(255, 0, 0), self.icon_rect, 2)
