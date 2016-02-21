import math
import pygame

import globals
from core.entity import Entity

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

    def draw(self, world, surface):
        if world.is_in_camera(self.cell):
            px, py = world.cell_to_screen(self.cell)
            points = []
            for ang in range(6):
                x = px + globals.HEX_RADIUS * math.cos(math.radians((ang + 1) * 60))
                y = py + globals.HEX_RADIUS * math.sin(math.radians((ang + 1) * 60))
                points.append([x, y])
            if self.ground_type == GroundType.GRASS:
                color = green
            elif self.ground_type == GroundType.WATER:
                color = blue
            else:
                color = black
            pygame.draw.polygon(surface, color, points)
            pygame.draw.polygon(surface, black, points, 2)
