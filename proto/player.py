import pygame


class Player:
    def __init__(self, surface, map_view, row, column):
        self.surface = surface
        self.row = row
        self.column = column
        self.map_view = map_view

    def draw(self):
        pos = self.map_view.cell_to_screen(self.row, self.column)
        if pos:
            pygame.draw.circle(self.surface, pygame.Color(255, 0, 0), pos, 10)
            pygame.draw.circle(self.surface, pygame.Color(0, 0, 0), pos, 10, 1)
