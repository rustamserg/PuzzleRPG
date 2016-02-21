import pygame
import math
import globals
from entity import Entity

green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
black = pygame.Color(0, 0, 0)


class GroundType:
    def __init__(self):
        pass

    WATER = 1
    GRASS = 2


class Ground(Entity):
    def __init__(self, cell, ground_type):
        Entity.__init__(self)
        self.ground_type = ground_type
        self.cell = cell

    def draw(self, map_view, surface):
        if map_view.is_in_view(self.cell):
            px, py = map_view.cell_to_screen(self.cell)
            points = []
            for ang in range(6):
                x = px + globals.HEX_RADIUS * math.cos(math.radians((ang + 1) * 60))
                y = py + globals.HEX_RADIUS * math.sin(math.radians((ang + 1) * 60))
                points.append([x + globals.VIEW_OFFSET[0], y + globals.VIEW_OFFSET[1]])
            if self.ground_type == GroundType.GRASS:
                color = blue
            elif self.ground_type == GroundType.WATER:
                color = green
            else:
                color = black
            pygame.draw.polygon(surface, color, points)
            pygame.draw.polygon(surface, black, points, 2)
