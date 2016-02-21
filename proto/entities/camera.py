import pygame
import globals


class Camera:
    def __init__(self, map_view):
        self.map_view = map_view

    def on_cell_click(self, parent_cell, cell):
        for c in cell.get_round_bbox():
            if c.row == parent_cell.row and c.column == parent_cell.column:
                nr = pygame.Rect(0, 0, globals.VIEW_WIDTH, globals.VIEW_HEIGHT)
                nr = nr.move(cell.column - globals.CAMERA_COLUMN, cell.row - globals.CAMERA_ROW)
                if nr.top >= 0 and nr.left >= 0:
                    if globals.WORLD_HEIGHT >= nr.top + globals.VIEW_HEIGHT:
                        if globals.WORLD_WIDTH >= nr.left + globals.VIEW_WIDTH:
                            self.map_view.view_rect = nr
                            del parent_cell.entities['camera']
                            cell.entities['camera'] = self

    def draw(self, surface, px, py):
        pass
