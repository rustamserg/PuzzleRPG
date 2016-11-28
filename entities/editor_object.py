import math
import pygame
import globals
from core.entity import Entity

red = pygame.Color(255, 0, 0)


class EditorObject(Entity):
    def __init__(self, cell):
        Entity.__init__(self)
        self.cell = cell

    def draw(self, game, surface):
        if game.is_in_camera(self.cell):
            px, py = game.cell_to_screen(self.cell)
            points = []
            for ang in range(6):
                x = px + globals.HEX_RADIUS * math.cos(math.radians((ang + 1) * 60))
                y = py + globals.HEX_RADIUS * math.sin(math.radians((ang + 1) * 60))
                points.append([x, y])
            pygame.draw.polygon(surface, red, points, 4)

    def on_cell_click(self, game, cell):
        self.cell = cell
        game.move_camera(cell)
        ui_layer = game.scene.get_layer('EditorUILayer')
        cell.ground = ui_layer.ground_type
