import pygame
import globals


class Player:
    def __init__(self, surface, map_view, row, column):
        self.surface = surface
        self.row = row
        self.column = column
        self.map_view = map_view

    def on_cell_click(self, cell):
        for c in cell.get_round_bbox():
            if c.row == self.row and c.column == self.column:
                nr = pygame.Rect(0, 0, globals.WORLD_VIEW_WIDTH, globals.WORLD_VIEW_HEIGHT)
                nr = nr.move(cell.column - globals.WORLD_PLAYER_COLUMN, cell.row - globals.WORLD_PLAYER_ROW)
                if nr.top >= 0 and nr.left >= 0:
                    if globals.WORLD_HEIGHT >= nr.top + globals.WORLD_VIEW_HEIGHT:
                        if globals.WORLD_WIDTH >= nr.left + globals.WORLD_VIEW_WIDTH:
                            self.map_view.view_rect = nr
                            self.column = cell.column
                            self.row = cell.row

    def draw(self):
        pos = self.map_view.cell_to_screen(self.row, self.column)
        if pos:
            pygame.draw.circle(self.surface, pygame.Color(255, 0, 0), pos, 10)
            pygame.draw.circle(self.surface, pygame.Color(0, 0, 0), pos, 10, 1)
