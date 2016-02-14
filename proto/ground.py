import pygame
import math
import globals


class Ground:
    def __init__(self, hex_map, color):
        self.hex_map = hex_map
        self.color = color

    def draw(self, surface, px, py):
        points = []
        for ang in range(6):
            x = px + self.hex_map.radius * math.cos(math.radians((ang + 1) * 60))
            y = py + self.hex_map.radius * math.sin(math.radians((ang + 1) * 60))
            points.append([x + globals.WORLD_VIEW_OFFSET[0], y + globals.WORLD_VIEW_OFFSET[1]])
        pygame.draw.polygon(surface, self.color, points)
        pygame.draw.polygon(surface, pygame.Color(0, 0, 0), points, 2)
