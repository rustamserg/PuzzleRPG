import pygame
from ground import GroundType


class Player:
    def __init__(self):
        pass

    def entity_type(self):
        return self.__class__.__name__

    def on_cell_click(self, parent_cell, cell):
        if cell.entities['ground'].ground_type == GroundType.GRASS:
            for c in parent_cell.get_round_bbox():
                if c.row == cell.row and c.column == cell.column:
                    del parent_cell.entities['player']
                    cell.entities['player'] = self

    def draw(self, surface, px, py):
        pygame.draw.circle(surface, pygame.Color(255, 0, 0), (int(px), int(py)), 10)
        pygame.draw.circle(surface, pygame.Color(0, 0, 0), (int(px), int(py)), 10, 1)
