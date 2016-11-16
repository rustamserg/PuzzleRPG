import math
import pygame

import globals
from core.entity import Entity

green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
black = pygame.Color(0, 0, 0)
yellow = pygame.Color(255, 255, 0)
grey = pygame.Color(100, 100, 100)


class GroundType:
    def __init__(self):
        pass

    WATER = 1
    GRASS = 2
    SAND = 3
    STONE = 4


class Ground(Entity):
    def __init__(self, cell, ground_type):
        Entity.__init__(self)
        self.ground_type = ground_type
        self.cell = cell

    def draw(self, game, surface):
        if game.is_in_camera(self.cell):
            px, py = game.cell_to_screen(self.cell)
            points = []
            for ang in range(6):
                x = px + globals.HEX_RADIUS * math.cos(math.radians((ang + 1) * 60))
                y = py + globals.HEX_RADIUS * math.sin(math.radians((ang + 1) * 60))
                points.append([x, y])
            if self.ground_type == GroundType.GRASS:
                color = green
            elif self.ground_type == GroundType.WATER:
                color = blue
            elif self.ground_type == GroundType.SAND:
                color = yellow
            elif self.ground_type == GroundType.STONE:
                color = grey
            else:
                color = black
            pygame.draw.polygon(surface, color, points)
            pygame.draw.polygon(surface, black, points, 2)
