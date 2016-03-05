import pygame
from core.cell import Cell
from core.entity import Entity
from entities.ground import GroundType
from world import TurnType
import globals


class Player(Entity):
    def __init__(self, cell):
        Entity.__init__(self)
        self.cell = cell

    def draw(self, world, surface):
        if world.is_in_camera(self.cell):
            px, py = world.cell_to_screen(self.cell)
            dest = (px - globals.HEX_RADIUS/2, py - globals.HEX_RADIUS/2)
            area = pygame.Rect(1*32, 2*32, 32, 32)
            surface.blit(world.tiles, dest, area)

    def on_cell_click(self, world, cell):
        if world.turn == TurnType.AI:
            return

        for c in Cell.round_bbox(self.cell):
            if c == cell:
                ground_layer = world.get_layer('GroundLayer')
                if ground_layer:
                    for ent in ground_layer.entities:
                        if ent.cell == cell and ent.ground_type == GroundType.GRASS:
                            world.move_camera(cell)
                            self.cell = cell
                            world.end_turn()
                            break
